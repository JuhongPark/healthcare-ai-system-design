# MLOps for regulated AI

Notes on MLOps practice adapted for regulated healthcare
and pharma contexts — SaMD for clinical AI, MIDD for
pharmacometric and pharmacokinetic models, and the
GLP/GCP/GMP expectations that shape data and process
discipline at each stage.

## Why regulated MLOps is different

General MLOps literature (Amershi et al., 2019; Paleyes
et al., 2022; Kreuzberger et al., 2023) treats
reproducibility, deployment, and monitoring as
engineering practice. In regulated settings the same
practices become regulatory evidence. A pipeline that
"works" is not enough; the pipeline's design,
documentation, and changes must withstand external
review years after the fact. Regulated MLOps is the
intersection of the engineering discipline and the
review surface it has to present.

## Two regulatory surfaces

Healthcare and pharma AI systems answer to different
regulatory regimes, often simultaneously:

- **Software as a Medical Device (SaMD).** A clinical
  AI system acting on a patient-specific input
  typically falls under FDA 21 CFR 820 (Quality System
  Regulation) or the incoming Quality Management System
  Regulation, EU MDR, or jurisdictional equivalents.
  Good Machine Learning Practice guiding principles
  (FDA, Health Canada, MHRA, 2021) and the
  Predetermined Change Control Plans (PCCP) guidance
  (2023) set expectations.
- **Model-Informed Drug Development (MIDD).** Models
  used to support regulatory decisions about a drug
  (popPK, PBPK, E-R, QSP) enter FDA and EMA submissions
  through pharmacometric review. Documentation is
  governed by guidance documents on each model class,
  and by cross-cutting good practices (Marshall et al.,
  2016).

A single program can touch both. A chemistry ML system
predicting ADMET is not a regulated device but its
outputs may feed regulatory evidence for a submission;
a clinical AI deployed at a hospital is a device but its
operator is also the validator.

## Reproducibility as a regulatory artifact

In regulated MLOps, reproducibility is not only a
research virtue:

- **Dataset provenance.** Every training and evaluation
  dataset is recorded with source, snapshot time,
  inclusion/exclusion logic, and access authority.
- **Code provenance.** Source repository state
  (commit hash, tag), build environment (lockfiles,
  container digests), and dependency versions are
  captured per artifact.
- **Deterministic builds.** Training runs are
  deterministic where possible; where not, the sources
  of nondeterminism (GPU nondeterminism, stochastic
  sampling) are documented and bounded.
- **Parameter captures.** Hyperparameters, split
  policies, random seeds, and checkpointing behavior
  live with the model registry entry, not scattered in
  notebooks.
- **Re-execution.** A reviewer years later should be
  able to re-run the analysis from the archived
  artifacts.

The test is not whether code runs but whether the
evidence package can reproduce the submitted numbers
from the archived inputs.

## Predetermined change control plans

PCCPs (FDA/HC/MHRA 2023) define, up front, the kinds of
model changes a sponsor intends to make over the
operational life of the device, and the validation
regime for each. The architectural implications:

- **Change taxonomy.** A list of change types —
  retraining on new data, hyperparameter updates,
  feature additions, architecture changes — with each
  one's validation regime.
- **Validation thresholds.** For each change type,
  the pre-stated acceptance criteria.
- **Monitoring that feeds the PCCP.** Metrics defined
  at go-live are the inputs the PCCP uses to judge
  post-release performance.
- **Automation with oversight.** Changes inside the
  PCCP envelope can ship with prescribed governance;
  changes outside require a new submission.

A PCCP well-integrated into MLOps turns update
governance (see `docs/ai-lifecycle-management.md`) into
an auditable, largely automated discipline.

## MIDD-grade documentation

For pharmacometric and related models:

- **Model description.** Structural model, error model,
  covariate model, with each decision motivated against
  the data and prior knowledge.
- **Assumption registry.** Every structural and
  distributional assumption listed, with the evidence
  or prior that justifies it.
- **Sensitivity analyses.** Key assumptions varied and
  reported alongside the primary analysis.
- **Simulation-based diagnostics.** Visual predictive
  checks, numerical predictive checks, posterior
  predictive checks as appropriate.
- **Dataset documentation.** Source trials, study data
  tabulation model (SDTM) provenance, included and
  excluded observations with reasons.
- **Code and artifact archive.** Analysis scripts,
  model control streams, estimation output, all
  runnable from archive.

The Marshall et al. (2016) good practices document and
the FDA population PK guidance (2022) set expectations
that MLOps for pharmacometrics has to meet.

