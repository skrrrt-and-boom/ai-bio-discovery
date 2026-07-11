# Current State

Last updated: 2026-07-11

## Mission

Learn to build AI systems that accelerate biological discovery, ultimately
contributing to the defeat of aging and disease.

## Active experiment

Experiment 001: predict cellular gene-expression responses to unseen genetic
perturbations and compare an existing model with simple baselines.

## Current stage

The reproducible CPU environment is installed and verified. The approved
Adamson dataset has been downloaded, checksum-verified, loaded in backed mode,
and inspected. The first descriptive walkthrough and plots are complete. No
predictive model has been trained yet.

## Environment

- Execution: managed browser workspace
- Operating system: Linux x86_64
- Python: 3.12.13
- Environment manager: uv
- Compute: CPU only; no dedicated GPU
- User's local computer: Apple-silicon Mac, currently unused for computation

## Verified facts

- The public repository exists and contains no credentials or private data.
- The first experiment specification is written.
- Python dependencies are declared in `pyproject.toml`.
- Exact dependency versions are frozen in `uv.lock`.
- The environment verification script, unit test, and lint check pass.
- The Adamson archive matches the expected 140,744,228-byte size and MD5.
- The processed dataset contains 68,603 cells, 5,060 genes, 24,263 controls,
  and 86 observed single-gene perturbation conditions.
- The matrix is 20.68% nonzero; a median cell has 1,077 detected genes.
- HSPA5 repression provides a clear teaching example, with lower average HSPA5
  expression in the targeted group than in controls.

## Exact next action

Explain the walkthrough to the user and confirm the central concepts. Then run
the remaining label, duplicate, imbalance, and leakage checks before defining a
train/test split.

## Recovery commands

If the browser workspace reconstructs its disposable environment, run:

```bash
make setup
make check
```

## Open questions

- Should the first published-model reproduction use GEARS directly or begin with
  a lighter implementation after the baseline pipeline is verified?
