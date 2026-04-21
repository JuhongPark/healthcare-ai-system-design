# Clinical AI case studies

A reading-style synthesis of published cases of clinical AI
deployment, with attention to what each case illustrates
about the systems gap between development and deployment.

## Why case studies

The system-design notes elsewhere in this repository read as
principles. Case studies make the same concerns concrete by
showing how specific systems failed or succeeded in specific
settings. The aim here is not to rank vendors or products
but to read the published literature with deployment lessons
in mind.

## The Epic Sepsis Model

Wong and colleagues (2021) externally validated a
proprietary sepsis prediction model widely deployed across
U.S. hospitals and reported substantially lower performance
than the vendor's internal evaluation suggested. Habib, Lin,
and Grant (2021) framed the case in an editorial as an
argument for routine external validation of widely deployed
clinical AI.

**What it illustrates.** A model that was well-marketed and
broadly deployed had not been independently validated at
deployment scale until clinicians at one site decided to
look. The gap between vendor reporting and external
performance shaped subsequent discussion of mandatory model
labeling and hospital-side validation duties.

**System lessons.** Local validation is the evidence that
matters for the local decision to deploy. Vendor performance
claims are not a substitute. Documentation patterns such as
model facts labels (Sendak et al., 2020) are part of the
response, not the whole response.

## Diabetic retinopathy screening in Thai clinics

Beede and colleagues (2020) reported on the human-centered
deployment of a deep-learning system for diabetic
retinopathy screening across eleven Thai clinics. Lab
accuracy exceeded ninety percent; in deployment, image
quality, network reliability, and workflow fit drove
substantial workflow disruption.

**What it illustrates.** Lab metrics and clinic metrics are
different metrics. The deployment context — patient queues,
network bandwidth, image-capture conditions, follow-up
referral pathways — determined whether the model's outputs
were useful.

**System lessons.** Workflow integration and operational
context are first-class design constraints, not residual
issues to address after a model is built. A high lab
benchmark is necessary but not sufficient.

## IBM Watson for Oncology

Trade press and clinician commentary documented a
substantial gap between marketing and capability for the
IBM Watson for Oncology product line (Strickland, 2019, in
IEEE Spectrum). The full picture is dispersed across
journalism, clinician reports, and partner-institution
statements; there is no single peer-reviewed paper that
captures the trajectory.

**What it illustrates.** A high-profile clinical AI program
can fail not from a single technical decision but from a
chain of mismatches: between the data the system was
trained on, the populations it was deployed in, the
workflows it needed to fit, and the claims that were made
about it.

**System lessons.** Clear and honest scoping at deployment
time is a safety property, not a marketing concern.
Cross-institution generalization should be treated as a
hypothesis that needs evidence, not a default assumption.

## Translation pipelines: Duke

Sendak and colleagues at Duke have written several papers
describing what it takes to translate a machine learning
product into healthcare delivery: a coordinated process
involving data infrastructure, validation, integration,
documentation, and ongoing monitoring (Sendak et al., 2020;
2020 model facts label work). The model facts label sits
inside that wider pipeline.

**What it illustrates.** Translation is a process, not an
event, and is staffed accordingly when it works. The
pipeline is more than a notebook handed to an integration
team.

**System lessons.** A hospital that wants to deploy AI
sustainably has to fund the translation work, not only the
model work. Documentation patterns travel with the model.

## Framings from clinicians and researchers

Char, Shah, and Magnus (2018) framed the implementation of
machine learning in healthcare as an ethical problem
requiring attention to bias, accountability, and informed
consent. Coiera (2019) called the gap between model
performance and clinical impact the last mile and argued
that closing it is a sociotechnical, not technical, problem.
Shah, Milstein, and Bagley (2019) argued that making models
clinically useful requires reasoning about decision context
and counterfactual outcomes, not only predictive accuracy.

**System lessons.** The framing matters: questions that
look technical (calibration, threshold choice) are also
ethical (which patients carry the cost of false negatives).
Treating these together avoids fixing one and breaking the
other.

## What case studies cannot do

Each case study describes a particular setting at a
particular time. The lessons generalize as questions, not
answers: any new deployment has to ask the same questions
for itself. A case study is a reading prompt, not a recipe.

## Limitations and cautions

- Case study summaries reflect the published record, not
  proprietary information from the institutions or vendors
  involved.
- Vendor and product references are descriptive, not
  evaluative; they appear because the public literature is
  built around them.
- The set of case studies covered here is illustrative, not
  exhaustive.
