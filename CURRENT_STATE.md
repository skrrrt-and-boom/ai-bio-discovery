# Current State

Last updated: 2026-07-11

## Mission

Learn to build AI systems that accelerate biological discovery, ultimately
contributing to the defeat of aging and disease.

## Active experiment

Experiment 001: predict cellular gene-expression responses to unseen genetic
perturbations and compare an existing model with simple baselines.

## Current stage

The reproducible CPU environment is installed and verified. No biological
dataset has been downloaded and no scientific experiment has been run yet.

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

## Exact next action

Select the smallest appropriate public perturbation dataset, document its
meaning and provenance, and load only a CPU-manageable subset before modeling.

## Recovery commands

If the browser workspace reconstructs its disposable environment, run:

```bash
make setup
make check
```

## Open questions

- Which small perturbation dataset is the safest first dataset for the available
  CPU and storage resources?
- Should the first published-model reproduction use GEARS directly or begin with
  a lighter implementation after the baseline pipeline is verified?
