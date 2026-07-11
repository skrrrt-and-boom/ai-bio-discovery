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

The exact dataset and published model will be locked only after environment and
resource checks. The current candidate is a small, documented subset of the
Norman perturbation data and the published GEARS implementation.

## Stages

- [x] Environment verified.
- [ ] Dataset identity and checksum recorded.
- [ ] Data dictionary written.
- [ ] Exploratory plots created.
- [ ] Evaluation split frozen.
- [ ] Baselines evaluated.
- [ ] Published model reproduced.
- [ ] Failure analysis completed.
- [ ] Short report written.

## Non-claims

Success on this benchmark would not prove rejuvenation, therapeutic usefulness,
or reliable prediction in humans. It would establish practical competence and
reveal the next bottleneck.
