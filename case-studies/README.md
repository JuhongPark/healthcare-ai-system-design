# Case studies

Executable end-to-end case studies live here. Case studies are
the repository's flagship artifacts: they connect evidence,
workflow, monitoring, incidents, evaluation, and governance into
one traceable synthetic lifecycle.

## Safety boundary

Case studies are synthetic-only unless explicitly documented
otherwise. They are not medical advice, not clinical decision
support, and not evidence about real patients, real populations,
or real clinical workflows.

## Current flagship

- `synthetic-care-program/` — an executable synthetic healthcare
  AI safety case. It generates a cohort, target trial
  specification, evidence report, dashboard, audit log,
  monitoring stream, monitoring report, incidents, governance
  decision, safety-case report, and evaluation registry.

Run it with:

```bash
python case-studies/synthetic-care-program/run_case.py
```

The generated safety case is intentionally conservative. The
default conclusion is not ready for deployment.
