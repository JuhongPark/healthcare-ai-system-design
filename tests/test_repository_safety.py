from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_check_claims_module():
    path = ROOT / "scripts" / "check_claims.py"
    spec = importlib.util.spec_from_file_location("check_claims", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepositorySafetyTests(unittest.TestCase):
    def test_claim_scanner_passes_current_repository(self) -> None:
        check_claims = load_check_claims_module()

        self.assertEqual(check_claims.main(), 0)


if __name__ == "__main__":
    unittest.main()
