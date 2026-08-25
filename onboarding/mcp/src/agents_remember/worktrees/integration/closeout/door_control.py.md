# mcp/src/agents_remember/worktrees/integration/closeout/door_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

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
| Public door commands publish under the canonical task CAS. | `closeout_door_tool`; `task_publication_lock`; `publish_door_intent` | mcp/src/agents_remember/worktrees/integration/closeout/door_control.py:38-84 |

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final public door-control boundary. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
