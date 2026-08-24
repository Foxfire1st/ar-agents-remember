# mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-queue overview](overview.md)

## Purpose

Owns closeout-projection invalidation, rebuild, preview, and bounded publication effects.

## Code Commentary

Canonical task or door mutations invalidate affected projections to durable invalid-empty first.
Rebuild then computes a complete off-side candidate, rechecks that its source identity is still
current under the short publication mutex, and publishes valid-built only on an exact match.
Failures return bounded projection effects and leave canonical mutation truth untouched.

## Invariants And Boundaries

- The transaction is canonical mutation, invalidation, off-side rebuild, exact-current publish.
- A refresh failure cannot roll back task, door, journal, commit, or integration truth.
- Stale members are never retained as a fallback.
- Preview performs no publication.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Invalidation and exact-current publication are the only projection mutations. | `refresh_closeout_projections` | `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final publication-effect owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
