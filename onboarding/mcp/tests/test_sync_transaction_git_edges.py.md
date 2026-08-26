# mcp/tests/test_sync_transaction_git_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_transaction_git_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused proof-boundary coverage for the exact Git refs, worktrees, merges, rollback, and
external-memory ledger validation used by resumable synchronization.

## Code Commentary

### Logic

The first group distinguishes an invalid ref name, a genuinely absent exact ref, and an unreadable
ref; pinned ref creation/deletion is idempotent only for the expected commit. Temporary worktrees
must retain journaled repository/branch identity, remain clean before removal, and translate Git
command failures into `SyncGitProofError`.

Merge cases cover retained replay, already-completed replay, dirty/unattributed results, pinned
memory MERGE_HEAD, validation and commit failure, continuation after a disappeared merge state,
and every incomplete staged-resolution proof. Rollback accepts only history mechanically owned by
the admitted generation and translates abort/reset/restore failures. Ledger tests require every
exact parent row and accept repeated code commits while still translating missing or invalid ledgers.

### Invariants And Boundaries

- Only quiet exact verification of a valid ref may produce absence.
- Every created/deleted ref and restored head is guarded by its admitted expected value.
- Retained conflicts and continuation stay bound to exact MERGE_HEAD and parent commits.
- Rollback refuses unrelated later history or an incompletely restored worktree.
- Divergent memory resolution preserves every exact parent row, including valid repeated-code
  memory history.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact ref and temporary-worktree failure boundaries are forced directly. | `test_read_ref_rejects_invalid_and_unreadable_refs`; `test_create_pinned_ref_is_idempotent_and_rejects_changes`; `test_temporary_worktree_creation_and_checkout_identity_fail_loud` | mcp/tests/test_sync_transaction_git_edges.py:49-64; mcp/tests/test_sync_transaction_git_edges.py:67-80; mcp/tests/test_sync_transaction_git_edges.py:97-119 |
| Merge, continuation, and rollback accept only operation-attributable state. | `test_start_side_merge_rejects_dirty_or_unattributed_results`; `test_validate_staged_resolution_rejects_each_incomplete_proof`; `test_rollback_side_translates_abort_reset_and_post_restore_failures` | mcp/tests/test_sync_transaction_git_edges.py:207-239; mcp/tests/test_sync_transaction_git_edges.py:334-349; mcp/tests/test_sync_transaction_git_edges.py:371-426 |
| Ledger proof preserves repeated-code history and rejects missing exact parent rows or invalid ledgers. | `test_ledger_validation_preserves_same_code_history_and_rejects_missing_rows`; `test_ledger_rows_translate_missing_and_invalid_ledgers` | mcp/tests/test_sync_transaction_git_edges.py:429-436; mcp/tests/test_sync_transaction_git_edges.py:438-453 |
| Production Git proof and mutation ownership is centralized in one focused module. | `read_ref`; `start_side_merge`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:23-35; mcp/src/agents_remember/worktrees/sync_transaction_git.py:135-173; mcp/src/agents_remember/worktrees/sync_transaction_git.py:251-279 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T14:32+02:00 — Replaced duplicate-key refusal forcing with exact parent-row
  preservation across valid same-code history. Verification remains closeout-owned.

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen resumable-sync Git edge
  suite. Verification metadata remains empty until closeout can stamp a real code commit.
