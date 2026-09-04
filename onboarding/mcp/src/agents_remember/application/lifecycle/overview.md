# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-04T17:15:00+02:00 |
| lastVerifiedCommitHash | `ce7f10b565f82bc41421d60ba914ee1d0abf61c4` |
| lastVerifiedCommitDate | 2026-09-04T17:04:29+02:00 |
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
Since CCR-R20 the detached worker's `OperationRuntime.fail` applies the typed terminal
rail-failure envelope (`terminal_rail_failure.py`) whenever a durable record exists, so
failed-rail facts reach the journal instead of a generic exception. Configured-contract admission
remains strict by default. Exact code-memory pair consumers may
delegate only candidate-worktree identity to the canonical pair validator; repository, task, and
enclosure authority remain at the application boundary.

## Local Invariants And Traps

- Application adapters translate lower-level failure families once; public callers must not
  reproduce the complete exception vocabulary.
- A delegated candidate check must have one explicit downstream owner; it must not become an
  unchecked permissive mode.
- Durable journal and enclosure state outrank task projections or stale in-memory observations.
- A direct operation is a distinct route, not an implicit fallback from queued closeout.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `direct_landing.py` | [direct_landing.py.md](direct_landing.py.md) | covered |
| `lifecycle_operation_worker.py` | [lifecycle_operation_worker.py.md](lifecycle_operation_worker.py.md) | covered |
| `terminal_rail_failure.py` | [terminal_rail_failure.py.md](terminal_rail_failure.py.md) | covered |

## Docs And Boundary References

No Domain Documentation or cross-repository source is configured for this route. Same-repository
authority is documented by the linked source sidecars and the worktrees integration overview.

## Update History

- 2026-09-04T17:15+02:00 — 260831-CCR-L20 Gate-5 memory pass (code commit `ce7f10b5`):
  recorded CCR-R20 typed terminal rail-failure propagation on the detached worker boundary:
  `OperationRuntime.fail` routes unclassified outer failures through
  `terminal_rail_failure.py`, and the route's File-Level Onboarding Map gained the new module.
  Verification stamp is the full leaf code commit
  `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.

- 2026-08-30T06:26+02:00 — MCAR-L03 A005: documented the strict-by-default admission boundary
  and its narrow single-owner transfer of candidate identity to exact-pair validation.

- 2026-08-25T15:44+02:00 — Created for PDLS whole-system reconciliation and the public
  lifecycle-error translation boundary. Verification remains closeout-owned.
