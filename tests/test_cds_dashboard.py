from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CDS_DIR = ROOT / "prototypes" / "cds-risk-dashboard"


def load_dashboard_module():
    path = CDS_DIR / "generate_dashboard.py"
    spec = importlib.util.spec_from_file_location("cds_dashboard", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dashboard = load_dashboard_module()


class CdsDashboardTests(unittest.TestCase):
    def test_patient_generation_is_reproducible(self) -> None:
        first = dashboard.generate_patients(size=6, seed=99)
        second = dashboard.generate_patients(size=6, seed=99)
        third = dashboard.generate_patients(size=6, seed=100)

        self.assertEqual(first, second)
        self.assertNotEqual(first, third)
        self.assertEqual(set(dashboard.PATIENT_FIELDS), set(first[0]))

    def test_dashboard_output_contains_required_workflow_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            patients = tmp_path / "patients.csv"
            audit = tmp_path / "audit.csv"
            html = tmp_path / "dashboard.html"

            exit_code = dashboard.main(
                [
                    "--patients",
                    str(patients),
                    "--audit",
                    str(audit),
                    "--dashboard",
                    str(html),
                    "--size",
                    "6",
                    "--seed",
                    "20260705",
                ]
            )

            self.assertEqual(exit_code, 0)
            self.assertTrue(patients.exists())
            self.assertTrue(audit.exists())
            text = html.read_text(encoding="utf-8").lower()
            self.assertIn("synthetic patient-like records only", text)
            self.assertIn("not medical advice", text)
            self.assertIn("not clinical decision support", text)
            self.assertIn("override capture", text)
            self.assertIn("minimum audit trail", text)


if __name__ == "__main__":
    unittest.main()
