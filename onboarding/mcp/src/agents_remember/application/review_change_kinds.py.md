# mcp/src/agents_remember/application/review_change_kinds.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The change-kind facts of a tree comparison's family context, computed on the server for the members a roster page
returned (MIK-R33, adopting ICR-R32@v1 rule 1).** `with_change_kinds(context, trees)` is the one entry point:
`knowledge_review.compose_review` passes the composed family context through it, and each family entry comes back
carrying `change_kinds` (`models/knowledge/review_change_kinds.ReviewFamilyChanges`): the fact of the family's own
guarantee, the deduplicated member total, and one `ReviewMemberChange` per returned member occurrence. A dataset review
(`trees` is `None`) gets its context back exactly as composed, so nothing here runs before a converted leaf's tree
comparison (inert until MIK-R37). The browser orders, counts and traverses by these facts and never recomputes one.

`review_change_kinds` computes the MIK-R33 change-kind facts of a tree comparison's family context for the members a roster page returned: intent, implementation and membership per member occurrence, travelling on each family context entry for the browser to order and traverse by. In W03 the recorded-meaning facts (guarantee, intent, membership) are delegated to the shared `RecordChanges`, so the detail badges and the navigation outline use one definition.
## Code Commentary

### Logic

- **One lane per read.** `with_change_kinds` opens MIK-L32's `open_tree_lane(trees)` once and builds `_ChangeKinds`
  over it: both memory sides are read through the lane's derived indexes, and every hunk intersection comes from
  `TreeLane.classify(change)`, memoized per changed path (`_file`). There is no second hunk classifier and no range
  arithmetic here (ruling 2026-09-30T15:11:20). If the trees cannot be read or compared (`LaneReadError`,
  `apsw.Error`), every family and every returned member is `unknown`, with the bounded error as the reason (`_unread`).
- **Returned members only.** `_returned` takes each member occurrence once by the roster's `member_id` (the same on
  both sides for one invariant under one family), so a revised member's two revision rows share one fact set and a
  member no page returned is never described (ICR-R32 rule 5).
- **`intent` (`_intent` → shared `RecordChanges.intent`).** The shared index-only owner compares
  live/retired presence, revision and byte-for-byte `statement`, `applicability`, `conditions` and
  `exclusions`. A same-revision wording difference sets `text_differs` and establishes intent;
  presence/wording helpers are not local `_presence`, `_WORDING` or `_wording` declarations here.
- **`implementation` (a) (`_entry_changes`).** An entry of the member added, retired or re-anchored between the sides.
  A changed anchor is a re-anchor unless it is the writer's mechanical carry (`classify.carried_mechanically` with the
  worklist `Classifier`'s class of the K_B entry, `_base_class`): of MIK-R08 definition 7's exemptions only that one is
  kept, because `touched`, `moved_or_absent` and `stale_at_base` exist for the worklist's own covering items (review R1
  F1, ruling 17:47:43). A repair of an entry already stale at the base reads "re-anchored (stale at base)" (ruling
  18:57:45). An undecidable class (a `CodeReadError`, an unparseable entry) leaves the fact `unknown`.
- **`implementation` (b) (`_hunks`, `_hunk_linked`).** Only changed paths where the member records an entry are
  classified, so a linked file in the inventory establishes nothing by itself. A hunk the lane links to an entry of
  the member establishes the fact; a proof entry counts and marks `test`. **Definition 8 (`_file_covered`):** on a
  changed non-text file a `file` entry of the member establishes it through the worklist's own `non_text_linked`
  (ruling 16:22:22 item 6b); a resolved non-file entry there stays `unknown` unless the fact is established
  (`_unintersectable`).
- **The unconditional unknown (`_unresolved`, review R1 F4).** An entry of the member on a side where the changed file
  changes lines (or whose content changed as non-text) that supplies no range there, or whose side's knowledge is
  unavailable, sets `range_unresolved`, so the `unknown` mark is added even beside an established `implementation`.
  `_withheld` words the lane's per-entry reason for a reviewer (the recorded and side blobs for
  `recorded_blob_mismatch`; plain words plus the code for `path_absent`, `unresolved`, `unsupported_locator`,
  `unreadable`).
- **`membership` (`_membership`).** Whether this family's record lists the invariant on each side; unknown when a
  side's family record cannot be read.
- **Reasons (shared `Fact.reasons`, local `_member`).** Each unknown fact names why; unresolved
  reasons for entries that established nothing come first. The local member assembly keeps
  change-kind and membership reasons apart and names bounded evidence only for established facts.
- **Family level.** `_guarantee`: `intent` when the `guarantee` text differs or the family is live on one side only,
  `unchanged` when the same, `unknown` when a side cannot be read. `_members_total`: the deduplicated union of live
  members on either side, `None` only when the family's own record file or a listed member's own file fails to parse
  (`_own_problem`, review R1 note). `_position`: the invariant's index in the family record's authored `members` (after
  side, else before), the tree's authored order (ruling 16:22:22 item 7).

### Conventions

- `_ChangeKinds` retains the lane, local implementation caches and a shared `RecordChanges`
  reader. `Fact` and `Known` are imported from `review_record_changes.py`, not local dataclasses.
  `with_change_kinds` remains the public entry. Shared recorded-meaning reasons and local
  implementation/evidence reasons remain bounded; `ReviewMemberChange.of` derives primary/marks.
- The current module is 538 lines, under the 1,200-line limit.

### Invariants And Boundaries

