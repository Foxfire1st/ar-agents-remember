# `mcp/src/agents_remember/models/lifecycles/operation_projection.py`

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Revision-bound public lifecycle-operation projection contracts (CCR-R18): the versioned state
matrix and the atomic public envelope `LifecycleOperationProjection` that one exact
operation kind, public generation, monotonic journal revision, and candidate/plan binding project.
Coherent result/approval/liveness/recommendation/control observations bind that envelope or are
omitted; an incoherent composition refuses with a bounded typed finding instead of splicing
individually-valid facts.

## Code Commentary

### Logic

`LifecycleProjectionStateRule` holds the per-kind state matrix; `classify_result`
and `validate_projection_state` check a record's cells against it, and
`validate_state_matrix_is_exhaustive` proves the matrix covers the full kind/phase/status
vocabulary. `LifecycleProjectionIdentity` carries the public identity (kind, generation,
record revision, fingerprint, contract binding); `LifecycleProjectionComponentBindings`
holds the coherent component set; envelope validators refuse unreadable projections that advertise
authority, envelopes whose components disagree with the identity, and task addresses that leave the
admitted contract scope.

### Conventions

The envelope is a strict response model with camel-case wire names and forbids extra fields.
Nested observations bind the envelope identity or are omitted — never free-standing.

### Invariants And Boundaries

- The public envelope never carries an operation key, worker PID, or lease.
- A projection is internally valid only when identity, components, and task addresses agree.
- CCR-R15: the envelope carries `meaningfulRevision`, the durable meaningful-state cursor
  of the exact journal snapshot it projects (adapters populate it for record-bound envelopes;
  unreadable journal refusals carry no record and omit it).

### Todos

None.

## Docs References

No configured external Domain Documentation source governs these internal wire contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this strict projection vocabulary. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The atomic public envelope and its per-kind state matrix. | `LifecycleOperationProjection`; `LifecycleProjectionStateRule` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:109-160; mcp/src/agents_remember/models/lifecycles/operation_projection.py:341-380 |
| CCR-R15 meaningful-state cursor on the envelope. | `meaningfulRevision` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:376-380 |
| Envelope coherence refusals keep observations internally valid. | `validate_projection_state`; `_require_unreadable_projection_has_no_authority`; `_require_component_bindings_match_envelope` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:196-217; mcp/src/agents_remember/models/lifecycles/operation_projection.py:408-421; mcp/src/agents_remember/models/lifecycles/operation_projection.py:422-443 |
| The durable record whose meaningful revision the envelope projects. | `LifecycleOperationRecord.meaningfulRevision` | mcp/src/agents_remember/models/lifecycles/operation.py:311-335 |
| The wait vocabulary that consumes the cursor. | `LifecycleWaitOutcome` | mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-46 |

## Cross-Repo References

No cross-repository projection contract is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The envelope is a same-repository task-lifecycle wire contract. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:341-380 |

## 260831-CCR-L15 Meaningful Revision On The Envelope

The envelope gained the optional `meaningfulRevision` cursor (int | None, ge=1, default
None): adapters populate it from the exact durable record's meaningful revision for record-bound
envelopes, so a status-change waiter compares the cursor it waited on against the cursor of the
envelope it receives; unreadable journal refusals carry no record and omit the field.

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card and recorded the CCR-R15 `meaningfulRevision` envelope field plus its adapter
  and waiter roles; the R18 envelope/state-matrix contract prose is preserved from the module and
  its siblings.
