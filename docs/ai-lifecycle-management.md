# AI lifecycle management

A systems-engineering view of the clinical ML lifecycle,
from problem definition through retirement, with stage
gates and MLOps practices adapted to the healthcare
context.

## Why lifecycle

A model is not an artifact with a single shipment date. It
is a capability with a multi-year operational profile: it
is trained, validated, deployed, monitored, updated, and
eventually retired. Treating each step as a separate
project hides the dependencies between them. A lifecycle
view makes the dependencies explicit and assigns
ownership.

## V-model adapted to clinical ML

A V-model maps design on the left arm to verification and
validation on the right arm. Adapted to clinical ML:

- **Concept → clinical problem definition.** Identify the
  decision the system supports, the user, the setting.
- **Requirements → clinical, regulatory, data, and
  operational requirements.** Articulate what the system
  must do, under what constraints.
- **Architecture → planes, interfaces, and topology.**
  Allocate the requirements to components.
- **Design → model, pipeline, serving, monitoring.** Fix
  the detailed design of each plane.
- **Implementation → code, infrastructure, documentation.**
- **Unit verification → component tests against spec.**
- **Integration verification → end-to-end tests across
  planes.**
- **Local validation → performance and calibration on
  local data.**
- **Clinical validation → workflow-embedded evaluation.**
- **Operational acceptance → monitoring and incident
  response proven.**

The right arm is not an audit after the fact. Each
validation activity is paired with a design activity on
the left arm and has exit criteria stated up front.

## Stage gates

A gate structure makes the transitions explicit. A gate
is not a formality; it is a go/no-go decision with a
named owner and documented criteria.

- **Gate 0 — Problem signed off.** Decision supported,
  user, setting, baseline and success criteria defined.
- **Gate 1 — Data access secured.** Access and consent
  (where applicable) resolved; data dictionary exists.
- **Gate 2 — Baseline established.** Non-ML baseline
  quantified; any new model must beat it for a specified
  reason.
- **Gate 3 — Internal validation passed.** Discrimination,
  calibration, and subgroup performance meet pre-stated
  thresholds.
- **Gate 4 — External or local validation passed.**
  Performance holds on data the model did not see during
  development.
- **Gate 5 — Shadow deployment completed.** Model runs
  alongside production without affecting decisions; outputs
  compared to historical ground truth.
- **Gate 6 — Go-live approved by governance.** Model
  facts label, monitoring plan, incident response plan,
  and retirement criteria signed off.
- **Gate 7 — Operational stability demonstrated.**
  Monitoring thresholds met for a specified period; no
  unresolved incidents above severity threshold.
- **Gate 8 — Update approved.** New model version evaluated
  against current and passes predetermined change control
  plan.
- **Gate 9 — Retirement executed.** Model taken out of
  service; successor identified or the use is
  discontinued; archival and documentation closed.

Gates 7 through 9 recur over the operational life of the
system.

## MLOps for clinical settings

MLOps practices adapted to clinical constraints:

- **Pipelines as code.** Training, evaluation, and serving
  pipelines are versioned, reviewable, and reproducible.
- **Model registry.** Each model version carries its
  evaluation report, training data snapshot reference,
  feature versions, and approval state.
- **Feature versioning.** Feature definitions change; the
  registry records which feature version a model depends
  on.
- **Shadow deployment.** New versions run alongside
  production for a defined period, with comparison
  dashboards.
- **Canary release.** Limited fraction of traffic to a
  new version, with automated rollback criteria.
- **Rollback mechanism.** Return to the previous model
  version without coordinated release, within a bounded
  time.
- **Post-release monitoring.** Metrics defined at Gate 6
  are the contract for operational stability; breaches
  trigger the incident response process.

## Update governance

Updates are the lifecycle step that most often goes wrong:
an update is shipped because it is better on average and
silently worse on a subgroup that matters. Update
governance should require:

- **Comparison to the incumbent** on the same evaluation
  slices used at Gates 3-4.
- **Subgroup breakdown** with pre-stated thresholds.
- **Shift check** — recent production data is part of the
  evaluation; training-time data alone is insufficient.
- **Predetermined change control plan conformance.**

## Retirement

A system without a retirement pathway accumulates in
production. Retirement criteria should be written at
Gate 6:

- Clinical indication changes.
- Data source becomes unavailable.
- Subgroup performance falls below threshold and cannot be
  restored within an agreed time.
- Successor model supersedes the current.
- Clinical environment change makes the use case obsolete.

Retirement is an operational event with its own owner and
its own postmortem.

## Open questions

- What is the smallest useful lifecycle governance for a
  single-site deployment?
- How does the V-model adapt when the vendor owns several
  lifecycle steps?
- How are stage-gate artifacts shared across deployments of
  the same model at different sites?
- How does the lifecycle change when the model is itself a
  continual learner?

## Limitations and cautions

- The V-model presentation is a management framing, not a
  project plan. Real work is iterative, and most gates
  are revisited.
- Stage gates are a coordination device; they do not
  substitute for the technical work inside each stage.
- Retirement criteria are easy to write and hard to
  enforce. Enforcement is an organizational problem.
