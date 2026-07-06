# Model or analysis card: synthetic monitoring rules

## Artifact

- Prototype: `monitoring-loop-sketch`
- Artifact name: synthetic monitoring summary and alert rules
- Artifact version: default monitoring report script
- Owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This artifact is a synthetic research sketch. It is not medical
advice, not clinical decision support, and not validated for real
patients, real populations, real model monitoring, or
operational use.

## Intended use

- Design question: how drift, calibration, and governance review
  can be made visible in a minimal monitoring loop.
- Intended user: repository reader studying AI lifecycle design.
- Intended output: monthly synthetic monitoring summary and
  human-readable report.
- Intended evaluation stage: internal monitoring demonstration
  only.
- Out-of-scope use: production model monitoring, safety
  surveillance, or model update authorization.

## Inputs and outputs

- Input data: synthetic stream from `outputs/synthetic_stream.csv`.
- Required fields: month, synthetic input signals, model score,
  and delayed outcome.
- Output fields: input shift index, outcome incidence, mean
  prediction, Brier score, calibration error, alert level, and
  review hint.
- Uncertainty or confidence display: not implemented.
- Human action this should not directly trigger: any real model
  pause, update, rollback, or clinical intervention.

## Method summary

- Method type: rule-based monitoring summary.
- Baseline or comparator: baseline month and simple threshold
  rules.
- Assumptions: generated later periods contain known changes
  that a monitoring report should flag.
- Parameters or seed: default generator and threshold settings.
- Dependencies: Python standard library only.

## Evaluation summary

- Internal validation: default report generation and tests.
- External validation: none.
- Local validation: none.
- Calibration: synthetic monthly calibration error.
- Subgroup or slice evaluation: month-level slices only.
- Workflow or human-factors evaluation: none.

## Limitations

- Known failure modes: thresholds can produce alerts without
  root-cause explanation.
- Data limitations: no real live pipeline, delayed labels, or
  operational noise.
- Metric limitations: monitoring metrics are demonstrations and
  not operating policy.
- Generalization limits: applies only to the generated stream.
- Interpretability limits: alert reasons are descriptive, not
  causal explanations.

## Monitoring and update

- Monitoring signals: input shift, outcome incidence, prediction
  mean, Brier score, and calibration error.
- Update trigger: changes to synthetic drift scenario,
  thresholds, or report schema.
- Pause or rollback trigger: any output language implying real
  safety surveillance or deployment authority.
- Owner for review: repository maintainer.

## Evidence references

Primary citation IDs: E001, E002, E003, E009, E010, E020.
