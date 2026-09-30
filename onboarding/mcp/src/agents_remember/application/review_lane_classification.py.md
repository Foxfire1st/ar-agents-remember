# mcp/src/agents_remember/application/review_lane_classification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_lane_classification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The one classification of a tree comparison's changed paths for the reviewer (MIK-R32, adopting ICR-R33@v1):
file buckets and hunk classes.** The unexplained-changes lane, its entry count, and the later triage badges (MIK-R33)
and per-hunk markers (MIK-R34) all read this module; nothing else classifies a hunk for the reviewer. It owns no hunk
arithmetic of its own. It calls MIK-R08's functions:

- a path's hunks come from `change_hunks` (definition 2), which the gate's linkage also calls;
- an entry's range comes from `CodeTrees.resolve` (definition 3), reached only at the entry's recorded blob;
- intersection uses `hits_old` and `hits_new`, on sides where the hunk changes lines only;
- a non-text change's gate linkage uses `non_text_linked` (definition 8), the gate's own predicate.

Each memory side is read through the derived index of its tree (`KnowledgeIndex`), as MIK-R25's data source does.

## Code Commentary

### Logic

- **Opening a comparison.** `open_tree_lane(trees)` opens the recorded comparison's code trees once
  (`CodeTrees.open`), lists B and C (a tree Git cannot list raises `LaneReadError`), and opens each memory side's
  index inside one `ExitStack`. `_side` gives a `LaneSide` with no index and a `detail` when the side's database is
  missing or its index cannot be opened, and otherwise keeps the index's parse `problems`.
- **What a side knows of a path.** `LaneSide.unavailable(path)` answers why the side's knowledge of the path is
  unknown: the whole side is unread, or the path's own sidecar (`onboarding/<path>.json`) is among the files a
  partial index failed to parse. A partial index therefore makes only its unparsed paths unknown.
  `LaneSide.complete` is true only for an index with no parse problem at all; `families_complete` is true when no
  family record failed to parse. `entries_at` returns the path's realization entries **and proof entries**.
  `revision`, `families_of` and `family_members` read and memoise the index's records.
- **The exact-blob rule (`TreeLane._place`).** Each entry recorded at the path on a side becomes a `Placed`: the
  span it supplies there, or the reason it supplies none, in this order:
  - `path_absent`: the side's code tree has no regular file at the path;
  - `recorded_blob_mismatch`: the entry's recorded `blob` is not the side's blob. A range mapped through a diff,
    or an entry MIK-R03 would still call current at another blob, supplies nothing here;
  - `unsupported_locator`: a kind other than `symbol`, `line_range` or `file`, or a symbol in a file with no
    shipped grammar;
  - `unreadable`: a Git read failed;
  - `unresolved`: the locator binds nothing in the blob (a symbol not bound uniquely, a line range outside it).
  Otherwise the entry supplies the resolved span. `_placement` resolves with the recorded blob equal to the blob,
  through L31's shared `PLACEMENTS` memo and its `observation_key`, so the cards read and the lane share answers.
- **Buckets, no hunk read (`TreeLane.bucket`, `_bucket`).**
  - *attributed*: an entry supplies a range on a side;
  - *unexplained*: neither side records any entry at the path and both sides were read (a side where the file is
    absent is read all the same);
  - *attribution_unknown*: every other path (a side's knowledge unavailable, or entries recorded that supply no
    range).
  The reason is prose built from the placements: `_attributed_reason` names the supplying entries per side and any
  unread side; `_unknown_facts` and `_withheld` name the unavailable side or the withholding entries with their
  reasons.
- **Hunks (`TreeLane.classify`, `_classified`).** `classify(change)` buckets the path, takes its hunks from
  `change_hunks` (a `CodeReadError` becomes `LaneReadError`), and classifies each hunk:
  - only the sides where the hunk changes lines are considered (`changes_lines`, exported since MIK-L33), so an insertion is matched
    against after-side ranges only and a deletion against before-side ranges only;
  - *linked* when those changed lines intersect a supplied range there (`_links`, `_intersects` through
    `hits_old`/`hits_new`); every intersecting entry per side is kept;
  - otherwise *attribution_unknown* when such a side is unavailable (`knowledge_unavailable`) or has entries that
    supply no range (`range_not_supplied`, with every withheld entry ID in `entries`), from `_unknown`;
  - otherwise *unexplained*.
