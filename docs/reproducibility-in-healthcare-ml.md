# Reproducibility in healthcare machine learning

Notes on reproducibility issues specific to clinical and
discovery-stage machine learning. Reproducibility is treated
here as a precondition for evidence, not as an extra.

## Why this matters

A claim about a model's performance is only as good as the
record needed to reproduce it: the data, the splits, the
preprocessing, the labels, the code, the training and
evaluation procedure, and the random seeds. In healthcare
machine learning, several of these are often absent or
incompletely described, and small differences can flip the
sign of a result.

## Clinical machine learning

McDermott and colleagues (2021) characterize the
reproducibility problem for ML in healthcare, noting limits
in code release, data access, and reporting of evaluation
procedures. Stupple, Singerman, and Celi (2019) frame the
issue in the context of digital medicine more broadly,
including publication norms.

The COVID-19 pandemic produced a particularly visible test
case. Wynants and colleagues (2020) systematically reviewed
prediction models for COVID-19 diagnosis and prognosis and
judged most at high risk of bias. Roberts and colleagues
(2021) reviewed ML approaches to COVID-19 chest imaging
and found common pitfalls including inadequate dataset
description, data leakage, and overlap between training
and testing distributions.

### Open questions

- What is the minimum reporting standard for a clinical ML
  paper to be reproducible enough for external evaluation?
- How are private-data ML claims contested when neither
  data nor models are released?
- What is the right tradeoff between code release and
  patient privacy for studies trained on protected data?

## Discovery-stage machine learning

Reproducibility concerns in chemistry and drug discovery
ML have a different shape: the data are often public, but
benchmark splits can leak structure between training and
test sets, and small evaluation choices change leaderboard
rankings.

Wallach and Heifets (2018) showed that several ligand-based
classification benchmarks reward memorization over
generalization. Bender and Cortes-Ciriano (2021), in a
two-part series, give a critical assessment of what AI in
drug discovery has and has not delivered, with attention
to benchmark design, dataset diversity, and the gap
between benchmark scores and chemistry impact.

### Open questions

- How are benchmark splits designed for chemistry to
  expose generalization rather than reward memorization?
- Which published gains in molecular property prediction
  survive proper scaffold or temporal splits?
- For generative chemistry, how should evaluation
  distinguish novelty from rediscovery of known
  structures?

## Cross-cutting practices

- **Clear data provenance.** A description of where data
  come from, how they were partitioned, and what was
  excluded.
- **Code release with environment.** A reader should be
  able to recreate the run, not only read about it.
- **Multiple seeds and reporting variability.** Single-run
  numbers underspecify the comparison.
- **Preregistration where applicable.** Especially for
  clinical evaluation studies.
- **Negative results.** Studies that did not work but were
  rigorously conducted are part of the record.

## Limitations and cautions

- Reproducibility, transparency, and accuracy are related
  but distinct. A reproducible study can still be wrong; a
  non-reproducible study cannot be checked.
- Reproducibility norms differ across communities;
  practices that are standard in one corner of the field
  may not be in another.
- Published reproducibility critiques themselves rest on
  evidence; they are arguments, not proofs.
