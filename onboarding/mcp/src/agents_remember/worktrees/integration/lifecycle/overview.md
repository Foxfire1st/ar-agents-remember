# Lifecycle Operation Integration Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

The durable lifecycle-operation authority: enclosure location, journal storage, generation start
and retry, public projection, legal controls, cancellation, and completed-disposition checks.

## Hot Path Summary

Read `lifecycle_operations.py` for start/resume/retry, `lifecycle_operation_location.py` for the
locator-to-enclosure chain, `lifecycle_operation_store.py` for transition validation, and
`lifecycle_operation_control_projection.py` for legal next actions.

## Operating Model

An independent locator addresses one enclosure manifest; that manifest addresses one canonical
journal. Operations are generation-scoped and lease-owned. Projection is derived from durable
evidence and legal controls are calculated without mutating the journal.

## Local Invariants And Traps

- The enclosure-root journal remains readable even when task documents are broken or edited.
- A failed generation is retryable through an explicit successor/replacement; exact duplicates
  converge rather than wedging a lane.
- Cancellation and cleanup require typed terminal evidence and cannot silently destroy commit or
  worker state.
- Public tools translate the shared read/refusal API; callers do not enumerate lower-level failure
  families independently.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `lifecycle_operations.py` | [lifecycle_operations.py.md](lifecycle_operations.py.md) | covered |
| `lifecycle_operation_location.py` | [lifecycle_operation_location.py.md](lifecycle_operation_location.py.md) | covered |
| `lifecycle_operation_store.py` | [lifecycle_operation_store.py.md](lifecycle_operation_store.py.md) | covered |
| `lifecycle_operation_projection.py` | [lifecycle_operation_projection.py.md](lifecycle_operation_projection.py.md) | covered |
| `lifecycle_operation_control_projection.py` | [lifecycle_operation_control_projection.py.md](lifecycle_operation_control_projection.py.md) | covered |
| `lifecycle_completed_disposition.py` | [lifecycle_completed_disposition.py.md](lifecycle_completed_disposition.py.md) | covered |
| `control/cancellation.py` | [control/cancellation.py.md](control/cancellation.py.md) | covered |

## Docs And Boundary References

No configured Domain Documentation or cross-repository source applies. The model/lifecycle and
integration overviews are same-repository context.

## Update History

- 2026-08-25T15:44+02:00 — Created for the enclosure-root journal, retry, cancellation, and legal
  control architecture. Verification remains closeout-owned.
