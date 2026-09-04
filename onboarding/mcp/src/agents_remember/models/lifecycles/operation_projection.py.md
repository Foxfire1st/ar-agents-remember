# mcp/src/agents_remember/models/lifecycles/operation_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Owns the versioned public projection contracts introduced by CCR-R18 (260831-CCR-L18): the
lifecycle-operation state matrix and the atomic public envelope that every lifecycle observation
must satisfy. The module guarantees that one public observation is an internally valid projection
of one exact operation kind, public generation, monotonic journal revision, and candidate/plan
binding; a composition that splices individually-valid facts across revisions is refused with a
bounded typed finding instead of being surfaced.

## Code Commentary

### Logic

The module is split between a pure state vocabulary and the wire models that consume it.

State vocabulary (import-time `validate_state_matrix_is_exhaustive`):

- `LifecycleProjectionWorkerState` (live / termination-requested / termination-required / exited),
  `LifecycleProjectionResultClass` (none / progress / recovery / developer-decision / termination /
  terminal), and `LifecycleProjectionControlAction` (retry / recover / cancel / revise / retire /
  supersede / integrate / direct-landing) are the closed public classes (lines 32-55).
- `STATE_MATRIX_VERSION = "lifecycle-operation-state-matrix/v1"` (line 57) versions the matrix.
- `STATE_MATRIX` (lines 116-160) maps every public `LifecycleOperationStatus` to a
  `LifecycleProjectionStateRule` that declares the admitted phases, worker states, result classes,
  and control actions for that status. `_RUNNING_PHASES` / `_DIRECT_PHASES` /
  `_INPUT_REQUIRED_PHASES` (lines 59-107) are the shared phase cells; `input-required` deliberately
  admits the running phases that shared evidence reporters legitimately park under
  (`memory-commit`, `ledger-commit`, `recovering-after-claim`) plus the contract-finalization and
  direct-landing decision cells.
- `classify_result` (lines 171-194) turns a public result mapping into a result class:
  worker-termination-required maps to `termination`, a developer-decision flag/next-action maps to
  `developer-decision`, terminal statuses map to `terminal`, retry/recover/retire edges map to
  `recovery`, and everything else is `progress`.
- `validate_projection_state` (lines 196-217) and `_validate_projection_cell` (lines 219-260) reject
  every status/phase/worker-state/result/control cell not declared by the matrix, and additionally
  refuse `cancelRequested` outside `termination-required`/`cancelled` and non-`cancel` controls on a
  `termination-required` cell. `LifecycleProjectionIncoherence` (lines 162-169) carries the bounded
  expected/observed facts that become the read-only public refusal.
- `validate_state_matrix_is_exhaustive` (lines 262-289) fails the import if either the public status
  or phase vocabulary changes without the matrix being updated, so the matrix cannot silently drift.

Wire envelope (all `StrictResponseModel`):

- `LifecycleProjectionIdentity` (lines 293-303) names one exact journal snapshot: operation kind,
  contract path, generation, `recordRevision`, candidate-tuple digest, plan-identity digest, and a
  digest over the whole tuple.
- `LifecycleProjectionComponentBindings` (lines 305-313) claims the envelope identity digest for
  each optional nested component (result / approval / worker / recommendedAction / legalControls).
- `LifecycleWorkerObservation` (lines 315-323) and `LifecycleApprovalObservation` (lines 325-329)
  expose liveness/approval class without leaking process or lease authority.
- `LifecycleRecommendedAction` (lines 331-339) is the required recovery edge, distinct from the
  optional `legalControls`.
- `LifecycleOperationProjection` (lines 341-388) is the coherent task-addressed envelope with
  `schemaVersion` and `stateMatrixVersion` literals; its `after` validator routes an
  `unreadable`/`incoherent`/coherent envelope through the private guards
  (`_require_unreadable_projection_has_no_authority`, `_require_component_bindings_match_envelope`,
  `_require_coherent_projection_components`, `_require_recommendation_coherence`,
  `_require_projection_task_addresses`, lines 390-513) so identity-less, mis-bound, or
  cross-task-addressed compositions never serialize.

### Conventions

Public projection vocabulary lives in `models/` (no I/O or scheduling ownership); the projection
*construction* that fills the envelope from a durable record lives in
`worktrees/integration/lifecycle/lifecycle_operation_projection.py`. Every model forbids extra
fields; bindings are digest-for-digest, never trusted copies.

### Invariants And Boundaries

- One coherent public observation binds exactly one journal revision; revision and generation
  splicing is refused, not smoothed over.
- Only the public projection crosses the MCP/dashboard boundary; identity digests are derived, not
  transmitted secrets.
- An `unreadable` or `incoherent` envelope cannot advertise recommended action, legal controls, or
  cancellability.
- Guidance that names a task address must name the envelope's own contract path.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these internal wire models.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this strict project vocabulary. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The durable record and input vocabulary this projection reads. | `LifecycleOperationRecord`; `CloseoutOperationInput` | mcp/src/agents_remember/models/lifecycles/operation.py:282-293; mcp/src/agents_remember/models/lifecycles/operation.py:311-399 |
| The status/phase/kind vocabulary the matrix exhausts. | `LifecycleOperationStatus`; `LifecycleOperationPhase`; `LifecycleOperationKind` | mcp/src/agents_remember/models/lifecycles/operation_kinds.py:4-39 |
| The construction site that fills the envelope from a record and rewrites results/decisions through the sole validator. | `operation_projection`; `bind_projection_result`; `bind_projection_decision`; `operation_projection_identity` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:81-330 |
| The task-intent identity projected onto the wire. | `TaskIntentIdentity` | mcp/src/agents_remember/models/task_intent/__init__.py:55-79 |
| The digest helper used for candidate/plan/identity digests. | `canonical_sha256` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:327-348 |
| The schema/TS consumer of the envelope shape. | `LifecycleOperationProjection` | dashboard/src/types/projection.ts:335-396 |
| The forcing suite that pins the matrix and envelope cells. | `validate_state_matrix_is_exhaustive` | mcp/tests/test_generation_coherent_lifecycle_projection.py:570-575 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository projection vocabulary; nothing crosses repositories. | — | — |

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: created for the new
  revision-bound public projection module (state matrix v1, identity/binding/worker/approval/
  recommendation cells, and the coherent `LifecycleOperationProjection` envelope moved out of
  `operation.py`). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.
