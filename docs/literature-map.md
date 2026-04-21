# Literature map

A map of reading areas relevant to healthcare AI systems design.
Categories are listed below; individual readings will be added
as real citations are verified.

No citations are invented. Entries marked TODO should be
replaced with verified references when they are added.

## Drug efficacy evaluation

**Why this matters.** Drug efficacy evaluation sets a high bar
for evidence. Understanding how that bar is defined — trial
design, endpoints, adjustment for multiplicity, intention to
treat — is a prerequisite for asking what observational data
can and cannot contribute.

**Questions to track.**

- How are primary and secondary endpoints chosen and
  pre-registered?
- How is heterogeneity of treatment effect reported, and when
  is it informative?
- How is safety signaling handled, both within trials and after
  approval?

**Readings.**

- ICH. *ICH E9(R1) Addendum on Estimands and Sensitivity Analysis in Clinical Trials.* 2019.
- Kent DM et al. *Personalized evidence based medicine: predictive approaches to heterogeneous treatment effects.* BMJ, 2018.
- Kent DM et al. *The Predictive Approaches to Treatment effect Heterogeneity (PATH) Statement.* Annals of Internal Medicine, 2020.

## Real-world evidence and observational healthcare data

**Why this matters.** Real-world evidence is a fast-moving area
with active debate about what observational data can support.
A grounded view here is necessary to avoid both over-claiming
and dismissing the data wholesale.

**Questions to track.**

- Under what designs do observational studies approximate trial
  findings, and when do they diverge?
- How is cohort construction documented so that a study is
  reproducible?
- What roles do registries, claims, and electronic health
  records play, and how do their biases differ?

**Readings.**

- U.S. FDA. *Framework for FDA's Real-World Evidence Program.* 2018.
- Hripcsak G et al. *OHDSI: Opportunities for Observational Researchers.* Studies in Health Technology and Informatics, 2015.
- Hernan MA, Robins JM. *Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available.* American Journal of Epidemiology, 2016.

## Comparative effectiveness and treatment outcomes

**Why this matters.** Comparative effectiveness asks which
treatment works better for which patients in routine care. It
overlaps with drug efficacy but is framed around real-world
decision making rather than regulatory approval.

**Questions to track.**

- When is an active comparator the right choice, and when is a
  non-user comparison defensible?
- How should subgroup effects be reported without inviting
  spurious claims?
- How is clinical utility distinguished from statistical
  significance?

**Readings.**

- Lund JL et al. *The Active Comparator, New User Study Design in Pharmacoepidemiology.* Current Epidemiology Reports, 2015.
- Concato J et al. *Randomized, Controlled Trials, Observational Studies, and the Hierarchy of Research Designs.* NEJM, 2000.
- Schneeweiss S et al. *High-dimensional Propensity Score Adjustment in Studies of Treatment Effects Using Health Care Claims Data.* Epidemiology, 2009.

## Causal inference and association limits

**Why this matters.** Most observational questions in healthcare
are causal questions in disguise. Taking causal inference
seriously — or admitting when it cannot be taken seriously — is
the core honesty of this line of work.

**Questions to track.**

- What assumptions does each adjustment method actually make?
- How should sensitivity analyses be reported so they are
  informative rather than ritual?
- When are negative controls and E-values useful, and when do
  they mislead?

**Readings.**

- Rosenbaum PR, Rubin DB. *The Central Role of the Propensity Score in Observational Studies for Causal Effects.* Biometrika, 1983.
- VanderWeele TJ, Ding P. *Sensitivity Analysis in Observational Research: Introducing the E-Value.* Annals of Internal Medicine, 2017.
- Lipsitch M et al. *Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies.* Epidemiology, 2010.
- Hernan MA, Robins JM. *Causal Inference: What If.* Chapman & Hall/CRC, 2020.

## Precision medicine

**Why this matters.** Precision medicine is a framing that
easily overstates what is possible at the individual level.
Reading here should include both optimistic cases and critical
reviews.

**Questions to track.**

- What does "individual" actually mean in precision medicine
  studies — a patient, a subgroup, a genotype?
- Which precision medicine successes have replicated, and which
  have not?
- How is uncertainty communicated to patients and clinicians?

**Readings.**

