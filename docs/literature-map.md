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

**Readings to add.**

- TODO: foundational references on trial design and endpoints.
- TODO: references on heterogeneity of treatment effect.
- TODO: references on safety signal evaluation.

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

**Readings to add.**

- TODO: overviews of real-world evidence frameworks.
- TODO: methodological papers on cohort construction.
- TODO: empirical comparisons of observational and trial
  estimates.

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

**Readings to add.**

- TODO: methodological reviews of comparative effectiveness
  research.
- TODO: case studies where comparator choice changed the
  conclusion.
- TODO: frameworks for clinical utility.

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

**Readings to add.**

- TODO: textbook references on causal inference.
- TODO: papers on propensity score methods and their failures.
- TODO: papers on negative controls and bias detection.

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

**Readings to add.**

- TODO: overviews of precision medicine concepts.
- TODO: critical reviews of precision medicine claims.
- TODO: patient-communication studies.

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

**Readings to add.**

- TODO: reviews of multimodal medical learning.
- TODO: papers on missing-modality robustness.
- TODO: papers on cross-site and cross-modality validation.

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
