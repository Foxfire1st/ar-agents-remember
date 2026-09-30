# mcp/tests/test_review_git_trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_git_trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R25 cases for the reviewer on Git trees, and since MIK-L31 the focused-card read (19 collected): four
trees, pins, the tree view, reopen, legacy, the pin-naming round trip, the cards' entries, and the proof admission at
the route.** The `world` fixture is a coordination root holding one task (`task.json` with an
id) and one leaf enclosure, a code repository and a converted memory repository (`main` is the official line of
both; the memory commit carries the `Code-Commit` trailer), and the leaf's two linked worktrees on their work
branches. The leaf edits code and knowledge without committing, which is the live review's ordinary state. The
archive-hook cases moved to `test_review_artifact_cleanup.py` (ruling 2026-09-30T02:32:42, the test split); this
file is 1,022 lines after MIK-L31. It uses no shared support module, so there is no catalog change; it runs in the
`unit-regression` lane (`test-evidence-lanes.toml:123`).

## Code Commentary

### Logic

- **Rule 1:** four trees with the uncommitted candidates pinned and reused; committed candidates need no ref and a
  failed pin refuses naming the repository and the ref; **a read writes only review refs and comparison objects,
  and a repeat writes nothing** (every ref, every object and every record file, bytes and mtime, compared by
  `_state`; ruling 22:22:37 Q5).
- **Rule 2 and 3:** the tree view shows the knowledge diff grouped by record and by source, the currentness per
  side and the worklist; a partial index shows its state on the affected side. Since MIK-L31 every key is
  snake_case, including the owners' own documents (`code_tree`, `tree_id`, `stale_members`, `owner_kind`; MIK-L25
  review F9), and the leaf-wide view carries no entries.
- **Rule 4:** a comparison reopens from its tree ids and names a tree Git can no longer produce (the refs deleted
  and both repositories garbage-collected; the code trees too, review F4); an unconverted before side is compared as
  its conversion; a comparison recorded before the conversion keeps its code sides only.
- **The no-`.sqlite` check:** every `apsw.Connection` and `sqlite3.connect` is recorded and every open lies inside
  `runtime/knowledge-index` (ruling 22:22:37 Q1).
- **Preservation:** an unconverted leaf keeps the dataset review; a tree comparison is never frozen into a dataset
  generation.
- **Naming:** pins are named by the task directory name, and archival removes them (ruling 02:32:42 (a); the one
  case here that calls the hook, to prove the round trip).
