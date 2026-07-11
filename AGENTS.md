# Instructions for AI collaborators

This repository is the source of truth for the AI for Biological Discovery
project. Do not rely on conversation memory alone.

## Read at the beginning of a work session

Read these files in order:

1. `CURRENT_STATE.md`
2. `ROADMAP.md`
3. `DECISIONS.md`
4. `EXPERIMENT_LOG.md`
5. The README inside the active experiment directory

Read the longer strategic documents only when a decision requires them.

## Working rules

- Explain simply before going technically deep.
- Separate fact, inference, and hypothesis.
- Use primary scientific sources for important scientific claims.
- Never invent citations, data, metrics, or experimental results.
- Start with simple baselines before sophisticated models.
- Keep training and evaluation data separate.
- Treat `data/raw/` as immutable.
- Never commit secrets, private health information, or large datasets.
- Do not interpret a younger-looking biomarker as proof of rejuvenation.
- Do not recommend personal biological experimentation.
- Preserve failed experiments and report them honestly.

## End-of-session protocol

Before finishing substantive work:

1. Update `CURRENT_STATE.md` with the exact next action.
2. Update `ROADMAP.md` if a milestone changed.
3. Add a decision to `DECISIONS.md` only when a consequential choice was made.
4. Update `EXPERIMENT_LOG.md` only when code or an analysis was actually run.
5. Run `make check` or the narrower relevant checks.
6. Publish the verified changes to GitHub when authorized.
