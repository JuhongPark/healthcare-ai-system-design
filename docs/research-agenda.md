# Research agenda

Notes on research directions for designing, evaluating, and
deploying AI in healthcare workflows. The goal is to articulate
open questions, design frameworks, and prototype ideas across
four connected tracks.

## Overview

Healthcare AI touches several interconnected problems:

- generating evidence about treatments and outcomes from
  observational data
- combining heterogeneous data types for patient-level reasoning
- integrating model outputs into clinical workflows in a way that
  is usable, interpretable, and safe
- maintaining systems over time as data, workflows, and
  populations change

The sections below outline four research tracks. They are not
independent — a model trained in Track 2 still needs the
governance of Track 4 to be usable, and the modeling choices in
Track 1 constrain what claims can be communicated in Track 3.

The tracks are read through a systems-engineering-and-management
lens: architecture, lifecycle, portfolio, organization, and risk,
developed in Track 7 and the cross-cutting topics below. The
lens applies across the other tracks — a Track 2 multimodal
model, for example, is designed, validated, deployed, and
retired inside the architecture and governance in Track 7.

## Track 1 — Real-world evidence and drug efficacy evaluation

### Motivation

Randomized trials are the reference standard for treatment
efficacy, but they are expensive, narrow in scope, and often do
not capture how therapies behave in routine care. Observational
healthcare data — claims, electronic health records, registries
— can in principle fill gaps in post-marketing surveillance,
comparative effectiveness, and studies of populations
under-represented in trials. In practice, using these data
responsibly is hard: confounding, selection bias, missingness,
and measurement error are all substantial.

### Open questions

- Under what conditions can observational data support causal
  claims about treatment effects, and when can it only support
  associational claims?
- How should cohort construction (index date, exposure
  definition, eligibility window) be stated so that a study is
  reproducible and contestable?
- Which negative controls and sensitivity analyses are most
  informative for a given design?
- How should comparative effectiveness results be communicated
  in a way that reflects uncertainty and residual confounding?
- How can propensity score methods and survival analysis be
  combined in ways that remain interpretable to clinicians and
  regulators?

### Possible prototype ideas

- A synthetic data generator with a known treatment effect and
  known confounders, used to compare several adjustment methods
  and quantify residual bias under misspecification.
- A notebook walking through cohort construction, propensity
  score estimation, weighted survival analysis, and a
  negative-control calibration step.
- A sensitivity analysis template that varies the treatment
  definition, eligibility window, and outcome ascertainment to
  show how robust (or fragile) an estimate is.

### Topical notes supporting this track

- `docs/pharmacoepidemiology-methods.md` — design
  choices (active comparator new user, target trial
  emulation, self-controlled designs), confounder
  adjustment, signal detection, and distributed data
  networks.
- `docs/clinical-pharmacology-and-midd.md` — how
  exposure-response and population PK evidence connects
  the efficacy question to dose, label, and population.
- `docs/ai-for-clinical-trials.md` — external comparator
  arms and synthetic controls that sit at the boundary
  of trial and observational evidence.

### Limitations and cautions

- Synthetic data cannot stand in for real evidence generation.
  It is useful for clarifying method behavior and failure modes,
  not for producing effect estimates that apply to patients.
- Observational analyses should be labeled as associations
  unless a credible causal design is justified and its
  assumptions are stated.
- Results are not post-marketing surveillance, not comparative
  effectiveness research fit for regulatory use, and not
  clinical guidance.

## Track 2 — Precision health and multimodal healthcare data

### Motivation

Patient-specific decision support is often discussed as if all
the relevant data were co-located, clean, and labeled. In
reality, clinical records, genomic signals, imaging-derived
features, behavioral data, and wearable signals live in
different systems, have different sampling rates, different
notions of ground truth, and different coverage across
populations. A model that fuses them inherits all of these
issues at once.

### Open questions

- How should models represent patients when modalities are
  missing in non-random ways?
- What does external validation look like for a multimodal model
  whose modalities differ across sites?
- When is a patient-level prediction meaningfully different from
  a subgroup-level prediction, and how should this distinction
  appear in the interface?
- How should uncertainty be propagated from noisy or incomplete
  modalities to the final output, and how should it be
  communicated?
- How can subgroup fairness be audited when some subgroups are
  small or only partially observed?

### Possible prototype ideas

- A schema for representing a synthetic patient with multiple
  modalities and explicit missingness patterns.
- A toy fusion model that compares late fusion, early fusion,
  and missing-modality gating strategies on synthetic data.
