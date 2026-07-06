# Project thesis

This repository studies healthcare AI as a lifecycle evidence
system. The core question is not whether a model can produce a
score. The core question is whether the surrounding system can
show what evidence exists, what evidence is missing, what could
fail, who owns the decision, and why deployment is or is not
justified.

## Thesis

Healthcare AI safety is a lifecycle evidence problem, not only a
model performance problem.

A clinically framed AI artifact is incomplete until it connects:

- data provenance and fitness
- intended use and non-use boundaries
- evaluation stage and metric limits
- workflow interface and human control
- monitoring signals and incident response
- governance decisions and accountable ownership

The repository therefore treats the model as one system
component. The safety case is the stronger unit of analysis.

## What the project demonstrates

The project should demonstrate an executable synthetic
healthcare AI safety case. A reader should be able to regenerate
a small case study and inspect how evidence design, workflow
display, monitoring, incidents, and governance decisions connect
through shared identifiers.

The default case should be failure-first. It should not try to
prove that a synthetic AI system is ready for deployment. It
should show why the system is not ready, which failure signals
were detected, and which review decision follows.

## What the project does not claim

The repository does not contain clinical tools, medical advice,
protected health information, private patient data, or validated
clinical decision support. Prototypes and case studies use
synthetic, simulated, or public data only.

No output in this repository supports treatment decisions,
diagnosis, triage, comparative effectiveness claims, model
safety claims, or deployment authorization for real patients or
real populations.

## Design stance

### Failure is a first-class output

Successful execution is not enough. A useful healthcare AI
safety case should surface unresolved causal assumptions,
calibration drift, dataset shift, alert burden, proxy-label
risk, and missing governance evidence.

### Traceability matters more than polish

Every important output should be traceable to a case identifier,
artifact identifier, incident identifier, evaluation identifier,
or citation identifier. Traceability is the mechanism that turns
scattered documentation into a system.

### Governance is executable

Governance should not appear only as a static checklist. The
flagship case should generate incidents, evaluation registry
entries, a governance decision, and a safety-case report from
one command.

### Synthetic safety boundaries are part of the design

The synthetic-only boundary is not a disclaimer added later. It
is a design constraint. The point is to make lifecycle logic
visible without implying clinical validity.

## Near-term project identity

Near term, the repository should be read as:

> An executable synthetic healthcare AI safety-case framework
> that connects evidence design, workflow display, monitoring,
> incident response, and governance decisions.

The existing RWE, CDS, and monitoring prototypes become component
sketches. The flagship synthetic care program becomes the center
of gravity.

## Evidence references

Primary citation IDs: E001, E002, E003, E005, E006, E007, E009,
E010, E019, E020, E027.
