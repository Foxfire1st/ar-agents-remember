# mcp/tests/test_knowledge_validator_routes.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R22 rule 8: where the validator runs, with a refusal test at each point wired in this leaf.** The cases cover the Git tree readers, the commit-route adapter, the worktree gate, the managed sync after a merge (automatic and retained-conflict paths), and the curator's `knowledge-validate` command. Registered in the `unit-regression` lane. Earlier collected-case and integration-ceiling figures are historical, not current collection or policy evidence; no fresh collection is claimed.

## Code Commentary

### Logic

`test_a_merge_moved_row_refuses_at_leaf_publication` takes the same real moved-row merge into the leaf-publication validator and requires `R09-history-rows`, never the report-only merged spelling. Ordinary managed-sync merge treatment remains separate.

- `test_git_trees_are_read_exactly_and_the_route_index_cache_is_ignored`: exact bytes through `read_git_blobs_bytes`, the cache and hidden directories skipped, a dot-named card read, and the directory and Git readers equal.
- `test_the_commit_route_adapter_refuses_naming_every_violation`: `GitKnowledgeValidation` over real commits: unconverted memory passes, a converted commit over an unconverted base is refused, an unreadable base is refused ("cannot read"), and a hand-added `[4]` is refused with its rendered line.
- `test_the_worktree_route_never_commits_converted_memory_unvalidated`: `memory_commit_refusal` refuses with no bound validator, with no paired code commit, and for an unreadable (`"0"*40`) tree, and passes unconverted memory.
- `test_the_managed_sync_refuses_a_merge_with_duplicate_ids_until_it_is_repaired`: a real `SyncFixture` sync is refused with `sync-knowledge-validation-refused` and the recovery line; `HEAD` is unchanged and `MERGE_HEAD` is the source; after `git rm` and a rerun, the sync completes with exact parents.
- `test_parallel_minted_ids_sync_cleanly`: the conforming example through the real sync.
- `test_the_standalone_command_validates_a_converted_fixture_tree` has two distinct scopes: the
  initial `--base` invocation asserts exit 0 with one carried legacy report; the malformed `[4]`
  JSON invocation omits `--base`, making legacy debt new, and asserts exit 1 with
  `[("R22.3-markers", False), (LEGACY_COUNT, False)]`. Unconverted memory is out of scope
  (exit 0), and unreadable `--base` exits 2. These are current source assertions, not a CLI run.
- `test_a_sync_merge_refuses_a_history_row_only_when_the_leaf_s_own_side_had_it_wrong` (MIK-R09, leaf 260928-MIK-L09; the sync part of ruling 2026-09-30T16:07:55), parametrised: after a real managed sync, the leaf's side (`knowledge/history/260928-MIK-L97.json`, `LEAF_HISTORY`) holds an open row covering the integrate route's entry, and the official line re-anchors that entry (`_moved`). "consistent" (the row agreed with the leaf's own side): the sync completes and the merged sidecar carries the incoming anchor, reported by `R09-history-rows-merged`. "already wrong" (the row's `after` disagreed on the leaf's side too): the sync is refused with `R09-history-rows`, not the merged rule. The cases live here, beside the module's `SyncFixture` cases, because importing either into the new route module would have added governed consumer rows to `evidence-lifecycle.toml` (review R1 F5 note).
- `test_a_resolved_memory_conflict_that_breaks_validation_is_refused_on_continue`: a real conflict resolved into duplicate IDs is refused on `continue` with the right state, then syncs after the repair.

### Conventions

- It imports `SyncFixture` from `test_worktree_sync.py` rather than duplicating it, and binds or restores worktree services around the gate tests.

### Invariants And Boundaries

- Each rule-8 integration point this leaf wires has a refusal test that drives real Git state, not a stub.

### Todos

Resolved: MIK-R09's routes have their own refusal tests, each entered through the route's public entry point (`test_knowledge_gate_routes.py`, `test_knowledge_closeout_gate.py`); the sync-merge cases are here.

Incoming converted-memory fast-forwards now have their own refusal-before-ref-movement cases. Structured refusal preserves per-path/rule violations and the full total while bounding the displayed list; repair clears the stored refusal. Text-only fallback remains a distinct case, not proof of structured validator output.

Four further source cases pin literal-markup recovery (`fenced code block`/`code span`), Git-visible working-tree existence (untracked included, ignored excluded), text/JSON no-base notes that authored records are new, and optional endpoint observations. The endpoint fixture resolves an archived record packet while a sidecar version mismatch remains unresolved; both observations are printed without becoming validator refusals. These are fixture/CLI assertions, not a live endpoint publication or execution receipt.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The route cases.

- The Git readers. [1]
- The adapter and the worktree gate. [2]
- The managed sync refusal and repair, and the conforming parallel sync. [3]
- A sync merge refuses a history row only when the leaf's own side had it wrong (MIK-R09). [5]
- The retained-conflict continuation. [6]

### Cross-Repo References

No meaningful cross-repo references found: the cases create their own temporary code and memory repositories.

No cross-repo boundary is crossed by this file.

- Standalone source assertions: based fixture pass with carried legacy report, baseless malformed-marker JSON refusal with both reportOnly flags False, out-of-scope and unreadable-input exits. [4]
- Current source delta inspected statically: Distinguish the based pass from baseless JSON refusal and repair the stale legacy reportOnly=True caption; retain sync/publication and reader-boundary accounts. [7]


- Incoming converted-memory fast-forwards now have their own refusal-before-ref-movement cases. Structured refusal preserves per-path/rule violations and the full total while bounding the displayed list; repair clears the stored refusal. Text-only fallback remains a distinct case, not proof of structured validator output. [8]


- The four added CLI/source cases pin literal recovery, Git-visible paths, baseless notes and nongating archived/unresolved endpoint observations. [9]
