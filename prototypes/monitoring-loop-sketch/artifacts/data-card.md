# Data card: synthetic monitoring stream

## Artifact

- Prototype: `monitoring-loop-sketch`
- Dataset name: synthetic model-output monitoring stream
- Dataset version: default generator output
- Data owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This dataset is synthetic-only. It contains no real patient data
and no protected health information. It is not medical advice,
not clinical decision support, and not evidence about real
patients, real populations, or real model performance.

## Motivation

- Design question: how a small monitoring loop can connect
  input drift, outcome incidence, calibration, alert level, and
  governance review.
- Intended use: demonstrate monitoring and escalation surfaces
  on a stream where drift is known.
- Out-of-scope use: real-world performance monitoring, clinical
  model validation, safety surveillance, or operational
  incident management.
- Decision this dataset should not support: deployment, pause,
  update, rollback, or any clinical action for a real system.

## Composition

- Unit of observation: synthetic encounter-like model-output
  row.
- Row count: 240 rows in the committed default example.
- Key fields: month bucket, synthetic input signals, model
  score, delayed synthetic outcome, and monitoring summary
  fields.
- Outcome or label: generated delayed synthetic outcome.
- Time horizon: synthetic monthly monitoring periods.
- Subgroups or slices: month slices only in the current report.

## Generation

- Source: `generate_monitoring_report.py`.
- Generation method: deterministic synthetic stream with an
  encoded later-period input and outcome shift.
- Random seed or data version: default script seed.
- Known encoded assumptions: baseline period and shifted period
  are constructed to produce detectable monitoring signals.
- Known omitted factors: real coding drift, staffing changes,
  feedback loops, changing practice patterns, and delayed label
  quality problems.

## Quality and limitations

- Missingness pattern: not realistic.
- Measurement noise: simplified synthetic signals.
- Selection effects: generated stream only.
- Proxy-label risk: not evaluated in the current prototype.
- Known mismatch with real-world data: no live data pipeline,
  no label adjudication, no site-specific review process, and no
  production feedback loop.

## Permitted use

- Permitted: local testing, monitoring report examples, and
  governance workflow design.
- Not permitted: clinical monitoring, medical advice, model
  safety claims, or real operational escalation.
- Regeneration instructions: run
  `python prototypes/monitoring-loop-sketch/generate_monitoring_report.py`.

## Linked artifacts

- Model or analysis card: `artifacts/model-card.md`.
- Interface contract: none in current prototype.
- Evaluation registry entry: `artifacts/evaluation-registry.csv`.
- Governance gate review: `artifacts/governance-gate-review.md`.

## Evidence references

Primary citation IDs: E001, E002, E007, E019.
