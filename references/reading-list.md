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

- Collins FS, Varmus H. *A New Initiative on Precision
  Medicine.* NEJM, 2015; 372:793-795.
  - Outlines the U.S. Precision Medicine Initiative and the
    case for genomic and clinical data in individualized care.
  - Track 2: foundational policy statement for precision
    medicine.
- Ashley EA. *Towards Precision Medicine.* Nature Reviews
  Genetics, 2016; 17:507-522.
  - Reviews technical and conceptual hurdles for integrating
    genome sequencing into clinical decision-making.
  - Track 2: comprehensive review of genomics-driven
    patient-level prediction.
- Relling MV, Evans WE. *Pharmacogenomics in the Clinic.*
  Nature, 2015; 526:343-350.
  - Synthesizes evidence for actionable pharmacogenes and
    barriers to translating pharmacogenomics into prescribing.
  - Track 2: pharmacogenomics implementation in routine care.
- Miotto R, Li L, Kidd BA, Dudley JT. *Deep Patient: An
  Unsupervised Representation to Predict the Future of Patients
  from the Electronic Health Records.* Scientific Reports, 2016;
  6:26094.
  - Demonstrates deep learning on EHR data from ~700K patients
    for general-purpose disease prediction.
  - Track 2: early deep learning approach to patient-level risk
    stratification from clinical records.
- Topol EJ. *High-Performance Medicine: The Convergence of
  Human and Artificial Intelligence.* Nature Medicine, 2019;
  25:44-56.
  - Reviews AI capabilities at clinician, health system, and
    patient levels, noting bias and transparency limitations.
  - Track 2: authoritative overview connecting AI to
    individualized care.

## Multimodal healthcare data integration

- Acosta JN, Falcone GJ, Rajpurkar P, Topol EJ. *Multimodal
  Biomedical AI.* Nature Medicine, 2022; 28:1773-1784.
  - Surveys the landscape of multimodal AI in health,
    identifying data heterogeneity and privacy as principal
    barriers.
  - Track 2: leading review of biomedical multimodal fusion
    challenges.
- Baltrusaitis T, Ahuja C, Morency L-P. *Multimodal Machine
  Learning: A Survey and Taxonomy.* IEEE TPAMI, 2019;
  41(2):423-443.
  - Proposes a taxonomy of five core multimodal ML challenges:
    representation, translation, alignment, fusion, co-learning.
  - Track 2: foundational methodological taxonomy for fusion
    work.
- Stahlschmidt SR, Ulfenborg B, Synnergren J. *Multimodal Deep
  Learning for Biomedical Data Fusion: A Review.* Briefings in
  Bioinformatics, 2022; 23(2):bbab569.
  - Reviews deep fusion strategies for biomedical applications
    and proposes a taxonomy of architectures.
  - Track 2: fusion architecture selection for clinical,
    genomic, and imaging data.
- Chen RJ, Lu MY, Williamson DFK, et al. *Pan-Cancer
  Integrative Histology-Genomic Analysis via Multimodal Deep
  Learning.* Cancer Cell, 2022; 40(8):865-878.
  - Fuses whole-slide pathology images with genomic profiles
    across 14 cancer types for survival prediction.
  - Track 2: large-scale demonstration of histopathology and
    multi-omic fusion.
- Lipkova J, Chen RJ, Chen B, et al. *Artificial Intelligence
  for Multimodal Data Integration in Oncology.* Cancer Cell,
  2022; 40(10):1095-1110.
  - Reviews AI for integrating radiology, histology, genomics,
    and EHR data, addressing missing-modality challenges.
  - Track 2: cross-modality heterogeneity and deployability.

## Clinical decision support and workflow integration

- Bates DW, Kuperman GJ, Wang S, et al. *Ten commandments for
  effective clinical decision support: making the practice of
  evidence-based medicine a reality.* JAMIA, 2003;
  10(6):523-530.
  - Distills CDS implementation experience into ten principles
    including workflow integration and point-of-care delivery.
  - Track 3: foundational framework for CDS design.
