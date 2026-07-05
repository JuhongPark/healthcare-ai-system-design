# Monitoring loop sketch

Prototype sketch for Track 4: monitoring, governance, and
safety on a synthetic model-output stream. The current
implementation generates a static monitoring report using only
the Python standard library.

## Design question

What does the smallest useful monitoring loop look like when it
must connect input drift, outcome incidence, calibration, and an
operational response?

The point of the sketch is not to validate a model. It is to
make the monitoring and escalation surfaces visible on a
dataset where the stream is synthetic and the drift is known.

## Intended scope

### Data

- **Synthetic model-output stream.** Generated encounter-like
  records with a timestamp bucket, synthetic input signals, a
  model score, and a delayed synthetic outcome.
- **Known drift scenario.** Later months shift the input mix and
  the outcome process so monitoring signals have something to
  detect.
- **No real patient data.** No protected health information,
  hospital extracts, restricted datasets, names, or contact
  details.

### Monitoring signals

- Input shift index against the baseline month.
- Outcome incidence by month.
- Mean prediction by month.
- Brier score and calibration error.
- Alert level and review action based on simple thresholds.

## How to run

```bash
python prototypes/monitoring-loop-sketch/generate_monitoring_report.py
```

The script writes:

- `outputs/synthetic_stream.csv` — regenerated synthetic
  stream, ignored by git.
- `outputs/example_monitoring_summary.csv` — monthly
  monitoring summary.
- `outputs/example_monitoring_report.md` — human-readable
  report with alerts, action hints, and limitations.

## Limitations and cautions

- This report is not medical advice, not clinical decision
  support, and not evidence about real patients.
- Thresholds are illustrative. They are not operating policy.
- The delayed outcome is generated, so calibration drift is a
  controlled demonstration rather than an empirical finding.
- Monitoring detects symptoms of change. It does not identify
  root cause by itself.
