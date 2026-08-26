# mcp/tests/test_sync_transaction_recovery_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_transaction_recovery_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused finalization, cancellation, damaged-journal, partial-authority, and rollback-attribution
coverage for resumable synchronization.

## Code Commentary

### Logic

Completion cases prove idempotence only when contract bases already equal the journaled result and
reject pair mismatch. Cancellation checks even sides whose merge plan did not move, then restores
participating sides before releasing authority. Unreadable and missing journal cases require an
explicit applied cancel, preserve recoverable evidence, and remain retryable when archive or ref
inspection cannot be proven.

Ref recovery distinguishes absent, partial, and complete authority; code-only operation shapes do
not invent memory refs. Partial rollback failure leaves remaining proof in place and returns exact
manual-repair evidence. Final matrices accept only exact active fast-forward/two-parent merge
history and reject every unattributed completed branch state.

### Invariants And Boundaries

- Terminal success is replayable only against the exact journaled contract/result pair.
- Cancellation is an explicit operation and releases refs only after every side is proven restored.
- Damaged or absent journals never authorize guessed rollback from ambient Git history.
- Partial authority is preserved for manual repair when automatic proof cannot finish.
- A branch head is operation-owned only through exact admitted parentage and pinned refs.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Completion/cancellation enforce exact pair and all-side proof. | `test_finalize_is_idempotent_when_contract_bases_are_already_current`; `test_cancel_checks_each_unchanged_side_before_releasing_authority` | mcp/tests/test_sync_transaction_recovery_edges.py:126-145; mcp/tests/test_sync_transaction_recovery_edges.py:174-198 |
| Damaged/missing journal recovery requires explicit cancellation and preserves retry evidence. | `test_unreadable_journal_preservation_and_ref_inspection_failures_are_retryable`; `test_missing_journal_requires_cancel_and_routes_applied_cancel`; `test_partial_authority_preserves_remaining_refs_when_rollback_fails` | mcp/tests/test_sync_transaction_recovery_edges.py:216-252; mcp/tests/test_sync_transaction_recovery_edges.py:255-277; mcp/tests/test_sync_transaction_recovery_edges.py:348-369 |
| Rollback and completed-head matrices reject unattributed history. | `test_rollback_proof_accepts_only_exact_active_fast_forward_or_merge`; `test_completed_branch_proof_rejects_each_unattributed_state` | mcp/tests/test_sync_transaction_recovery_edges.py:385-434; mcp/tests/test_sync_transaction_recovery_edges.py:437-473 |
| The focused recovery owner performs terminal publication, rollback, quarantine, and authority cleanup. | `finalize_sync`; `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:54-89; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:156-181; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:184-254; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:257-274 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen sync recovery edge suite.
  Verification metadata remains empty until closeout can stamp a real code commit.
