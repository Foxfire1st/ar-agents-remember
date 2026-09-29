# mcp/tests/test_knowledge_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rules 1–5 and the Failure rule: sources, key, answers, partial state, cache and the `knowledge-index` command.** Every case builds a real memory tree in a real Git repository (`write_review_tree`) and indexes it through the public cache, so the key, the capture and the Git-object reads are the production ones. Registered in the `unit-regression` lane; 22 collected cases (the index-flag case is parametrized over both flags; MIK-R04 added the root-route case).

## Code Commentary

### Logic

- **Sources and key:** a working tree and its Git tree index to the same key and answers; a historical tree is read through objects without a checkout (HEAD and status unchanged); the key equals `HEAD^{tree}` when clean, `git stash create`'s tree when edited, is restored by reverting, is equal for an identical copy, and ignores an ignored `overview.index.json`; capturing writes nothing (index bytes, object set and status unchanged); a plain directory has no key.
- **Answers:** path lookups, the invariant answer (code, tests, families, links, history), family members and routes with routes answering their families, a family routed at the root route `.` governing both a root-level file and a deep file (MIK-R04, added by leaf 260928-MIK-L04 for review R3-1), incoming links, and history rows by subject and by leaf (the index query moved here from MIK-R07).
- **Freshness and failure:** an edited working tree is never answered from the previous content; a file failing its schema marks the index `partial` and is named; an unconverted tree indexes empty and says so.
- **Cache:** reuse, rebuild and loss-free deletion; eviction by age and size; a cache inside a Git working tree is refused with no directory left behind; an `assume-unchanged` or `skip-worktree` flag never hides an edit; the file declares its format and key.
- **Command and filter:** `knowledge-index` reports JSON and exits 0/1/2 by state; the index reads the files the validator reads (knowledge record, hidden directory, route cache, census, Markdown).

### Conventions

- The `memory` fixture writes the review tree and commits it; the `cache` fixture places the cache under `tmp_path`, outside the repository.

### Invariants And Boundaries

- Each packet obligation has a case that drives real Git state, not a stub.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixtures: a committed review tree and a cache outside it. | `memory`; `cache` | mcp/tests/test_knowledge_index.py:46-58 |
| Sources and key. | `test_a_working_tree_and_its_git_tree_index_to_the_same_key_and_answers`; `test_a_historical_git_tree_is_read_through_objects_without_a_checkout`; `test_the_key_is_the_tree_id_of_the_captured_state_and_depends_on_content_only`; `test_capturing_a_key_writes_nothing_into_the_repository`; `test_a_directory_outside_git_has_no_key` | mcp/tests/test_knowledge_index.py:68-151 |
| Answers. | `test_path_lookups_return_realizations_and_proofs`; `test_an_invariant_answers_its_code_tests_families_links_and_history`; `test_a_family_answers_members_and_routes_and_routes_answer_their_families`; `test_incoming_links_reach_any_record`; `test_history_rows_are_found_by_subject_and_by_leaf` | mcp/tests/test_knowledge_index.py:157-259 |
| A family routed at the root governs every path. | `test_a_family_routed_at_the_root_governs_every_path` | mcp/tests/test_knowledge_index.py:217-232 |
| Freshness, partial state and an unconverted tree. | `test_an_edited_working_tree_is_never_answered_from_the_previous_content`; `test_a_file_failing_its_schema_marks_the_index_partial_and_is_named`; `test_an_unconverted_tree_is_indexed_empty_and_says_so` | mcp/tests/test_knowledge_index.py:265-327 |
| Cache, flags and format. | `test_the_cache_reuses_rebuilds_and_loses_nothing_when_deleted`; `test_old_and_excess_index_files_are_evicted`; `test_the_cache_is_never_placed_inside_a_git_working_tree`; `test_an_index_flag_never_hides_an_edit_from_the_key`; `test_the_index_file_declares_its_format_and_key` | mcp/tests/test_knowledge_index.py:333-414 |
| The command and the shared file filter. | `test_the_command_reports_the_index_and_exits_by_state`; `test_the_index_reads_the_files_the_validator_reads` | mcp/tests/test_knowledge_index.py:417-464 |
| The lane row. | "mcp/tests/test_knowledge_index.py" | mcp/tests/test-evidence-lanes.toml:102-102 |

## Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — one MIK-R04 case: a family routed at `.` governs every path.** The Answers bullet names it and one row is added. The other rows were re-pointed by the exact line shift (one import line, the 19-line case), their claims unchanged; the lane row now reads `:102`. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