- **Candidate invariant (not ingested; no speculative ingestion): change-kind facts are computed on the server, for
  returned members only, from recorded comparison facts; the hunk intersection comes only from MIK-L32's
  classification, and the client never recomputes it.** Realized by `with_change_kinds` (one `open_tree_lane` per
  read), `_returned`, `_hunk_linked` over `TreeLane.classify`, and the entry validator in `review_family_context.py`
  that requires facts for exactly the returned members. Proved by `test_review_change_kinds.py`
  (`test_a_partial_page_describes_only_the_members_it_returned`,
  `test_the_facts_are_derived_and_describe_exactly_the_returned_members`), the worker's real-data reconciliation (every
  hunk-established fact is a link in `classify_changed_path` for its path, 2 of 2), and mutations "the validator no
  longer checks the returned members" and "a proof link establishes nothing", both caught.
- **Candidate invariant (not ingested): unreadable or partial knowledge produces `unknown` with a stated reason, never
  `unchanged` or a complete-looking total.** Realized by `_unread`, `_record`'s parse-problem answer, `_entries`'
  unparsed-sidecar answer, `_unresolved`, `_unintersectable`, `_members_total` returning `None`, and the model's
  `_unknowns_say_why`. Proved by `test_an_unreadable_sidecar_leaves_implementation_unknown_never_unchanged`,
  `test_an_unreadable_family_record_leaves_guarantee_and_membership_unknown`,
  `test_trees_that_cannot_be_read_make_every_fact_unknown`,
  `test_an_unread_sidecar_of_a_changed_file_marks_unknown_beside_an_established_fact` and
  `test_the_total_is_unknown_only_when_the_familys_own_records_fail`, with the mutations "an unparsed sidecar is
  ignored", "an unread family record reads unchanged" and "a withheld range leaves nothing unknown", all caught.
- **Candidate invariant (not ingested): changed intent text is never `unchanged`, even at the same revision.**
  Realized by `_intent` delegating to `RecordChanges.intent` and its shared `wording` comparison with `text_differs`. Proved by
  `test_every_member_occurrence_carries_its_kind_from_the_recorded_comparison` (INV-PPPPPP reworded in
  `applicability` reads `intent` with `text_differs`, INV-EEEEEE beside it reads `unchanged`), and the mutation "a
  same-revision text change reads unchanged", caught.
- Nothing here is a verdict, a risk score or an assessment (ICR-R32 Exclusions).

### Todos

- **Pre-curation unknowns are the lane's literal rule** (ruling 16:22:22 item 4): until an uncurated leaf's entries in
  changed files are re-recorded at the candidate blob, they supply no range there and mark `unknown`. On the worker's
  real scratch, FAM-R6R095RW read 7 unknown before curation and 0 after (three `+unknown` marks remained for entries
  recorded at an older before-side blob, MIK-L32's Q2, carried to L37).
- Review R2-4 (accepted as a note): the presence facts (`intent`, `guarantee`, `membership`) still use `_record`'s broad
  rule, so a missing record reads `unknown` when any record of that kind fails to parse on that side; only the total
  was narrowed. This is honest and never `unchanged`.
- Review R3-2 (accepted): when the whole comparison or an invariant identity cannot be read, `unknown_reasons` and
  `membership_reasons` carry the same detail, which the tree draws as two lines for two unknown facts.

`_ChangeKinds` holds `meaning: RecordChanges` beside the lane. `_guarantee` maps shared `added`/`removed`/`changed` results to the detail badge word `intent`, while `unknown` and `unchanged` remain unchanged; the outline may retain added/removed/changed, so the two vocabularies are not identical. `_intent` and `_membership` return the shared facts directly. Member identity/authored position, implementation facts over realization/proof entries and lane hunks, evidence shaping and unread-side fallback stay local. The public entry and refusal behavior remain unchanged.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: facts computed here, for returned members only, each read from the comparison itself. [1]
- The entry point: one lane per read, a dataset review's context unchanged, unreadable trees make every fact unknown. [2]
- The family's own row and its total over the family's own records (review R1 note). [4]
- One member occurrence: three facts, bounded evidence, and the change kind's reasons apart from the membership's. [5]
- Membership on each side of this family's record. [7]
- Implementation (a): added, retired or re-anchored; only the mechanical carry is exempt (review R1 F1); stale-at-base repairs worded apart. [8]
- Implementation (b) through the lane's links only, and definition 8 on a changed non-text file. [9]
- The unconditional unknown for an unresolved range, the lane's reason in a reviewer's words, and a non-file entry at a non-text change. [10]
- The worklist classifier's class of one base entry, for definition 7. [11]
- Records and entries read through each side's index; an unparsed record or sidecar answers why instead. [12]
- The change inventory read once, and each changed path classified once by the lane. [13]
- Its one caller: the composed review's family context. [14]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Meaning facts come from the shared index-only module [15]
- One comparison's facts ride beside the lane reader [16]
- The family badge maps the shared guarantee onto badge words [17]
- Member intent and membership are the shared facts directly [18]

- The shared Fact exposes established/unknown/not_established states and orders unresolved reasons from non-establishing entries first. [3]
- The local _intent delegates revision, retired-presence and same-revision wording classification to shared RecordChanges.intent, presence and wording. [6]
- The local _intent delegates revision, retired-presence and same-revision wording classification to shared RecordChanges.intent, presence and wording. [19]
- The local _intent delegates revision, retired-presence and same-revision wording classification to shared RecordChanges.intent, presence and wording. [20]
- The local _intent delegates revision, retired-presence and same-revision wording classification to shared RecordChanges.intent, presence and wording. [21]
