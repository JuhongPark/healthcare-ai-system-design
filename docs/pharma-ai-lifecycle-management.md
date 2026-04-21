# Pharma AI lifecycle management

Lifecycle and stage-gate structure for AI models inside a
pharma R&D organization — the discovery and development
counterpart to the clinical AI lifecycle in
`docs/ai-lifecycle-management.md`.

## Why a separate lifecycle

Clinical AI models and pharma R&D AI models share the
V-model shape and the idea of stage gates. They diverge
at almost every other level: the unit being validated
(patient-specific prediction vs. compound-level
prediction), the ground truth (clinical outcome vs.
assay readout), the feedback cadence (outcome events in
days to months vs. assay results in days to weeks), and
the regulatory surface (SaMD vs. MIDD and ICH). A
lifecycle copied from clinical AI without this work
misses the shape of R&D decisions.

## V-model adapted to R&D ML

Left arm — design activities; right arm — verification
and validation activities, paired by exit criteria.

- **Concept → scientific question.** What decision
  will the model support: a target nomination, a hit
  prioritization, a property cutoff, a trial design
  choice?
- **Requirements → scientific, operational, and
  regulatory requirements.** Data access and license,
  evaluation rigor, auditability, regulatory
  applicability (MIDD, ICH, GCP).
- **Architecture → data, model, serving, monitoring,
  governance planes.** See
  `docs/pharma-ai-systems-architecture.md`.
- **Design → split policy, representation, model
  class, evaluation harness.** Scaffold and time
  splits, applicability domain, uncertainty
  representation.
- **Implementation → code, pipelines, documentation.**
  Pretraining and finetuning as distinct stages with
  separate artifacts.
- **Unit verification → component tests.** Data
  loaders, featurizers, training-run determinism
  where achievable.
- **Integration verification → end-to-end tests.**
  Batch and interactive paths tested on representative
  fixtures.
- **Retrospective validation → held-out benchmark
  performance.** Random, scaffold, and time splits
  reported together.
- **Prospective validation → pre-registered
  comparison to assay or trial readouts.** The number
  that actually bounds decision value.
- **Operational acceptance → monitoring and update
  governance proven.**

The right arm is not audit. Prospective validation in
particular is a design-time commitment: the evaluation
set is registered before the outcomes are observed, so
the comparison is honest when it arrives.

## Stage gates for R&D models

The clinical lifecycle uses Gates 0 through 9. The R&D
lifecycle reuses the gate idea with scientifically
relevant exit criteria. The model stage-gates below are
distinct from the program stage-gates in
`docs/drug-discovery-program-architecture.md` (Gates A
through F), though the two sets interact.

- **Gate M0 — Scientific question signed off.**
  Decision, user, setting, baseline, and success
  criteria defined; a non-ML baseline quantified.
- **Gate M1 — Data access and curation.** Data
  licenses resolved; canonicalization and split
  policy decided and documented.
- **Gate M2 — Retrospective baseline.** Retrospective
  performance meets pre-stated threshold on scaffold
  and time splits; calibration reported alongside
  ranking metrics.
- **Gate M3 — Applicability domain established.** The
  applicability domain is defined, evaluated on held-
  out data, and packaged with the model artifact.
- **Gate M4 — Prospective validation plan locked.** A
  pre-registered, prospective evaluation is defined;
  acceptance criteria and comparator are set before
  the prospective data are seen.
- **Gate M5 — Prospective validation passed.**
  Prospective performance meets criteria; evaluation
  report finalized.
- **Gate M6 — Deployment approved.** Intended-use
  statement, model facts analog, monitoring plan,
  change-control plan, retirement criteria signed off.
- **Gate M7 — Operational stability.** Prospective
  monitoring thresholds met for a defined period;
  active learning loop behaviors characterized.
- **Gate M8 — Update approved.** New version evaluated
  against incumbent on the prospective-validation
  harness; subgroup and chemotype coverage checks
  documented.
- **Gate M9 — Retirement executed.** Model withdrawn;
  successor identified or use discontinued; archive
  and audit closure complete.

Gate M5 is the most scientifically load-bearing and the
one most often skipped. A retrospective benchmark number
without a prospective check is a model, not a deployable
system.

## Mapping model gates to program gates

Program gates A through F in
`docs/drug-discovery-program-architecture.md` are the
candidate-trajectory equivalents. The interaction:

- **Program Gate B (tractability).** Needs structure
  prediction (at Gate M6 or M7) and property models
  ready to support decisions.
- **Program Gate C (hit series selected).** Consumes
  property prediction and activity prediction outputs
  with applicability-domain labels.
- **Program Gate D (lead declared).** Consumes ADMET
  predictions; these must be at Gate M6 or later, not
  at M2.
