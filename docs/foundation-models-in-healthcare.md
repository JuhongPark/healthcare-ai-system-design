# Foundation models in healthcare

Notes on the use of large pretrained models — clinical
language models, multimodal medical models, and chemistry
foundation models — in healthcare AI. The framing here
treats foundation models as one tool among several, with
strong orienting questions about evaluation, scope, and
deployment.

## Why foundation models

Foundation models are large models pretrained on broad data
and adapted to many downstream tasks (Bommasani et al.,
2021). In healthcare they show up at three layers:

- **Clinical language and EHR models.** Pretrained on
  clinical or biomedical text, sometimes on structured EHR
  data, with downstream tasks ranging from coding to
  clinical question answering.
- **Multimodal medical models.** Combining text with
  imaging, signals, or structured data toward generalist
  medical AI.
- **Chemistry foundation models.** Pretrained on molecular
  representations (SMILES, graphs, learned embeddings) for
  downstream property and activity prediction.

Each has its own evaluation pitfalls and deployment risks;
the term foundation model bundles them together but the
underlying methods and audiences differ.

## Clinical language models

Domain-pretrained models for clinical text predate the
recent generation of large general-purpose LLMs. GatorTron
(Yang et al., 2022) showed task-specific gains over general
models when pretrained on a large corpus of clinical notes.
Lehman and colleagues (2023) compared general and clinical
models and asked whether continued pretraining still pays
off given the size of recent general models — the answer,
they argue, depends on the task and on the data available.

Singhal and colleagues introduced Med-PaLM (Singhal et al.,
2023) as a large language model evaluated on medical
question answering benchmarks, with subsequent iterations
reaching expert-level performance on specific benchmarks.
Moor and colleagues (2023) framed the broader vision of
generalist medical AI built on foundation models, while
also noting the evidence and evaluation gaps.

### Open questions

- When does clinical pretraining still pay off relative to
  prompting a sufficiently capable general model?
- Which clinical tasks have benchmarks that meaningfully
  reflect clinical use, and which are stuck on shortcut
  metrics?
- How are hallucinations characterized for medical question
  answering, and what does an acceptable rate look like for
  each downstream use?

## Multimodal medical models

Multimodal medical foundation models add imaging, signals,
or structured data to language. Their evaluation needs to
cover modality coverage, missing-modality behavior, and
cross-population performance — the same concerns as
multimodal medical models in general, raised again at
foundation-model scale.

### Open questions

- How is generalization from public benchmarks to local
  clinical data being evaluated, and what counts as
  evidence of fitness for a specific use?
- How are multimodal foundation models being adapted at the
  hospital level, and what does the integration overhead
  look like?
- When does a generalist model win against a focused
  task-specific model in clinical settings, and when does
  it not?

## Chemistry foundation models

Chemistry foundation models pretrained on large molecular
corpora — ChemBERTa (Chithrananda et al., 2020), MoLFormer
(Ross et al., 2022), and graph-based variants — provide
representations for downstream property and activity
prediction. They sit alongside structure-prediction models
such as AlphaFold (Jumper et al., 2021) and ESMFold (Lin
et al., 2023), which are foundation-scale efforts in a
different modality.

### Open questions

- What constitutes meaningful out-of-distribution
  evaluation for a chemistry foundation model whose
  pretraining corpus already covers most of medicinal
  chemistry?
- How are activity-prediction benchmarks vulnerable to
  memorization (Wallach and Heifets, 2018), and how should
  benchmark splits be designed to expose generalization?
- Which downstream tasks transfer well from pretraining,
  and which need substantial supervised data anyway?

## Issues across all three layers

- **Evaluation.** Benchmarks selected during pretraining
  influence what looks like progress; benchmarks selected
  during deployment determine whether progress is real.
- **Documentation.** Foundation models inherit dataset and
  model documentation problems at a larger scale.
- **Deployment cost.** Inference, governance, and
  monitoring costs do not scale linearly with capability.

## Limitations and cautions

- Foundation model results from generic benchmarks do not
  establish fitness for any clinical use.
- Clinical tasks built on top of pretrained models inherit
  pretraining biases that are often not characterized in
  detail.
- Chemistry foundation models can score well on benchmarks
  that reward memorization; benchmark scores alone do not
  establish drug-discovery utility.
