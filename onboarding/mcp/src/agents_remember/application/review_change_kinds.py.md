# mcp/src/agents_remember/application/review_change_kinds.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_change_kinds.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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
- **`intent` (`_intent`, `_presence`).** The invariant record's `revision` in K_B against K_C; a record live on one
  side only is `added` or `removed`, and a `retired` record counts as removed (ruling 16:22:22 item 6a). **One revision
  whose authored text differs** (`_WORDING`: statement, applicability, conditions, exclusions, compared byte for byte)
  is `intent` marked `text_differs`, never `unchanged` (ruling 16:22:22 item 5, the master's byte-comparison rule).
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
- **Reasons (`_Fact.reasons`, `_member`).** Each unknown fact names why; entries that established nothing come first
  (review R2-3). The change kind's reasons (intent, implementation, unresolved ranges) and the membership's reasons are
  kept apart (`unknown_reasons` and `membership_reasons`, the merge round), and `evidence` names only what established
  each established fact, all bounded.
- **Family level.** `_guarantee`: `intent` when the `guarantee` text differs or the family is live on one side only,
  `unchanged` when the same, `unknown` when a side cannot be read. `_members_total`: the deduplicated union of live
  members on either side, `None` only when the family's own record file or a listed member's own file fails to parse
  (`_own_problem`, review R1 note). `_position`: the invariant's index in the family record's authored `members` (after
  side, else before), the tree's authored order (ruling 16:22:22 item 7).

### Conventions

- Module-private helpers around one dataclass (`_ChangeKinds`) that holds the lane and two memo caches; `_Fact` and
  `_Known` are small mutable/frozen dataclasses local to the module. The public surface is `with_change_kinds` only.
- Every reason string is built here in the reviewer's words and bounded by the lane's `bounded_text` or the model's
  clipping; the model derives `primary` and `marks` from the facts (`ReviewMemberChange.of`), so this module never
  sets them by hand.
- 671 lines (the application card's size note; under the 1,200-line limit).

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
  Realized by `_intent`'s `_wording` comparison and `text_differs`. Proved by
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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement: facts computed here, for returned members only, each read from the comparison itself. | "The facts are computed here, on"; "Nothing is inferred: a side that cannot be read makes the facts it would decide" | mcp/src/agents_remember/application/review_change_kinds.py:1-33 |
| The entry point: one lane per read, a dataset review's context unchanged, unreadable trees make every fact unknown. | `with_change_kinds`; `_unread` | mcp/src/agents_remember/application/review_change_kinds.py:104-121; mcp/src/agents_remember/application/review_change_kinds.py:138-152 |
| A fact's three states, and its reasons with the entries that established nothing first (review R2-3). | `_Fact` | mcp/src/agents_remember/application/review_change_kinds.py:164-206 |
| The family's own row and its total over the family's own records (review R1 note). | `_guarantee`; `_members_total`; `_own_problem` | mcp/src/agents_remember/application/review_change_kinds.py:240-273; mcp/src/agents_remember/application/review_change_kinds.py:641-647 |
| One member occurrence: three facts, bounded evidence, and the change kind's reasons apart from the membership's. | `_member`; `_position` | mcp/src/agents_remember/application/review_change_kinds.py:277-325 |
| Intent: the revision, presence (retired counts as removed) and a same revision whose text differs. | `_intent`; `_presence`; `_WORDING` | mcp/src/agents_remember/application/review_change_kinds.py:335-353; mcp/src/agents_remember/application/review_change_kinds.py:534-546; mcp/src/agents_remember/application/review_change_kinds.py:94-94 |
| Membership on each side of this family's record. | `_membership` | mcp/src/agents_remember/application/review_change_kinds.py:355-368 |
| Implementation (a): added, retired or re-anchored; only the mechanical carry is exempt (review R1 F1); stale-at-base repairs worded apart. | `_entry_changes`; "carried_mechanically(old, new, entry_class)"; "(stale at base)" | mcp/src/agents_remember/application/review_change_kinds.py:385-416 |
| Implementation (b) through the lane's links only, and definition 8 on a changed non-text file. | `_hunks`; `_hunk_linked`; `_file_covered` | mcp/src/agents_remember/application/review_change_kinds.py:418-437; mcp/src/agents_remember/application/review_change_kinds.py:554-585 |
| The unconditional unknown for an unresolved range, the lane's reason in a reviewer's words, and a non-file entry at a non-text change. | `_withheld`; `_unresolved`; `_unintersectable` | mcp/src/agents_remember/application/review_change_kinds.py:588-638 |
| The worklist classifier's class of one base entry, for definition 7. | `_base_class` | mcp/src/agents_remember/application/review_change_kinds.py:506-531 |
| Records and entries read through each side's index; an unparsed record or sidecar answers why instead. | `_record`; `_entries` | mcp/src/agents_remember/application/review_change_kinds.py:449-480 |
| The change inventory read once, and each changed path classified once by the lane. | `_change`; `_file` | mcp/src/agents_remember/application/review_change_kinds.py:482-504 |
| Its one caller: the composed review's family context. | "family_context=with_change_kinds(family.context, resolved.trees)," | mcp/src/agents_remember/application/knowledge_review.py:555-555 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new server module of MIK-R33, recording rulings 2026-09-30T15:11:20 (start), 16:22:22 (items 1 to 11), 17:47:43 (review R1 F1, F2, F4 and its notes), 18:57:45 (review R2) and 21:41:02 (merge round), and three candidate invariants. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
