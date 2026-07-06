# Annotated bibliography for healthcare AI system design

This bibliography backs the repository's current direction:
healthcare AI should be designed as a full system, not as a
model-only artifact. Entries are intentionally short. They focus
on the design implication for this repository rather than on
complete paper summaries.

## Kelly et al. 2019 - Key challenges for clinical impact

Kelly et al. frame the translation problem directly: healthcare
AI has many impressive retrospective demonstrations but few
robust deployments with proven clinical impact. The paper
emphasizes independent and local test sets, clinically meaningful
metrics, prospective evaluation, regulation, dataset shift,
bias, and post-market surveillance. This is the best single
orientation paper for the repository's system-level stance.

System-design implication: every prototype should state what it
does not prove, and every model-like output should be paired
with validation, workflow, and monitoring questions.

Repo links: Track 3, Track 4, Track 7,
`prototypes/cds-risk-dashboard`, `prototypes/monitoring-loop-sketch`.

Source: https://doi.org/10.1186/s12916-019-1426-2

## Sculley et al. 2015 - Hidden technical debt in ML systems

Sculley et al. explain why ML systems accumulate maintenance
costs through hidden feedback loops, data dependencies,
configuration complexity, undeclared consumers, and changes in
the external world. Although not healthcare-specific, it is one
of the strongest foundations for treating monitoring,
interfaces, and ownership as architectural concerns. It supports
the repo's claim that a model artifact is not a deployable
system.

System-design implication: the repository should keep building
explicit contracts, audit surfaces, and monitoring outputs.

Repo links: Track 4, Track 7, `prototypes/monitoring-loop-sketch`.

Source: https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html

## Wong et al. 2021 - External validation of the Epic Sepsis Model

Wong et al. externally evaluated a widely implemented
proprietary sepsis prediction model and found substantially
worse performance than developer-reported results. The paper is
a concrete warning against deployment without local validation,
calibration analysis, threshold evaluation, and alert-burden
analysis. It is especially useful because it connects model
performance to a real operational context.

System-design implication: the monitoring prototype should
remain central, and any CDS interface should include calibration,
alerting, and audit considerations.

Repo links: Track 3, Track 4, Track 5,
`prototypes/cds-risk-dashboard`, `prototypes/monitoring-loop-sketch`.

Source: https://doi.org/10.1001/jamainternmed.2021.2626

## Beede et al. 2020 - Human-centered deployment in diabetic retinopathy

Beede et al. studied a deep learning system deployed in clinics
for diabetic retinopathy screening. The value of the paper is
not only model evaluation but the field evidence about workflow,
trust, infrastructure, and human interaction. It shows that a
system can fail or change meaning when moved from controlled
evaluation into actual work.

System-design implication: the CDS dashboard should foreground
workflow timing, user role, limitations, and override capture.

Repo links: Track 3, Track 5, Track 7,
`prototypes/cds-risk-dashboard`.

Source: https://doi.org/10.1145/3313831.3376718

## Liu et al. 2020 - CONSORT-AI

CONSORT-AI extends clinical trial reporting standards for
interventions involving AI. It asks trial reports to describe the
AI intervention, setting, input and output handling, human-AI
interaction, and error cases. The paper is useful even though
the repository is not running clinical trials, because it
defines what transparent AI evaluation should eventually contain.

System-design implication: prototype reports should document
intended use, setting, input/output handling, interaction
surface, error modes, and limitations.

Repo links: Track 3, Track 7, all prototype reports.

Source: https://doi.org/10.1038/s41591-020-1034-x

## Rivera et al. 2020 - SPIRIT-AI

SPIRIT-AI complements CONSORT-AI by addressing clinical trial
protocols for AI interventions. It reinforces prospective
specification: intended use, users, setting, data inputs, and
human-AI interaction should be defined before evaluation. For
this repository, the key lesson is to make design assumptions
visible before showing model-like outputs.

System-design implication: future prototypes should begin with a
protocol-like design card.

