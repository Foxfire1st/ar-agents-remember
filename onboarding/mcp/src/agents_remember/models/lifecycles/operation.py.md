# mcp/src/agents_remember/models/lifecycles/operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

This module defines the strict input, durable-record, and public-projection vocabularies for asynchronous closeout and integration. It separates private operation identity and recovery evidence from the task-addressed status exposed to agents.

## Code Commentary

### Logic

The closeout and integration inputs capture every accepted decision needed for retry. `LifecycleOperationRecord` persists the immutable operation fingerprint, candidate tree, gate snapshot, worker progress, boundary, terminal result, and failure evidence. `LifecycleOperationProjection` exposes task state without leaking the operation key or worker PID.

Added the three L5 wire models: `IntegrationQualityCertification` (durable exact full-Dagger proof with result-hash revalidation), `IntegrationQueueCompletionEvidence` (durable queue-removal intent), and `OrganizationalCompletionRepairEvidence` (immutable reset-generation identity).

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
| The input and record models capture immutable approval and recovery identity. | `CloseoutOperationInput`; `LifecycleOperationRecord` | mcp/src/agents_remember/models/lifecycles/operation.py:218-226; mcp/src/agents_remember/models/lifecycles/operation.py:246-291 |
| The public projection intentionally omits private execution identifiers. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:394-409 |

## Cross-Repo References

No cross-repository vocabulary is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Models represent one repository task contract and its lifecycle edge. | `CloseoutOperationInput`; `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:218-226; mcp/src/agents_remember/models/lifecycles/operation.py:394-409 |

## L23 Final Candidate Disposition

Validated lifecycle-operation records carry accepted candidate identity and the monotonic recovery
commit tuple needed after post-claim crashes. Public projections derive bounded phase/report facts
from that record without exposing the private operation key or worker lease.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L1 Durable Operation Model

Closeout durable input contains only typed `effectiveInput`; schema reading is strict `3.0` with no compatibility reader, fallback, or runtime bypass. Closeout progress carries per-leg mutation evidence and an optional exact finalized-contract publication hash. Model validators keep enabled legs, evidence repositories, derived recovery commits, and generation retention consistent, so recovery cells cannot contradict authoritative proof.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added the immutable wire models `IntegrationQualityCertification`, `IntegrationQueueCompletionEvidence`, and `OrganizationalCompletionRepairEvidence` for the organizational-completion full gate, queue removal, and repair path. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 final candidate review: operation records carry exact candidate and
  recovery-commit evidence for validated monotonic reconciliation while public projections remain
  free of operation ids and worker PIDs. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved the preserved asynchronous-operation vocabulary card into the cohesive `models/lifecycles/` package and rebound its governing overview and citations; behavior is unchanged. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23 asynchronous lifecycle operation records and projections; verification provenance remains closeout-owned.
