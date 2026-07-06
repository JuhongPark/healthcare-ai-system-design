from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TEMPLATE_FILES = {
    "README.md",
    "data-card.md",
    "model-card.md",
    "evaluation-registry.csv",
    "interface-contract.md",
    "governance-gate-review.md",
}

PROTOTYPE_ARTIFACTS = {
    "rwe-drug-efficacy-sketch": {
        "data-card.md",
        "model-card.md",
        "evaluation-registry.csv",
    },
    "cds-risk-dashboard": {
        "data-card.md",
        "interface-contract.md",
        "governance-gate-review.md",
        "evaluation-registry.csv",
    },
    "monitoring-loop-sketch": {
        "data-card.md",
        "model-card.md",
        "governance-gate-review.md",
        "evaluation-registry.csv",
    },
}

REQUIRED_REGISTRY_COLUMNS = {
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
}

REQUIRED_MARKDOWN_PHRASES = {
    "synthetic",
    "medical advice",
    "clinical decision support",
    "intended",
    "limitation",
}

CITATION_ID_RE = re.compile(r"\bE\d{3}\b")


def evidence_ids() -> set[str]:
    matrix_path = ROOT / "references" / "evidence-matrix.csv"
    with matrix_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {row["id"] for row in reader}


class GovernanceArtifactTests(unittest.TestCase):
    def test_templates_exist(self) -> None:
        templates_dir = ROOT / "templates"

        for filename in TEMPLATE_FILES:
            with self.subTest(filename=filename):
                self.assertTrue((templates_dir / filename).is_file())

    def test_prototype_artifacts_exist(self) -> None:
        for prototype, filenames in PROTOTYPE_ARTIFACTS.items():
            artifact_dir = ROOT / "prototypes" / prototype / "artifacts"
            with self.subTest(prototype=prototype):
                self.assertTrue(artifact_dir.is_dir())

            for filename in filenames:
                with self.subTest(prototype=prototype, filename=filename):
                    self.assertTrue((artifact_dir / filename).is_file())

    def test_markdown_artifacts_keep_safety_language(self) -> None:
        markdown_paths = [
            path
            for path in (ROOT / "templates").glob("*.md")
            if path.name != "README.md"
        ]
        for artifact_dir in (ROOT / "prototypes").glob("*/artifacts"):
            markdown_paths.extend(artifact_dir.glob("*.md"))

        for path in sorted(markdown_paths):
            text = " ".join(path.read_text(encoding="utf-8").lower().split())
            missing = [
                phrase for phrase in REQUIRED_MARKDOWN_PHRASES if phrase not in text
            ]
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(missing, [])

    def test_evaluation_registries_have_required_columns(self) -> None:
        registry_paths = [ROOT / "templates" / "evaluation-registry.csv"]
        registry_paths.extend((ROOT / "prototypes").glob("*/artifacts/evaluation-registry.csv"))

        for path in sorted(registry_paths):
            with path.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                columns = set(reader.fieldnames or [])
                rows = list(reader)

            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(REQUIRED_REGISTRY_COLUMNS.issubset(columns))
                self.assertGreaterEqual(len(rows), 1)

    def test_citation_ids_resolve_to_evidence_matrix(self) -> None:
        known_ids = evidence_ids()
        artifact_paths = list((ROOT / "templates").glob("*"))
        for artifact_dir in (ROOT / "prototypes").glob("*/artifacts"):
            artifact_paths.extend(path for path in artifact_dir.glob("*") if path.is_file())

        for path in sorted(artifact_paths):
            text = path.read_text(encoding="utf-8")
            ids = set(CITATION_ID_RE.findall(text))
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertGreaterEqual(len(ids), 1)
                self.assertTrue(ids.issubset(known_ids))


if __name__ == "__main__":
    unittest.main()
