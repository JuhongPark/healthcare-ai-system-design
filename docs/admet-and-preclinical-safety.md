# ADMET and preclinical safety

Notes on AI methods applied to absorption, distribution,
metabolism, excretion, and toxicity — the preclinical stage
where many candidates fail and where model predictions have
to survive an expensive experimental check.

## Why ADMET and preclinical safety deserve their own note

The drug design note treats ADMET as a line inside the
optimization loop. In program economics it is much more than
that: attrition at preclinical and early clinical stages is
dominated by safety and pharmacokinetic failures, not by a
lack of potency against the primary target. A model that
nominates a potent compound whose metabolism cannot be fixed
has not helped the program. ADMET prediction is therefore a
place where method behavior, data quality, and portfolio
economics all meet at the same decision.

## What ADMET models predict

Typical end points handled by in-silico models:

- **Absorption.** Solubility, Caco-2 permeability, membrane
  partitioning, human intestinal absorption.
- **Distribution.** Plasma protein binding, volume of
  distribution, blood-brain barrier penetration, tissue
  distribution.
- **Metabolism.** Cytochrome P450 inhibition and substrate
  status, metabolic stability (microsomal, hepatocyte),
  reactive metabolite formation.
- **Excretion.** Clearance, half-life, transporter
  involvement.
- **Toxicity.** hERG inhibition and cardiotoxicity, hepatotoxicity,
  genotoxicity signals (Ames), acute toxicity, carcinogenicity
  hazard flags, reproductive and developmental toxicity.

Each end point has its own assay, its own noise profile, and
its own reference dataset. A single ADMET model is rarely one
model; it is a portfolio of models with correlated but
distinct behavior.

## Data sources and their limits

- **Public datasets.** Tox21, ToxCast, ClinTox, SIDER, and
  the Therapeutics Data Commons ADMET Benchmark Group expose
  open end-point data; they are standard benchmarking
  substrates but underrepresent proprietary assay conditions.
- **Chemistry databases.** ChEMBL and PubChem provide
  activity-labeled compounds, but ADMET coverage is partial
  and assay protocols differ.
- **In-house assay data.** The dominant signal inside a pharma
  program; rarely released, heavily filtered by project
  selection, and often imbalanced across chemotype and
  concentration.
- **Regulatory documents.** FDA Adverse Event Reporting
  System and Summary Basis of Approval content capture
  clinical signals but do not speak to preclinical
  predictions in matched form.

Data quality for ADMET is asymmetric — some end points
(hERG, logP) have abundant consistent data; others
(idiosyncratic hepatotoxicity, carcinogenicity) are rare
events where public benchmarks overstate achievable
accuracy.

## Methods

- **Classical QSAR.** Descriptor-based regression and
  classification models; still competitive on small, clean
  datasets.
- **Graph neural networks.** Chemprop (Yang et al., 2019)
  and successors treat the molecule as a graph and learn
  representations end to end; strong baselines on public
  ADMET tasks.
- **Chemistry foundation models.** Pretrained molecular
  language models and graph models (ChemBERTa, MoLFormer,
  Uni-Mol) feed downstream property heads; gains are
  dataset-dependent.
- **Multitask and transfer learning.** ADMET end points
  correlate; joint training or transfer from related tasks
  is often more data-efficient than single-task models.
- **Physics-grounded models.** Physiologically based
  pharmacokinetic (PBPK) modeling and free-energy methods
  sit alongside learned models and are sometimes more
  interpretable to toxicologists and regulators.

The reading list records the Bender and Cortes-Ciriano
critiques (2021) as a corrective to claims about in-silico
ADMET replacing experiment; the position here follows that
reading — models accelerate and prioritize, they do not
replace preclinical safety evaluation.

## Evaluation and applicability domain

- **Scaffold and time splits.** Random splits on molecule
  data overestimate generalization because of chemotype
  clustering; scaffold splits and time-based holdouts are
  stricter and more realistic.
- **Calibration.** A well-calibrated probability is more
  useful than a higher AUC when the output enters a
  threshold-driven gate. Reliability diagrams and Brier
  scores belong alongside ranking metrics.
- **Applicability domain.** A prediction outside the region
  of chemistry the model saw in training is an
  extrapolation. The applicability domain of an ADMET
  model should be reported with each prediction, not
  inferred later by the consumer.
- **Negative and prospective controls.** Retrospective
  benchmark numbers do not establish prospective
  performance. Programs that track prospective prediction
  vs. assay readouts over time get the only honest
  accuracy number they will have.

## Propagation to program decisions

An ADMET prediction rarely decides a compound on its own;
it feeds a lead optimization cycle and, eventually, a
development candidate gate. Design choices that shape
whether predictions do useful work:

- **Integration with design-make-test-analyze (DMTA).**
  Predictions enter the design step, assay readouts update
  the training set, and the cycle closes faster than
  either humans or models would on their own.
- **Confidence-aware prioritization.** High-confidence
  negative predictions filter cheaply; low-confidence
  predictions trigger early experimental check rather than
  late-stage surprise.
- **Gate evidence packaging.** At a development candidate
  gate (see `docs/drug-discovery-program-architecture.md`),
  an ADMET prediction is documented with its model version,
  applicability domain, and matched experimental result,
  so the reviewer can separate the prediction from the
  confirmation.

## Regulatory posture

Regulators accept in-silico evidence for certain
preclinical end points. ICH M7 (2017) on genotoxicity
impurities explicitly allows two complementary
(Q)SAR models for DNA reactivity assessment. The FDA
Model-Informed Drug Development framework
(`docs/clinical-pharmacology-and-midd.md`) covers PBPK and
population PK submissions but not general ML ADMET
models. Expectations for broader in-silico safety evidence
are evolving; the defensible posture is to document
methods at the level a reviewer can audit rather than to
claim parity with in-vivo evidence.

## Open questions

- How should applicability-domain statements for ADMET
  models be standardized across a program portfolio so
  they are comparable across chemotypes and projects?
- When is a multitask ADMET model worth the maintenance
  burden relative to a set of single-task models, given
  heterogeneous data release cadence?
- How is prospective accuracy of ADMET predictions
  tracked over program lifetime, and how is the tracking
  fed back into gate evidence?
- Where does PBPK modeling complement learned ADMET
  models, and where does it compete?
- What does an auditable ADMET evidence package look
  like for a development candidate, and how is it
  connected to the clinical pharmacology package that
  follows?

## Relationship to other notes

- Method-level context: `docs/drug-design.md` (property
  prediction, active learning).
- Program-level context:
  `docs/drug-discovery-program-architecture.md` (stage-gate
  architecture, capability sourcing).
- Downstream handoff:
  `docs/clinical-pharmacology-and-midd.md` (PK/PD and
  exposure-response modeling that inherits ADMET
  assumptions).
- Post-approval feedback: `docs/drug-design.md`
  pharmacovigilance section and
  `docs/pharmacoepidemiology-methods.md`.

## Limitations and cautions

- No claim is made that any ADMET method here replaces
  experimental evaluation. Preclinical safety is
  ultimately validated in assay, in animal, and in
  clinic.
- Public ADMET benchmarks reflect the assay conditions
  and compound distributions of their sources; benchmark
  ranking is not a substitute for prospective program
  performance.
- Applicability domain statements are necessary but not
  sufficient; a prediction inside the domain can still
  be wrong, and domain definitions vary across
  implementations.
- Regulatory acceptance of in-silico safety evidence is
  end-point specific and jurisdiction specific; general
  claims about acceptance should be checked against
  current guidance.
