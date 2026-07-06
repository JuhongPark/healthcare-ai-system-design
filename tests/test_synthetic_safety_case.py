from __future__ import annotations

import csv
import importlib.util
import re
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "case-studies" / "synthetic-care-program"
RUN_CASE_PATH = CASE_DIR / "run_case.py"

EXPECTED_OUTPUTS = {
    "synthetic_cohort.csv",
    "target_trial_spec.md",
    "evidence_report.md",
    "cds_dashboard.html",
    "workflow_audit_log.csv",
    "monitoring_stream.csv",
    "monitoring_report.md",
    "incidents.csv",
    "governance_decision.md",
    "safety_case.md",
    "evaluation_registry.csv",
}

SAFETY_PHRASES = {
    "synthetic",
    "not medical advice",
    "not clinical decision support",
    "not evidence about real patients",
}

CITATION_ID_RE = re.compile(r"\bE\d{3}\b")


def load_run_case_module():
    spec = importlib.util.spec_from_file_location("synthetic_care_program", RUN_CASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {RUN_CASE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def evidence_ids() -> set[str]:
    with (ROOT / "references" / "evidence-matrix.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        return {row["id"] for row in csv.DictReader(handle)}


class SyntheticSafetyCaseTests(unittest.TestCase):
    def test_run_case_generates_expected_outputs(self) -> None:
        run_case = load_run_case_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            paths = run_case.generate_case(output_dir)
            generated = {path.name for path in paths}

            self.assertEqual(generated, EXPECTED_OUTPUTS)
            for filename in EXPECTED_OUTPUTS:
                with self.subTest(filename=filename):
                    self.assertTrue((output_dir / filename).is_file())

    def test_generated_outputs_keep_safety_language(self) -> None:
        run_case = load_run_case_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            run_case.generate_case(output_dir)

            for filename in [
                "evidence_report.md",
                "cds_dashboard.html",
                "monitoring_report.md",
                "governance_decision.md",
                "safety_case.md",
            ]:
                text = " ".join((output_dir / filename).read_text(encoding="utf-8").lower().split())
                missing = [phrase for phrase in SAFETY_PHRASES if phrase not in text]
                with self.subTest(filename=filename):
                    self.assertEqual(missing, [])

    def test_failure_first_incidents_and_pause_decision(self) -> None:
        run_case = load_run_case_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            run_case.generate_case(output_dir)
            incidents = read_csv(output_dir / "incidents.csv")
            decision_text = (output_dir / "governance_decision.md").read_text(
                encoding="utf-8"
            )
            safety_case = (output_dir / "safety_case.md").read_text(encoding="utf-8")

            self.assertGreaterEqual(len(incidents), 1)
            self.assertIn("Decision: `pause`", decision_text)
            self.assertIn("not ready for deployment", safety_case)

            incident_ids = {row["incident_id"] for row in incidents}
            for incident_id in incident_ids:
                with self.subTest(incident_id=incident_id):
                    self.assertIn(incident_id, decision_text)
                    self.assertIn(incident_id, safety_case)

    def test_governance_decision_references_registry(self) -> None:
        run_case = load_run_case_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            run_case.generate_case(output_dir)
            registry = read_csv(output_dir / "evaluation_registry.csv")
            decision_text = (output_dir / "governance_decision.md").read_text(
                encoding="utf-8"
            )

            evaluation_ids = {row["evaluation_id"] for row in registry}
            for required_id in {"SCP-EV-005", "SCP-EV-006"}:
                with self.subTest(required_id=required_id):
                    self.assertIn(required_id, evaluation_ids)
                    self.assertIn(required_id, decision_text)

    def test_citation_ids_resolve_to_evidence_matrix(self) -> None:
        run_case = load_run_case_module()
        known_ids = evidence_ids()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            run_case.generate_case(output_dir)

            citation_paths = [
                output_dir / "evidence_report.md",
                output_dir / "monitoring_report.md",
                output_dir / "governance_decision.md",
                output_dir / "safety_case.md",
                output_dir / "evaluation_registry.csv",
            ]
            for path in citation_paths:
                text = path.read_text(encoding="utf-8")
                ids = set(CITATION_ID_RE.findall(text))
                with self.subTest(filename=path.name):
                    self.assertGreaterEqual(len(ids), 1)
                    self.assertTrue(ids.issubset(known_ids))

    def test_dashboard_avoids_clinical_action_language(self) -> None:
        run_case = load_run_case_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            run_case.generate_case(output_dir)
            dashboard = (output_dir / "cds_dashboard.html").read_text(
                encoding="utf-8"
            ).lower()

            for phrase in [
                "recommend treatment",
                "start treatment",
                "diagnose",
                "discharge patient",
                "escalate care",
            ]:
                with self.subTest(phrase=phrase):
                    self.assertNotIn(phrase, dashboard)


if __name__ == "__main__":
    unittest.main()
