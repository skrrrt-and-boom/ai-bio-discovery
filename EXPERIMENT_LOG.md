# Experiment Log

No scientific experiments have been run yet.

## SETUP-RUN001 — Scientific Python environment verification

- Date: 2026-07-11
- Question: Can the locked CPU environment run the core data and modeling stack?
- Inputs: a synthetic four-row regression problem and a synthetic 2×2 AnnData
  object; no biological data.
- Procedure: synchronized dependencies with uv, ran the environment script,
  unit test, and Ruff lint check.
- Result: passed.
- Verified packages: NumPy 2.4.6, pandas 3.0.3, SciPy 1.18.0,
  scikit-learn 1.9.0, AnnData 0.13.1, and Scanpy 1.12.1.
- Scientific interpretation: none; this was an infrastructure test.
- Next action: select and document the first small public perturbation dataset.

Use one entry for every meaningful run, including failed runs.

## Entry template

### Run ID: EXP001-RUN000

- Date and time:
- Git commit:
- Question:
- Dataset and version:
- Data split:
- Code or notebook:
- Parameters:
- Expected result:
- Actual result:
- Metrics:
- Files produced:
- Problems or anomalies:
- Interpretation:
- Next action:
