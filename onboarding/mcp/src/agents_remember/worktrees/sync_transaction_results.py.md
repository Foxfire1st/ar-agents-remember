# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T15:06+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file centralizes typed public result construction for resumable sync so phase routing does not
duplicate or drift recovery guidance, agent ownership, preview semantics, or terminal replay.

## Code Commentary

### Logic

Result builders cover required memory policy choice, mutation-free sync preview, retained conflict
with reported side/worktree/files and continue/cancel calls, staged-resolution preview, parked-
candidate validation preview, active and cancel previews, completed/cancelled generation replay, and
no-authority quarantine replay. The
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

## Parked-Candidate Result Surface

`resolution_required` now emits `resolution.wipRestore = true` and a parked-specific summary when
the retained conflict is a parked-candidate reapply (`side.wipState == "restore-conflict"`), while an
ordinary retained merge keeps its exact previous payload shape. `parked_wip_validation_preview` is
the read-only counterpart the driver reaches for `dry_run` + `resolution_action=continue`: it
reports `would-settle-parked-wip` when no unmerged path remains, or `sync-resolution-incomplete`
with the remaining files, and mutates nothing.

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
| The sync driver selects these result builders from exact journal phases. | `_route_sync_record`; `_resume_active` | mcp/src/agents_remember/worktrees/sync_transaction.py:155-175; mcp/src/agents_remember/worktrees/sync_transaction.py:418-438 |
| Read-only staged-resolution proof and unmerged-path enumeration are Git-owned. | `validate_staged_resolution`; `unmerged_paths` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:235-239; mcp/src/agents_remember/worktrees/sync_transaction_git.py:345-366 |
| Completed result reconstruction and manual repair remain recovery-owned. | `completed_sync_result`; `manual_repair_result` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:96-157; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:300-313 |
| The retained-conflict builder marks a parked-candidate reapply, and a read-only preview gates settling it. | `resolution_required`; `parked_wip_validation_preview`; `resolution_validation_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-113; mcp/src/agents_remember/worktrees/sync_transaction_results.py:116-143; mcp/src/agents_remember/worktrees/sync_transaction_results.py:146-170 |
| The remaining public result builders keep the phase vocabulary stable. | `memory_choice_required`; `sync_preview`; `active_preview`; `cancel_preview`; `terminal_resolution_replay`; `quarantine_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:28-50; mcp/src/agents_remember/worktrees/sync_transaction_results.py:53-68; mcp/src/agents_remember/worktrees/sync_transaction_results.py:173-187; mcp/src/agents_remember/worktrees/sync_transaction_results.py:190-207; mcp/src/agents_remember/worktrees/sync_transaction_results.py:210-245; mcp/src/agents_remember/worktrees/sync_transaction_results.py:248-261 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-10T15:06+02:00 — Parked-candidate result surface: recorded the `wipRestore` marker and parked-specific summary on `resolution_required`, and the read-only `parked_wip_validation_preview`. Re-derived the builder anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of preview, retained-resolution,
  cancellation, quarantine, and terminal replay result vocabulary.

- 2026-08-26T02:55+02:00 — Drafted sync-result ownership; final vocabulary, citations, and
  verification remain open.