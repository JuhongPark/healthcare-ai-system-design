# Target trial specification

Case ID: `SCP-001`

This output is synthetic-only. It is not medical advice, not clinical decision support, and not evidence about real patients or real populations.

## Design question

What evidence would be needed before a synthetic treatment-outcome
signal could be treated as more than an association?

## Protocol-like specification

| Element | Synthetic specification |
| --- | --- |
| Eligibility | Synthetic subjects in the generated cohort. |
| Treatment strategies | Treatment indicator 1 vs. 0 in the generated data. |
| Assignment time | Synthetic index point at cohort entry. |
| Follow-up | Single generated follow-up window. |
| Outcome | Generated binary outcome. |
| Causal contrast | Not estimated. Current report stays at association. |
| Analysis plan | Compare crude rates, treatment groups, and negative-control signal. |
| Required missing evidence | Real data provenance, local validation, causal assumptions, and sensitivity analysis. |

## Evidence references

Primary citation IDs: E008, E011, E012, E013, E014.
