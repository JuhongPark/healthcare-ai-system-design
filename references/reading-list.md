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

- Finlayson SG, Subbaswamy A, Singh K, et al. *The Clinician
  and Dataset Shift in Artificial Intelligence.* NEJM, 2021;
  385(3):283-286.
  - Introduces dataset shift as a key failure mode for clinical
    AI and explains it for a clinical audience.
  - Track 4: widely cited clinical primer on dataset shift.
- Nestor B, McDermott MBA, Boag W, et al. *Feature Robustness
  in Non-stationary Health Records: Caveats to Deployable Model
  Performance in Common Clinical Machine Learning Tasks.* MLHC,
  PMLR 106:381-405, 2019.
  - Shows clinical ML models suffer up to 0.29 AUROC drop under
    temporal shift in EHR data.
  - Track 4: early empirical study quantifying temporal drift in
    clinical prediction.
- Vela D, Sharp A, Zhang R, et al. *Temporal Quality
  Degradation in AI Models.* Scientific Reports, 2022;
  12:11654.
  - Large-scale analysis showing 91% of ML models degrade over
    time as data distributions drift.
  - Track 4: empirical evidence for near-universal temporal
    performance decay.
- Guo LL, Pfohl SR, Fries J, et al. *Systematic Review of
  Approaches to Preserve Machine Learning Performance in the
  Presence of Temporal Dataset Shift in Clinical Medicine.*
  Applied Clinical Informatics, 2021; 12(4):808-815.
  - Reviews 15 studies on temporal shift, finding calibration
    decay is more common than discrimination decay.
  - Track 4: first systematic review of shift mitigation in
    clinical ML.

## Governance and safety

- U.S. FDA. *Artificial Intelligence/Machine Learning
  (AI/ML)-Based Software as a Medical Device (SaMD) Action
  Plan.* FDA, 2021.
  - Five-action regulatory strategy for AI/ML medical devices
    including predetermined change control plans.
  - Track 4: primary U.S. regulatory roadmap for AI/ML in
    healthcare.
- World Health Organization. *Ethics and Governance of
  Artificial Intelligence for Health: WHO Guidance.* WHO, 2021.
  - Six ethical principles and governance recommendations for
    equitable, transparent, and rights-respecting health AI.
  - Track 4: first global intergovernmental AI health governance
    framework.
- Mitchell M, Wu S, Zaldivar A, et al. *Model Cards for Model
  Reporting.* FAT*, 2019.
  - Proposes standardized model documentation detailing
    performance across demographic and contextual conditions.
  - Track 4: foundational transparency tool for AI deployment.
- Gebru T, Morgenstern J, Vecchione B, et al. *Datasheets for
  Datasets.* Communications of the ACM, 2021; 64(12):86-92.
  - Standardized dataset documentation covering motivation,
    composition, collection, and intended uses.
  - Track 4: data governance companion to model cards.
- Reddy S, Allan S, Coghlan S, Cooper P. *A Governance Model
  for the Application of AI in Health Care.* JAMIA, 2020;
  27(3):491-497.
  - Structured governance model for healthcare AI encompassing
    fairness, transparency, and clinical safety assessment.
  - Track 4: governance framework tailored to healthcare AI.
- Raji ID, Smart A, White RN, et al. *Closing the AI
  Accountability Gap: Defining an End-to-End Framework for
  Internal Algorithmic Auditing.* FAT*, 2020; pp. 33-44.
  - Introduces SMACTR, an end-to-end internal algorithmic
    auditing framework for operationalizing AI ethics.
  - Track 4: practical auditing methodology for accountability.

## Hospital information systems and operations

- Mandl KD, Kohane IS. *Escaping the EHR Trap — The Future
  of Health IT.* NEJM, 2012; 366(24):2240-2242.
  - Argues that the EHR market is locked in by data and
    interface monopolies, and lays out the case for an
    apps-on-data ecosystem.
  - Track 5: foundational critique of EHR architecture and
    case for interoperability.
- Sittig DF, Singh H. *A new sociotechnical model for
  studying health information technology in complex adaptive
  healthcare systems.* Quality and Safety in Health Care,
  2010; 19(Suppl 3):i68-i74.
  - Eight-dimensional sociotechnical model covering hardware,
    software, content, interface, people, workflow, policy,
    and measurement.
  - Track 5: standard framework for analyzing health IT
    failures and successes.
