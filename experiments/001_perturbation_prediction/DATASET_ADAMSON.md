# Adamson dataset record

## Why this dataset was selected

The Adamson Perturb-seq dataset is the smallest complete preprocessed archive
supported by the official GEARS loader. It is large enough to hold out entire
gene interventions for testing, but narrow enough for a first CPU-based project.

The original experiment studied how human K562 cells respond when genes involved
in protein processing and cellular stress are repressed with CRISPR interference.

## Provenance

- Original study: Adamson et al., *Cell* (2016)
- Original GEO record: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90546
- GEARS implementation: https://github.com/snap-stanford/GEARS
- Processed-data collection: https://doi.org/10.7910/DVN/Q2ZV3E
- Dataverse file ID: `6154417`
- Archive name: `adamson.zip`
- License of processed-data collection: CC0 1.0

## Integrity record

- Downloaded size: `140744228` bytes
- Expected and observed MD5: `0bde631bae60ee8c105991ff0e0d4a20`
- ZIP integrity test: passed
- Uncompressed H5AD size: `606502516` bytes
- Gene-information CSV size: `34758919` bytes

The archive is stored at:

`data/raw/adamson_gears/archive/adamson.zip`

Raw data are ignored by Git and must not be uploaded to the public repository.
Because the browser workspace remaps large persistent files, the verified archive
is extracted into `/tmp/ai-bio-discovery/adamson-working` for analysis.

## What is in the processed dataset

| Item | Observed value | Plain meaning |
|---|---:|---|
| Cells | 68,603 | Separate measured cells; rows of the matrix |
| Genes | 5,060 | Gene-expression features; columns of the matrix |
| Control cells | 24,263 | Cells without a targeted gene repression |
| Perturbed cells | 44,340 | Cells assigned to a targeted gene repression |
| Perturbed conditions | 86 | Different genes individually targeted |
| Cells per intervention | 185–1,267 | Replicate cells available for each intervention |
| Median cells per intervention | 504.5 | Typical number of replicate cells |
| Cell types | 1 | A processed K562 cell population |

All 86 processed perturbation conditions contain one targeted gene plus the
`ctrl` placeholder. This version is therefore suited to unseen **single-gene**
prediction, not combinatorial prediction.

## Data dictionary

### Expression matrix `X`

- Shape: 68,603 cells × 5,060 genes.
- Stored sparsely, so zero measurements do not consume full dense-matrix space.
- Stored as `float32`.
- Sampled nonzero values are non-integer, so this is processed expression rather
  than raw molecule counts.
- The precise normalization transformation must be confirmed from the upstream
  preprocessing before numeric magnitudes are interpreted biologically.

### Per-cell fields in `obs`

- `condition`: intervention label, such as `HSPA5+ctrl`, or `ctrl` for control.
- `condition_name`: expanded internal label including cell type and dose.
- `control`: `1` for control cells and `0` for perturbed cells.
- `dose_val`: legacy condition encoding; `1` for controls and `1+1` for the
  processed single-gene perturbations.
- `cell_type`: labeled `K562(?)` for all processed cells.

### Per-gene fields in `var`

- The row index contains Ensembl gene identifiers.
- `gene_name` contains human-readable gene symbols.

### Precomputed metadata in `uns`

The file includes upstream differential-expression and non-dropout gene lists.
These may help reproduce GEARS, but they must not be allowed to leak information
from held-out test interventions into model training.

## What this dataset does not prove

- It is a cancer-derived cell line, not an adult human tissue or whole person.
- It studies cellular stress, not aging directly.
- A transcriptional prediction is not evidence that an intervention is safe or
  therapeutic.
- Accurate prediction on this dataset would establish technical competence, not
  rejuvenation.

## Next analysis step

Create a beginner-friendly data walkthrough and quality report before modeling:

1. Explain control, perturbation, gene expression, cell, and replicate.
2. Plot cell counts per intervention.
3. Compare average expression for one intervention with controls.
4. Check missing labels, duplicated cells, sparsity, and condition imbalance.
5. Define the train/validation/test split by entire interventions.

