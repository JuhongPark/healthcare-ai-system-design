# AI systems architecture

A reference architecture for clinical AI systems, viewed as
engineered artifacts with identifiable components,
interfaces, and owners. The unit of analysis is the system,
not the model.

## Why architecture

A model without a surrounding architecture is not deployable.
A deployed model without an explicit architecture is
deployable but not maintainable. Architecture captures the
decomposition, interfaces, and design decisions that let a
system be operated, evaluated, and changed over time by
people other than the original authors.

## Reference architecture: five planes

A clinical AI system decomposes into five planes. Each plane
has its own components, its own interfaces, and its own
operating owner. The planes are coupled through well-defined
contracts, not through direct dependencies.

### Data plane

- **Ingestion.** Interfaces to source systems (EHR via HL7
  v2 or FHIR, lab systems, imaging archives, device feeds).
- **Identity and consent.** Patient identity resolution,
  consent state, purpose-of-use tags.
- **Transformation.** Schema mapping to an internal model
  (for example, OMOP CDM), feature computation, batch vs.
  streaming semantics.
- **Feature store.** Versioned, materialized features with
  point-in-time correctness guarantees.
- **Lineage.** Record of how each feature was derived and
  from which source tables.

### Model plane

- **Experiment tracking.** Runs, hyperparameters, datasets,
  metrics.
- **Training orchestration.** Pipelines as code, artifact
  capture, reproducibility metadata.
- **Model registry.** Versioned, signed model artifacts with
  evaluation reports.
- **Evaluation harness.** Standard evaluation slices
  including subgroup, temporal, and shift evaluation.

### Serving plane

- **Inference runtime.** Latency and availability targets,
  autoscaling, warm models.
- **Routing.** Traffic splitting for A/B, shadow, and canary
  deployments.
- **Caching.** Feature and prediction caching with
  invalidation rules.
- **Output contract.** Score, uncertainty, model version,
  feature versions, timestamp.

### Monitoring plane

- **Input monitoring.** Distribution drift on inputs and
  features.
- **Output monitoring.** Drift in the prediction
  distribution; calibration vs. observed outcomes where
  ground truth is available.
- **Outcome tracking.** Downstream event capture (admission,
  readmission, mortality, operational action) with lag.
- **Alerting.** Thresholds and escalation paths; signal
  routing to model owner and operations.

### Governance plane

- **Approval workflow.** Intake, review, approval, and
  retirement for each model version.
- **Change control.** Predetermined change control plans
  aligned with regulatory expectations.
- **Audit log.** Immutable record of decisions, access, and
  overrides.
- **Access policy.** Role-based access control across data,
  model, serving, and governance planes.

## Interface contracts

Interfaces between planes are the design parameters that
most affect maintainability. Candidates for explicit
contracts:

- **Feature contract.** Feature name, type, source, valid
  range, freshness, default behavior on missingness.
- **Prediction contract.** Output schema, confidence
  semantics, model and feature version, fallback when
  unavailable.
- **Event contract.** Outcome event definition, latency,
  deduplication rule.
- **Audit contract.** What is logged for each serve, who
  can read it, retention.

A change to a contract is a change to the system. Changes
to contracts go through the governance plane; changes
within a plane do not need to.

## Deployment topologies

- **On-premise monolithic.** All five planes at the
  hospital, single tenant. High control, high operational
  burden.
- **Hybrid.** Training on cloud or vendor, serving on
  hospital infrastructure. Data crosses a boundary that
  needs explicit contracts.
- **Edge.** Inference runs on point-of-care devices (for
  example, imaging modalities) with offline capability.
- **Federated.** Training coordinates across sites without
  moving raw data; serving is per-site.

Each topology fixes different system properties: latency,
availability, data locality, regulatory surface, and cost
of change.

## System properties

The same architecture can be tuned to very different
operating points. Relevant design parameters:

- **Latency budget.** End-to-end time from source event to
  clinician-visible score.
- **Availability target.** Expected uptime; degraded-mode
  behavior when the serving plane is down.
- **Consistency.** Whether downstream systems must see the
  same model version and feature snapshot at the same time.
- **Privacy boundary.** Where patient-identifiable data
  crosses a trust boundary, and how that crossing is
  gated.
- **Change cadence.** Allowed frequency of model updates
  given validation and governance overhead.

## Open questions

- Which interface contracts break most often in practice,
  and what does a standard contract look like at a hospital
  site?
- What does an architecture description language useful at
  a hospital look like — light enough to maintain, formal
  enough to review?
- How are cross-plane responsibilities assigned when the
  vendor owns some planes and the hospital owns others?
- How does the reference architecture differ for a drug
  discovery program compared to a clinical deployment, and
  what maps cleanly between them?

## Limitations and cautions

- A reference architecture is a starting template, not a
  prescription. Real systems diverge based on context.
- The five-plane decomposition is one useful partitioning;
  others are defensible.
- Architecture documents go stale quickly. The architecture
  is what the system actually does, not what the document
  says.
