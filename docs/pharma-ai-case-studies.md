# Pharma AI case studies

A reading-style synthesis of published cases from AI-enabled
drug discovery and development, read for systems lessons
rather than as vendor or program endorsements. This note is
the pharma-side counterpart to
`docs/clinical-ai-case-studies.md`.

## Why case studies

Method-level notes elsewhere in the repository describe what
AI does in drug discovery. Case studies show how specific
programs assembled methods into a pipeline, what the
published record says happened, and where the gap between
press release and peer-reviewed evidence lies. The aim is
to read the public literature with program architecture
and evidence standards in mind.

## Halicin and open-ended antibiotic screening

Stokes and colleagues (2020) trained a graph neural network
on a curated library to predict growth inhibition of
Escherichia coli and used the model to screen large
out-of-distribution libraries. The paper reported halicin
(a repositioned compound) and structurally distinct
candidates with experimentally confirmed activity.

**What it illustrates.** Discovery-scale screening with a
deep-learning prior can surface chemotypes that
descriptor-based screens would have missed, provided the
prior was trained on well-curated data and the downstream
experimental validation is built into the loop.

**System lessons.** The press attention outran the
evidence: halicin has not advanced through the late-stage
development needed to establish clinical utility. A case
study that shows the promise of a method should not be
read as a finished therapeutic. The program architecture
that surrounds the model — library curation, assay
selection, downstream chemistry, ADMET and preclinical
safety — does the work that turns a hit into a candidate.

## Exscientia DSP-1181 and AI-accompanied discovery

In 2020, Exscientia and Sumitomo Dainippon Pharma announced
DSP-1181, reported as the first molecule designed using AI
to enter Phase 1 trials. Subsequent reporting indicated
that Phase 1 did not meet criteria to advance and the
program was discontinued.

**What it illustrates.** AI-accompanied design shortened
the time from target to candidate by the sponsors' own
account, but shortening the design phase does not change
the underlying probability that a clinical trial will meet
its endpoints. Program attrition retains its classical
structure even when AI has changed the cycle time.

**System lessons.** Program-level success and method-level
success are different claims. A candidate reaching Phase 1
faster than a traditional program is an operational
success for the discovery organization; clinical success
requires evidence downstream that does not depend on the
AI component.

## Insilico Medicine INS018_055 and target-plus-chemistry AI

Insilico Medicine has described an end-to-end AI pipeline
that nominated a novel target (TNIK) and a novel small
molecule (INS018_055) for idiopathic pulmonary fibrosis,
with the candidate entering Phase 2 trials as of the
company's public disclosures.

**What it illustrates.** A pipeline that couples target
identification from transcriptomic and biomedical-graph
evidence with generative and property-prediction
chemistry is a recognizable architectural pattern, now
in clinical evaluation rather than purely in silico.

**System lessons.** Programs that claim end-to-end AI
contribution inherit a reviewability challenge: the
evidence that the AI components changed the outcome,
relative to what a conventional program would have done,
is indirect. As clinical readouts arrive, the reading
will turn from architectural pattern to outcome.

## Recursion Pharmaceuticals and phenomic screening

Recursion's published work (including Celik et al., 2024,
and antecedent preprints) describes phenotypic screening
at scale using cellular imaging and self-supervised
representation learning. The company has reported a
pipeline of partnered and in-house programs arising from
this platform.

**What it illustrates.** Phenomic screening is a different
discovery philosophy from target-centric design — it
optimizes against observed cellular phenotypes rather
than a hypothesis about a specific target. The platform
view aligns with a portfolio-level build/buy/partner
conversation (`docs/ai-portfolio-and-strategy.md`).

**System lessons.** Platform companies bear the cost of
infrastructure and data that programs using the platform
amortize over time. Whether the platform pays off
depends on how many programs reach stage-gate decisions
and on how many of those decisions change because of the
platform.

## Isomorphic Labs and structure-first discovery

Isomorphic Labs, spun out of DeepMind, emphasizes a
structure-first discovery approach building on the
AlphaFold lineage. Public disclosures include
collaboration agreements with multiple pharma sponsors
and early-pipeline programs.

