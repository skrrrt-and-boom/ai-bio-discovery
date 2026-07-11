# Roadmap

## Long-term direction

Develop the ability to build AI systems that help discover and verify biological
interventions, ultimately contributing to the defeat of aging and disease.

## Current stage

Learn the real workflow through one reproducible public-data experiment.

## Experiment 001

**Question:** Can a model predict how cellular gene expression changes after an
unseen genetic perturbation better than deliberately simple baselines?

### Milestones

- [x] Create the ChatGPT research Project.
- [x] Attach the three strategic source files.
- [x] Create the technical workspace skeleton.
- [x] Identify the user's operating system and browser execution environment.
- [ ] Install one reproducible Python environment.
- [ ] Learn the minimum biology and data vocabulary needed to inspect the data.
- [ ] Load a small public perturbation dataset.
- [ ] Produce a data-quality report and simple plots.
- [ ] Implement trivial and statistical baselines.
- [ ] Reproduce one published model result.
- [ ] Compare models on held-out perturbations.
- [ ] Analyze important failures.
- [ ] Write a two-page result and obtain researcher feedback.

## Success criteria

Experiment 001 is complete when:

1. Another person can reproduce the result from the repository.
2. The comparison includes at least two simple baselines.
3. Evaluation uses data not used to fit the model.
4. We can explain at least three meaningful failure cases.
5. We can state a justified next experiment connected to aging biology.

## Exact next action

Select dependencies compatible with the managed browser workspace's Python
3.12 CPU environment. Use that environment for data inspection and baselines;
use a separate GPU environment later only if the published-model reproduction
requires it. Do not install Python tools directly on the user's Mac yet.
