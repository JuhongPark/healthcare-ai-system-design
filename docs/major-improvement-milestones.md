# Major improvement milestones

This plan captures the next major improvement path for the
repository. The goal is not to add more disconnected prototypes.
The goal is to turn the repository into an executable synthetic
healthcare AI safety-case framework.

## North star

Build an executable synthetic healthcare AI safety case that
shows how evidence design, workflow display, monitoring,
incident response, and governance decisions connect across an AI
lifecycle.

The repository should make this claim concrete:

> Healthcare AI safety is a lifecycle evidence problem, not only
> a model performance problem.

The flagship artifact should show why a system is not ready for
deployment, what evidence is missing, what failure signals were
observed, and which governance decision follows.

## Critical repositioning

The current repository is valuable, but still reads as a broad
research workspace with several synthetic sketches. The major
upgrade is to reposition it as a safety-case simulator.

Current center of gravity:

- literature-backed research notes
- separate synthetic RWE, CDS, and monitoring prototypes
- governance artifact templates and first-pass documentation

Target center of gravity:

- one executable end-to-end synthetic care program
- traceable safety-case outputs
- failure-first demonstrations
- governance decisions linked to evidence and incidents
- existing prototypes treated as components of the flagship
  safety case

## Target structure

The flagship case study should live under:

```text
case-studies/synthetic-care-program/
  README.md
  run_case.py
  artifacts/
    data-card.md
    model-card.md
    interface-contract.md
    governance-gate-review.md
  outputs/
    synthetic_cohort.csv
    target_trial_spec.md
    evidence_report.md
    cds_dashboard.html
    workflow_audit_log.csv
    monitoring_stream.csv
    monitoring_report.md
    incidents.csv
    governance_decision.md
    safety_case.md
    evaluation_registry.csv
```

All generated outputs should share a case identifier, artifact
identifier, and evaluation identifier where relevant.

## Milestone 1: Define the safety-case thesis

Objective: make the new project identity explicit.

Planned work:

- Add `docs/project-thesis.md`.
- Add `docs/safety-case-framework.md`.
- Update the README to state that the repository demonstrates
  an executable synthetic healthcare AI safety case.

Acceptance criteria:

- The project thesis explains why the repository focuses on
  lifecycle evidence rather than model performance alone.
- The safety-case framework defines claims, evidence, hazards,
  mitigations, open assumptions, incidents, and governance
  decisions.
- The documents preserve the safety boundary: synthetic-only,
  not medical advice, not clinical decision support, and not
  evidence about real patients.

Suggested commit:

- `docs: define safety case project thesis`

## Milestone 2: Add the end-to-end synthetic case study

Objective: create the flagship executable case.

Planned work:

- Add `case-studies/synthetic-care-program/README.md`.
- Add `case-studies/synthetic-care-program/run_case.py`.
- Generate a synthetic cohort, evidence report, target trial
  specification, dashboard, audit log, monitoring stream,
  monitoring report, safety case, and evaluation registry.
- Keep the implementation standard-library-only unless a
  dependency is explicitly approved.

Acceptance criteria:

- One command regenerates the full case:
  `python case-studies/synthetic-care-program/run_case.py`.
- Outputs are committed as small example artifacts.
- Each output states that it is synthetic, not medical advice,
  not clinical decision support, and not evidence about real
  patients.
- The case links evidence design, workflow display, monitoring,
  and governance outputs through shared identifiers.

Suggested commit:

- `feat: add synthetic safety case study`

## Milestone 3: Make the case failure-first

Objective: make the demo powerful by showing failure signals
instead of only successful execution.

Planned work:

- Encode dataset shift in later monitoring periods.
- Encode calibration drift.
- Encode alert burden growth.
- Encode a proxy-label bias warning.
- Encode a negative-control warning or unresolved causal
  assumption.
- Generate `outputs/incidents.csv`.
- Generate `outputs/governance_decision.md`.

Acceptance criteria:

- At least one incident is generated on every default run.
- Each incident has severity, trigger metric, suspected root
  cause, required review, owner, decision, and follow-up date.
- The governance decision is selected from `continue`,
  `monitor`, `pause`, `update`, or `rollback`.
- The governance decision references the incident table and
  evaluation registry.

Suggested commit:

- `feat: add safety case incident workflow`

## Milestone 4: Generate an automated safety-case report

Objective: turn governance artifacts from static documentation
into generated system outputs.

