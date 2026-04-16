# Healthcare AI deployment notes

Notes on why deploying AI in healthcare is a systems problem,
not a modeling problem.

## Workflow mismatch

A model that runs off a nightly batch cannot support a decision
that happens during a 15-minute visit. A model whose output
appears three screens away from where the decision is made will
not be used. Workflow mismatch is easy to identify after
deployment and hard to fix. It should be considered at design
time.

## Alert fatigue

Every alert competes for attention with every other alert a
clinician has already seen today. A model that is correct 80%
of the time but fires ten times a shift can be worse than no
model at all, because it teaches users to ignore its class of
output. Decision thresholds and presentation choices matter at
least as much as model accuracy.

## Unclear accountability

When a model influences a decision that leads to a bad outcome,
responsibility is distributed across the developer, the
deploying organization, the local validator, and the clinician
who acted. If that chain is not clear before deployment, it
will be argued over after. Accountability is a design input.

## Uncertainty communication

Point estimates hide disagreement. A 0.27 risk score looks
precise but may come from a model that is poorly calibrated on
the user's subgroup. Clinical users are not statisticians, but
they are also not helpless with uncertainty — they reason about
it every day in other forms. Uncertainty should be communicated,
not hidden behind a rounded number.

## Dataset shift

Healthcare data drifts. Coding practices change, guidelines
change, case mix changes, and software updates change what is
captured. A model trained on last year's data may be silently
off today. Dataset shift is not an edge case; it is the
steady-state behavior of a deployed system.

## Local validation

A model that performs well in the paper that introduced it may
not perform well at a given site. Local validation is the
evidence that matters for the local decision to deploy. It is
also the evidence that is hardest to gather, because the site
typically does not have the resources of the original
development team.

## Post-deployment monitoring

Monitoring is the answer to "how do you know it is still
working?" The smallest useful answer is: track the input
distribution, the output distribution, the outcome rate, and
calibration over time, and set thresholds that trigger a human
review. Anything less is wishful.

## Model updates

Models need to be updated, but updates are also risky: a new
version may be better on average and worse on the subgroup that
matters most. Update governance is the process that decides
when an update is acceptable, what evidence is required, and
who signs off.

## Governance processes

Governance here means the organizational machinery around the
model: intended use statements, known limitations, escalation
paths, audit logs, retirement criteria. These are not glamorous,
but they determine whether anyone can tell what a deployed
system is actually doing.

## Feedback loops

A system whose outputs influence the actions that generate the
next round of training data has a feedback loop. Feedback loops
can improve a system, but they can also stabilize its mistakes.
Prototypes should note whether a feedback loop is possible and
whether it has been considered.
