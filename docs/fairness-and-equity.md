# Fairness and equity

Notes on fairness, bias, and equity in healthcare AI —
spanning clinical decision support, predictive risk scores,
and AI in drug discovery and trial design. The framing here
treats equity as a system property, not a model property.

## Why this matters

Healthcare AI inherits the inequities of the data it is
trained on, the populations it is evaluated on, and the
care systems it is deployed in. A model that performs well
on average can perform poorly for the patients with the
least leverage. Fairness in this setting is not a
constraint added on top; it is a question about whose
errors the system absorbs.

## Risk score bias

Obermeyer and colleagues (2019) showed that a widely used
commercial risk-prediction algorithm, by using cost as a
proxy for need, systematically under-allocated care to
Black patients at the same level of illness as white
patients. The case is now the canonical example of how a
label choice can encode structural bias and be hidden by
good aggregate performance.

**What it illustrates.** Proxy labels carry the inequities
of the systems that produced them. A label that looks
neutral can encode unequal access to care.

## Imaging model disparities

Seyyed-Kalantari and colleagues (2021) showed that chest
radiograph classifiers had higher under-diagnosis rates for
female, Black, Hispanic, and low-socioeconomic-status
patients across multiple datasets. The disparities did not
disappear with simple debiasing approaches and tracked the
representation of subgroups in training data.

**What it illustrates.** Imaging models learn from labeled
historical data; the distribution of labels and patients
shapes who the model is reliable for.

## Equity as opportunity

Pierson and colleagues (2021) used algorithmic methods to
identify unexplained pain disparities in knee
osteoarthritis, showing how AI applied carefully can
surface inequities rather than produce them. Paired with
Obermeyer et al., the case illustrates that the same
methodology can do either.

**What it illustrates.** What an AI system does for equity
depends on what it is asked to do, on what data, and with
what evaluation.

## In drug discovery and trials

Equity issues in drug development show up earlier in the
pipeline. Genome-wide association data, the populations
that contribute to public chemistry datasets, the
populations enrolled in clinical trials — each carries
representation biases that flow downstream. AI tools that
amplify the available data also amplify their biases.

### Open questions

- How are training datasets in drug discovery characterized
  for population coverage, and where does that coverage
  affect downstream candidate selection?
- How are clinical trials designed using AI for eligibility
  filtering or site selection assessed for representation
  effects?
- Where do post-marketing real-world evidence efforts pick
  up the inequities introduced earlier in the pipeline?

## Limits of post-hoc fairness fixes

Ghassemi, Naumann, and Pierson (2021) argue that current
explainable AI approaches do not deliver what clinical
users need. Several authors have made parallel arguments
about post-hoc fairness adjustments: a model that has
already absorbed biased training signal cannot be reliably
re-fairened by tuning a threshold per subgroup.
Rajkomar and colleagues (2018) frame fairness for clinical
ML as a matter of design choices made across the pipeline,
not at a single tuning step. Chen, Joshi, and Ghassemi
(2020) argue for treating disparity reduction as a primary
design objective in healthcare AI.

### System lessons

- Address fairness at the data, label, and design stages,
  not only at the prediction-threshold stage.
- Report subgroup performance alongside aggregate
  performance.
- Treat bias auditing as an ongoing monitoring duty, not a
  one-time exercise.

## Limitations and cautions

- Equity discussions in this repository draw on published
  cases; they are not audits of any specific deployed
  system.
- Subgroup analyses on synthetic or public data illustrate
  methods, not population effects.
- Fairness frameworks differ; this note does not adjudicate
  between them.
