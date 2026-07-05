"""Generate a static synthetic CDS dashboard sketch."""

from __future__ import annotations

import argparse
import csv
import html
import math
import random
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
DEFAULT_PATIENTS_PATH = HERE / "outputs" / "synthetic_patients.csv"
DEFAULT_AUDIT_PATH = HERE / "outputs" / "example_audit_log.csv"
DEFAULT_DASHBOARD_PATH = HERE / "outputs" / "cds_dashboard.html"

PATIENT_FIELDS = [
    "encounter_id",
    "age_band",
    "care_area",
    "acuity_signal",
    "lab_trend",
    "prior_utilization",
    "missing_signals",
    "risk_score",
    "uncertainty_low",
    "uncertainty_high",
    "uncertainty_label",
    "synthetic_outcome",
]

AUDIT_FIELDS = ["sequence", "event_type", "actor_role", "captured_value"]

STYLE = """
:root {
  color-scheme: light;
  --ink: #17202a;
  --muted: #53616f;
  --line: #cfd8dc;
  --page: #f6f8f9;
  --panel: #ffffff;
  --teal: #1f7a76;
  --blue: #315f9c;
  --amber: #a76500;
  --red: #a33a3a;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--page);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.45;
}

header {
  border-bottom: 1px solid var(--line);
  background: #ffffff;
  padding: 18px 24px;
}

h1, h2, h3, p {
  margin-top: 0;
}

h1 {
  margin-bottom: 6px;
  font-size: 24px;
  letter-spacing: 0;
}

h2 {
  font-size: 17px;
  margin-bottom: 12px;
}

h3 {
  font-size: 14px;
  margin-bottom: 8px;
}

.subhead {
  color: var(--muted);
  margin-bottom: 0;
}

.safety {
  margin-top: 14px;
  border: 1px solid #d7c59a;
  border-left: 5px solid var(--amber);
  background: #fff8e8;
  padding: 10px 12px;
  max-width: 980px;
  border-radius: 6px;
}

main {
  display: grid;
  grid-template-columns: minmax(260px, 340px) minmax(0, 1fr);
  gap: 18px;
  padding: 18px 24px 28px;
}

section, aside {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
}

aside {
  padding: 14px;
}

.workspace {
  display: grid;
  gap: 14px;
}

.panel {
  padding: 16px;
}

.metric-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}

.metric {
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 12px;
  min-height: 102px;
}

.label {
  color: var(--muted);
  display: block;
  font-size: 12px;
  margin-bottom: 6px;
}

.value {
  display: block;
  font-size: 24px;
  font-weight: 700;
}

.risk-high {
  color: var(--red);
}

.risk-elevated {
  color: var(--amber);
}

.risk-watch {
  color: var(--blue);
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border-bottom: 1px solid #e5ebee;
  font-size: 13px;
  padding: 8px 6px;
  text-align: left;
  vertical-align: top;
}

th {
  color: var(--muted);
  font-weight: 650;
}

.queue td:last-child,
.queue th:last-child {
  text-align: right;
}

.two-column {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 14px;
}

.callout {
  border-left: 4px solid var(--teal);
  background: #edf7f5;
  border-radius: 6px;
  padding: 12px;
}

.warning {
  border-left-color: var(--amber);
  background: #fff8e8;
}

.audit {
  border-left-color: var(--blue);
  background: #eef4fb;
}

.override-grid {
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: 8px;
}

.field {
  border: 1px solid var(--line);
  border-radius: 6px;
  min-height: 38px;
  padding: 9px 10px;
  background: #fafcfd;
}

@media (max-width: 860px) {
  main,
  .two-column,
  .metric-grid {
    grid-template-columns: 1fr;
  }
}
"""


