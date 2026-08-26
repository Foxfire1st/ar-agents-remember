# mcp/tests/test_sync_transaction_git_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_transaction_git_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
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
the admitted generation and translates abort/reset/restore failures. Ledger tests reject missing,
invalid, or duplicate per-code-commit mappings instead of weakening memory proof.

### Invariants And Boundaries

- Only quiet exact verification of a valid ref may produce absence.
- Every created/deleted ref and restored head is guarded by its admitted expected value.
- Retained conflicts and continuation stay bound to exact MERGE_HEAD and parent commits.
- Rollback refuses unrelated later history or an incompletely restored worktree.
- Divergent memory resolution preserves all parent rows and exactly one row per admitted code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact ref and temporary-worktree failure boundaries are forced directly. | `test_read_ref_rejects_invalid_and_unreadable_refs`; `test_create_pinned_ref_is_idempotent_and_rejects_changes`; `test_temporary_worktree_creation_and_checkout_identity_fail_loud` | mcp/tests/test_sync_transaction_git_edges.py:49-64; mcp/tests/test_sync_transaction_git_edges.py:67-80; mcp/tests/test_sync_transaction_git_edges.py:97-119 |
| Merge, continuation, and rollback accept only operation-attributable state. | `test_start_side_merge_rejects_dirty_or_unattributed_results`; `test_validate_staged_resolution_rejects_each_incomplete_proof`; `test_rollback_side_translates_abort_reset_and_post_restore_failures` | mcp/tests/test_sync_transaction_git_edges.py:207-239; mcp/tests/test_sync_transaction_git_edges.py:334-349; mcp/tests/test_sync_transaction_git_edges.py:371-426 |
| Ledger proof rejects missing and duplicate code mappings. | `test_ledger_validation_rejects_missing_and_duplicate_code_mappings`; `test_ledger_rows_translate_missing_and_invalid_ledgers` | mcp/tests/test_sync_transaction_git_edges.py:429-436; mcp/tests/test_sync_transaction_git_edges.py:439-454 |
| Production Git proof and mutation ownership is centralized in one focused module. | `read_ref`; `start_side_merge`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:24-36; mcp/src/agents_remember/worktrees/sync_transaction_git.py:136-174; mcp/src/agents_remember/worktrees/sync_transaction_git.py:252-280 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen resumable-sync Git edge
  suite. Verification metadata remains empty until closeout can stamp a real code commit.
