# mcp/src/agents_remember/application/review_assessment_currentness.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The missing half of the assessment-currentness question for one review read** (`ICR-R15@v1`): *whether
anybody measured anything*, and what the answer means for the collection's availability.

An assessment records the exact inputs it examined, and the shipped comparison decides whether a recorded
identity still matches the value measured for it. That comparison is handed a **measurement** — it cannot
itself decide whether one was ever taken, because it has no store to consult. The review surface used to
answer that question from the **presence of a mapping**, which produced two facts the store never held: an
absent measurement rendered every stored assessment `stale`, and an empty mapping (`current={}`) rendered
every one of them `current`. The defect and the projection live in
[`review_record_rendering`](review_record_rendering.py.md), the composition in
[`review_evidence_records`](review_evidence_records.py.md), and the rule in
[`review_assessment_binding`](../models/lifecycles/review_assessment_binding.py.md).

This module owns the measurement the review read was missing — one measurement of **the identities the
viewed comparison itself publishes**, produced from the comparison's own resolution, plus the availability
statement that goes with it. It produces no assessment, authors no judgment and approves nothing.

## Code Commentary

### Logic

**`comparison_currentness_measurement` measures the identities the viewed comparison publishes, and
nothing else.** Everything it reports comes from the resolution it is handed: the two code endpoints the
resolution bound (`code-tree:baseline` / `code-tree:candidate`, algorithm `git-object`), the leaf's
scope-manifest reference (the leaf identity, digested by the same `canonical_sha256` the declaration
builder used), the enclosure comparison reference, and the two validator versions the shipped assessment
publication declares as constants. Each is a name an assessment declares, so the names compared are the
*same* names — a second spelling here would compare two identities that never meet.

**A resolution that binds nothing still publishes two identities, so the state is always `measured`.**
The two validator versions are appended unconditionally, which is why the measurement's own docstring now
states that its state cannot be `not-measured` (the leaf's fix round 1 deleted the branch that had claimed
otherwise). What varies between resolutions is only **how many** identities the measurement holds — both
endpoints and the two recorded references for a resolved live comparison, fewer for a caller-assembled
pair. An identity outside that list is reported `not-measured` **by the projection**, rather than being
read as agreement; that is the whole reason the measurement's keys are its coverage.

**The recorded generation is the one the resolution bound.** A review reopened from a leaf's durable record
measures its assessments against *that* generation's endpoints; a live review measures them against the
candidate captured now. Selecting between the two is the resolution's own explicit choice
(`history == "recorded"`, `ICR-R12@v1`) and is never a fallback here.

**Assessment collection availability determines whether any binding could be measured.** A historical collection that was never captured is `not_selected`, so its currentness channel is `not_measured`. Source identities may still be measurable; they do not turn an uncaptured collection into measured absence. An owner-confirmed empty collection remains `none_recorded`, failed authority remains `unavailable`, and a captured collection with measurement remains `recorded` with uncovered axes explicit.

**The count is bindings compared, not bindings current.** `_measured_detail` counts how many stored
bindings the measurement was compared against and how they fell (`current` / `stale` / `not-measured`); an
assessment whose declaration this comparison cannot cover is reported `not-measured` on its **own**
display, and the channel states how many were compared rather than how many matched.

### Conventions

`__all__` publishes three names: `CURRENTNESS_OWNER`, `comparison_currentness_measurement` and
`currentness_channel`. `CURRENTNESS_OWNER` is one declaration naming **which authority to look at**, so a
reader of the channel learns which code path answered rather than which one happened to run. The module
holds no state, performs **no I/O** (so its measurement cannot fail halfway), opens no store and writes
nothing. It imports the equality authority from the shipped model and the two validator constants from the
assessment publication — it re-spells neither. `_SCOPE_MANIFEST` and `_COMPARISON` declare the two
`evidence-bytes` identities in one place, so the measured name and the declared name cannot drift.

### Invariants And Boundaries

- **A measurement is a fact, and its absence is not a clearance.** The vocabulary has no favourable
  default: an empty measurement covers nothing and therefore marks nothing current.
- **The equality decision is not made here.** The shipped comparison stays the single authority; this
  module supplies the values it is compared against and never decides equivalence.
- **Partial coverage is stated, never absorbed.** Identities the comparison publishes no value for are
  named in `unreadable` and reported `not-measured` per binding.
- **It does not re-run the curator-coherence observation.** The pair identity, registered topology
  fingerprint, task-intent digest and memory candidate tree are that observation's own inputs;
  re-deriving them in a review read would be a second implementation of an existing owner. They are
  reported as identities this comparison publishes no value for.
- **Nothing is repaired, re-pointed or re-judged.** A moved input is a fact to report, and recovery is a
  new authored assessment through the existing publication path.
- **One implementation, one caller.** The measurement is called by the record adapter and by nothing else;
  the adapter and the projection delegate to it rather than repeating it.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the shipped
comparison it delegates to, and in the records model whose channel it builds.

- The module's own statement of the defect it closes, the three questions it answers, and the owner boundary it refuses to cross. [1]
- The published surface, and the one declaration naming which authority answers for this collection. [2]
- **The measurement: the identities the viewed comparison publishes, read from the resolution, with the two validator identities appended unconditionally — which is why its state is always `measured`.** [3]
- **The availability statement: the three product states a resolved candidate can earn, and the assertion that a measurement nobody performed has no channel here.** [4]
- The count that says how many bindings were *compared*, and the per-binding not-measured statement. [5]
- The one unavailability construction, carrying its own reason and remedy. [6]
- **The measurement value and the vocabulary it is built from — the state, the values whose keys are the coverage, and the unmeasured remainder.** [7]
- **The whole equality rule this module feeds but never makes: a measured disagreement is stale, a complete agreement is current, everything else — including an empty measurement — is not-measured.** [8]
- The comparison's own equality authority and its declared-dependency edges, which this module supplies values for and never re-implements. [9]
- The availability vocabulary the channel is built in, and the validator that makes "a count nobody measured" unrepresentable. [10]
- The digest the declaration builder used, reused here so a measured spelling and a declared spelling are one name. [11]
- The two validator identities the shipped assessment publication declares as constants — the reason a resolution binding nothing is still measurable. [12]
- **The one production caller: the record bundle produces this measurement for the comparison the review is viewing, and names this module as the collection's owner.** [13]
- The resolution whose bound endpoints and recorded references are the identities measured. [14]

The following declarations carry the changed boundary.

- Uncaptured assessment history stays not-measured rather than empty or current. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one comparison's own resolution and
touches no repository boundary.

No meaningful cross-repo references found.
