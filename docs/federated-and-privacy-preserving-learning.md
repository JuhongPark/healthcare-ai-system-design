# Federated and privacy-preserving learning

Notes on federated learning, differential privacy, and
related approaches to training models across institutions
without centralizing patient data.

## Why this matters

Healthcare data are partitioned across institutions, with
strong legal and ethical reasons to keep them partitioned.
Federated learning, secure computation, and differential
privacy are families of methods that try to combine
learning across institutions without combining the data
itself. None of them is a complete solution; together they
shape what multi-institution learning can look like.

## Federated learning

Federated learning, as introduced by McMahan and colleagues
(2017), trains a shared model across decentralized data by
exchanging model updates rather than raw data. Rieke and
colleagues (2020) and Sheller and colleagues (2020) frame
the case for federated learning in healthcare and report
multi-institutional collaborations. Pati and colleagues
(2022) report on the FeTS effort for rare-cancer boundary
detection across many sites.

### Open questions

- How are non-IID data across institutions handled, and how
  is performance reported per site?
- What is the smallest useful federated setup for a given
  question, given coordination and engineering overhead?
- How are subgroup-fairness audits conducted in a federated
  setting where the auditor cannot see the data?

## Differential privacy

Differential privacy gives a formal definition of how much
an individual record can affect a model output. The
foundations are surveyed in Dwork and Roth (2014); medical
imaging applications are reviewed in Kaissis and colleagues
(2020). Privacy budgets, noise mechanisms, and utility
trade-offs remain active research questions in clinical
settings.

### Open questions

- How are privacy budgets chosen for clinical use, and how
  are they communicated to users and regulators?
- How does differentially private training interact with
  subgroup performance, and where do small subgroups suffer
  most?
- What is the relationship between formal differential
  privacy guarantees and the kinds of re-identification
  risks hospitals actually worry about?

## Combinations

Many real proposals combine federated learning with
differential privacy, secure aggregation, or trusted
execution environments. Each combination has different
threat models and different operational costs. Single-site
hospitals adopting these methods face an additional layer
of governance and engineering work.

### Open questions

- For a given hospital, what does the path from no
  federated capability to a single multi-site collaboration
  realistically look like?
- How are model updates audited across institutions when
  no single party sees all the data?
- How is consent designed when patients' data influence a
  model that lives outside the institution that captured
  the data?

## Limitations and cautions

- Privacy guarantees depend on assumptions about
  adversaries and infrastructure. Stated guarantees do not
  transfer if those assumptions change.
- Federated and differentially private experiments on
  public datasets illustrate methods; they do not
  establish that a particular hospital deployment will
  deliver the same trade-offs.
- Privacy-preserving language can mislead if the
  underlying assumptions are not stated alongside the
  claims.
