# AI evaluation strategy

Notes on evaluation as an architectural concern: which
evaluations belong at which stage, how their results
connect, and how an evaluation strategy outlives any
single model version.

## Why evaluation is architecture

Evaluation is often treated as an activity that happens
once, somewhere between model training and release.
Treated that way, it becomes brittle: a benchmark
passed at Gate 3 has no carry-over to post-deployment
monitoring, and a post-deployment alert has no tie-back
to the pre-deployment report. A deployed AI system
needs an evaluation strategy — a deliberately designed
set of evaluations with defined scopes, consumers, and
renewal cadences — that sits inside the reference
architecture.

## Evaluation planes and stages

Evaluations align with the planes in the reference
architectures (`docs/ai-systems-architecture.md` and
`docs/pharma-ai-systems-architecture.md`) and the
lifecycle gates in
`docs/ai-lifecycle-management.md` and
`docs/pharma-ai-lifecycle-management.md`.

- **Internal validation.** On data the team controls;
  covers baseline comparison, discrimination,
  calibration, subgroup performance.
- **External validation.** On data from another site
  or period; covers generalization across space and
  time.
- **Local validation.** At the deploying site on its
  own data; the evidence that matters for the local
  decision to deploy.
- **Shadow evaluation.** In production infrastructure
  but without affecting decisions; end-to-end checks
  of the serving, monitoring, and integration planes.
- **Canary evaluation.** Small-traffic production with
  rollback triggers; real-world but bounded-blast-
  radius.
- **Prospective validation.** Pre-registered
  comparison against outcomes observed after model
  freeze; the strongest evidence and the one most
  often skipped.
- **Post-deployment monitoring.** Continuous
  evaluation on live data; covers drift,
  calibration, subgroup, operational metrics.

The architectural claim is that these are not
alternatives. A mature system does several at once, and
the results link.

## Evaluation dimensions

Orthogonal to stage, evaluations vary on what they
measure.

- **Discrimination and ranking.** ROC-AUC, PR-AUC,
  top-k precision, concordance.
- **Calibration.** Reliability diagrams, Brier score,
  expected calibration error, piecewise calibration
  by subgroup.
- **Subgroup performance.** Metrics broken down by
  demographic, clinical, or chemotype group; the
  primary vehicle for fairness evaluation (see
  `docs/fairness-and-equity.md`).
- **Robustness.** Stability under distribution shift,
  adversarial perturbations, or scaffold changes.
- **Applicability domain.** Coverage of input space
  and behavior on boundary inputs.
- **Decision impact.** Whether and how often model
  outputs changed decisions, and with what downstream
  effect; net benefit (Vickers, Elkin, 2006) or
  analogous economic framings.
- **Operational quality.** Latency, availability,
  freshness, rollback frequency.
- **Generative quality.** For generative models
  (chemistry, text), measures of novelty, diversity,
  synthesizability, validity, and faithfulness.

No single metric answers every question. Metric
choice is a design decision; metric aggregation hides
more than it reveals.

## Slice-based evaluation

Aggregate metrics hide where a model is failing.
Slice-based evaluation (Chen et al., Snorkel-era work;
Goel et al., 2021) breaks performance down by meaningful
subsets of inputs.

**Candidate slicing dimensions.**

- Clinical: age band, sex, race/ethnicity where
  recorded, comorbidity groups, site, time period.
- Pharma: chemotype family, molecular-weight range,
  target family, assay condition, source database.
- Structural: sequence similarity to training set,
  fold family, resolution band.
- Modality: image type, note length, data completeness.

**Design parameters.**

- Pre-registered vs. post-hoc slicing; post-hoc
  slicing can find anything.
- Minimum slice size for a metric to be meaningful.
- Threshold adjustment by slice vs. uniform threshold
  with subgroup-specific calibration reporting; both
  are defensible choices with different consequences.

## Evaluation data management

Evaluation datasets are artifacts with their own
lifecycle.

- **Held-out by construction.** Scaffold, time, or
  site splits that stay held out across model
  versions.
- **Versioning.** The evaluation set has a version
  identifier; using a different version means using a
  different evaluation.
- **Freshness.** Held-out sets become stale. Refresh
  cadence is a governance decision.
- **Access control.** The evaluation set can leak into
  training through model iteration and ablation
  choices; access policy matters.
- **Dataset sheets.** Datasheets for Datasets (Gebru
  et al., 2021) is the orienting reference for how
  evaluation datasets should be documented.
