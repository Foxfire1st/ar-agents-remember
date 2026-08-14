# mcp/src/agents_remember/models/lifecycles/operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T08:40+02:00 |
| lastVerifiedCommitHash |  `aeca9a2839c965218a61a3040e15cb84367ebeca`|
| lastVerifiedCommitDate |  2026-08-14T13:35:55+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

This module defines the strict input, durable-record, and public-projection vocabularies for asynchronous closeout and integration. It separates private operation identity and recovery evidence from the task-addressed status exposed to agents.

## Code Commentary

### Logic

The closeout and integration inputs capture every accepted decision needed for retry. `LifecycleOperationRecord` persists the immutable operation fingerprint, candidate tree, gate snapshot, worker progress, boundary, terminal result, and failure evidence. `LifecycleOperationProjection` exposes task state without leaking the operation key or worker PID.

### Conventions

All models forbid extra fields. The input union is discriminated by `kind`; public status uses `StrictResponseModel` and camel-case wire names.

### Invariants And Boundaries

- Operation identity is plane-owned and private.
- Task, operation kind, accepted input, state fingerprint, and candidate tree are immutable across retry.
- Only the public projection crosses the MCP/dashboard boundary.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for these internal wire models.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this strict project vocabulary. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The input and record models capture immutable approval and recovery identity. | `CloseoutOperationInput`; `LifecycleOperationRecord` | mcp/src/agents_remember/models/lifecycles/operation.py:37-106 |
| The public projection intentionally omits private execution identifiers. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:108-123 |

## Cross-Repo References

No cross-repository vocabulary is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Models represent one repository task contract and its lifecycle edge. | `CloseoutOperationInput`; `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:45-123 |

## L23 Final Candidate Disposition

Validated lifecycle-operation records carry accepted candidate identity and the monotonic recovery
commit tuple needed after post-claim crashes. Public projections derive bounded phase/report facts
from that record without exposing the private operation key or worker lease.

## Update History
- 2026-08-14T06:32+02:00 — L23 final candidate review: operation records carry exact candidate and
  recovery-commit evidence for validated monotonic reconciliation while public projections remain
  free of operation ids and worker PIDs. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved the preserved asynchronous-operation vocabulary card into the cohesive `models/lifecycles/` package and rebound its governing overview and citations; behavior is unchanged. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23 asynchronous lifecycle operation records and projections; verification provenance remains closeout-owned.
