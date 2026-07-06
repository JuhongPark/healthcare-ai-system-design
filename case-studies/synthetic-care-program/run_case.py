"""Generate an executable synthetic healthcare AI safety case."""

from __future__ import annotations

import argparse
import csv
import html
import math
from dataclasses import dataclass
from pathlib import Path


CASE_ID = "SCP-001"
CASE_TITLE = "Synthetic care program safety case"
ARTIFACT_PREFIX = "SCP"
ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = ROOT / "outputs"
SAFETY_BOUNDARY = (
    "This output is synthetic-only. It is not medical advice, not clinical "
    "decision support, and not evidence about real patients or real populations."
)


@dataclass(frozen=True)
class CohortRow:
    subject_id: str
    age: int
    severity: int
    comorbidity: int
    proxy_cost_score: int
    latent_need: int
    treatment: int
    outcome: int
    negative_control: int
    risk_score: float


@dataclass(frozen=True)
class MonitoringRow:
    month: int
    encounter_id: str
    acuity: int
    risk_score: float
    outcome: int
    alert: int


@dataclass(frozen=True)
class Incident:
    incident_id: str
    severity: str
    trigger_metric: str
    observed_value: str
    threshold: str
    suspected_root_cause: str
    required_review: str
    owner: str
    decision: str
    follow_up_date: str
    linked_evaluation_id: str


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def risk_band(score: float) -> str:
    if score >= 0.78:
        return "high"
    if score >= 0.58:
        return "watch"
    return "routine"


def generate_cohort() -> list[CohortRow]:
    rows: list[CohortRow] = []
    for index in range(1, 73):
        age = 42 + (index * 7) % 39
        severity = 1 + (index * 5) % 10
        comorbidity = (index * 3 + 2) % 6
        proxy_cost_score = 2 + (age - 40) // 12 + comorbidity + (index % 3)
        latent_need = severity + comorbidity + (2 if age >= 70 else 0)
        treatment_probability = logistic(-2.1 + 0.23 * severity + 0.18 * comorbidity)
        treatment = int(((index * 37) % 100) / 100 < treatment_probability)
        risk_score = logistic(-3.0 + 0.055 * age + 0.22 * severity + 0.18 * comorbidity)
        outcome_probability = logistic(
            -3.4 + 0.05 * age + 0.31 * severity + 0.22 * comorbidity - 0.34 * treatment
        )
        negative_probability = logistic(-2.5 + 0.07 * age + 0.14 * comorbidity)
        outcome = int(((index * 29 + 11) % 100) / 100 < outcome_probability)
        negative_control = int(((index * 31 + 7) % 100) / 100 < negative_probability)
        rows.append(
            CohortRow(
                subject_id=f"{CASE_ID}-S{index:03d}",
                age=age,
                severity=severity,
                comorbidity=comorbidity,
                proxy_cost_score=proxy_cost_score,
                latent_need=latent_need,
                treatment=treatment,
                outcome=outcome,
                negative_control=negative_control,
                risk_score=round(risk_score, 3),
            )
        )
    return rows


def generate_monitoring_stream() -> list[MonitoringRow]:
    rows: list[MonitoringRow] = []
    for month in range(1, 7):
        for item in range(1, 25):
            index = (month - 1) * 24 + item
            drift = 2 if month >= 5 else 0
            acuity = 1 + ((index * 4 + month) % 8) + drift
            base_score = logistic(-2.9 + 0.33 * acuity + 0.14 * month)
            score = min(0.96, base_score + (0.09 if month >= 5 else 0.0))
            outcome_probability = min(0.92, base_score + (0.17 if month >= 5 else 0.0))
            outcome = int(((index * 17 + month * 5) % 100) / 100 < outcome_probability)
            alert = int(score >= 0.68)
            rows.append(
                MonitoringRow(
                    month=month,
                    encounter_id=f"{CASE_ID}-E{index:03d}",
                    acuity=acuity,
                    risk_score=round(score, 3),
                    outcome=outcome,
                    alert=alert,
                )
            )
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_cohort(path: Path, rows: list[CohortRow]) -> None:
    write_csv(
        path,
        [
            "case_id",
            "subject_id",
            "age",
            "severity",
            "comorbidity",
            "proxy_cost_score",
            "latent_need",
            "treatment",
            "outcome",
            "negative_control",
            "risk_score",
            "risk_band",
        ],
        [
            {
                "case_id": CASE_ID,
                "subject_id": row.subject_id,
                "age": row.age,
                "severity": row.severity,
                "comorbidity": row.comorbidity,
                "proxy_cost_score": row.proxy_cost_score,
                "latent_need": row.latent_need,
                "treatment": row.treatment,
                "outcome": row.outcome,
                "negative_control": row.negative_control,
                "risk_score": f"{row.risk_score:.3f}",
                "risk_band": risk_band(row.risk_score),
            }
            for row in rows
        ],
    )


