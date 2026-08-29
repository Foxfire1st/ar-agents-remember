# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Application overview](../overview.md)

## What This Area Is

Public application adapters for starting, observing, controlling, and executing durable lifecycle
operations. These modules translate configuration and caller context into typed worktree-domain
requests; they do not own journal transition policy.

## Hot Path Summary

Start with `direct_landing.py` for the public direct route and
`lifecycle_operation_worker.py` for the detached worker boundary.

## Operating Model

Application tools admit configured contracts, resolve durable operation locations, invoke the
worktree lifecycle owners, and project typed refusals. The worker binds default services, owns one
lease, advances the durable record, and publishes a terminal result without inventing recovery.

## Local Invariants And Traps

- Application adapters translate lower-level failure families once; public callers must not
  reproduce the complete exception vocabulary.
- Durable journal and enclosure state outrank task projections or stale in-memory observations.
- A direct operation is a distinct route, not an implicit fallback from queued closeout.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `direct_landing.py` | [direct_landing.py.md](direct_landing.py.md) | covered |
| `lifecycle_operation_worker.py` | [lifecycle_operation_worker.py.md](lifecycle_operation_worker.py.md) | covered |

## Docs And Boundary References

No Domain Documentation or cross-repository source is configured for this route. Same-repository
authority is documented by the linked source sidecars and the worktrees integration overview.

## Update History

- 2026-08-25T15:44+02:00 — Created for PDLS whole-system reconciliation and the public
  lifecycle-error translation boundary. Verification remains closeout-owned.