- **Non-text changes.** A path with no hunks (non-text or type change, or an empty added or deleted file) or a mode
  change gets a `ReviewLaneNonText` with its content state, the mode flag and `gate`: `_gate` answers the gate's own
  linkage through `non_text_linked` over every placed entry's locator kind, and `unknown` unless **both** sides are
  `complete`.
- **Bounded reasons (review R1 F4).** A reason names at most `NAMED_ENTRIES` (10) entries per side, then "and K
  more" (`_named`); quoted owner details are clipped to `DETAIL_LIMIT` (2,000) characters by `bounded_text`. The
  per-hunk `entries` still carry every ID.

### Conventions

- The code trees and both indexes are opened once per `TreeLane` and closed with it; the reads above are
  memoised per side.
- The module states once, in its docstring, where it differs from the gate; it keeps the gate's functions
  unchanged and calls them.

### Invariants And Boundaries

- **Candidate invariant (not ingested): the reviewer classifies changed files and hunks through MIK-R08's
  definitions only, one classification shared with the gate.** Realized by `TreeLane.classify` calling
  `change_hunks`, `CodeTrees.resolve`, `hits_old`/`hits_new` and `non_text_linked`, which the gate's
  `_Run._path_hunks` and `_Run._file_covered` now also call. Proved by the reviewer's real-data agreement check
  (review R1 and R2: on all 7 real paths the hunks and the non-text linkage equal the gate's, every gate-held
  non-text change is listed, and every hunk the lane links the gate links), and by the L08/L10 worklist suites
  passing unchanged.
- **Candidate invariant (not ingested): an entry supplies a range only when a side's blob is exactly its recorded
  blob** (MIK-R32 substitution, definition 3, R3-R32-F1). Realized by `TreeLane._place` ("if recorded != blob:")
  and `_placement`. Proved by `test_hunks_are_classified_on_their_changed_lines_at_each_sides_recorded_blob` (the
  pre-curation `recorded_blob_mismatch` on the after side of `pkg/a.py`, the insertion inside `f` that the gate
  would link) and by the mutation "relax the exact-blob rule" (3 failing cases).
- **Candidate invariant (not ingested): the lane says unknown when the gate could not be computed, never "gate
  unexplained".** Realized by `_gate` requiring both sides `complete` (review R1 F3, ruling 2026-09-30T13:07:38).
  Proved by `test_an_unreadable_side_is_never_unexplained_and_the_readable_side_still_links` and
  `test_a_partial_index_makes_only_its_unparsed_files_unknown`; restoring the old unavailable-only rule fails the
  second.
- **Unknown is never unexplained.** No file is unexplained while a side is unread, and changed lines on an unread
  side are `knowledge_unavailable` (MIK-R32 Failure and Recovery).
- **The lane and the gate may differ, and the gate decides gate items.** An insertion in an attributed file before
  curation is `attribution_unknown` here and `unexplained_hunk` at the gate (the packet's closing note); an entry
  recorded at an older blob links a hunk at the gate through a mapped range and supplies nothing here.
- **Since MIK-R09 the per-side rule is the same on both views (L09 review R1 F8, ruling 2026-09-30T16:07:55).** The
  gate's `compute._linked` applies definition 8 symmetrically (an insertion-only hunk is linked only by a K_C range at
  C, a deletion-only hunk only by a K_B range at B), so the docstring no longer says the gate "also counts an
  insertion strictly inside a before-side range". The two views now differ only in where ranges come from: the gate
  maps line ranges through the diff, and the lane uses only the entry's own recorded blob. L32's real-data agreement
  check (7 paths) is unchanged: that sample held no insertion-only hunk inside a before-side range.
- **Ruling Q2 (2026-09-30T12:19:20): the exact-blob rule is the packet's.** Entries recorded at an older blob read
  unknown until re-recorded. On the real converted memory, 47 of 178 entries (18 files) are recorded at an older
  blob; whether the cutover conversion should re-record content-identical entries is carried to L37 as a check
  item.
- **Ruling Q7: a rename counts as a deletion plus an addition,** as in the gate: the change inventory runs with
  `--no-renames`, so each side's path is the changed path itself.