- Adler-Milstein J, Jha AK. *HITECH Act drove large gains in
  hospital electronic health record adoption.* Health
  Affairs, 2017; 36(8):1416-1422.
  - Documents the policy-driven jump in U.S. hospital EHR
    adoption following the HITECH Act.
  - Track 5: empirical anchor for the modern EHR landscape.
- Mandel JC, Kreda DA, Mandl KD, Kohane IS, Ramoni RB. *SMART
  on FHIR: a standards-based, interoperable apps platform
  for electronic health records.* JAMIA, 2016;
  23(5):899-908.
  - Describes SMART on FHIR as an open, standards-based
    platform for substitutable EHR apps.
  - Track 5: reference architecture for hospital-side
    interoperability.
- Bates DW, Saria S, Ohno-Machado L, Shah A, Escobar G. *Big
  data in health care: Using analytics to identify and
  manage high-risk and high-cost patients.* Health Affairs,
  2014; 33(7):1123-1131.
  - Surveys six application areas where hospital analytics on
    EHR data can improve care for high-risk patients.
  - Track 5: framing for hospital-scale analytics on
    routinely collected data.
- Sendak MP, Gao M, Brajer N, Balu S. *Presenting machine
  learning model information to clinical end users with
  model facts labels.* npj Digital Medicine, 2020; 3:41.
  - Proposes a model facts label modeled on nutrition labels
    for communicating ML model information to clinicians.
  - Track 5: hospital-side documentation pattern for deployed
    models.
- Wong A, Otles E, Donnelly JP, et al. *External Validation
  of a Widely Implemented Proprietary Sepsis Prediction
  Model in Hospitalized Patients.* JAMA Internal Medicine,
  2021; 181(8):1065-1070.
  - External validation of the Epic Sepsis Model finding
    substantially worse performance than the vendor reported.
  - Track 5: case study of hospital-side validation revealing
    a deployed model's limits.

## Drug discovery and computational drug design

- Vamathevan J, Clark D, Czodrowski P, et al. *Applications
  of machine learning in drug discovery and development.*
  Nature Reviews Drug Discovery, 2019; 18:463-477.
  - Broad review of where ML is being applied across the
    drug discovery pipeline, with a balanced view on
    limitations.
  - Track 6: orientation review for ML in drug discovery.
- Schneider P, Walters WP, Plowright AT, et al. *Rethinking
  drug design in the artificial intelligence era.* Nature
  Reviews Drug Discovery, 2020; 19:353-364.
  - Argues that AI is changing drug design but emphasizes the
    need for chemist-in-the-loop workflows and realistic
    expectations.
  - Track 6: design-process framing for AI-assisted medicinal
    chemistry.
- Stokes JM, Yang K, Swanson K, et al. *A Deep Learning
  Approach to Antibiotic Discovery.* Cell, 2020;
  180(4):688-702.
  - Uses a graph neural network to screen for antibacterial
    activity, identifying halicin from a chemical library.
  - Track 6: well-known case of screening ML yielding a
    candidate of interest.
- Jumper J, Evans R, Pritzel A, et al. *Highly accurate
  protein structure prediction with AlphaFold.* Nature,
  2021; 596:583-589.
  - Presents AlphaFold's neural-network architecture for
    protein structure prediction at near-experimental
    accuracy.
  - Track 6: structural input that has reshaped what
    structure-based design can use.
- Gomez-Bombarelli R, Wei JN, Duvenaud D, et al. *Automatic
  Chemical Design Using a Data-Driven Continuous
  Representation of Molecules.* ACS Central Science, 2018;
  4(2):268-276.
  - Variational autoencoder over SMILES strings enabling
    optimization in a learned latent chemical space.
  - Track 6: foundational generative chemistry paper.
- Segler MHS, Preuss M, Waller MP. *Planning chemical
  syntheses with deep neural networks and symbolic AI.*
  Nature, 2018; 555:604-610.
  - Combines neural networks with Monte Carlo tree search to
    propose multi-step retrosynthetic routes.
  - Track 6: synthetic accessibility tooling that
    complements generative design.
- Wu Z, Ramsundar B, Feinberg EN, et al. *MoleculeNet: A
  Benchmark for Molecular Machine Learning.* Chemical
  Science, 2018; 9(2):513-530.
  - Standardized benchmark suite of molecular datasets and
    tasks for evaluating ML models.
  - Track 6: shared evaluation ground for molecular property
    prediction.
