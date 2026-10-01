# mcp/src/agents_remember/application/review_tree_entries.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The server side of the reviewer's focused expression cards (MIK-R31): every realization and proof entry of the
named invariants, located on both code sides of one tree comparison, with the range's text.** For a comparison of
four Git trees (MIK-R25), `tree_entries` lists each entry ID that the memory tree K_B or K_C holds for the named
invariants, and places it on the code base B and the code candidate C with the worklist's own resolution
(`CodeTrees.resolve`, MIK-R08 definition 3). Each side carries the side's own authored fields (role and rationale
for a realization, facet for a proof), its MIK-R03 entry state through `observe_entry`, and the resolved range's
excerpt from that side's exact blob.

The read is on demand: `application/review_tree_knowledge.py` calls it only when the query names invariants
(`/api/review/trees?invariants=`, ruling 2026-09-30T05:36:19 Q2). Carrying every entry's excerpt leaf-wide measured
637 KB on the real repository; one family's card read measured about 38 KB (the captured body is 38,264 bytes).

## Code Commentary

### Logic

- **Which entries.** `_side` opens each memory side's derived index (no side read means `unreadable` with the
  side's own detail); `_entries_of` walks `record_ids("invariant")` and keeps an invariant whose
  `text_uuid("identity", …)` is among the wanted keys, the identity the landed review payload addresses invariants
  by. A key no memory tree holds contributes nothing.
- **One entry, two sides.** `_entry` takes each side's own entry, else the other side's (so an added entry still
  shows the region it names at B, and a retired one at C). `_located` sets `recorded` (`None` when the memory side
  could not be read), the authored fields only from the side's own entry (`_authored`; empty text is `None`, never
  a placeholder), and the currentness only where the side records the entry (`_currentness`).
- **Where it lands.** `_placed` answers `unavailable` (the code tree could not be opened, with its problem) or
  `absent` (no regular file at the path), else `_in_blob`: `_unsupported` refuses a locator kind other than
  `symbol`, `line_range` or `file`, a symbol in a file no shipped grammar reads, and a `line_range` whose recorded
  blob the store cannot give (`unavailable`, never guessed). `_resolve` then asks `CodeTrees.resolve`; `None` is
  `unresolved` with the reason `_unresolved` names; a `CodeReadError` or a failed Git read is `unavailable`.
  **Since MIK-R09 (L09 review R3-2, ruling 2026-09-30T19:16:07)** the `_unsupported` probe runs inside the same
  `try`: its `has_blob` call now raises a `CodeReadError` when Git cannot say whether it holds the recorded blob
  (`CodeTrees.has_blob`), and that is `unavailable` with the named reason instead of an unhandled error. Git's
  documented not-found answer is still the probe's "the store cannot give" `unavailable`. This is one of L09's stated
  exceptions to "inert until the cutover" (with `has_blob` itself and the conversion's Git-failure naming): it is not
  behind the gate's marker probe, and it changes only what a Git failure reads as, from an escaping error to a named
  `unavailable`.
- **The excerpt.** `_excerpt` slices lines `start..end` of the exact blob with `blob_lines`, keeps at most
  `EXCERPT_MAX_LINES` (400) lines and `EXCERPT_MAX_CHARACTERS` (48,000) characters, sets `excerpt_truncated` when it
  cut, and never re-encodes: a range that is not UTF-8 carries a reason and no excerpt, and a blob the store cannot
  give is named.
- **The change.** `_change` compares the two resolved ranges' content identities: `unchanged` or `changed`;
  resolved on one side and `absent` on the other is `changed` (an added or deleted file); anything else is
  `undetermined`. An `unchanged` entry keeps its excerpt on the after side only (one content identity, one text).
- **Order.** `tree_entries` sorts by invariant, kind, path and ID; the client applies MIK-R01's family order.
- **The placement cache.** `PLACEMENTS` is a `BoundedMemo` of 8,192 entries keyed by `observation_key` (the
  observation cache's bound and key). Only answers are remembered, including "does not resolve"; a read that
  raised is asked again.

### Conventions

- Nothing is written, re-anchored or judged, and no text is supplied that the entry does not carry.
- Each path's blob comes from the pinned code tree's listing (`code.files`); the anchor's recorded blob is used
  only to map a line range, never as the excerpt's source (review R1 focus check 2).

### Invariants And Boundaries

- **Candidate invariant (not ingested): a card excerpt comes only from the pinned tree's exact blob, bounded, with
  per-side state.** Realized by `_placed`, `_in_blob`, `_excerpt` and `_change`. Proved by
  `test_the_cards_read_locates_each_entry_of_the_named_invariants_on_both_code_sides`,
  `test_the_cards_read_names_an_unreadable_side_unavailable_and_a_missing_file_absent`,
  `test_an_excerpt_longer_than_its_bound_is_a_stated_prefix`, and the reviewer's real-data check (an excerpt equal
  to `git cat-file blob <side blob>` sliced to its range, on both sides of RLZ-CXH58B4W).
- `absent` and `unavailable` are different facts and are never merged; an unresolved side names its reason and
  carries no range.
- The cache bound is tested (`test_the_placement_cache_remembers_answers_only_and_stays_within_its_bound`,
  review F3).
- Inert on the installed runtime: only a converted leaf's tree comparison reaches this module.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R31@v1` with its rulings in `31_focused-expression-cards.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The placement cache: 8,192 answers under the observation key. [1]
- Each entry of the named invariants on B and C, ordered by invariant, kind, path and ID. [2]
- A memory side's entries, or its unreadable detail; the invariants chosen by the payload's identity. [3]
- One entry on both sides; an unchanged entry's text carried once. [4]
- The side's own recorded flag, authored fields and MIK-R03 state. [5]
- Unavailable, absent, resolved or unresolved, from the pinned tree's own blob. [6]
- The bounded excerpt of the exact blob. [7]
- The cached resolution, and the locators refused before any read. [8]
- The caller: a query naming invariants gets only the entries, as one focused answer (since MIK-L32 through `_focused`, beside the lane and file reads). [9]
- The shapes this module fills. [10]
- The cases: four entries located, unavailable against absent, the excerpt bound and the cache bound. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
