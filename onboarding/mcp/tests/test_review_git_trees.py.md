# mcp/tests/test_review_git_trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_git_trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R25 cases for the reviewer on Git trees (13 collected): four trees, pins, the tree view, reopen, legacy,
and the pin-naming round trip.** The `world` fixture is a coordination root holding one task (`task.json` with an
id) and one leaf enclosure, a code repository and a converted memory repository (`main` is the official line of
both; the memory commit carries the `Code-Commit` trailer), and the leaf's two linked worktrees on their work
branches. The leaf edits code and knowledge without committing, which is the live review's ordinary state. The
archive-hook cases moved to `test_review_artifact_cleanup.py` (ruling 2026-09-30T02:32:42, the test split); this
file is 750 lines. It uses no shared support module, so there is no catalog change; it runs in the
`unit-regression` lane (`test-evidence-lanes.toml:122`).

## Code Commentary

### Logic

- **Rule 1:** four trees with the uncommitted candidates pinned and reused; committed candidates need no ref and a
  failed pin refuses naming the repository and the ref; **a read writes only review refs and comparison objects,
  and a repeat writes nothing** (every ref, every object and every record file, bytes and mtime, compared by
  `_state`; ruling 22:22:37 Q5).
- **Rule 2 and 3:** the tree view shows the knowledge diff grouped by record and by source, the currentness per
  side and the worklist; a partial index shows its state on the affected side.
- **Rule 4:** a comparison reopens from its tree ids and names a tree Git can no longer produce (the refs deleted
  and both repositories garbage-collected; the code trees too, review F4); an unconverted before side is compared as
  its conversion; a comparison recorded before the conversion keeps its code sides only.
- **The no-`.sqlite` check:** every `apsw.Connection` and `sqlite3.connect` is recorded and every open lies inside
  `runtime/knowledge-index` (ruling 22:22:37 Q1).
- **Preservation:** an unconverted leaf keeps the dataset review; a tree comparison is never frozen into a dataset
  generation.
- **Naming:** pins are named by the task directory name, and archival removes them (ruling 02:32:42 (a); the one
  case here that calls the hook, to prove the round trip).
- **The route:** served over the port, and 503 when unwired.

### Conventions

- The module's docstring still ends "… archive" although the archive cases moved out (reviewer R6 note 3,
  cosmetic).

### Invariants And Boundaries

- These cases prove the candidate invariants recorded on `application/review_tree_comparison.py`: pins before
  display and idempotent re-reads; directory-name refs; `unavailable-history` never substituted; unconverted reads
  unchanged.

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
| The converted-memory fixture world with its live leaf. | `World`; `world` | mcp/tests/test_review_git_trees.py:181-300 |
| Pins and reuse. | `test_a_live_review_is_four_trees_with_its_uncommitted_candidates_pinned_and_reused` | mcp/tests/test_review_git_trees.py:334-379 |
| A repeat read writes nothing. | `_state`; `test_a_read_writes_only_review_refs_and_comparison_objects_and_a_repeat_writes_nothing` | mcp/tests/test_review_git_trees.py:382-420 |
| Committed candidates and the refused pin. | `test_committed_candidates_need_no_ref_and_a_failed_pin_refuses_naming_repository_and_ref` | mcp/tests/test_review_git_trees.py:423-447 |
| The tree view and the partial index. | `test_the_tree_view_shows_the_knowledge_diff_currentness_per_side_and_the_worklist`; `test_a_partial_index_shows_its_state_on_the_affected_side` | mcp/tests/test_review_git_trees.py:453-513 |
| Reopen, the converted base, and the legacy comparison. | `test_a_comparison_reopens_from_its_tree_ids_and_names_a_tree_git_can_no_longer_produce`; `test_an_unconverted_before_side_is_compared_as_its_conversion`; `test_a_comparison_recorded_before_the_conversion_keeps_its_code_sides_only` | mcp/tests/test_review_git_trees.py:519-641 |
| No database but the index; unconverted unchanged; never frozen. | `test_no_review_path_opens_a_database_other_than_the_derived_index`; `test_an_unconverted_leaf_keeps_the_dataset_review`; `test_a_tree_comparison_is_never_frozen_into_a_dataset_generation` | mcp/tests/test_review_git_trees.py:644-699 |
| Directory-name pins and the route. | `test_pins_are_named_by_the_task_directory_and_archival_removes_them`; `test_the_tree_view_route_serves_the_port_and_refuses_when_unwired` | mcp/tests/test_review_git_trees.py:705-744 |
| The lane row. | "mcp/tests/test_review_git_trees.py" | mcp/tests/test-evidence-lanes.toml:122-122 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new test file MIK-R25 adds, recording rulings 22:22:37 (Q1, Q5), 23:15:34 (F4) and 02:32:42 (a, the test split). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
