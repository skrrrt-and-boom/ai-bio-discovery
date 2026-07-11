"""Create descriptive Adamson dataset plots without fitting a model."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".cache" / "matplotlib")
)

import matplotlib.pyplot as plt
import numpy as np
import scanpy as sc
from scipy import sparse


def _matrix_block(adata: sc.AnnData, start: int, end: int):
    block = adata.X[start:end]
    if hasattr(block, "to_memory"):
        block = block.to_memory()
    return block


def _row_nonzero_counts(block) -> np.ndarray:
    if sparse.issparse(block):
        return np.asarray(block.getnnz(axis=1)).ravel()
    return np.count_nonzero(block, axis=1)


def _column_sum(block) -> np.ndarray:
    return np.asarray(block.sum(axis=0)).ravel()


def _column_values(block, column: int) -> np.ndarray:
    values = block[:, column]
    if sparse.issparse(values):
        return values.toarray().ravel()
    return np.asarray(values).ravel()


def create_walkthrough(path: Path, output_dir: Path, chunk_size: int = 2048) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    adata = sc.read_h5ad(path, backed="r")

    try:
        conditions = adata.obs["condition"].astype(str).to_numpy()
        counts = adata.obs["condition"].value_counts()
        counts = counts[counts > 0]
        perturbation_counts = counts.drop(labels="ctrl", errors="ignore")

        gene_names = adata.var["gene_name"].astype(str).to_numpy()
        target_matches = np.flatnonzero(gene_names == "HSPA5")
        if len(target_matches) != 1:
            raise ValueError(f"Expected one HSPA5 gene, found {len(target_matches)}")
        hspa5_index = int(target_matches[0])

        detected_genes = np.empty(adata.n_obs, dtype=np.int32)
        total_nonzero = 0
        control_sum = np.zeros(adata.n_vars, dtype=np.float64)
        hspa5_sum = np.zeros(adata.n_vars, dtype=np.float64)
        control_n = 0
        hspa5_n = 0
        control_hspa5_values: list[np.ndarray] = []
        perturbed_hspa5_values: list[np.ndarray] = []

        for start in range(0, adata.n_obs, chunk_size):
            end = min(start + chunk_size, adata.n_obs)
            block = _matrix_block(adata, start, end)
            detected = _row_nonzero_counts(block)
            detected_genes[start:end] = detected
            total_nonzero += int(detected.sum())

            condition_chunk = conditions[start:end]
            control_mask = condition_chunk == "ctrl"
            hspa5_mask = condition_chunk == "HSPA5+ctrl"

            if control_mask.any():
                control_block = block[control_mask]
                control_sum += _column_sum(control_block)
                control_n += int(control_mask.sum())
                control_hspa5_values.append(
                    _column_values(control_block, hspa5_index)
                )

            if hspa5_mask.any():
                hspa5_block = block[hspa5_mask]
                hspa5_sum += _column_sum(hspa5_block)
                hspa5_n += int(hspa5_mask.sum())
                perturbed_hspa5_values.append(
                    _column_values(hspa5_block, hspa5_index)
                )

        control_mean = control_sum / control_n
        hspa5_mean = hspa5_sum / hspa5_n
        expression_delta = hspa5_mean - control_mean
        top_changed = np.argsort(np.abs(expression_delta))[-10:][::-1]
        control_target = np.concatenate(control_hspa5_values)
        perturbed_target = np.concatenate(perturbed_hspa5_values)

        plt.style.use("seaborn-v0_8-whitegrid")

        fig, ax = plt.subplots(figsize=(7, 4.5))
        labels = ["Control cells", "Perturbed cells"]
        values = [int(counts.get("ctrl", 0)), int(perturbation_counts.sum())]
        bars = ax.bar(labels, values, color=["#8da0cb", "#66c2a5"])
        ax.set_ylabel("Number of cells")
        ax.set_title("Most cells belong to a gene intervention")
        ax.bar_label(bars, labels=[f"{value:,}" for value in values], padding=4)
        ax.set_ylim(0, max(values) * 1.15)
        fig.tight_layout()
        fig.savefig(output_dir / "01_control_vs_perturbed.png", dpi=180)
        plt.close(fig)

        top_counts = perturbation_counts.sort_values().tail(15)
        fig, ax = plt.subplots(figsize=(8, 7))
        ax.barh(top_counts.index, top_counts.values, color="#66c2a5")
        ax.axvline(
            perturbation_counts.median(),
            color="#444444",
            linestyle="--",
            label=f"Median: {perturbation_counts.median():.0f}",
        )
        ax.set_xlabel("Cells measured")
        ax.set_ylabel("Gene reduced with CRISPRi")
        ax.set_title("Fifteen interventions with the most replicate cells")
        ax.legend()
        fig.tight_layout()
        fig.savefig(output_dir / "02_largest_interventions.png", dpi=180)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(8, 4.8))
        ax.hist(detected_genes, bins=50, color="#fc8d62", edgecolor="white")
        median_detected = float(np.median(detected_genes))
        ax.axvline(
            median_detected,
            color="#333333",
            linestyle="--",
            label=f"Median: {median_detected:.0f} detected genes",
        )
        ax.set_xlabel("Genes with a nonzero measurement in one cell")
        ax.set_ylabel("Number of cells")
        ax.set_title("A single cell reveals only part of the 5,060-gene panel")
        ax.legend()
        fig.tight_layout()
        fig.savefig(output_dir / "03_detected_genes_per_cell.png", dpi=180)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(7, 4.8))
        violin = ax.violinplot(
            [control_target, perturbed_target],
            positions=[1, 2],
            showmedians=True,
            showextrema=False,
        )
        for body in violin["bodies"]:
            body.set_facecolor("#8da0cb")
            body.set_alpha(0.75)
        ax.set_xticks([1, 2], ["Control", "HSPA5 reduced"])
        ax.set_ylabel("Processed HSPA5 expression")
        ax.set_title("Direct check: expression of the targeted HSPA5 gene")
        fig.tight_layout()
        fig.savefig(output_dir / "04_hspa5_target_expression.png", dpi=180)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.scatter(control_mean, hspa5_mean, s=9, alpha=0.24, color="#666666")
        lower = float(min(control_mean.min(), hspa5_mean.min()))
        upper = float(max(control_mean.max(), hspa5_mean.max()))
        ax.plot([lower, upper], [lower, upper], linestyle="--", color="#333333")
        ax.scatter(
            control_mean[top_changed],
            hspa5_mean[top_changed],
            s=28,
            color="#d95f02",
        )
        for index in top_changed:
            ax.annotate(
                gene_names[index],
                (control_mean[index], hspa5_mean[index]),
                xytext=(4, 3),
                textcoords="offset points",
                fontsize=7,
            )
        ax.set_xlabel("Average expression in control cells")
        ax.set_ylabel("Average expression after reducing HSPA5")
        ax.set_title("Reducing one gene changes a broader expression pattern")
        fig.tight_layout()
        fig.savefig(output_dir / "05_hspa5_global_response.png", dpi=180)
        plt.close(fig)

        summary = {
            "cells": int(adata.n_obs),
            "genes_in_processed_panel": int(adata.n_vars),
            "control_cells": int(control_n),
            "perturbed_cells": int(perturbation_counts.sum()),
            "perturbations": int(len(perturbation_counts)),
            "detected_genes_per_cell": {
                "min": int(detected_genes.min()),
                "median": median_detected,
                "mean": float(detected_genes.mean()),
                "max": int(detected_genes.max()),
            },
            "matrix_nonzero_fraction": float(
                total_nonzero / (adata.n_obs * adata.n_vars)
            ),
            "hspa5": {
                "control_cells": int(control_n),
                "perturbed_cells": int(hspa5_n),
                "target_expression_control_mean": float(control_target.mean()),
                "target_expression_perturbed_mean": float(
                    perturbed_target.mean()
                ),
                "target_expression_control_zero_fraction": float(
                    np.mean(control_target == 0)
                ),
                "target_expression_perturbed_zero_fraction": float(
                    np.mean(perturbed_target == 0)
                ),
                "largest_absolute_mean_changes": [
                    {
                        "gene": str(gene_names[index]),
                        "control_mean": float(control_mean[index]),
                        "perturbed_mean": float(hspa5_mean[index]),
                        "difference": float(expression_delta[index]),
                    }
                    for index in top_changed
                ],
            },
        }

        (output_dir / "walkthrough_summary.json").write_text(
            json.dumps(summary, indent=2) + "\n", encoding="utf-8"
        )
        return summary
    finally:
        adata.file.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    summary = create_walkthrough(args.path, args.output_dir)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