- Collins FS, Varmus H. *A New Initiative on Precision Medicine.* NEJM, 2015.
- Ashley EA. *Towards Precision Medicine.* Nature Reviews Genetics, 2016.
- Relling MV, Evans WE. *Pharmacogenomics in the Clinic.* Nature, 2015.
- Miotto R et al. *Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the EHR.* Scientific Reports, 2016.
- Topol EJ. *High-Performance Medicine: The Convergence of Human and Artificial Intelligence.* Nature Medicine, 2019.

## Multimodal healthcare data integration

**Why this matters.** Integrating clinical records, genomic
signals, imaging features, and wearable data raises questions
that any single-modality paper can ignore. This category tracks
those integration problems.

**Questions to track.**

- How is missingness across modalities handled during training
  and inference?
- What are the failure modes of late versus early fusion in
  medical settings?
- How is cross-modality validation designed?

**Readings.**

- Acosta JN et al. *Multimodal Biomedical AI.* Nature Medicine, 2022.
- Baltrusaitis T et al. *Multimodal Machine Learning: A Survey and Taxonomy.* IEEE TPAMI, 2019.
- Stahlschmidt SR et al. *Multimodal Deep Learning for Biomedical Data Fusion: A Review.* Briefings in Bioinformatics, 2022.
- Chen RJ et al. *Pan-Cancer Integrative Histology-Genomic Analysis via Multimodal Deep Learning.* Cancer Cell, 2022.
- Lipkova J et al. *Artificial Intelligence for Multimodal Data Integration in Oncology.* Cancer Cell, 2022.

## Clinical decision support and workflow integration

**Why this matters.** Clinical decision support has a long
history, much of it instructive about failure. Reading the
history is useful before designing the next system.

**Questions to track.**

- Which clinical decision support systems have succeeded, and
  what did they have in common?
- Which have failed, and why?
- How is workflow integration actually measured?

**Readings.**

- Bates DW et al. *Ten commandments for effective clinical decision support.* JAMIA, 2003.
- Kawamoto K et al. *Improving clinical practice using clinical decision support systems: a systematic review.* BMJ, 2005.
- Middleton B et al. *Clinical decision support: a 25 year retrospective and a 25 year vision.* Yearbook of Medical Informatics, 2016.

## Deployment-aware AI systems

**Why this matters.** Deployment-aware AI treats the model as
one component among many and focuses on what it takes to put it
into a setting without breaking the setting. This is the
systems-design lens behind the research tracks in this
repository.

**Questions to track.**

- What design practices distinguish systems that survive
  deployment from those that do not?
- How are validation, monitoring, and governance staged across
  time?
- What is the smallest useful version of each?

**Readings.**

- Sculley D et al. *Hidden technical debt in machine learning systems.* NeurIPS, 2015.
- Kelly CJ et al. *Key challenges for delivering clinical impact with artificial intelligence.* BMC Medicine, 2019.
- Subbaswamy A, Saria S. *From development to deployment: dataset shift, causality, and shift-stable models in health AI.* Biostatistics, 2020.
- Beede E et al. *A human-centered evaluation of a deep learning system deployed in clinics for the detection of diabetic retinopathy.* ACM CHI, 2020.

## Human-centered AI and interpretability

**Why this matters.** Human-centered AI asks what users need
rather than what the model can show. Interpretability is one
tool among several for meeting that need.

**Questions to track.**

- What does an interpretability method actually explain, and to
  whom?
- How stable are explanations under small input changes?
- When does an explanation improve user decisions, and when
  does it mislead them?

**Readings.**

- Ribeiro MT et al. *"Why should I trust you?": Explaining the predictions of any classifier.* ACM KDD, 2016.
- Lundberg SM, Lee SI. *A unified approach to interpreting model predictions.* NeurIPS, 2017.
- Rudin C. *Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead.* Nature Machine Intelligence, 2019.
- Tonekaboni S et al. *What clinicians want: contextualizing explainable machine learning for clinical end use.* MLHC, 2019.

## Monitoring and dataset shift

**Why this matters.** Dataset shift is the main way that a
deployed model silently stops working. Monitoring is the main
way anyone notices.

**Questions to track.**

