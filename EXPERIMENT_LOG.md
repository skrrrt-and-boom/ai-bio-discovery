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

## DATA-RUN001 — Adamson acquisition and metadata inspection

- Date: 2026-07-11
- Question: Is the approved Adamson archive authentic, readable, and suitable
  for a CPU-first unseen-intervention experiment?
- Source: Harvard Dataverse file `6154417`, derived from GEO `GSE90546`.
- Archive: 140,744,228 bytes; MD5
  `0bde631bae60ee8c105991ff0e0d4a20`; ZIP test passed.
- Procedure: extracted a disposable working copy under `/tmp`, opened the H5AD
  in backed mode, and inspected dimensions, labels, controls, and storage type.
- Result: 68,603 cells × 5,060 genes; 24,263 control cells; 44,340 perturbed
  cells; 86 observed single-gene conditions; 185–1,267 cells per intervention.
- Data issue caught: persistent-workspace extraction truncated the 607 MB H5AD;
  the intact verified ZIP was instead extracted under `/tmp` and read correctly.
- Modeling performed: none.
- Next action: create a plain-language data walkthrough and quality report.

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
