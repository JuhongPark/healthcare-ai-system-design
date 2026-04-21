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