- Pushpakom S, Iorio F, Eyers PA, et al. *Drug repurposing:
  progress, challenges and recommendations.* Nature Reviews
  Drug Discovery, 2019; 18:41-58.
  - Surveys computational and experimental approaches to
    drug repurposing and the regulatory and economic
    context.
  - Track 6: orientation reference for the repurposing
    setting.
- Yang K, Swanson K, Jin W, et al. *Analyzing Learned
  Molecular Representations for Property Prediction.*
  Journal of Chemical Information and Modeling, 2019;
  59(8):3370-3388.
  - Introduces directed message passing networks (Chemprop)
    and analyzes learned chemical representations.
  - Track 6: widely used baseline for molecular property
    prediction.
- Walters WP, Murcko M. *Assessing the impact of generative
  AI on medicinal chemistry.* Nature Biotechnology, 2020;
  38:143-145.
  - Cautious assessment of generative chemistry's track
    record, distinguishing demonstrations from impact on
    real medicinal chemistry workflows.
  - Track 6: corrective viewpoint against over-claiming.

## Clinical AI deployment case studies

- Habib AR, Lin AL, Grant RW. *The Epic Sepsis Model Falls
  Short — The Importance of External Validation.* JAMA
  Internal Medicine, 2021; 181(8):1040-1041.
  - Editorial framing the Epic Sepsis Model external
    validation as a general argument for routine
    independent evaluation of widely deployed clinical AI.
  - Cross-cutting: case-study companion to the Wong et al.
    validation paper.
- Strickland E. *IBM Watson, Heal Thyself: How IBM
  Overpromised and Underdelivered on AI Health Care.* IEEE
  Spectrum, 2019.
  - Long-form investigation of the IBM Watson for Oncology
    program and the gap between marketing and capability.
  - Cross-cutting: trade-press case study used as a
    cautionary reference in the deployment literature.
- Char DS, Shah NH, Magnus D. *Implementing Machine Learning
  in Health Care — Addressing Ethical Challenges.* NEJM,
  2018; 378(11):981-983.
  - Frames implementation of ML in healthcare as an ethical
    problem requiring attention to bias, accountability, and
    informed consent.
  - Cross-cutting: short, widely cited orientation piece on
    ethical scoping at deployment.
- Coiera E. *The Last Mile: Where Artificial Intelligence
  Meets Reality.* Journal of Medical Internet Research,
  2019; 21(11):e16323.
  - Argues that closing the gap between model performance
    and clinical impact is a sociotechnical problem, not a
    purely technical one.
  - Cross-cutting: framing for the deployment-gap question.
- Shah NH, Milstein A, Bagley SC. *Making Machine Learning
  Models Clinically Useful.* JAMA, 2019; 322(14):1351-1352.
  - Argues that clinical usefulness requires reasoning
    about decision context and counterfactual outcomes,
    not only predictive accuracy.
  - Cross-cutting: viewpoint on action-relevance for
    clinical ML.

## Regulatory landscape for healthcare AI

- U.S. FDA, Health Canada, MHRA. *Good Machine Learning
  Practice for Medical Device Development: Guiding
  Principles.* 2021.
  - Ten guiding principles jointly issued by three
    regulators, framed as a starting point rather than a
    regulation.
  - Cross-cutting: most-cited regulator joint statement on
    ML medical device development.
- U.S. FDA, Health Canada, MHRA. *Predetermined Change
  Control Plans for Machine Learning-Enabled Medical
  Devices: Guiding Principles.* 2023.
  - Joint guiding principles on managing model
    modifications across the lifecycle without
    re-submitting for every change.
  - Cross-cutting: foundational document for change-control
    practice.
- Muehlematter UJ, Daniore P, Vokinger KN. *Approval of
  artificial intelligence and machine learning-based
  medical devices in the USA and Europe (2015-20): a
  comparative analysis.* Lancet Digital Health, 2021;
  3(3):e195-e203.
  - Comparative analysis of AI/ML medical device approvals
    in the U.S. and Europe over five years.
  - Cross-cutting: empirical anchor for the regulator-side
    landscape.
- Benjamens S, Dhunnoo P, Mesko B. *The state of
  artificial intelligence-based FDA-approved medical
  devices and algorithms: an online database.* npj Digital
  Medicine, 2020; 3:118.
  - Curated database of FDA-cleared AI/ML medical devices
    with category and modality breakdowns.
  - Cross-cutting: reference dataset for tracking
    approvals.
