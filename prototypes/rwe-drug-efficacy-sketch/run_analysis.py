"""Run the synthetic RWE analysis sketch."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

from generate_synthetic_cohort import (
    DEFAULT_OUTPUT as DEFAULT_COHORT_PATH,
    TRUE_TREATMENT_LOG_ODDS,
    generate_cohort,
    logistic,
    write_cohort,
)


HERE = Path(__file__).resolve().parent
DEFAULT_SUMMARY_PATH = HERE / "outputs" / "example_summary.csv"
DEFAULT_REPORT_PATH = HERE / "outputs" / "example_report.md"
COVARIATES = ["age_years", "comorbidity_score", "prior_event", "frailty_index"]


def read_cohort(path: Path) -> list[dict[str, float | str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows: list[dict[str, float | str]] = []
        for row in reader:
            rows.append(
                {
                    "subject_id": row["subject_id"],
                    "age_years": float(row["age_years"]),
                    "comorbidity_score": float(row["comorbidity_score"]),
                    "prior_event": float(row["prior_event"]),
                    "frailty_index": float(row["frailty_index"]),
                    "treatment": float(row["treatment"]),
                    "treatment_probability": float(row["treatment_probability"]),
                    "baseline_outcome_logit": float(row["baseline_outcome_logit"]),
                    "primary_event": float(row["primary_event"]),
                    "followup_days": float(row["followup_days"]),
                    "negative_control_event": float(row["negative_control_event"]),
                }
            )
    return rows


def dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def standardized_matrix(
    rows: list[dict[str, float | str]], covariates: list[str]
) -> list[list[float]]:
    means = {
        covariate: sum(float(row[covariate]) for row in rows) / len(rows)
        for covariate in covariates
    }
    stds: dict[str, float] = {}
    for covariate in covariates:
        variance = (
            sum((float(row[covariate]) - means[covariate]) ** 2 for row in rows)
            / len(rows)
        )
        stds[covariate] = math.sqrt(variance) or 1.0

    return [
        [1.0]
        + [
            (float(row[covariate]) - means[covariate]) / stds[covariate]
            for covariate in covariates
        ]
        for row in rows
    ]


def fit_propensity_scores(
    rows: list[dict[str, float | str]],
    iterations: int = 2400,
    learning_rate: float = 0.05,
    l2_penalty: float = 0.015,
) -> list[float]:
    matrix = standardized_matrix(rows, COVARIATES)
    labels = [float(row["treatment"]) for row in rows]
    beta = [0.0 for _ in matrix[0]]

    for _ in range(iterations):
        gradient = [0.0 for _ in beta]
        for features, label in zip(matrix, labels):
            prediction = logistic(dot(beta, features))
            error = prediction - label
            for index, value in enumerate(features):
                gradient[index] += error * value
        for index in range(len(beta)):
            regularization = 0.0 if index == 0 else l2_penalty * beta[index]
            beta[index] -= learning_rate * (gradient[index] / len(rows) + regularization)

    return [min(0.97, max(0.03, logistic(dot(beta, features)))) for features in matrix]


def weighted_mean(values: list[float], weights: list[float]) -> float:
    return sum(value * weight for value, weight in zip(values, weights)) / sum(weights)


def weighted_variance(values: list[float], weights: list[float]) -> float:
    mean = weighted_mean(values, weights)
    return sum(weight * (value - mean) ** 2 for value, weight in zip(values, weights)) / sum(
        weights
    )


def group_weights(
    rows: list[dict[str, float | str]],
    treatment_value: float,
    weights: list[float] | None = None,
) -> list[float]:
    if weights is None:
        weights = [1.0 for _ in rows]
    return [
        weight
        for row, weight in zip(rows, weights)
        if float(row["treatment"]) == treatment_value
    ]


def group_values(
    rows: list[dict[str, float | str]], treatment_value: float, column: str
) -> list[float]:
    return [
        float(row[column])
        for row in rows
        if float(row["treatment"]) == treatment_value
    ]


def risk_difference(
    rows: list[dict[str, float | str]],
    outcome: str,
    weights: list[float] | None = None,
) -> float:
    treated_values = group_values(rows, 1.0, outcome)
    control_values = group_values(rows, 0.0, outcome)
    treated_weights = group_weights(rows, 1.0, weights)
    control_weights = group_weights(rows, 0.0, weights)
    return weighted_mean(treated_values, treated_weights) - weighted_mean(
        control_values, control_weights
    )


def odds_ratio(
    rows: list[dict[str, float | str]], outcome: str, weights: list[float] | None = None
) -> float:
    if weights is None:
        weights = [1.0 for _ in rows]
    cells = {"a": 0.5, "b": 0.5, "c": 0.5, "d": 0.5}
    for row, weight in zip(rows, weights):
        treatment = float(row["treatment"])
        event = float(row[outcome])
        if treatment == 1.0 and event == 1.0:
            cells["a"] += weight
        elif treatment == 1.0:
            cells["b"] += weight
        elif event == 1.0:
            cells["c"] += weight
        else:
            cells["d"] += weight
    return (cells["a"] * cells["d"]) / (cells["b"] * cells["c"])


def standardized_mean_difference(
    rows: list[dict[str, float | str]],
    covariate: str,
    weights: list[float] | None = None,
) -> float:
    treated_values = group_values(rows, 1.0, covariate)
    control_values = group_values(rows, 0.0, covariate)
    treated_weights = group_weights(rows, 1.0, weights)
    control_weights = group_weights(rows, 0.0, weights)
    treated_mean = weighted_mean(treated_values, treated_weights)
    control_mean = weighted_mean(control_values, control_weights)
    treated_variance = weighted_variance(treated_values, treated_weights)
    control_variance = weighted_variance(control_values, control_weights)
    pooled = math.sqrt((treated_variance + control_variance) / 2.0) or 1.0
    return (treated_mean - control_mean) / pooled


def effective_sample_size(weights: list[float]) -> float:
    return sum(weights) ** 2 / sum(weight**2 for weight in weights)


def stabilized_ipw(rows: list[dict[str, float | str]], scores: list[float]) -> list[float]:
    treatment_prevalence = sum(float(row["treatment"]) for row in rows) / len(rows)
    weights = []
    for row, score in zip(rows, scores):
        if float(row["treatment"]) == 1.0:
            weights.append(treatment_prevalence / score)
        else:
            weights.append((1.0 - treatment_prevalence) / (1.0 - score))
    return weights


def oracle_true_risk_difference(rows: list[dict[str, float | str]]) -> float:
    treated = [
        logistic(float(row["baseline_outcome_logit"]) + TRUE_TREATMENT_LOG_ODDS)
        for row in rows
    ]
    control = [logistic(float(row["baseline_outcome_logit"])) for row in rows]
    unit_weights = [1.0 for _ in rows]
    return weighted_mean(treated, unit_weights) - weighted_mean(control, unit_weights)


def summarize(rows: list[dict[str, float | str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    scores = fit_propensity_scores(rows)
    weights = stabilized_ipw(rows, scores)

    balance_rows = []
    for covariate in COVARIATES:
        before = standardized_mean_difference(rows, covariate)
        after = standardized_mean_difference(rows, covariate, weights)
        balance_rows.append(
            {
                "covariate": covariate,
                "smd_before": f"{before:.4f}",
                "smd_after": f"{after:.4f}",
            }
        )

    max_before = max(abs(float(row["smd_before"])) for row in balance_rows)
    max_after = max(abs(float(row["smd_after"])) for row in balance_rows)
    treatment_prevalence = sum(float(row["treatment"]) for row in rows) / len(rows)

    summary_rows = [
        {
            "analysis": "cohort",
            "estimand": "synthetic rows",
            "value": f"{len(rows)}",
            "interpretation": "Number of synthetic records analyzed.",
        },
        {
            "analysis": "cohort",
            "estimand": "treatment prevalence",
            "value": f"{treatment_prevalence:.4f}",
            "interpretation": "Fraction assigned to synthetic treatment.",
        },
        {
            "analysis": "known truth",
            "estimand": "true treatment log odds",
            "value": f"{TRUE_TREATMENT_LOG_ODDS:.4f}",
            "interpretation": "Protective effect encoded in the generator.",
        },
        {
            "analysis": "known truth",
            "estimand": "oracle primary risk difference",
            "value": f"{oracle_true_risk_difference(rows):.4f}",
            "interpretation": "Average synthetic risk difference if treatment were set by intervention.",
        },
        {
            "analysis": "crude",
            "estimand": "primary risk difference",
            "value": f"{risk_difference(rows, 'primary_event'):.4f}",
            "interpretation": "Unadjusted association, confounded by design.",
        },
        {
            "analysis": "ipw adjusted",
            "estimand": "primary risk difference",
            "value": f"{risk_difference(rows, 'primary_event', weights):.4f}",
            "interpretation": "Association after estimated propensity weighting.",
        },
        {
            "analysis": "crude",
            "estimand": "primary odds ratio",
            "value": f"{odds_ratio(rows, 'primary_event'):.4f}",
            "interpretation": "Unadjusted event odds ratio.",
        },
        {
            "analysis": "ipw adjusted",
            "estimand": "effective sample size",
            "value": f"{effective_sample_size(weights):.1f}",
            "interpretation": "Weight stability diagnostic for the adjusted analysis.",
        },
        {
            "analysis": "balance",
            "estimand": "max absolute SMD before weighting",
            "value": f"{max_before:.4f}",
            "interpretation": "Largest observed covariate imbalance before weighting.",
        },
        {
            "analysis": "balance",
            "estimand": "max absolute SMD after weighting",
            "value": f"{max_after:.4f}",
            "interpretation": "Largest observed covariate imbalance after weighting.",
        },
        {
            "analysis": "negative control",
            "estimand": "crude risk difference",
            "value": f"{risk_difference(rows, 'negative_control_event'):.4f}",
            "interpretation": "Residual association for an outcome with no treatment effect in the generator.",
        },
        {
            "analysis": "negative control",
            "estimand": "ipw risk difference",
            "value": f"{risk_difference(rows, 'negative_control_event', weights):.4f}",
            "interpretation": "Weighted residual association for the negative-control outcome.",
        },
    ]
    return summary_rows, balance_rows


def write_summary(summary_rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["analysis", "estimand", "value", "interpretation"])
        writer.writeheader()
        writer.writerows(summary_rows)


def markdown_table(rows: list[dict[str, str]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    lines = [header, separator]
    for row in rows:
        lines.append("| " + " | ".join(row[column] for column in columns) + " |")
    return "\n".join(lines)


def write_report(
    summary_rows: list[dict[str, str]],
    balance_rows: list[dict[str, str]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(
        [
            "# RWE synthetic analysis report",
            "",
            "Generated by `run_analysis.py` from synthetic data only.",
            "",
            "## Safety label",
            "",
            "This report is not medical advice, not clinical decision support, "
            "and not evidence about real patients. It is a research sketch for "
            "showing method behavior when the data-generating process is known.",
            "",
            "## Summary",
            "",
            markdown_table(summary_rows, ["analysis", "estimand", "value", "interpretation"]),
            "",
            "## Balance diagnostics",
            "",
            markdown_table(balance_rows, ["covariate", "smd_before", "smd_after"]),
            "",
            "## Known data-generating process",
            "",
            "- Treatment assignment depends on age, comorbidity score, prior event, "
            "and frailty index.",
            "- Primary outcome risk depends on the same confounders plus the "
            f"encoded treatment log odds of {TRUE_TREATMENT_LOG_ODDS:.2f}.",
            "- The negative-control outcome has no encoded treatment effect.",
            "",
            "## Limitations",
            "",
            "- All estimates are associations unless an explicit causal argument is "
            "made outside this report.",
            "- The propensity model is intentionally small and fit only to observed "
            "synthetic covariates.",
            "- Good behavior on this generator does not imply good behavior on real "
            "healthcare data.",
            "",
        ]
    )
    output_path.write_text(content, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the synthetic RWE analysis.")
    parser.add_argument("--cohort", type=Path, default=DEFAULT_COHORT_PATH)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--size", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260705)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.cohort.exists():
        rows_for_write = generate_cohort(size=args.size, seed=args.seed)
        write_cohort(rows_for_write, args.cohort)

    rows = read_cohort(args.cohort)
    summary_rows, balance_rows = summarize(rows)
    write_summary(summary_rows, args.summary)
    write_report(summary_rows, balance_rows, args.report)
    print(f"analyzed {len(rows)} synthetic rows")
    print(f"wrote summary to {args.summary}")
    print(f"wrote report to {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
