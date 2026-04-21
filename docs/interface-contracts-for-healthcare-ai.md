# Interface contracts for healthcare AI

A deep treatment of the interfaces between components of
healthcare and pharma AI systems — what they carry, how
they evolve, and how they fail. The reference
architectures in `docs/ai-systems-architecture.md` and
`docs/pharma-ai-systems-architecture.md` call out
contracts as first-class design artifacts; this note
develops them.

## Why contracts, not APIs

An API describes how a caller invokes a service. A
contract describes the mutual obligations between
producer and consumer of data, including semantics that
a wire format does not capture: units, freshness,
missingness behavior, and the definition of the
underlying event. A healthcare AI system fails most
often at the contract layer, not the API layer — a
feature whose definition changed upstream, a prediction
consumed with a stale model version, an outcome event
redefined by a coding practice change. Treating contracts
as artifacts that are reviewed and versioned makes these
failure modes addressable.

## Contract anatomy

Every contract includes:

- **Identity.** A stable name that survives refactoring.
- **Schema.** Fields, types, and cardinalities.
- **Semantics.** What each field means, in terms the
  producer and consumer both agree to.
- **Units and ontologies.** For every measurement, the
  unit; for every coded value, the code system and
  version.
- **Validity.** Value ranges, allowed enum values,
  nullability rules.
- **Freshness.** Maximum acceptable lag from the
  underlying event to availability.
- **Missingness behavior.** What the consumer should do
  when a field is absent.
- **Versioning policy.** How a change is announced, how
  compatibility is signaled, how deprecation is handled.
- **Ownership.** A single accountable party per
  contract.

A contract without all of these is underspecified and
will drift silently.

## Core contract types

### Feature contract

A feature is a computed input to a model. The contract
specifies:

- Feature name and logical definition.
- Source tables and columns, with their own contracts
  transitively.
- Aggregation window and point-in-time semantics.
- Valid range and expected distribution as monitoring
  input.
- Default behavior when source is missing.
- Refresh cadence and staleness budget.
- Version. A semantic change is a new version; the old
  version is either migrated or retired.

Feature stores enforce some of this at the schema level;
the semantic parts are policy, not code.

### Prediction contract

A prediction is the output of a model. The contract
specifies:

- Score and score type (probability, risk category,
  continuous value, ranked list, generated object).
- Uncertainty representation (interval, distribution,
  categorical confidence, epistemic vs. aleatoric where
  distinguished).
- Model identifier and version.
- Feature version set used to produce the prediction.
- Applicability-domain flag where the model defines
  one.
- Timestamp of prediction production.
- Intended-use statement, attached as metadata and
  enforced at the consumer.
- Fallback semantics when the model is unavailable.

A prediction stripped of version metadata is not a
prediction, it is a number.

### Event contract

An event is an observable fact about the world — a lab
result, an admission, an adverse-event report, an assay
readout. The contract specifies:

- Event name and definition.
- Source system and capture latency.
- Deduplication rule (some systems emit revisions).
- Corrections policy — does a correction replace the
  prior event, supersede with a new record, or emit
  under a different name?
- Ontology and coding version (ICD, SNOMED, LOINC,
  MedDRA, RxNorm; for pharma, ChEMBL target IDs,
  UniProt, MeSH).
- Time of event vs. time of capture vs. time of
  availability; any of these three can be the
  appropriate join key.

Event contracts are the most often broken by external
coding practice changes that look like data, not like
contract changes.

### Outcome contract

An outcome is the target a model is trying to predict or
an effect the system is trying to measure. The contract
specifies:

- Outcome definition (including inclusion and exclusion
  windows, censoring rules).
- Ascertainment method (ICD codes, chart review,
  claims adjudication, assay readout).
- Latency from true event to ascertainment, with
  distribution if variable.
- Handling of outcomes that arrive after a model has
  been scored.
- How the outcome definition is versioned as the
  clinical or scientific consensus changes.

Outcome drift is the most dangerous drift because the
numerator and denominator of every evaluation shift
together.

### Audit contract

An audit record says who did what, when, under what
authority, and what data flowed. The contract specifies:

- What is logged at each serve (input digest,
  prediction, user, purpose).
- Retention period and storage location.
- Access rules — who can read, under what authorization.
- Immutability — logs are append-only; retractions are
  new records, not deletions.
- Export format for external audits or regulatory
  review.

### Identity and consent contract

For clinical systems, each data crossing carries:

- Patient identifier and linkage rule.
- Consent state at time of capture.
- Purpose-of-use tag.
- Re-identification risk and aggregation policy.

For pharma discovery systems, the analogous contract is
around compound identity and IP:

- Compound identifier and canonical representation.
- Invention provenance and disclosure state.
- Access boundary by chemotype or program.
- External-partner disclosure rules.

## Schema evolution and versioning

Contracts change. Useful discipline:

- **Semantic versioning at the contract level.** Major
  for breaking changes, minor for additive changes,
  patch for bug fixes that preserve semantics.
- **Dual-publish during migration.** Both old and new
  schemas emitted in parallel for a defined window.
