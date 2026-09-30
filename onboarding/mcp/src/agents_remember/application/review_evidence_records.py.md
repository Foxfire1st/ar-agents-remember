# mcp/src/agents_remember/application/review_evidence_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_evidence_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076` |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the two owner
recipes it adds (`detection.recorded_run_ids`, `evidence_records.claim_ids`), in the channel vocabulary
it carries, in the two compositions that call it, and in the ten cases that drive it through the
production port. Three details a reader should carry: **the bundle's states are the owners' own
answers** rather than a convention this module invented; **the per-record guard is what makes the
partial-collection states reachable at all**; and the currentness channel is the one entry this
composition deliberately leaves unmeasured.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it owns, the five availability facts, the per-collection isolation and the three responsibilities it leaves to R26, R15 and the owners. | "The complete owner-produced record collection for one review" | mcp/src/agents_remember/application/review_evidence_records.py:1-41 |
| The published surface, and the one declaration of what "a record this composition cannot serve" means. | `__all__`; `_DAMAGED_RECORD_ERRORS` |mcp/src/agents_remember/application/review_evidence_records.py:111-119; mcp/src/agents_remember/application/review_evidence_records.py:125-125|
| **The record kinds the authored-effects channel counts, moved here beside the channel that reports them, and the same declaration for the claims collection.** | `AUTHORED_EFFECT_KINDS`; `EVIDENCE_CLAIM_KINDS` |mcp/src/agents_remember/application/review_evidence_records.py:131-133; mcp/src/agents_remember/application/review_evidence_records.py:134-134|
| **Every collection with the owner whose read answers for it — the pointer a reader of an absent collection follows — and the five collections plus the measurement, in the order they are read.** | `_COLLECTION_OWNERS`; `_COLLECTION_NAMES` | mcp/src/agents_remember/application/review_evidence_records.py:136-143; mcp/src/agents_remember/application/review_evidence_records.py:148-154 |
| **The currentness owner the bundle names, and the measurement this module now delegates instead of stating.** | `CURRENTNESS_OWNER`; `_COLLECTION_OWNERS` | mcp/src/agents_remember/application/review_assessment_currentness.py:69-69; mcp/src/agents_remember/application/review_evidence_records.py:136-143 |
| The two matrix-sourced collections, declared as kinds so the channel and the pane cannot disagree, and the next action an unopened dataset earns. | `_SELECTION_KINDS`; `_PLACE_DATASET` |mcp/src/agents_remember/application/review_evidence_records.py:158-160; mcp/src/agents_remember/application/review_evidence_records.py:164-167|
| **The production entry point: same candidate resolution as the surface, and an unresolvable candidate reported per collection rather than as five empty tuples.** | `review_records_for` | mcp/src/agents_remember/application/review_evidence_records.py:170-195 |
| The assembly of one resolved candidate's bundle: four collections read, one measurement stated. | `review_records_for_resolution` | mcp/src/agents_remember/application/review_evidence_records.py:198-235 |
| **The two matrix-owned channels, added where the matrix's own answer is, with `not_selected` for a review that never asked and the view's declared row bound carried through.** | `with_selection_channels`; `_selection_channel` | mcp/src/agents_remember/application/review_evidence_records.py:274-299; mcp/src/agents_remember/application/review_evidence_records.py:302-323; mcp/src/agents_remember/application/review_evidence_records.py:256-256 |
| Assessment collection availability comes from the durable curator bridge: captured records, measured empty, uncaptured, and unreadable expected inputs remain distinct. | `review_curator_records`; `_historical_records`; `_without_pin` | mcp/src/agents_remember/application/review_curator_records.py:41-70; mcp/src/agents_remember/application/review_curator_records.py:147-175; mcp/src/agents_remember/application/review_curator_records.py:111-139; mcp/src/agents_remember/application/review_curator_records.py:178-194 |
| **The detection collection read through the owner's own run reader, over the identity listing the owner exposes.** | `_detection_signals`; `recorded_run_ids` |mcp/src/agents_remember/application/review_evidence_records.py:326-352; mcp/src/agents_remember/memory/knowledge/detection.py:565-579|
| **The three states of a partly readable collection: no run recorded, all runs unreadable, or a supplied subset with the unreadable identities named.** | `_signal_channel` |mcp/src/agents_remember/application/review_evidence_records.py:355-384|
| **The per-record guard that makes a damaged run survivable: one identity named, its siblings still supplied.** | `_read_signal_runs` | mcp/src/agents_remember/application/review_evidence_records.py:387-412 |
| **The observation collection selected by both halves of the candidate's own binding, so a foreign candidate's observation is not selected.** | `_observations`; `ObservationCandidateSeed` | mcp/src/agents_remember/application/review_evidence_records.py:415-447; mcp/src/agents_remember/models/knowledge/evidence_read.py:248-272 |
| **The evidence owner's own `selector_absent` as a measured zero, and every other refusal as unavailability carrying its code and next action.** | `_observation_refusal` |mcp/src/agents_remember/application/review_evidence_records.py:450-474|
| **The claims collection as the owner's complete one, read one record at a time so a damaged claim is named and its siblings served.** | `_evidence_claims`; `_claim_records`; `claim_ids` | mcp/src/agents_remember/application/review_evidence_records.py:521-545; mcp/src/agents_remember/memory/knowledge/evidence_records.py:838-850 |
| **One claim's authored fields rendered verbatim: author from the admission, lifecycle from the record, declared limitations and asserted coverage as recorded.** | `_claim_record`; `ReviewClaimRecord`; `coverage_identity` | mcp/src/agents_remember/application/review_evidence_records.py:548-571; mcp/src/agents_remember/application/review_record_rendering.py:80-106; mcp/src/agents_remember/models/knowledge/evidence.py:642-647 |
| The candidate read context, and the absent or unopenable dataset reported as unavailability rather than as an empty collection. | `_candidate_context`; `_open_candidate_store`; `_absent_dataset` | mcp/src/agents_remember/application/review_evidence_records.py:623-636; mcp/src/agents_remember/application/review_evidence_records.py:639-648; mcp/src/agents_remember/application/review_evidence_records.py:585-607 |
| **The unresolvable-candidate bundle: every collection unavailable, one entry per class, because nothing resolved and so no owner was asked.** | `_unresolved_channels` |mcp/src/agents_remember/application/review_evidence_records.py:651-678|
| The one channel construction point: the answer varies, the owner does not. | `_answered`; `_Answer`; `_channel` | mcp/src/agents_remember/application/review_evidence_records.py:681-706; mcp/src/agents_remember/application/review_evidence_records.py:709-722; mcp/src/agents_remember/application/review_evidence_records.py:781-792 |
| The four non-answer states and the two notes that keep a partial or bounded collection truthful. | `_recorded`; `_absent`; `_unavailable`; `_not_selected`; `_remaining_note`; `_unreadable_note` | mcp/src/agents_remember/application/review_evidence_records.py:725-736; mcp/src/agents_remember/application/review_evidence_records.py:739-742; mcp/src/agents_remember/application/review_evidence_records.py:745-762; mcp/src/agents_remember/application/review_evidence_records.py:765-778; mcp/src/agents_remember/application/review_evidence_records.py:795-824; mcp/src/agents_remember/application/review_evidence_records.py:827-835 |
| One unavailability statement: what failed, under which owner status, in the owner's own words. | `_provenance` |mcp/src/agents_remember/application/review_evidence_records.py:838-842|
| **The availability vocabulary this module builds, and the validator that makes "a count nobody measured" unrepresentable.** | `ReviewRecordChannel`; `ReviewRecordChannelState`; `ReviewRecordClassName` | mcp/src/agents_remember/models/knowledge/review_records.py:32-39; mcp/src/agents_remember/models/knowledge/review_records.py:47-53; mcp/src/agents_remember/models/knowledge/review_records.py:68-123 |
| **The subject composition's own call site: it adds the two matrix-owned channels where the matrix's answer is, and reports the view's declared row bound.** | `with_selection_channels`; `compose_review`; `_matrix_rows_remaining` | mcp/src/agents_remember/application/review_evidence_records.py:274-299; mcp/src/agents_remember/application/knowledge_review.py:335-577; mcp/src/agents_remember/application/knowledge_review.py:650-663; mcp/src/agents_remember/application/knowledge_review.py:578-591 |
| **The task-context composition's call site: no matrix was read, so the matrix-owned collections are reported `not_selected`.** | `without_selected_matrix`; `task_context_review` | mcp/src/agents_remember/application/review_evidence_records.py:238-254; mcp/src/agents_remember/application/review_task_context.py:93-191 |
| **The production port this bundle is read through, and the adapter's re-export of the resolver so the port keeps resolving without a new home to learn.** | `review_port`; `review_records_for`; `serving_collaborators` | mcp/src/agents_remember/cli/dashboard.py:88-102; mcp/src/agents_remember/cli/dashboard.py:67-132; mcp/src/agents_remember/application/knowledge_review.py:81-81 |
| **The channel list as part of the served payload, one entry per class the composition read.** | `ReviewEvidencePane`; `channels` | mcp/src/agents_remember/models/knowledge/review.py:956-996 |
| **The ten cases that drive this module through the production port, including the two per-record damage cases.** | `test_the_production_composition_supplies_every_owner_produced_record_class`; `test_a_damaged_detection_run_is_named_while_its_siblings_are_supplied`; `test_a_damaged_evidence_claim_is_named_while_its_siblings_are_supplied` | mcp/tests/test_knowledge_review_evidence_channels.py:566-618; mcp/tests/test_knowledge_review_evidence_channels.py:825-844; mcp/tests/test_knowledge_review_evidence_channels.py:847-870 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| All owner records are collected for the already resolved comparison pair. | `review_records_for_resolution` | mcp/src/agents_remember/application/review_evidence_records.py:198-235 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one candidate's own dataset and its
enclosure's own curator authority and touches no repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`knowledge_review.py`) moved with the leaf's inserted lines: 6 passing row(s) normalised by the fixer; 1 row(s) the fixer declined re-pointed by the exact base-to-staged line shift (each byte-identical to memory HEAD, its anchors checked in the base and shifted ranges). The fixer's normalisation also re-measured ranges into files this leaf did not change (`review.py`, `review_curator_records.py`, `review_records.py`, `review_task_context.py`, `test_knowledge_review_evidence_channels.py`). One extra range already dead at the base, which the fixer's normalisation left unshifted, was shifted exactly (`knowledge_review.py:575-588` → `578-591`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 1 citation into `mcp/src/agents_remember/memory/knowledge/evidence_records.py` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/application/knowledge_review.py`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.

- 2026-09-27T05:31:41+00:00 — Selected the actual value/model declarations for 2 ambiguous source-linked citation(s), including container members and delegated type owners where applicable. The bounded claim is retained; generated history and real stamps remain unchanged.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 7 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.

- 2026-09-27T05:25:19+00:00 — Reconciled the L41 moved record/path owners and explicit retained-parent recovery boundary with current source. Prior generated history and real verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 15 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:56:35+00:00 — Updated record-collection ownership for exact-pair capture and historical pinned assessments, preserving per-channel isolation. Verification hashes/dates remain closeout-owned.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **L7-aftershock citation repair: the composition row re-cited to the landed declarations** (`compose_review` `:380-477`, `_rows_remaining` `:560-575`). Wording retained; no stamp advanced.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **three enforced rows re-cited.** The two call-site rows and the port row cited pre-merge adapter/task-context ranges; they now cite the merged call sites (`knowledge_review.py:424-426`/`542-553`, `review_task_context.py:108-115`) and re-exports (`72-72`/`149-151`, `dashboard.py:88-88`). Wording unchanged; no stamp advanced.
- 2026-09-21T21:20:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): created this one-to-one card for the module this leaf introduced as `ICR-R14@v1`'s production owner. The card records what the module *is* rather than only where the code lives: the five owner-produced collections plus the one deliberate non-measurement, resolved through each owner's own read; the availability fact carried per collection with the three states an empty tuple used to collapse; the **per-record** guard that makes "one damaged record named while its siblings are supplied" reachable at all (the detection owner reports damage by raising, and the evidence owner's enumerator is all-or-nothing); the double-half candidate binding that keeps a foreign candidate's observation out of the collection; and the two matrix-owned collections that arrive from the matrix's own answer, `not_selected` when the review never asked. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line `ar/260921_complete-code-and-intent-review` at its current tip and this leaf's own base — because every construct cited here exists only in this leaf's uncommitted candidate and no commit contains the content a stamp would otherwise claim to have verified. That is a statement of what the reading was against, not a claim that these constructs exist in that commit; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp.

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

## Update History
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **a stated remainder always names the action that reaches it, and a refused read is not a zero.**
`MatrixSelection` carries the page (when it is the records collection's own), the owner's remainder and
any refusal; `with_selection_channels` gained the page and the refusal; the task-context branch became
the extracted `without_selected_matrix`. Every row on this card that cited this module by line was
re-derived against this candidate, because this leaf moved them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
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

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the claim's own recorded subject revision enters the R14 bundle (840 → 862 lines; `ICR-R26@v1`).** The card records `subject_of_claim` as the read, `_claim_subject_revision`'s invariant-revision-only rule (a facet subject is the absence it is, never narrowed), and that the extension adds a reader rather than a second record reader. **Citation accounting:** `_claim_records` `454-521`→`548-572` (its declaration is now 548) and `_claim_record` `73`/`104`→`548-572`/`575-598`, with `ReviewClaimRecord` re-pointed at its own extent in the record renderer. Wording was retained where the claim still states what the code does. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
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

## Update History
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate uncommitted; basis: leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **nine enforced citation rows re-pointed to the declarations they name; the two `_CURRENTNESS` rows left untouched for the curator.** Citation accounting: `__all__` `:101-108`→`:113-120` and `_DAMAGED_RECORD_ERRORS` `:114-114`→`:126-126`; `AUTHORED_EFFECT_KINDS` `:120-122`→`:132-134` and `EVIDENCE_CLAIM_KINDS` `:123-123`→`:135-135`; `_SELECTION_KINDS` `:166-168`→`:159-161` and `_PLACE_DATASET` `:172-175`→`:165-168`; the six-anchor non-answer row widened `:745-855`→`:745-872` so it reaches `_unreadable_note` at 864; and the two per-record damage cases re-pointed in `mcp/tests/test_knowledge_review_evidence_channels.py` (`:695-717`→`:825-844`, `:719-745`→`:847-870`). Wording, Findings and Anchors all unchanged. The two `_CURRENTNESS` rows (`:144-158`) are deliberately **not** re-pointed: this leaf deleted that constant, it resolves nowhere in the code tree, so the claim itself — not its pointer — is what needs the curator's re-reading. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header's stamp values are untouched, and the governed closeout owns the real stamp.
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the record bundle is read for the record the request named (ICR-R12@v1).** `review_records_for`
resolves with `recorded=request.history == "recorded"`, so the records handed to a caller belong to the
comparison the same request renders. Nothing else in the bundle changed. **Citation accounting:** every
row into this module was re-derived against the candidate. **Stamp accounting:** no verification stamp
was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
