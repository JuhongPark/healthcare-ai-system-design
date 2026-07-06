# Claim to citation map

This map connects repository-level claims to the literature
reviewed in `references/evidence-matrix.csv`. It is not a
substitute for reading the sources. It is a guardrail against
unsupported project claims.

## System-level healthcare AI

| Repository claim | Support level | Supporting sources | Repo artifact | Design consequence |
| --- | --- | --- | --- | --- |
| Healthcare AI should be evaluated as a full system, not only as a model. | Strong conceptual support | E001, E002, E005, E006, E007, E027 | `docs/system-design-framework.md`, `docs/ai-evaluation-strategy.md` | Keep data, interface, monitoring, governance, and workflow as first-class design surfaces. |
| Deployment claims require local validation, calibration, and alert-burden analysis. | Strong empirical and guidance support | E001, E003, E005, E010, E027 | `prototypes/cds-risk-dashboard`, `prototypes/monitoring-loop-sketch` | Do not present aggregate model performance as deployment readiness. |
| AI lifecycle work needs explicit monitoring and change-control artifacts. | Strong guidance support | E001, E002, E009, E010 | `docs/mlops-for-regulated-ai.md`, `prototypes/monitoring-loop-sketch` | Treat monitoring reports and update gates as required system outputs. |

## Evidence and observational analysis

| Repository claim | Support level | Supporting sources | Repo artifact | Design consequence |
| --- | --- | --- | --- | --- |
| Real-world evidence depends on data relevance, data reliability, and study design. | Strong regulatory and methods support | E008, E011, E012 | `prototypes/rwe-drug-efficacy-sketch` | Add protocol-like cohort design tables before effect estimates. |
| Observational treatment comparisons should default to association unless causal assumptions are explicit. | Strong methods support | E011, E012, E013, E014 | `docs/system-design-framework.md`, `prototypes/rwe-drug-efficacy-sketch` | Keep causal language guarded and pair estimates with assumptions and diagnostics. |
| Negative controls are bias diagnostics, not proof that a causal estimate is correct. | Strong methods support | E014 | `prototypes/rwe-drug-efficacy-sketch` | Label negative-control results as warnings or reassurance signals, not validation. |

## Workflow and interface design

| Repository claim | Support level | Supporting sources | Repo artifact | Design consequence |
| --- | --- | --- | --- | --- |
| Clinical decision support value depends on workflow timing, actionability, and user burden. | Strong CDS literature support | E004, E015, E016, E027 | `prototypes/cds-risk-dashboard` | Compare passive, inline, and interruptive display patterns before choosing an alert form. |
| Explanation panels can mislead if they imply a feature ranking validates a model or decision. | Strong cautionary support | E017, E018 | `prototypes/cds-risk-dashboard` | Pair explanations with uncertainty, limits, and missing-context notes. |
| Early clinical AI evaluation should include human factors and small-scale safety evidence. | Strong reporting-guideline support | E004, E027 | `docs/human-ai-interaction-patterns.md`, future CDS experiments | Define an early evaluation packet before workflow-readiness claims. |

## Documentation, fairness, and reproducibility

| Repository claim | Support level | Supporting sources | Repo artifact | Design consequence |
| --- | --- | --- | --- | --- |
| Datasets and model-like artifacts need structured documentation. | Strong documentation-framework support | E019, E020 | future templates | Add data-card and model-card templates for synthetic generators and model-like outputs. |
| Proxy labels can encode inequity even when protected attributes are not directly used. | Strong audit case support | E021 | `docs/fairness-and-equity.md`, future audit prototype | Add proxy-label audits before model performance summaries. |
| Repository artifacts should keep no-clinical-use and synthetic-only boundaries visible. | Strong governance support | E007, E019, E020 | all prototypes | Continue safety labels in prototype READMEs and generated outputs. |

## Pharma and drug development systems

| Repository claim | Support level | Supporting sources | Repo artifact | Design consequence |
| --- | --- | --- | --- | --- |
| Drug discovery AI is a program component, not proof of therapeutic value. | Strong review and case-study support | E022, E025, E026 | future pharma prototype | Separate computational prioritization from assay, ADMET, and program-stage evidence. |
| Molecular ML benchmarks help comparison but do not remove applicability-domain and generalization concerns. | Strong benchmark support | E023, E024 | future ADMET or property-prediction prototype | Report splits, applicability domain, calibration, and benchmark limitations together. |
