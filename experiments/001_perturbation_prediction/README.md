# Experiment 001 — Cellular Perturbation Prediction

## Research question

Can an existing biological prediction model outperform simple baselines when
predicting the gene-expression response to a genetic perturbation excluded from
its training examples?

## Why this experiment comes first

It is small enough to reproduce with public data, but it contains the essential
parts of a serious biological discovery system: interventions, measurements,
generalization, uncertainty, and experimental comparison.

## Planned comparison

1. Predict no change from the control condition.
2. Predict an average or similar known response.
3. Fit a simple statistical model.
4. Reproduce one existing perturbation-prediction model.

The selected dataset is the GEARS-preprocessed Adamson Perturb-seq dataset. It
contains 86 observed single-gene perturbation conditions in one processed K562
cell population. The published-model choice remains open until the baseline
pipeline and resource requirements are verified.

## Stages

- [x] Environment verified.
- [x] Dataset identity and checksum recorded.
- [x] Data dictionary written.
- [x] Exploratory plots created.
- [ ] Data-quality checks completed and reviewed.
- [ ] Evaluation split frozen.
- [ ] Baselines evaluated.
- [ ] Published model reproduced.
- [ ] Failure analysis completed.
- [ ] Short report written.

The command `make quality-adamson` checks labels, exact duplicate expression
rows, intervention imbalance, and metadata leakage risks. It must be run and
reviewed before the evaluation split is created.

## Non-claims

Success on this benchmark would not prove rejuvenation, therapeutic usefulness,
or reliable prediction in humans. It would establish practical competence and
reveal the next bottleneck.
