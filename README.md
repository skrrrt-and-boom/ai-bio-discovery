# AI for Biological Discovery

This is the active technical workspace for learning and testing whether AI can
improve biological discovery, beginning with cellular perturbation prediction
and later moving toward aging-relevant questions.

## Current objective

Complete Experiment 001: compare simple baselines with an existing model for
predicting how cells respond to unseen genetic perturbations.

This first experiment is an entry ramp, not a claim that we can reverse aging.

## Files with distinct jobs

- `ROADMAP.md`: current objective and next actions.
- `DECISIONS.md`: important choices and why they were made.
- `EXPERIMENT_LOG.md`: what was actually run and what happened.
- `CURRENT_STATE.md`: the short handoff that lets a future session resume.
- `AGENTS.md`: mandatory working instructions for AI collaborators.
- `experiments/001_perturbation_prediction/README.md`: the specification for
  the first experiment.

## Rules that prevent avoidable mistakes

1. Never edit files in `data/raw/` after downloading them.
2. Never commit passwords, tokens, private health data, or `.env` files.
3. Do not add large datasets or generated model files to Git.
4. Record failed experiments; do not delete or disguise them.
5. Establish a simple baseline before using a sophisticated model.
6. Keep training data separate from evaluation data.
7. Do not interpret a younger-looking biomarker as proof of rejuvenation.
8. Do not perform personal biological experiments based on computational work.

## Setup status

- ChatGPT Project: created.
- Background sources: attached.
- Execution environment: managed browser workspace running Linux x86_64.
- Available Python: 3.12.13.
- Available Git: 2.51.1.
- Available environment manager: uv 0.9.25.
- Dedicated GPU: not available in the browser workspace.
- Python project environment: locked in `uv.lock` and verified.
- Git repository: published publicly at
  `https://github.com/skrrrt-and-boom/ai-bio-discovery`.
- Dataset: Adamson archive downloaded and checksum-verified in the managed
  workspace; raw data remain intentionally excluded from Git.
- Descriptive walkthrough: complete.
- Data-quality command: `make quality-adamson` is implemented and awaits a run
  in the workspace containing the raw archive.
- Local computer: macOS on Apple silicon; no local installation is currently
  required.

## Recreate and verify the environment

The Python environment is disposable and is not committed. The lockfile is the
reproducible record. In the browser workspace, run:

```bash
make setup
make check
```

## Resume this project in a new ChatGPT chat

Use this prompt:

```text
Resume my AI for Biological Discovery project using the GitHub app.
Repository: https://github.com/skrrrt-and-boom/ai-bio-discovery
Read AGENTS.md and CURRENT_STATE.md first, then the files they direct you to.
Tell me the current state and exact next action before making changes.
```
