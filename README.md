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
- Python project environment: not created yet.
- Git repository: not initialized yet.
- Dataset: not downloaded yet.
- Local computer: macOS on Apple silicon; no local installation is currently
  required.
