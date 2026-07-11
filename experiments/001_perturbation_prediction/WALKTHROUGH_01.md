# Walkthrough 01 — What the Adamson matrix represents

## The central picture

Each row represents one measured cell. Each column represents one selected gene.
The value at their intersection is processed gene expression: an estimate of
how actively that gene's RNA was observed in that cell.

Each cell also has a condition label:

- `ctrl`: no targeted gene repression;
- `HSPA5+ctrl`: HSPA5 was reduced with CRISPR interference;
- other `GENE+ctrl` labels: that named gene was reduced.

The `+ctrl` part is a GEARS condition-format placeholder. These are single-gene
conditions, not two-gene combinations.

## Why the processed matrix has 5,060 genes

The official Adamson preprocessing notebook begins with 69,249 cells and 16,528
measured genes. It then:

1. normalizes total expression per cell;
2. applies a `log1p` transformation;
3. identifies the 5,000 most variable genes;
4. adds targeted perturbation genes not already present among those 5,000;
5. keeps the union, producing 5,060 gene features.

This is feature selection. It does **not** imply that humans have only 5,060
genes.

Official preprocessing source:
https://github.com/yhr91/GEARS_misc/blob/f88211870dfa89c38a2eedbd69ca1abd28a25f3c/data/preprocessing/Adamson2016.ipynb

## What “most variable” means

A gene is useful for this experiment when its measured expression varies across
cells and conditions. A gene that is nearly always zero or nearly constant adds
little information for distinguishing cellular responses, so the model authors
reduced the feature set for tractability and signal quality.

Highly variable does not mean biologically most important. It means most
informative under this dataset's statistical selection rule.

## Descriptive findings

### Dataset composition

- 68,603 processed cells in total.
- 24,263 control cells (35.4%).
- 44,340 perturbed cells (64.6%).
- 86 observed single-gene intervention conditions.
- Median 504.5 cells per intervention.

### Sparse measurements

- Median detected genes per cell: 1,077 of the 5,060-gene panel.
- Mean detected genes per cell: 1,046.
- Range: 169–1,788 detected genes.
- Nonzero fraction of the full matrix: 20.68%.
- Zero fraction: 79.32%.

A zero can mean that the gene was not active enough to detect, that the assay
missed its RNA, or both. It must not automatically be read as “this gene is
biologically absent.”

### One teaching example: HSPA5

The HSPA5 intervention contains 1,002 cells.

- Mean processed HSPA5 expression in controls: 1.624.
- Mean after targeting HSPA5: 0.949.
- Fraction with a zero HSPA5 measurement in controls: 10.0%.
- Fraction with a zero after targeting HSPA5: 27.8%.

This is consistent with successful repression at the group level. It is not a
claim that every cell was edited equally.

Reducing HSPA5 also coincides with changes in other measured genes. The largest
absolute average differences include HSP90B1, PDIA3, PDIA6, SDF2L1, MANF,
PDIA4, HBZ, PPIB, NUCB2, and DERL3. These are descriptive differences. We have
not established mechanisms or fitted a predictive model.

## Why many cells are necessary

Single-cell measurements are noisy and cells genuinely differ from one another.
Hundreds of replicate cells let us estimate a distribution instead of trusting
one possibly misleading cell.

## Plot reproduction

Run:

```bash
make walkthrough-adamson
```

This creates five local plots under `artifacts/data_walkthrough/`:

1. control versus perturbed cell counts;
2. interventions with the most replicate cells;
3. detected genes per cell;
4. HSPA5 expression in control versus HSPA5-targeted cells;
5. control versus HSPA5-targeted average expression across all 5,060 genes.

## What has not happened

- No train, validation, or test split has been created.
- No model or baseline has been fitted.
- No intervention has been scored as predictable or unpredictable.
- No therapeutic or aging conclusion has been drawn.