- A validation template that separates within-site, cross-site,
  and cross-population evaluation and reports all three.

### Limitations and cautions

- No protected health information, no private patient records,
  and no restricted datasets are used. Multimodal experiments
  rely on public, synthetic, or simulated data.
- Precision health language can easily overstate what a model
  can do for an individual patient. Prototypes should avoid
  deterministic framing and make uncertainty explicit.
- Subgroup analyses on synthetic data do not generalize — they
  illustrate a method, not a population effect.

## Track 3 — Clinical decision support and workflow integration

### Motivation

A predictive model is only one component of a clinical decision
support system. The larger question is how information enters a
care workflow: who sees the output, at what step, alongside what
other information, with what opportunity to act on it, and with
what accountability if something goes wrong. Models that score
well in isolation can still fail in deployment because they
ignore workflow fit, alert fatigue, and the cost of false
positives in a specific care setting.

### Open questions

- How should a model's output be staged into a clinician's
  workflow so that it is available when useful and quiet when
  not?
- What does uncertainty communication look like for an audience
  that is not a statistician?
- How should human-in-the-loop override be designed so that
  clinicians remain accountable without being overloaded?
- What does a minimally auditable decision support interaction
  look like — what needs to be logged for later review?
- How should decision thresholds be set, revisited, and
  renegotiated with clinical users as they learn the system?

### Possible prototype ideas

- A workflow-aware dashboard sketch that places a risk estimate,
  an uncertainty indicator, an explanation panel, a limitations
  panel, and an override control on a single screen, and logs
  the interaction for review.
- An alert-design exercise that compares blocking alerts, inline
  signals, and passive indicators on a simulated task.
- A "why this output" panel that surfaces feature contributions
  together with their caveats rather than as a ranking alone.

### Limitations and cautions

- Prototypes in this track are interface sketches on synthetic
  patient-like data. They are not clinical decision support,
  not medical advice, and not validated tools. They exist to
  make design questions concrete.
- Interpretability displays can create a false sense of
  understanding. Any explanation shown in a prototype should
  also show what it does not explain.
- Workflow claims made from synthetic data are hypotheses, not
  evidence.

## Track 4 — Monitoring, governance, and safety

### Motivation

Healthcare data and workflows change over time. Coding practices
drift, case mix shifts, software updates change what is
captured, and the standard of care moves. A deployed AI system
is therefore never "finished." Monitoring, update governance,
and feedback loops are part of the system, not afterthoughts.

### Open questions

- What metrics best detect dataset shift in a clinical setting,
  and how should they be chosen for a given model?
- What is the smallest useful monitoring setup for a single-site
  deployment, and what does it cost to operate?
- How should update governance decide when a model change is
  acceptable without triggering full re-validation?
- How should failure modes be cataloged so that a later
  maintainer can recognize them?
- Where do accountability boundaries sit between the model
  developer, the local validator, the deploying team, and the
  end user?

### Possible prototype ideas

- A monitoring sketch that tracks input distribution drift,
  outcome incidence, and calibration over time on a synthetic
  stream.
- A governance template that records, for each model version,
  the intended use, known limitations, validation evidence, and
  escalation path.
- A failure-mode checklist that lists, for a given prototype,
  how it could be wrong and how someone would notice.

### Limitations and cautions

- Monitoring methods illustrated on synthetic data do not
  represent real clinical performance.
- Governance templates are starting points for thinking, not
  policies.
- Feedback loops can become confounders if outputs start to
  influence the inputs. Prototypes should note when that risk
  applies.

## Track 5 — Hospital systems design

### Motivation

Decision support models, predictive risk scores, and
clinician-facing interfaces all live inside larger hospital
systems: clinical information systems, operational pipelines,
governance structures, vendor relationships. The hospital is
the deployment environment, not the background. Many of the
deployment failure modes described in Tracks 3 and 4 are
hospital-system failures: a model that runs against an
extract that drifted, a workflow that does not survive a
shift change, an inventory of models that no one maintains.

### Open questions

- How does a hospital maintain a current inventory of
  deployed models, and who owns the inventory?
- How are conflicting outputs from different models reconciled
  at the bedside?
- How are extract pipelines maintained when source systems
  change underneath them, and how is that change communicated
  to model owners?
- What does a minimum viable hospital AI governance committee
  look like at a single site?
- How are operational AI outputs (length-of-stay, no-show,
  surge forecasts) evaluated when they feed human scheduling
  rather than acting directly?

### Possible prototype ideas

- A hospital-system inventory template that records, for each
  deployed model, its data sources, owners, intended use,
  monitoring footprint, and retirement criteria.