- Inert on the installed runtime: only a converted leaf's tree comparison reaches this module.

### Todos

- **Carried to L37 (ruling Q2):** decide whether the cutover conversion re-records content-identical entries at
  the current blob, so the first real review does not show more "unknown" than the content warrants.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R32@v1` (adopting `ICR-R33@v1` with substitutions) and its rulings in `32_unexplained-changes-lane.json`; they
live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: one classification, no hunk arithmetic of its own, and where it differs from the gate. | "An entry supplies a range on a side only at its own recorded blob."; "Only changed lines are intersected." | mcp/src/agents_remember/application/review_lane_classification.py:1-33 |
| The bounds on a reason: ten named entries, clipped details. | `NAMED_ENTRIES`; `DETAIL_LIMIT` | mcp/src/agents_remember/application/review_lane_classification.py:103-104 |
| A side's knowledge of one path: an unread side, or the path's own unparsed sidecar. | `LaneSide`; "problem = self.problems.get(sidecar)" | mcp/src/agents_remember/application/review_lane_classification.py:116-189 |
| A side read whole; realization and proof entries at a path; family records all read. | "return self.index is not None and not self.problems"; "return (*found.realizations, *found.proofs)"; `families_complete` | mcp/src/agents_remember/application/review_lane_classification.py:148-148; mcp/src/agents_remember/application/review_lane_classification.py:154-154; mcp/src/agents_remember/application/review_lane_classification.py:156-162 |
| One entry placed, one side of a path, one hunk and one file's result with its counts. | `Placed`; `SideReading`; `HunkResult`; `FileResult` | mcp/src/agents_remember/application/review_lane_classification.py:192-199; mcp/src/agents_remember/application/review_lane_classification.py:202-217; mcp/src/agents_remember/application/review_lane_classification.py:220-227; mcp/src/agents_remember/application/review_lane_classification.py:230-249 |
| The comparison's changed paths, from the landed change inventory. | "def observe(self) -> TreePaths:" | mcp/src/agents_remember/application/review_lane_classification.py:257-264 |
| The file bucket, read without any hunk. | "def bucket(self, path: str)"; `_reading` | mcp/src/agents_remember/application/review_lane_classification.py:277-277; mcp/src/agents_remember/application/review_lane_classification.py:282-288 |
| The exact-blob rule and the other reasons an entry supplies no range. | `_place`; "if recorded != blob:" | mcp/src/agents_remember/application/review_lane_classification.py:290-316 |
| One path whole: bucket, the gate's hunks, and the non-text fact. | "def classify(self, change: TreeChange) -> FileResult:"; "hunks = change_hunks(self.code, change, before.blob, after.blob)" | mcp/src/agents_remember/application/review_lane_classification.py:317-340 |
| The trees opened once; a side with no index or an unopenable one named. | `open_tree_lane`; `_side` | mcp/src/agents_remember/application/review_lane_classification.py:346-364; mcp/src/agents_remember/application/review_lane_classification.py:367-384 |
| A range resolved at its own recorded blob, through the placements the cards read shares. | `_placement`; "PLACEMENTS.get(key)" | mcp/src/agents_remember/application/review_lane_classification.py:387-402 |
| The three buckets. | `_bucket` | mcp/src/agents_remember/application/review_lane_classification.py:408-418 |
| Bounded text and at most ten named entries. | `bounded_text`; `_named` | mcp/src/agents_remember/application/review_lane_classification.py:421-424; mcp/src/agents_remember/application/review_lane_classification.py:427-432 |
| The bucket reasons. | `_attributed_reason`; `_unknown_facts`; `_withheld` | mcp/src/agents_remember/application/review_lane_classification.py:435-446; mcp/src/agents_remember/application/review_lane_classification.py:449-456; mcp/src/agents_remember/application/review_lane_classification.py:459-467 |
| Only sides with changed lines are intersected (the exported `changes_lines`, MIK-L33); linked, unknown or unexplained. | "def changes_lines(hunk: Hunk, side: LaneSideName) -> bool:"; `_intersects`; `_links`; `_classified` | mcp/src/agents_remember/application/review_lane_classification.py:473-476; mcp/src/agents_remember/application/review_lane_classification.py:479-483; mcp/src/agents_remember/application/review_lane_classification.py:486-494; mcp/src/agents_remember/application/review_lane_classification.py:497-505 |
| Why a hunk is attribution unknown, per side, with every withheld entry. | `_unknown` | mcp/src/agents_remember/application/review_lane_classification.py:508-522 |
| The gate's non-text linkage, unknown unless both sides were read whole (review F3). | `_gate`; "if not (before.side.complete and after.side.complete):" | mcp/src/agents_remember/application/review_lane_classification.py:525-540 |
| The hunks the gate and the lane share (definition 2). | `change_hunks` | mcp/src/agents_remember/application/knowledge_worklist/code.py:342-361 |
| The gate's non-text predicate, now shared (definition 8). | `non_text_linked` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:592-598 |
| The lane's reads over this module. | `lane_summary`; `unexplained_lane`; `classify_changed_path` | mcp/src/agents_remember/application/review_unexplained_lane.py:87-110; mcp/src/agents_remember/application/review_unexplained_lane.py:129-155; mcp/src/agents_remember/application/review_unexplained_lane.py:226-244 |
| Buckets, exact-blob hunks, pre- and post-curation. | `test_every_changed_file_takes_one_bucket_and_the_destinations_reconcile`; `test_hunks_are_classified_on_their_changed_lines_at_each_sides_recorded_blob` | mcp/tests/test_review_unexplained_lane.py:356-373; mcp/tests/test_review_unexplained_lane.py:447-474 |
| An unread side, a partial index, and bounded reasons. | `test_an_unreadable_side_is_never_unexplained_and_the_readable_side_still_links`; `test_a_partial_index_makes_only_its_unparsed_files_unknown`; `test_a_reason_names_a_bounded_number_of_entries` | mcp/tests/test_review_unexplained_lane.py:515-532; mcp/tests/test_review_unexplained_lane.py:545-561; mcp/tests/test_review_unexplained_lane.py:574-593 |
| `changes_lines` is exported, the lane's own helper renamed with its one caller, and the change kinds reuse it (MIK-L33, review R1 note). | "\"changes_lines\","; "if not ("; "_non_text_content(result) or any(changes_lines(one.hunk, name) for one in result.hunks)" | mcp/src/agents_remember/application/review_lane_classification.py:95-95; mcp/src/agents_remember/application/review_change_kinds.py:615-617 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-R33:** `_changes_lines` is exported as `changes_lines` (renamed, with a docstring, its one caller updated), so MIK-L33's change kinds reuse the lane's own rule instead of a duplicate (review R1 note, ruling 2026-09-30T17:47:43); the lane's behaviour is unchanged. **Reopened claim reworded and re-anchored** on the line-exact `changes_lines` declaration (its old anchor `_changes_lines` no longer exists); its ranges re-measured. One row added. The other moved rows were re-pointed by the installed fixer (its bullets kept) or the exact base-to-staged line shift.
- 2026-09-30T20:23:46+00:00: Generated citation repair: `NAMED_ENTRIES`; `DETAIL_LIMIT` repointed to mcp/src/agents_remember/application/review_lane_classification.py:103-103; mcp/src/agents_remember/application/review_lane_classification.py:104-104. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09 (the docstring only).** L09 review R1 F8 rewrote the docstring's "Only changed lines are intersected" paragraph: the gate's linkage is now the same symmetric per-side rule (definition 8), and the two views differ only in where ranges come from. One Invariants bullet records it. The module-docstring row and the rows below it were re-pointed or normalised by the installed fixer (its bullets are kept, since no claim was reworded).
- 2026-09-30T17:59:32+00:00: Generated citation repair: `NAMED_ENTRIES`; `DETAIL_LIMIT` repointed to mcp/src/agents_remember/application/review_lane_classification.py:102-102; mcp/src/agents_remember/application/review_lane_classification.py:103-103. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new module MIK-R32 adds, recording rulings 2026-09-30T12:19:20 Q2 (the exact-blob rule, carried to L37) and Q7 (renames), review R1 F3 (the gate linkage is unknown over a partial index) and F4 (bounded reasons), both fixed at 13:07:38, and three candidate invariants. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