- **Public benchmark hygiene.** Chemistry benchmarks
  that reward memorization (Wallach and Heifets,
  2018) are a persistent concern; benchmark selection
  is itself an evaluation-strategy decision.

## Prospective validation discipline

Prospective validation is the evaluation that bounds
the others. Its discipline:

- **Pre-registration.** Evaluation plan locked before
  outcomes are observed.
- **Hypothesis pre-specification.** Acceptance
  criterion, primary and secondary endpoints, subgroup
  analyses, and handling of missing or partial
  outcomes stated up front.
- **Comparator pre-specification.** What the model is
  being compared against (baseline, prior version,
  clinical rule).
- **Separation of roles.** The pre-registration, the
  analysis, and the operational deployment are not
  all the same person's responsibility.
- **Results release.** Prospective results are
  reported whether favorable or unfavorable; selective
  reporting is a governance failure.

For pharma, prospective validation is the comparison
against assay readouts after the compound list was
scored; for clinical AI, it is the comparison against
outcomes after the model output was produced at the
point of care.

## Monitoring as ongoing evaluation

Post-deployment monitoring is continuous evaluation.
The monitoring plan is part of the evaluation strategy,
not a separate artifact.

- **Drift metrics.** Input drift, prediction drift,
  calibration drift, subgroup metric drift.
- **Outcome alignment.** As outcomes arrive with lag,
  the moving comparison between prediction and
  observed outcome carries the calibration and
  discrimination signal.
- **Alert thresholds.** Set to detect degradation
  meaningful to the decision, not degradation
  meaningful to the metric.
- **Review cadence.** A monthly review of monitoring
  results by the governance committee turns signals
  into decisions; without that review, signals
  accumulate unread (see
  `docs/ai-organizational-design.md`).

## Evaluation registry

An evaluation registry is the cross-stage artifact that
ties internal, external, local, shadow, prospective,
and monitoring evaluations for one model together:

- **Per-model entry.** All evaluations that ran on a
  model version, with their data versions, metrics,
  and conclusions.
- **Per-decision entry.** What evaluations were
  consulted at each gate and how they influenced the
  decision.
- **Cross-version comparison.** Structured comparison
  across model versions so that drift in model
  behavior is visible.
- **Read access.** Governance, operations, and
  audit roles read the registry; model developers
  write to it.

A registry of this kind is rare in practice. It is
also the artifact a regulator most often wants on hand.

## Evaluation anti-patterns

- **Benchmark leaderboard substitution.** A public
  leaderboard ranking is not a validation of deployed
  behavior.
- **Single-metric focus.** A model that optimizes one
  metric while silently degrading on another breaks
  at deployment.
- **Retrospective-only evaluation.** A retrospective
  benchmark that was passed at Gate M2 is not the
  evaluation that matters for Gate M5.
- **Post-hoc subgroup analysis passed off as
  pre-registered.** Multiple testing across
  subgroups inflates apparent robustness.
- **Evaluation without a consumer.** A metric that
  no one uses to make a decision is notation debt.

## Connection to other notes

- Reference architectures:
  `docs/ai-systems-architecture.md`,
  `docs/pharma-ai-systems-architecture.md`.
- Lifecycle and stage gates:
  `docs/ai-lifecycle-management.md`,
  `docs/pharma-ai-lifecycle-management.md`.
- Reproducibility discipline that evaluation relies on:
  `docs/reproducibility-in-healthcare-ml.md`.
- Fairness-specific evaluation:
  `docs/fairness-and-equity.md`.
- Regulated context:
  `docs/mlops-for-regulated-ai.md`.
- Cross-model composition that evaluation has to
  cover: `docs/multi-model-orchestration-patterns.md`.

## Open questions

- What is the smallest useful evaluation registry for
  a single-site hospital or a single discovery
  program?
- How should evaluation strategy evolve for continually-
  learning models that do not have a single frozen
  snapshot to evaluate?
- Which decision-impact metrics (net benefit,
  clinical utility, portfolio NPV contribution) have
  usable adoption, and which remain academic?
- How is cross-stage evaluation consistency enforced
  in a system of systems where constituents set their
  own evaluation policies?

## Limitations and cautions

- Evaluation strategy does not replace scientific
  judgment. Metrics are inputs to decisions, not
  substitutes for them.
- The evaluation-registry idea is an aspiration in
  most organizations; the useful first step is a
  minimal per-model evaluation record.
- Slice-based evaluation can proliferate; the
  discipline is in selecting the slices that matter,
  not in reporting every slice that exists.