- **Program Gate E (development candidate).**
  Preclinical-safety models at full lifecycle
  operational stability; MIDD-supporting models
  beginning regulatory review.
- **Program Gate F (clinical progression).** Clinical-
  pharmacology models carry their own MIDD lifecycle;
  see `docs/clinical-pharmacology-and-midd.md`.

A useful governance rule: no model output enters a
program gate vote unless the model has cleared its own
corresponding M-gate.

## DMTA integration

The design-make-test-analyze cycle is the operational
feedback loop of lead optimization. An AI system lives
inside a DMTA cycle rather than above it:

- **Design step.** Property, activity, and
  synthesizability predictions with uncertainty
  propose compounds.
- **Make step.** Synthesis cost, route feasibility,
  and IP considerations filter and prioritize.
- **Test step.** Assay readouts arrive on the
  compounds actually synthesized.
- **Analyze step.** Assay readouts are added to the
  training corpus; models are retrained under the
  change-control plan.

The lifecycle discipline sits on top: the cycle's
retraining is a Gate M8 event, not an uncontrolled
continual-learning loop.

## MLOps practice for R&D contexts

R&D MLOps borrows from clinical MLOps (see
`docs/mlops-for-regulated-ai.md`) and specializes:

- **Pipelines as code.** Pretraining, finetuning, and
  evaluation pipelines versioned independently.
- **Model registry.** Every entry carries training-data
  digest, split policy, applicability domain,
  evaluation report (retrospective and prospective),
  intended-use statement, retirement conditions.
- **Feature store for chemistry.** Canonicalized
  features, assay-version-aware; a chemistry feature
  store is unusual but the discipline it imposes is
  load-bearing.
- **Shadow scoring.** New model candidates score
  compounds alongside the production model before
  promotion, with prospective assay comparison.
- **Champion-challenger for property models.** See
  `docs/multi-model-orchestration-patterns.md`.
- **Reproducibility archive.** Full reconstruction of
  any model version that contributed to a regulatory
  or IP record.

## Update governance

Pharma R&D models update for different reasons than
clinical ones:

- **New assay data.** The most common reason, usually
  covered by an operational PCCP-equivalent for R&D.
- **New public data release.** Foundation-model
  pretraining or benchmark refresh; separate
  validation cadence.
- **New chemistry foundation model.** Upstream choice
  affects all downstream property models; change
  control is at a different scope.
- **Scope expansion to new chemotype or modality.** An
  applicability-domain expansion rather than a
  performance update; governance treats it
  accordingly.

Update governance should require:

- Prospective comparison to the incumbent on the
  registered evaluation harness.
- Applicability-domain delta documented (expanded,
  contracted, redefined).
- Chemotype-coverage check where relevant.
- Downstream-consumer notification via contract
  versioning (see
  `docs/interface-contracts-for-healthcare-ai.md`).

## Retirement

An R&D model retires when:

- The program it supports retires.
- An upstream foundation model or data source becomes
  unavailable.
- A successor model supersedes it on the registered
  evaluation harness.
- Applicability-domain drift makes current predictions
  uninterpretable.
- Regulatory use has transitioned to a physics-grounded
  or parametric alternative that the organization
  maintains instead.

Retirement includes archiving the model version,
freezing its evaluation record, and closing out any
prospective predictions that depended on it.

## Connection to other notes

- Clinical-side lifecycle:
  `docs/ai-lifecycle-management.md`.
- Program-level gates:
  `docs/drug-discovery-program-architecture.md`.
- Architecture: `docs/pharma-ai-systems-architecture.md`.
- Regulated MLOps: `docs/mlops-for-regulated-ai.md`.
- Downstream lifecycle for clinical pharmacology:
  `docs/clinical-pharmacology-and-midd.md`.
- Evaluation strategy: `docs/ai-evaluation-strategy.md`.

## Open questions

- What is the smallest useful model-lifecycle
  governance for a single discovery program, as
  opposed to a pharma-wide platform?
- How does the lifecycle change for a partner-supplied
  model used inside an internal program?
- How is prospective validation designed when the
  prospective batch is small (tens of compounds per
  quarter)?
- How should continual-learning R&D models be governed
  when retraining is routine but formal Gate M8
  cadence is too slow?

## Limitations and cautions

- Model and program gates are coordination devices;
  they do not substitute for the scientific work
  inside each stage.
- The M-gate labels are a framing, not a standard; a
  given organization may use different labels, fewer
  gates, or a continuous governance model, and that
  can be correct for its scale.
- Prospective-validation discipline is often at odds
  with program speed; the balance is a program-
  leadership decision, not a methodological one.
