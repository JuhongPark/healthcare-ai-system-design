# Pharma AI systems architecture

A reference architecture for AI systems inside a pharma
R&D organization — the discovery, preclinical, and
development-stage counterpart to the hospital-facing
architecture in `docs/ai-systems-architecture.md`.

## Why a separate architecture

Clinical AI systems and pharma R&D AI systems share
planes, contracts, and lifecycle concerns, but the
entities flowing through them are different. A clinical
system reasons over patients and encounters; a pharma R&D
system reasons over targets, compounds, assays,
structures, and trials. The data, the latency budgets,
the evaluation regimes, and the regulatory surfaces all
differ. A hospital architecture retargeted to R&D without
this work reproduces patterns that do not fit.

## Reference architecture: five planes, pharma instantiation

### Data plane

- **Compound and biologic registries.** Canonical
  molecular representations (InChI, InChIKey, canonical
  SMILES, HELM for biologics), linked identifiers across
  internal and public sources (ChEMBL, PubChem,
  BindingDB, DrugBank).
- **Assay and screening data.** Plate-level and
  well-level records with assay protocol version,
  concentration-response data, Z' and positive-control
  tracking, reference-compound trending over time.
- **Structural data.** Experimental structures (PDB),
  predicted structures (AlphaFold DB, ESM Atlas), and
  derived pocket annotations with confidence scores.
- **Biomedical knowledge graphs.** Target-disease,
  target-pathway, drug-side-effect, and gene-phenotype
  relations, with curation provenance and release
  versions.
- **Omics and phenotypic data.** Transcriptomic,
  proteomic, and imaging-derived features, usually at
  cell-line, sample, or cohort granularity.
- **Identity and IP.** Internal compound identifiers
  tied to invention records, with access boundaries
  around chemotype families.
- **Transformation.** Standardization to canonical
  forms, tautomer and stereochemistry handling, unit
  and ontology mapping (UniProt, MeSH, MedDRA).
- **Lineage.** Full derivation of each feature from its
  source record, including assay protocol version and
  data-release version for public sources.

The load-bearing assumption is canonicalization. A
program that treats SMILES as text without tautomer
normalization and stereochemistry handling is keeping
duplicates in the registry it does not know about.

### Model plane

- **Experiment tracking.** Runs, training corpora,
  scaffold-aware split identifiers, early-stopping
  checkpoints, and prospective-evaluation attachments.
- **Training orchestration.** Pipelines as code with
  artifact capture; self-supervised pretraining
  (ChemBERTa, MoLFormer, ESM) and supervised finetuning
  treated as separate pipeline stages.
- **Model registry.** Versioned, signed model
  artifacts, each carrying: training set digest, split
  policy, applicability domain definition, evaluation
  report (including calibration), intended-use
  statement, retirement conditions.
- **Evaluation harness.** Standard evaluations for
  property prediction, activity prediction, structure
  prediction, and retrosynthesis; scaffold and
  time-based splits; prospective validation harness
  that consumes assay readouts as they arrive.

### Serving plane

Pharma serving is heterogeneous by access pattern:

- **Batch virtual screening.** Millions to billions of
  compound evaluations with latency measured in hours
  to days; the budget is throughput per dollar, not
  per-request latency.
- **Interactive design support.** Medicinal chemist
  workflows (property lookup, retrosynthesis
  suggestions, structure-based design iterations) with
  latency measured in seconds.
- **Structure-prediction service.** Mixed batch
  (proteome-scale folding) and interactive (mutant
  structures on request).
- **Active-learning loop.** Tight coupling between
  serving and data capture, closing the
  design-make-test-analyze loop.
- **Output contract.** Prediction, uncertainty (epistemic
  where available), applicability-domain flag, model
  version, feature version, timestamp, provenance
  token.

### Monitoring plane

Monitoring in pharma differs from clinical monitoring by
feedback source and latency:

- **Input monitoring.** Distribution drift over
  chemotype space, target families, assay conditions.
- **Output monitoring.** Distribution of predictions,
  calibration of uncertainty, drift in
  applicability-domain coverage.
- **Prospective validation feedback.** As assay
  readouts arrive on compounds the model scored,
  automatic comparison to prospective predictions with
  rolling metrics; this is the ground-truth stream
  that matters for programs.
- **Retrosynthesis feasibility feedback.** Route
  proposals that chemists accept vs. reject; an active
  feedback signal about route models.
- **Downstream decision tracking.** Which predictions
  changed a design round, which changed a gate vote,
  which were set aside in favor of experimental
  evidence.
- **Alerting.** Calibration drift, applicability-domain
  coverage collapse, assay-quality drift that
  invalidates incoming training data.

