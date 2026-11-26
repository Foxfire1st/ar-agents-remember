# mcp/tests/test_terminal_enclosure_archive_sync_journal.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Source-declared regression tests verifying that the sync transaction journal lives in `reports/` as working state rather than terminal `.lifecycle/` evidence, that a pre-move `.lifecycle/sync-operation.json` is recorded as removed working state without being archived, and that active sync journals and unrecognised `.lifecycle/` files still refuse cleanup.

## Code Commentary

Helper functions construct an external-memory closed leaf (`_closed_leaf`), build a schema-valid `SyncOperationRecord` in a chosen `SyncPhase` (`_sync_journal`), seed a pre-move copy strictly at `legacy_sync_operation_path` under `.lifecycle/` (`_write_legacy_sync_journal`), and invoke `terminal_archive_required_result` for `worktree_cleanup` (`_cleanup`).

The four tests cover distinct boundaries over temporary `tmp_path` fixtures:

1. `test_sync_write_relocates_the_journal_out_of_the_lifecycle_root` seeds a legacy `.lifecycle/sync-operation.json`, writes a `completed` record through `SyncOperationStore.write`, and asserts the store publishes under `reports/`, reads back the exact record, and deletes the legacy `.lifecycle/` copy.
2. `test_pre_move_sync_journal_is_removed_with_the_enclosure_never_archived` places a `completed` legacy journal in `.lifecycle/` on a closed leaf, verifies `sync_operation_path` points to `reports/` rather than `.lifecycle/`, runs live cleanup archival (`dry_run=False`), and asserts `returncode == 0`, `state == "terminal-archive-proven"`, exclusion of `sync-operation.json` from `canonicalEntries`, and exact SHA-256/size/`"removed-with-enclosure"` accounting in `removedWorkingState` both in the command payload and in the persisted `TerminalEnclosureArchive` file at `archivePath`.
3. `test_unrecognised_canonical_lifecycle_artifact_still_refuses_cleanup` writes `.lifecycle/mystery.json`, runs dry-run cleanup archival, and asserts `returncode == 2`, `state == "terminal-archive-unowned-artifact"`, `observed` naming `mystery.json` and `lifecycleDirectory`, detail containing `"No automated remedy exists"`, `nextAction == "developer-decision"`, `developerDecisionRequired is True`, and that `mystery.json` stays on disk.
4. `test_live_sync_transaction_refuses_cleanup_with_a_named_remedy` writes a legacy journal at `phase="code-resolution-required"`, runs dry-run cleanup archival, and asserts `returncode == 2`, `state == "terminal-archive-sync-transaction-active"`, detail naming the journal and `"resolution-required"`, `nextAction == "worktree_sync"`, `nextTool == "worktree_sync"`, `nextArgs` specifying the resolved `contract_path` with `resolution_action="cancel"` and `dry_run=False`, and that the journal remains on disk.

These are source-declared fixture assertions; their presence does not by itself establish a fresh test run or acceptance verdict.

## Relationships

- Protects `SyncOperationStore`, `sync_operation_path`, and `legacy_sync_operation_path` in `mcp/src/agents_remember/worktrees/sync_transaction_state.py`, `terminal_archive_required_result` in `mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py`, the pre-move working-state and unowned-artifact classifiers in `mcp/src/agents_remember/worktrees/integration/terminal_enclosure_evidence.py`, and `TerminalEnclosureArchive` in `mcp/src/agents_remember/models/lifecycles/enclosure.py`.
- Uses `_authority_fixture` and `_closed_external_leaf_worktrees` from `mcp/tests/integration_branch_authority_test_support.py`, and is registered in `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, and `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py`.

## Evidence

- `SyncOperationStore.write` publishes the sync journal under `reports/`, reads back the same record, and removes any pre-move `.lifecycle/sync-operation.json` copy. [1]
- A completed pre-move `.lifecycle/sync-operation.json` is excluded from `canonicalEntries` and recorded in `removedWorkingState` with `sha256`, `sizeBytes`, and `removed-with-enclosure` in both the result payload and persisted `TerminalEnclosureArchive`. [2]
- An unrecognised file in `.lifecycle/` refuses cleanup with `terminal-archive-unowned-artifact`, `developer-decision`, and no deletion. [3]
- A non-terminal legacy sync journal (`code-resolution-required`) refuses cleanup with `terminal-archive-sync-transaction-active`, a `worktree_sync` cancel remedy, and no deletion. [4]
