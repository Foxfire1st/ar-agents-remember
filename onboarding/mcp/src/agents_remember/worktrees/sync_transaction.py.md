# mcp/src/agents_remember/worktrees/sync_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file is the state-machine driver for resumable, contract-addressed mid-task source
synchronization. It replaces abort-and-block merge handling with one durable generation that an
agent can observe, continue after resolving a retained conflict, cancel, or recover.

## Code Commentary

### Logic

`sync_contract_under_authority` validates typed inputs, reads the stable enclosure-root store, and
routes missing/malformed journal recovery, quarantine replay, identity checks, active resume,
terminal replay, or new admission. No integration lock survives the return, so conflict resolution
happens between calls in the reported worktree.

Admission reads the exact official pair, validates its external-memory ledger mapping, plans each
side as already-current/fast-forward/merge/skip, checks non-temporary worktrees before any refs are
pinned, writes the journal, creates temporary `.sync` worktrees for series sides, and starts code
then memory. A genuine merge conflict records the side and conflict files without aborting. Continue
validates the exact staged merge and advances the same generation; cancel delegates exact rollback.
Automatic replay reconciles a side whose operation-owned commit already exists and finalizes only
after both participating sides are proven.

### Conventions

The driver delegates durable models/store, Git proof, authority, results, and recovery to focused
modules; it owns only phase routing. Input refusals happen before selector, refs, journal, or Git
mutation. State is returned as `WorktreeCommandResult`. The top-level safety boundary translates
unexpected I/O, proof, and value failures into `sync-operation-refused`, names the caught failure
family in the summary, and preserves `str(error)` in the structured `detail` field so a useful Git
or journal refusal is not collapsed into a generic status.

### Invariants And Boundaries

- One active generation is addressed by canonical contract, never a public operation id.
- Pinned source/base/pre-sync refs plus the stable journal are recovery authority.
- Retained conflicts are agent-owned action, not terminal failure.
- Continue/cancel cannot change the admitted memory-sync choice.
- Normal sync fails closed for malformed, missing-after-admission, or identity-invalid journal state.
- Queue rows and task prose never reconstruct operation lifecycle evidence.

### Todos

State-machine claims and citations are reconciled to the frozen source; commit-derived verification
remains closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict journal records and read-only status projection live at the enclosure root. | `SyncSideRecord`; `SyncOperationRecord`; `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:37-57; mcp/src/agents_remember/worktrees/sync_transaction_state.py:60-77; mcp/src/agents_remember/worktrees/sync_transaction_state.py:145-295; mcp/src/agents_remember/worktrees/sync_transaction_state.py:298-314 |
| Admission and pinned identity validate contract/source/ledger authority. | `preflight_official_pair`; `pin_authority`; `require_pinned_authority` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:121-161; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:164-169; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:172-186 |
| Git operations retain conflicts and prove exact staged, completed, or rolled-back heads. | `start_side_merge`; `continue_side_merge`; `validate_staged_resolution`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:136-174; mcp/src/agents_remember/worktrees/sync_transaction_git.py:201-225; mcp/src/agents_remember/worktrees/sync_transaction_git.py:228-249; mcp/src/agents_remember/worktrees/sync_transaction_git.py:252-280 |
| Finalization, cancellation, quarantine, and damaged-journal escape are separate recovery ownership. | `finalize_sync`; `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:54-89; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:156-181; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:184-254; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:257-274 |
| Public result constructors keep recovery guidance consistent across phases. | `memory_choice_required`; `resolution_required`; `active_preview`; `cancel_preview`; `terminal_resolution_replay`; `quarantine_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:28-50; mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-104; mcp/src/agents_remember/worktrees/sync_transaction_results.py:134-148; mcp/src/agents_remember/worktrees/sync_transaction_results.py:151-168; mcp/src/agents_remember/worktrees/sync_transaction_results.py:171-206; mcp/src/agents_remember/worktrees/sync_transaction_results.py:209-222 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the resumable state machine and its
  detail-preserving controlled refusal boundary.

- 2026-08-26T06:20+02:00 — Recorded that the public refusal boundary preserves the lower-level
  proof failure's exact detail while keeping the result controlled. No test-execution claim is
  made.

- 2026-08-26T02:55+02:00 — Drafted resumable-sync driver onboarding against the pre-Dagger
  partition; final state vocabulary, citations, and verification remain open.