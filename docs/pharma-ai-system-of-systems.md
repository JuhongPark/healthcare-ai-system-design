# Pharma AI as a system of systems

A cross-stage view of AI across pharma R&D — discovery,
preclinical, clinical development, manufacturing, and
post-marketing — as a system of systems with emergent
behavior, cross-stage handoffs, and DSM-style
dependency structure.

## Why system of systems

A single model, a single platform, and a single program
are each legitimate units of analysis. None of them
captures the behavior that emerges when a discovery
model's output becomes a preclinical hypothesis, feeds
first-in-human dosing assumptions, shapes trial
eligibility, and surfaces as a post-marketing signal
whose investigation changes the next generation of
discovery. System-of-systems (SoS) framing (Maier, 1998;
INCOSE SE Handbook) is the discipline that treats these
cross-stage interactions as the subject.

Characteristic SoS properties that apply here:

- **Operational independence.** Each constituent
  system (a discovery AI platform, a CMC AI system, a
  trial operations AI) has useful function on its own.
- **Managerial independence.** Each is owned by a
  distinct group, often with distinct budgets,
  timelines, and KPIs.
- **Evolutionary development.** The SoS is not
  designed; it is assembled over time by independent
  decisions in the constituents.
- **Emergent behavior.** The SoS behaves in ways none
  of the constituents would on its own.
- **Geographic distribution.** Constituents sit in
  different sites, organizations, and regulatory
  jurisdictions.

Pharma R&D AI hits all five, which makes SoS framing
rather than platform framing the right level at which
to reason about integration.

## Constituent systems

The constituents this note focuses on:

- **Discovery AI system** (see
  `docs/pharma-ai-systems-architecture.md`). Target
  identification, generative chemistry, property and
  structure prediction, active learning loops.
- **Preclinical-safety AI system** (see
  `docs/admet-and-preclinical-safety.md`). ADMET and
  toxicity prediction, physics-grounded models, assay
  feedback loops.
- **Clinical pharmacology AI system** (see
  `docs/clinical-pharmacology-and-midd.md`). Population
  PK, PBPK, exposure-response, QSP, digital endpoints.
- **Clinical trials AI system** (see
  `docs/ai-for-clinical-trials.md`). Recruitment, site
  selection, external comparators, adaptive designs,
  digital endpoints.
- **CMC and manufacturing AI system.** Process
  analytical technology, in-process control,
  stability prediction, continuous manufacturing
  monitoring; out of scope for deep coverage in this
  repository, but part of the SoS.
- **Pharmacovigilance and pharmacoepidemiology AI
  system** (see `docs/pharmacoepidemiology-methods.md`
  and the pharmacovigilance section of
  `docs/drug-design.md`). Signal detection, distributed
  surveillance, real-world evidence generation.

Each constituent has its own architecture, lifecycle,
and governance (covered in the dedicated notes). The SoS
view is about what happens when they share data,
hypotheses, or decision contexts.

## Cross-stage handoffs

Handoffs between constituents are the design surface of
the SoS.

- **Target → discovery chemistry.** Target hypotheses
  feed generative and property models; uncertainty in
  target tractability should propagate into design-
  stage priors.
- **Chemistry → preclinical safety.** Lead compounds
  feed ADMET and toxicity models; applicability-domain
  information has to survive the handoff so the
  preclinical team can interpret it.
- **Preclinical → first-in-human.** ADMET profile
  feeds allometric scaling or PBPK for starting-dose
  projection; assumptions registered at the
  preclinical handoff are the same assumptions that
  govern the clinical-pharmacology analysis.
- **Clinical pharmacology → trial design.** E-R
  modeling feeds dose selection and stratification;
  the populations characterized in popPK shape
  eligibility.
- **Trial → post-marketing.** Trial-population
  characteristics anchor the generalization claims
  that observational post-marketing evidence has to
  support or contest.
- **Post-marketing → next-generation discovery.**
  Pharmacovigilance signals surface mechanisms and
  populations that feed back into target nomination
  and trial design for successors.

Each handoff is a contract crossing (see
`docs/interface-contracts-for-healthcare-ai.md`) and
an evidence transfer whose integrity is the load-bearing
question.

## Cross-stage DSM

A Design Structure Matrix across constituents exposes
where dependencies are concentrated and where long-range
couplings create risk. An illustrative sketch (systems
on both axes, dependency where row depends on column):

| | Disc | Preclin | ClinPharm | Trials | CMC | PV |
|---|---|---|---|---|---|---|
| Discovery | X | — | — | — | — | small |
| Preclinical safety | strong | X | — | — | — | small |
| Clinical pharmacology | small | strong | X | — | — | medium |
| Trials | small | small | strong | X | small | small |
| CMC | medium | small | — | medium | X | — |
| Pharmacovigilance | medium | small | medium | medium | — | X |

