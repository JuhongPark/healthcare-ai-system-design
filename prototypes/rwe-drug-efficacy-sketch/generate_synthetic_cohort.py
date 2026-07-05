"""Generate a synthetic treatment-outcome cohort for the RWE sketch."""

from __future__ import annotations

import argparse
import csv
import math
import random
from pathlib import Path
from typing import Iterable


DEFAULT_OUTPUT = Path(__file__).resolve().parent / "outputs" / "synthetic_cohort.csv"
TRUE_TREATMENT_LOG_ODDS = -0.45

FIELDS = [
    "subject_id",
    "age_years",
    "comorbidity_score",
    "prior_event",
    "frailty_index",
    "treatment",
    "treatment_probability",
    "baseline_outcome_logit",
    "primary_event",
    "followup_days",
    "negative_control_event",
]


def logistic(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def draw_bernoulli(rng: random.Random, probability: float) -> int:
    return 1 if rng.random() < probability else 0


def weighted_choice(rng: random.Random, values: list[tuple[int, float]]) -> int:
    threshold = rng.random() * sum(weight for _, weight in values)
    cumulative = 0.0
    for value, weight in values:
        cumulative += weight
        if threshold <= cumulative:
            return value
    return values[-1][0]


def generate_cohort(
    size: int = 800,
    seed: int = 20260705,
    true_treatment_log_odds: float = TRUE_TREATMENT_LOG_ODDS,
) -> list[dict[str, float | int | str]]:
    if size < 20:
        raise ValueError("size must be at least 20")

    rng = random.Random(seed)
    rows: list[dict[str, float | int | str]] = []

    for index in range(1, size + 1):
        age_years = int(min(90, max(35, rng.gauss(63, 11))))
        comorbidity_score = weighted_choice(
            rng,
            [(0, 0.24), (1, 0.30), (2, 0.24), (3, 0.14), (4, 0.06), (5, 0.02)],
        )
        prior_event_probability = logistic(
            -2.0 + 0.035 * (age_years - 60) + 0.38 * comorbidity_score
        )
        prior_event = draw_bernoulli(rng, prior_event_probability)
        frailty_index = min(
            0.95,
            max(
                0.02,
                0.08
                + 0.0045 * (age_years - 50)
                + 0.055 * comorbidity_score
                + 0.11 * prior_event
                + rng.gauss(0, 0.055),
            ),
        )

        treatment_logit = (
            -0.95
            + 0.018 * (age_years - 60)
            + 0.34 * comorbidity_score
            + 0.58 * prior_event
            + 1.20 * frailty_index
        )
        treatment_probability = logistic(treatment_logit)
        treatment = draw_bernoulli(rng, treatment_probability)

        baseline_outcome_logit = (
            -2.75
            + 0.026 * (age_years - 60)
            + 0.37 * comorbidity_score
            + 0.70 * prior_event
            + 0.88 * frailty_index
        )
        primary_event_probability = logistic(
            baseline_outcome_logit + treatment * true_treatment_log_odds
        )
        primary_event = draw_bernoulli(rng, primary_event_probability)

        if primary_event:
            followup_days = min(180, max(1, int(10 + rng.expovariate(1 / 55))))
        else:
            followup_days = 180

        negative_control_probability = logistic(
            -3.35 + 0.012 * (age_years - 60) + 0.10 * comorbidity_score
        )
        negative_control_event = draw_bernoulli(rng, negative_control_probability)

        rows.append(
            {
                "subject_id": f"SYN-{index:05d}",
                "age_years": age_years,
                "comorbidity_score": comorbidity_score,
                "prior_event": prior_event,
                "frailty_index": round(frailty_index, 4),
                "treatment": treatment,
                "treatment_probability": round(treatment_probability, 4),
                "baseline_outcome_logit": round(baseline_outcome_logit, 5),
                "primary_event": primary_event,
                "followup_days": followup_days,
                "negative_control_event": negative_control_event,
            }
        )

    return rows


def write_cohort(rows: Iterable[dict[str, float | int | str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a synthetic cohort for the RWE prototype."
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--size", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260705)
    parser.add_argument(
        "--true-treatment-log-odds",
        type=float,
        default=TRUE_TREATMENT_LOG_ODDS,
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    rows = generate_cohort(
        size=args.size,
        seed=args.seed,
        true_treatment_log_odds=args.true_treatment_log_odds,
    )
    write_cohort(rows, args.output)
    print(f"wrote {len(rows)} synthetic rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