def write_target_trial(path: Path) -> None:
    path.write_text(
        f"""# Target trial specification

Case ID: `{CASE_ID}`

{SAFETY_BOUNDARY}

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
""",
        encoding="utf-8",
    )


def rate(rows: list[CohortRow], field: str, treatment: int | None = None) -> float:
    selected = rows if treatment is None else [row for row in rows if row.treatment == treatment]
    if not selected:
        return 0.0
    numerator = sum(getattr(row, field) for row in selected)
    return numerator / len(selected)


def write_evidence_report(path: Path, rows: list[CohortRow]) -> None:
    treated = [row for row in rows if row.treatment == 1]
    untreated = [row for row in rows if row.treatment == 0]
    outcome_gap = rate(rows, "outcome", 1) - rate(rows, "outcome", 0)
    negative_gap = rate(rows, "negative_control", 1) - rate(rows, "negative_control", 0)
    mean_treated_severity = sum(row.severity for row in treated) / len(treated)
    mean_untreated_severity = sum(row.severity for row in untreated) / len(untreated)

    path.write_text(
        f"""# Evidence report

Case ID: `{CASE_ID}`

{SAFETY_BOUNDARY}

## Summary

This report is a synthetic evidence-design artifact. It does not
estimate treatment efficacy, does not authorize clinical use, and
does not provide clinical decision support.

## Cohort snapshot

- Synthetic rows: {len(rows)}
- Treated rows: {len(treated)}
- Untreated rows: {len(untreated)}
- Mean severity among treated rows: {mean_treated_severity:.2f}
- Mean severity among untreated rows: {mean_untreated_severity:.2f}

## Association checks

- Treated outcome rate: {rate(rows, "outcome", 1):.3f}
- Untreated outcome rate: {rate(rows, "outcome", 0):.3f}
- Crude outcome-rate difference: {outcome_gap:.3f}
- Negative-control treated rate: {rate(rows, "negative_control", 1):.3f}
- Negative-control untreated rate: {rate(rows, "negative_control", 0):.3f}
- Negative-control rate difference: {negative_gap:.3f}

## Interpretation boundary

The outcome-rate difference is an association in synthetic data.
The target trial specification lists evidence that would be
needed before any causal or deployment claim could be discussed.

## Missing evidence

- Real data provenance and data-quality review.
- Pre-specified causal assumptions and sensitivity analysis.
- Local validation in a real deployment setting.
- Human-factors evaluation of the workflow surface.
- Governance owner approval for any non-synthetic use.

## Evidence references

Primary citation IDs: E008, E011, E012, E013, E014, E027.
""",
        encoding="utf-8",
    )


