# mcp/src/agents_remember/application/review_evidence_records.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Composes review evidence from the selected candidate's published curator assessments, retained artifacts and measured binding currentness.

## Code Commentary

A resolved candidate reads the immutable curator authority and its artifact references. The returned channels distinguish an assessment collection from the currentness measurement of its exact dependency binding. Canonical detection, verification-observation and evidence-claim collections are retired and explicitly unavailable; they are not measured empty. Authored effects are unavailable with their removal as the reason: the review matrix left with the retired envelope tables (MIK-R74 rule 1), so no review reads it now. An unresolved candidate yields unavailable channels. The removed `_claim_record` projection is not a current reader.

### Logic

**`review_records_for` is the whole production entry point, and it resolves the candidate exactly as
the surface resolves it.** `resolve_review_candidate` is called with the same request, so the records a
caller is handed belong to the comparison the same request renders. A candidate that does **not**
resolve supplies no records and states that fact per collection (`_unresolved_channels`), rather than
five empty tuples: the surface refuses that request, and a bundle claiming an absence would report an
unresolvable candidate as a candidate with no records. `review_records_for_resolution` assembles the owner collections for that exact resolved pair and delegates currentness measurement to its existing owner.

**Assessments retain the curator owner's identity and artifacts.** The dedicated `review_curator_records` bridge reads the current authority for a live comparison and only the comparison-bound immutable generation for recorded history. The complete assessment channel and owner artifacts travel with the record inputs; unavailable or uncaptured history does not withdraw other readable channels.

**The currentness channel was a constant here, and this leaf replaced it with a real measurement.** At
this card's previous reading the module stated the collection `not_measured` from a constant
(`_CURRENTNESS`) and supplied no measurement of its own. `260921-ICR-L15` (`ICR-R15@v1`) deleted that
constant: the composition now takes the measurement of the comparison it is viewing from
`review_assessment_currentness.comparison_currentness_measurement`, and
`_COLLECTION_OWNERS["assessment_currentness"]` names that module's own `CURRENTNESS_OWNER`. The module
still supplies **no measurement of its own** — and uncaptured historical assessments retain `not_measured` even when source identities are measurable. The channel therefore states one of
`recorded` / `none_recorded` / `unavailable`, and an assessment this comparison publishes no value for is
reported `not-measured` on its own display rather than promoted to current.

**Every state is built through one channel constructor.** `_Answer` carries the varying half (state,
detail, count, unreadable identities, next action) and `_channel` attaches the owner from the single
`_COLLECTION_OWNERS` declaration, so a channel's `owner` names **which authority to look at** rather
than which code path happened to run. `_answered` selects the owner-answered pair: `_recorded` carries a measured count, while
`_absent` carries `none_recorded` with a real zero. `_unavailable` is the count-free non-answer.
Both `_recorded` and `_unavailable` may name unreadable identities. The two removal constructors state unavailability with
its reason: `_removed_matrix_channel` for authored effects (the matrix left with the retired envelope
tables, MIK-R74 rule 1) and `_retired_channel` for the three retired canonical classes (no writer or
record format on a converted tree, MIK-R26).

### Invariants And Boundaries

- **One responsibility: which owner-produced records does this review carry, and what did each owner's
  answer mean.** The module reads; it never produces, filters or judges.
- **Availability is per collection and never inferred from a collection's length.** The channel is
  computed from the read's own answer, and the model refuses a count on a state that measured none.
- **No favourable default exists in this vocabulary.** No state means "nothing to worry about"; an
  unreadable authority has no count and an unmeasured assessment remains explicitly not measured.
- **Nothing is selected by subject.** Records for other subjects arrive unfiltered; classifying them is
  `ICR-R26@v1`'s applicability decision, which is why this module adds no isolation claim.

## Evidence

### Repo-Internal References

- Three collection owners are retired canonical records (MIK-R26): `detection_signals`, `verification_observations` and `evidence_claims` name retired-canonical records and are unavailable through `_retired_channel`; `assessments` and `assessment_currentness` have live owners, and `authored_effects` is unavailable through `_removed_matrix_channel` — the matrix left with the retired envelope tables (MIK-R74 rule 1). [42]

- `review_records_for_resolution` owns the current boundary described above. [30]
- `_retired_channel` owns the current boundary described above. [31]
- `_removed_matrix_channel` owns the current boundary described above. [32]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The authored-effects channel states the removal, not a count:** `_removed_matrix_channel` reports `unavailable` with the rule-1 removal as its reason and no count, and the knowledge pane carries no such collection. [33]
- **The currentness owner the bundle names, and the measurement this module now delegates instead of stating.** [34]
- Assessment collection availability comes from the durable curator bridge: captured records, measured empty, uncaptured, and unreadable expected inputs remain distinct. [35]
- **The unresolvable-candidate bundle: every collection unavailable, one entry per class, because nothing resolved and so no owner was asked.** [36]
- The one channel construction point: the answer varies, the owner does not. [37]
- **The availability vocabulary this module builds, and the validator that makes "a count nobody measured" unrepresentable.** [38]
- **The task-context composition carries the same bundle: the matrix-owned collections are unavailable with their removal or retirement as the reason, never a measured zero.** [39]
- **The channel list as part of the served payload, one entry per class the composition read.** [40]
- All owner records are collected for the already resolved comparison pair. [41]

## 260921-ICR-L10 A Stated Remainder Always Names The Action That Reaches It (retired with the matrix)

`260921-ICR-L10` (`ICR-R10@v1`) made the matrix channels tell the truth about a page through
`MatrixSelection` and the extracted `without_selected_matrix`. Both left with the review matrix
that read the retired envelope tables (MIK-R74 rule 1): no records page exists, no records cursor
is admitted, and the removed collection earns the `comparison_page_unreadable` refusal instead of a
walk. Retained here as the history of the remainder rule, not as current machinery.

## 260921-ICR-L12 The Record Bundle Is Read For The Record The Request Named

`260921-ICR-L12` (`ICR-R12@v1`) adds one argument to this module's resolution and changes nothing
else: `review_records_for` now resolves with `recorded=request.history == "recorded"`, so a review of a
leaf's **recorded** comparison is handed the records of that same recorded pair rather than of whatever
the leaf holds now. The distinction is the module's own subject applied to a second question: the
records a caller is handed must belong to the comparison the same request renders, and a bundle read
from the live pair under a recorded request would attribute records to a comparison they were not
measured against.

The bundle's own rules are untouched: availability is still a fact per collection, an empty tuple still
never stands for three different ones, and an unresolved candidate still supplies no records and says
so per collection rather than claiming an absence.