- Vokinger KN, Feuerriegel S, Kesselheim AS. *Continual
  learning in medical devices: FDA's action plan and
  beyond.* Lancet Digital Health, 2021; 3(6):e337-e338.
  - Critical reading of regulatory framing for continual
    learning systems and what it leaves underspecified.
  - Cross-cutting: regulator-policy commentary on
    continual learning.
- European Commission. *Regulation (EU) 2017/745 of the
  European Parliament and of the Council on Medical
  Devices (MDR).* 2017.
  - EU Medical Device Regulation governing software and
    AI as a medical device in the European Union.
  - Cross-cutting: primary EU regulatory text for clinical
    AI.

## Foundation models in healthcare

- Bommasani R, Hudson DA, Adeli E, et al. *On the
  Opportunities and Risks of Foundation Models.*
  arXiv:2108.07258, 2021.
  - Stanford CRFM report defining foundation models and
    surveying capabilities, applications, and risks across
    domains.
  - Cross-cutting: standard reference for the foundation
    model concept itself.
- Singhal K, Azizi S, Tu T, et al. *Large language models
  encode clinical knowledge.* Nature, 2023; 620:172-180.
  - Introduces Med-PaLM and reports on medical question
    answering performance with prompt engineering and
    instruction tuning.
  - Cross-cutting: anchor paper for clinical LLM
    evaluation.
- Yang X, Chen A, PourNejatian N, et al. *A large
  language model for electronic health records.* npj
  Digital Medicine, 2022; 5:194.
  - Introduces GatorTron, an EHR-pretrained LLM, and
    reports gains on clinical NLP tasks.
  - Cross-cutting: example of domain pretraining on
    structured-plus-text clinical data.
- Lehman E, Hernandez E, Mahajan D, et al. *Do We Still
  Need Clinical Language Models?* Conference on Health,
  Inference, and Learning (CHIL), 2023.
  - Compares general and clinical LLMs across tasks and
    asks under what conditions clinical pretraining still
    pays off.
  - Cross-cutting: empirical recalibration of when
    in-domain pretraining matters.
- Moor M, Banerjee O, Abad ZSH, et al. *Foundation models
  for generalist medical artificial intelligence.* Nature,
  2023; 616:259-265.
  - Articulates a vision of generalist medical AI built on
    foundation models, with explicit attention to
    evaluation and governance gaps.
  - Cross-cutting: framing piece for multimodal medical
    foundation models.
- Chithrananda S, Grand G, Ramsundar B. *ChemBERTa:
  Large-Scale Self-Supervised Pretraining for Molecular
  Property Prediction.* arXiv:2010.09885, 2020.
  - Adapts BERT-style self-supervised pretraining to SMILES
    strings for downstream molecular property prediction.
  - Cross-cutting: early chemistry foundation model.
- Ross J, Belgodere B, Chenthamarakshan V, et al.
  *Large-scale chemical language representations capture
  molecular structure and properties.* Nature Machine
  Intelligence, 2022; 4:1256-1264.
  - Introduces MoLFormer, a large-scale chemistry language
    model, and benchmarks downstream property tasks.
  - Cross-cutting: scaling chemistry language modeling.
- Lin Z, Akin H, Rao R, et al. *Evolutionary-scale
  prediction of atomic-level protein structure.* Science,
  2023; 379:1123-1130.
  - Introduces ESM-2 and ESMFold, demonstrating
    evolutionary-scale protein language models for
    structure prediction.
  - Cross-cutting: foundation-scale alternative to
    AlphaFold for structural biology.

## Federated and privacy-preserving learning

- McMahan HB, Moore E, Ramage D, Hampson S, Aguera y Arcas
  B. *Communication-Efficient Learning of Deep Networks
  from Decentralized Data.* AISTATS, 2017.
  - Introduces federated averaging for training shared
    models across decentralized data.
  - Cross-cutting: foundational paper for federated
    learning.
- Rieke N, Hancox J, Li W, et al. *The future of digital
  health with federated learning.* npj Digital Medicine,
  2020; 3:119.
  - Position paper on federated learning for medicine,
    surveying applications and operational considerations.
  - Cross-cutting: orientation reference for federated
    learning in healthcare.
