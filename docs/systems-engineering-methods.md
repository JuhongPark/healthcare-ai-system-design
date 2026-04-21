# Systems engineering methods

Notes on formal systems-engineering methods applied to
healthcare AI: Design Structure Matrix for dependency
analysis, system dynamics for feedback loops, axiomatic
design for requirement-parameter mapping, stakeholder
value analysis for architecture decisions, and
Object-Process Methodology for model-based description.

## Why formal methods

Healthcare AI systems are complex: many components, many
stakeholders, feedback between design decisions and
operational outcomes. Informal reasoning scales poorly.
Formal methods trade notation overhead for precision.
Each method below has a narrow scope; using several
together is more informative than committing to one.

## Design Structure Matrix

A Design Structure Matrix (DSM) is an NxN square matrix
whose rows and columns are system elements and whose
off-diagonal entries mark a dependency from row to
column. Eppinger and Browning (2012) collect the
methodology and applications.

For a hospital clinical AI deployment, a component DSM
might include:

- Source systems (EHR, lab, pharmacy)
- Ingestion and ETL
- Feature store
- Training pipeline
- Model registry
- Serving runtime
- Monitoring
- Clinician interface
- Governance workflow
- Audit log

Dependencies are marked where a change in one component
requires coordinated change in another. Clusters on the
diagonal reveal modules; marks far from the diagonal
reveal long-range couplings that are design risks.

Organizational DSMs apply the same method to teams or
roles, exposing where responsibility and communication
patterns diverge.

### Open questions

- Which long-range couplings appear most often in
  hospital AI DSMs?
- How are DSMs kept current as systems evolve, or are
  they single-use artifacts?
- Does matching a component DSM against an
  organizational DSM expose coordination failures?

## System dynamics

System dynamics (Sterman, 2000) models feedback loops,
delays, and accumulations. Several feedback loops in
healthcare AI warrant explicit modeling:

- **Trust loop.** Clinician trust → usage → more
  performance data → calibration evidence → trust. A
  reinforcing loop that can also run in reverse after an
  incident.
- **Alert fatigue loop.** Alert frequency → dismissal
  rate → missed alerts → threshold adjustment →
  frequency. A balancing loop with a delay that can
  oscillate.
- **Drift loop.** Model outputs → clinician actions →
  patient trajectories → future training data →
  retrained model → outputs. A reinforcing loop that can
  entrench model errors.
- **Update loop.** New evidence → update proposal →
  validation → release → monitoring → next update.
  Sequencing determines whether updates help or
  destabilize.

Simulating these loops, even qualitatively with causal
loop diagrams, exposes failure modes that static analyses
miss.

### Open questions

- Which feedback loops in hospital AI deployments have
  been empirically measured, and which are conjectured?
- How are model-output feedbacks on training data
  neutralized for evaluation?

## Axiomatic design

Axiomatic design (Suh, 2001) maps functional
requirements (FRs) to design parameters (DPs). The
Independence Axiom holds if each DP affects only one FR;
coupling indicates that design choices entangle
requirements.

For a clinical AI system, candidate FRs include:

- Produce a score at the right time in the workflow.
- Communicate uncertainty.
- Keep patient data within a trust boundary.
- Make the system auditable.
- Allow the user to override.

Candidate DPs include:

- Serving topology (on-prem, hybrid, edge, federated).
- Output schema (point estimate, interval, categorical).
- Access control and audit implementation.
- Interface affordances for override.

A coupling analysis reveals where a single DP change
affects multiple FRs — a design weakness. Many coupled
choices are defensible (platform constraints, legacy
integrations) but should be explicit.

## Stakeholder value analysis

Crawley, Cameron, and Selva (2015) frame architecture as
the allocation of function to form under stakeholder
value constraints. For healthcare AI:

- List stakeholders (see `docs/ai-organizational-design.md`).
- Identify value flows: what each stakeholder provides to
  and expects from the system.
- Identify misalignments: where the system asks for input
  without returning value, or returns value without
  responsibility.
- Use the map to test architectural choices against
  stakeholder value, not only against technical metrics.

Stakeholder value is uneven. A design that maximizes
administrator value while degrading clinician value tends
to fail in deployment. A design that returns value to
patients primarily through improved aggregate outcomes
still needs to avoid imposing individual harm.

## Object-Process Methodology

Object-Process Methodology (OPM; Dori, 2016) is a
model-based systems engineering language that represents
objects and processes together. For a clinical AI
system, an OPM diagram captures:

- The clinical encounter as a process
- Patient data as an object with states (captured,
  transformed, stored, used)
- The model as a process with inputs, outputs, and
  governance states
- The clinician as an enabling agent

OPM is heavier than informal block diagrams and lighter
than SysML. It is most useful when the system needs to
be reviewed by stakeholders with mixed backgrounds.

## Integration and sequencing

No single method is sufficient. A typical sequencing:

- Start with stakeholder value to fix what the system is
  for and for whom.
- Use axiomatic design to articulate functional
  requirements and decide on the top-level decomposition.
- Use DSM to expose coupling within the chosen
  decomposition and to guide team structure.
- Use system dynamics to reason about feedback loops and
  operational behavior.
- Use OPM (or block diagrams) to communicate the system
  across disciplines.

The overhead of any formal method has to be paid for by
the decisions it changes. A method whose use does not
change a decision is not worth its notation cost.

## Open questions

- Which methods most often change architectural
  decisions in healthcare AI in practice?
- How do these methods combine with MLOps-style
  engineering practice?
- Are there healthcare AI DSMs or OPM models published as
  worked examples?

## Applied reading across the repository

The methods above are used, sometimes implicitly,
across other notes:

- `docs/pharma-ai-system-of-systems.md` carries a
  cross-stage DSM sketch and a naming of emergent
  behavior patterns.
- `docs/human-ai-interaction-patterns.md` develops
  the trust-loop and alert-fatigue feedback loops
  into interaction design patterns.
- `docs/ai-organizational-design.md` and
  `docs/ai-portfolio-and-strategy.md` enact
  stakeholder-value analysis at the organization and
  portfolio level.
- `docs/interface-contracts-for-healthcare-ai.md`
  makes axiomatic-design coupling concrete for the
  interface layer.

## Limitations and cautions

- Formal methods do not make decisions. They structure
  reasoning; decisions still require judgment.
- Notation cost is real. A large OPM or DSM that nobody
  reads is worse than a short diagram that the team uses.
- The methods originate in other domains; adaptation is
  required.
