# Data card: synthetic care program

## Artifact

- Prototype: `synthetic-care-program`
- Dataset name: synthetic care program cohort and monitoring
  stream
- Dataset version: `SCP-001`
- Data owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This dataset is synthetic-only. It contains no real patient data
and no protected health information. It is not medical advice,
not clinical decision support, and not evidence about real
patients, real populations, or real clinical workflows.

## Motivation

- Design question: how evidence design, workflow display,
  monitoring, and evaluation artifacts can be linked in one
  executable synthetic healthcare AI lifecycle.
- Intended use: demonstrate safety-case traceability.
- Out-of-scope use: clinical validation, treatment guidance,
  model safety claims, or deployment authorization.
- Decision this dataset should not support: any real clinical or
  operational decision.

## Composition

- Unit of observation: synthetic subject rows and synthetic
  encounter-like monitoring rows.
- Key fields: synthetic severity, comorbidity, treatment,
  outcome, negative control, risk score, month, acuity, alert.
- Outcome or label: generated binary synthetic outcomes.
- Time horizon: synthetic index period and six monitoring
  months.
- Subgroups or slices: month slices and synthetic risk bands.

## Generation

- Source: `run_case.py`.
- Generation method: deterministic standard-library generator.
- Random seed or data version: deterministic formulas under
  case ID `SCP-001`.
- Known encoded assumptions: later monitoring periods include
  higher acuity and outcome drift.
- Known omitted factors: real data provenance, missingness,
  label adjudication, site effects, clinical workflow, and
  production feedback loops.

## Quality and limitations

- Missingness pattern: no realistic missingness.
- Measurement noise: simplified synthetic values.
- Selection effects: generated case only.
- Proxy-label risk: intentionally represented as a future
  safety-case warning, not real inequity evidence.
- Known mismatch with real-world data: no real RWD, EHR,
  claims, registry, hospital, or patient data.

## Permitted use

- Permitted: local safety-case demonstration and automated
  tests.
- Not permitted: medical advice, clinical decision support,
  clinical validation, or real-world evidence claims.
- Regeneration instructions:
  `python case-studies/synthetic-care-program/run_case.py`.

## Linked artifacts

- Model or analysis card: `artifacts/model-card.md`.
- Interface contract: `artifacts/interface-contract.md`.
- Evaluation registry entry: `outputs/evaluation_registry.csv`.
- Governance gate review: `artifacts/governance-gate-review.md`.

## Evidence references

Primary citation IDs: E001, E007, E019, E027.
