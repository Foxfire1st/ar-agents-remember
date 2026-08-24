# mcp/src/agents_remember/worktrees/integration/closeout_door_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout_door_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-integration overview](overview.md)

## Purpose

Owns public status, declaration, provenance update, defer, resume, and withdrawal commands for the
canonical closeout door.

## Code Commentary

Each mutation takes the short task-publication lock, re-reads configured authority, authorizes the
caller, and publishes exact contract bytes. It then requests a best-effort refresh of every affected
disposable projection. A publication conflict exposes bounded expected/observed evidence; only a
proven accepted-before result is retryable.

## Invariants And Boundaries

- Door publication is canonical; projection refresh is a downstream effect.
- Projection failure never rolls back an accepted task or door mutation.
- The task-publication lock is bounded to compare-and-swap publication, never leaf execution.
- No queue state authorizes a task or door mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public door commands publish under the canonical task CAS. | `apply_closeout_door_request` | `mcp/src/agents_remember/worktrees/integration/closeout_door_control.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final public door-control boundary. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
