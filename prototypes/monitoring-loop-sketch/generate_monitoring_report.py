"""Generate a synthetic monitoring loop report."""

from __future__ import annotations

import argparse
import csv
import math
import random
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
DEFAULT_STREAM_PATH = HERE / "outputs" / "synthetic_stream.csv"
DEFAULT_SUMMARY_PATH = HERE / "outputs" / "example_monitoring_summary.csv"
DEFAULT_REPORT_PATH = HERE / "outputs" / "example_monitoring_report.md"

STREAM_FIELDS = [
    "record_id",
    "month",
    "age_signal",
    "acuity_signal",
    "missingness_signal",
    "prediction",
    "synthetic_outcome",
]

SUMMARY_FIELDS = [
    "month",
    "records",
    "mean_age_signal",
    "mean_acuity_signal",
    "missingness_rate",
    "mean_prediction",
    "outcome_rate",
    "brier_score",
    "calibration_error",
    "input_shift_index",
    "alert_level",
    "action_hint",
]


def logistic(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def draw_bernoulli(rng: random.Random, probability: float) -> int:
    return 1 if rng.random() < probability else 0


def generate_stream(
    months: int = 6,
    records_per_month: int = 180,
    seed: int = 20260705,
) -> list[dict[str, str]]:
    if months < 3:
        raise ValueError("months must be at least 3")
    if records_per_month < 30:
        raise ValueError("records_per_month must be at least 30")

    rng = random.Random(seed)
    rows: list[dict[str, str]] = []
    record_index = 1

    for month in range(1, months + 1):
        drift = max(0, month - 3)
        for _ in range(records_per_month):
            age_signal = min(1.0, max(0.0, rng.gauss(0.48 + 0.035 * drift, 0.17)))
            acuity_signal = min(1.0, max(0.0, rng.gauss(0.38 + 0.075 * drift, 0.18)))
            missingness_probability = min(0.38, 0.09 + 0.045 * drift)
            missingness_signal = draw_bernoulli(rng, missingness_probability)

            prediction = logistic(
                -2.15
                + 1.45 * age_signal
                + 1.95 * acuity_signal
                + 0.45 * missingness_signal
            )
            outcome_logit = (
                -2.28
                + 1.55 * age_signal
                + 2.10 * acuity_signal
                + 0.55 * missingness_signal
                + 0.20 * drift
            )
            synthetic_outcome = draw_bernoulli(rng, logistic(outcome_logit))

            rows.append(
                {
                    "record_id": f"SYN-MON-{record_index:05d}",
                    "month": str(month),
                    "age_signal": f"{age_signal:.4f}",
                    "acuity_signal": f"{acuity_signal:.4f}",
                    "missingness_signal": str(missingness_signal),
                    "prediction": f"{prediction:.4f}",
                    "synthetic_outcome": str(synthetic_outcome),
                }
            )
            record_index += 1

    return rows


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def group_by_month(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["month"], []).append(row)
    return grouped


def month_metrics(rows: list[dict[str, str]]) -> dict[str, float]:
    age_values = [float(row["age_signal"]) for row in rows]
    acuity_values = [float(row["acuity_signal"]) for row in rows]
    missing_values = [float(row["missingness_signal"]) for row in rows]
    predictions = [float(row["prediction"]) for row in rows]
    outcomes = [float(row["synthetic_outcome"]) for row in rows]
    brier = mean([(prediction - outcome) ** 2 for prediction, outcome in zip(predictions, outcomes)])

    return {
        "records": float(len(rows)),
        "mean_age_signal": mean(age_values),
        "mean_acuity_signal": mean(acuity_values),
        "missingness_rate": mean(missing_values),
        "mean_prediction": mean(predictions),
        "outcome_rate": mean(outcomes),
        "brier_score": brier,
        "calibration_error": abs(mean(predictions) - mean(outcomes)),
    }


def alert_level(input_shift: float, calibration_error: float, brier_score: float) -> str:
    if input_shift >= 0.20 or calibration_error >= 0.12 or brier_score >= 0.27:
        return "review"
    if input_shift >= 0.12 or calibration_error >= 0.07 or brier_score >= 0.24:
        return "watch"
    return "stable"


def action_hint(level: str) -> str:
    if level == "review":
        return "Open owner review before further model updates."
    if level == "watch":
        return "Increase monitoring cadence and inspect recent data changes."
    return "Continue routine monthly monitoring."


def summarize_stream(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped = group_by_month(rows)
    baseline = month_metrics(grouped[min(grouped, key=int)])
    summary_rows: list[dict[str, str]] = []

    for month in sorted(grouped, key=int):
        metrics = month_metrics(grouped[month])
        input_shift = (
            abs(metrics["mean_age_signal"] - baseline["mean_age_signal"])
            + abs(metrics["mean_acuity_signal"] - baseline["mean_acuity_signal"])
            + abs(metrics["missingness_rate"] - baseline["missingness_rate"])
        )
        level = alert_level(input_shift, metrics["calibration_error"], metrics["brier_score"])
        summary_rows.append(
            {
                "month": month,
                "records": f"{int(metrics['records'])}",
                "mean_age_signal": f"{metrics['mean_age_signal']:.4f}",
                "mean_acuity_signal": f"{metrics['mean_acuity_signal']:.4f}",
                "missingness_rate": f"{metrics['missingness_rate']:.4f}",
                "mean_prediction": f"{metrics['mean_prediction']:.4f}",
                "outcome_rate": f"{metrics['outcome_rate']:.4f}",
                "brier_score": f"{metrics['brier_score']:.4f}",
                "calibration_error": f"{metrics['calibration_error']:.4f}",
                "input_shift_index": f"{input_shift:.4f}",
                "alert_level": level,
                "action_hint": action_hint(level),
            }
        )

    return summary_rows


def write_csv(
    rows: Iterable[dict[str, str]], output_path: Path, fieldnames: list[str]
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, str]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    lines = [header, separator]
    for row in rows:
        lines.append("| " + " | ".join(row[column] for column in columns) + " |")
    return "\n".join(lines)


def write_report(summary_rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    alert_rows = [row for row in summary_rows if row["alert_level"] != "stable"]
    alert_text = (
        "No watch or review months were generated."
        if not alert_rows
        else markdown_table(alert_rows, ["month", "alert_level", "input_shift_index", "calibration_error", "action_hint"])
    )
    content = "\n".join(
        [
            "# Synthetic monitoring loop report",
            "",
            "Generated by `generate_monitoring_report.py` from synthetic data only.",
            "",
            "## Safety label",
            "",
            "This report is not medical advice, not clinical decision support, "
            "not a validated monitoring policy, and not evidence about real patients.",
            "",
            "## Monthly summary",
            "",
            markdown_table(
                summary_rows,
                [
                    "month",
                    "records",
                    "mean_prediction",
                    "outcome_rate",
                    "brier_score",
                    "calibration_error",
                    "input_shift_index",
                    "alert_level",
                ],
            ),
            "",
            "## Alert queue",
            "",
            alert_text,
            "",
            "## Monitoring interpretation",
            "",
            "- `input_shift_index` compares monthly age, acuity, and missingness "
            "signals with the baseline month.",
            "- `calibration_error` is the absolute difference between mean "
            "prediction and observed synthetic outcome rate for the month.",
            "- Alert levels are illustrative operating signals, not deployment "
            "policy.",
            "",
            "## Limitations",
            "",
            "- The stream is simulated and contains no real patient records.",
            "- Delayed outcomes are generated, so monitoring behavior is a "
            "controlled demonstration.",
            "- A review alert says that an owner should inspect the system. It "
            "does not identify root cause by itself.",
            "",
        ]
    )
    output_path.write_text(content, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the synthetic monitoring loop report.")
    parser.add_argument("--stream", type=Path, default=DEFAULT_STREAM_PATH)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--months", type=int, default=6)
    parser.add_argument("--records-per-month", type=int, default=180)
    parser.add_argument("--seed", type=int, default=20260705)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    stream_rows = generate_stream(
        months=args.months,
        records_per_month=args.records_per_month,
        seed=args.seed,
    )
    summary_rows = summarize_stream(stream_rows)
    write_csv(stream_rows, args.stream, STREAM_FIELDS)
    write_csv(summary_rows, args.summary, SUMMARY_FIELDS)
    write_report(summary_rows, args.report)
    print(f"wrote {len(stream_rows)} synthetic monitoring records to {args.stream}")
    print(f"wrote monitoring summary to {args.summary}")
    print(f"wrote monitoring report to {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
