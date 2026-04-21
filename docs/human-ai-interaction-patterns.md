# Human-AI interaction patterns

Notes on the design space where a human decision-maker
meets a model's output — clinicians consuming decision
support in routine care, medicinal chemists iterating
in lead optimization, pharmacologists reviewing
simulation outputs, reviewers adjudicating adverse
events. The patterns below are about the interaction,
not the underlying model.

## Why interaction matters separately

A high-accuracy model can still fail as a deployed
system if the interface does not match the task, the
user, or the consequences. Beede et al. (2020) on Thai
diabetic retinopathy clinics is the canonical
illustration on the clinical side; the less-publicized
counterpart in discovery is a generative chemistry
model whose outputs no chemist accepts because the
interface does not surface why a compound was proposed.
Interaction design is the layer that determines whether
model accuracy translates into decision value.

## Audiences and their tasks

The interaction problem looks different across
audiences, even when the underlying model is similar.

- **Clinicians at the point of care.** Short time
  budgets, many concurrent tasks, high consequence for
  errors, alert fatigue a first-order constraint.
- **Clinical reviewers and adjudicators.** Longer time
  budgets per case, comparing evidence across
  modalities, writing decisions that become training
  data.
- **Medicinal chemists in a DMTA cycle.** Rapid
  iteration on compound sets, domain knowledge about
  chemotype, high skepticism toward proposals that
  look uninterpretable.
- **Pharmacologists and modelers.** Reviewing
  simulation outputs, inspecting sensitivity analyses,
  packaging evidence for regulators.
- **Operations and safety scientists.** Managing
  monitoring dashboards and signal workflows, paging
  patterns, threshold tuning.

The patterns below are general; their instantiation has
to fit the audience.

## Pattern: staged presentation

Rather than putting all information on one surface,
stage it: the headline output, the confidence, the
explanation, the caveats, the override.

**Why.** Mixed audiences and mixed tasks do not share a
single ideal information density. Staging lets the
reader pull for detail when the case requires it and
stay on the headline when it does not.

**Design parameters.**

- What is the headline — a score, a category, a
  ranking, a generated object?
- What is always visible vs. revealed on demand?
- How is the stage boundary signaled so the user knows
  more information exists?

## Pattern: uncertainty surfacing

Model uncertainty is a property of the output and a
first-class interaction element.

**Options for representation.**

- **Numeric.** A confidence number or interval; short
  but often miscalibrated in the user's head.
- **Categorical.** High/medium/low bands; easier to
  reason about, easier to hide calibration problems.
- **Graphical.** Intervals, shaded regions, or
  probability distributions; more information at the
  cost of screen real estate and training.
- **Reasoned.** A short sentence that names what the
  model is uncertain about — a format that conveys
  structure, not only magnitude.

**Design parameters.**

- Whether the representation supports the decision a
  user has to make.
- Whether the user has been trained on its meaning.
- Whether the representation degrades gracefully when
  the model cannot produce a calibrated estimate.

## Pattern: applicability-domain surfacing

For property, ADMET, and structure models, whether the
input falls inside the model's applicability domain is
as important as the point estimate.

**Presentation options.**

- An explicit flag (in domain / near boundary / out
  of domain) next to the prediction.
- Nearest-neighbor retrieval from training data with
  distance, so the user can judge novelty.
- A per-feature breakdown of which features drive the
  domain classification.
- A disclaimer that appears only when the prediction
  is out of domain, so the interface stays quiet in
  routine cases.

**Design parameters.**

- Whether the domain definition is meaningful to the
  user; a domain defined in an embedding space a
  chemist has no intuition for is marginal value.
- How false positives (flagging safe predictions as
  out of domain) are managed; an overly cautious
  flag becomes noise.

## Pattern: provenance and reasoning surfaces

Users accept model outputs more readily when they can
see where the output came from.

**Provenance options.**

- Training-data citation (for retrieval-augmented
  systems).
- Feature contributions or attribution maps (for
  predictive models), with known limits on what they
  mean.
- Counterexamples and nearest-neighbors from training
  data.
- Version stamps and links to the model facts label.
- For generative chemistry, scaffold retrieval from
  training data, synthetic-route hypothesis, and IP
  landscape flags.

**Design parameters.**

- Faithfulness of the explanation to the model
  (Rudin, 2019); post-hoc explanations can mislead.
- Training and experience the user has to interpret
  the provenance.
- The difference between an explanation of the model
  and an explanation of the decision the system is
  recommending.

## Pattern: override and feedback capture

A human in the loop is only in the loop if they can
disagree, and only useful to the system if their
disagreement is captured.

**Design parameters.**

- Override affordance. A visible, reversible action;
  not buried under confirmation dialogs that
  discourage use.
- Free-form vs. structured feedback. Free form is
  richer; structured feedback is easier to aggregate.