- Sheller MJ, Edwards B, Reina GA, et al. *Federated
  learning in medicine: facilitating multi-institutional
  collaborations without sharing patient data.* Scientific
  Reports, 2020; 10:12598.
  - Multi-institutional federated learning experiment for
    brain tumor segmentation, comparing federated and
    centralized training.
  - Cross-cutting: empirical demonstration in medical
    imaging.
- Kaissis GA, Makowski MR, Ruckert D, Braren RF. *Secure,
  privacy-preserving and federated machine learning in
  medical imaging.* Nature Machine Intelligence, 2020;
  2:305-311.
  - Reviews federated learning, differential privacy, and
    secure computation for medical imaging.
  - Cross-cutting: review tying federated and
    privacy-preserving methods together.
- Pati S, Baid U, Edwards B, et al. *Federated learning
  enables big data for rare cancer boundary detection.*
  Nature Communications, 2022; 13:7346.
  - Reports on the FeTS federated learning effort for
    rare-cancer boundary detection across many sites.
  - Cross-cutting: large-scale federated medical imaging
    case study.
- Dwork C, Roth A. *The Algorithmic Foundations of
  Differential Privacy.* Foundations and Trends in
  Theoretical Computer Science, 2014; 9(3-4):211-407.
  - Foundational monograph on differential privacy
    definitions, mechanisms, and analyses.
  - Cross-cutting: standard reference for differential
    privacy.

## Fairness and equity in healthcare AI

- Obermeyer Z, Powers B, Vogeli C, Mullainathan S.
  *Dissecting racial bias in an algorithm used to manage
  the health of populations.* Science, 2019;
  366(6464):447-453.
  - Shows that a widely used commercial risk-prediction
    algorithm under-allocated care to Black patients
    because it used cost as a proxy for need.
  - Cross-cutting: canonical case of label-choice bias in
    a deployed clinical algorithm.
- Pierson E, Cutler DM, Leskovec J, Mullainathan S,
  Obermeyer Z. *An algorithmic approach to reducing
  unexplained pain disparities in underserved
  populations.* Nature Medicine, 2021; 27:136-140.
  - Uses algorithmic methods to identify pain not
    accounted for by standard radiographic measures,
    disproportionately affecting Black patients.
  - Cross-cutting: example of AI used to surface rather
    than create disparities.
- Seyyed-Kalantari L, Zhang H, McDermott MBA, Chen IY,
  Ghassemi M. *Underdiagnosis bias of artificial
  intelligence algorithms applied to chest radiographs in
  under-served patient populations.* Nature Medicine,
  2021; 27:2176-2182.
  - Demonstrates higher under-diagnosis rates by chest
    radiograph classifiers for female, Black, Hispanic,
    and low-SES patients across multiple datasets.
  - Cross-cutting: empirical evidence for subgroup
    disparities in deployed-class imaging AI.
- Rajkomar A, Hardt M, Howell MD, Corrado G, Chin MH.
  *Ensuring Fairness in Machine Learning to Advance Health
  Equity.* Annals of Internal Medicine, 2018;
  169(12):866-872.
  - Frames fairness in clinical ML as a chain of design
    choices spanning data, label, model, and deployment.
  - Cross-cutting: orientation paper for the design-stage
    framing of fairness.
- Chen IY, Joshi S, Ghassemi M. *Treating health
  disparities with artificial intelligence.* Nature
  Medicine, 2020; 26:16-17.
  - Argues for treating disparity reduction as a primary
    design objective in healthcare AI.
  - Cross-cutting: positioning piece for equity-as-goal.
- Ghassemi M, Naumann T, Pierson E. *The False Hope of
  Current Approaches to Explainable Artificial
  Intelligence in Health Care.* Lancet Digital Health,
  2021; 3(11):e745-e750.
  - Argues that current explainable AI approaches do not
    deliver what clinical users actually need from
    explanations.
  - Cross-cutting: critique of post-hoc explanation as a
    general fairness or trust solution.

## Reproducibility in healthcare ML

- McDermott MBA, Wang S, Marinsek N, Ranganath R,
  Foschini L, Ghassemi M. *Reproducibility in machine
  learning for health research: still a ways to go.*
  Science Translational Medicine, 2021; 13(586):eabb1655.
  - Surveys reproducibility issues in clinical ML across
    code release, data access, and reporting.
  - Cross-cutting: empirical anchor for the
    reproducibility argument in clinical ML.