- Which shift detection methods are practical at a single site?
- How are monitoring metrics chosen so that they are both
  informative and maintainable?
- How is a detected shift translated into an action?

**Readings.**

- Finlayson SG et al. *The Clinician and Dataset Shift in Artificial Intelligence.* NEJM, 2021.
- Nestor B et al. *Feature Robustness in Non-stationary Health Records.* MLHC, 2019.
- Vela D et al. *Temporal Quality Degradation in AI Models.* Scientific Reports, 2022.
- Guo LL et al. *Systematic Review of Approaches to Preserve Machine Learning Performance in the Presence of Temporal Dataset Shift in Clinical Medicine.* Applied Clinical Informatics, 2021.

## Governance and safety

**Why this matters.** Governance determines what happens after
something goes wrong, and often whether anyone notices. It is a
social problem as much as a technical one.

**Questions to track.**

- Who is accountable for each stage of a deployed system?
- How are updates reviewed and approved?
- What does a minimum viable governance structure look like at
  a single site?

**Readings.**

- U.S. FDA. *AI/ML-Based Software as a Medical Device (SaMD) Action Plan.* 2021.
- WHO. *Ethics and Governance of Artificial Intelligence for Health.* 2021.
- Mitchell M et al. *Model Cards for Model Reporting.* FAT*, 2019.
- Gebru T et al. *Datasheets for Datasets.* Communications of the ACM, 2021.
- Reddy S et al. *A Governance Model for the Application of AI in Health Care.* JAMIA, 2020.
- Raji ID et al. *Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing.* FAT*, 2020.

## Hospital information systems and operations

**Why this matters.** A clinical AI deployment lives inside a
hospital information landscape — EHRs, ADT systems, lab and
pharmacy systems, interoperability standards, and the
governance structures around them. Understanding that
landscape is a prerequisite for asking what a deployed model
actually sees and how it interacts with care.

**Questions to track.**

- How have EHR adoption and meaningful-use policy shaped what
  data is captured?
- Which interoperability standards have stuck, and what
  applications do they enable?
- How are hospital-scale failures of clinical AI documented
  in the literature?

**Readings.**

- Mandl KD, Kohane IS. *Escaping the EHR Trap — The Future of Health IT.* NEJM, 2012.
- Sittig DF, Singh H. *A new sociotechnical model for studying health information technology in complex adaptive healthcare systems.* Quality and Safety in Health Care, 2010.
- Adler-Milstein J, Jha AK. *HITECH Act drove large gains in hospital electronic health record adoption.* Health Affairs, 2017.
- Mandel JC, Kreda DA, Mandl KD, Kohane IS, Ramoni RB. *SMART on FHIR: a standards-based, interoperable apps platform for electronic health records.* JAMIA, 2016.
- Bates DW, Saria S, Ohno-Machado L, Shah A, Escobar G. *Big data in health care: Using analytics to identify and manage high-risk and high-cost patients.* Health Affairs, 2014.
- Sendak MP, Gao M, Brajer N, Balu S. *Presenting machine learning model information to clinical end users with model facts labels.* npj Digital Medicine, 2020.
- Wong A, Otles E, Donnelly JP, et al. *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients.* JAMA Internal Medicine, 2021.

## Drug discovery and computational drug design

**Why this matters.** Drug discovery sits upstream of the
efficacy questions covered in earlier categories. AI methods
now appear at every stage of discovery — target
identification, generative chemistry, property prediction,
structure prediction — with very different data and failure
modes at each stage.

**Questions to track.**

- Where in the discovery pipeline does AI demonstrably add
  value, and where is the evidence still preliminary?
- How are generative chemistry models evaluated when their
  outputs are intended to be novel?
- How are property and structure predictions used together,
  and how is their joint uncertainty handled?

**Readings.**

