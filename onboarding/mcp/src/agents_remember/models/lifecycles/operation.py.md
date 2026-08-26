# mcp/src/agents_remember/models/lifecycles/operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

This module defines the strict input, durable-record, and public-projection vocabularies for asynchronous closeout and integration. It separates private operation identity and recovery evidence from the task-addressed status exposed to agents.

## Code Commentary

### Logic

The closeout and integration inputs capture every accepted decision needed for retry. `LifecycleOperationRecord` persists the immutable operation fingerprint, candidate tree, gate snapshot, worker progress, boundary, terminal result, and failure evidence. `LifecycleOperationProjection` exposes task state without leaking the operation key or worker PID.

The integration evidence vocabulary includes `IntegrationQualityCertification` (durable exact
full-Dagger proof with result-hash revalidation) and
`OrganizationalCompletionRepairEvidence` (immutable reset-generation identity). CLIVE L2 removes
the former queue-completion evidence model; integration claim/publication evidence now lives in the
journal-owned operation fields rather than a queue-removal lifecycle cell.

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
| The input and record models capture immutable approval and recovery identity. | `CloseoutOperationInput`; `LifecycleOperationRecord` | mcp/src/agents_remember/models/lifecycles/operation.py:295-303; mcp/src/agents_remember/models/lifecycles/operation.py:324-389 |
| The public projection intentionally omits private execution identifiers. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:801-819 |

## Cross-Repo References

No cross-repository vocabulary is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Models represent one repository task contract and its lifecycle edge. | `CloseoutOperationInput`; `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:300-308; mcp/src/agents_remember/models/lifecycles/operation.py:801-819 |

## L23 Final Candidate Disposition

Validated lifecycle-operation records carry accepted candidate identity and the monotonic recovery
commit tuple needed after post-claim crashes. Public projections derive bounded phase/report facts
from that record without exposing the private operation key or worker lease.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L1 Durable Operation Model

Closeout durable input contains only typed `effectiveInput`; schema reading is strict `3.0` with no compatibility reader, fallback, or runtime bypass. Closeout progress carries per-leg mutation evidence and an optional exact finalized-contract publication hash. Model validators keep enabled legs, evidence repositories, derived recovery commits, and generation retention consistent, so recovery cells cannot contradict authoritative proof.

## 260821-CLIVE-L2 Current Contract

The current source seams include `LifecycleOperationRecoveryCommits`, `OrganizationalTaskPublicationIntent`, `IntegrationPublicationIntent`. The lifecycle record now owns operation generation, legal controls, root-journal publication, door/successor state, worker termination, direct landing, and bounded legacy proof. Queue projection is absent from the authoritative lifecycle union.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `LifecycleOperationRecoveryCommits`, `OrganizationalTaskPublicationIntent`, `IntegrationPublicationIntent` at this ownership boundary. | `LifecycleOperationRecoveryCommits`; `OrganizationalTaskPublicationIntent`; `IntegrationPublicationIntent` | mcp/src/agents_remember/models/lifecycles/operation.py:68-75; mcp/src/agents_remember/models/lifecycles/operation.py:78-108; mcp/src/agents_remember/models/lifecycles/operation.py:111-149 |

## 260821-CLIVE Journal-Owned Source And Door Evidence

Integration publication now transfers the exact claimed door plus source operation kind,
generation, fingerprint, key, and source-journal digest; queue candidate identity is absent.
Operation generations retain bounded door history and per-scope projection effects. Supersede
declarations have their own immutable fingerprint, and direct landing may carry the same proven door
publication. The operation journal is the durable owner of running, commit, certification,
integration, cancellation, retirement, and supersession evidence even when a projection is emptied.


## PDLS Reconciliation

Lifecycle record validation was decomposed into single-purpose commit-leg, irreversible-boundary, recovery, legacy-migration, mutation-history, and worker-authority validators while preserving one strict model boundary.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced residual queue bindings with exact door/source-journal evidence and supersede identity. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added the immutable wire models `IntegrationQualityCertification`, `IntegrationQueueCompletionEvidence`, and `OrganizationalCompletionRepairEvidence` for the organizational-completion full gate, queue removal, and repair path. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 final candidate review: operation records carry exact candidate and
  recovery-commit evidence for validated monotonic reconciliation while public projections remain
  free of operation ids and worker PIDs. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved the preserved asynchronous-operation vocabulary card into the cohesive `models/lifecycles/` package and rebound its governing overview and citations; behavior is unchanged. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23 asynchronous lifecycle operation records and projections; verification provenance remains closeout-owned.
