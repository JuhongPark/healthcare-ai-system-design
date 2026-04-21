# AI risk and reliability

Notes on risk management and reliability engineering for
clinical AI systems — failure modes, service level
objectives, incident response, and the technical debt that
accumulates when these are not designed in.

## Why risk and reliability

A deployed clinical AI system is a production service, not
a research artifact. It has availability, latency, and
correctness requirements, and it fails in ways that a
research evaluation did not measure. Risk and reliability
engineering import tools from software and hardware
engineering and adapt them to the specifics of clinical
ML: data drift, silent degradation, subgroup failure.

## Failure modes and effects analysis

FMEA is a structured walkthrough of potential failures. For
a clinical AI system, relevant failure categories include:

- **Data pipeline failures.** A source feed stops; a field
  changes meaning; a join condition silently excludes
  rows; a time zone bug shifts timestamps.
- **Label or outcome changes.** A coding practice change
  redefines the outcome; a ground-truth system changes
  interpretation criteria.
- **Feature staleness.** A feature definition changes
  upstream without the feature store being invalidated.
- **Model degradation — covariate shift.** Input
  distribution moves; calibration and possibly
  discrimination drop.
- **Model degradation — label shift.** The base rate of
  the outcome changes; predictions stay the same.
- **Subgroup failure.** Aggregate metrics remain healthy;
  subgroup metrics degrade.
- **Serving failure.** Latency breaches SLO; inference
  service returns errors; a caching bug returns stale
  predictions.
- **Integration failure.** The clinician interface shows
  a stale score; the routing layer sends traffic to a
  wrong version.
- **Governance failure.** A change ships without the
  predetermined change control plan being exercised.
- **Incident response failure.** A known severity trigger
  fires and no one is paged.

For each mode, an FMEA table records severity, likelihood,
detectability (before effect), and the mitigation in
place. The useful output is the prioritized list of
modes with insufficient detectability.

## Service level objectives

SLOs translate reliability goals into measurable
commitments. Candidate SLOs and SLIs for a clinical AI
serving system:

- **Availability.** Fraction of inference requests served
  successfully within the latency budget.
- **Latency.** p50, p95, p99 end-to-end latency from input
  event to score available to the clinician.
- **Freshness.** Time from source event to feature
  available for scoring.
- **Prediction quality band.** Rolling-window calibration
  and discrimination within pre-stated bands.
- **Monitoring latency.** Time between a performance
  breach occurring and the alert reaching a human.
- **Incident response SLO.** Time to acknowledge and time
  to mitigate for each severity class.

SLO targets are policy choices, not technical ones. They
are negotiated with the clinical champion and the
governance committee; they are revisited as the service
matures.

## Incident response

An incident is a deviation from SLO or a safety event.
Recommended practices imported from site reliability
engineering:

- **Severity levels.** Defined and documented. Severity 1
  stops or restricts the service; lower severities allow
  continued operation with mitigation.
- **On-call rotation.** Named people on each of operations
  and clinical sides, not shared mailboxes.
- **Runbooks.** For each detected signal, a checklist of
  triage and mitigation steps; the runbook is kept with
  the code, not in a separate binder.
- **Blameless postmortems.** After any severity 2 or
  above, a written postmortem with timeline, contributing
  factors, and tracked actions.
- **Postmortem review.** Actions tracked to closure in the
  governance forum.

The goal is not to prevent all incidents; it is to make
them visible and to learn from them.

## Technical debt

Sculley and colleagues (2015) catalog technical debt
specific to ML systems. A hospital deployment accumulates
characteristic debt:

- **Pipeline jungles.** Ad-hoc glue code between source
  systems and features that grows un-reviewed.
- **Configuration debt.** Model hyperparameters,
  thresholds, and routing rules spread across files
  without a single source of truth.
- **Entanglement.** Small changes in one model affect
  downstream systems in hard-to-trace ways.
- **Correction cascades.** Fixing one model's bug
  requires retraining downstream models.
- **Abandoned experiments.** Branches of code retained
  for historical reasons that should have been cleaned
  up.
- **Undeclared consumers.** Downstream teams reading
  model outputs without the model owner knowing.

Debt is paid by refactoring, testing investments, and by
retirement of obsolete systems. It is rarely paid down
under schedule pressure; the governance forum is one
place to allocate the time.

## Risk register

A risk register for a clinical AI program distinguishes:

- **Technical risks.** Failure modes from the FMEA.
- **Clinical risks.** Risks to patients from an incorrect
  score, a missed alert, or an alert-fatigue-induced
  dismissal.
- **Operational risks.** Vendor failure, infrastructure
  outage, staffing loss.
- **Regulatory and legal risks.** Non-conformance with
  applicable guidance or contractual commitments.
- **Reputational risks.** Public incidents with
  institutional consequences.

Each entry has an owner, a mitigation, and a review date.

## Open questions

- Which SLOs are most informative for clinical AI
  services, given the delay between score and outcome?
- What does a blameless postmortem look like when the
  failure crosses vendor and hospital boundaries?
- How is clinical risk — a score that influences a bad
  outcome — separated from operational risk in incident
  taxonomy?
- Which debts in clinical ML pay down fastest, and which
  compound?

## Limitations and cautions

- FMEA exercises are only as good as the failure-mode
  imagination that goes into them.
- SLO frameworks imported from general site reliability
  engineering need adaptation to the slow-feedback nature
  of clinical outcomes.
- A risk register can become paperwork; the discipline is
  in reviewing it, not in filling it in.