- Vamathevan J, Clark D, Czodrowski P, et al. *Applications of machine learning in drug discovery and development.* Nature Reviews Drug Discovery, 2019.
- Schneider P, Walters WP, Plowright AT, et al. *Rethinking drug design in the artificial intelligence era.* Nature Reviews Drug Discovery, 2020.
- Stokes JM, Yang K, Swanson K, et al. *A Deep Learning Approach to Antibiotic Discovery.* Cell, 2020.
- Jumper J, Evans R, Pritzel A, et al. *Highly accurate protein structure prediction with AlphaFold.* Nature, 2021.
- Gomez-Bombarelli R, Wei JN, Duvenaud D, et al. *Automatic Chemical Design Using a Data-Driven Continuous Representation of Molecules.* ACS Central Science, 2018.
- Segler MHS, Preuss M, Waller MP. *Planning chemical syntheses with deep neural networks and symbolic AI.* Nature, 2018.
- Wu Z, Ramsundar B, Feinberg EN, et al. *MoleculeNet: A Benchmark for Molecular Machine Learning.* Chemical Science, 2018.
- Pushpakom S, Iorio F, Eyers PA, et al. *Drug repurposing: progress, challenges and recommendations.* Nature Reviews Drug Discovery, 2019.
- Yang K, Swanson K, Jin W, et al. *Analyzing Learned Molecular Representations for Property Prediction.* Journal of Chemical Information and Modeling, 2019.
- Walters WP, Murcko M. *Assessing the impact of generative AI on medicinal chemistry.* Nature Biotechnology, 2020.

## Clinical AI deployment case studies

**Why this matters.** Principles about deployment become
sharp when read through specific cases. Published case
studies of clinical AI — successful and failed — anchor
abstract design questions in observed sociotechnical
behavior.

**Questions to track.**

- Which features distinguish deployments that survive
  contact with the clinic from those that do not?
- How are external validation results received in
  comparison to vendor-reported performance?
- Which failure modes recur across cases, and which are
  particular to one setting?

**Readings.**

- Habib AR, Lin AL, Grant RW. *The Epic Sepsis Model Falls Short — The Importance of External Validation.* JAMA Internal Medicine, 2021.
- Strickland E. *IBM Watson, Heal Thyself.* IEEE Spectrum, 2019.
- Char DS, Shah NH, Magnus D. *Implementing Machine Learning in Health Care — Addressing Ethical Challenges.* NEJM, 2018.
- Coiera E. *The Last Mile: Where Artificial Intelligence Meets Reality.* Journal of Medical Internet Research, 2019.
- Shah NH, Milstein A, Bagley SC. *Making Machine Learning Models Clinically Useful.* JAMA, 2019.

## Regulatory landscape for healthcare AI

**Why this matters.** Regulation shapes evaluation, change
control, and post-market evidence requirements. Reading
regulators directly is part of building systems that can
be deployed responsibly.

**Questions to track.**

- How are AI/ML medical devices being approved across
  jurisdictions, and what does the trend look like?
- How are predetermined change control plans being
  operationalized?
- What does regulatory attention to bias and equity look
  like in practice?

**Readings.**

- U.S. FDA, Health Canada, MHRA. *Good Machine Learning Practice for Medical Device Development: Guiding Principles.* 2021.
- U.S. FDA, Health Canada, MHRA. *Predetermined Change Control Plans for Machine Learning-Enabled Medical Devices: Guiding Principles.* 2023.
- Muehlematter UJ, Daniore P, Vokinger KN. *Approval of artificial intelligence and machine learning-based medical devices in the USA and Europe (2015-20): a comparative analysis.* Lancet Digital Health, 2021.
- Benjamens S, Dhunnoo P, Mesko B. *The state of artificial intelligence-based FDA-approved medical devices and algorithms: an online database.* npj Digital Medicine, 2020.
- Vokinger KN, Feuerriegel S, Kesselheim AS. *Continual learning in medical devices: FDA's action plan and beyond.* Lancet Digital Health, 2021.
- European Commission. *Regulation (EU) 2017/745 on medical devices (MDR).* 2017.

## Foundation models in healthcare

**Why this matters.** Foundation models are now part of
the clinical and discovery toolset. Their evaluation,
deployment, and governance raise familiar questions at
larger scale.

**Questions to track.**

- When does domain pretraining still matter relative to
  prompting a sufficiently capable general model?
- What does meaningful out-of-distribution evaluation look
  like for foundation models in clinical and chemical
  domains?
- How are deployment costs and governance overheads
  accounted for at hospital and lab scale?

**Readings.**

