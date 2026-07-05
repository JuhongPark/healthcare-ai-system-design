from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONITORING_DIR = ROOT / "prototypes" / "monitoring-loop-sketch"


def load_monitoring_module():
    path = MONITORING_DIR / "generate_monitoring_report.py"
    spec = importlib.util.spec_from_file_location("monitoring_loop", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


monitoring = load_monitoring_module()


class MonitoringLoopTests(unittest.TestCase):
    def test_stream_generation_is_reproducible(self) -> None:
        first = monitoring.generate_stream(months=4, records_per_month=40, seed=17)
        second = monitoring.generate_stream(months=4, records_per_month=40, seed=17)
        third = monitoring.generate_stream(months=4, records_per_month=40, seed=18)

        self.assertEqual(first, second)
        self.assertNotEqual(first, third)
        self.assertEqual(set(monitoring.STREAM_FIELDS), set(first[0]))

    def test_summary_escalates_late_drift(self) -> None:
        rows = monitoring.generate_stream(months=6, records_per_month=180, seed=20260705)
        summary = monitoring.summarize_stream(rows)

        self.assertEqual(len(summary), 6)
        self.assertEqual(summary[0]["alert_level"], "stable")
        self.assertIn(summary[-1]["alert_level"], {"watch", "review"})
        self.assertGreater(float(summary[-1]["input_shift_index"]), 0.12)

    def test_report_writes_required_safety_labels(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            stream = tmp_path / "stream.csv"
            summary = tmp_path / "summary.csv"
            report = tmp_path / "report.md"

            exit_code = monitoring.main(
                [
                    "--stream",
                    str(stream),
                    "--summary",
                    str(summary),
                    "--report",
                    str(report),
                    "--months",
                    "4",
                    "--records-per-month",
                    "60",
                    "--seed",
                    "20260705",
                ]
            )

            self.assertEqual(exit_code, 0)
            self.assertTrue(stream.exists())
            self.assertTrue(summary.exists())
            text = report.read_text(encoding="utf-8").lower()
            self.assertIn("synthetic data only", text)
            self.assertIn("not medical advice", text)
            self.assertIn("not clinical decision support", text)
            self.assertIn("alert queue", text)


if __name__ == "__main__":
    unittest.main()
