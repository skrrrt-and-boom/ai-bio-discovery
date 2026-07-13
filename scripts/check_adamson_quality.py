"""Check Adamson labels, duplicates, imbalance, and leakage risks.

This script is descriptive only. It does not create a split or fit a model.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np
import scanpy as sc
from scipy import sparse


def _matrix_block(adata: sc.AnnData, start: int, end: int):
    block = adata.X[start:end]
    if hasattr(block, "to_memory"):
        block = block.to_memory()
    return block


def _row_hashes(block) -> list[str]:
    matrix = sparse.csr_matrix(block)
    hashes: list[str] = []
    for row in range(matrix.shape[0]):
        start, end = matrix.indptr[row], matrix.indptr[row + 1]
        digest = hashlib.blake2b(digest_size=16)
        digest.update(matrix.indices[start:end].astype(np.int64).tobytes())
        digest.update(matrix.data[start:end].astype(np.float64).tobytes())
        hashes.append(digest.hexdigest())
    return hashes


def check_quality(path: Path, chunk_size: int = 2048) -> dict:
    adata = sc.read_h5ad(path, backed="r")
    try:
        if "condition" not in adata.obs:
            raise ValueError("Required obs column 'condition' is missing")

        conditions = adata.obs["condition"].astype("string")
        missing_conditions = int(conditions.isna().sum())
        condition_counts = conditions.value_counts(dropna=False)
        non_control = condition_counts.drop(labels="ctrl", errors="ignore")

        malformed = sorted(
            str(value)
            for value in conditions.dropna().unique()
            if value != "ctrl" and not str(value).endswith("+ctrl")
        )
        targets = sorted(
            {
                str(value).removesuffix("+ctrl")
                for value in conditions.dropna().unique()
                if value != "ctrl" and str(value).endswith("+ctrl")
            }
        )

        gene_names = (
            adata.var["gene_name"].astype("string")
            if "gene_name" in adata.var
            else adata.var_names.astype("string")
        )
        gene_set = set(gene_names.dropna().astype(str))
        targets_missing_from_panel = sorted(set(targets) - gene_set)

        obs_index_duplicates = int(adata.obs_names.duplicated().sum())
        var_index_duplicates = int(adata.var_names.duplicated().sum())
        gene_name_duplicates = int(gene_names.duplicated().sum())

        row_hash_counts: Counter[str] = Counter()
        for start in range(0, adata.n_obs, chunk_size):
            end = min(start + chunk_size, adata.n_obs)
            row_hash_counts.update(_row_hashes(_matrix_block(adata, start, end)))
        duplicate_expression_groups = sum(count > 1 for count in row_hash_counts.values())
        cells_in_duplicate_expression_groups = sum(
            count for count in row_hash_counts.values() if count > 1
        )
        excess_duplicate_expression_rows = sum(
            count - 1 for count in row_hash_counts.values() if count > 1
        )

        perturbation_counts = non_control.astype(int)
        imbalance = {
            "minimum_cells": int(perturbation_counts.min()),
            "median_cells": float(perturbation_counts.median()),
            "maximum_cells": int(perturbation_counts.max()),
            "max_to_min_ratio": float(
                perturbation_counts.max() / perturbation_counts.min()
            ),
            "conditions_below_250_cells": int((perturbation_counts < 250).sum()),
            "conditions_above_1000_cells": int((perturbation_counts > 1000).sum()),
        }

        split_like_columns = sorted(
            column
            for column in adata.obs.columns
            if any(token in column.lower() for token in ("split", "train", "test", "val"))
        )
        condition_encoding_columns = []
        for column in adata.obs.columns:
            if column == "condition":
                continue
            values = adata.obs[column]
            if values.isna().all():
                continue
            table = adata.obs.groupby("condition", observed=True)[column].nunique(
                dropna=False
            )
            if len(table) and int(table.max()) == 1:
                condition_encoding_columns.append(column)

        return {
            "dataset": {"cells": int(adata.n_obs), "genes": int(adata.n_vars)},
            "labels": {
                "missing_condition_labels": missing_conditions,
                "unique_conditions_including_control": int(len(condition_counts)),
                "perturbation_conditions": int(len(perturbation_counts)),
                "malformed_condition_labels": malformed,
                "targets_missing_from_expression_panel": targets_missing_from_panel,
            },
            "duplicates": {
                "duplicate_cell_ids": obs_index_duplicates,
                "duplicate_gene_ids": var_index_duplicates,
                "duplicate_gene_names": gene_name_duplicates,
                "duplicate_expression_groups": duplicate_expression_groups,
                "cells_in_duplicate_expression_groups": cells_in_duplicate_expression_groups,
                "excess_duplicate_expression_rows": excess_duplicate_expression_rows,
                "note": "Expression-row hashes detect exact equality in the processed matrix; identical rows are not automatically the same biological cell.",
            },
            "imbalance": imbalance,
            "leakage": {
                "split_like_obs_columns": split_like_columns,
                "columns_constant_within_each_condition": sorted(
                    condition_encoding_columns
                ),
                "required_rule": "Split by perturbation condition, never by individual cell. Remove condition-derived metadata from model inputs.",
                "reason": "A random cell split would place replicate cells from the same intervention in both training and evaluation.",
            },
        }
    finally:
        adata.file.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--chunk-size", type=int, default=2048)
    args = parser.parse_args()

    summary = check_quality(args.path, chunk_size=args.chunk_size)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
