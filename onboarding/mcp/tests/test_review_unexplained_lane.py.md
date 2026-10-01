# mcp/tests/test_review_unexplained_lane.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R32's backend evidence: file buckets, hunk classes, destinations, the per-file response and the entry count
(11 collected cases, 709 lines).** Each comparison is four real Git trees: a code repository with a base and a
candidate commit, and a converted memory repository with a base and a candidate commit, reopened as the reviewer
reopens a recorded comparison (`reopened_trees`), so every knowledge side is read through the derived index of its
tree. The route and live-leaf cases reuse `test_review_git_trees.py`'s `world` fixture. Registered in the
`unit-regression` lane (`test-evidence-lanes.toml:125`).

## Code Commentary

### Logic

- **The fixture (ten changed paths, one code change throughout).** `pkg/a.py` (a replace inside `land` and a new
  function appended; symbol entries for `land` and `keep`), `pkg/lines.txt` (two adjacent replaces and a delete; one
  `line_range` over lines 2-3), `pkg/whole.py` (a `file` entry), `pkg/stale.py` (an entry recorded at a blob neither
  side holds), `pkg/unbound.py` (a symbol the file does not define), `tests/test_a.py` (one proof entry with a facet),
  `pkg/mode.py` (mode change only; a symbol entry), `pkg/new.py` (added, no entry), `pkg/data.bin` (a binary rewrite
  with a `file` entry) and `pkg/inside.py` (a line inserted strictly inside `f`). `_knowledge` builds the memory
  tree; `curated=True` re-records `pkg/a.py` at the candidate blob. `BEFORE_FAMILIES` and `AFTER_FAMILIES` make one
  family keep A, one reassign it to B, and one exist only before.
- **Cases:**
  1. `test_every_changed_file_takes_one_bucket_and_the_destinations_reconcile`: 10 files = 7 attributed + 1
     unexplained + 2 unknown; the `Unexplained changes` destination lists `pkg/new.py`, then `pkg/lines.txt` (its
     delete-only run) and `pkg/mode.py` (the mode-only change the gate holds unexplained); the `Unknown attribution`
     destination lists the stale and the unresolved file with their reasons, then `a.py`, `inside.py` and
     `lines.txt`; `_every_path_bucket` checks `paths` (ruling Q1: the stale file unknown, the proof-linked test
     attributed); the summary agrees; the binary with a `file` entry is gate-`linked` and listed nowhere.
  2. `test_the_entry_count_reads_file_buckets_only`: with `CodeTrees.hunks` patched to fail, the summary still
     counts and the lane read fails (rule 9's request economy).
  3. `test_hunks_are_classified_on_their_changed_lines_at_each_sides_recorded_blob`: pre-curation, `land`'s edit
     links through the before side and the appended function is `attribution_unknown` (the after entries carry
     `recorded_blob_mismatch`); `lines.txt` gives linked, unknown and unexplained; the insertion inside `f` is
     unknown (the gate would call it hit); a resolving `file` entry links every line; after curation the insertion
     is `unexplained` and the edit links on both sides.
  4. `test_a_linked_hunk_names_its_entries_revisions_and_family_occurrences`: the invariant revision and its keys;
     `member`, `removed_or_reassigned` and `before_only`; the proof link with `kind: proof` and its facet;
     `confirmed_no_family`.
  5. `test_an_unreadable_side_is_never_unexplained_and_the_readable_side_still_links`: a memory base tree Git
     cannot produce: no file is unexplained, the readable side still links, changed lines on the unread side are
     `knowledge_unavailable`, and the mode change's gate linkage is `unknown`.
  6. `test_a_partial_index_makes_only_its_unparsed_files_unknown`: an unparsable after sidecar makes only
     `pkg/new.py` unknown; an unparsable before family record makes membership `membership_unknown`; and (review R1
     F3) the mode change's gate linkage is `unknown`, listed under `Unknown attribution`, never "gate unexplained".
  7. `test_a_reason_names_a_bounded_number_of_entries` (review R1 F4): 300 stale entries at one path; the reason
     says "300 entries" and "and 290 more", names ten IDs per side, the hunk still carries all 300, and the lane
     answers `measured`.
  8. `test_an_unmeasured_change_set_has_no_count`: a non-UTF-8 name makes both reads `partial` naming it; a code
     tree Git cannot produce is `unavailable` with no destinations and a typed refusal; an index failing mid-read
     is `unavailable`.
  9. `test_the_route_asks_one_focused_question_at_a_time`: `lane=files` and `file=` reach the port; `lane=all`,
     `lane` with `file`, and `invariants` with `file` are 400.
  10. `test_a_live_tree_leaf_serves_the_lane_and_its_entry_count`: on the live tree leaf, the summary carries a
      counted `attribution`, the lane read lists the new file, a changed path is classified, an unchanged path is
      refused, and (review R1 F2, `_long_paths_are_typed_refusals`) `file=` values of 1,025 and 4,096 characters
      answer the typed 200 refusal with a 1,024-character `offending_input`.
  11. `test_a_dataset_review_entry_carries_no_attribution`: an unconverted leaf's summary has no `attribution`.

### Conventions

- `_no_bound_services` resets the worktree services after each case, as in the git-trees module.
- The module imports `world` from `test_review_git_trees.py` (with `noqa: F811` on its uses).

### Invariants And Boundaries

- Proves the candidate invariants recorded on `review_lane_classification.py.md` and `review_unexplained_lane.py.md`:
  one classification through MIK-R08's functions, the exact-blob rule, unknown rather than "gate unexplained" over a
  side not read whole, the explorer's `paths`, and typed answers to every validated request.
- **Mutation checks (worker and reviewer):** relaxing the exact-blob rule, intersecting every side and dropping
  proofs each fail 3 cases; a stale file counted as unexplained fails 2; the gate ignoring an unread side fails 1;
  the old unavailable-only gate rule fails case 6; uncapped names fail case 7; an unclipped refusal fails case 10.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R32@v1` (adopting `ICR-R33@v1`) and its rulings in `32_unexplained-changes-lane.json`; they live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The ten changed paths the fixture comparison holds. [1]
- The memory tree over the code, and the curated re-record of `pkg/a.py`. [2]
- The family records before and after. [3]
- A comparison reopened as the reviewer reopens it. [4]
- Buckets, destinations, paths and the summary agree. [5]
- The entry count reads no hunk. [6]
- Hunks on their changed lines at each side's recorded blob, before and after curation. [7]
- Links, revisions, proofs and membership. [8]
- An unread side and a partial index (review F3). [9]
- Bounded reasons (review F4). [10]
- Unmeasured change sets carry no count. [11]
- One focused question per request. [12]
- The live tree leaf, and long paths answered typed (review F2). [13]
- A dataset review's entry has no attribution. [14]
- The module's lane row. [15]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
