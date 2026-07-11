"""Inspect an AnnData file without loading its expression matrix into memory."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".cache" / "matplotlib")
)

import numpy as np
import scanpy as sc


def _json_value(value: Any) -> Any:
    if isinstance(value, (np.integer, np.floating)):
        return value.item()
    return str(value)


def inspect_h5ad(path: Path) -> dict[str, Any]:
    adata = sc.read_h5ad(path, backed="r")
    try:
        summary: dict[str, Any] = {
            "path": str(path),
            "file_size_bytes": path.stat().st_size,
            "cells": int(adata.n_obs),
            "genes": int(adata.n_vars),
            "matrix_backend": type(adata.X).__name__,
            "obs_columns": {
                column: {
                    "dtype": str(adata.obs[column].dtype),
                    "unique_values": int(adata.obs[column].nunique(dropna=False)),
                }
                for column in adata.obs.columns
            },
            "var_columns": {
                column: {
                    "dtype": str(adata.var[column].dtype),
                    "unique_values": int(adata.var[column].nunique(dropna=False)),
                }
                for column in adata.var.columns
            },
            "layers": sorted(adata.layers.keys()),
            "obsm": sorted(adata.obsm.keys()),
            "uns": sorted(adata.uns.keys()),
        }

        if "condition" in adata.obs:
            counts = adata.obs["condition"].value_counts()
            counts = counts[counts > 0]
            perturbed_counts = counts.drop(labels="ctrl", errors="ignore")
            summary["conditions"] = {
                "count": int(len(counts)),
                "perturbed_condition_count": int(len(perturbed_counts)),
                "control_cells": int(counts.get("ctrl", 0)),
                "perturbed_cells": int(perturbed_counts.sum()),
                "cells_per_perturbation_min": int(perturbed_counts.min()),
                "cells_per_perturbation_median": float(perturbed_counts.median()),
                "cells_per_perturbation_max": int(perturbed_counts.max()),
                "largest_conditions": {
                    str(key): int(value) for key, value in counts.head(10).items()
                },
                "smallest_conditions": {
                    str(key): int(value) for key, value in counts.tail(10).items()
                },
            }

        if "cell_type" in adata.obs:
            counts = adata.obs["cell_type"].value_counts()
            summary["cell_types"] = {
                str(key): int(value) for key, value in counts.items()
            }

        if "condition_name" in adata.obs:
            summary["condition_name_examples"] = [
                _json_value(value)
                for value in adata.obs["condition_name"].drop_duplicates().head(10)
            ]

        summary["var_index_examples"] = [str(value) for value in adata.var_names[:10]]
        if "gene_name" in adata.var:
            summary["gene_name_examples"] = [
                str(value) for value in adata.var["gene_name"].head(10)
            ]
        return summary
    finally:
        adata.file.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    summary = inspect_h5ad(args.path)
    rendered = json.dumps(summary, indent=2, sort_keys=True)
    print(rendered)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
