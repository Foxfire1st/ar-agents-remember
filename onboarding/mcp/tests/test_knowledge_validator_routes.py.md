# mcp/tests/test_knowledge_validator_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_validator_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T00:17:15+02:00 |
| lastVerifiedCommitHash | `c493b55731545a090d6b81f504bf02e1e427ec74`|
| lastVerifiedCommitDate | 2026-09-30T00:38:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R22 rule 8: where the validator runs, with a refusal test at each point wired in this leaf.** The cases cover the Git tree readers, the commit-route adapter, the worktree gate, the managed sync after a merge (automatic and retained-conflict paths), and the curator's `knowledge-validate` command. Registered in the `unit-regression` lane (the integration lane is at its 400-case ceiling); 7 collected cases.

## Code Commentary

### Logic

- `test_git_trees_are_read_exactly_and_the_route_index_cache_is_ignored`: exact bytes through `read_git_blobs_bytes`, the cache and hidden directories skipped, a dot-named card read, and the directory and Git readers equal.
- `test_the_commit_route_adapter_refuses_naming_every_violation`: `GitKnowledgeValidation` over real commits: unconverted memory passes, a converted commit over an unconverted base is refused, an unreadable base is refused ("cannot read"), and a hand-added `[4]` is refused with its rendered line.
- `test_the_worktree_route_never_commits_converted_memory_unvalidated`: `memory_commit_refusal` refuses with no bound validator, with no paired code commit, and for an unreadable (`"0"*40`) tree, and passes unconverted memory.
- `test_the_managed_sync_refuses_a_merge_with_duplicate_ids_until_it_is_repaired`: a real `SyncFixture` sync is refused with `sync-knowledge-validation-refused` and the recovery line; `HEAD` is unchanged and `MERGE_HEAD` is the source; after `git rm` and a rerun, the sync completes with exact parents.
- `test_parallel_minted_ids_sync_cleanly`: the conforming example through the real sync.
- `test_the_standalone_command_validates_a_converted_fixture_tree`: the CLI passes the fixture (exit 0, "0 violation(s), 1 report-only finding(s)": since MIK-R27, leaf 260928-MIK-L27, the one report-only finding is the legacy count of the fixture's exported family), refuses an appended `[4]` with exit 1 and JSON output whose full sorted violation list is pinned with its report-only flags, `[("R22.3-markers", False), (LEGACY_COUNT, True)]` (review R1 finding F3, ruling 23:04:57), reports unconverted memory as out of scope (exit 0), and exits 2 for an unreadable `--base`.
- `test_a_resolved_memory_conflict_that_breaks_validation_is_refused_on_continue`: a real conflict resolved into duplicate IDs is refused on `continue` with the right state, then syncs after the repair.

### Conventions

- It imports `SyncFixture` from `test_worktree_sync.py` rather than duplicating it, and binds or restores worktree services around the gate tests.

### Invariants And Boundaries

- Each rule-8 integration point this leaf wires has a refusal test that drives real Git state, not a stub.

### Todos

MIK-R09's routes will add their own refusal tests.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The route cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Git readers. | `test_git_trees_are_read_exactly_and_the_route_index_cache_is_ignored` | mcp/tests/test_knowledge_validator_routes.py:74-96 |
| The adapter and the worktree gate. | `test_the_commit_route_adapter_refuses_naming_every_violation`; `test_the_worktree_route_never_commits_converted_memory_unvalidated` | mcp/tests/test_knowledge_validator_routes.py:99-127; mcp/tests/test_knowledge_validator_routes.py:130-154 |
| The managed sync refusal and repair, and the conforming parallel sync. | `test_the_managed_sync_refuses_a_merge_with_duplicate_ids_until_it_is_repaired`; `test_parallel_minted_ids_sync_cleanly` | mcp/tests/test_knowledge_validator_routes.py:157-189; mcp/tests/test_knowledge_validator_routes.py:192-208 |
| The standalone command: the pass line counts the one report-only legacy finding, and the JSON refusal's full violation list is pinned. | `test_the_standalone_command_validates_a_converted_fixture_tree` | mcp/tests/test_knowledge_validator_routes.py:216-244 |
| The retained-conflict continuation. | `test_a_resolved_memory_conflict_that_breaks_validation_is_refused_on_continue` | mcp/tests/test_knowledge_validator_routes.py:247-280 |

## Cross-Repo References

No meaningful cross-repo references found: the cases create their own temporary code and memory repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — the standalone-command case counts MIK-R27's report-only legacy finding and pins the JSON output's full list (ruling F3).** The Logic bullet and the command row were reworded; the retained-conflict row re-pointed by the exact line shift. No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