The pattern worth noticing is that pharmacovigilance
depends on many earlier constituents but is depended on
by few — it receives upstream choices as assumptions it
inherits. The structural implication is that
post-marketing problems are often upstream problems
that surface late.

## Emergent behavior

Patterns that emerge from the cross-stage interactions
and not from any constituent alone:

- **Selection-driven training data.** Candidates that
  fail at preclinical safety or in trials never
  contribute outcome data at later stages; discovery
  models trained on advanced-compound data reflect
  the selection pressure rather than biology.
- **Confounded post-market evidence.** Populations
  selected by trial eligibility inform prescribing;
  observational post-marketing evidence reflects that
  prescribing pattern rather than the underlying
  effect; feedback into repositioning models inherits
  that confounding.
- **Discovery-trial divergence.** A chemotype optimized
  against a biomarker assay carries assay-specific
  biases into trial-endpoint measurement, sometimes
  invisibly.
- **Shared-assumption chains.** A PBPK assumption
  adopted at preclinical dosing follows the compound
  through first-in-human, Phase 2, and label; a late-
  stage finding that contradicts it forces rework
  across the chain.

Naming these patterns is the prerequisite to noticing
them in a specific program.

## Architectural responses

SoS integration does not happen by exhortation. Specific
architectural responses the SoS framing suggests:

- **Evidence registry at the SoS level.** A shared
  registry of AI-supported evidence across stages,
  searchable by compound, target, and program, with
  stage-of-origin and confidence metadata. Each stage
  writes, later stages read.
- **Cross-stage versioning policy.** Interface
  contracts between constituents are versioned under a
  shared policy so cross-stage comparisons remain
  valid.
- **Shared applicability-domain vocabulary.** The same
  compound is in the applicability domain of a
  property model and out of domain for an ADMET model;
  the SoS needs a shared way to state and query this.
- **Federated observability.** Monitoring dashboards
  that join across constituents (e.g. preclinical
  predictions vs. clinical PK readouts for the same
  series) need cross-stage join keys that were not
  designed in.
- **SoS governance forum.** A small standing forum
  that reviews cross-stage incidents and drift,
  distinct from constituent-level governance.

## Organizational design implications

SoS integration is as much an organizational problem as
a technical one (see `docs/ai-organizational-design.md`):

- **Boundary-spanning roles.** People whose role is to
  translate between constituents (medicinal chemist
  liaison to clin pharm; pharmacometrician liaison to
  discovery) rather than sitting fully inside one
  constituent.
- **Shared tooling investment.** A cross-stage
  evidence registry is a platform capability, not a
  program deliverable.
- **Incentive alignment.** Constituent KPIs that
  measure hand-off quality, not only constituent
  outcome.
- **Postmortem crossing.** When a program fails at a
  downstream gate, the postmortem includes the
  upstream constituents whose assumptions were
  involved.

## Connection to other notes

- Architecture: `docs/ai-systems-architecture.md`,
  `docs/pharma-ai-systems-architecture.md`.
- Lifecycle: `docs/ai-lifecycle-management.md`,
  `docs/pharma-ai-lifecycle-management.md`.
- Discovery program:
  `docs/drug-discovery-program-architecture.md`.
- Constituent-specific notes listed above.
- Methods: `docs/systems-engineering-methods.md`
  (DSM, system dynamics) specialized with pharma
  examples.

## Open questions

- Which SoS integration patterns have working
  examples published in the pharma literature, and
  which remain aspirational?
- How is a cross-stage evidence registry scoped so
  that it is useful without becoming a duplicate of
  every constituent's own record?
- How are incentives set so that constituent teams
  prioritize handoff quality alongside constituent
  outcome?
- How does an SoS governance forum avoid becoming a
  layer of review that slows constituents without
  changing decisions?
- Where does the CMC and manufacturing constituent
  belong in the decomposition, and what does its
  interface to discovery and clinical look like?

## Limitations and cautions

- SoS framing is valuable when cross-stage integration
  is the bottleneck. If a single constituent is the
  bottleneck, SoS work is displacement activity.
- DSM sketches like the one above are illustrative;
  real organizational DSMs are larger and messier.
- Emergent behavior is easier to name in retrospect
  than to predict prospectively. The note is a
  vocabulary for noticing, not a forecasting tool.
- The CMC and manufacturing AI constituent is
  referenced here but not developed in the repository;
  it is a candidate for future expansion.