- **Deprecation schedule.** A stated date by which the
  old version is retired, communicated to all
  registered consumers.
- **Consumer registry.** The producer knows who reads
  the contract; undeclared consumers surface during
  deprecation and carry their own risk.
- **Backward-incompatible changes require governance.**
  A new major version goes through the change-control
  process in `docs/ai-lifecycle-management.md`.

## Contract testing

Contracts are enforced by tests, not by hope:

- **Producer tests.** The producer asserts that its
  output matches the declared schema, semantics, and
  value ranges on representative data.
- **Consumer tests.** The consumer asserts that its
  expectations match the contract, not the current
  behavior. A consumer that tests "what the producer
  currently emits" is coupled to the producer's
  implementation rather than to the contract.
- **Contract diffs.** Tooling detects when a producer
  emits values that drift outside the contract — new
  enum values, distribution shifts, freshness
  breaches.
- **Cross-contract invariants.** Joins across contracts
  often carry implicit assumptions about uniqueness,
  ordering, or time alignment; those assumptions are
  themselves contracts.

## Failure modes

Typical contract failures in deployed clinical and pharma
AI systems:

- **Silent semantics drift.** A field's meaning changes
  upstream without the contract version changing;
  downstream calculations are still "correct" on the
  new meaning and wrong on the old one.
- **Ontology version divergence.** Producer and
  consumer use different releases of a coding system;
  some codes exist in one and not the other.
- **Unit confusion.** mg/dL vs. mmol/L, nanomolar vs.
  micromolar, Fahrenheit vs. Celsius. Often discovered
  when a downstream model loses calibration.
- **Timestamp ambiguity.** Local time vs. UTC, time of
  event vs. time of capture; joins produce spurious
  lag.
- **Missingness interpretation.** Consumer treats null
  as absence; producer uses null to mean "not applicable."
- **Invalid joins.** A join on patient identifier
  succeeds when the identifier was reused; a join on
  compound identifier succeeds when stereoisomers were
  collapsed.
- **Orphan consumers.** A consumer reads a contract the
  producer did not know about; producer deprecates,
  consumer fails.
- **Shadow contracts.** Undocumented, implicit
  assumptions that only a senior team member knows
  about; they survive as long as that person does.

## Diagnostic practice

When a system misbehaves and the proximate cause is
unclear, a contract-first diagnostic often outperforms a
model-first one:

- Read the contract the misbehaving component expected.
- Read what the upstream is emitting today.
- Compare to what was emitted before the misbehavior.
- The delta between those three is the first place to
  look.

Prediction-layer debugging that ignores contract layers
usually circles.

## Healthcare-specific contract concerns

- **HL7 v2 vs. FHIR.** Two largely different contract
  styles; same field name can mean different things.
- **OMOP CDM.** A shared canonical contract for
  observational data; implementations diverge in ways
  that matter at join time.
- **SMART on FHIR.** Adds an app-launch contract on
  top of the FHIR data contract.
- **Code system versions.** ICD-9 → ICD-10 is the
  classic; SNOMED and LOINC also version.
- **Lab result mapping.** Local codes to LOINC is a
  contract that programs maintain, and its errors are
  long-lived.

## Pharma-specific contract concerns

- **Canonical compound form.** Decisions about tautomers,
  stereochemistry, counterions, and salt stripping are
  policy decisions that live in the contract.
- **Assay protocol version.** A protocol change is a
  contract change; data before and after cannot be
  pooled without explicit handling.
- **Structural confidence.** Experimental vs. predicted
  structures carry different confidence semantics; a
  contract that flattens them is an error source.
- **Biomedical knowledge graph release.** Node and edge
  identifiers change between releases; embeddings
  trained on one release do not map cleanly to another.
- **Partnership data boundaries.** External collaborators
  see specific slices; the contract is part of the
  collaboration agreement.

## Connection to other notes

- Reference architectures: `docs/ai-systems-architecture.md`
  and `docs/pharma-ai-systems-architecture.md`.
- Lifecycle and change control:
  `docs/ai-lifecycle-management.md`.
- Regulated MLOps: `docs/mlops-for-regulated-ai.md`.
- Multi-model orchestration:
  `docs/multi-model-orchestration-patterns.md`
  (contracts are how the models compose).
- Reliability: `docs/ai-risk-and-reliability.md`
  (contract breaches show up as FMEA entries).

## Open questions

- What is the smallest useful contract registry for a
  single-site hospital AI deployment?
- How should cross-organization contracts be governed
  when producer and consumer are in different
  regulatory regimes?
- When is a contract change better handled as a new
  contract (with phased migration) vs. as a version
  bump on the existing one?
- How are implicit contracts (shared assumptions)
  surfaced before they fail?

## Limitations and cautions

- Contract discipline has overhead. Premature contract
  formality on small teams is notation debt; late
  contract formality on large systems is incident debt.
- Contract tests are as fallible as the test data they
  run on. Representative fixtures matter as much as
  the test framework.
- Contract versioning cannot compensate for bad
  semantic choices made early; some contracts should
  be replaced, not versioned.