## GLP, GCP, and GMP intersections

Regulated pharma AI sits inside broader quality systems
that govern how data are generated and handled:

- **Good Laboratory Practice (GLP).** Governs
  nonclinical safety studies. AI models that consume
  GLP data — often preclinical toxicology and
  pharmacokinetic studies — inherit audit-trail and
  change-control expectations for that data.
- **Good Clinical Practice (GCP).** Governs clinical
  trial conduct. AI used in trial operations (see
  `docs/ai-for-clinical-trials.md`) touches GCP when
  it influences eligibility, enrollment, or endpoint
  ascertainment.
- **Good Manufacturing Practice (GMP).** Governs
  manufacturing and release of clinical-trial and
  commercial product. AI used in process analytical
  technology and in-process control sits inside the
  GMP quality system.

The architectural question is not "is the model
regulated" but "which quality system governs each input
and output", and whether the MLOps practice integrates
with those systems or requires a parallel track.

## Access control and data minimization

Regulated MLOps adds specificity to generic access
control:

- **Purpose-of-use tags.** Each access is tagged with
  why, not only by whom.
- **Role separation.** Validators, developers, and
  operators have distinct roles; combining them is a
  governance failure (see
  `docs/ai-organizational-design.md`).
- **Data minimization.** The minimum necessary data
  reaches each stage; training data carry different
  access rules from serving features.
- **Cross-boundary transfer.** Where data cross
  organizational boundaries (CRO, cloud, partner),
  the transfer is covered by an explicit agreement
  that names the contracts in
  `docs/interface-contracts-for-healthcare-ai.md`.

## Continuous learning under regulation

Systems that learn from new data during operational life
present specific MLOps challenges:

- **Training-data drift.** Incorporating new data must
  not silently shift the intended-use population;
  population monitoring is a separate monitor from
  performance monitoring.
- **Evaluation lock-in.** A frozen evaluation set used
  across model versions enables comparison but becomes
  stale; refresh schedules are governance decisions.
- **Rollback semantics.** Rolling back a continually-
  learning model means returning to a specific
  snapshot; the snapshot cadence is a policy choice.
- **Regulatory notification.** Continual learning does
  not remove change-control obligations; PCCPs either
  cover the learning protocol or the learning is
  stopped and retraining happens under explicit change
  control.

## Incident response in regulated contexts

An incident in a regulated AI system is also a
regulatory event when it meets threshold criteria:

- **Reportable events.** Adverse events tied to model
  output, safety-related software malfunctions, or
  labeling inaccuracies; reporting timelines are set
  by regulation, not by internal policy.
- **Hold orders.** The capacity to stop inference or
  stop a model's use across deployment sites must exist
  and must be testable.
- **Postmortem discipline.** Incident analyses need to
  meet internal quality-system expectations for CAPA
  (corrective and preventive action).

## Connection to other notes

- Lifecycle and stage gates:
  `docs/ai-lifecycle-management.md` and the pharma
  counterpart `docs/pharma-ai-lifecycle-management.md`.
- Regulatory landscape:
  `docs/regulatory-landscape.md`.
- Interface contracts that carry regulatory obligations
  across boundaries:
  `docs/interface-contracts-for-healthcare-ai.md`.
- Reproducibility discipline in research:
  `docs/reproducibility-in-healthcare-ml.md`.
- Reliability posture:
  `docs/ai-risk-and-reliability.md`.

## Open questions

- Which PCCP change categories are most commonly
  submitted and accepted, and what do they look like
  in practice?
- How should MIDD documentation discipline and
  clinical-SaMD documentation discipline be unified for
  a sponsor that runs both programs?
- What does a minimum viable regulated-MLOps pipeline
  look like for a single-site hospital deploying a
  vendor-supplied device?
- How are cloud-hosted components brought into the
  quality system, and what certifications substitute
  for direct audit?
- When a model is continually learning, what is the
  smallest unit of change that still triggers PCCP
  review?

## Limitations and cautions

- This note synthesizes public guidance and industry
  practice; specific regulatory submissions must be
  developed against current guidance and regulator
  feedback, not against summaries.
- Regulatory expectations around AI and ML in medical
  devices and drug development are evolving quickly;
  some of the patterns described here will be
  superseded.
- Quality-system integration depends on the
  organization's existing GLP/GCP/GMP infrastructure;
  a retrofit of AI practice onto a legacy quality
  system is often where the work is.
- Continual-learning descriptions here are orientation;
  operational continual learning inside a regulated
  medical device remains rare in current approvals.
