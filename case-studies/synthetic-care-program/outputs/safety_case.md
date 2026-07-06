# Synthetic healthcare AI safety case

Case ID: `SCP-001`

This output is synthetic-only. It is not medical advice, not clinical decision support, and not evidence about real patients or real populations.

## Deployment-readiness conclusion

Conclusion: **not ready for deployment**.

The generated governance decision is `pause`. The decision
does not authorize deployment, clinical use, medical advice,
clinical decision support, or use with real patient data.

## System claim reviewed

Claim `SCP-CL-001`: the synthetic system is not ready for
deployment because lifecycle evidence is incomplete and failure
signals require review.

Claim status: supported.

## Supporting evidence

- Target trial specification: `outputs/target_trial_spec.md`.
- Evidence report: `outputs/evidence_report.md`.
- Dashboard: `outputs/cds_dashboard.html`.
- Workflow audit log: `outputs/workflow_audit_log.csv`.
- Monitoring report: `outputs/monitoring_report.md`.
- Incident table: `outputs/incidents.csv`.
- Governance decision: `outputs/governance_decision.md`.
- Evaluation registry: `outputs/evaluation_registry.csv`.

Linked incident IDs: SCP-INC-001, SCP-INC-002, SCP-INC-003, SCP-INC-004

Linked evaluation IDs: SCP-EV-001, SCP-EV-002, SCP-EV-003, SCP-EV-004, SCP-EV-005, SCP-EV-006, SCP-EV-007

## Missing evidence

- Real data provenance and data-quality review.
- External validation.
- Local validation.
- Prospective validation.
- Calibration review using real delayed outcomes.
- Human-factors and workflow-burden evaluation.
- Subgroup and proxy-label audit with real governance review.
- Approved change-control and rollback plan.

## Known hazards

- Dataset shift can make monitoring metrics diverge from
  baseline expectations.
- Calibration drift can make displayed risk values misleading.
- Alert burden can increase even for a passive dashboard.
- Negative-control imbalance can reveal unresolved confounding.
- Proxy labels can diverge from latent need.
- A dashboard can look more actionable than its evidence allows.

## Generated incidents

| Incident | Severity | Trigger metric | Observed value | Decision | Linked evaluation |
| --- | --- | --- | ---: | --- | --- |
| SCP-INC-001 | high | month 6 shift_index | 3.00 | pause | SCP-EV-004 |
| SCP-INC-002 | high | month 5 calibration_gap | 0.085 | pause | SCP-EV-004 |
| SCP-INC-003 | medium | month 5 alert_rate | 0.500 | monitor | SCP-EV-003 |
| SCP-INC-004 | medium | negative_control_rate_difference | 0.179 | update | SCP-EV-002 |

## Governance decision

Decision: `pause`.

Rationale: high-severity synthetic monitoring incidents and
missing lifecycle evidence block any deployment-readiness claim.
The correct next step is review and redesign, not clinical use.

## Open assumptions

- The synthetic data generator is intentionally simplified.
- Monitoring thresholds are illustrative and not operating
  policy.
- The dashboard is a workflow hypothesis, not a validated
  interface.
- The evaluation registry demonstrates traceability, not
  regulatory sufficiency.

## Next required review

1. Review incident root-cause assumptions.
2. Add richer target-trial and sensitivity sections.
3. Add workflow variant comparison.
4. Add proxy-label fairness audit.
5. Regenerate this safety case after changes.

## Evidence references

Primary citation IDs: E001, E002, E003, E005, E006, E007, E009,
E010, E019, E020, E027.
