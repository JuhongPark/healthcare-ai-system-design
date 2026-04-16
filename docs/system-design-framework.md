# System design framework

A framework for thinking about healthcare AI as a full system
rather than only as a model. The sections below are not a
checklist to pass — they are the questions a design should be
able to answer.

## Core message

Healthcare AI should be evaluated as a full system, not only as
a model. The model is one component among many: the data
pipeline, the workflow integration, the interface, the
monitoring layer, the update process, and the accountability
structure all shape whether the system is useful and safe.

A system that has a good model but no monitoring, or a good
interface but an unclear source of ground truth, or a clear
workflow fit but no update process, is not a good system.

## Problem definition

- What decision is being supported?
- Who makes that decision today, and with what information?
- What would change if the system were present? What would not
  change?
- What is the closest acceptable "do nothing" alternative, and
  why is a model expected to do better?
- How would you know, after deployment, whether the system
  helped?

A weak answer here makes every later section harder.

## Stakeholders and workflow context

- Who sees the system's output? Who acts on it? Who is
  accountable?
- At what step of the workflow does the output appear?
- What other information is present at that step, and how does
  the system's output interact with it?
- What happens if the system is unavailable?
- What happens if the system disagrees with the user?

Workflow questions belong at the beginning of a design, not at
the end.

## Data provenance and quality

- Where does each data source come from, and how was it
  collected?
- What is the target label, and how is it constructed? Is it a
  proxy for the thing that actually matters?
- What is missing, and is it missing at random?
- How has coding or measurement changed over time?
- How will the data pipeline change between development and
  deployment?

Data provenance is often the weakest link. Document it early
and update the notes as the pipeline evolves.

## Observational vs. causal claims

- Is the system trying to predict, to explain, or to estimate a
  treatment effect?
- If the system is used to guide a decision, is the user
  implicitly making a causal claim?
- What confounders are plausible, and which are adjusted for?
- What design choices (matching, weighting, instrumental
  variables, negative controls) support the claim?
- Which sensitivity analyses would change your conclusion?

The default for observational analyses should be that they are
associational. Causal claims need an explicit design and
explicit assumptions.

## Modeling and uncertainty

- What is the outcome, the loss, and the evaluation metric?
- What is the baseline that any new model must beat, and why?
- How is uncertainty quantified — aleatoric, epistemic, or both?
- How does the model behave on inputs it has never seen?
- How does the model behave when a modality is missing?

A model that reports point estimates without any sense of
uncertainty is under-specified for clinical use.

## Human workflow fit

- When does the output appear?
- How much time does the user have to read it?
- What does the user need to ignore in order to act on it?
- How is disagreement with the model captured?
- Does the interface make the right thing easy and the wrong
  thing visible?

Workflow fit is a design constraint, not an aesthetic choice.

## Interpretability and communication

- What does the system claim to explain?
- What does it not explain, and is that stated?
- How is uncertainty communicated to a non-statistical audience?
- Are explanations stable under small input changes?
- Do explanations expose shortcuts the model is taking?

Interpretability is easy to simulate and hard to deliver.
Prototypes should be honest about which they are doing.

## Validation and monitoring

- What does local validation look like, and who runs it?
- What is evaluated: discrimination, calibration, subgroup
  performance, clinical utility, workflow impact?
- What happens when performance drifts?
- What is the smallest useful monitoring setup?
- Who reads the monitoring dashboard, and how often?

Monitoring is part of the system from the start, not an
afterthought.

## Governance and safety

- Who owns the model? Who owns the deployment? Who owns the
  data pipeline?
- Under what conditions is the system paused, updated, or
  retired?
- Who authorizes a change, and who reviews it?
- What are the known failure modes, and how would a user
  recognize one?
- What is logged, for how long, and who can read the logs?

Governance is easier to design before deployment than after an
incident.

## Deployment and feedback loops

- How is a new model version staged, shadow-tested, and
  released?
- How are outputs used — and therefore how might they influence
  the next round of training data?
- What feedback does the user give to the system, and how is it
  used?
- What is the rollback plan?
- How will the design be revisited a year from now?

Every deployed system eventually becomes part of the
data-generating process. Plan for it.