- A simulated patient flow scenario that compares operational
  decisions with and without a length-of-stay forecast,
  recording where the forecast actually changed an action.
- A multi-model dashboard sketch showing how outputs from
  several models on a single patient encounter are presented
  together, including conflict cases.

### Limitations and cautions

- Hospital design notes are descriptive, not prescriptive
  policy, and do not represent any specific institution.
- Operational simulations on synthetic flow data illustrate
  trade-offs; they do not predict real hospital behavior.
- Inventory and governance templates are starting points for
  thinking, not artifacts intended for production use.

## Track 6 — Drug design and discovery

### Motivation

Track 1 covers how a drug is evaluated once it exists.
Track 6 covers the upstream side: how a candidate is found,
optimized, and characterized before it reaches a trial. The
two ends of the pipeline use different data and methods, but
the design choices made upstream shape the questions that can
be asked downstream — what targets are studied, what
populations the candidates were optimized for, what
biomarkers anchor the trial. Between the two ends sit
preclinical ADMET, clinical pharmacology, and trial design
and operations, each covered in dedicated notes that this
track points into rather than restates.

### Open questions

- When does a target identified from omics or genetic data
  translate into a tractable drug target, and when does the
  signal not survive validation?
- How is a generative chemistry model evaluated when its
  outputs are meant to be novel and therefore have no ground
  truth?
- How are property predictions (activity, selectivity, ADMET)
  calibrated, and how is their applicability domain
  communicated to a chemist?
- For which targets is a predicted protein structure good
  enough for structure-based design, and for which is it not?
- How should design-stage records be structured so that a
  later real-world evaluator can interpret them?
- How does AI-supported evidence cross stage gates from
  target identification through preclinical safety, first-
  in-human dosing, and pivotal trial design without losing
  version and applicability-domain information along the
  way?

### Possible prototype ideas

- A property-prediction sketch on a public molecular dataset
  (for example MoleculeNet) that compares simple baselines
  against a graph neural network and reports calibration
  alongside accuracy.
- An applicability-domain template for a property model that
  marks which compounds the model should not be trusted on.
- A documentation template that records, for a candidate
  molecule, the design rationale, the assays used, the
  applicability domain of the predictions, and the known
  caveats.
- A preclinical ADMET reporting sketch on public benchmark
  tasks (Therapeutics Data Commons ADMET group) that pairs
  ranking metrics with calibration and applicability-domain
  reporting.
- A minimal stage-gate evidence package template that
  carries AI-supported evidence from discovery into
  clinical pharmacology and trial design.

### Topical notes supporting this track

- `docs/drug-design.md` — method-level survey across the
  discovery pipeline.
- `docs/drug-discovery-program-architecture.md` — program-
  level system-of-systems view and stage gates.
- `docs/admet-and-preclinical-safety.md` — in-silico ADMET
  and preclinical safety, applicability domain, and gate
  evidence packaging.
- `docs/clinical-pharmacology-and-midd.md` — PK/PD,
  exposure-response, and the MIDD framing for
  regulatory-facing modeling.
- `docs/ai-for-clinical-trials.md` — AI in recruitment,
  site selection, external comparator arms, adaptive
  designs, and digital endpoints.
- `docs/pharma-ai-case-studies.md` — reading of
  publicly documented AI-enabled discovery and
  development programs.

### Limitations and cautions

- No candidate, target, or repurposed compound discussed in
  prototypes is positioned as suitable for clinical use.
- Generative chemistry outputs are not synthesizable
  candidates by virtue of being generated.
- Public datasets only; no proprietary compound libraries and
  no licensed assay data.

## Track 7 — AI systems architecture and management

### Motivation

Tracks 1 through 6 describe what to build and why; Track 7
describes how an AI system is designed, operated, and
managed as an engineered artifact in a healthcare
organization. The framing is systems engineering and
management: reference architecture, lifecycle, portfolio
strategy, organizational design, risk and reliability,
and formal systems methods. The aim is to put the other
tracks on a footing that can be operated, audited, and
evolved.

### Open questions

- What does a minimum viable reference architecture look
  like for a clinical AI system at a single site, and
  which interface contracts break most often in practice?
- How should stage gates for clinical ML be calibrated so
  that gate reviews change decisions rather than
  rubber-stamp them?
- Which AI capabilities are best centralized across a
  hospital network or pharma portfolio, and which belong
  per program?
- How are organizational roles (model owner, validator,
  operations, clinical champion, governance chair)
  divided so that review is independent of delivery?
