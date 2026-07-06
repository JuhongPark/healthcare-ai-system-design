# Governance decision

Case ID: `SCP-001`

This output is synthetic-only. It is not medical advice, not clinical decision support, and not evidence about real patients or real populations.

## Decision

Decision: `pause`

This decision does not authorize deployment, clinical use,
medical advice, or clinical decision support. It records the
synthetic governance response for the case study.

## Evidence reviewed

- Incident artifact: `outputs/incidents.csv`
- Evaluation artifact: `outputs/evaluation_registry.csv`
- Linked incident IDs: SCP-INC-001, SCP-INC-002, SCP-INC-003, SCP-INC-004
- Linked evaluation IDs: SCP-EV-002, SCP-EV-003, SCP-EV-004, SCP-EV-005, SCP-EV-006

## Incident summary

- Total incidents: 4
- High severity incidents: 2
- Medium severity incidents: 2

## Rationale

The default case is paused because high-severity synthetic
monitoring signals require review before any deployment-readiness
claim. Missing local validation and unresolved evidence gaps
also block any clinical-use claim.

## Required follow-up

- Review drift and calibration assumptions.
- Review workflow burden before adding alert variants.
- Review negative-control and proxy-label warnings.
- Regenerate the safety case after changes.

## Evidence references

Primary citation IDs: E001, E002, E003, E007, E009, E010, E027.