- Stupple A, Singerman D, Celi LA. *The reproducibility
  crisis in the age of digital medicine.* npj Digital
  Medicine, 2019; 2:2.
  - Frames reproducibility for digital medicine, including
    publication norms and data-sharing constraints.
  - Cross-cutting: orientation piece on the broader
    reproducibility problem.
- Wynants L, Van Calster B, Collins GS, et al.
  *Prediction models for diagnosis and prognosis of
  covid-19: systematic review and critical appraisal.*
  BMJ, 2020; 369:m1328.
  - Systematic review judging most COVID-19 prediction
    models at high risk of bias.
  - Cross-cutting: large-scale empirical case for
    methodological scrutiny of clinical ML.
- Roberts M, Driggs D, Thorpe M, et al. *Common pitfalls
  and recommendations for using machine learning to
  detect and prognosticate for COVID-19 using chest
  radiographs and CT scans.* Nature Machine Intelligence,
  2021; 3:199-217.
  - Reviews ML approaches to COVID-19 imaging and
    catalogs recurring pitfalls including data leakage
    and inadequate dataset description.
  - Cross-cutting: detailed pitfalls catalog for clinical
    imaging ML.
- Wallach IZ, Heifets A. *Most Ligand-Based
  Classification Benchmarks Reward Memorization Rather
  than Generalization.* Journal of Chemical Information
  and Modeling, 2018; 58(5):916-932.
  - Shows that several molecular classification
    benchmarks can be solved by memorization rather than
    generalization, undermining apparent gains.
  - Cross-cutting: foundational reproducibility critique
    in chemistry ML.
- Bender A, Cortes-Ciriano I. *Artificial intelligence in
  drug discovery: what is realistic, what are illusions?
  Part 1: Ways to make an impact, and why we are not
  there yet.* Drug Discovery Today, 2021;
  26(2):511-524.
  - Critical assessment of the gap between AI drug
    discovery claims and clinical impact.
  - Cross-cutting: corrective reading on the discovery-
    AI hype cycle.
- Bender A, Cortes-Ciriano I. *Artificial intelligence in
  drug discovery: what is realistic, what are illusions?
  Part 2: A discussion of chemical and biological data.*
  Drug Discovery Today, 2021; 26(4):1040-1052.
  - Companion paper focused on data quality, dataset
    diversity, and benchmark design problems in
    discovery ML.
  - Cross-cutting: detailed reading on data limits in
    drug discovery ML.

## Hospital cybersecurity, telehealth, and process mining

- Coventry L, Branley D. *Cybersecurity in healthcare: A
  narrative review of trends, threats and ways forward.*
  Maturitas, 2018; 113:48-52.
  - Narrative review of cybersecurity threats specific to
    healthcare environments and proposed responses.
  - Cross-cutting: orientation reference for healthcare
    cybersecurity.
- Webster P. *Virtual health care in the era of
  COVID-19.* Lancet, 2020; 395(10231):1180-1181.
  - Frames the rapid pandemic-era expansion of virtual
    care and the questions it raised for health systems.
  - Cross-cutting: short framing piece on telehealth
    acceleration.
- Mans RS, van der Aalst WMP, Vanwersch RJB. *Process
  Mining in Healthcare: Evaluating and Exploiting
  Operational Healthcare Processes.* Springer, 2015.
  - Methodological treatment of process mining as applied
    to healthcare event logs.
  - Cross-cutting: book-length reference for healthcare
    process mining.
- Rojas E, Munoz-Gama J, Sepulveda M, Capurro D. *Process
  mining in healthcare: A literature review.* Journal of
  Biomedical Informatics, 2016; 61:224-236.
  - Systematic review of healthcare process mining
    studies, methods, and reporting practices.
  - Cross-cutting: review article for the healthcare
    process-mining literature.

## Drug discovery extensions: knowledge graphs, protein design, trials, and pharmacovigilance

- Reker D, Schneider G. *Active-learning strategies in
  computer-assisted drug discovery.* Drug Discovery
  Today, 2015; 20(4):458-465.
  - Surveys active-learning approaches in
    computer-assisted drug discovery and characterizes
    where they pay off.
  - Cross-cutting: orientation reference for active
    learning in chemistry.
