# Model or analysis card: synthetic RWE analysis

## Artifact

- Prototype: `rwe-drug-efficacy-sketch`
- Artifact name: synthetic propensity-adjusted RWE analysis
- Artifact version: default analysis script
- Owner: repository prototype
- Last updated: 2026-07-06

## Safety boundary

This artifact is a synthetic research sketch. It is not medical
advice, not clinical decision support, and not validated for real
patients, real populations, real treatments, or operational use.

## Intended use

- Design question: how to keep observational association,
  adjustment, balance, and negative-control diagnostics visible
  in a treatment-outcome analysis.
- Intended user: repository reader studying healthcare AI system
  design.
- Intended output: summary table and report showing crude and
  adjusted synthetic associations.
- Intended evaluation stage: internal method demonstration only.
- Out-of-scope use: causal claims about treatment effects or
  real-world evidence claims.

## Inputs and outputs

- Input data: synthetic cohort from `outputs/synthetic_cohort.csv`.
- Required fields: treatment indicator, observed synthetic
  covariates, primary outcome, and negative-control outcome.
- Output fields: crude association, weighted association,
  balance diagnostics, negative-control diagnostic, and
  limitation text.
- Uncertainty or confidence display: none beyond reported
  summary values in the current sketch.
- Human action this should not directly trigger: any clinical,
  regulatory, or treatment decision.

## Method summary

- Method type: small standard-library analysis with logistic
  propensity estimation and inverse probability weighting.
- Baseline or comparator: crude unadjusted association.
- Assumptions: observed confounders are represented by the
  synthetic generator, and weighting is a demonstration rather
  than proof of causal validity.
- Parameters or seed: default generator and analysis settings.
- Dependencies: Python standard library only.

## Evaluation summary

- Internal validation: default example regenerates and analyzes
  the synthetic cohort.
- External validation: none.
- Local validation: none.
- Calibration: not applicable to the current association sketch.
- Subgroup or slice evaluation: covariate balance diagnostics.
- Workflow or human-factors evaluation: none.

## Limitations

- Known failure modes: adjustment can look reassuring even when
  unmeasured confounding would remain in a real study.
- Data limitations: no real RWD source, coding drift, site
  variation, missingness, or censoring.
- Metric limitations: association summaries do not establish
  efficacy.
- Generalization limits: applies only to the generated synthetic
  dataset.
- Interpretability limits: coefficients and weights are method
  demonstrations, not explanations of real outcomes.

## Monitoring and update

- Monitoring signals: not applicable for a static synthetic
  analysis.
- Update trigger: changes to generator assumptions or analysis
  methods.
- Pause or rollback trigger: any output language implying real
  clinical, regulatory, or causal evidence.
- Owner for review: repository maintainer.

## Evidence references

Primary citation IDs: E008, E011, E012, E013, E014, E020.
