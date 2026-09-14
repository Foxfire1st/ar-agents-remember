# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
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
| The sync driver selects these result builders from exact journal phases. | `_route_sync_record`; `_resume_active` | mcp/src/agents_remember/worktrees/sync_transaction.py:154-174; mcp/src/agents_remember/worktrees/sync_transaction.py:419-439 |
| Read-only staged-resolution proof and unmerged-path enumeration are Git-owned. | `validate_staged_resolution`; `unmerged_paths` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:235-239; mcp/src/agents_remember/worktrees/sync_transaction_git.py:249-253; mcp/src/agents_remember/worktrees/sync_transaction_git.py:353-372 |
| Completed result reconstruction and manual repair remain recovery-owned. | `completed_sync_result`; `manual_repair_result` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:95-156; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:299-312 |
| The retained-conflict builder marks a parked-candidate reapply, and a read-only preview gates settling it. | `resolution_required`; `parked_wip_validation_preview`; `resolution_validation_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-113; mcp/src/agents_remember/worktrees/sync_transaction_results.py:116-143; mcp/src/agents_remember/worktrees/sync_transaction_results.py:146-170 |
| The remaining public result builders keep the phase vocabulary stable. | `memory_choice_required`; `sync_preview`; `active_preview`; `cancel_preview`; `terminal_resolution_replay`; `quarantine_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:28-50; mcp/src/agents_remember/worktrees/sync_transaction_results.py:53-68; mcp/src/agents_remember/worktrees/sync_transaction_results.py:173-187; mcp/src/agents_remember/worktrees/sync_transaction_results.py:190-207; mcp/src/agents_remember/worktrees/sync_transaction_results.py:210-245; mcp/src/agents_remember/worktrees/sync_transaction_results.py:248-261 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the parked-candidate
  result surface is the frozen change and the card documents it. Re-checked all nine cited ranges:
  they hold. No wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/sync_transaction_results.py` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — Parked-candidate result surface: recorded the `wipRestore` marker and parked-specific summary on `resolution_required`, and the read-only `parked_wip_validation_preview`. Re-derived the builder anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of preview, retained-resolution,
  cancellation, quarantine, and terminal replay result vocabulary.

- 2026-08-26T02:55+02:00 — Drafted sync-result ownership; final vocabulary, citations, and
  verification remain open.