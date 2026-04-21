# Multi-model orchestration patterns

Notes on how multiple models compose into a working
system — cascade, gating, ensemble, fallback,
champion-challenger, and physics-ML hybrid patterns. The
reference architectures list orchestration as a concern;
this note develops the vocabulary of patterns and their
trade-offs.

## Why patterns

A single model rarely does the job alone. Clinical
deployments fuse predictions from several models on the
same patient; drug discovery pipelines chain property,
structure, and generative models in tight loops. The
design question is not whether to compose models but how
to compose them such that the system's behavior is
understandable, evaluable, and correctable. The patterns
below are a vocabulary for that question.

## Pattern: cascade (two-stage or staged filtering)

A cascade passes inputs through a sequence of models,
each one deciding whether to forward to the next stage.
Early stages are cheap and coarse; later stages are
expensive and precise.

**Where it shows up.**

- Virtual screening: a structure-free property filter
  prunes a billion-compound library before a
  docking-based filter prunes to a thousand.
- Clinical triage: a simple rule-based screen picks
  candidates for a model-based risk score.
- Imaging: a detector proposes regions; a classifier
  characterizes them.

**Design parameters.**

- Stage thresholds and the recall they enforce;
  missed items are lost permanently unless the
  cascade is re-run.
- Calibration discipline at the earliest stage —
  miscalibration there sets an envelope on everything
  downstream.
- Monitoring coverage at each stage independently; an
  aggregate metric hides per-stage degradation.

## Pattern: ensemble

An ensemble combines predictions from multiple models
with different training data, architectures, or
initializations.

**Where it shows up.**

- Chemistry property prediction with Chemprop, graph
  transformers, and descriptor-based regression
  averaged or stacked.
- Clinical risk scores where an ML model is blended
  with a logistic-regression baseline and a clinical
  rule.
- Structure prediction ensembles for confidence
  calibration (averaging over AlphaFold recycling
  seeds, ESMFold inference runs).

**Design parameters.**

- Diversity: ensembles that average near-identical
  models waste compute; diversity is the mechanism by
  which the ensemble buys anything.
- Weighting scheme and its data dependence — learned
  weights can overfit on a small validation set.
- Uncertainty aggregation: an ensemble's disagreement
  is a useful uncertainty signal if interpreted with
  care.

## Pattern: gating and routing

A gating model decides which specialist model processes
the input. Routing separates paths at inference time.

**Where it shows up.**

- Clinical NLP pipelines that route to different
  extractors depending on document type (discharge
  summary, radiology report, pathology report).
- Chemistry pipelines that route molecules to the
  appropriate property head based on chemotype or
  modality (small molecule vs. peptide vs. biologic).
- Foundation-model-backed systems that route prompts
  to fine-tuned adapters per task.

**Design parameters.**

- Gating accuracy; a mis-routed input may be scored
  by a model outside its applicability domain and
  returned with misleading confidence.
- Observability: which inputs went to which
  specialist, and how the mix shifts over time.
- Fallback when the gate is uncertain — route to a
  generalist, escalate, or defer.

## Pattern: fallback

A primary model is preferred; a simpler or older model
runs as a backup when the primary is unavailable,
returns out-of-distribution, or violates an
applicability check.

**Where it shows up.**

- Clinical serving where a sophisticated model falls
  back to a clinical rule when the feature pipeline is
  degraded.
- Structure prediction where a full AlphaFold run falls
  back to a sequence-only model under time pressure.
- Generative chemistry that falls back to a
  nearest-neighbor retrieval when the generative model
  has low confidence.

**Design parameters.**

- Fallback triggering criteria, observable and
  testable.
- Documentation of degraded-mode performance so the
  consumer knows what to expect.
- Alerting on fallback rate; a rising fallback rate is
  a leading indicator of primary-model degradation or
  infrastructure issue.

## Pattern: champion-challenger

A production model (champion) serves traffic while one
or more candidate models (challengers) run in shadow or
on a small traffic fraction. Promotion criteria are
pre-stated.

**Where it shows up.**

- Any serving plane that is mature enough to retain
  challenger evaluation infrastructure.
- Pharmacometric modeling where a legacy popPK model
  is compared against an ML-augmented one in parallel.
- Chemistry property pipelines where new foundation-
  model releases are benchmarked against production
  models on prospective assay batches.

**Design parameters.**

- Promotion criteria — in-distribution performance,
  subgroup checks, calibration, operational metrics.
- Statistical design of the comparison; a challenger
  that wins on a single post-hoc metric is not a
  challenger that has won.
- Traffic-allocation ethics: in clinical settings,
  running a challenger on patients requires its own
  governance.

## Pattern: human-in-the-loop composition

A model proposes; a human decides; the human's decision
feeds back into training data. This is less a single
pattern than a family: active learning,
design-make-test-analyze, clinician override, and
adjudication pipelines.

