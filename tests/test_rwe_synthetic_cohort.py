from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RWE_DIR = ROOT / "prototypes" / "rwe-drug-efficacy-sketch"


def load_module(name: str, path: Path):
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


generator = load_module("rwe_generator", RWE_DIR / "generate_synthetic_cohort.py")
analysis = load_module("rwe_analysis", RWE_DIR / "run_analysis.py")


class SyntheticCohortTests(unittest.TestCase):
    def test_generator_is_reproducible(self) -> None:
        first = generator.generate_cohort(size=60, seed=1234)
        second = generator.generate_cohort(size=60, seed=1234)
        third = generator.generate_cohort(size=60, seed=1235)

        self.assertEqual(first, second)
        self.assertNotEqual(first, third)

    def test_generated_rows_have_required_columns(self) -> None:
        rows = generator.generate_cohort(size=40, seed=20260705)

        self.assertEqual(set(generator.FIELDS), set(rows[0]))
        self.assertEqual(len(rows), 40)
        self.assertTrue(all(row["subject_id"].startswith("SYN-") for row in rows))
        self.assertTrue(all(row["treatment"] in {0, 1} for row in rows))
        self.assertTrue(all(row["primary_event"] in {0, 1} for row in rows))

    def test_weighting_improves_balance_for_default_seed(self) -> None:
        rows = generator.generate_cohort(size=800, seed=20260705)
        summary_rows, _ = analysis.summarize(rows)
        values = {row["estimand"]: float(row["value"]) for row in summary_rows}

        self.assertGreater(values["max absolute SMD before weighting"], 0.20)
        self.assertLess(values["max absolute SMD after weighting"], 0.10)
        self.assertLess(
            abs(values["primary risk difference"] - values["oracle primary risk difference"]),
            0.08,
        )

    def test_analysis_writes_safety_labeled_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            cohort = tmp_path / "cohort.csv"
            summary = tmp_path / "summary.csv"
            report = tmp_path / "report.md"

            exit_code = analysis.main(
                [
                    "--cohort",
                    str(cohort),
                    "--summary",
                    str(summary),
                    "--report",
                    str(report),
                    "--size",
                    "120",
                    "--seed",
                    "20260705",
                ]
            )

            self.assertEqual(exit_code, 0)
            self.assertTrue(cohort.exists())
            self.assertTrue(summary.exists())
            report_text = report.read_text(encoding="utf-8").lower()
            self.assertIn("synthetic data only", report_text)
            self.assertIn("not medical advice", report_text)
            self.assertIn("not clinical decision support", report_text)


if __name__ == "__main__":
    unittest.main()