- Bommasani R, Hudson DA, Adeli E, et al. *On the Opportunities and Risks of Foundation Models.* arXiv:2108.07258, 2021.
- Singhal K, Azizi S, Tu T, et al. *Large language models encode clinical knowledge.* Nature, 2023.
- Yang X, Chen A, PourNejatian N, et al. *A large language model for electronic health records.* npj Digital Medicine, 2022.
- Lehman E, Hernandez E, Mahajan D, et al. *Do We Still Need Clinical Language Models?* Conference on Health, Inference, and Learning (CHIL), 2023.
- Moor M, Banerjee O, Abad ZSH, et al. *Foundation models for generalist medical artificial intelligence.* Nature, 2023.
- Chithrananda S, Grand G, Ramsundar B. *ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property Prediction.* arXiv:2010.09885, 2020.
- Ross J, Belgodere B, Chenthamarakshan V, et al. *Large-scale chemical language representations capture molecular structure and properties.* Nature Machine Intelligence, 2022.
- Lin Z, Akin H, Rao R, et al. *Evolutionary-scale prediction of atomic-level protein structure.* Science, 2023.

## Federated and privacy-preserving learning

**Why this matters.** Multi-institution learning is one of
the few practical options for combining evidence across
hospitals without combining their data. Federated
learning, differential privacy, and related methods sit at
the center of that conversation.

**Questions to track.**

- How are non-IID effects across sites characterized and
  reported?
- How are privacy budgets chosen and explained?
- What threat models do specific federated and
  privacy-preserving deployments actually defend against?

**Readings.**

- McMahan HB, Moore E, Ramage D, et al. *Communication-Efficient Learning of Deep Networks from Decentralized Data.* AISTATS, 2017.
- Rieke N, Hancox J, Li W, et al. *The future of digital health with federated learning.* npj Digital Medicine, 2020.
- Sheller MJ, Edwards B, Reina GA, et al. *Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data.* Scientific Reports, 2020.
- Kaissis GA, Makowski MR, Ruckert D, Braren RF. *Secure, privacy-preserving and federated machine learning in medical imaging.* Nature Machine Intelligence, 2020.
- Pati S, Baid U, Edwards B, et al. *Federated learning enables big data for rare cancer boundary detection.* Nature Communications, 2022.
- Dwork C, Roth A. *The Algorithmic Foundations of Differential Privacy.* Foundations and Trends in Theoretical Computer Science, 2014.

## Fairness and equity in healthcare AI

**Why this matters.** Healthcare AI inherits the
inequities of its training data, evaluation populations,
and deployment settings. Fairness here is not a constraint
added on top but a question about whose errors the system
absorbs.

**Questions to track.**

- Which design choices most often introduce or magnify
  disparities, and at what stage do they enter?
- How are subgroup performance and post-hoc fairness
  adjustments distinguished from upstream design fixes?
- How do equity questions in drug discovery, trials, and
  clinical deployment connect to each other?

**Readings.**

- Obermeyer Z, Powers B, Vogeli C, Mullainathan S. *Dissecting racial bias in an algorithm used to manage the health of populations.* Science, 2019.
- Pierson E, Cutler DM, Leskovec J, Mullainathan S, Obermeyer Z. *An algorithmic approach to reducing unexplained pain disparities in underserved populations.* Nature Medicine, 2021.
- Seyyed-Kalantari L, Zhang H, McDermott MBA, Chen IY, Ghassemi M. *Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations.* Nature Medicine, 2021.
- Rajkomar A, Hardt M, Howell MD, Corrado G, Chin MH. *Ensuring Fairness in Machine Learning to Advance Health Equity.* Annals of Internal Medicine, 2018.
- Chen IY, Joshi S, Ghassemi M. *Treating health disparities with artificial intelligence.* Nature Medicine, 2020.
- Ghassemi M, Naumann T, Pierson E. *The False Hope of Current Approaches to Explainable Artificial Intelligence in Health Care.* Lancet Digital Health, 2021.

## Reproducibility in healthcare ML

**Why this matters.** Reporting, code release, and
benchmark design determine whether a healthcare ML claim
can be checked. Reproducibility is a precondition for
accumulating evidence.

**Questions to track.**

- What is the minimum reporting standard that lets a
  third party challenge or replicate a clinical ML claim?