**What it illustrates.** Structure-first strategy is a
bet that structural prediction at new accuracy regimes
is a bottleneck relief for programs rather than a final
answer. Translating AlphaFold-quality predictions into
productive drug discovery requires the pipeline around
them — pocket analysis, docking and binding-affinity
estimation with calibrated uncertainty, chemistry
follow-through.

**System lessons.** A capability that is valuable at
scale is not automatically a product by itself.
Isomorphic's choice to combine in-house pipeline with
partnership agreements is a public statement about how
platform capabilities monetize at different program
stages.

## BenevolentAI and baricitinib repositioning

Early in the COVID-19 pandemic, BenevolentAI used a
biomedical knowledge graph to prioritize baricitinib as
a candidate for repositioning against COVID-19 (Richardson
et al., 2020). Baricitinib was subsequently trialed and
received Emergency Use Authorization in 2020 and full
FDA approval for COVID-19 in 2022.

**What it illustrates.** Repositioning hypotheses from
knowledge-graph reasoning can enter clinical evaluation
quickly when the experimental and regulatory environment
favors speed. The approval trajectory ran through
randomized controlled trials, not through the AI
prioritization step alone.

**System lessons.** An AI repositioning hypothesis is an
input to a regulatory evidence process, not a substitute
for it. The case is often read as a success for AI
repositioning; reading it as a success for a clinical
evaluation machinery that responded quickly to an
AI-surfaced candidate is equally defensible and more
portable.

## AlphaFold lineage and community infrastructure

AlphaFold (Jumper et al., 2021), AlphaFold-Multimer
(Evans et al., 2022 preprint), and AlphaFold 3 (Abramson
et al., 2024) successively broadened the scope of
structure prediction from single protein chains to
multimeric complexes and to complexes with ligands and
nucleic acids. The AlphaFold Protein Structure Database
(Varadi et al., 2022) made predictions available at
proteome scale.

**What it illustrates.** Community infrastructure
changes what downstream programs can assume. Pipelines
that previously required internal structural biology can
access predicted structures as a baseline, with
uncertainty estimates that vary across targets.

**System lessons.** Infrastructure provided as a shared
resource shifts the build/buy/partner boundary across
the industry. Programs that build around predicted
structures inherit AlphaFold's error modes; programs
that do not use them carry the cost of producing their
own structures where it can be avoided.

## Cross-case themes

- **Method success versus program success.** Shortened
  cycle time, novel chemotype discovery, and
  prioritization ranking are method-level outcomes.
  Patient benefit runs through stage-gate attrition
  that AI methods do not by themselves change.
- **Public disclosure asymmetry.** Companies publish
  successes more than discontinuations; the reading
  here intentionally includes discontinued and
  uncertain cases because the system lessons depend on
  both.
- **Infrastructure versus product.** Capabilities
  (structure prediction, phenotypic platforms,
  biomedical knowledge graphs) propagate across
  programs differently from clinical candidates;
  portfolio-level reasoning treats them separately.

## What case studies cannot do

Each case reflects what is publicly known at a point in
time. Proprietary data, internal development decisions,
and unpublished negative results shape the complete
picture and are not available to this reading. The
lessons generalize as design questions, not as predictive
claims about future programs.

## Connection to other notes

- Architectural framing:
  `docs/drug-discovery-program-architecture.md`.
- Method-level detail: `docs/drug-design.md`,
  `docs/admet-and-preclinical-safety.md`.
- Portfolio perspective:
  `docs/ai-portfolio-and-strategy.md`.
- Case-material counterpart for clinical deployment:
  `docs/clinical-ai-case-studies.md`.
- Regulatory surround:
  `docs/regulatory-landscape.md`.

## Limitations and cautions

- Case summaries reflect the published record as of
  the current reading date; company trajectories,
  clinical results, and regulatory status change.
- Mention of specific sponsors, programs, and
  candidates is descriptive, not evaluative; inclusion
  is driven by what public literature documents, not
  by any judgment about quality or safety.
- No clinical claim is made about any candidate
  discussed here. Clinical evidence is established by
  the trials and regulatory reviews cited, not by this
  reading.
- Press releases and company disclosures are used with
  caution; wherever possible, peer-reviewed references
  are given alongside company statements.
