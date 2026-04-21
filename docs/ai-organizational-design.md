# AI organizational design

Notes on the organizational structure around a clinical AI
system: stakeholders, roles, responsibilities, decision
rights, and operating cadence. The framing treats the
organization as part of the system.

## Why organization

A deployed AI system is embedded in an organization. Who
decides when a model is released, who is called when it
breaks, who signs off on an update, and who decides to
retire it are organizational questions, not technical
ones. A system without these questions answered has no
operator.

## Stakeholder map

A stakeholder map for a hospital-deployed AI system
typically includes:

- **Patients.** The people whose data and outcomes are
  affected.
- **Clinicians.** Users who see outputs and act on them.
- **Clinical champion.** A clinician accountable for the
  clinical fit of the system.
- **Nursing and allied health.** Often the first to see
  alerts in practice.
- **IT and informatics.** Infrastructure, integration, and
  access control.
- **Hospital administration.** Budget, risk, and strategic
  alignment.
- **Data stewards.** Accountable for data quality and
  lineage.
- **Model owner.** Accountable for model behavior across
  its lifecycle.
- **Validation lead.** Accountable for local validation.
- **Operations engineer.** Accountable for serving and
  monitoring reliability.
- **Governance committee.** Approves, reviews, retires
  models.
- **Privacy and compliance office.** Interprets regulatory
  and consent constraints.
- **Vendor or developer.** The external party that
  supplies the model or platform.
- **Regulators and payers.** External actors whose rules
  and incentives shape the space.

Each stakeholder has needs, concerns, and authority. A
stakeholder value flow (who provides what to whom) is a
useful companion to the stakeholder list.

## Roles and responsibilities

A minimum set of named roles for an operational clinical
AI system:

- **Model owner.** Single accountable party for model
  behavior across the lifecycle. Signs off on gates,
  authorizes changes, owns postmortems.
- **Data steward.** Accountable for the sources the model
  depends on, their quality, and their lineage.
- **Validation lead.** Runs local validation and signs off
  on Gates 3 and 4 in the lifecycle.
- **Operations engineer.** Maintains serving and monitoring
  infrastructure. On-call for operational incidents.
- **Clinical champion.** Represents clinical users, signs
  off on workflow fit, participates in retirement
  decisions.
- **Governance committee chair.** Runs the committee that
  approves, reviews, and retires models.
- **Incident commander.** Coordinates response during an
  incident above a defined severity threshold.
- **Privacy officer.** Interprets consent and privacy
  requirements in concrete cases.

Some roles are combined in smaller organizations; larger
organizations may split them further. Combining roles that
should provide independent review (validation and
ownership, for example) is a common source of failure.

## RACI for key decisions

For each significant decision, specify responsible,
accountable, consulted, informed (RACI) parties. A
starting pattern:

- **Release a new model version.** Model owner A;
  validation lead R; clinical champion C; ops R;
  governance I (or A for high-risk changes).
- **Declare a clinical AI incident.** Clinical champion
  R; incident commander A; ops R; governance C; privacy
  officer C if data at issue.
- **Approve a model update inside the change control
  plan.** Model owner R; validation lead A; governance I.
- **Approve a model update outside the change control
  plan.** Model owner R; validation lead C; governance A.
- **Retire a model.** Clinical champion R; model owner
  R; governance A; ops I.

The exact assignments depend on the organization's other
governance structures. The discipline is having them
written down.

## Governance operating model

A functioning governance committee needs more than a
membership list:

- **Cadence.** A regular meeting (monthly is common) with
  a standing agenda.
- **Intake process.** A defined way for new AI proposals
  to enter review, with standard documentation.
- **Review criteria.** What the committee checks at each
  stage gate.
- **Escalation paths.** When a decision goes beyond the
  committee.
- **Retirement review.** Periodic review of deployed
  systems against retirement criteria.
- **Records.** Meeting minutes and decision log retained
  for audit.

A committee without a documented operating model tends to
rubber-stamp new requests and defer retirement.

## Incident response structure

Operational incidents follow a lifecycle:

- **Detection.** A monitoring signal or user report meets
  a threshold.
- **Triage.** The operations engineer and on-call clinical
  champion assess severity.
- **Mitigation.** Roll back, restrict traffic, disable
  outputs, or fall back to a safe mode.
- **Resolution.** Restore the service or retire the use.
- **Postmortem.** Blameless root-cause analysis with
  actions tracked to closure.

Severity levels should be defined in advance. Incident
severity drives who is paged and how fast.

## Organizational anti-patterns

Observable failure modes in organization design:

- **Orphan models.** Deployed models with no named
  model owner.
- **Validation-owner conflation.** The same person who
  built the model validates it.
- **Passive governance.** Committees that approve new
  systems but never retire old ones.
- **Absent clinical champion.** No clinician accountable
  for workflow fit.
- **Vendor-driven updates.** The vendor updates
  production without the organization's update governance
  being exercised.

## Open questions

- What is the smallest functioning governance committee
  for a single-site hospital?
- How does responsibility partition when the vendor
  retains some of the lifecycle steps?
- How are cross-team postmortems structured when a
  failure spans data, model, serving, and clinical
  layers?
- How is stakeholder value flow documented and kept
  current as the system changes?

## Related notes

- `docs/pharma-ai-system-of-systems.md` — cross-stage
  roles and boundary-spanning responsibilities that
  complement the within-system RACI here.
- `docs/human-ai-interaction-patterns.md` — how
  user-facing roles interact with the system, which
  the organizational structure has to support.
- `docs/mlops-for-regulated-ai.md` — role separation
  and access control under SaMD and MIDD
  expectations.
- `docs/ai-risk-and-reliability.md` — incident
  response structure that these roles have to
  execute.

## Limitations and cautions

- Organization design is descriptive here; no single set
  of roles is universally correct.
- RACI templates become noise if not maintained; the
  discipline is in the conversations they force, not in
  the document.
- Governance descriptions reflect patterns in the
  literature, not any specific institution.