- How are chemistry benchmarks designed to expose
  generalization rather than reward memorization?
- Where do reproducibility critiques themselves rely on
  evidence rather than assertion?

**Readings.**

- McDermott MBA, Wang S, Marinsek N, et al. *Reproducibility in machine learning for health research: still a ways to go.* Science Translational Medicine, 2021.
- Stupple A, Singerman D, Celi LA. *The reproducibility crisis in the age of digital medicine.* npj Digital Medicine, 2019.
- Wynants L, Van Calster B, Collins GS, et al. *Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal.* BMJ, 2020.
- Roberts M, Driggs D, Thorpe M, et al. *Common pitfalls and recommendations for using machine learning to detect and prognosticate for COVID-19 using chest radiographs and CT scans.* Nature Machine Intelligence, 2021.
- Wallach IZ, Heifets A. *Most Ligand-Based Classification Benchmarks Reward Memorization Rather than Generalization.* Journal of Chemical Information and Modeling, 2018.
- Bender A, Cortes-Ciriano I. *Artificial intelligence in drug discovery: what is realistic, what are illusions? Part 1.* Drug Discovery Today, 2021.
- Bender A, Cortes-Ciriano I. *Artificial intelligence in drug discovery: what is realistic, what are illusions? Part 2.* Drug Discovery Today, 2021.

## Hospital cybersecurity, telehealth, and process mining

**Why this matters.** AI deployments share infrastructure
with the rest of the hospital. Cybersecurity events,
telehealth data flows, and the actual paths patients take
through care all shape what a deployed AI system sees.

**Questions to track.**

- How are AI components included in hospital incident
  response?
- How does the data captured during telehealth differ
  from in-person data, and how does that affect models
  trained on either?
- Which clinical pathways diverge from documented care
  maps, and how do those divergences appear in event logs?

**Readings.**

- Coventry L, Branley D. *Cybersecurity in healthcare: A narrative review of trends, threats and ways forward.* Maturitas, 2018.
- Webster P. *Virtual health care in the era of COVID-19.* Lancet, 2020.
- Mans RS, van der Aalst WMP, Vanwersch RJB. *Process Mining in Healthcare: Evaluating and Exploiting Operational Healthcare Processes.* Springer, 2015.
- Rojas E, Munoz-Gama J, Sepulveda M, Capurro D. *Process mining in healthcare: A literature review.* Journal of Biomedical Informatics, 2016.

## Drug discovery extensions: knowledge graphs, protein design, trials, and pharmacovigilance

**Why this matters.** Beyond small-molecule chemistry,
discovery and post-market work depend on biomedical
knowledge organization, protein design, AI-assisted trial
design, and signal detection. Each of these connects
upstream design to downstream evidence.

**Questions to track.**

- How are biomedical knowledge graphs curated, and how
  stale do they become?
- How is in-silico protein design validated, and what is
  the failure rate from sequence to functional assay?
- How are AI-assisted trial-design choices documented for
  regulatory review?
- How are pharmacovigilance signals fed back into the
  design pipeline?

**Readings.**

- Reker D, Schneider G. *Active-learning strategies in computer-assisted drug discovery.* Drug Discovery Today, 2015.
- Himmelstein DS, Lizee A, Hessler C, et al. *Systematic integration of biomedical knowledge prioritizes drugs for repurposing.* eLife, 2017.
- Zitnik M, Agrawal M, Leskovec J. *Modeling polypharmacy side effects with graph convolutional networks.* Bioinformatics, 2018.
- Dauparas J, Anishchenko I, Bennett N, et al. *Robust deep learning-based protein sequence design using ProteinMPNN.* Science, 2022.
- Watson JL, Juergens D, Bennett NR, et al. *De novo design of protein structure and function with RFdiffusion.* Nature, 2023.
- Harrer S, Shah P, Antony B, Hu J. *Artificial Intelligence for Clinical Trial Design.* Trends in Pharmacological Sciences, 2019.
- Liu R, Rizzo S, Whipple S, et al. *Evaluating eligibility criteria of oncology trials using real-world data and AI.* Nature, 2021.
- Ball R, Dal Pan G. *"Artificial Intelligence" for Pharmacovigilance: Ready for Prime Time?* Drug Safety, 2022.