- Himmelstein DS, Lizee A, Hessler C, et al. *Systematic
  integration of biomedical knowledge prioritizes drugs
  for repurposing.* eLife, 2017; 6:e26726.
  - Introduces Hetionet, a heterogeneous biomedical
    knowledge graph, and uses it for systematic
    repurposing prioritization.
  - Cross-cutting: foundational biomedical knowledge graph
    paper.
- Zitnik M, Agrawal M, Leskovec J. *Modeling polypharmacy
  side effects with graph convolutional networks.*
  Bioinformatics, 2018; 34(13):i457-i466.
  - Introduces Decagon for graph-convolutional prediction
    of polypharmacy side effects.
  - Cross-cutting: applied biomedical knowledge graph ML
    paper.
- Dauparas J, Anishchenko I, Bennett N, et al. *Robust
  deep learning-based protein sequence design using
  ProteinMPNN.* Science, 2022; 378(6615):49-56.
  - Introduces ProteinMPNN for sequence design given a
    structural backbone, with experimental validation.
  - Cross-cutting: protein sequence design baseline.
- Watson JL, Juergens D, Bennett NR, et al. *De novo
  design of protein structure and function with
  RFdiffusion.* Nature, 2023; 620:1089-1100.
  - Introduces RFdiffusion for de novo design of protein
    structure and function via diffusion modeling on
    structure.
  - Cross-cutting: structure-side of the protein design
    pipeline.
- Harrer S, Shah P, Antony B, Hu J. *Artificial
  Intelligence for Clinical Trial Design.* Trends in
  Pharmacological Sciences, 2019; 40(8):577-591.
  - Surveys AI applications across clinical trial design
    including eligibility, site selection, and
    stratification.
  - Cross-cutting: orientation reference for AI in trial
    design.
- Liu R, Rizzo S, Whipple S, et al. *Evaluating
  eligibility criteria of oncology trials using real-world
  data and artificial intelligence.* Nature, 2021;
  592:629-633.
  - Uses real-world data and AI to evaluate the impact of
    oncology trial eligibility criteria on patient
    inclusion.
  - Cross-cutting: empirical case for AI-supported
    eligibility analysis.
- Ball R, Dal Pan G. *"Artificial Intelligence" for
  Pharmacovigilance: Ready for Prime Time?* Drug Safety,
  2022; 45:429-438.
  - Reviews readiness of AI methods for pharmacovigilance
    and the evaluation challenges that remain.
  - Cross-cutting: orientation reference for AI in
    pharmacovigilance.

## Systems engineering and architecture methods

- Crawley E, Cameron B, Selva D. *System Architecture:
  Strategy and Product Development for Complex Systems.*
  Pearson, 2015.
  - Treats system architecture as allocation of function
    to form under stakeholder value constraints, with a
    design process and worked examples.
  - Track 7: primary MIT SDM architecture reference used
    for stakeholder value and functional analysis.
- de Weck OL, Roos D, Magee CL. *Engineering Systems:
  Meeting Human Needs in a Complex Technological World.*
  MIT Press, 2011.
  - Positions engineering systems as a discipline
    addressing complex, sociotechnical artifacts beyond
    single-engineer scope.
  - Track 7: framing reference for healthcare AI as an
    engineering system.
- Eppinger SD, Browning TR. *Design Structure Matrix
  Methods and Applications.* MIT Press, 2012.
  - Methodological reference for DSM analysis of product,
    organization, and process architectures.
  - Track 7: basis for component and organizational DSM
    exercises on healthcare AI deployments.
- Suh NP. *Axiomatic Design: Advances and Applications.*
  Oxford University Press, 2001.
  - Presents axiomatic design with Independence and
    Information axioms, mapping functional requirements to
    design parameters.
  - Track 7: method for exposing functional coupling in
    healthcare AI architectures.
- Sterman JD. *Business Dynamics: Systems Thinking and
  Modeling for a Complex World.* Irwin McGraw-Hill, 2000.
  - Comprehensive treatment of system dynamics with
    applications to feedback loops, delays, and stocks
    and flows.
  - Track 7: basis for causal-loop and stock-and-flow
    models of alert fatigue, trust, and drift in clinical
    AI.
- Dori D. *Model-Based Systems Engineering with OPM and
  SysML.* Springer, 2016.
  - Introduces Object-Process Methodology alongside
    SysML for model-based systems engineering.
  - Track 7: candidate notation for cross-discipline
    description of clinical AI systems.
