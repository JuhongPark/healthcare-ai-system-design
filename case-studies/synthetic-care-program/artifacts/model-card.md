# Model or analysis card: synthetic safety-case outputs

## Artifact

- Prototype: `synthetic-care-program`
- Artifact name: synthetic evidence, risk, and monitoring output
- Artifact version: `SCP-001`
- Owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This artifact is a synthetic research sketch. It is not medical
advice, not clinical decision support, and not validated for real
patients, real populations, real clinical workflows, or
operational use.

## Intended use

- Design question: how model-like outputs can be documented and
  linked to evidence, monitoring, and governance artifacts.
- Intended user: repository reader studying healthcare AI
  lifecycle design.
- Intended output: synthetic reports, dashboard, monitoring
  stream, and evaluation registry.
- Intended evaluation stage: internal synthetic demonstration.
- Out-of-scope use: clinical prediction, clinical decision
  support, treatment guidance, or deployment authorization.

## Inputs and outputs

- Input data: deterministic synthetic cohort and monitoring
  stream from `run_case.py`.
- Required fields: synthetic severity, comorbidity, treatment,
  outcome, negative control, risk score, month, acuity, alert.
- Output fields: target trial specification, evidence report,
  dashboard, audit log, monitoring report, and evaluation
  registry.
- Uncertainty or confidence display: not modeled beyond
  safety-case limitations.
- Human action this should not directly trigger: any clinical,
  regulatory, deployment, or operational decision.

## Method summary

- Method type: deterministic synthetic lifecycle generator.
- Baseline or comparator: explicit missing-evidence and
  non-use boundaries.
- Assumptions: outputs are traceability artifacts, not clinical
  evidence.
- Parameters or seed: case ID `SCP-001`.
- Dependencies: Python standard library only.

## Evaluation summary

- Internal validation: generated outputs and tests.
- External validation: none.
- Local validation: none.
- Calibration: synthetic monitoring gap only.
- Subgroup or slice evaluation: month and risk-band slices only.
- Workflow or human-factors evaluation: none.

## Limitations

- Known failure modes: outputs may look more realistic than the
  synthetic evidence supports.
- Data limitations: no real patient data or local validation.
- Metric limitations: monitoring metrics are not operating
  policy.
- Generalization limits: applies only to the generated case.
- Interpretability limits: synthetic risk factors are not real
  clinical explanations.

## Monitoring and update

- Monitoring signals: shift index, calibration gap, alert rate,
  negative-control signal, and missing-evidence checks.
- Update trigger: changes to case logic or generated artifacts.
- Pause or rollback trigger: any language implying real clinical
  use or deployment authorization.
- Owner for review: repository maintainer.

## Evidence references

Primary citation IDs: E001, E002, E003, E020, E027.
