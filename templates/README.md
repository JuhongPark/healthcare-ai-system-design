# Governance artifact templates

Reusable artifact templates for healthcare AI system design
prototypes.

These templates turn the repository's evidence base into a
repeatable documentation spine. Each prototype should use the
smallest set that matches its design question, while preserving
the safety boundary: synthetic-only, not medical advice, not
clinical decision support, and not evidence about real patients.

## Templates

- `data-card.md` — dataset motivation, composition, generation,
  limits, and permitted uses.
- `model-card.md` — model-like artifact purpose, evaluation,
  limits, and known failure modes.
- `evaluation-registry.csv` — cross-stage evaluation inventory.
- `interface-contract.md` — workflow-facing input, output,
  user, action, and audit boundary.
- `governance-gate-review.md` — release, monitoring, update,
  pause, and retirement decision record.

## Evidence base

- Dataset documentation: E019.
- Model-like artifact documentation: E020.
- Clinical AI reporting and protocol discipline: E005, E006,
  E027.
- Governance and lifecycle accountability: E001, E002, E007,
  E009, E010.
