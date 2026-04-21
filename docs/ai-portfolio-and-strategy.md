# AI portfolio and strategy

Notes on strategy and portfolio decisions for healthcare
AI at the organization level — not about which model to
build next, but about which capabilities to acquire, how
to sequence them, and how to manage them as a portfolio.

## Why portfolio

A single AI project is a project decision. A set of AI
projects at a hospital or pharma organization is a
portfolio decision: which capabilities to build once and
reuse, which to outsource, which to run in parallel, and
which to kill. Portfolio thinking is the difference
between a few pilots and a sustained AI capability.

## Capability maturity

A capability maturity model for AI in a healthcare
organization:

- **Level 0 — Ad hoc.** Projects start and stop without a
  common playbook. No shared data, model, or monitoring
  infrastructure.
- **Level 1 — Documented pilots.** Individual projects
  produce reusable documentation (data dictionaries,
  model facts, monitoring plans), but infrastructure
  remains per-project.
- **Level 2 — Repeatable deployments.** A shared
  deployment pathway exists; the stage gates in this
  repository apply consistently; governance is routine.
- **Level 3 — Managed portfolio.** Models run against
  shared data, serving, monitoring, and governance
  planes; cross-model incidents are detected; retirement
  is enforced.
- **Level 4 — Optimized.** Operational data drives
  decisions about which capabilities to invest in,
  expand, or retire; feedback loops are explicit and
  monitored.

Most healthcare organizations operate across several
levels at once. The question is not where the
organization is on the scale but which capability is at
which level.

## Build, buy, or partner

The build/buy/partner decision has to be made per
capability, not per system. A useful matrix has
capabilities on the rows and sourcing options on the
columns. Typical capabilities:

- Data integration and feature computation
- Model development and training
- Model serving and inference
- Monitoring and drift detection
- Governance and audit
- User interface and workflow integration

For each capability, the relevant design parameters are:

- **Differentiation.** Is this a source of competitive or
  clinical differentiation, or a commodity?
- **Time to capability.** How long to build internally
  vs. to buy or partner?
- **Switching cost.** How hard is it to change providers
  later?
- **Data exposure.** What does each option require in
  terms of data crossing a trust boundary?
- **Total cost of ownership.** Including long-term
  operations, not only acquisition.

## Real options under uncertainty

AI investments sit in a regime where uncertainty is high
and information arrives over time. Real options analysis
is one framing for this:

- **Option to defer.** Delay commitment until a key
  uncertainty is resolved (a regulatory decision, a
  competitive product, a technical benchmark).
- **Option to expand.** Make a small investment that
  preserves the right to scale if early evidence is
  favorable.
- **Option to abandon.** Staged commitment with explicit
  exit criteria. The cost of keeping this option is the
  option value.
- **Option to switch.** Design so that the system can
  switch providers, models, or topologies without rewriting
  the rest of the architecture.

Stage gates in the lifecycle are option exercise points.
Governance is the process by which options are evaluated
and exercised.

## Platform versus product

A platform is a capability that multiple products can
build on. A product is a single use-case deployment.
Platform-versus-product decisions at a healthcare
organization include:

- **Feature store.** Shared feature store across use
  cases or per-use-case features?
- **Model registry.** Organization-wide registry or
  per-team?
- **Monitoring infrastructure.** Shared vs. per-model
  monitoring?
- **Interface substrate.** For hospitals, SMART on FHIR
  as a platform choice for apps on EHR data.

Platforms have higher up-front cost and lower marginal
cost per added product. Products have the opposite
profile. A premature platform is a sunk cost; a missing
platform is recurring duplication.

## Vendor strategy and lock-in

Vendor decisions shape what the organization can do
later. Relevant considerations:

- **Data portability.** Can the organization take its
  data elsewhere? In what format, on what timeline?
- **Model portability.** Can a model trained with one
  vendor be served by another?
- **Interface openness.** Are interfaces standards-based
  (FHIR, OMOP) or proprietary?
- **Contractual exit terms.** What happens if the vendor
  changes pricing, changes strategy, or goes out of
  business?

## Sequencing

A portfolio is not a static set. Sequencing decisions:

- **Prerequisite capabilities.** A monitoring plane is a
  prerequisite for sustained deployment; standing up one
  model without a monitoring plane creates technical
  debt that blocks the next five.
- **Cross-project learning.** The second deployment
  should be faster than the first. If it is not,
  something in the pathway is not being documented.
- **Retirement as capacity creation.** Retiring an
  obsolete system frees attention for the next one.

## Open questions

- Which capabilities most often become unexpected
  bottlenecks as an AI portfolio grows?
- How is the option value of modular architecture
  reflected in budgeting and procurement?
- What does an AI capability roadmap look like for a
  regional hospital system vs. a large academic medical
  center?
- For pharma, how does AI capability portfolio
  interaction with the drug program portfolio change
  outsourcing choices?

## Related notes

- `docs/pharma-ai-systems-architecture.md` — pharma
  instantiation of the reference architecture that
  capability maturity applies to.
- `docs/pharma-ai-system-of-systems.md` — portfolio
  considerations change shape when constituents span
  discovery through pharmacovigilance.
- `docs/drug-discovery-program-architecture.md` —
  program-level sourcing, portfolio, and attrition
  framing that interacts with AI capability
  portfolios.
- `docs/ai-evaluation-strategy.md` — the evaluation
  evidence portfolio decisions rely on.

## Limitations and cautions

- Strategy frameworks are descriptive and heuristic; they
  do not determine decisions.
- Capability maturity models risk becoming checklists;
  the useful question is behavior, not the level label.
- Real options analysis in AI investments is qualitatively
  informative but rarely supports precise valuation.