- Outcome tracking. Overrides that are later shown to
  have been correct or incorrect feed back into
  monitoring and model improvement.
- Feedback loop discipline. Raw user feedback is not
  training data without review; see the feedback
  loops discussion in
  `docs/systems-engineering-methods.md`.

## Pattern: alert staging

For systems that push outputs to the user, the staging
of the push matters as much as the underlying accuracy.

**Options along a spectrum.**

- **Blocking alert.** The workflow halts until the
  user acknowledges; highest attention cost.
- **Inline signal.** Visible where the user is
  working; moderate attention cost.
- **Passive indicator.** Present for reference;
  lowest attention cost.
- **Asynchronous digest.** Summary delivered
  out-of-band for review at the user's cadence.

**Design parameters.**

- Mapping severity and urgency to staging; not every
  serious output belongs in a blocking alert.
- Aggregation. Frequent signals of the same kind
  should aggregate, not repeat.
- Snooze and dismissal semantics; snooze should not
  silently become dismissal.
- Alert fatigue monitoring. Dismissal rate is a first-
  order signal about interface design, not user
  compliance.

## Pattern: active-learning and DMTA interaction

For pharma discovery, the interaction is not a
one-shot decision but a repeated cycle. The interface
has to support selecting a batch for experimentation,
tracking what comes back, and updating expectations
based on new readouts.

**Design parameters.**

- Batch-selection affordances — diversity,
  uncertainty, and predicted-value trade-offs made
  legible.
- Experimental-history threading; a proposal that
  repeats a previously tested compound without calling
  that out is a design error.
- Readout ingestion; when new assay data arrives, how
  quickly does the interface reflect updated
  predictions, and how is the user notified of
  changed rankings.

## Pattern: paired evidence display

Many pharma decisions are made on multiple pieces of
evidence that disagree. The interface that surfaces
agreement and disagreement across models is more useful
than an interface that shows one consensus number.

**Design parameters.**

- Side-by-side per-model outputs with their
  uncertainties and applicability-domain flags.
- Aggregation into a consensus label only where the
  aggregation is defensible; otherwise show the
  disagreement.
- Historical tracking of how different models have
  agreed on similar cases in the past.

## Pattern: logging and review

Every interaction that a user takes with a clinical
or discovery AI is an auditable record.

**Design parameters.**

- What is logged: the input, the prediction, the
  staged presentation, the user's response, the
  consequent action.
- Retention and access policy (see
  `docs/interface-contracts-for-healthcare-ai.md`).
- Review cadence; a log that no one reads is debt
  rather than oversight.
- User-visible logs; users who can see their own
  history interact with the system differently from
  users who cannot.

## Anti-patterns

Recurring failure modes on the interaction layer:

- **Precision theater.** Four decimal places on a
  score the user could not reliably distinguish.
- **Explanation without faithfulness.** A plausible-
  looking explanation unrelated to what the model
  actually used (Ghassemi, Naumann, Pierson, 2021).
- **Override as exit.** Overrides are allowed but
  discouraged, so users stop using them and the system
  loses its main feedback signal.
- **Alert ladder collapse.** Everything becomes a
  blocking alert because triage is too hard; dismissal
  rate climbs until the alerts are ignored.
- **Chemist-proof interface.** A chemistry design UI
  that hides the information chemists actually need,
  because it was built by ML engineers without domain
  users in the room.

## Connection to other notes

- Reference architectures:
  `docs/ai-systems-architecture.md`,
  `docs/pharma-ai-systems-architecture.md`.
- Clinical case material:
  `docs/clinical-ai-case-studies.md`.
- Pharma case material:
  `docs/pharma-ai-case-studies.md`.
- Fairness and equity in interaction:
  `docs/fairness-and-equity.md`.
- System dynamics for alert and trust loops:
  `docs/systems-engineering-methods.md`.
- Multi-model composition that users have to
  interpret: `docs/multi-model-orchestration-patterns.md`.

## Open questions

- Which interaction patterns carry the strongest
  empirical evidence for sustained use, and which are
  mostly aspirational?
- How should explanation interfaces be evaluated when
  the explanation can alter user behavior
  independently of model output?
- How do interaction patterns change when the user is
  a regulator conducting review rather than a user in
  routine operation?
- What does a minimum viable interaction logbook look
  like for a single-site hospital or a single
  discovery program?

## Limitations and cautions

- Interaction design claims are often evaluated on
  small, short-duration studies; sustained behavior
  under real operational pressure is less well
  characterized.
- Patterns generalize across audiences at the
  vocabulary level; their correct instantiation is
  highly context-dependent.
- Interface decisions intersect with fairness (which
  users are served well by the default) and equity
  (which patient groups carry the cost of a bad
  interaction default). Interface evaluation should
  examine both.
