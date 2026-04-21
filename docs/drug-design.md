# Drug design

Notes on AI in drug discovery and design — the upstream side
of the pipeline that produces the candidates later evaluated
in trials and in real-world data.

## Why drug design

The drug efficacy track in this repository covers how a
candidate is judged once it exists. Drug design covers how a
candidate is found and refined in the first place. The two
ends of the pipeline raise different methodological questions
and use different data, but they are connected: a candidate
that is poorly characterized upstream is harder to evaluate
downstream, and a treatment that fails in real-world data
raises questions about the design choices that produced it.

## Pipeline overview

A simplified view of the discovery pipeline:

- **Target identification.** Selecting a biological target
  whose modulation is expected to change disease state.
- **Hit discovery.** Finding molecules that interact with the
  target.
- **Lead optimization.** Refining hits to improve potency,
  selectivity, and pharmacokinetic properties.
- **Preclinical evaluation.** Toxicity, ADMET (absorption,
  distribution, metabolism, excretion, toxicity), and animal
  models.
- **Clinical development.** Phase 1 to 3 trials, then
  approval.

AI methods now appear at every stage, with very different
data, evaluation criteria, and failure modes at each.

## Target identification and validation

Target identification draws on omics data, genetic
associations, pathway analysis, and increasingly on
representation learning over biomedical knowledge graphs.
The hardest question is not finding a candidate target but
deciding whether modulating it will change disease.

### Open questions

- When does a strong genetic association translate into a
  tractable drug target, and when does it not?
- How should multi-omic evidence be weighted when modalities
  disagree?
- What does external validation look like for a target
  prediction whose ground truth is years of preclinical and
  clinical work?
- How are negative results from past target programs
  incorporated, given that they are often not published?

## Molecular generation and property prediction

Generative models — variational autoencoders over SMILES,
graph neural networks, transformer-based chemistry models —
propose new molecules. Property prediction models score them
for activity, selectivity, ADMET properties, and synthetic
accessibility. The two are typically used in a loop: generate,
score, filter, refine.

### Open questions

- How is a generative model evaluated when its outputs are
  meant to be novel and therefore have no ground truth?
- How are property predictions calibrated, and how is their
  applicability domain communicated to a chemist?
- What does a meaningful baseline look like for a generative
  chemistry model?
- How are synthetic accessibility, intellectual property, and
  toxicity handled alongside predicted activity?

## Structure prediction and structure-based design

Protein structure prediction at usable accuracy changes the
inputs available to structure-based drug design. Docking,
binding-affinity prediction, and free-energy calculation can
build on predicted structures, but the propagation of
prediction error through the downstream pipeline is itself a
research question.

### Open questions

- For which targets is a predicted structure good enough for
  structure-based design, and for which is it not?
- How is uncertainty in predicted structures propagated into
  binding-affinity estimates?
- How should structure-based and ligand-based methods be
  combined when both are available?

## Drug repurposing

Repurposing reuses approved or investigational compounds for
new indications. The data setting is different from de novo
discovery: rich existing safety data, known pharmacokinetics,
but also strong selection effects in which compounds have
been studied.

### Open questions

- How is a repurposing hypothesis evaluated when the original
  indication's data is much richer than the new one's?
- When can real-world data support a repurposing claim, and
  when does it produce a confounded association?
- How is the link between a discovery-stage repurposing
  hypothesis and a downstream observational study designed
  end-to-end?

## Linking design to evaluation

Design choices upstream constrain what can be claimed
downstream. A target picked from one population's genetics
may behave differently in another. A molecule optimized
against a particular assay may carry assay-specific
artifacts. A clinical trial designed around a particular
biomarker carries that biomarker's measurement properties
into post-marketing data.

### Open questions

- How should upstream design choices be documented so that a
  downstream evaluator can interpret them?
- Which design-stage decisions most often surface as problems
  in real-world evaluation?
- What does a unified record of a candidate look like, from
  target hypothesis to post-marketing surveillance?

## Active learning and Bayesian optimization

