# mcp/src/agents_remember/application/review_lane_classification.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R32@v1` (adopting `ICR-R33@v1` with substitutions) and its rulings in `32_unexplained-changes-lane.json`; they
live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: one classification, no hunk arithmetic of its own, and where it differs from the gate. [1]
- The bounds on a reason: ten named entries, clipped details. [2]
- A side's knowledge of one path: an unread side, or the path's own unparsed sidecar. [3]
- A side read whole; realization and proof entries at a path; family records all read. [4]
- One entry placed, one side of a path, one hunk and one file's result with its counts. [5]
- The comparison's changed paths, from the landed change inventory. [6]
- The file bucket, read without any hunk. [7]
- The exact-blob rule and the other reasons an entry supplies no range. [8]
- One path whole: bucket, the gate's hunks, and the non-text fact. [9]
- The trees opened once; a side with no index or an unopenable one named. [10]
- A range resolved at its own recorded blob, through the placements the cards read shares. [11]
- The three buckets. [12]
- Bounded text and at most ten named entries. [13]
- The bucket reasons. [14]
- Only sides with changed lines are intersected (the exported `changes_lines`, MIK-L33); linked, unknown or unexplained. [15]
- Why a hunk is attribution unknown, per side, with every withheld entry. [16]
- The gate's non-text linkage, unknown unless both sides were read whole (review F3). [17]
- The hunks the gate and the lane share (definition 2). [18]
- The gate's non-text predicate, now shared (definition 8). [19]
- The lane's reads over this module. [20]
- Buckets, exact-blob hunks, pre- and post-curation. [21]
- An unread side, a partial index, and bounded reasons. [22]
- `changes_lines` is exported, the lane's own helper renamed with its one caller, and the change kinds reuse it (MIK-L33, review R1 note). [23]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
