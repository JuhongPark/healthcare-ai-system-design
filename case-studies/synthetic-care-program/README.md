# Synthetic care program safety case

Executable flagship case study for the repository's healthcare
AI safety-case direction.

The case connects evidence design, workflow display, monitoring,
and evaluation registry outputs through one synthetic lifecycle.
It is deliberately small and standard-library-only so the full
case can be regenerated locally.

## Safety boundary

This case is synthetic-only. It contains no real patient data and
no protected health information. It is not medical advice, not
clinical decision support, and not evidence about real patients,
real populations, or real clinical workflows.

## How to run

```bash
python case-studies/synthetic-care-program/run_case.py
```

The command writes the default example outputs under
`case-studies/synthetic-care-program/outputs/`.

Use a separate output directory for temporary runs:

```bash
python case-studies/synthetic-care-program/run_case.py --output-dir /tmp/synthetic-care-program
```

## Generated outputs

- `synthetic_cohort.csv` — synthetic cohort used by the case.
- `target_trial_spec.md` — protocol-like design specification.
- `evidence_report.md` — synthetic evidence-design report.
- `cds_dashboard.html` — static synthetic workflow display.
- `workflow_audit_log.csv` — example audit trail.
- `monitoring_stream.csv` — synthetic model-output stream.
- `monitoring_report.md` — monitoring summary.
- `incidents.csv` — failure-first incident table.
- `governance_decision.md` — decision record linked to
  incidents and evaluation rows.
- `evaluation_registry.csv` — traceability registry for checks.

Later milestones extend this case with a generated safety-case
report.

## Evidence references

Primary citation IDs: E001, E002, E003, E005, E006, E007, E008,
E011, E012, E015, E016, E019, E020, E027.
