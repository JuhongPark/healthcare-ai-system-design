# Prototypes

This directory holds prototype sketches. Each sketch exists to
make a specific design question concrete.

## Philosophy

- **Synthetic, public, or simulated data only.** No real patient
  data, no protected health information, no private clinical
  extracts.
- **Design questions first.** Each prototype exists to make a
  specific design question concrete. It does not exist to
  demonstrate performance.
- **Make limitations visible.** A prototype that hides its
  limitations is worse than no prototype. Known failure modes,
  assumptions, and caveats should live next to the outputs, not
  in a separate document.
- **Distinguish association from causation.** Any analysis of
  synthetic treatment data should be labeled as associational
  unless a causal design is explicitly stated, and even then
  the claim applies only to the synthetic data.
- **Avoid medical advice.** Outputs must not be framed as
  suggestions for individual patients. Language should describe
  method behavior, not patient care.
- **Outputs are research sketches.** If a prototype looks like a
  clinical tool, that is an artifact of the interface, not a
  change in status.

## What to expect in a prototype directory

Each prototype directory should contain, at minimum:

- a short README describing the design question, the synthetic
  data used, the method, the limitations, and what the sketch
  is not;
- a clearly labeled entry point (notebook or script);
- a note on where the synthetic data comes from and how to
  regenerate it.

## Current directories

- `rwe-drug-efficacy-sketch/` — prototype for Track 1 questions
  about observational treatment-outcome analysis on synthetic
  data.
- `cds-risk-dashboard/` — prototype for Track 3 questions about
  workflow-aware decision support on synthetic patient-like
  data.

Each directory currently describes what the sketch will
explore; implementation is not yet committed.
