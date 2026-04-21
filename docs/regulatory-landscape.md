# Regulatory landscape

Notes on the regulatory context that shapes how AI is
developed, evaluated, and deployed in healthcare — covering
both clinical AI as software as a medical device and AI as
a tool inside the drug development pipeline.

## Why regulation

Regulation is one of the constraints that distinguishes
healthcare AI from other ML domains. Decisions about study
design, monitoring, change control, and post-market
evidence are shaped by what regulators can and will accept.
Reading regulators directly — not only secondary commentary
— is part of the systems-design discipline.

## United States: FDA

The U.S. Food and Drug Administration regulates clinical AI
under the Software as a Medical Device (SaMD) framework,
informed by the International Medical Device Regulators
Forum. Several developments are central:

- **AI/ML SaMD Action Plan (2021).** A five-action plan
  including a tailored regulatory framework for AI/ML-based
  SaMD, Good Machine Learning Practice, a patient-centered
  approach to transparency, regulatory science methods for
  bias, and real-world performance monitoring.
- **Good Machine Learning Practice Guiding Principles
  (2021).** A joint FDA, Health Canada, and MHRA document
  of ten guiding principles, framed as a starting point
  rather than a regulation.
- **Predetermined Change Control Plans Guiding Principles
  (2023).** Joint guiding principles for managing
  modifications to ML-enabled medical devices over time
  without re-submission for every change.
- **Approval database trends.** Empirical reviews
  (Muehlematter et al., 2021; Benjamens et al., 2020)
  show rapid growth in approved AI/ML medical devices,
  with most concentrated in radiology and a small share
  including continuous learning.

For drug development, the FDA's Model-Informed Drug
Development program covers a different but related
landscape: how computational models support submissions and
labeling decisions. A 2023 FDA discussion paper introduced
considerations for AI in drug manufacturing, signaling
extension of regulatory attention from the clinic into
production.

## European Union: MDR and the AI Act

The Medical Device Regulation (MDR, Regulation (EU)
2017/745) governs clinical AI as a medical device. The AI
Act adds a horizontal classification of high-risk AI
systems, with obligations on risk management, data
governance, transparency, human oversight, accuracy, and
post-market monitoring.

Vokinger and colleagues (2021) trace the implications for
continual learning systems in particular: regulatory
framing has historically assumed a more stable artifact
than continually learning models provide.

## Other jurisdictions

- **United Kingdom.** Post-Brexit, the MHRA has issued its
  own roadmap for software and AI as a medical device.
- **Canada.** Health Canada participates in the joint GMLP
  document.
- **Japan, China, South Korea.** Each has issued AI medical
  device guidance with varying timelines and content.
  Cross-jurisdiction comparison is itself an active
  research area.

## Cross-cutting themes

- **Transparency.** Transparency requirements increasingly
  cover what is in training data and how performance varies
  across subgroups.
- **Post-market monitoring.** Regulators increasingly expect
  ongoing performance reporting, not only pre-market
  evidence.
- **Predetermined change control.** A pathway for managing
  expected modifications without re-submitting from scratch
  is now broadly endorsed in principle; operational details
  vary.
- **Bias and equity.** Bias is now a stated regulatory
  concern, with limited but growing methodological guidance.
- **Drug discovery AI.** Regulatory expectations for AI
  used in target identification, candidate generation, and
  trial design are still being articulated and overlap with
  Model-Informed Drug Development guidance.

## Open questions

- How is the operational meaning of a predetermined change
  control plan being settled across jurisdictions?
- Where do regulator-required monitoring duties intersect
  with hospital-side monitoring described elsewhere in this
  repository?
- For AI used in drug discovery, what regulatory submission
  patterns are emerging, and how do they relate to
  Model-Informed Drug Development?
- How are bias auditing requirements being operationalized,
  and what does compliance evidence look like?

## Limitations and cautions

- Regulatory documents change. Cited dates indicate the
  state of the document at issue, not a current snapshot.
- Discussion is descriptive, not legal advice.
- Cross-jurisdiction comparisons are intentionally
  high-level and may obscure local nuance.
