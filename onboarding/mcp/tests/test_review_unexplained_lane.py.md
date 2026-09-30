# mcp/tests/test_review_unexplained_lane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_unexplained_lane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R32@v1` (adopting `ICR-R33@v1`) and its rulings in `32_unexplained-changes-lane.json`; they live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ten changed paths the fixture comparison holds. | "the same throughout:" | mcp/tests/test_review_unexplained_lane.py:1-21 |
| The memory tree over the code, and the curated re-record of `pkg/a.py`. | `_knowledge` | mcp/tests/test_review_unexplained_lane.py:208-277 |
| The family records before and after. | `BEFORE_FAMILIES`; `AFTER_FAMILIES` | mcp/tests/test_review_unexplained_lane.py:280-281 |
| A comparison reopened as the reviewer reopens it. | `Lane`; `precuration` | mcp/tests/test_review_unexplained_lane.py:284-323 |
| Buckets, destinations, paths and the summary agree. | `test_every_changed_file_takes_one_bucket_and_the_destinations_reconcile`; `_every_path_bucket`; `_unexplained_destination`; `_unknown_destination` | mcp/tests/test_review_unexplained_lane.py:356-427 |
| The entry count reads no hunk. | `test_the_entry_count_reads_file_buckets_only` | mcp/tests/test_review_unexplained_lane.py:430-441 |
| Hunks on their changed lines at each side's recorded blob, before and after curation. | `test_hunks_are_classified_on_their_changed_lines_at_each_sides_recorded_blob`; `_precuration_edit_and_insertion` | mcp/tests/test_review_unexplained_lane.py:447-490 |
| Links, revisions, proofs and membership. | `test_a_linked_hunk_names_its_entries_revisions_and_family_occurrences` | mcp/tests/test_review_unexplained_lane.py:493-509 |
| An unread side and a partial index (review F3). | `test_an_unreadable_side_is_never_unexplained_and_the_readable_side_still_links`; `test_a_partial_index_makes_only_its_unparsed_files_unknown`; `_gate_unknown_on_a_partial_side` | mcp/tests/test_review_unexplained_lane.py:515-571 |
| Bounded reasons (review F4). | `test_a_reason_names_a_bounded_number_of_entries` | mcp/tests/test_review_unexplained_lane.py:574-593 |
| Unmeasured change sets carry no count. | `test_an_unmeasured_change_set_has_no_count` | mcp/tests/test_review_unexplained_lane.py:596-618 |
| One focused question per request. | `test_the_route_asks_one_focused_question_at_a_time` | mcp/tests/test_review_unexplained_lane.py:624-645 |
| The live tree leaf, and long paths answered typed (review F2). | `test_a_live_tree_leaf_serves_the_lane_and_its_entry_count`; `_long_paths_are_typed_refusals` | mcp/tests/test_review_unexplained_lane.py:659-695 |
| A dataset review's entry has no attribution. | `test_a_dataset_review_entry_carries_no_attribution` | mcp/tests/test_review_unexplained_lane.py:698-703 |
| The module's lane row. | "mcp/tests/test_review_unexplained_lane.py" | mcp/tests/test-evidence-lanes.toml:125-125 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new test module (11 cases), recording ruling 2026-09-30T12:19:20 Q1 (`_every_path_bucket`) and review R1 F2, F3 and F4 (fixed at 13:07:38) with their mutation checks. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