- Which SLOs and failure modes are most informative for
  clinical AI, given the delay between score and
  outcome?
- Which formal methods (DSM, system dynamics, axiomatic
  design, stakeholder value) change decisions in
  practice, and which are notation overhead?

### Possible prototype ideas

- A reference-architecture description for a synthetic
  hospital AI deployment, with explicit interface
  contracts and deployment topology options.
- A reference-architecture description for a synthetic
  pharma R&D deployment that parallels the hospital
  sketch, for cross-domain comparison.
- A stage-gate artifact template covering Gates 0-9
  (problem, data, baseline, internal validation, external
  validation, shadow, go-live, operational stability,
  update, retirement) and a companion template for
  Gates M0-M9 for a discovery ML model.
- A contract catalog template (feature, prediction,
  event, outcome, audit) applied to a synthetic
  deployment, including a breaking-change scenario and
  a versioning response.
- A multi-model orchestration worksheet that labels a
  synthetic deployment with its composition patterns
  (cascade, gating, ensemble, fallback,
  champion-challenger) and the observability each
  requires.
- A failure-mode catalog and FMEA worksheet for a
  synthetic clinical AI system, with SLO candidates and
  incident-response runbook sketches.
- A Design Structure Matrix for a synthetic hospital AI
  deployment, with a paired organizational DSM showing
  coordination mismatches, and a cross-stage SoS DSM
  sketch spanning discovery through pharmacovigilance.
- A system-dynamics causal-loop diagram for alert
  fatigue, for the model-output-to-training-data
  loop, and for the DMTA cycle as a reinforcing loop.
- A build/buy/partner matrix template for a hospital AI
  capability portfolio, and a companion matrix for a
  pharma AI capability portfolio.
- An evaluation-registry template that carries a single
  model through internal, external, local, shadow,
  prospective, and monitoring evaluations with shared
  identifiers and consumers.
- An interaction-design storyboard for one clinician
  workflow and one medicinal-chemistry workflow,
  labeling staged presentation, uncertainty surfacing,
  applicability-domain flagging, override, and
  logging.

### Topical notes supporting this track

- `docs/ai-systems-architecture.md` — five-plane reference
  architecture and interface contracts.
- `docs/pharma-ai-systems-architecture.md` — the same
  decomposition specialized for pharma R&D.
- `docs/interface-contracts-for-healthcare-ai.md` —
  deep treatment of contracts between planes.
- `docs/multi-model-orchestration-patterns.md` —
  cascade, ensemble, gating, fallback, champion-
  challenger, and physics-ML hybrid composition.
- `docs/ai-lifecycle-management.md` — V-model and stage
  gates.
- `docs/pharma-ai-lifecycle-management.md` — V-model
  and Gates M0-M9 for discovery and development ML
  models, with DMTA integration.
- `docs/mlops-for-regulated-ai.md` — MLOps under SaMD,
  MIDD, GLP/GCP/GMP expectations.
- `docs/ai-evaluation-strategy.md` — evaluation as an
  architectural concern rather than a single activity.
- `docs/ai-portfolio-and-strategy.md` — capability
  maturity, build/buy/partner, real options.
- `docs/ai-organizational-design.md` — stakeholder map,
  roles, RACI, governance operating model.
- `docs/ai-risk-and-reliability.md` — FMEA, SLO/SLI,
  incident response, technical debt.
- `docs/human-ai-interaction-patterns.md` — interaction
  patterns for clinicians, chemists, and reviewers
  across the system surface.
- `docs/systems-engineering-methods.md` — DSM, system
  dynamics, axiomatic design, stakeholder value, OPM.
- `docs/pharma-ai-system-of-systems.md` — cross-stage
  SoS view of pharma AI from discovery through
  pharmacovigilance.
- `docs/drug-discovery-program-architecture.md` —
  program-level view of AI in drug discovery.

### Limitations and cautions

- Architecture and governance descriptions are
  descriptive, not prescriptive, and do not represent any
  specific institution.
- Stage gates and RACI templates are coordination devices,
  not project plans.
- Formal methods are tools; they do not decide designs.

## Cross-cutting topics

Some questions cut across more than one track and live in
their own topical notes rather than inside a single track.
These are not separate research programs; they are framings
that the tracks above need to share.

- **Clinical AI deployment case studies** —
  `docs/clinical-ai-case-studies.md`. Specific deployments
  (Epic Sepsis, Thailand diabetic retinopathy, IBM Watson,
  Duke translation pipeline) read for systems lessons.
