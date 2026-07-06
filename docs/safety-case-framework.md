# Safety-case framework

This framework defines the structure used by the repository's
synthetic healthcare AI safety cases. It is a practical artifact
model, not a regulatory submission template.

## Safety boundary

Every safety case in this repository is synthetic-only. It is
not medical advice, not clinical decision support, and not
evidence about real patients, real populations, real products,
or real clinical workflows.

## Core objects

### Case

A case is one end-to-end synthetic lifecycle example.

Required fields:

- case ID
- case title
- intended synthetic setting
- non-use boundary
- owner
- generated artifact list
- evidence references

### Claim

A claim is a statement the case evaluates. Claims should be
about lifecycle readiness, not clinical truth.

Examples:

- The synthetic system is not ready for deployment.
- Calibration drift requires governance review.
- The workflow interface is a hypothesis, not clinical decision
  support.
- Missing local validation blocks any deployment claim.

Required fields:

- claim ID
- claim text
- claim status
- supporting evidence
- missing evidence
- linked hazards

### Evidence

Evidence is an artifact used to support or weaken a claim.

Evidence types:

- target trial specification
- evidence report
- dashboard or interface output
- audit log
- monitoring report
- incident table
- evaluation registry row
- governance decision
- citation ID

Evidence should be traceable through explicit identifiers.

### Hazard

A hazard is a way the synthetic system could mislead a user or
fail as a lifecycle artifact.

Required fields:

- hazard ID
- hazard description
- trigger or source
- linked incident
- mitigation
- residual risk

Examples:

- dataset shift
- calibration drift
- alert burden growth
- proxy-label bias
- negative-control warning
- missing local validation
- ambiguous workflow action

### Incident

An incident is a generated failure signal or review-triggering
event.

Required fields:

- incident ID
- severity
- trigger metric
- observed value
- threshold
- suspected root cause
- required review
- owner
- decision
- follow-up date

The default flagship case should always generate at least one
incident. A safety case without a failure signal is not useful
for this project.

### Governance decision

A governance decision records what the owner does with the
evidence and incidents.

Allowed decisions:

- `continue`
- `monitor`
- `pause`
- `update`
- `rollback`

The decision must reference incident IDs and evaluation IDs. The
default flagship case should not authorize deployment.

### Evaluation registry

The evaluation registry is the traceability table for all checks
performed in the case.

Required columns:

- prototype
- artifact
- evaluation_id
- stage
- data_version
- metric_or_check
- result
- decision
- status
- owner
- citation_ids
- notes

Citation IDs must resolve to `references/evidence-matrix.csv`.

## Generated report structure

The safety-case report should contain:

- safety boundary
- deployment-readiness conclusion
- case summary
- claims reviewed
- supporting evidence
- missing evidence
- known hazards
- generated incidents
- governance decision
- open assumptions
- next required review
- citation IDs

## Readiness logic

The default readiness conclusion should be conservative.

Deployment should be blocked when any of these are present:

- unresolved high-severity incident
- missing local validation
- calibration drift above threshold
- dataset shift above threshold
- proxy-label bias warning
- ambiguous interface action
- missing governance owner

For this repository, blocked or paused conclusions are expected
and useful. The point is to show lifecycle reasoning, not to
make deployment look easy.

## Evidence references

Primary citation IDs: E001, E002, E003, E005, E006, E007, E009,
E010, E019, E020, E027.
