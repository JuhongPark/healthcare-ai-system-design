# Hospital systems design

Notes on hospitals as sociotechnical systems and how AI fits
into the broader picture beyond a single point-of-care model.
The unit of analysis here is the hospital, not the model.

## Why hospitals

Decision support tools, predictive risk scores, and
clinician-facing interfaces all live inside larger hospital
systems: clinical information systems, operational pipelines,
governance structures, and vendor relationships. A model that
ignores its host hospital is a demo, not a deployment. Many of
the failure modes described elsewhere in this repository —
workflow mismatch, alert fatigue, dataset shift, unclear
accountability — surface when a model meets a hospital that
was not designed to receive it.

## Information systems

The electronic health record is one component of a wider
information landscape. Admit-discharge-transfer (ADT) systems,
laboratory information systems, picture archiving and
communication systems (PACS), pharmacy systems, and revenue
systems each have different update cadences, schemas, and
ownership. A research dataset is the result of stitching
several of these together, often through interfaces that were
not designed for analytic use.

Interoperability standards (HL7 v2, FHIR, the OMOP common
data model) determine what can be combined within a hospital
and across hospitals. Coding standards (ICD-10, SNOMED CT,
LOINC, RxNorm) shape what is recorded and how it can be
queried. These standards are not fixed: their adoption varies,
and local conventions shape what each code actually means at
a given site.

### Open questions

- Where does data quality break down between source system
  and research dataset, and where is that documented?
- Which interoperability standards are stable enough to design
  on, and which are still moving?
- How are extract and transform pipelines maintained when
  source systems change underneath them?
- How do local coding conventions diverge from nominal
  standards, and how is that reconciled in multi-site work?

## Patient flow and operations

Emergency department arrivals, admissions, transfers,
discharges, operating room scheduling, and bed management
form flow problems with capacity constraints. Staffing levels,
shift handovers, and on-call structure shape how decisions are
actually made. Operational AI in this context — for example,
length-of-stay prediction, no-show prediction, surge
forecasting — sits inside scheduling and capacity decisions
that have many human inputs.

### Open questions

- When can predictive models for length-of-stay, readmission,
  or no-show meaningfully change operational decisions, and
  when are they routed around?
- How are operational AI systems evaluated when their outputs
  feed human scheduling rather than acting directly?
- How do operational metrics (throughput, occupancy) interact
  with clinical metrics (safety, outcomes) when both are
  affected by the same model?
- What does fairness look like for an operational model whose
  errors have different consequences for different patients?

## Hospital-scale AI integration

A hospital deploying multiple AI models faces portfolio
problems that the single-model literature rarely addresses.
Who maintains an inventory of deployed models? Who owns
updates and pauses? When two models give conflicting outputs
at the same bedside, how is that resolved? When a single
patient encounter is touched by several models in sequence,
how are the cumulative effects tracked?

Workflow integration also has to work across services and
shifts, not only at the moment of demonstration. A model that
is well-integrated for the day team may be invisible to the
night team.

### Open questions

- What does a hospital-level AI inventory look like, and who
  maintains it?
- How are conflicting outputs from different models reconciled
  at the bedside?
- How are downstream cumulative effects of multiple models on
  a single patient trajectory tracked?
- What does shift-spanning workflow integration require beyond
  what point-of-care interface design covers?

## Privacy, security, and access control

Hospital data infrastructure carries identity, audit, and
access control requirements that pure ML pipelines often
ignore. De-identification is rarely complete; combination
with external data can re-identify patients. Audit logs need
to be designed at the hospital-system layer, not only the
model layer. Vendor access, research access, and clinical
access each have different rules.

### Open questions

- What is the smallest useful audit footprint for a single
  AI integration?
- How are access controls maintained across the data
  lifecycle from clinical capture to research use to vendor
  analytics?
- How are breach notification and incident response designed
  for AI systems specifically?
- Where do hospital data protection responsibilities end and
  vendor responsibilities begin?

## Hospital governance for AI

Many hospitals now stand up internal AI governance
committees; their authority, scope, and composition vary.
Hospital governance interacts with vendor governance,
regulator governance, and payer policy. A clear escalation
and retirement path is the practical expression of
governance.

### Open questions

- What does a minimum viable hospital AI governance committee
  look like at a single site?
- How does hospital governance relate to the SaMD-style
  regulatory governance covered in the monitoring and safety
  notes?
- Which decisions stay with the local validator, and which
  go upstream to the developer or vendor?
- How are model retirement criteria written so that a stale
  system actually gets retired?

## Process mining for clinical pathways

Process mining methods extract event logs from clinical
information systems and reconstruct the actual paths
patients take through care, distinct from the paths that
guidelines or care maps describe. Mans, van der Aalst, and
Vanwersch (2015) collect the methodology and applications;
Rojas and colleagues (2016) review the healthcare
literature. The method is interesting at the
hospital-system layer because the same data underlying
operational dashboards can be used to discover where
pathways diverge from intent.

### Open questions

- Which event-log sources at a hospital are usable for
  process mining without bespoke extraction work?
- How are deviations from documented care pathways
  attributed to clinical reasoning versus operational
  constraints?
- How should process-mining outputs be presented to
  clinical and operational audiences who use different
  vocabularies?

## Telehealth integration

Telehealth changed the encounter envelope in ways that are
still being absorbed by hospital information systems and AI
deployments. Webster (2020) frames the immediate
acceleration during the COVID-19 pandemic; subsequent
literature debates which changes will persist. The relevant
question for systems design is what data is captured during
a telehealth encounter, how it flows into the same EHR
infrastructure as in-person care, and how AI systems
trained on in-person data behave on telehealth-generated
records.

### Open questions

- How are telehealth encounters represented in the same
  data structures as in-person encounters, and where do
  schemas diverge?
- What does data drift look like when an AI model trained
  on in-person encounters meets a population whose recent
  encounters were largely telehealth?
- How are quality and safety metrics defined for AI
  systems whose inputs include teleconsultation data?

## Cybersecurity

Hospital cybersecurity is a system-wide concern that
affects whether AI components can be relied on at all. A
ransomware event that takes the EHR offline removes the
data feed that an AI system depends on; a compromised
endpoint is also a compromised AI input. Coventry and
Branley (2018) review the threat landscape and the
particular weaknesses of healthcare environments.

### Open questions

- How are AI systems explicitly included in incident
  response and recovery plans?
- How is the integrity of model inputs and outputs assured
  when source systems may be compromised?
- What is the smallest useful continuity plan for a
  hospital-deployed model when its data feeds are
  unavailable?

## Limitations and cautions

- Discussion is descriptive, not prescriptive policy.
- No assumption is made about a particular health system,
  vendor, or jurisdiction.
- Examples are public, synthetic, or simulated. No
  hospital-internal documents and no proprietary architecture
  details are used.
- Hospital governance descriptions reflect general patterns
  in the literature, not any specific institution.
- Cybersecurity discussion is high-level orientation, not
  a security recommendation for any environment.
