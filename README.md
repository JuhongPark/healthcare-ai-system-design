# Healthcare AI System Design

Research on how AI and data systems can be designed, evaluated,
and deployed in healthcare workflows.

## Repository purpose

This repository is a research and prototyping workspace for
healthcare AI system design. The unit of analysis is the full
system: data, model, workflow, interface, monitoring,
governance, and organizational ownership.

The repository does not contain clinical tools, medical advice,
protected health information, private patient data, or validated
decision-support products. Prototypes use synthetic, simulated,
or public data only.

## Tracks

- Drug efficacy evaluation with real-world evidence —
  observational data, comparative effectiveness, association vs.
  causation
- Pharmacoepidemiology methodology — active comparator new-user
  designs, target trial emulation, signal detection, distributed
  data networks
- Precision medicine and multimodal healthcare data — integrating
  clinical, genomic, imaging, and behavioral signals
- Clinical decision support with deployment-aware AI and workflow
  integration — uncertainty communication, fit to existing care
  processes
- Monitoring, governance, and safety — post-deployment dataset
  shift, auditability, local validation
- Hospital systems design — information systems,
  interoperability, operations, hospital-scale AI integration
  and governance
- Drug design and discovery — AI for target identification,
  molecular generation and property prediction, structure-based
  design, repurposing
- ADMET and preclinical safety — in-silico toxicity and ADMET
  prediction, applicability domain, development-candidate gate
  evidence
- Clinical pharmacology and model-informed drug development —
  PK/PD, exposure-response, MIDD framing for regulatory evidence
- AI for clinical trial design and operations — recruitment,
  site selection, external comparator arms, adaptive and
  platform designs, digital endpoints
- Pharma AI program case studies — reading AI-enabled discovery
  and development programs for systems lessons
- AI systems architecture — reference architectures, interface
  contracts, multi-model orchestration patterns, and the
  pharma R&D specialization
- AI lifecycle and regulated MLOps — V-model, stage gates,
  predetermined change control, GLP/GCP/GMP integration, MIDD
  documentation discipline
- Human-AI interaction — interaction patterns for clinicians,
  medicinal chemists, pharmacologists, and reviewers
- AI evaluation strategy — evaluation as an architectural
  concern, slice-based evaluation, evaluation registry,
  benchmark hygiene
- Pharma AI system of systems — cross-stage integration
  spanning discovery, preclinical, clinical development,
  manufacturing, and pharmacovigilance

## Main materials

- `docs/research-agenda.md` — the seven-track research agenda
  and near-term prototype queue.
- `docs/evidence-base.md` — literature-backed synthesis of why
  the repository treats healthcare AI as a system-design problem.
- `docs/research-gaps.md` — evidence-based gaps and next
  development sequence.
- `docs/major-improvement-milestones.md` — flagship improvement
  plan for turning the repository into an executable synthetic
  healthcare AI safety-case framework.
- `docs/literature-map.md` — verified reading areas organized
  by topic.
- `references/reading-list.md` — citation-oriented reading
  list and short relevance notes.
- `references/evidence-matrix.csv` — source-by-source claim and
  design-implication map.
- `templates/` — reusable data-card, model-card, interface,
  evaluation-registry, and governance gate artifacts.
- `docs/system-design-framework.md` — a reusable design
  question framework for healthcare AI systems.
- `prototypes/` — executable or planned sketches that make
  selected design questions concrete.

## Current prototype priorities

1. Synthetic real-world-evidence analysis for treatment-outcome
   questions. Implemented in `prototypes/rwe-drug-efficacy-sketch/`.
2. Workflow-aware clinical decision support dashboard sketch on
   synthetic patient-like records. Implemented in
   `prototypes/cds-risk-dashboard/`.
3. Synthetic monitoring loop for drift, calibration, and
   governance questions. Implemented in
   `prototypes/monitoring-loop-sketch/`.

Each prototype is a research sketch. Outputs illustrate method
behavior and system-design trade-offs; they do not support
claims about real patients or real populations.

## Governance artifact spine

The current executable prototypes now carry lightweight
governance artifacts under each prototype's `artifacts/`
directory. These artifacts document the data boundary, model-like
or analysis output, interface contract where relevant,
evaluation registry entries, and governance gate review where
relevant.

The artifacts are intentionally small. Their role is to make the
system boundary visible: synthetic-only data, intended use,
limitations, evaluation stage, owner, and follow-up decision.
The structure is backed by the literature synthesis in
`docs/evidence-base.md` and checked by
`tests/test_governance_artifacts.py`.
