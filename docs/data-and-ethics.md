# Data and ethics notes

Working principles for data use in this repository. These are
constraints first, not aspirations.

## Data sources

- Use public, synthetic, or simulated data only.
- No protected health information.
- No private patient records, no hospital extracts, no
  restricted or licensed datasets.
- No data that would require a data use agreement or access
  controls.
- Any dataset referenced by name should be publicly available
  and appropriately cited when it is actually used.

## Clinical claims

- No clinical use. Nothing here is intended for use in patient
  care.
- No medical advice. Outputs are not suggestions for
  individuals and must not be framed as such.
- No claims of validated decision support.
- No positioning as a medical device or as a component of one.

## Evidence claims

- Observational analyses are described as associations unless a
  causal design is made explicit and its assumptions are
  stated.
- Effect estimates from synthetic data illustrate the behavior
  of methods. They do not estimate real-world effects.
- Subgroup performance on synthetic data does not reflect real
  subgroup performance.
- External validation claims require external data. Internal
  splits are not external validation.

## Uncertainty and limitations

- Uncertainty should be quantified and communicated where
  plausible, and labeled as unknown where it is not.
- Limitations should appear in the same place as the results,
  not in a separate appendix.
- Known failure modes should be listed alongside known
  capabilities.

## Prototypes

- Prototypes are research sketches. They exist to make design
  questions concrete, not to demonstrate performance on real
  patients.
- A prototype that looks like a clinical tool is not a clinical
  tool. The appearance of polish should not be read as evidence
  of validation.
- Any notebook or dashboard should make its synthetic or public
  data source visible at the top.

## Responsibility

- The author takes responsibility for what is in this
  repository. Readers are responsible for not using it outside
  the constraints stated above.
- Issues and corrections are welcome.
