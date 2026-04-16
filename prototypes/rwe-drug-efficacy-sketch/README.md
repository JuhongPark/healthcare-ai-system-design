# RWE drug efficacy sketch

Prototype sketch for Track 1: real-world evidence and drug
efficacy evaluation on synthetic data. This document describes
the intended scope of the sketch; implementation is not yet
committed.

## Design question

What does a careful observational treatment-outcome analysis
look like when every assumption is made explicit and every step
is labeled with the thing it depends on?

The point of the sketch is not to estimate a treatment effect.
It is to make method behavior and failure modes visible on a
dataset where the truth is known.

## Intended scope

### Data

- **Synthetic medication exposure.** A simulated cohort with a
  defined index date, a defined exposure window, and a defined
  treatment indicator.
- **Synthetic outcomes.** Time-to-event outcomes generated from
  a known data-generating process with a known treatment
  effect.
- **Synthetic confounders.** A set of confounders with varying
  strengths and varying overlap between treated and untreated
  groups.

The synthetic data generator itself is part of the prototype.
It should be easy to rerun with different confounder
structures, sample sizes, and effect sizes.

### Cohort construction

- A written cohort definition: who is eligible, what the index
  date is, how the exposure window is defined, what counts as an
  outcome, and what the follow-up rule is.
- An explicit statement of the target population the cohort is
  meant to represent (within the synthetic world).
- A pre-analysis list of decisions that will be varied in
  sensitivity analyses.

### Methods

- **Propensity score methods.** At minimum, matching and
  inverse probability weighting, with diagnostics for covariate
  balance and effective sample size.
- **Survival analysis.** Weighted Kaplan–Meier and a
  proportional hazards model, with a check on the
  proportional-hazards assumption.
- **Negative controls.** A set of outcomes with no plausible
  causal relationship to the exposure, used to estimate
  residual bias.
- **Sensitivity analyses.** Variation in the exposure
  definition, the eligibility window, the outcome ascertainment
  rule, and the adjustment set. Each variation is a separate
  row in a summary table.

### Reporting

- Every estimate is labeled as **association** unless the
  report includes an explicit causal argument.
- Every estimate is reported alongside the sensitivity analyses
  that could undo it.
- The known data-generating process is revealed at the end, so
  a reader can see how the methods did against the ground
  truth.

## Limitations and cautions

- This prototype does not estimate a real treatment effect. The
  numbers it produces apply only to the synthetic data
  generator it is run on.
- Results do not constitute comparative effectiveness research,
  post-marketing surveillance, or clinical guidance.
- The value of the sketch is in showing method behavior and
  failure modes, not in the specific effect estimates.
- A well-behaving method on synthetic data is not a
  well-behaving method in general; it is a method that handled
  this particular data-generating process.