**Where it shows up.**

- Medicinal chemistry design iterations (see DMTA
  under `docs/pharma-ai-lifecycle-management.md`).
- Active learning for property and activity models.
- Clinician override in decision support
  (`docs/human-ai-interaction-patterns.md`).
- Adjudication pipelines for adverse-event detection.

**Design parameters.**

- Feedback discipline: which decisions feed back,
  under what framing, to prevent feedback loops from
  entrenching model errors.
- Labeling protocol when a human output becomes
  training data.
- Latency: the loop closes on the cadence of human
  review, not model inference.

## Pattern: physics-ML hybrid

A learned model is composed with a physics-grounded
model. The learned component handles what the physics
cannot address at scale; the physics component anchors
what the learned model cannot guarantee.

**Where it shows up.**

- Structure-based drug design: ML scoring for
  coarse filtering; free-energy calculation (MM-PBSA,
  FEP) for refinement.
- PK/PD: an ML layer on covariates inside a
  compartmental model; the compartmental structure
  preserves mechanistic interpretation.
- QSP: mechanistic pathway models with data-driven
  parameter estimation.

**Design parameters.**

- Where the interface between the learned and the
  mechanistic components sits; learned-in-the-middle
  hybrids are different animals from learned-as-prior
  hybrids.
- Uncertainty handling across the boundary — physics
  models carry their own uncertainty, and composing
  with an ML uncertainty estimate is not always
  straightforward.
- Auditability: regulators often find physics-grounded
  pieces easier to review, which shapes the choice of
  boundary.

## Pattern: retrieval-augmented generation

A generator is composed with a retriever that grounds
generation in external, up-to-date, or
organization-specific context.

**Where it shows up.**

- Clinical LLMs grounding answers in guideline text,
  institutional policy, and patient chart snippets.
- Chemistry generation grounded in nearest-neighbor
  retrieval from a curated library.
- Knowledge-graph-grounded question answering over
  biomedical literature.

**Design parameters.**

- Retrieval quality; a confidently wrong retrieval is
  worse than no retrieval.
- Grounding discipline; the generator may ignore or
  contradict the retrieval without the consumer
  noticing.
- Provenance: retrieved passages carry citations, and
  the consumer sees them.

## Cross-cutting concerns

Regardless of which pattern is used, orchestrated
systems face shared concerns:

- **Observability.** Each model in the composition is
  a separate thing to monitor, with its own
  calibration, drift, and utilization metrics.
- **Evaluation.** Component-level metrics tell a
  different story than system-level metrics. Both
  belong in the dashboard.
- **Versioning.** The set of model versions composed
  in an output is a contract in itself (see
  `docs/interface-contracts-for-healthcare-ai.md`).
- **Uncertainty propagation.** Composing models often
  compounds uncertainty in ways that the naive output
  interval hides.
- **Failure isolation.** A broken component should not
  take down the whole composition; fallback and
  graceful degradation are design decisions.
- **Auditability.** A regulatory-facing output whose
  components are a tangled set of services is
  effectively unauditable.

## Anti-patterns

- **Unbounded chains.** Models that call models that
  call models, without an explicit composition, drift
  into spaghetti.
- **Silent retries.** Fallback that fires
  automatically without observability hides
  degradation.
- **Post-hoc ensembling as a fix.** Ensembling to
  paper over a miscalibrated primary model usually
  moves the problem rather than solving it.
- **Gate coupled to champion.** A gate trained on the
  production model's decisions treats those decisions
  as ground truth and cements any error in them.

## Open questions

- Which orchestration patterns are most often used in
  regulated pharma and clinical AI deployments, and
  which remain experimental?
- How should component-level SLOs aggregate into a
  system-level SLO for a composed service?
- What does a minimum viable observability set look
  like for an orchestrated system?
- How are physics-ML hybrid models evaluated for
  regulatory submissions when neither pure-physics
  nor pure-ML review practice applies?

## Connection to other notes

- Reference architectures:
  `docs/ai-systems-architecture.md`,
  `docs/pharma-ai-systems-architecture.md`.
- Interface contracts:
  `docs/interface-contracts-for-healthcare-ai.md`.
- Evaluation strategy:
  `docs/ai-evaluation-strategy.md`.
- Regulated MLOps: `docs/mlops-for-regulated-ai.md`.
- Reliability: `docs/ai-risk-and-reliability.md`.

## Limitations and cautions

- Pattern labels are descriptive, not prescriptive;
  real systems mix patterns and carry context-specific
  constraints.
- Orchestration makes a system more capable and also
  harder to evaluate; increased complexity should be
  justified by decisions the patterns change.
- Some patterns that are conventional in general ML
  (for example, heavy ensembling) face adoption
  barriers in regulated settings where reviewability
  and maintenance burden matter.
