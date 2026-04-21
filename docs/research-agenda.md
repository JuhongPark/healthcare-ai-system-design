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
biomarkers anchor the trial.

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

### Limitations and cautions

- No candidate, target, or repurposed compound discussed in
  prototypes is positioned as suitable for clinical use.
- Generative chemistry outputs are not synthesizable
  candidates by virtue of being generated.
- Public datasets only; no proprietary compound libraries and
  no licensed assay data.

## Cross-cutting topics

Some questions cut across more than one track and live in
their own topical notes rather than inside a single track.
These are not separate research programs; they are framings
that the tracks above need to share.

- **Clinical AI deployment case studies** —
  `docs/clinical-ai-case-studies.md`. Specific deployments
  (Epic Sepsis, Thailand diabetic retinopathy, IBM Watson,
  Duke translation pipeline) read for systems lessons.
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
