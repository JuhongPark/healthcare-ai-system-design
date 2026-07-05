# CDS risk dashboard sketch

Prototype sketch for Track 3: a workflow-aware clinical decision
support dashboard on synthetic patient-like data. The current
implementation generates a static HTML dashboard using only the
Python standard library.

## Design question

What does it take to put a risk estimate in front of a user in
a way that respects workflow, communicates uncertainty, shows
its limitations, and keeps the user in charge?

The prototype is an interface sketch. It is not decision support
for real patients.

## Intended scope

### Data

- **Synthetic patient-like records.** A small set of simulated
  patients with enough structure to populate a dashboard:
  demographics, a few clinical variables, a few time-varying
  signals, and a synthetic outcome label.
- **No real patient data.** No protected health information,
  no hospital extracts, no restricted datasets.

### Interface elements

- **Risk estimate.** A primary number or category, with a clear
  statement of what it is estimating and over what horizon.
- **Uncertainty display.** A visible indicator of how confident
  the estimate is, designed for a non-statistical reader. This
  is the hardest element and the one most worth iterating on.
- **Explanation panel.** A contextual explanation of the
  estimate that also shows what it is not explaining. The goal
  is to avoid turning the panel into a ranking that invites
  over-interpretation.
- **Limitations panel.** Known limitations shown alongside the
  estimate, not hidden behind a link.
- **Human override.** An explicit override control that records
  the reason and keeps the user accountable for the final
  decision.
- **Audit trail.** A log of what was shown, what was clicked,
  and what was overridden. Part of the design question is what
  the minimum viable audit trail should contain.
- **Workflow timing.** Notes on when in a simulated encounter
  the dashboard would appear and why, including what it should
  not interrupt.

### Local validation concept

Even a sketch should carry a clear idea of what local validation
would look like if the prototype were ever used somewhere. This
includes:

- a statement of the target setting (which is, for this sketch,
  "none — synthetic only");
- the metrics that would be evaluated at a hypothetical site;
- the subgroup breakdowns that would be required before use;
- a note on what would have to be true before any local
  deployment conversation.

## How to run

```bash
python prototypes/cds-risk-dashboard/generate_dashboard.py
```

The script writes:

- `outputs/synthetic_patients.csv` — regenerated synthetic
  patient-like records, ignored by git.
- `outputs/example_audit_log.csv` — minimum audit trail
  example.
- `outputs/cds_dashboard.html` — static dashboard sketch that
  can be opened directly in a browser.

The dashboard is intentionally static. It exists to show how
risk, uncertainty, limitations, override capture, and audit
review might share one workflow surface.

## Limitations and cautions

- This is an interface sketch, not clinical decision support,
  not medical advice, and not a validated tool.
- Risk estimates produced by the prototype describe synthetic
  labels on synthetic data. They do not describe real patients.
- Interpretability displays can create a false sense of
  understanding. The prototype should make that risk visible.
- Any workflow claims drawn from the sketch are hypotheses
  about interaction design, not evidence about clinical
  outcomes.
