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

**Readings to add.**

- TODO: histories and reviews of clinical decision support.
- TODO: post-mortems of deployed systems.
- TODO: studies on workflow and adoption.

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

**Readings to add.**

- TODO: reviews of deployment-aware machine learning.
- TODO: case studies of deployed medical AI systems.
- TODO: frameworks for validation and monitoring stages.

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

**Readings to add.**

- TODO: surveys of interpretability methods.
- TODO: user studies on explanation use.
- TODO: critiques of interpretability claims.

## Monitoring and dataset shift

**Why this matters.** Dataset shift is the main way that a
deployed model silently stops working. Monitoring is the main
way anyone notices.

**Questions to track.**

- Which shift detection methods are practical at a single site?
- How are monitoring metrics chosen so that they are both
  informative and maintainable?
- How is a detected shift translated into an action?

**Readings to add.**

- TODO: surveys of dataset shift.
- TODO: papers on monitoring in healthcare AI.
- TODO: reports from deployed monitoring systems.

## Governance and safety

**Why this matters.** Governance determines what happens after
something goes wrong, and often whether anyone notices. It is a
social problem as much as a technical one.

**Questions to track.**

- Who is accountable for each stage of a deployed system?
- How are updates reviewed and approved?
- What does a minimum viable governance structure look like at
  a single site?

**Readings to add.**

- TODO: regulatory and policy frameworks.
- TODO: institutional governance templates.
- TODO: incident reports and post-mortems.
