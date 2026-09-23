# mcp/src/agents_remember/application/review_assessment_currentness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_assessment_currentness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T12:00:00+02:00 |
| lastVerifiedCommitHash | `e605822eb3bf83bf63a45963c5f51d5fc28859ee` |
| lastVerifiedCommitDate | 2026-09-23T12:19:01+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

**`currentness_channel` states the measurement's availability, and a resolved candidate has exactly three
product states.** `unavailable` — the assessment authority could not be read, so nothing was measurable,
carrying that authority's own reason; `none_recorded` — the authority answered and records no assessment,
so there was no binding to measure (a measured zero, not an absence of an answer); `recorded` — a
measurement was performed, with the number of stored bindings it was compared against and the declared
identities it holds no value for named in `unreadable`, so a partial measurement is stated rather than
absorbed. `not_measured` is deliberately **not** among them: the composing read always measures a resolved
candidate, a bundle nobody measured carries no channels at all, and rendering one here would state a
comparison that never happened. That contract is asserted rather than guessed at, in the shipped style of
an operation's own precondition.

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the shipped
comparison it delegates to, and in the records model whose channel it builds.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the defect it closes, the three questions it answers, and the owner boundary it refuses to cross. | `comparison_currentness_measurement`; `currentness_channel` | mcp/src/agents_remember/application/review_assessment_currentness.py:1-38; mcp/src/agents_remember/application/review_assessment_currentness.py:82-181 |
| The published surface, and the one declaration naming which authority answers for this collection. | `__all__`; `CURRENTNESS_OWNER` | mcp/src/agents_remember/application/review_assessment_currentness.py:59-63; mcp/src/agents_remember/application/review_assessment_currentness.py:65-68 |
| **The measurement: the identities the viewed comparison publishes, read from the resolution, with the two validator identities appended unconditionally — which is why its state is always `measured`.** | `comparison_currentness_measurement`; `_SCOPE_MANIFEST`; `_COMPARISON` | mcp/src/agents_remember/application/review_assessment_currentness.py:82-122; mcp/src/agents_remember/application/review_assessment_currentness.py:78-79 |
| **The availability statement: the three product states a resolved candidate can earn, and the assertion that a measurement nobody performed has no channel here.** | `currentness_channel` | mcp/src/agents_remember/application/review_assessment_currentness.py:125-181 |
| The count that says how many bindings were *compared*, and the per-binding not-measured statement. | `_measured_detail`; `_unmeasured_spellings` | mcp/src/agents_remember/application/review_assessment_currentness.py:184-199; mcp/src/agents_remember/application/review_assessment_currentness.py:202-211 |
| The one unavailability construction, carrying its own reason and remedy. | `_unavailable`; `_REPAIR_ACTION` | mcp/src/agents_remember/application/review_assessment_currentness.py:214-226; mcp/src/agents_remember/application/review_assessment_currentness.py:70-73 |
| **The measurement value and the vocabulary it is built from — the state, the values whose keys are the coverage, and the unmeasured remainder.** | `AssessmentCurrentnessMeasurement`; `measured_currentness` | mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:224-247; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:271-296 |
| **The whole equality rule this module feeds but never makes: a measured disagreement is stale, a complete agreement is current, everything else — including an empty measurement — is not-measured.** | `measured_binding_status`; `measured_binding_statuses`; `unmeasured_identities` | mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:317-350; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:352-369; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:299-314 |
| The comparison's own equality authority and its declared-dependency edges, which this module supplies values for and never re-implements. | `disputed_dependencies`; `assessment_currentness` | mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:143-173; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:175-198 |
| The availability vocabulary the channel is built in, and the validator that makes "a count nobody measured" unrepresentable. | `ReviewRecordChannel`; `ReviewRecordChannelState` | mcp/src/agents_remember/models/knowledge/review_records.py:68-123; mcp/src/agents_remember/models/knowledge/review_records.py:47-66 |
| The digest the declaration builder used, reused here so a measured spelling and a declared spelling are one name. | `canonical_sha256` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:354-376 |
| The two validator identities the shipped assessment publication declares as constants — the reason a resolution binding nothing is still measurable. | `ASSESSMENT_RESOLVER_VERSION`; `ASSESSMENT_POLICY_VERSION` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:69-70 |
| **The one production caller: the record bundle produces this measurement for the comparison the review is viewing, and names this module as the collection's owner.** | `_resolved_records`; `_COLLECTION_OWNERS`; `review_records_for` | mcp/src/agents_remember/application/review_evidence_records.py:199-220; mcp/src/agents_remember/application/review_evidence_records.py:137-142; mcp/src/agents_remember/application/review_evidence_records.py:171-196 |
| The resolution whose bound endpoints and recorded references are the identities measured. | `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:121-160 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one comparison's own resolution and
touches no repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; production line at this leaf's base `3103e1142a3ded8a843c3e5bbefca14861ba4a58`): created this one-to-one card for the module this leaf introduced as `ICR-R15@v1`'s production measurement — the leaf's own answer to the packet's defect, that an absent measurement became `stale` and an empty mapping `current`, both decided from the *presence of a mapping* rather than from a measurement. The card records what the module **is**: one measurement of the identities the viewed comparison publishes, read from the comparison's own resolution and never from a store; the two validator identities appended unconditionally, which is why the state is always `measured` and why the channel's `not_measured` member was deleted in fix round 1; the recorded-generation rule that keeps a reopened review measuring its own generation rather than today's; and the exactly-three product states (`recorded` / `none_recorded` / `unavailable`) a resolved candidate can earn, with the assertion that a measurement nobody performed has no channel here. It also records the boundary the module refuses: the curator-coherence observation's own inputs are **not** re-derived, and no binding is repaired or re-judged. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — this leaf's base commit — because every construct cited here exists only in this leaf's uncommitted candidate and no commit contains the content a stamp would otherwise claim to have verified. That is a statement of what the reading was against, not a claim that these constructs exist in that commit; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp. **Citation accounting:** all ranges on this card were derived against the frozen post-fix-round candidate bytes (the module is 226 lines there), and each cited range was checked to contain the anchor's declaration line.
