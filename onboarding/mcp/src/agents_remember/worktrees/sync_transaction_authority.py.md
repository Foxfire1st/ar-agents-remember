# mcp/src/agents_remember/worktrees/sync_transaction_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file owns admission and identity authority for resumable source synchronization: exact side
locations/plans, official code-memory pair validation, pinned refs, journal-to-contract identity,
finalization/cancellation preconditions, and common response evidence.

## Code Commentary

### Logic

`side_record` binds one code or memory side to repository, operation worktree, source/work branch,
admitted source commit, pre-sync head, recorded base, three deterministic backup refs, and a plan.
Series sync uses temporary enclosure `.sync` worktrees; leaves use their ordinary worktrees.
`preflight_official_pair` reads `memory.md` at the admitted official memory tip and requires a
newest current mapping for the admitted code tip before mutation. Older same-code rows remain valid
history.

`pin_authority`, `require_pinned_authority`, and `delete_authority` manage exact base/pre-sync/source
refs. Recovery reconstructs a side only when all three exist. Contract validation binds journal
path, task id, kind, repositories, worktrees, and branches; finalization additionally constrains
base transitions, while cancellation requires original bases. Shared helpers update the journal and
shape side/result payloads without changing authority.

### Conventions

Git authority uses full commit ids and compare-exact refs. Source pair means local protected branch
tips; upstream fetch evidence lives elsewhere. Missing one member of a recovery-ref triple is an
error, not partial success.

### Invariants And Boundaries

- External-memory admission requires the newest valid ledger mapping for the exact code tip; global
  code-key uniqueness is not an admission rule.
- Journal identity cannot be rebound to another contract, repository, branch, or worktree.
- All participating refs are pinned before the journaled mutation proceeds.
- Cleanup deletes refs only when they still equal the admitted commits.
- This module does not infer authority from queue state or ambient checkout position.

### Todos

Authority and result-state claims are reconciled to the frozen source; verification metadata awaits
the real code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The journal models store every side identity and deterministic ref used here. | `SyncSideRecord`; `SyncOperationRecord`; `sync_side_refs` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:37-57; mcp/src/agents_remember/worktrees/sync_transaction_state.py:60-77; mcp/src/agents_remember/worktrees/sync_transaction_state.py:132-134 |
| Exact ref, checkout, merge, and rollback proof is centralized in the Git module. | `create_pinned_ref`; `require_side_checkout`; `start_side_merge`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:38-47; mcp/src/agents_remember/worktrees/sync_transaction_git.py:79-85; mcp/src/agents_remember/worktrees/sync_transaction_git.py:135-173; mcp/src/agents_remember/worktrees/sync_transaction_git.py:251-279 |
| The driver admits and advances only after this authority preflight succeeds. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T14:32+02:00 — Corrected official source-pair admission to use newest-first current
  mapping authority while accepting retained same-code memory history. Verification remains
  closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of source-pair, ledger, contract, and
  pinned-ref admission authority.

- 2026-08-26T02:55+02:00 — Drafted strict sync-authority onboarding; final source freeze and
  verification remain open.