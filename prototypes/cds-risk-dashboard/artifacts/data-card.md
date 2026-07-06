# Data card: synthetic CDS patient-like records

## Artifact

- Prototype: `cds-risk-dashboard`
- Dataset name: synthetic patient-like dashboard records
- Dataset version: default generator output
- Data owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This dataset is synthetic-only. It contains no real patient data
and no protected health information. It is not medical advice,
not clinical decision support, and not evidence about real
patients, real populations, or real clinical workflows.

## Motivation

- Design question: how risk, uncertainty, limitations, override
  capture, and audit review can share one workflow surface.
- Intended use: populate a static dashboard sketch for interface
  and workflow reasoning.
- Out-of-scope use: diagnosis, triage, treatment advice,
  clinician performance assessment, or deployment testing.
- Decision this dataset should not support: any care decision or
  operational decision.

## Composition

- Unit of observation: synthetic patient-like dashboard row.
- Row count: 6 rows in the committed default example.
- Key fields: synthetic patient identifier, age band, clinical
  signals, risk score, confidence band, explanation factors,
  limitations, and audit fields.
- Outcome or label: generated synthetic risk and outcome-like
  fields for display only.
- Time horizon: illustrative dashboard horizon.
- Subgroups or slices: none large enough for meaningful
  subgroup evaluation.

## Generation

- Source: `generate_dashboard.py`.
- Generation method: deterministic synthetic records embedded in
  the dashboard generator.
- Random seed or data version: default script data.
- Known encoded assumptions: selected variables are simplified
  to exercise the interface layout.
- Known omitted factors: real clinical context, missingness,
  competing priorities, staffing constraints, and site-specific
  workflows.

## Quality and limitations

- Missingness pattern: simplified and not representative.
- Measurement noise: synthetic values only.
- Selection effects: hand-sized example set.
- Proxy-label risk: not evaluated in the current prototype.
- Known mismatch with real-world data: no EHR extraction,
  clinical adjudication, local validation, or workflow study.

## Permitted use

- Permitted: static interface review, workflow hypothesis
  generation, and audit-field design.
- Not permitted: clinical decision support, medical advice,
  local validation, or real patient risk estimation.
- Regeneration instructions: run
  `python prototypes/cds-risk-dashboard/generate_dashboard.py`.

## Linked artifacts

- Model or analysis card: none in current prototype.
- Interface contract: `artifacts/interface-contract.md`.
- Evaluation registry entry: `artifacts/evaluation-registry.csv`.
- Governance gate review: `artifacts/governance-gate-review.md`.

## Evidence references

Primary citation IDs: E004, E007, E019, E027.
