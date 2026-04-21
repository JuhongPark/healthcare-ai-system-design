# Pharmacoepidemiology methods

Notes on observational study designs that specifically
address drug exposure, outcome, and confounding in healthcare
data — the methodological layer beneath the real-world
evidence discussion in Track 1.

## Why a separate note

The real-world-evidence and causal-inference categories in
the literature map cover general observational methodology.
Pharmacoepidemiology is narrower: it is the applied
discipline for treatment-outcome questions in pharmacy-,
claims-, and EHR-based data. Its design choices — active
comparator selection, index-date anchoring, exposure window,
washout, new-user restriction — are the parameters that
decide whether a study is defensible or confounded by
indication. They are also the parameters that AI methods
applied to RWE either help or silently break.

## Reference designs

- **Active comparator, new-user (ACNU).** Compare
  initiators of drug A to initiators of an active
  comparator drug B for the same indication, with a
  washout requiring no prior use of either. Lund,
  Richardson, and Sturmer (2015) formalized the
  rationale: confounding by indication and healthy-user
  effects are attenuated when both arms reflect a
  treatment decision.
- **Prevalent-user bias.** Comparing prevalent users to
  non-users conflates initiation, persistence, and
  survival. Ray (2003) argued that pharmacoepidemiologic
  studies should restrict to new users to avoid this
  bias.
- **Self-controlled designs.** Self-controlled case
  series (SCCS) and case-crossover designs use each
  patient as their own control, removing time-invariant
  confounding; they are useful for acute-onset outcomes
  and episodic exposures.
- **Target trial emulation.** Hernan and Robins (2016)
  framed observational analysis as emulation of a
  hypothetical randomized trial; design choices
  (eligibility, assignment, follow-up, outcome) are
  stated in trial terms so that violations are
  inspectable.
- **Instrumental variables.** When an instrument is
  plausible (physician preference, calendar time,
  geographic variation), IV analysis can address
  unobserved confounding; the assumptions are strong
  and contestable in most clinical settings.

## Confounding adjustment

- **Propensity scores.** Matching, stratification,
  weighting, and covariate adjustment based on the
  propensity score (Rosenbaum and Rubin, 1983). Balance
  diagnostics and effective sample size reports belong
  with any propensity-score analysis.
- **High-dimensional propensity scores.** Schneeweiss et
  al. (2009) described empirical covariate generation
  from claims data; still the reference for large,
  noisy covariate spaces.
- **Disease risk scores and doubly robust methods.**
  Alternative or complementary adjustments when the
  propensity model is fragile.
- **E-values and quantitative bias analysis.**
  VanderWeele and Ding (2017) operationalized residual
  confounding in an interpretable metric; more elaborate
  quantitative bias analysis traces specific
  assumptions.

## Signal detection and post-marketing surveillance

Once a drug is on the market, observational data are the
primary evidence stream for safety signals. Characteristic
methods:

- **Disproportionality analysis.** Reporting odds
  ratios, proportional reporting ratios, and Bayesian
  shrinkage methods applied to spontaneous reporting
  systems (FDA FAERS, WHO VigiBase). Noren et al.'s
  work on information-component-based methods is the
  reference point.
- **Sequential monitoring.** Group sequential and
  conditional sequential designs used in the FDA
  Sentinel System for active surveillance in claims
  and EHR data.
- **Tree-based scan and LASSO signal detection.**
  Extensions that scale to many exposure-outcome pairs
  with error-rate control.
- **NLP on unstructured reports.** Signal extraction
  from adverse-event narratives and EHR notes; Ball and
  Dal Pan (2022) review readiness for pharmacovigilance.

The balance between sensitivity, specificity, and
adjudication workload is the working constraint of any
post-marketing system, not the choice of model.

## Distributed data networks

Multi-site observational research happens largely on
distributed networks that share a common data model
rather than a pooled dataset:

- **OHDSI and OMOP.** Hripcsak et al. (2015) introduced
  the OHDSI collaboration on the OMOP Common Data Model;
  it is the largest international substrate for
  reproducible observational analyses.
- **FDA Sentinel System.** Active safety surveillance
  across U.S. health plans and EHR partners, built on
  the Sentinel Common Data Model and a catalog of
  standardized analytic programs.
- **PCORnet.** Patient-centered outcomes network with
  a distinct common data model, oriented toward
  comparative effectiveness.
- **European ENCePP and national registries.** Local
  and regional infrastructures with their own data
  standards and governance.

Distributed networks change the technical footprint:
analyses are executed locally, only summary results
cross the boundary, and the common data model is a
load-bearing assumption. When it drifts or is
implemented differently, a multi-site result can be
wrong in ways that look coherent.

## Where ML helps, where it hurts

Machine-learning methods enter pharmacoepidemiology at
several points:

- **Phenotype definition.** ML classifiers can extract
  cohort membership from unstructured text; they
  typically succeed or fail on sensitivity and
  specificity at the concept level rather than at the
  aggregate level.
- **High-dimensional confounder identification.**
  Beyond the hdPS approach, ML confounder selection
  risks including instruments and mediators unless
  domain structure is enforced.
- **Outcome modeling.** Flexible outcome regression
  underpins doubly robust and g-methods approaches;
  instability in small cohorts can undo the theoretical
  advantage.
- **Matching and balance.** Embedding-based matching
  and targeted learning methods extend classical
  propensity-score workflows; their gains are design
  dependent.

The recurring failure mode is a flexible model that
optimizes prediction accuracy rather than bias
reduction. Pharmacoepidemiology rewards designs that
are transparent about their assumptions, not models
that are opaque about their confounding structure.

## Connection to other notes

- Upstream design: `docs/drug-design.md`,
  `docs/admet-and-preclinical-safety.md`, and
  `docs/clinical-pharmacology-and-midd.md` shape what
  observational questions are worth asking about a
  candidate.
- Trial-side counterparts:
  `docs/ai-for-clinical-trials.md` covers synthetic
  controls and external comparator arms, which sit at
  the boundary of trial and observational evidence.
- Track 1 prototype: the `prototypes/rwe-drug-efficacy-sketch`
  illustrates design choices on synthetic data that are
  framed in the language of this note.
- Regulatory surround:
  `docs/regulatory-landscape.md` and the FDA RWE
  framework.

## Open questions

- How should cohort definitions be versioned and shared
  so that a reader can rerun a study on a different
  data source without reinventing inclusion logic?
- When does an ML-derived phenotype improve outcome
  ascertainment, and when does it encode institutional
  documentation practice rather than clinical state?
- Which signal-detection methods have track records
  that justify a specific acceptance threshold, and
  which are still benchmark-stage?
- How are distributed-network analyses audited when
  only summary results leave the site?
- What is the analog of target trial emulation for
  repurposing hypotheses that start from discovery-stage
  evidence?

## Limitations and cautions

- This note describes methodology at a high level; any
  specific study should be designed against current
  guidance (FDA RWE framework, ICH, ISPE recommendations)
  and domain input.
- Examples from OHDSI, Sentinel, and FAERS are cited to
  orient readers; they are not endorsements of any
  particular analytic program or finding.
- Method choices in pharmacoepidemiology interact
  strongly with data source, indication, and outcome
  timing; importing a design across settings without
  re-examining assumptions is a common failure mode.
- None of the methods here promote an observational
  association to a causal claim by themselves; the
  causal claim is a design decision supported by
  method, not an output of a method.