def logistic(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def weighted_choice(rng: random.Random, values: list[tuple[str, float]]) -> str:
    threshold = rng.random() * sum(weight for _, weight in values)
    cumulative = 0.0
    for value, weight in values:
        cumulative += weight
        if threshold <= cumulative:
            return value
    return values[-1][0]


def risk_label(score: float) -> str:
    if score >= 0.45:
        return "high"
    if score >= 0.27:
        return "elevated"
    return "watch"


def generate_patients(size: int = 12, seed: int = 20260705) -> list[dict[str, str]]:
    if size < 3:
        raise ValueError("size must be at least 3")

    rng = random.Random(seed)
    age_bands = [("35-44", 0), ("45-54", 1), ("55-64", 2), ("65-74", 3), ("75-84", 4)]
    care_areas = [("Emergency", 0.36), ("Ward", 0.42), ("Observation", 0.22)]
    acuity = [("stable", 0), ("watch", 1), ("escalating", 2)]
    lab_trends = [("flat", 0), ("mild change", 1), ("marked change", 2)]

    rows: list[dict[str, str]] = []
    for index in range(1, size + 1):
        age_band, age_index = rng.choice(age_bands)
        care_area = weighted_choice(rng, care_areas)
        acuity_signal, acuity_index = rng.choice(acuity)
        lab_trend, lab_index = rng.choice(lab_trends)
        prior_utilization = rng.randint(0, 4)
        missing_signals = rng.choice([0, 0, 0, 1, 1, 2])

        risk_logit = (
            -2.15
            + 0.22 * age_index
            + 0.55 * acuity_index
            + 0.42 * lab_index
            + 0.24 * prior_utilization
            + 0.30 * missing_signals
        )
        risk_score = logistic(risk_logit)
        uncertainty_width = 0.06 + 0.035 * missing_signals + 0.02 * (acuity_index == 2)
        uncertainty_low = max(0.01, risk_score - uncertainty_width)
        uncertainty_high = min(0.99, risk_score + uncertainty_width)
        uncertainty_label = "wide" if uncertainty_width >= 0.11 else "moderate"
        synthetic_outcome = 1 if rng.random() < risk_score else 0

        rows.append(
            {
                "encounter_id": f"SYN-ENC-{index:03d}",
                "age_band": age_band,
                "care_area": care_area,
                "acuity_signal": acuity_signal,
                "lab_trend": lab_trend,
                "prior_utilization": str(prior_utilization),
                "missing_signals": str(missing_signals),
                "risk_score": f"{risk_score:.3f}",
                "uncertainty_low": f"{uncertainty_low:.3f}",
                "uncertainty_high": f"{uncertainty_high:.3f}",
                "uncertainty_label": uncertainty_label,
                "synthetic_outcome": str(synthetic_outcome),
            }
        )

    return rows


def make_audit_events(selected: dict[str, str]) -> list[dict[str, str]]:
    return [
        {
            "sequence": "1",
            "event_type": "dashboard_viewed",
            "actor_role": "synthetic reviewer",
            "captured_value": f"encounter={selected['encounter_id']}",
        },
        {
            "sequence": "2",
            "event_type": "risk_panel_viewed",
            "actor_role": "synthetic reviewer",
            "captured_value": f"risk_score={selected['risk_score']}",
        },
        {
            "sequence": "3",
            "event_type": "limitations_acknowledged",
            "actor_role": "synthetic reviewer",
            "captured_value": "synthetic-only limitations visible",
        },
        {
            "sequence": "4",
            "event_type": "override_reason_recorded",
            "actor_role": "synthetic reviewer",
            "captured_value": "workflow context outside model display",
        },
    ]


def write_csv(
    rows: Iterable[dict[str, str]], output_path: Path, fieldnames: list[str]
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def pct(value: str) -> str:
    return f"{float(value) * 100:.1f}%"


def escape(value: str) -> str:
    return html.escape(value, quote=True)


def queue_rows(patients: list[dict[str, str]]) -> str:
    rows = []
    for patient in patients:
        risk = float(patient["risk_score"])
        rows.append(
            "<tr>"
            f"<td>{escape(patient['encounter_id'])}</td>"
            f"<td>{escape(patient['care_area'])}</td>"
            f"<td>{escape(patient['acuity_signal'])}</td>"
            f"<td>{pct(patient['risk_score'])}</td>"
            "</tr>"
        )
    return "\n".join(rows)


def audit_rows(events: list[dict[str, str]]) -> str:
    rows = []
    for event in events:
        rows.append(
            "<tr>"
            f"<td>{escape(event['sequence'])}</td>"
            f"<td>{escape(event['event_type'])}</td>"
            f"<td>{escape(event['actor_role'])}</td>"
            f"<td>{escape(event['captured_value'])}</td>"
            "</tr>"
        )
    return "\n".join(rows)


def write_dashboard(
    patients: list[dict[str, str]],
    audit_events: list[dict[str, str]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sorted_patients = sorted(patients, key=lambda row: float(row["risk_score"]), reverse=True)
    selected = sorted_patients[0]
    risk_class = f"risk-{risk_label(float(selected['risk_score']))}"
    risk_range = f"{pct(selected['uncertainty_low'])} to {pct(selected['uncertainty_high'])}"

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Synthetic CDS Risk Dashboard Sketch</title>
  <style>{STYLE}</style>
</head>
<body>
  <header>
    <h1>Synthetic CDS Risk Dashboard Sketch</h1>
    <p class="subhead">Workflow-aware display for a simulated risk estimate, uncertainty, limitations, override capture, and audit review.</p>
    <div class="safety">
      This static dashboard uses synthetic patient-like records only. It is not medical advice, not clinical decision support, not a validated tool, and not evidence about real patients.
    </div>
  </header>
  <main>
    <aside>
      <h2>Encounter Queue</h2>
      <table class="queue">
        <thead>
          <tr><th>Encounter</th><th>Area</th><th>Acuity</th><th>Risk</th></tr>
        </thead>
        <tbody>
          {queue_rows(sorted_patients)}
        </tbody>
      </table>
    </aside>
    <div class="workspace">
      <section class="panel">
        <h2>Selected Synthetic Encounter</h2>
        <div class="metric-grid">
          <div class="metric">
            <span class="label">72-hour synthetic risk label</span>
            <span class="value {risk_class}">{pct(selected['risk_score'])}</span>
            <span class="label">Not a patient-care recommendation</span>
          </div>
          <div class="metric">
            <span class="label">Uncertainty range</span>
            <span class="value">{risk_range}</span>
            <span class="label">{escape(selected['uncertainty_label'])} uncertainty</span>
          </div>
          <div class="metric">
            <span class="label">Synthetic encounter</span>
            <span class="value">{escape(selected['encounter_id'])}</span>
            <span class="label">{escape(selected['care_area'])}</span>
          </div>
        </div>
      </section>
      <section class="panel two-column">
        <div>
          <h2>Signal Context</h2>
          <table>
            <tbody>
              <tr><th>Age band</th><td>{escape(selected['age_band'])}</td></tr>
              <tr><th>Acuity signal</th><td>{escape(selected['acuity_signal'])}</td></tr>
              <tr><th>Lab trend</th><td>{escape(selected['lab_trend'])}</td></tr>
              <tr><th>Prior utilization count</th><td>{escape(selected['prior_utilization'])}</td></tr>
              <tr><th>Missing signals</th><td>{escape(selected['missing_signals'])}</td></tr>
            </tbody>
          </table>
        </div>
        <div class="callout">
          <h2>Explanation Caveats</h2>
          <p>The display shows which synthetic signals are present near the score. It does not prove causality, explain a real patient trajectory, or validate any action.</p>
          <p>The uncertainty band widens when synthetic inputs are missing or the acuity signal is escalating.</p>
        </div>
      </section>
      <section class="panel two-column">
        <div class="callout warning">
          <h2>Limitations Visible With Output</h2>
          <p>Risk values describe generated labels in a simulated dataset. They should not be used for triage, diagnosis, treatment, staffing, or real workflow decisions.</p>
          <p>Workflow claims from this page are design hypotheses only.</p>
        </div>
        <div>
          <h2>Override Capture Mock</h2>
          <div class="override-grid">
            <span class="label">Disposition</span>
            <span class="field">No action recorded in prototype</span>
            <span class="label">Reason category</span>
            <span class="field">Workflow context outside model display</span>
            <span class="label">Reviewer note</span>
            <span class="field">Synthetic audit example only</span>
          </div>
        </div>
      </section>
      <section class="panel callout audit">
        <h2>Minimum Audit Trail Example</h2>
        <table>
          <thead>
            <tr><th>#</th><th>Event</th><th>Actor role</th><th>Captured value</th></tr>
          </thead>
          <tbody>
            {audit_rows(audit_events)}
          </tbody>
        </table>
      </section>
    </div>
  </main>
</body>
</html>
"""
    output_path.write_text(document, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the static CDS dashboard sketch.")
    parser.add_argument("--patients", type=Path, default=DEFAULT_PATIENTS_PATH)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT_PATH)
    parser.add_argument("--dashboard", type=Path, default=DEFAULT_DASHBOARD_PATH)
    parser.add_argument("--size", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260705)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    patients = generate_patients(size=args.size, seed=args.seed)
    selected = sorted(patients, key=lambda row: float(row["risk_score"]), reverse=True)[0]
    audit_events = make_audit_events(selected)

    write_csv(patients, args.patients, PATIENT_FIELDS)
    write_csv(audit_events, args.audit, AUDIT_FIELDS)
    write_dashboard(patients, audit_events, args.dashboard)

    print(f"wrote {len(patients)} synthetic patient-like records to {args.patients}")
    print(f"wrote audit example to {args.audit}")
    print(f"wrote dashboard to {args.dashboard}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
