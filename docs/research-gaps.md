# Research gaps and next development plan

This document converts the literature review into development
work. The goal is to identify what the repository still lacks
relative to its own system-design thesis.

## High-priority gaps

### Unified synthetic case study

The repository has three useful prototypes: RWE, CDS, and
monitoring. They are still separate sketches. The literature
supports a stronger story in which the same synthetic clinical
program moves from evidence design, to workflow display, to
post-deployment monitoring.

Completed foundation: `case-studies/synthetic-care-program/`
now links one synthetic dataset, one evidence-design report, one
dashboard, one monitoring report, one incident table, one
governance decision, one safety-case report, and one evaluation
registry.

Next work: deepen the case with richer target-trial sensitivity
sections, dashboard variants, proxy-label audit, and more
realistic synthetic data adapters.

### Data and model documentation

Datasheets, Model Cards, CONSORT-AI, SPIRIT-AI, DECIDE-AI, and
WHO guidance all point toward structured documentation. The repo
now has reusable documentation templates and first-pass
prototype artifacts. The remaining gap is to keep those artifacts
current as prototype behavior changes and to deepen them where a
prototype becomes more executable.

Completed foundation:

- `templates/data-card.md`
- `templates/model-card.md`
- `templates/evaluation-registry.csv`
- `templates/interface-contract.md`
- `templates/governance-gate-review.md`

Next work: add richer prototype-specific evidence packets when
the RWE, CDS, monitoring, fairness, and pharma sketches expand.

### RWE protocol discipline

The RWE prototype demonstrates confounding, weighting, balance,
and a negative-control outcome. It does not yet make target
trial emulation or active comparator new-user design explicit.

Next work: add a target trial table to the example report,
including eligibility, treatment strategies, assignment time,
follow-up, outcome, causal contrast, and analysis plan. Add a
sensitivity grid that varies comparator, eligibility window, and
outcome ascertainment.

### CDS workflow experiment

The dashboard is a single interface sketch. The CDS literature
suggests that workflow timing and alert form are core design
variables, not polish.

Next work: generate three dashboard variants: passive banner,
inline action prompt, and interruptive alert. Report the
expected user burden, audit event, and failure mode for each.

### Monitoring incident workflow

The monitoring loop detects drift and calibration movement, but
it does not yet show how a governance owner acts on a signal.

Next work: add incident records with severity, trigger metric,
suspected root cause, required review, decision, owner, and
follow-up date. Link incidents to evaluation registry entries.

### Equity and proxy-label audit

The repository discusses fairness, but no prototype performs a
proxy-label audit. Obermeyer et al. make this a high-value next
step because proxy choice can encode inequity before model
training begins.

Next work: add a small synthetic audit that compares a proxy
label against a latent need variable, then shows how performance
and allocation differ by subgroup.

### Pharma executable prototype

The pharma track is conceptually developed but lacks an
executable sketch. The literature suggests a public-data
property-prediction or ADMET prototype with careful benchmark
framing.

Next work: build a lightweight public benchmark prototype that
reports data split, applicability domain, calibration, and
handoff decision. Avoid therapeutic claims.

## Evidence gaps

The current survey is broad enough to justify the repository's
direction, but it is not the final literature base.

Missing or shallow areas:

- recent AI prediction-model reporting standards beyond the
  current guideline set
- implementation science for clinical AI adoption
- alert fatigue and clinician workload measurement
- post-deployment monitoring methods for single-site clinical AI
- evaluation of foundation models and generative AI in health
- regulatory change-control practice after AI/ML SaMD guidance
- drug discovery applicability-domain and assay-handoff
  literature

These should be handled as additional waves, not mixed into the
first survey retroactively.

## Proposed research waves

### Wave 2: reporting and evaluation guidelines

Extend the evidence matrix with prediction-model reporting,
diagnostic accuracy, early evaluation, prospective validation,
and reproducibility guidance. Output: a repo-specific evaluation
packet template.

### Wave 3: implementation science and workflow evidence

Survey CDS implementation, alert fatigue, human factors,
workflow integration, and audit logging. Output: dashboard
variant requirements and a usability-evaluation checklist.

### Wave 4: monitoring and regulated MLOps

Survey dataset shift, performance monitoring, update governance,
change control, rollback, and incident management. Output:
monitoring incident schema and governance gate definitions.

### Wave 5: pharma and drug development validation

Survey molecular ML benchmarking, ADMET, applicability domain,
assay validation, model-informed drug development, and
AI-enabled discovery case studies. Output: first public-data
pharma prototype design.

## Implementation order

Completed:

- Major improvement milestones are saved in
  `docs/major-improvement-milestones.md`.
- Safety-case thesis and object model are defined in
  `docs/project-thesis.md` and `docs/safety-case-framework.md`.
- The flagship executable case lives in
  `case-studies/synthetic-care-program/`.
- Shared templates for data cards, model cards, interface
  contracts, evaluation registry, and governance gate reviews.
- First-pass application of those artifacts to the three
  existing executable prototypes.
- Automated tests that check artifact presence, safety language,
  evaluation registry columns, citation ID validity, and the
  synthetic safety-case workflow.

Next:

1. Expand the flagship case with richer target-trial sensitivity
   design sections.
2. Add CDS dashboard variants for workflow comparison.
3. Add a proxy-label fairness audit.
4. Add a realistic synthetic data adapter.
5. Add the first public-data pharma prototype after the
   healthcare safety case remains stable.

This order keeps the repository aligned with the literature:
make the system spine explicit before adding larger or more
ambitious modeling work.