### Governance plane

- **Approval workflow.** Intake and review specific to
  model type — a property model and a structure
  prediction model have different review criteria.
- **Change control.** Model and pipeline changes tied
  to program stage (exploratory vs. lead optimization
  vs. regulatory-supporting).
- **Audit log.** Immutable record of model versions,
  prospective predictions, and the decisions they
  contributed to. Required if AI-supported evidence
  will enter a regulatory submission.
- **Access policy.** Role-based across programs and
  chemotype families; partnership agreements define
  which external parties see which data.
- **IP and provenance.** Capture of invention-relevant
  timestamps and of model influence on candidate
  nomination, important where AI-involvement claims
  enter patent and regulatory records.

## Interface contracts for pharma AI

Interface contracts between planes are where the
architecture earns its keep. Contracts that matter most
in pharma:

- **Compound contract.** Canonical representation,
  identifier, stereochemistry, provenance; consumers
  agree on a single form or explicitly handle
  conversions.
- **Assay contract.** Protocol version, units,
  concentration-response shape, valid range, positive
  controls; a change in protocol version is a contract
  change.
- **Prediction contract.** Score, uncertainty, model
  version, feature version, applicability-domain flag,
  training-data digest, timestamp.
- **Structure contract.** Coordinates, pLDDT or PAE or
  equivalent confidence, source (experimental or
  predicted), version of the prediction model.
- **Audit contract.** What is logged for each
  prospective prediction, who can read it, retention
  policy; particularly load-bearing when regulatory use
  is possible.

See `docs/interface-contracts-for-healthcare-ai.md` for
the deeper treatment of contract patterns.

## Deployment topologies

- **On-premise.** Compound libraries, assay data, and
  model training on internal infrastructure. Highest
  control, highest operational burden.
- **Hybrid.** Foundation-model pretraining on cloud,
  finetuning and serving on internal infrastructure;
  public-data pipelines share cloud resources.
- **Partner-hosted.** An external AI partner owns some
  planes (usually model plane or structure-prediction
  service); data crosses a contractual trust boundary
  with explicit minimization.
- **Federated.** Cross-organization training over
  chemistry or assay data without pooling raw records;
  relevant for consortia and pre-competitive collaborations.

Each topology fixes different properties: latency,
IP exposure, regulatory surface, cycle time, and cost of
change. Partner-hosted arrangements in particular make
audit and documentation a contract-negotiation problem,
not only a technical one.

## System properties

- **Latency budget.** Batch hours for library
  screening; seconds for interactive chemistry; minutes
  for structure prediction.
- **Throughput.** Compounds scored per dollar per
  minute at the batch tier.
- **Accuracy budget.** Different end points tolerate
  different error; a development-candidate ADMET
  decision and a triage filter for a million-compound
  library have very different precision requirements.
- **Uncertainty discipline.** Epistemic uncertainty
  and applicability-domain reporting are first-class
  design parameters, not afterthoughts.
- **IP boundary.** Where proprietary chemistry data
  crosses a trust boundary, and how.
- **Change cadence.** Model updates inside program life
  vs. at cross-program release points; continual
  learning loops vs. frozen models for regulatory
  snapshots.

## Coupling to program architecture

The reference architecture above supports the program-
architecture view in
`docs/drug-discovery-program-architecture.md`:

- Stage gates draw evidence from the model plane and
  the prospective-validation monitoring stream.
- Capability architecture is an allocation of model-
  plane and data-plane components to organizational
  units or partners.
- Sourcing decisions change which planes the
  organization owns end to end.
- Portfolio management reconciles the shared vs.
  per-program split of platform capabilities.

## Open questions

- Which interface contracts in pharma AI break most
  often in practice, and what pattern does the failure
  follow?
- How should applicability-domain signals from multiple
  models be combined when they enter a gate vote?
- What does a cross-program model-reuse governance
  policy look like when chemotype coverage differs?
- How do federated topologies trade off generalization
  against IP exposure for chemistry and assay data?
- Where does the CMC and manufacturing AI plane fit
  relative to the discovery and development planes?

## Limitations and cautions

- A reference architecture is a starting template, not
  a prescription. Real programs diverge by therapeutic
  area, modality, and sourcing strategy.
- The five-plane decomposition is one useful
  partitioning; others are defensible.
- Public datasets and registries are cited to orient
  readers; their use in a specific program depends on
  license and validation work outside this note.
- Regulatory expectations around AI evidence in drug
  submissions are evolving; architectural descriptions
  here should be read alongside current FDA, EMA, and
  PMDA guidance.
