# Evidence base for the project direction

This document summarizes how the literature review supports the
repository's current direction. It is a design synthesis, not a
clinical claim. Source-level details live in
`references/evidence-matrix.csv` and
`references/annotated-bibliography.md`.

## Core conclusion

The repository's strongest direction is healthcare AI system
design: treating AI as a managed system made of data, models,
interfaces, workflow integration, validation, monitoring,
governance, and organizational ownership.

That direction is well supported. The strongest sources do not
argue that better model performance alone is enough. They argue
that clinical impact depends on evaluation design, local
validation, workflow fit, human factors, monitoring, update
control, transparent documentation, and accountable governance.

## Why system design is the right unit

Kelly et al. and DECIDE-AI frame the central translation gap:
many AI systems show promising retrospective or preclinical
performance, while far fewer show robust clinical value in real
settings. Sculley et al. explain the engineering side of the
same problem: ML systems accumulate hidden technical debt through
data dependencies, feedback loops, undeclared consumers, and
changes in the external world.

Design consequence: the repository should keep the model as one
component, not the product. Every prototype should expose the
surrounding system: data assumptions, user context, evaluation
stage, monitoring plan, and governance boundary.

Supported by: E001, E002, E005, E006, E027.

## Evidence layer: RWE and causal discipline

The RWE literature supports the repository's cautious treatment
of observational treatment-outcome work. FDA's RWE framework
distinguishes data source reliability, data relevance, and study
methodology. Target trial emulation and active comparator
new-user design shift the work from model-first analysis toward
protocol-like design. Propensity scores and negative controls
are useful, but only under explicit assumptions and as part of a
larger design.

Design consequence: the RWE prototype should grow into a
protocol-oriented sketch. The next iteration should add a target
trial table, index-date and comparator definitions, eligibility
windows, balance diagnostics, and sensitivity analyses. The
prototype should continue to label results as synthetic method
illustrations, not evidence about real products or patients.

Supported by: E008, E011, E012, E013, E014.

## Workflow layer: CDS and human use

The CDS literature supports the dashboard prototype's
workflow-first posture. Bates and Kawamoto emphasize timing,
workflow integration, automatic availability, and actionable
recommendations. Beede et al. show that deployed clinical AI
changes meaning in real work settings where infrastructure,
trust, and human interaction matter. Tonekaboni et al. and Rudin
warn that explanation displays should not be treated as generic
trust generators.

Design consequence: the dashboard should become an experiment in
workflow patterns rather than a prettier risk score. Future
versions should compare passive indicators, inline signals, and
interruptive alerts. Explanation panels should include
uncertainty and limits, not only feature rankings.

Supported by: E004, E015, E016, E017, E018, E027.

## Operations layer: monitoring and lifecycle control

External validation and lifecycle sources support the monitoring
loop prototype. Wong et al. give a concrete case where a widely
implemented model performed worse under external validation than
developer-reported performance. FDA AI/ML SaMD documents and the
ML technical debt literature both point toward lifecycle
governance: monitoring, real-world performance evidence,
transparent update logic, and controlled modification paths.

Design consequence: monitoring should stay central, not become a
later add-on. The prototype should expand from drift and
calibration flags into incident records, root-cause review,
pause/update/rollback decisions, and links back to an evaluation
registry.

Supported by: E001, E002, E003, E009, E010, E027.

## Documentation and governance layer

WHO guidance, Datasheets for Datasets, Model Cards, CONSORT-AI,
SPIRIT-AI, and DECIDE-AI support the repository's emphasis on
documentation. These sources make the same architectural point:
AI artifacts need intended-use boundaries, data provenance,
evaluation context, known limits, human interaction details, and
failure modes.

Design consequence: the next shared artifacts should be
templates. At minimum, add a data card, model card, evaluation
registry, interface contract, and governance gate review. The
templates should be applied to the existing synthetic
prototypes before adding larger models.

Supported by: E005, E006, E007, E019, E020, E027.

## Fairness and proxy-label risk

Obermeyer et al. support a specific fairness lesson that fits the
repository: the label is part of the system design. A model can
look technically neutral while using a proxy that encodes
structural inequity.

Design consequence: future prototypes should include a proxy-
label audit step before performance reporting. This should be
handled as a data-design and governance issue, not only a
post-training fairness metric.

Supported by: E007, E019, E020, E021.

## Pharma and drug development extension

The pharma literature supports the repository's expansion beyond
hospital CDS into drug discovery and development systems.
Vamathevan et al., MoleculeNet, TDC, Stokes et al., and
AlphaFold all point to the same boundary: computational models
can prioritize, predict, or structure evidence, but they do not
replace downstream validation. Benchmarks are useful, yet
generalization, applicability domain, assay handoff, ADMET, and
program-stage evidence still govern whether an output matters.

Design consequence: the first pharma prototype should avoid
overclaiming discovery. A good next sketch is a public benchmark
property-prediction or ADMET workflow that reports benchmark
choice, split logic, calibration, applicability domain, and
handoff decision.

Supported by: E022, E023, E024, E025, E026.

## Portfolio implication

The repository should continue as a portfolio of small,
executable, synthetic or public-data prototypes that each expose
one system-design problem. The strongest next move is not a
larger model. It is a unified evidence-and-governance spine that
connects the existing prototypes:

- data cards for each synthetic generator
- model or analysis cards for each model-like output
- an evaluation registry across prototype stages
- interface contracts for workflow-facing outputs
- governance gate reviews for release, monitoring, update, and
  retirement decisions

This would make the repository's research thesis concrete: safe
healthcare AI is a system architecture and lifecycle problem,
not only a modeling problem.
