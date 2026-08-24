# mcp/src/agents_remember/worktrees/queue/closeout_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-queue overview](overview.md)

## Purpose

Builds an exact current-source census for the disposable sprint closeout projection.

## Code Commentary

A rebuild reads current task topology, canonical waiting closeout doors, and active series contracts
at their exact addresses. Prior projection rows are never input. Unreadable, malformed, or
bounded-overflow sources become explicit bounded problems; only a waiting door whose candidate,
master, sprint, and contract identities agree becomes a member.

## Invariants And Boundaries

- The projection cannot create, claim, certify, or complete lifecycle authority.
- Each build is derived from current canonical sources and carries their fingerprint.
- Source failure is explicit and yields invalid-empty service, never stale-row reuse.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source capture and member census are rebuilt from scratch. | `capture_projection_source` | `mcp/src/agents_remember/worktrees/queue/closeout_projection.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final projection census. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
