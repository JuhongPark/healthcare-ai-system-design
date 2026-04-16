# Reading list

List of readings to add, organized by the same categories as
`docs/literature-map.md`. No citations have been invented —
items are TODO placeholders until a verified reference is
added.

Format, once a real reference is added:

    - Author(s). *Title.* Venue, Year. [link]
      - One-sentence summary of what the reading argues or reports.
      - Why it is here (which track, which question).

## Drug efficacy evaluation

- ICH. *ICH E9(R1) Addendum on Estimands and Sensitivity
  Analysis in Clinical Trials.* ICH, 2019.
  - Regulatory framework defining how trial objectives
    translate into estimands and sensitivity analyses.
  - Track 1: foundational standard for efficacy endpoints.
- Kent DM, Steyerberg EW, van Klaveren D. *Personalized
  evidence based medicine: predictive approaches to
  heterogeneous treatment effects.* BMJ, 2018; 363:k4245.
  - Reviews risk-based approaches for predicting HTE at
    the individual patient level.
  - Track 1: why average treatment effects can mislead.
- Kent DM, Paulus JK, van Klaveren D, et al. *The Predictive
  Approaches to Treatment effect Heterogeneity (PATH)
  Statement.* Annals of Internal Medicine, 2020; 172(1):35-45.
  - Consensus guidance recommending routine HTE examination
    using baseline risk as the primary dimension.
  - Track 1: methodological standard for HTE in trials.

## Real-world evidence and observational healthcare data

- U.S. FDA. *Framework for FDA's Real-World Evidence Program.*
  FDA, 2018.
  - Defines when and how RWE from EHR, claims, and registries
    can support regulatory decisions.
  - Track 1: foundational regulatory document for RWE.
- Hripcsak G, Duke JD, Shah NH, et al. *Observational Health
  Data Sciences and Informatics (OHDSI): Opportunities for
  Observational Researchers.* Studies in Health Technology and
  Informatics, 2015; 216:574-578.
  - Introduces the OHDSI collaborative and OMOP-based
    infrastructure for reproducible observational studies.
  - Track 1: largest international RWE data infrastructure.
- Hernan MA, Robins JM. *Using Big Data to Emulate a Target
  Trial When a Randomized Trial Is Not Available.* American
  Journal of Epidemiology, 2016; 183(8):758-764.
  - Formalizes target trial emulation for designing rigorous
    causal studies from observational data.
  - Track 1: foundational cohort construction methodology.

## Comparative effectiveness and treatment outcomes

- Lund JL, Richardson DB, Sturmer T. *The Active Comparator,
  New User Study Design in Pharmacoepidemiology.* Current
  Epidemiology Reports, 2015; 2:221-228.
  - Reviews the ACNU design for reducing confounding by
    indication by comparing active treatment initiators.
  - Track 1: standard design for observational CER.
- Concato J, Shah N, Horwitz RI. *Randomized, Controlled
  Trials, Observational Studies, and the Hierarchy of Research
  Designs.* NEJM, 2000; 342(25):1887-1892.
  - Shows well-designed observational studies do not
    systematically overestimate treatment effects vs. RCTs.
  - Track 1: landmark challenge to the rigid evidence hierarchy.
- Schneeweiss S, Rassen JA, Glynn RJ, et al. *High-dimensional
  Propensity Score Adjustment in Studies of Treatment Effects
  Using Health Care Claims Data.* Epidemiology, 2009;
  20(4):512-522.
  - Algorithm that empirically identifies hundreds of potential
    confounders from claims data for propensity score models.
  - Track 1: scalable confounder adjustment for claims data.

## Causal inference and association limits

- Rosenbaum PR, Rubin DB. *The Central Role of the Propensity
  Score in Observational Studies for Causal Effects.* Biometrika,
  1983; 70(1):41-55.
  - Proves conditioning on the propensity score removes bias
    from all observed covariates.
  - Track 1: foundational paper for propensity score methods.
- VanderWeele TJ, Ding P. *Sensitivity Analysis in
  Observational Research: Introducing the E-Value.* Annals of
  Internal Medicine, 2017; 167(4):268-274.
  - Introduces the E-value for quantifying robustness to
    unmeasured confounding.
  - Track 1: practical sensitivity analysis tool.
- Lipsitch M, Tchetgen Tchetgen E, Cohen T. *Negative Controls:
  A Tool for Detecting Confounding and Bias in Observational
  Studies.* Epidemiology, 2010; 21(3):383-388.
  - Formalizes negative control exposures and outcomes as
    diagnostic tools for unmeasured confounding.
  - Track 1: standard falsification check for observational
    studies.
- Hernan MA, Robins JM. *Causal Inference: What If.* Chapman &
  Hall/CRC, 2020.
  - Comprehensive textbook covering counterfactual theory,
    causal diagrams, IPW, and target trial emulation.
  - Track 1: definitive reference for modern causal inference.

## Precision medicine

- TODO: add overviews of precision medicine concepts.
- TODO: add critical reviews.
- TODO: add patient-communication studies.

## Multimodal healthcare data integration

- TODO: add reviews of multimodal medical learning.
- TODO: add papers on missing-modality robustness.
- TODO: add papers on cross-site and cross-modality validation.

## Clinical decision support and workflow integration

- TODO: add histories and reviews of clinical decision support.
- TODO: add post-mortems of deployed systems.
- TODO: add studies on workflow and adoption.

## Deployment-aware AI systems

- TODO: add reviews of deployment-aware machine learning.
- TODO: add case studies of deployed medical AI systems.
- TODO: add frameworks for validation and monitoring stages.

## Human-centered AI and interpretability

- TODO: add surveys of interpretability methods.
- TODO: add user studies on explanation use.
- TODO: add critiques of interpretability claims.

## Monitoring and dataset shift

- TODO: add surveys of dataset shift.
- TODO: add papers on monitoring in healthcare AI.
- TODO: add reports from deployed monitoring systems.

## Governance and safety

- TODO: add regulatory and policy frameworks.
- TODO: add institutional governance templates.
- TODO: add incident reports and post-mortems.