Planned work:

- Generate `outputs/safety_case.md`.
- Include system claims, supporting evidence, missing evidence,
  known hazards, mitigations, open assumptions, incident links,
  governance decision, and next required review.
- Tie safety-case claims to citation IDs from
  `references/evidence-matrix.csv`.

Acceptance criteria:

- The safety case contains an explicit deployment-readiness
  conclusion.
- The default conclusion should not authorize deployment.
- Missing evidence is listed separately from known hazards.
- Every citation ID used in the report exists in the evidence
  matrix.

Suggested commit:

- `feat: generate safety case report`

## Milestone 5: Add automated safety-case guardrails

Objective: make the flagship case durable.

Planned work:

- Add `tests/test_synthetic_safety_case.py`.
- Verify that `run_case.py` executes in a temporary output
  directory.
- Verify that all expected outputs are created.
- Verify that safety language appears in the safety case,
  dashboard, governance decision, and evidence report.
- Verify that at least one incident is generated.
- Verify that the governance decision references incident and
  evaluation artifacts.
- Verify that citation IDs resolve to
  `references/evidence-matrix.csv`.

Acceptance criteria:

- Full unittest discovery passes.
- `scripts/check_claims.py` passes.
- The test fails if the flagship case stops producing an
  incident, safety case, or governance decision.

Suggested commit:

- `test: add synthetic safety case coverage`

## Milestone 6: Rewire the repository around the flagship

Objective: make the new center of gravity visible.

Planned work:

- Add `case-studies/README.md`.
- Update `README.md`.
- Update `docs/research-gaps.md`.
- Update `prototypes/README.md` to frame RWE, CDS, and
  monitoring sketches as components feeding the flagship case.

Acceptance criteria:

- A reader can understand the project by starting from the
  README and running the flagship case.
- The old prototype list no longer feels like the project
  center. It reads as a component library for safety-case work.
- Future pharma and ADMET work are described as extensions, not
  the near-term center.

Suggested commit:

- `docs: position synthetic safety case as flagship`

## Milestone 7: Add realism without losing safety

Objective: increase credibility after the synthetic safety case
works end to end.

Planned work:

- Evaluate a public synthetic healthcare data source such as a
  Synthea-style dataset, if licensing and dependency constraints
  are acceptable.
- Add a realistic synthetic data adapter that preserves the
  no-clinical-use boundary.
- Add optional public-data pharma or ADMET case study only after
  the healthcare safety case is stable.

Acceptance criteria:

- No protected health information, private patient data, or
  clinical-use implication is introduced.
- Any public data source has a documented license and provenance.
- The safety-case report continues to distinguish evidence
  demonstration from real-world clinical evidence.

Suggested commit:

- `feat: add realistic synthetic data adapter`

## Implementation priority

Immediate sequence:

1. Milestone 1: define the safety-case thesis.
2. Milestone 2: add the executable case study.
3. Milestone 3: add incidents and governance decisions.
4. Milestone 4: generate the safety-case report.
5. Milestone 5: add tests.
6. Milestone 6: rewire repo documentation.

Milestone 7 should wait until the flagship case is stable.

## Definition of done

The improvement program is complete when the repository can be
described accurately as:

> An executable synthetic healthcare AI safety-case framework
> that connects evidence design, workflow display, monitoring,
> incident response, and governance decisions.

Minimum evidence of completion:

- `python case-studies/synthetic-care-program/run_case.py`
  regenerates the flagship outputs.
- `outputs/safety_case.md` contains the deployment-readiness
  conclusion and missing-evidence list.
- `outputs/incidents.csv` contains at least one default incident.
- `outputs/governance_decision.md` references incident and
  evaluation artifacts.
- `python scripts/check_claims.py` passes.
- `python -m unittest discover -s tests` passes.

## Risks

- Scope creep: the repository could keep expanding tracks
  without a stronger flagship. Mitigation: prioritize the
  synthetic care program until it is coherent.
- Documentation without execution: safety-case artifacts could
  become static checklists. Mitigation: generate key outputs
  from `run_case.py`.
- False realism: richer synthetic data could make outputs look
  clinically meaningful. Mitigation: keep synthetic-only and
  no-clinical-use language in generated outputs and tests.
- Weak differentiation: healthcare AI governance is a crowded
  theme. Mitigation: focus on executable traceability from
  failure signal to governance decision.