Repo links: Track 3, Track 7, future case study templates.

Source: https://doi.org/10.1038/s41591-020-1037-7

## WHO 2021 - Ethics and governance of AI for health

WHO's guidance sets a governance frame around health AI:
ethics, human rights, accountability, affected communities, and
the responsibilities of public and private actors. It is not a
modeling paper, but it is central to the repository's public
safety posture. It supports the repeated no-clinical-use and
synthetic-only constraints in the prototypes.

System-design implication: safety labels and accountability
surfaces are part of the design, not decorative caveats.

Repo links: Cross-cutting, Track 4, Track 7, all prototypes.

Source: https://www.who.int/publications/i/item/9789240029200

## FDA 2018 - Real-World Evidence Program

FDA's RWE framework distinguishes real-world data from
real-world evidence and emphasizes the reliability and relevance
of data sources as well as study methodology. This directly backs
the RWE prototype's cautious framing. Synthetic outputs are useful
for illustrating method behavior, but they cannot be treated as
evidence about real products or patients.

System-design implication: RWE work should separate data fitness,
study design, causal assumptions, and regulatory claim strength.

Repo links: Track 1, `prototypes/rwe-drug-efficacy-sketch`.

Source: https://www.fda.gov/media/120060/download

## Lund et al. 2015 - Active comparator new-user design

Lund, Richardson, and Sturmer review the active comparator
new-user design as a way to mitigate biases in
pharmacoepidemiology and approximate head-to-head trial logic.
It is important for the RWE prototype because it shifts the focus
from modeling after the fact to careful cohort construction
before analysis.

System-design implication: the next RWE iteration should add
explicit index-date, comparator, and new-user design variants.

Repo links: Track 1, `prototypes/rwe-drug-efficacy-sketch`.

Source: https://doi.org/10.1007/s40471-015-0053-5

## Hernan and Robins 2016 - Target trial emulation

Hernan and Robins argue that observational analyses should be
designed by first specifying the randomized trial they would have
liked to run. This is a core guardrail for the repository's RWE
direction. It prevents analysis from becoming a model-first
exercise and makes assumptions easier to audit.

System-design implication: RWE outputs should include a
target-trial-style design table.

Repo links: Track 1, future RWE expansion.

Source: https://doi.org/10.1093/aje/kwv254

## Rosenbaum and Rubin 1983 - Propensity scores

Rosenbaum and Rubin established the propensity score as a
balancing score in observational causal studies under defined
assumptions. The RWE prototype uses propensity weighting as a
teaching device, not as proof that the synthetic association is
causal. The paper is foundational for explaining what adjustment
can and cannot repair.

System-design implication: balance diagnostics and assumption
labels should remain visible beside estimates.

Repo links: Track 1, `prototypes/rwe-drug-efficacy-sketch`.

Source: https://doi.org/10.1093/biomet/70.1.41

## Lipsitch et al. 2010 - Negative controls

Lipsitch, Tchetgen Tchetgen, and Cohen describe negative controls
as tools for detecting confounding and bias in observational
studies. This backs the RWE prototype's negative-control outcome.
The lesson is diagnostic humility: a negative control can reveal
problems, but a clean result does not automatically validate a
causal claim.

System-design implication: negative controls should be reported
as bias diagnostics.

Repo links: Track 1, `prototypes/rwe-drug-efficacy-sketch`.

Source: https://doi.org/10.1097/EDE.0b013e3181d61eeb

## Bates et al. 2003 - Ten commandments for CDS

Bates et al. provide durable design principles for effective
clinical decision support, especially workflow integration and
timely delivery. The paper supports the CDS prototype's focus on
when, where, and how a signal is shown. A risk score shown in the
wrong workflow location can be worse than useless.

System-design implication: CDS design should be judged by
workflow fit, timing, and user burden.

Repo links: Track 3, `prototypes/cds-risk-dashboard`.

Source: https://doi.org/10.1197/jamia.M1370

## Kawamoto et al. 2005 - CDS systematic review

