# AI for clinical trial design and operations

Notes on AI methods applied to the trial machinery that sits
between drug candidate selection and regulatory evidence —
patient recruitment, site selection, external comparator
arms, adaptive designs, and digital endpoints.

## Why a separate note

`docs/drug-design.md` touches trial design; `docs/research-agenda.md`
Track 1 covers how trial-generated evidence interacts with
observational data. This note focuses on the trial as an
operational system: how a protocol is populated with
patients, how sites are chosen, how modeled comparators
enter the evidence, and how digital instruments change
what the trial measures. AI in this territory promises
shorter timelines and better-matched populations; the
methodological risk is that AI-driven choices silently
shift the estimand the trial is meant to estimate.

## Patient recruitment and matching

- **Eligibility criteria refinement.** ML on EHR cohorts
  can estimate how restrictive a criterion set is and
  which criteria exclude the most otherwise-eligible
  patients. Liu et al. (2021) reported on using
  real-world data and AI to evaluate oncology trial
  eligibility; the structural insight is that many
  criteria fail a utility check when they are
  confronted with population data.
- **Candidate identification.** Rule-based and
  ML-augmented matching systems scan EHRs and
  registries to propose candidates for screening. The
  persistent question is how consent and contact
  workflows are integrated; a good match surfaced to
  no one is not a recruited patient.
- **Decentralized recruitment.** Wearable-enrolled
  cohorts, virtual screening visits, and direct-to-
  patient outreach shift the upstream distribution.
  Representation and digital access effects are
  first-order, not residual.

## Site selection and feasibility

- **Performance prediction.** Historical trial
  performance (screen-fail rate, enrollment rate,
  protocol deviations) feeds site-selection models. A
  performance model that optimizes recruitment rate
  alone can select sites that see patients who look
  unlike the intended label population.
- **Country and region mix.** Protocol feasibility
  depends on standard-of-care variation, regulatory
  lead times, and competing studies. Models that take
  only the first of these seriously produce selection
  that breaks on the others.
- **Capacity matching.** Site infrastructure — imaging
  modalities, central-lab shipping, device handling —
  bounds what a protocol can actually measure. Feasibility
  assessment crosses clinical, logistical, and data
  pipelines at once.

## External comparator arms and synthetic controls

Hybrid and single-arm trials increasingly rely on
external comparator arms drawn from real-world data or
historical trial controls:

- **Hybrid designs.** A randomized internal arm is
  augmented with an external cohort to improve
  precision; statistical borrowing methods (dynamic
  borrowing, MAP priors) regulate the contribution.
- **Single-arm trials with external comparators.**
  Rare-disease and oncology programs where randomization
  is unethical or infeasible; the external cohort is
  the comparator rather than a supplement.
- **Regulatory posture.** FDA and EMA have accepted
  external comparator evidence in selected oncology and
  rare-disease approvals. Acceptance is case by case
  and evidence standards are rising; methodological
  critique has paralleled acceptance.

The design question is whether the external comparator
reproduces the standard of care and measurement regime
the internal arm would have seen. When it does not, the
comparison is confounded in ways that the statistical
borrowing framework cannot repair.

## Adaptive and platform designs

- **Adaptive designs.** Pre-specified modifications to
  sample size, randomization ratio, dose, or
  population based on accruing data. Adaptive-design
  guidance emphasizes that adaptation rules are part
  of the protocol and part of the type-I error
  accounting.
- **Master protocols.** Umbrella, basket, and platform
  trials share infrastructure across arms, sub-studies,
  or indications. REMAP-CAP and I-SPY are the
  reference examples.
- **Bayesian monitoring.** Posterior probabilities of
  efficacy or futility drive interim decisions;
  properly calibrated, they control operating
  characteristics without fully pre-specified stopping
  boundaries.
- **Simulation-based design.** Trial simulation
  evaluates operating characteristics under realistic
  scenarios; virtual twins and disease-progression
  models feed the simulations, with their own
  validation needs.

AI methods can propose adaptive rules and evaluate
operating characteristics, but the audit trail the
regulator expects is the simulation protocol and its
result, not the training process that produced the
rule.

## Digital endpoints and biomarkers

- **Wearable and sensor endpoints.** Step count,
  activity, sleep, cardiovascular signals; measurement
  properties depend on device, firmware, and wear
  adherence.
- **Image-derived endpoints.** Standardized radiology
  reads, AI-augmented reads, and fully automated
  endpoints. The 21st Century Cures Act and FDA
  biomarker qualification pathway govern use at the
  approval level.
- **ePROs.** Electronic patient-reported outcomes with
  their own psychometric and comparability questions
  relative to paper instruments.

Qualifying a digital endpoint is a program of its own;
using one in a trial before qualification means the
endpoint carries its own evidence burden alongside the
treatment question.

## Operational AI: monitoring, safety, and data management

- **Risk-based monitoring.** ML-informed prioritization
  of site visits and data-quality checks; ICH E6(R3)
  guidance emphasizes risk-based quality management.
- **Safety signal detection in trial.** Real-time
  pharmacovigilance on ongoing trials rather than
  post-approval only.
- **Central data review.** Automated flagging of
  outliers, inconsistent data, and endpoint
  adjudication inputs.
- **eSource and interoperability.** Direct capture
  from EHR into trial databases; data provenance and
  reconciliation rules are load-bearing.

## Connection to other notes

- Upstream context: `docs/clinical-pharmacology-and-midd.md`
  (dose and population selection informed by PK/PD).
- Post-approval continuation:
  `docs/pharmacoepidemiology-methods.md` (the
  observational methodology that carries the evidence
  after the trial).
- Program-level framing:
  `docs/drug-discovery-program-architecture.md`
  (stage-gate integration of trial design choices).
- Regulatory surround:
  `docs/regulatory-landscape.md`.
- Case material: `docs/pharma-ai-case-studies.md`
  (including cases where AI-assisted trial components
  were cited in the approval narrative).

## Open questions

- How should an AI-derived eligibility refinement be
  documented so that a reviewer can separate the
  recruitment gain from the population shift it
  introduced?
- When is an external comparator arm a reasonable
  substitute for a concurrent control, and which
  indications have drawn stable guidance?
- How are digital endpoints qualified across sponsors
  so that qualification work does not have to be
  repeated by each program?
- What does an auditable simulation package look like
  for an adaptive design whose rules came from an ML
  model?
- How do adaptive and platform trial infrastructures
  connect to post-marketing observational data so that
  the same question is carried across the evidence
  lifecycle?

## Limitations and cautions

- Descriptions of regulatory acceptance reflect
  published guidance and public approvals; specific
  programs should rely on current FDA, EMA, and PMDA
  guidance rather than this note.
- Digital endpoint examples are orientation; device-
  and indication-specific qualification work is
  required before use in a pivotal trial.
- Synthetic controls and external comparator arms are
  methodologically active areas; claims about
  equivalence to randomization should be checked
  against current evidence.
- AI-assisted trial operations tools can improve
  speed and cost without changing the underlying
  statistical and clinical validity of a protocol;
  speed alone is not evidence quality.