- INCOSE. *INCOSE Systems Engineering Handbook.* 5th
  edition, Wiley, 2023.
  - Reference handbook for systems engineering lifecycle,
    processes, and management practices.
  - Track 7: general systems-engineering reference used
    as a baseline across tracks.

## ML engineering, operations, and technical debt

- Amershi S, Begel A, Bird C, et al. *Software Engineering
  for Machine Learning: A Case Study.* International
  Conference on Software Engineering (ICSE-SEIP), 2019;
  pp. 291-300.
  - Observes teams at Microsoft building ML applications
    and articulates a nine-stage workflow with
    engineering challenges specific to ML.
  - Track 7: empirical reference for ML software
    engineering practice.
- Paleyes A, Urma RG, Lawrence ND. *Challenges in
  Deploying Machine Learning: A Survey of Case Studies.*
  ACM Computing Surveys, 2022; 55(6):Article 114.
  - Surveys published ML deployment case studies and
    maps challenges to stages of the deployment
    workflow.
  - Track 7: consolidated reference for ML deployment
    failure modes.
- Breck E, Cai S, Nielsen E, Salib M, Sculley D. *The ML
  Test Score: A Rubric for ML Production Readiness and
  Technical Debt Reduction.* IEEE International
  Conference on Big Data, 2017.
  - Rubric of tests across data, model, infrastructure,
    and monitoring for scoring ML production readiness.
  - Track 7: practical scorecard for clinical ML
    deployment review.
- Kreuzberger D, Kuhl N, Hirschl S. *Machine Learning
  Operations (MLOps): Overview, Definition, and
  Architecture.* IEEE Access, 2023; 11:31866-31879.
  - Aggregates principles, components, roles, and
    architecture for MLOps from literature, tool review,
    and interviews.
  - Track 7: reference for MLOps operating model.
- Shankar S, Garcia R, Hellerstein JM, Parameswaran AG.
  *Operationalizing Machine Learning: An Interview
  Study.* arXiv:2209.09125, 2022.
  - Qualitative interview study of ML practitioners
    characterizing the gaps between research ML and
    production ML.
  - Track 7: ethnographic reference for ML operations
    in practice.
- Huyen C. *Designing Machine Learning Systems.*
  O'Reilly, 2022.
  - Book-length treatment of ML systems design covering
    data, training, deployment, and monitoring.
  - Track 7: accessible reference for end-to-end ML
    systems design.
- Wiens J, Saria S, Sendak M, et al. *Do no harm: a
  roadmap for responsible machine learning for health
  care.* Nature Medicine, 2019; 25:1337-1340.
  - Roadmap for responsible healthcare ML covering
    design, evaluation, reporting, and deployment
    practices.
  - Track 7: widely cited roadmap bridging clinical
    research and ML engineering practice.

## Pharmaceutical R&D economics and portfolio strategy

- Paul SM, Mytelka DS, Dunwiddie CT, et al. *How to
  improve R&D productivity: the pharmaceutical industry's
  grand challenge.* Nature Reviews Drug Discovery, 2010;
  9:203-214.
  - Analyzes pharmaceutical R&D productivity with a
    stage-by-stage attrition and cost model, proposing
    shifts in investment across stages.
  - Track 7 and 6: standard reference for the pharma R&D
    economic model in which discovery AI investments sit.
- Kola I, Landis J. *Can the pharmaceutical industry
  reduce attrition rates?* Nature Reviews Drug Discovery,
  2004; 3:711-715.
  - Quantifies clinical-stage attrition by cause and
    argues for reallocating effort toward early-stage
    de-risking.
  - Track 7 and 6: classic reference for attrition
    drivers in drug development.
- DiMasi JA, Grabowski HG, Hansen RW. *Innovation in the
  pharmaceutical industry: new estimates of R&D costs.*
  Journal of Health Economics, 2016; 47:20-33.
  - Re-estimates capitalized R&D cost per approved drug
    using proprietary data, with methodology discussion.
  - Track 7 and 6: cost-side reference in pharma
    portfolio analysis.
- Wouters OJ, McKee M, Luyten J. *Estimated Research and
  Development Investment Needed to Bring a New Medicine
  to Market, 2009-2018.* JAMA, 2020; 323(9):844-853.
  - Public-data estimate of capitalized R&D cost per new
    therapeutic, offering a methodologically distinct
    counterpoint to prior industry-data estimates.
  - Track 7 and 6: public-data anchor for pharma R&D
    cost discussions.