- **The route:** served over the port, and 503 when unwired. Since MIK-L31: the numbered read for the live leaf's
  current comparison keeps its `computed` worklist (review F11), a cards read passes its invariants to the port, a
  65-character key and 501 keys are each a 400 (review F10 and ruling Q2's bound).
- **The cards read (MIK-L31):**
  - `test_the_cards_read_locates_each_entry_of_the_named_invariants_on_both_code_sides`: K_C retires `keep`
    (RLZ-A00002), adds a proof PRF-A00003 and a realization of a gone name (RLZ-A00004); the four entries come back in
    order with one invariant key. The helpers assert one changed range with each side's own excerpt and MIK-R03
    state (`_changed_range`), the retired entry located on both sides with its text carried once and unrecorded
    after (`_retired_entry`), the proof's facet with no role (`_proof_entry`), and the unresolved entry with a reason
    and no range (`_unresolved_entry`). An identity no tree holds contributes nothing.
  - `test_the_cards_read_names_an_unreadable_side_unavailable_and_a_missing_file_absent`: a deleted file is
    `absent` and `changed`; an unreadable candidate tree is `unavailable` with its problem, `undetermined`, and no
    excerpt.
  - `test_history_rows_are_found_by_the_row_subject_an_item_names`: the PS-1 lookup through `facts.row`.
  - Review F3: `test_an_excerpt_longer_than_its_bound_is_a_stated_prefix` (a 500-line range gives the first 400
    lines with `excerpt_truncated`) and `test_the_placement_cache_remembers_answers_only_and_stays_within_its_bound`
    (an answer is remembered, a `CodeReadError` is asked again, the table evicts past its bound, `PLACEMENTS` is
    8,192).
  - Review F12 (ruling Q1 at the route): `test_an_unchanged_path_only_a_proof_names_opens_in_a_tree_review` adds an
    unchanged test file with its paired memory commit; before a proof exists the content read refuses it, after a
    K_C proof it is `attributed_unchanged` with the detail "a realization or proof recorded for the path in the
    comparison's after knowledge" naming "the after snapshot records a proof here". `_inventory` and `_named`
    assert the payload and the tree IDs before use (review R2-1's pyright fix).

### Conventions

- The module's docstring still ends "… archive" although the archive cases moved out (reviewer R6 note 3,
  cosmetic).

### Invariants And Boundaries

- These cases prove the candidate invariants recorded on `application/review_tree_comparison.py`: pins before
  display and idempotent re-reads; directory-name refs; `unavailable-history` never substituted; unconverted reads
  unchanged. Since MIK-L31 they also prove the one recorded on `application/review_tree_entries.py` (a card excerpt
  only from the pinned tree's exact blob, bounded, with per-side state) and the server half of the one on
  `application/review_tree_knowledge.py` (a numbered read answers for exactly that comparison).
- The radon D block `test_the_tree_view_shows_…` rose from D26 to D28 in MIK-L31 (review R1, pre-existing D).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` lives outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The converted-memory fixture world with its live leaf. | `World`; `world` | mcp/tests/test_review_git_trees.py:190-266; mcp/tests/test_review_git_trees.py:277-309 |
| Pins and reuse. | `test_a_live_review_is_four_trees_with_its_uncommitted_candidates_pinned_and_reused` | mcp/tests/test_review_git_trees.py:343-388 |
| A repeat read writes nothing. | `_state`; `test_a_read_writes_only_review_refs_and_comparison_objects_and_a_repeat_writes_nothing` | mcp/tests/test_review_git_trees.py:391-406; mcp/tests/test_review_git_trees.py:409-429 |
| Committed candidates and the refused pin. | `test_committed_candidates_need_no_ref_and_a_failed_pin_refuses_naming_repository_and_ref` | mcp/tests/test_review_git_trees.py:432-456 |
| The tree view (every key snake_case, no entries leaf-wide, the history row's `owner_kind`) and the partial index. | `test_the_tree_view_shows_the_knowledge_diff_currentness_per_side_and_the_worklist`; `test_a_partial_index_shows_its_state_on_the_affected_side` | mcp/tests/test_review_git_trees.py:462-505; mcp/tests/test_review_git_trees.py:514-525 |
| Reopen, the converted base, and the legacy comparison. | `test_a_comparison_reopens_from_its_tree_ids_and_names_a_tree_git_can_no_longer_produce`; `test_an_unconverted_before_side_is_compared_as_its_conversion`; `test_a_comparison_recorded_before_the_conversion_keeps_its_code_sides_only` | mcp/tests/test_review_git_trees.py:531-580; mcp/tests/test_review_git_trees.py:583-621; mcp/tests/test_review_git_trees.py:624-653 |
| No database but the index; unconverted unchanged; never frozen. | `test_no_review_path_opens_a_database_other_than_the_derived_index`; `test_an_unconverted_leaf_keeps_the_dataset_review`; `test_a_tree_comparison_is_never_frozen_into_a_dataset_generation` | mcp/tests/test_review_git_trees.py:656-681; mcp/tests/test_review_git_trees.py:684-698; mcp/tests/test_review_git_trees.py:701-711 |
| Directory-name pins, and the route with the pinned numbered read, the cards read and the key bounds. | `test_pins_are_named_by_the_task_directory_and_archival_removes_them`; `test_the_tree_view_route_serves_the_port_and_refuses_when_unwired` | mcp/tests/test_review_git_trees.py:717-727; mcp/tests/test_review_git_trees.py:730-776 |
| The cards read: four entries located on both sides, each helper's per-entry facts. | `_with_proof_and_unresolved`; `test_the_cards_read_locates_each_entry_of_the_named_invariants_on_both_code_sides`; `_changed_range`; `_retired_entry`; `_proof_entry`; `_unresolved_entry` | mcp/tests/test_review_git_trees.py:779-860 |
| Unavailable against absent, and the history row found through `facts.row`. | `test_the_cards_read_names_an_unreadable_side_unavailable_and_a_missing_file_absent`; `test_history_rows_are_found_by_the_row_subject_an_item_names` | mcp/tests/test_review_git_trees.py:863-883; mcp/tests/test_review_git_trees.py:886-897 |
| The excerpt bound and the placement cache (review F3). | `test_an_excerpt_longer_than_its_bound_is_a_stated_prefix`; `test_the_placement_cache_remembers_answers_only_and_stays_within_its_bound` | mcp/tests/test_review_git_trees.py:900-913; mcp/tests/test_review_git_trees.py:916-936 |
| The proof admission at the route (review F12), with the asserted payload and tree IDs (R2-1). | `_inventory`; `_named`; `test_an_unchanged_path_only_a_proof_names_opens_in_a_tree_review` | mcp/tests/test_review_git_trees.py:939-947; mcp/tests/test_review_git_trees.py:950-1016 |
| The lane row. | "mcp/tests/test_review_git_trees.py" | mcp/tests/test-evidence-lanes.toml:123-123 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose (19 collected, 1,022 lines, lane row now `:123` after L05's row) and Logic record the snake_case assertions (MIK-L25 review F9), the route's pinned numbered read, cards read and key bounds (review F10, F11; ruling Q2), the cards-read cases with their four helpers, the F3 bound cases, the PS-1 row-subject case and the F12 route case for ruling Q1 (with R2-1's asserted payload and IDs). **Reopened claim reworded:** the tree-view row; this pass's generated bullet for it was removed. Four rows added; the route row reworded.
- 2026-09-30T07:54:18+00:00: Generated citation repair: `test_no_review_path_opens_a_database_other_than_the_derived_index`; `test_an_unconverted_leaf_keeps_the_dataset_review`; `test_a_tree_comparison_is_never_frozen_into_a_dataset_generation` repointed to mcp/tests/test_review_git_trees.py:656-681; mcp/tests/test_review_git_trees.py:684-698; mcp/tests/test_review_git_trees.py:701-711. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:54:18+00:00: Generated citation repair: "mcp/tests/test_review_git_trees.py" repointed to mcp/tests/test-evidence-lanes.toml:123-123. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new test file MIK-R25 adds, recording rulings 22:22:37 (Q1, Q5), 23:15:34 (F4) and 02:32:42 (a, the test split). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