Generation and screening loops over chemical space rarely
have the budget to evaluate every candidate. Active learning
and Bayesian optimization choose which candidate to
evaluate next, given uncertainty estimates from a surrogate
model. Reker and Schneider (2015) survey active learning in
computer-assisted drug discovery; Gomez-Bombarelli and
colleagues (2018) demonstrate latent-space optimization
over a learned chemical representation. The choice of
acquisition function, the calibration of the surrogate, and
the relationship between in-silico scores and assay
behavior all shape whether the loop converges on useful
chemistry or on artifacts.

### Open questions

- How are uncertainty estimates from a surrogate model
  validated before they are trusted as inputs to an
  acquisition function?
- How is the cost structure of different assays reflected
  in batch design?
- When does an active-learning loop entrench artifacts of
  the initial dataset rather than escape them?

## Biomedical knowledge graphs

Knowledge graphs combine structured biomedical knowledge —
genes, proteins, diseases, drugs, side effects, pathways —
into a relational substrate that can be queried, embedded,
or reasoned over. Himmelstein and colleagues (2017)
introduced Hetionet and used it for systematic drug
repurposing prioritization. Zitnik, Agrawal, and Leskovec
(2018) introduced Decagon for graph-convolutional
prediction of polypharmacy side effects. Knowledge graphs
sit alongside structure-based and chemistry-foundation-
model approaches as another way to organize what is known
about candidate biology.

### Open questions

- How is the curation provenance of a biomedical knowledge
  graph documented, and how stale does it become between
  releases?
- How are negative or contradictory associations
  represented, and how do downstream models behave around
  them?
- How are knowledge-graph embeddings evaluated for tasks
  whose ground truth is years of laboratory work?

## Antibody and protein design

Beyond small molecules, deep learning has moved into the
design of proteins themselves. Dauparas and colleagues
(2022) introduced ProteinMPNN for sequence design given a
backbone; Watson and colleagues (2023) introduced
RFdiffusion for de novo design of protein structure and
function. Antibody discovery and engineering are an active
target for these methods. Foundational structure prediction
work in the same generation (Lin et al., 2023, ESMFold)
expands the inputs available to design.

### Open questions

- How is in-silico designed protein activity validated, and
  what is the failure rate from design to functional
  expression?
- How are structural and sequence-based methods combined
  in antibody design, and how is novelty distinguished from
  rediscovery?
- How do structure-prediction errors propagate into design
  decisions?

## AI in clinical trial design

Clinical trial design and operations sit between drug
design and drug efficacy evaluation. AI methods are now
applied to eligibility-criteria refinement, site selection,
patient stratification, and synthetic control arms. Harrer
and colleagues (2019) survey applications across trial
design; Liu and colleagues (2021) report on using
real-world data and AI to evaluate eligibility criteria of
oncology trials.

### Open questions

- How are AI-derived eligibility refinements assessed for
  representation effects across populations?
- When are external comparator arms — synthetic controls
  drawn from real-world data — defensible, and when do
  they introduce confounding equivalent to the missing
  randomization?
- How are AI-supported trial-design decisions documented
  for regulatory review?

## AI in pharmacovigilance

Once a drug is in use, signal detection in adverse-event
reports, EHR records, and unstructured text is itself a
machine-learning problem. Ball and Dal Pan (2022) review
the readiness of AI for pharmacovigilance with attention
to evaluation challenges. Pharmacovigilance closes a loop
back to the drug efficacy and real-world evidence
considerations covered earlier in this repository.

### Open questions

- How are AI-derived safety signals evaluated when ground
  truth itself depends on labor-intensive case adjudication?
- Where do natural-language processing pipelines for
  adverse events introduce biases that mirror the biases
  in the underlying records?
- How are pharmacovigilance signals fed back into design
  and trial planning for next-generation candidates?

## Limitations and cautions

- No claim is made that any candidate, target, or repurposed
  compound discussed here is suitable for clinical use.
- Computational results from public datasets illustrate
  method behavior; they do not establish biological activity.
- Generative chemistry outputs are not synthesizable
  candidates by virtue of being generated; synthesizability,
  toxicity, and intellectual property all sit outside the
  generation step.
- Public, synthetic, or simulated data only. No proprietary
  compound libraries, no licensed assay data, no internal
  pipeline documents.
- Protein design and pharmacovigilance descriptions are
  high-level orientation, not validated workflows.
