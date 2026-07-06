# Data card: synthetic RWE cohort

## Artifact

- Prototype: `rwe-drug-efficacy-sketch`
- Dataset name: synthetic treatment-outcome cohort
- Dataset version: default generator output
- Data owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This dataset is synthetic-only. It contains no real patient data
and no protected health information. It is not medical advice,
not clinical decision support, and not evidence about real
patients, real populations, or real medications.

## Motivation

- Design question: how an observational treatment-outcome
  analysis changes when confounding, adjustment, and negative
  controls are visible.
- Intended use: demonstrate method behavior and documentation
  needs for real-world evidence design.
- Out-of-scope use: comparative effectiveness claims, product
  evaluation, post-marketing surveillance, or clinical guidance.
- Decision this dataset should not support: treatment selection
  for any patient or population.

## Composition

- Unit of observation: synthetic subject row.
- Row count: 120 rows in the committed default example.
- Key fields: treatment indicator, age, comorbidity score,
  baseline severity, frailty score, synthetic outcome, and
  synthetic negative-control outcome.
- Outcome or label: generated binary primary outcome and
  generated negative-control outcome.
- Time horizon: synthetic single-index follow-up window.
- Subgroups or slices: observed covariate slices only. They do
  not represent real demographic groups.

## Generation

- Source: `generate_synthetic_cohort.py`.
- Generation method: deterministic synthetic cohort generator
  with encoded treatment assignment, confounding, and outcomes.
- Random seed or data version: default script seed.
- Known encoded assumptions: treatment assignment depends on
  observed synthetic covariates, and the primary outcome has a
  known generated relationship to treatment and covariates.
- Known omitted factors: unobserved clinical context, coding
  changes, adherence, censoring, site effects, and outcome
  adjudication.

## Quality and limitations

- Missingness pattern: no realistic missingness process is
  represented in the default example.
- Measurement noise: simplified generated covariates, not
  clinical measurements.
- Selection effects: synthetic cohort construction only.
- Proxy-label risk: low for the sketch because outcomes are
  generated directly, but real RWE would require label audit.
- Known mismatch with real-world data: no claims data, EHR data,
  registry data, or operational data quality problems.

## Permitted use

- Permitted: local testing, documentation examples, and method
  behavior demonstrations.
- Not permitted: evidence generation, medical advice, clinical
  decision support, or external claims about real populations.
- Regeneration instructions: run
  `python prototypes/rwe-drug-efficacy-sketch/generate_synthetic_cohort.py`.

## Linked artifacts

- Model or analysis card: `artifacts/model-card.md`.
- Interface contract: none in current prototype.
- Evaluation registry entry: `artifacts/evaluation-registry.csv`.
- Governance gate review: none in current prototype.

## Evidence references

Primary citation IDs: E007, E008, E011, E012, E019.