def write_dashboard(path: Path, rows: list[CohortRow]) -> None:
    display_rows = sorted(rows, key=lambda row: row.risk_score, reverse=True)[:8]
    table_rows = "\n".join(
        f"""<tr>
  <td>{html.escape(row.subject_id)}</td>
  <td>{row.age}</td>
  <td>{row.severity}</td>
  <td>{row.comorbidity}</td>
  <td>{row.risk_score:.3f}</td>
  <td>{html.escape(risk_band(row.risk_score))}</td>
  <td>Workflow hypothesis only</td>
</tr>"""
        for row in display_rows
    )
    path.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(CASE_TITLE)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2rem; color: #17202a; }}
    .banner {{ border: 2px solid #7d3c98; padding: 1rem; margin-bottom: 1rem; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccd1d1; padding: 0.45rem; text-align: left; }}
    th {{ background: #eef2f3; }}
  </style>
</head>
<body>
  <h1>Synthetic care program dashboard</h1>
  <div class="banner">
    <strong>Safety boundary.</strong>
    This dashboard is synthetic-only. It is not medical advice,
    not clinical decision support, and not evidence about real
    patients or real populations.
  </div>
  <p>
    Case ID: <code>{html.escape(CASE_ID)}</code>. This static
    display studies workflow communication, uncertainty, and
    auditability. It must not request diagnosis, treatment,
    triage, escalation, or any patient-specific action.
  </p>
  <h2>Highest synthetic risk rows</h2>
  <table>
    <thead>
      <tr>
        <th>Subject</th>
        <th>Age</th>
        <th>Severity</th>
        <th>Comorbidity</th>
        <th>Risk score</th>
        <th>Risk band</th>
        <th>Allowed interpretation</th>
      </tr>
    </thead>
    <tbody>
{table_rows}
    </tbody>
  </table>
  <h2>Limitations</h2>
  <ul>
    <li>No real patient data or protected health information.</li>
    <li>No local validation, calibration study, or workflow study.</li>
    <li>Risk scores are generated synthetic display values.</li>
  </ul>
</body>
</html>
""",
        encoding="utf-8",
    )


def write_audit_log(path: Path, rows: list[CohortRow]) -> None:
    display_rows = sorted(rows, key=lambda row: row.risk_score, reverse=True)[:4]
    write_csv(
        path,
        [
            "case_id",
            "audit_event_id",
            "subject_id",
            "displayed_risk_band",
            "user_action",
            "reason_captured",
            "safety_boundary",
        ],
        [
            {
                "case_id": CASE_ID,
                "audit_event_id": f"{ARTIFACT_PREFIX}-AUD-{index:03d}",
                "subject_id": row.subject_id,
                "displayed_risk_band": risk_band(row.risk_score),
                "user_action": "reviewed synthetic display",
                "reason_captured": "workflow hypothesis review",
                "safety_boundary": "synthetic only; not medical advice; not clinical decision support",
            }
            for index, row in enumerate(display_rows, start=1)
        ],
    )


def write_monitoring_stream(path: Path, rows: list[MonitoringRow]) -> None:
    write_csv(
        path,
        ["case_id", "month", "encounter_id", "acuity", "risk_score", "outcome", "alert"],
        [
            {
                "case_id": CASE_ID,
                "month": row.month,
                "encounter_id": row.encounter_id,
                "acuity": row.acuity,
                "risk_score": f"{row.risk_score:.3f}",
                "outcome": row.outcome,
                "alert": row.alert,
            }
            for row in rows
        ],
    )


def monthly_summary(rows: list[MonitoringRow]) -> list[dict[str, object]]:
    summaries: list[dict[str, object]] = []
    baseline = [row for row in rows if row.month == 1]
    baseline_acuity = sum(row.acuity for row in baseline) / len(baseline)
    for month in sorted({row.month for row in rows}):
        selected = [row for row in rows if row.month == month]
        mean_acuity = sum(row.acuity for row in selected) / len(selected)
        mean_score = sum(row.risk_score for row in selected) / len(selected)
        outcome_rate = sum(row.outcome for row in selected) / len(selected)
        alert_rate = sum(row.alert for row in selected) / len(selected)
        calibration_gap = outcome_rate - mean_score
        summaries.append(
            {
                "month": month,
                "rows": len(selected),
                "mean_acuity": mean_acuity,
                "mean_score": mean_score,
                "outcome_rate": outcome_rate,
                "alert_rate": alert_rate,
                "shift_index": mean_acuity - baseline_acuity,
                "calibration_gap": calibration_gap,
            }
        )
    return summaries


def write_monitoring_report(path: Path, rows: list[MonitoringRow]) -> None:
    summaries = monthly_summary(rows)
    table = "\n".join(
        "| {month} | {rows} | {mean_acuity:.2f} | {mean_score:.3f} | {outcome_rate:.3f} | {alert_rate:.3f} | {shift_index:.2f} | {calibration_gap:.3f} |".format(
            **summary
        )
        for summary in summaries
    )
    path.write_text(
        f"""# Monitoring report

Case ID: `{CASE_ID}`

{SAFETY_BOUNDARY}

## Summary

This report is a synthetic monitoring artifact. It is not medical
advice, not clinical decision support, and not real-world model
performance evidence.

| Month | Rows | Mean acuity | Mean score | Outcome rate | Alert rate | Shift index | Calibration gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
{table}

## Interpretation boundary

The monitoring stream is generated to make lifecycle review
visible. Metrics are not operating policy. They should be read as
signals for a synthetic governance workflow.

## Evidence references

Primary citation IDs: E001, E002, E003, E009, E010, E027.
""",
        encoding="utf-8",
    )


def write_evaluation_registry(path: Path) -> None:
    write_csv(
        path,
        [
            "prototype",
            "artifact",
            "evaluation_id",
            "stage",
            "data_version",
            "metric_or_check",
            "result",
            "decision",
            "status",
            "owner",
            "citation_ids",
            "notes",
        ],
        [
            {
                "prototype": "synthetic-care-program",
                "artifact": "synthetic-cohort",
                "evaluation_id": "SCP-EV-001",
                "stage": "data-boundary-review",
                "data_version": CASE_ID,
                "metric_or_check": "synthetic safety boundary",
                "result": "present",
                "decision": "continue",
                "status": "complete",
                "owner": "repository",
                "citation_ids": "E007;E019",
                "notes": "No real patient data or clinical-use claim.",
            },
            {
                "prototype": "synthetic-care-program",
                "artifact": "target-trial-spec",
                "evaluation_id": "SCP-EV-002",
                "stage": "evidence-design-review",
                "data_version": CASE_ID,
                "metric_or_check": "association boundary",
                "result": "present",
                "decision": "continue",
                "status": "complete",
                "owner": "repository",
                "citation_ids": "E008;E011;E012",
                "notes": "Causal claims are blocked by missing evidence.",
            },
            {
                "prototype": "synthetic-care-program",
                "artifact": "cds-dashboard",
                "evaluation_id": "SCP-EV-003",
                "stage": "workflow-interface-review",
                "data_version": CASE_ID,
                "metric_or_check": "no clinical recommendation language",
                "result": "present",
                "decision": "continue",
                "status": "complete",
                "owner": "repository",
                "citation_ids": "E015;E016;E017;E027",
                "notes": "Dashboard is labeled as workflow hypothesis only.",
            },
            {
                "prototype": "synthetic-care-program",
                "artifact": "monitoring-report",
                "evaluation_id": "SCP-EV-004",
                "stage": "monitoring-review",
                "data_version": CASE_ID,
                "metric_or_check": "monthly monitoring summary",
                "result": "present",
                "decision": "continue",
                "status": "complete",
                "owner": "repository",
                "citation_ids": "E001;E002;E003;E010",
                "notes": "Monitoring output is synthetic and not operating policy.",
            },
            {
                "prototype": "synthetic-care-program",
                "artifact": "incidents",
                "evaluation_id": "SCP-EV-005",
                "stage": "incident-review",
                "data_version": CASE_ID,
                "metric_or_check": "failure-first incidents",
                "result": "present",
                "decision": "pause",
                "status": "complete",
                "owner": "repository",
                "citation_ids": "E001;E002;E003;E007;E010",
                "notes": "Default run generates incidents for governance review.",
            },
            {
                "prototype": "synthetic-care-program",
                "artifact": "governance-decision",
                "evaluation_id": "SCP-EV-006",
                "stage": "governance-review",
                "data_version": CASE_ID,
                "metric_or_check": "decision references incidents",
                "result": "present",
                "decision": "pause",
                "status": "complete",
                "owner": "repository",
                "citation_ids": "E001;E007;E009;E010;E027",
                "notes": "Governance decision blocks deployment authorization.",
            },
        ],
    )


def negative_control_gap(rows: list[CohortRow]) -> float:
    return rate(rows, "negative_control", 1) - rate(rows, "negative_control", 0)


def proxy_label_warning(rows: list[CohortRow]) -> float:
    mean_need = sum(row.latent_need for row in rows) / len(rows)
    high_proxy = [row for row in rows if row.proxy_cost_score >= 7]
    if not high_proxy:
        return 0.0
    low_need_high_proxy = [row for row in high_proxy if row.latent_need < mean_need]
    return len(low_need_high_proxy) / len(high_proxy)


def generate_incidents(
    cohort: list[CohortRow], monitoring: list[MonitoringRow]
) -> list[Incident]:
    incidents: list[Incident] = []
    summaries = monthly_summary(monitoring)
    max_shift = max(summaries, key=lambda item: abs(float(item["shift_index"])))
    max_calibration = max(summaries, key=lambda item: abs(float(item["calibration_gap"])))
    max_alert = max(summaries, key=lambda item: float(item["alert_rate"]))
    neg_gap = negative_control_gap(cohort)
    proxy_warning = proxy_label_warning(cohort)

    if abs(float(max_shift["shift_index"])) >= 2.5:
        incidents.append(
            Incident(
                incident_id="SCP-INC-001",
                severity="high",
                trigger_metric=f"month {max_shift['month']} shift_index",
                observed_value=f"{float(max_shift['shift_index']):.2f}",
                threshold="2.50",
                suspected_root_cause="synthetic later-period acuity mix shift",
                required_review="review data drift before any deployment claim",
                owner="repository maintainer",
                decision="pause",
                follow_up_date="before next generated release",
                linked_evaluation_id="SCP-EV-004",
            )
        )

    if abs(float(max_calibration["calibration_gap"])) >= 0.075:
        incidents.append(
            Incident(
                incident_id="SCP-INC-002",
                severity="high",
                trigger_metric=f"month {max_calibration['month']} calibration_gap",
                observed_value=f"{float(max_calibration['calibration_gap']):.3f}",
                threshold="0.075",
                suspected_root_cause="synthetic outcome process shifted after baseline",
                required_review="review calibration and outcome lag assumptions",
                owner="repository maintainer",
                decision="pause",
                follow_up_date="before next generated release",
                linked_evaluation_id="SCP-EV-004",
            )
        )

    if float(max_alert["alert_rate"]) >= 0.35:
        incidents.append(
            Incident(
                incident_id="SCP-INC-003",
                severity="medium",
                trigger_metric=f"month {max_alert['month']} alert_rate",
                observed_value=f"{float(max_alert['alert_rate']):.3f}",
                threshold="0.350",
                suspected_root_cause="synthetic risk scores crossed passive display threshold",
                required_review="review workflow burden and alert fatigue risk",
                owner="repository maintainer",
                decision="monitor",
                follow_up_date="before dashboard variant work",
                linked_evaluation_id="SCP-EV-003",
            )
        )

    if abs(neg_gap) >= 0.12:
        incidents.append(
            Incident(
                incident_id="SCP-INC-004",
                severity="medium",
                trigger_metric="negative_control_rate_difference",
                observed_value=f"{neg_gap:.3f}",
                threshold="0.120",
                suspected_root_cause="synthetic imbalance remains visible in negative-control outcome",
                required_review="review confounding and target-trial assumptions",
                owner="repository maintainer",
                decision="update",
                follow_up_date="before RWE target-trial expansion",
                linked_evaluation_id="SCP-EV-002",
            )
        )

    if proxy_warning >= 0.30:
        incidents.append(
            Incident(
                incident_id="SCP-INC-005",
                severity="medium",
                trigger_metric="high_proxy_low_need_share",
                observed_value=f"{proxy_warning:.3f}",
                threshold="0.300",
                suspected_root_cause="synthetic proxy score can diverge from latent need",
                required_review="review proxy-label bias before allocation claims",
                owner="repository maintainer",
                decision="update",
                follow_up_date="before fairness audit prototype",
                linked_evaluation_id="SCP-EV-001",
            )
        )

    return incidents


def write_incidents(path: Path, incidents: list[Incident]) -> None:
    write_csv(
        path,
        [
            "case_id",
            "incident_id",
            "severity",
            "trigger_metric",
            "observed_value",
            "threshold",
            "suspected_root_cause",
            "required_review",
            "owner",
            "decision",
            "follow_up_date",
            "linked_evaluation_id",
        ],
        [
            {
                "case_id": CASE_ID,
                "incident_id": incident.incident_id,
                "severity": incident.severity,
                "trigger_metric": incident.trigger_metric,
                "observed_value": incident.observed_value,
                "threshold": incident.threshold,
                "suspected_root_cause": incident.suspected_root_cause,
                "required_review": incident.required_review,
                "owner": incident.owner,
                "decision": incident.decision,
                "follow_up_date": incident.follow_up_date,
                "linked_evaluation_id": incident.linked_evaluation_id,
            }
            for incident in incidents
        ],
    )


def governance_decision(incidents: list[Incident]) -> str:
    if any(incident.severity == "high" for incident in incidents):
        return "pause"
    if any(incident.decision == "update" for incident in incidents):
        return "update"
    if incidents:
        return "monitor"
    return "continue"


def write_governance_decision(path: Path, incidents: list[Incident]) -> None:
    decision = governance_decision(incidents)
    incident_ids = ", ".join(incident.incident_id for incident in incidents)
    evaluation_ids = ", ".join(
        sorted({incident.linked_evaluation_id for incident in incidents} | {"SCP-EV-005", "SCP-EV-006"})
    )
    high_count = sum(1 for incident in incidents if incident.severity == "high")
    medium_count = sum(1 for incident in incidents if incident.severity == "medium")

    path.write_text(
        f"""# Governance decision

Case ID: `{CASE_ID}`

{SAFETY_BOUNDARY}

## Decision

Decision: `{decision}`

This decision does not authorize deployment, clinical use,
medical advice, or clinical decision support. It records the
synthetic governance response for the case study.

## Evidence reviewed

- Incident artifact: `outputs/incidents.csv`
- Evaluation artifact: `outputs/evaluation_registry.csv`
- Linked incident IDs: {incident_ids}
- Linked evaluation IDs: {evaluation_ids}

## Incident summary

- Total incidents: {len(incidents)}
- High severity incidents: {high_count}
- Medium severity incidents: {medium_count}

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
""",
        encoding="utf-8",
    )


def generate_case(output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    cohort = generate_cohort()
    monitoring = generate_monitoring_stream()
    incidents = generate_incidents(cohort, monitoring)
    paths = {
        "synthetic_cohort": output_dir / "synthetic_cohort.csv",
        "target_trial": output_dir / "target_trial_spec.md",
        "evidence_report": output_dir / "evidence_report.md",
        "dashboard": output_dir / "cds_dashboard.html",
        "audit_log": output_dir / "workflow_audit_log.csv",
        "monitoring_stream": output_dir / "monitoring_stream.csv",
        "monitoring_report": output_dir / "monitoring_report.md",
        "incidents": output_dir / "incidents.csv",
        "governance_decision": output_dir / "governance_decision.md",
        "evaluation_registry": output_dir / "evaluation_registry.csv",
    }
    write_cohort(paths["synthetic_cohort"], cohort)
    write_target_trial(paths["target_trial"])
    write_evidence_report(paths["evidence_report"], cohort)
    write_dashboard(paths["dashboard"], cohort)
    write_audit_log(paths["audit_log"], cohort)
    write_monitoring_stream(paths["monitoring_stream"], monitoring)
    write_monitoring_report(paths["monitoring_report"], monitoring)
    write_incidents(paths["incidents"], incidents)
    write_governance_decision(paths["governance_decision"], incidents)
    write_evaluation_registry(paths["evaluation_registry"])
    return list(paths.values())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for generated case outputs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = generate_case(args.output_dir)
    print(f"generated {len(paths)} synthetic safety-case artifact(s)")
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