- Kawamoto K, Houlihan CA, Balas EA, Lobach DF. *Improving
  clinical practice using clinical decision support systems: a
  systematic review of trials to identify features critical to
  success.* BMJ, 2005; 330(7494):765.
  - Systematic review of 70 RCTs finding four features critical
    to CDS success, including automatic workflow integration.
  - Track 3: most cited evidence base for CDS adoption factors.
- Middleton B, Sittig DF, Wright A. *Clinical decision support:
  a 25 year retrospective and a 25 year vision.* Yearbook of
  Medical Informatics, 2016; Suppl 1:S103-S116.
  - Reviews 25 years of CDS evolution and projects a
    forward-looking vision through 2040.
  - Track 3: definitive historical survey of the CDS field.

## Deployment-aware AI systems

- Sculley D, Holt G, Golovin D, et al. *Hidden technical debt
  in machine learning systems.* NeurIPS, 2015.
  - Argues real-world ML systems incur massive maintenance costs
    from feedback loops, entanglement, and data dependencies.
  - Track 3: foundational paper on why ML systems fail in
    production.
- Kelly CJ, Karthikesalingam A, Suleyman M, et al. *Key
  challenges for delivering clinical impact with artificial
  intelligence.* BMC Medicine, 2019; 17:195.
  - Maps the gap between benchmark performance and real-world
    clinical impact for healthcare AI.
  - Track 3: position paper on deployment barriers.
- Subbaswamy A, Saria S. *From development to deployment:
  dataset shift, causality, and shift-stable models in health
  AI.* Biostatistics, 2020; 21(2):345-352.
  - Proposes a causal framework for anticipating distribution
    shifts during model training rather than post-deployment.
  - Track 3 and 4: shift-stable model design.
- Beede E, Baylor E, Hersch F, et al. *A human-centered
  evaluation of a deep learning system deployed in clinics for
  the detection of diabetic retinopathy.* ACM CHI, 2020.
  - Reports that Google's DR screening AI encountered
    significant real-world deployment challenges across 11 Thai
    clinics despite >90% lab accuracy.
  - Track 3: canonical case study of lab-to-clinic gap.

## Human-centered AI and interpretability

- Ribeiro MT, Singh S, Guestrin C. *"Why should I trust you?":
  Explaining the predictions of any classifier.* ACM KDD, 2016;
  1135-1144.
  - Introduces LIME for model-agnostic local explanations via
    interpretable surrogate models.
  - Track 3: foundational paper for local post-hoc
    explanations.
- Lundberg SM, Lee SI. *A unified approach to interpreting
  model predictions.* NeurIPS, 2017; 4766-4777.
  - Presents SHAP values as the unique additive feature
    attribution method satisfying key axioms.
  - Track 3: dominant feature-attribution method in clinical ML.
- Rudin C. *Stop explaining black box machine learning models
  for high stakes decisions and use interpretable models
  instead.* Nature Machine Intelligence, 2019; 1:206-215.
  - Argues post-hoc explanations are fundamentally unreliable
    for high-stakes domains like healthcare.
  - Track 3: most influential critique of the post-hoc
    explanation paradigm.
- Tonekaboni S, Joshi S, McCradden MD, Goldenberg A. *What
  clinicians want: contextualizing explainable machine learning
  for clinical end use.* MLHC, PMLR 106:359-380, 2019.
  - Surveys clinicians to identify what ML explanations they
    actually find useful, finding needs are context-dependent.
  - Track 3: user study grounding interpretability in clinical
    needs.

## Monitoring and dataset shift

- TODO: add surveys of dataset shift.
- TODO: add papers on monitoring in healthcare AI.
- TODO: add reports from deployed monitoring systems.

## Governance and safety

- TODO: add regulatory and policy frameworks.
- TODO: add institutional governance templates.
- TODO: add incident reports and post-mortems.
