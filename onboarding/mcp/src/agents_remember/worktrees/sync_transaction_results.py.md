# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file centralizes typed public result construction for resumable sync so phase routing does not
duplicate or drift recovery guidance, agent ownership, preview semantics, or terminal replay.

## Code Commentary

### Logic

Result builders cover required memory policy choice, mutation-free sync preview, retained conflict
with reported side/worktree/files and continue/cancel calls, staged-resolution preview, active and
cancel previews, completed/cancelled generation replay, and no-authority quarantine replay. The
retained-conflict payload explicitly names the agent as resolution owner. Terminal replay refuses
late cancel after completion but permits exact continue to reconstruct the completed result.

### Conventions

Every builder returns `WorktreeCommandResult`; public calls are contract-addressed and never expose
the private journal/ref prefix. Shared `side_payload`, `recovery_guidance`, and recovery result
owners keep response shapes consistent.

### Invariants And Boundaries

- Preview never claims mutation or completion.
- Conflict guidance includes both exact continue and cancel calls.
- A completed generation cannot be retroactively cancelled.
- Quarantine replay never claims branch restoration without refs.
- This module shapes evidence; it does not read/write journals or run Git mutations.

### Todos

Exact response vocabulary is reconciled to the frozen source; verification remains empty until the
real code commit exists.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sync driver selects these result builders from exact journal phases. | `_route_sync_record`; `_resume_active` | mcp/src/agents_remember/worktrees/sync_transaction.py:144-164; mcp/src/agents_remember/worktrees/sync_transaction.py:307-327 |
| Read-only staged-resolution proof and unmerged-path enumeration are Git-owned. | `validate_staged_resolution`; `unmerged_paths` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:228-249; mcp/src/agents_remember/worktrees/sync_transaction_git.py:118-122 |
| Completed result reconstruction and manual repair remain recovery-owned. | `completed_sync_result`; `manual_repair_result` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:92-153; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:290-303 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of preview, retained-resolution,
  cancellation, quarantine, and terminal replay result vocabulary.

- 2026-08-26T02:55+02:00 — Drafted sync-result ownership; final vocabulary, citations, and
  verification remain open.