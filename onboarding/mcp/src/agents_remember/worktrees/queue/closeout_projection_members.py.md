# mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-queue overview](overview.md)

## Purpose

Computes candidate-local readiness, reasons, and deterministic ordering for closeout-projection
members.

## Code Commentary

The builder rechecks completion, provenance freshness, admission, scheduling and predecessor
blockers, and the candidate topology fingerprint against the exact waiting door and current task
facts. Reasons are bounded; member identity and ordering are deterministic.

## Invariants And Boundaries

- Readiness is a disposable view, not durable certification.
- Only waiting door generations may become members.
- Projection reasons do not mutate tasks, doors, operations, or integration state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Member readiness is recomputed from door and task truth. | `build_projection_members` | `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final member builder. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
