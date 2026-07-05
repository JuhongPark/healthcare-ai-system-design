"""Scan repository text for safety labels and obvious sensitive content."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".csv", ".html", ".json", ".md", ".py", ".txt", ".yaml", ".yml"}
SKIP_DIRS = {
    ".git",
    ".agents",
    ".claude",
    ".codex",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
}

SECRET_PATTERNS = [
    re.compile(r"(?i)\b(api[_-]?key|secret|password|private[_-]?key)\b\s*[:=]"),
    re.compile(r"(?i)\bbearer\s+[a-z0-9._-]{20,}"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]

PERSONAL_DATA_PATTERNS = [
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    re.compile(r"\b\d{3}[-. ]\d{3}[-. ]\d{4}\b"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
]

REQUIRED_REPORT_PHRASES = [
    "synthetic",
    "not medical advice",
    "not clinical decision support",
]


def iter_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def scan_sensitive_content(paths: list[Path]) -> list[str]:
    findings: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS + PERSONAL_DATA_PATTERNS:
            for match in pattern.finditer(text):
                findings.append(f"{path.relative_to(ROOT)}: suspicious pattern `{match.group(0)}`")
    return findings


def scan_report_labels(root: Path) -> list[str]:
    findings: list[str] = []
    report_paths = list((root / "prototypes").glob("*/outputs/*report*.md"))
    report_paths.extend((root / "prototypes").glob("*/outputs/*dashboard*.html"))
    for path in sorted(report_paths):
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        missing = [phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in text]
        if missing:
            joined = ", ".join(missing)
            findings.append(f"{path.relative_to(ROOT)}: missing required safety phrase(s): {joined}")
    return findings


def main() -> int:
    paths = iter_text_files(ROOT)
    findings = scan_sensitive_content(paths)
    findings.extend(scan_report_labels(ROOT))
    if findings:
        print("claim and sensitive-content check failed")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print(f"claim and sensitive-content check passed for {len(paths)} text files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
