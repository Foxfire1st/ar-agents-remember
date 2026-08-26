# mcp/src/agents_remember/worktrees/sync_transaction_git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_git.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file owns every exact Git mutation and proof for resumable sync. It makes retained conflicts,
agent continuation, exact result attribution, rollback, temporary worktree cleanup, and
external-memory ledger preservation mechanical rather than caller-specific.

## Code Commentary

### Logic

`read_ref` first validates the complete ref name with `git check-ref-format`, then resolves exactly
`<ref>^{commit}` through `git rev-parse --verify --quiet --end-of-options`. Only the latter
command's missing-ref return code becomes `None`; an invalid name or any other inspection failure
raises `SyncGitProofError` with Git's detail. Pinned refs are then created and deleted by
expected-value checks, so malformed authority cannot masquerade as absent authority. Temporary
worktrees are created only for the journaled repository/branch and are removed only when clean.
Checkout proof compares repository identity and branch, while helpers inspect status, MERGE_HEAD,
and unmerged paths.

`start_side_merge` attempts the pinned source merge and leaves a genuine conflict in place. A
divergent memory merge is staged without auto-commit until both parent ledgers are validated.
`validate_staged_resolution` proves the exact MERGE_HEAD, zero unmerged/unstaged paths, index
sanity, and memory-ledger preservation before `continue_side_merge` commits. Completion accepts
only the admitted fast-forward or a two-parent commit with exact pre-sync/source parents.
`rollback_side` restores only an active or completed operation-owned delta and refuses later work.

### Conventions

All Git commands use the shared bounded runner. `SyncGitProofError` means live Git cannot be
attributed exactly to this journal generation; callers return manual-repair/cancel guidance rather
than weakening the proof.

### Invariants And Boundaries

- A conflict is retained only when MERGE_HEAD equals the pinned source and unmerged paths exist.
- Missing exact refs are distinct from invalid ref names and Git inspection failures.
- Continue commits only a fully staged exact retained merge.
- Memory resolution must contain every exact parent ledger row. Repeated code rows are valid
  newest-first history and are not collapsed during merge validation.
- Automatic rollback refuses unrelated/later commits or dirty post-sync work.
- Temporary worktree removal and ref deletion are evidence-checked, never best-effort deletion.

### Todos

Reconcile line ranges after Dagger fixes; verification remains empty for the uncommitted source.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Side records carry the exact repository, worktree, commits, refs, plan, and conflict set proven here. | `SyncSideRecord` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:37-57 |
| The driver records retained conflicts and delegates continue through these proof functions. | `_continue_resolution`; `continue_side_merge`; `validate_staged_resolution` | mcp/src/agents_remember/worktrees/sync_transaction.py:424-450; mcp/src/agents_remember/worktrees/sync_transaction_git.py:201-225; mcp/src/agents_remember/worktrees/sync_transaction_git.py:228-249 |
| Recovery uses exact-created-head and rollback proof before restoring or finalizing. | `_recover_from_refs`; `exact_created_head`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:306-364; mcp/src/agents_remember/worktrees/sync_transaction_git.py:282-290; mcp/src/agents_remember/worktrees/sync_transaction_git.py:251-279 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T14:32+02:00 — Removed the unrequested per-code uniqueness rule from staged
  memory-merge validation. Exact parent-row preservation remains mandatory and same-code history is
  retained. Verification remains closeout-owned.

- 2026-08-26T06:20+02:00 — Reconciled exact authority-ref lookup: validate the ref name first,
  return absence only for quiet exact verification's missing-ref result, and preserve every other
  Git failure as `SyncGitProofError`. No test-execution claim is made.

- 2026-08-26T02:55+02:00 — Drafted exact Git-proof onboarding for the resumable sync partition;
  final citations and verification remain open.