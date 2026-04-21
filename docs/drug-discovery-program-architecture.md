# Drug discovery program architecture

A program-level view of AI-enabled drug discovery: the
discovery pipeline as a system of systems, with
architectural, sourcing, portfolio, and regulatory
decisions treated explicitly.

## Why program architecture

AI in drug discovery is often discussed as a collection
of methods. At the program level, the question is how
methods are assembled into a working pipeline, which
capabilities are in-house, how candidates move through
stage gates, and how the program interacts with the
broader R&D portfolio. This is system-of-systems
engineering applied to discovery.

## Discovery pipeline as system of systems

The discovery pipeline has distinct subsystems, each a
system in its own right:

- **Target identification system.** Omics, genetic
  association data, pathway tools, literature curation,
  sometimes biomedical knowledge graphs.
- **Hit discovery system.** High-throughput screening,
  virtual screening, de novo generative chemistry.
- **Lead optimization system.** Medicinal chemistry
  workflows, property prediction, retrosynthesis
  planning.
- **Preclinical evaluation system.** In vitro, in vivo,
  and ADMET workflows, safety pharmacology.
- **Clinical development system.** Protocol design, site
  selection, execution.

AI components sit inside each subsystem with different
roles. The system-of-systems perspective asks how the
subsystems share data, models, and decisions, and where
coupling causes fragility.

## Stage-gate architecture

A stage-gate architecture for AI-enabled discovery:

- **Gate A — Target validated for the program.** Evidence
  package including genetic, functional, and clinical
  rationale; AI-supported target evidence explicitly
  flagged as such.
- **Gate B — Tractability established.** Structural
  availability, assayability, chemical or biological
  matter accessible; AI-assisted assessments documented.
- **Gate C — Hit series selected.** Diversity, novelty,
  and initial activity criteria; AI-generated or
  AI-prioritized hits labeled with model versions and
  applicability domains.
- **Gate D — Lead declared.** Potency, selectivity,
  ADMET, and synthetic accessibility meet program
  thresholds; AI predictions accompanied by experimental
  validation.
- **Gate E — Development candidate.** Full preclinical
  package; AI-supported design decisions summarized for
  regulatory readability.
- **Gate F — Clinical progression.** Phase-specific go/
  no-go with AI-assisted trial design decisions
  documented.

The shared design decision is how evidence from AI
components enters each gate — as direct evidence, as a
prioritization tool, or as one input among several.

## Capability architecture

Core capabilities a discovery program needs to assemble:

- Chemical and biological data infrastructure (compound
  registries, assay databases, biologics data)
- Compute capacity for training and inference
- Model registry and experiment tracking for discovery
  models
- Property prediction, activity prediction,
  structure prediction, retrosynthesis, de novo
  generation
- Biomedical knowledge graphs for target and mechanism
  reasoning
- Experimental automation and feedback into data stores
- Regulatory documentation and traceability

The capabilities map to the five-plane reference
architecture (see `docs/ai-systems-architecture.md`) with
domain-specific instantiations.

## Sourcing and partnerships

The AI drug discovery landscape spans AI-first biotech
companies, large pharma in-house AI groups, academic
collaborations, and open-source tools. Build, buy, or
partner decisions for a program include:

- **In-house AI group.** Deepest integration with
  program scientists; highest fixed cost; slowest to
  pivot.
- **External AI partner.** Specialized capabilities
  (for example, generative chemistry or structure
  prediction); faster to access; interface and IP
  complexity.
- **Academic collaboration.** Access to novel methods
  and graduate-level talent; slower timelines; publication
  considerations.
- **Open source and public datasets.** Reduces duplication
  for commodity tasks; reproducibility concerns on
  benchmark quality.

Each source interacts differently with data governance,
intellectual property, and program timelines. The
appropriate mix varies by program stage and by
capability.

## Portfolio management

A drug discovery portfolio is a collection of programs
across therapeutic areas and modalities. Program-level
AI investments interact with portfolio decisions:

- **Prioritization.** Which programs get AI-enabled
  acceleration and which continue on traditional
  timelines?
- **Shared infrastructure.** Which capabilities are
  funded at portfolio level (model registry, knowledge
  graph) vs. at program level?
- **Knowledge sharing.** How are lessons learned from one
  program's AI deployment transferred to the next?
- **Attrition.** How is AI-supported go/no-go distinct
  from traditional attrition analysis, and how does it
  affect portfolio-level risk-adjusted value estimates
  (Paul et al., 2010; Kola and Landis, 2004)?

## Regulatory documentation

AI-supported design decisions enter regulatory review
when the program progresses. The documentation burden
includes:

- Description of the AI method used (algorithm, training
  data, evaluation).
- Role of the AI method in the decision (prioritization,
  screening, direct evidence).
- Applicability domain statement for predictions.
- Version control and change log.
- Relationship to the FDA Model-Informed Drug Development
  framework where applicable.

The program architecture should surface this
documentation as part of the stage-gate artifact set, not
as a separate regulatory activity.

## Stage-specific topical notes

The gate architecture above summarizes the evidence
shape at each stage. Stage-specific topical notes carry
the detail:

- Discovery method survey: `docs/drug-design.md`.
- Preclinical safety evidence at Gate D and E:
  `docs/admet-and-preclinical-safety.md`.
- First-in-human and exposure-response at Gate E and
  F: `docs/clinical-pharmacology-and-midd.md`.
- Trial design and operations feeding Gate F:
  `docs/ai-for-clinical-trials.md`.
- Post-approval observational evidence that feeds back
  into next-generation programs:
  `docs/pharmacoepidemiology-methods.md`.
- Program-level case material:
  `docs/pharma-ai-case-studies.md`.

## Open questions

- Which capabilities are most effective to centralize
  across a pharma portfolio, and which are better at the
  program level?
- How is AI-supported evidence weighed against
  experimental evidence at each gate?
- How are cross-program model reuse and data reuse
  documented and governed?
- What does the AI-enabled equivalent of a stage-gate
  review package look like in practice?

## Limitations and cautions

- Program architecture descriptions are general; real
  programs carry organization-specific structures.
- Sourcing discussion is descriptive, not a
  recommendation; partnership strategies vary by program
  and by firm.
- Portfolio implications are directional; risk-adjusted
  value estimates depend on many assumptions outside
  the scope of these notes.
- Regulatory documentation expectations evolve; the
  discussion here is orientation, not guidance.