Kawamoto et al. reviewed trials of clinical decision support and
identified features associated with success, including automatic
support, integration into workflow, and recommendations at the
time and location of decision-making. The paper gives empirical
backing to the dashboard's workflow-first posture.

System-design implication: future CDS prototypes should compare
passive indicators, inline signals, and interruptive alerts.

Repo links: Track 3, future CDS experiments.

Source: https://doi.org/10.1136/bmj.38398.500764.8F

## Tonekaboni et al. 2019 - What clinicians want

Tonekaboni et al. surveyed clinicians about explainability for
clinical ML. The paper shows that explanations are not generic
objects; they depend on setting, user needs, and the action being
supported. This aligns with the dashboard's explanation caveats.

System-design implication: explanation panels should show what
they do not explain.

Repo links: Track 3, `prototypes/cds-risk-dashboard`.

Source: https://arxiv.org/abs/1905.05134

## Gebru et al. 2021 - Datasheets for Datasets

Datasheets for Datasets proposes structured dataset
documentation covering motivation, composition, collection, use,
and limitations. The repository already describes synthetic data
sources, but a formal data-card template would make the
prototypes more reusable.

System-design implication: add `templates/data-card.md` and
apply it to each synthetic generator.

Repo links: Track 2, Track 4, Track 7, all prototypes.

Source: https://arxiv.org/abs/1803.09010

## Mitchell et al. 2019 - Model cards

Model Cards for Model Reporting proposes concise documentation
for model intended use, evaluation, limitations, and subgroup
performance. The repository does not yet have real models, but
its synthetic analyses still produce model-like outputs. The
model-card concept should shape future artifact templates.

System-design implication: add `templates/model-card.md` and
link it to evaluation registry work.

Repo links: Track 4, Track 7, all prototypes.

Source: https://arxiv.org/abs/1810.03993

## Obermeyer et al. 2019 - Racial bias in a health algorithm

Obermeyer et al. showed how a seemingly race-neutral population
health algorithm became biased because healthcare cost was used
as a proxy for health need. This is an essential case for the
repository's data and ethics posture: labels and proxies are
design decisions with equity consequences.

System-design implication: future prototypes should include a
proxy-label audit step before model evaluation.

Repo links: Track 2, Track 3, Track 7.

Source: https://doi.org/10.1126/science.aax2342

## Vamathevan et al. 2019 - ML in drug discovery and development

Vamathevan et al. review ML applications across drug discovery
and development, while emphasizing interpretability,
repeatability, data quality, and validation challenges. It
supports the pharma track's stance that discovery models are
program components rather than proof of therapeutic value.

System-design implication: future pharma prototypes should
document applicability domain, assay handoff, and stage-gate
evidence.

Repo links: Track 6, Track 7.

Source: https://doi.org/10.1038/s41573-019-0024-5

## Wu et al. 2018 - MoleculeNet

MoleculeNet provides benchmark datasets and evaluation practices
for molecular ML. It is useful for future property-prediction or
ADMET sketches because it shows why benchmark choice, task
definition, imbalance, and data scarcity matter. It also gives a
public-data path that stays inside repository safety rules.

System-design implication: future molecular prototypes should
use public benchmarks and report limitations, not just scores.

Repo links: Track 6.

Source: https://doi.org/10.1039/C7SC02664A

## Vasey et al. 2022 - DECIDE-AI

DECIDE-AI is a consensus reporting guideline for early-stage
clinical evaluation of AI-driven decision support systems. It
bridges the gap between in silico performance and full clinical
trials by focusing on small-scale clinical performance, safety,
human factors, and implementation context.

System-design implication: future CDS and monitoring prototypes
should define an early evaluation packet before they present any
workflow-readiness claim.

Repo links: Track 3, Track 4, Track 7,
`prototypes/cds-risk-dashboard`, `prototypes/monitoring-loop-sketch`.

Source: https://doi.org/10.1038/s41591-022-01772-9
