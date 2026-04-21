# Clinical pharmacology and model-informed drug development

Notes on the quantitative layer that sits between preclinical
characterization and clinical evidence — pharmacokinetics,
pharmacodynamics, exposure-response, and the
model-informed drug development (MIDD) framework under
which these models enter regulatory review.

## Why clinical pharmacology is a systems problem

Clinical pharmacology turns a candidate's preclinical
profile into decisions about dose, schedule, population,
and label. Its models sit between the ADMET evidence
package (`docs/admet-and-preclinical-safety.md`) and the
efficacy evidence produced by trials and real-world
studies (`docs/research-agenda.md`, Track 1). MIDD is the
regulatory face of this layer: the set of practices by
which PK, PD, and related models enter FDA and EMA
decisions. A program that cannot connect its preclinical
predictions, its first-in-human PK, and its exposure-
response evidence into a single narrative has a
clinical-pharmacology gap, not a modeling gap.

## Core modeling types

- **Noncompartmental analysis.** Summary PK parameters
  (AUC, Cmax, half-life) computed directly from
  concentration-time data; the starting point for most
  first-in-human read-outs.
- **Compartmental PK.** Parametric models (one, two,
  three compartments) fit to individual or pooled data.
- **Population PK (popPK).** Nonlinear mixed-effects
  models that describe between-subject variability and
  covariate effects; Sheiner and Beal's work established
  this as the standard clinical-pharmacology language.
- **Pharmacodynamic (PD) models.** Link concentration
  to biomarker or clinical effect; direct, indirect,
  and link models each carry different assumptions
  about delay and hysteresis.
- **Exposure-response (E-R).** Joint modeling of
  exposure metrics and efficacy or safety outcomes,
  supporting dose selection and label claims.
- **Physiologically based pharmacokinetic (PBPK)
  modeling.** Mechanistic, organ-level models used for
  drug-drug interaction prediction, special populations,
  and first-in-human dose projection.
- **Quantitative systems pharmacology (QSP).**
  Mechanistic pathway models aiming to describe
  drug-target-disease interaction quantitatively; broader
  ambition, more assumptions, more scrutiny.

AI and ML methods sit alongside, not in place of, these
traditions. The pharmacometrics community has absorbed
techniques such as neural ordinary differential
equations, mixed machine-learning and mechanistic
models, and Bayesian workflows, but the decision-making
structure around dose, label, and trial design still
runs through the modeling types above.

## Model-informed drug development

The FDA MIDD paradigm encompasses the use of
exposure-based, biological, and statistical models to
support drug development and regulatory decisions. The
public-facing artifacts include:

- The MIDD paired meeting program, in which sponsors
  present modeling approaches to FDA review divisions
  before a submission.
- Guidance documents on population pharmacokinetics,
  exposure-response, PBPK, and drug-drug interaction.
- Review-side pharmacometric analyses that sometimes
  differ from sponsor analyses on the same data.

MIDD reframes modeling from a support activity into
formal evidence. That framing has implications for how
data, code, and assumptions are documented:

- **Model provenance.** Version-controlled model code,
  parameter estimates, and datasets, paired with the
  analysis scripts that produced each figure.
- **Assumption registry.** A list of structural and
  distributional assumptions, with the evidence used to
  justify each.
- **Sensitivity analyses.** Variations on key
  assumptions and covariate structures, reported as
  part of the submission rather than as an appendix.

These practices align with reproducibility expectations
elsewhere in the repository (see
`docs/reproducibility-in-healthcare-ml.md`), but MIDD
predates the current ML reproducibility discussion and
has its own conventions.

## Where ML enters

- **PopPK covariate modeling.** ML methods have been
  explored for covariate selection and model-building
  automation; the persistent question is whether a
  model that generalizes well on concentration
  prediction also supports dose and label decisions.
- **PBPK parameter estimation.** QSAR models of
  physicochemical and in-vitro ADME inputs feed PBPK
  simulations; errors in those inputs propagate into
  clinical dose predictions.
- **Biomarker discovery and PD linking.** Multi-omics
  and imaging-derived biomarkers are candidate
  quantities for PD endpoints; validation and
  qualification pathways differ from standard assay
  endpoints.
- **Digital biomarkers and endpoints.** Wearable and
  sensor data feed PD models when clinical outcomes are
  sparse. The measurement properties of digital
  endpoints are themselves a modeling problem.
- **Trial simulation.** E-R models are used to simulate
  trial outcomes under alternative designs and doses;
  ML-based disease-progression models sometimes
  augment them.

## Decisions the models support

- **First-in-human starting dose.** Preclinical PK and
  PD projected to human through allometric scaling or
  PBPK.
- **Dose escalation and stopping rules.** Bayesian
  designs (CRM, BLRM) and exposure-guided dose
  adjustments for Phase 1.
- **Dose selection for pivotal trials.** E-R analyses
  integrating Phase 2 efficacy and safety endpoints.
- **Special-population dosing.** Renal and hepatic
  impairment, pediatrics, pregnancy; often supported
  primarily by PBPK and popPK rather than by dedicated
  trials.
- **Drug-drug interaction labeling.** Static and PBPK
  predictions replace or extend dedicated DDI studies
  for low-risk combinations.
- **Post-approval label updates.** E-R evidence from
  Phase 3 and post-marketing data can expand or
  restrict dosing claims.

The common thread is that a clinical-pharmacology model
is only as valuable as the decision it supports. A
perfectly fit popPK model that does not change a dose or
label is notation, not evidence.

## Connection to other tracks and notes

- Upstream ADMET feeds first-in-human projection:
  `docs/admet-and-preclinical-safety.md`.
- Efficacy-side trial and observational evidence:
  `docs/research-agenda.md` Track 1,
  `docs/pharmacoepidemiology-methods.md`.
- Trial design with modeling inputs:
  `docs/ai-for-clinical-trials.md`.
- Program-level gate integration:
  `docs/drug-discovery-program-architecture.md`.
- Regulatory surround:
  `docs/regulatory-landscape.md`.

## Open questions

- Which parts of the clinical-pharmacology workflow are
  best served by ML augmentation, and which are better
  left to parametric pharmacometric models that
  regulators are tuned to review?
- How should an ML-derived covariate model be
  documented so that a reviewer can evaluate it without
  re-running the analysis?
- When is a QSP model decision-relevant, and when does
  its complexity outpace the data available to
  constrain it?
- How are digital endpoint measurement properties
  qualified for use in PD and E-R models?
- What does an MIDD-grade reproducibility package look
  like for a model that mixes parametric and ML
  components?

## Limitations and cautions

- Descriptions of MIDD practice here follow public
  guidance and published commentary; they are not a
  substitute for current FDA or EMA guidance.
- ML augmentation of pharmacometric workflows is an
  active research area; claims about routine regulatory
  acceptance should be checked against current
  submissions and decisions.
- QSP and digital biomarker examples are orientation,
  not validated workflows for any specific program.
- Dose and label decisions in real programs are taken
  on the totality of evidence; the modeling layer
  supports those decisions rather than making them.