- **Pharma AI case studies** — `docs/pharma-ai-case-studies.md`.
  Publicly documented AI-enabled discovery and
  development programs (Halicin, DSP-1181, INS018_055,
  Recursion, Isomorphic, baricitinib repositioning,
  AlphaFold lineage) read for program-level lessons.
- **Regulatory landscape** — `docs/regulatory-landscape.md`.
  FDA SaMD and Good Machine Learning Practice, EU MDR and
  the AI Act, Model-Informed Drug Development, and
  cross-jurisdiction comparison.
- **Foundation models in healthcare** —
  `docs/foundation-models-in-healthcare.md`. Clinical
  language models, multimodal medical models, and chemistry
  foundation models, with their distinct evaluation and
  deployment risks.
- **Federated and privacy-preserving learning** —
  `docs/federated-and-privacy-preserving-learning.md`.
  Federated learning, differential privacy, and their
  combinations as multi-institution training options.
- **Fairness and equity** — `docs/fairness-and-equity.md`.
  Risk score bias, imaging disparities, equity-as-opportunity
  cases, and equity questions inside the drug development
  pipeline.
- **Reproducibility in healthcare ML** —
  `docs/reproducibility-in-healthcare-ml.md`. Reproducibility
  for clinical ML and for discovery-stage chemistry ML, with
  COVID-era case material.
- **ADMET and preclinical safety** —
  `docs/admet-and-preclinical-safety.md`. In-silico ADMET,
  applicability domain, and how preclinical predictions
  enter development-candidate gate evidence.
- **Clinical pharmacology and MIDD** —
  `docs/clinical-pharmacology-and-midd.md`. PK/PD,
  exposure-response, and model-informed drug development
  as the regulatory-facing modeling layer.
- **Pharmacoepidemiology methods** —
  `docs/pharmacoepidemiology-methods.md`. Active
  comparator new-user, target trial emulation, signal
  detection, and distributed data networks.
- **Interface contracts** —
  `docs/interface-contracts-for-healthcare-ai.md`.
  Feature, prediction, event, outcome, and audit
  contracts with versioning, testing, and failure-mode
  vocabulary.
- **Multi-model orchestration patterns** —
  `docs/multi-model-orchestration-patterns.md`. Cascade,
  ensemble, gating, fallback, champion-challenger,
  physics-ML hybrid, and retrieval-augmented patterns
  for composed systems.
- **MLOps for regulated AI** —
  `docs/mlops-for-regulated-ai.md`. MLOps specialized
  for SaMD, MIDD, GLP/GCP/GMP contexts, including
  predetermined change control plans and reproducibility
  as regulatory artifact.
- **Human-AI interaction patterns** —
  `docs/human-ai-interaction-patterns.md`. Staged
  presentation, uncertainty and applicability-domain
  surfacing, override, alert staging, and logging for
  clinicians, chemists, and reviewers.
- **AI evaluation strategy** —
  `docs/ai-evaluation-strategy.md`. Evaluation as an
  architectural concern, stage-keyed evaluation types,
  slice-based evaluation, and the evaluation registry.
- **Pharma AI system of systems** —
  `docs/pharma-ai-system-of-systems.md`. Cross-stage
  view of pharma AI from discovery through
  pharmacovigilance with handoff contracts and
  emergent-behavior vocabulary.
- **AI for clinical trials** —
  `docs/ai-for-clinical-trials.md`. Recruitment and site
  selection, external comparator arms, adaptive designs,
  and digital endpoints.

Each topical note ties back into the tracks it most affects.
The notes are reading-style syntheses, not new research
programs of their own.

## Near-term prototype ideas

In rough order of how concrete they are:

- A synthetic medication-exposure and outcome generator with a
  known treatment effect and known confounders, used as a
  testbed for Track 1 methods.
- A minimal notebook for observational treatment-outcome
  analysis that labels every step with the assumption it
  depends on.
- A workflow-aware decision-support dashboard sketch on
  synthetic patient-like data, for Track 3 design questions.
- A monitoring loop over a synthetic data stream that reports
  input drift, outcome shift, and calibration changes, for
  Track 4.

Each of these is a sketch, intended to expose design questions
rather than produce evidence.

## Limitations and cautions

- Nothing here is a finished system, a validated tool, or a
  clinical product.
- No protected health information is used, and no private
  clinical datasets are accessed.
- Observational analyses are described as associations unless a
  causal design is made explicit and its assumptions are
  stated.
- Results from synthetic data illustrate methods; they do not
  support claims about real patients or real populations.
