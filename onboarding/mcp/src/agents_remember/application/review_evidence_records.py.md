# mcp/src/agents_remember/application/review_evidence_records.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The complete owner-produced record collection for one review** (`ICR-R14@v1`), and nothing else. A
review has five collections — the curator authority's published **assessments**, the detection owner's
**signals**, the evidence owner's **verification observations** and **evidence claims**, and the review
matrix's **authored effects** — plus one quantity nobody in this composition measures (**dependency
currentness**). Before this module the production port supplied only the assessments and reported every
other collection as an empty tuple, which is what the F09 defect was: an omission with three faces
(signals, observations and measurement inputs never supplied; "the authority published none" and "the
authority could not be read" collapsed into one empty tuple).

This module resolves all of them for one resolved candidate through **each owner's own read operation**
and hands them over as the bundle the surface renders. It produces no record, re-derives no owner's
content and decides nothing.

**Availability is a fact per collection, and an empty tuple never stands for three different ones.**
Every collection carries a
[`ReviewRecordChannel`](../models/knowledge/review_records.py.md) naming the state its owner's answer
earned — `recorded` / `none_recorded` (the owner answered), `unavailable` (expected content that could
not be read, with the owner's own refusal as provenance), `not_measured` (a quantity nothing measured)
and `not_selected` (a collection this composition never read). A loader failure is therefore never
reported as "no records ever existed", and no channel reports a positive it did not measure: an
unreadable authority carries **no count** rather than a zero.

**One collection that cannot be read does not withdraw the others.** Every read is guarded per
collection, and inside the two multi-record collections the guard is per **record**: a damaged
detection run, or a claim whose stored payload no longer decodes, is named on its channel
(`unreadable`) while its siblings are still supplied. That is the packet's failure behavior, and it is
why this module reads the two listable collections one record at a time through the owner's own
single-record reader rather than through an all-or-nothing enumerator.

**What this module deliberately does not do.** It does not filter records by subject or generation
(`ICR-R26@v1` owns applicability classification), it does not measure dependency currentness
(`ICR-R15@v1` owns that measurement, and the currentness channel names it rather than guessing), and
it never re-runs detection, executes a command or authors anything.

## Code Commentary

### Logic

`review_records_for_resolution` accepts the already resolved source/knowledge pair, so capture does not resolve a second candidate while collecting records. Assessments and immutable artifact references come from `review_curator_records`; detection, execution, claims, effects, applicability and currentness retain their existing owners. A historical collection never follows the current curator pointer.

**`review_records_for` is the whole production entry point, and it resolves the candidate exactly as
the surface resolves it.** `resolve_review_candidate` is called with the same request, so the records a
caller is handed belong to the comparison the same request renders. A candidate that does **not**
resolve supplies no records and states that fact per collection (`_unresolved_channels`), rather than
five empty tuples: the surface refuses that request, and a bundle claiming an absence would report an
unresolvable candidate as a candidate with no records. `review_records_for_resolution` assembles the owner collections for that exact resolved pair and delegates currentness measurement to its existing owner.

**Assessments retain the curator owner's identity and artifacts.** The dedicated `review_curator_records` bridge reads the current authority for a live comparison and only the comparison-bound immutable generation for recorded history. The complete assessment channel and owner artifacts travel with the record inputs; unavailable or uncaptured history does not withdraw other readable channels.

**Detection signals are read run-by-run, and the run listing is the detection owner's own.** The
signals a review should carry have to be addressed by run, so `recorded_run_ids` lists the identities
and each one is read through the shipped `read_detection_run` — no second reader of the same tables.
`_read_signal_runs` guards **each** run: the detection owner reports a damaged revision by *raising*
(recomputing the stored seal), so an unguarded loop would let one damaged run withdraw the channel
before `_signal_channel` could name it. `_DAMAGED_RECORD_ERRORS` is the one declaration of what "a
record this composition cannot serve" means (`KnowledgeStorageError` for a seal/row refusal,
`ValidationError` for a payload that no longer parses). `_signal_channel` then distinguishes three
states: no run recorded at all is a measured zero, **all** runs unreadable is `unavailable` (with the
identities named), and a partial read is `recorded` with the unreadable identities named in the detail.

**Observations are selected by both halves of the candidate's own binding.** `_observations` opens the
candidate side, builds an `ObservationCandidateSeed` naming the candidate dataset's logical digest
**and** the captured code tree, and reads through the shipped application seam
`knowledge_evidence.read_evidence_scope`. An observation recorded against a foreign candidate tree is
therefore *not* selected — the collection is the candidate's own binding, not a namespace listing.
`_observation_refusal` turns the evidence owner's `selector_absent` code into a measured zero and every
other refusal (absent dataset, unreadable snapshot, a selection past its bound) into `unavailable`
carrying that refusal's own code, detail and next action.

**Evidence claims are the evidence owner's complete collection, read one record at a time.** The
matrix page selects *which* claims a subject reaches; this collection is what the candidate *records*.
`claim_ids` lists the identities without decoding them and each is read through `claim_record` +
`claimed_coverage_of_claim` under the same per-record guard, so a claim whose envelope, payload or
coverage cannot be read is named while its siblings are supplied. `_claim_record` renders one claim's
own authored fields — the admission's actor as `author_ref`, the record's `state_at_origin` as
`lifecycle`, the declared `limitations` verbatim, and the asserted coverage endpoints as
`kind:identity` strings via `coverage_identity` — and derives nothing.

**The two matrix-owned collections arrive from the matrix's own answer, not from a listing.**
`with_selection_channels` is called by the two compositions *after* they have read (or deliberately not
read) the review matrix: a review that selected a subject reports what the view returned, including how
many rows the view declared beyond the page it rendered (`_remaining_note`), and a review that selected
no operand reports `not_selected` — "the review did not ask", which is a different fact from an owner
answering that it holds none. `_SELECTION_KINDS` declares the kinds each matrix collection selects, so
the channel that counts a collection and the pane that renders it cannot come to disagree.

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
than which code path happened to run. `_answered` is the owner-answered pair (`recorded` with a count,
or `none_recorded` with a real zero); `_absent`, `_unavailable` and `_not_selected` are the three
non-answers, and only `_unavailable` takes unreadable identities.

**An absent or unopenable candidate dataset is unavailability, never an empty collection.**
`_open_candidate_store` and `_candidate_context` catch the storage open failure and `apsw`'s own error
as well, so a file that exists and cannot be read reaches the caller as a state instead of an
exception, and both name the same next action (place the dataset, then reopen).

### Conventions

`__all__` publishes four names: `AUTHORED_EFFECT_KINDS`, `EVIDENCE_CLAIM_KINDS`, `review_records_for`
and `with_selection_channels`. `AUTHORED_EFFECT_KINDS` **moved here from the review adapter** and is
imported back by it, which is deliberate: the kinds a channel counts and the kinds a pane renders are
one declaration, so they cannot drift. The module declares one dataclass of its own (`_Answer`, a
private value) and one frozenset pair; every value it returns is a shipped type from
`models/knowledge/review.py`, `models/knowledge/detection.py` or
`application/review_record_rendering.py`. It holds no state, writes nothing and opens only the
candidate's own dataset read-only.

### Invariants And Boundaries

- **One responsibility: which owner-produced records does this review carry, and what did each owner's
  answer mean.** The module reads; it never produces, filters or judges.
- **Availability is per collection and never inferred from a collection's length.** The channel is
  computed from the read's own answer, and the model refuses a count on a state that measured none.
- **A damaged record is named, never fatal and never silently dropped.** The guard is per record for
  the two multi-record collections.
- **No favourable default exists in this vocabulary.** No state means "nothing to worry about"; an
  unreadable authority has no count and an unmeasured assessment remains explicitly not measured.
- **The owners keep their collections.** Signals come from the detection owner's read, observations
  and claims from the evidence owner's, assessments from the curator authority's publication, authored
  effects from the review matrix — and no owner's content is re-derived here.
- **Nothing is selected by subject.** Records for other subjects arrive unfiltered; classifying them is
  `ICR-R26@v1`'s applicability decision, which is why this module adds no isolation claim.
- **It does not restate the task-context composition's rule.** A task-context review passes
  `selected=False`; this module states the state and lets the composition say why.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the two owner
recipes it adds (`detection.recorded_run_ids`, `evidence_records.claim_ids`), in the channel vocabulary
it carries, in the two compositions that call it, and in the ten cases that drive it through the
production port. Three details a reader should carry: **the bundle's states are the owners' own
answers** rather than a convention this module invented; **the per-record guard is what makes the
partial-collection states reachable at all**; and the currentness channel is the one entry this
composition deliberately leaves unmeasured.

- The module's own statement of what it owns, the five availability facts, the per-collection isolation and the three responsibilities it leaves to R26, R15 and the owners. [1]
- The published surface, and the one declaration of what "a record this composition cannot serve" means. [2]
- **The record kinds the authored-effects channel counts, moved here beside the channel that reports them, and the same declaration for the claims collection.** [3]
- **Every collection with the owner whose read answers for it — the pointer a reader of an absent collection follows — and the five collections plus the measurement, in the order they are read.** [4]
- **The currentness owner the bundle names, and the measurement this module now delegates instead of stating.** [5]
- The two matrix-sourced collections, declared as kinds so the channel and the pane cannot disagree, and the next action an unopened dataset earns. [6]
- **The production entry point: same candidate resolution as the surface, and an unresolvable candidate reported per collection rather than as five empty tuples.** [7]
- The assembly of one resolved candidate's bundle: four collections read, one measurement stated. [8]
- **The two matrix-owned channels, added where the matrix's own answer is, with `not_selected` for a review that never asked and the view's declared row bound carried through.** [9]
- Assessment collection availability comes from the durable curator bridge: captured records, measured empty, uncaptured, and unreadable expected inputs remain distinct. [10]
- **The detection collection read through the owner's own run reader, over the identity listing the owner exposes.** [11]
- **The three states of a partly readable collection: no run recorded, all runs unreadable, or a supplied subset with the unreadable identities named.** [12]
- **The per-record guard that makes a damaged run survivable: one identity named, its siblings still supplied.** [13]
- **The observation collection selected by both halves of the candidate's own binding, so a foreign candidate's observation is not selected.** [14]
- **The evidence owner's own `selector_absent` as a measured zero, and every other refusal as unavailability carrying its code and next action.** [15]
- **The claims collection as the owner's complete one, read one record at a time so a damaged claim is named and its siblings served.** [16]
- **One claim's authored fields rendered verbatim: author from the admission, lifecycle from the record, declared limitations and asserted coverage as recorded.** [17]
- The candidate read context, and the absent or unopenable dataset reported as unavailability rather than as an empty collection. [18]
- **The unresolvable-candidate bundle: every collection unavailable, one entry per class, because nothing resolved and so no owner was asked.** [19]
- The one channel construction point: the answer varies, the owner does not. [20]
- The four non-answer states and the two notes that keep a partial or bounded collection truthful. [21]
- One unavailability statement: what failed, under which owner status, in the owner's own words. [22]
- **The availability vocabulary this module builds, and the validator that makes "a count nobody measured" unrepresentable.** [23]
- **The subject composition's own call site: it adds the two matrix-owned channels where the matrix's answer is, and reports the view's declared row bound.** [24]
- **The task-context composition's call site: no matrix was read, so the matrix-owned collections are reported `not_selected`.** [25]
- **The production port this bundle is read through, and the adapter's re-export of the resolver so the port keeps resolving without a new home to learn.** [26]
- **The channel list as part of the served payload, one entry per class the composition read.** [27]
- **The ten cases that drive this module through the production port, including the two per-record damage cases.** [28]

The following declarations carry the changed boundary.

- All owner records are collected for the already resolved comparison pair. [29]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one candidate's own dataset and its
enclosure's own curator authority and touches no repository boundary.

No meaningful cross-repo references found.

## 260921-ICR-L10 A Stated Remainder Always Names The Action That Reaches It

`260921-ICR-L10` (`ICR-R10@v1`) makes the matrix channels tell the truth about a page. The
channels now take a `MatrixSelection` — the published page **only when it is this collection's page**,
the owner's own remainder, and any refusal — so a sentence about a bound always names the way to reach
it: when the request paged the comparison, the note names the request that does reach the records
(`pageOf=records`) instead of claiming a cursor that continues the comparison, and a refused read is
reported `unavailable` rather than as a measured zero.

The task-context branch is now the extracted `without_selected_matrix`, the one implementation of "this
review read no matrix", which is why `review_task_context.py` calls it rather than repeating the
construction.

## 260921-ICR-L26 The Claim's Own Recorded Subject Travels With It

`260921-ICR-L26` (`ICR-R26@v1`) extends this owner's renderer input by **exactly one field**, so a
claim can be attributed to a subject instead of being displayed unattributed: `_claim_records` now reads
`evidence_records.subject_of_claim(store, claim_id)` beside the record and its coverage, and
`_claim_record(record, coverage, subject)` renders `ReviewClaimRecord.subject_revision_id` from it.
**840 → 862 lines.**

**The subject is the invariant revision or it is nothing.** `_claim_subject_revision` returns the exact
revision id only when the owner's own subject edge records an `invariant_revision`; a facet-revision
subject is a different kind of identity and the review's selected subject is never a facet, so it is
reported as the absence it is rather than narrowed into an invariant revision id. An absent subject is
never filled with the candidate's or the selection's identity — the classifier reads the absence and
reports the record unresolved, which is the honest state rather than a guess.

**Nothing else about this owner changed.** The complete collections, the channels, the damaged-claim
handling and every authored field travel exactly as before: this leaf adds a reader of the claim's own
subject edge to the introducer's contract by its consumer, which is the seam rule for extending a
bundle rather than reading around its owner.

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
