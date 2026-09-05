# mcp/src/agents_remember/models/lifecycles/operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T08:46+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
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

Under CCR-R03@v1 the durable record carries a typed direct-dependency declaration:
`lifecycle_operation_dependencies` maps the operation kind to the correct record type
(`lifecycle-closeout-operation/v3` / `lifecycle-direct-landing-operation/v3` /
`lifecycle-integration-operation/v3`) and declares the admitted candidate state, normalized
operation input, gate-policy rail plan, and validator; commit operations additionally bind the exact
code tree, digest-bearing task intent, and admitted closeout-door generation, refusing
`lifecycle-operation-candidate-dependencies-missing` or
`lifecycle-operation-door-dependency-missing` when absent
cit:([`lifecycle_operation_dependencies`], mcp/src/agents_remember/models/lifecycles/operation.py:428-484).
`require_lifecycle_operation_dependencies` refuses `lifecycle-operation-dependencies-stale` when the
record's declared edges differ from its admitted immutable inputs
cit:([`require_lifecycle_operation_dependencies`], mcp/src/agents_remember/models/lifecycles/operation.py:464-479).

### Conventions

All models forbid extra fields. The input union is discriminated by `kind`; public status uses `StrictResponseModel` and camel-case wire names. Operation dependency edges reuse the shared evidence-dependency encoding and are recomputed before persistence and every launch/currentness gate.

### Invariants And Boundaries

- Operation identity is plane-owned and private.
- Task, operation kind, accepted input, state fingerprint, and candidate tree are immutable across retry.
- Only the public projection crosses the MCP/dashboard boundary.
- The declared dependencies are the admitted door, certifying plan, and acceptance candidate; a
  record never binds a universal candidate tuple, and dependencies are omitted only when the
  record-type policy proves the record never reads them.

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
| The closeout input records the exact contract, normalized effective input, approval note, and gate-policy snapshot. | "class CloseoutOperationInput(" | mcp/src/agents_remember/models/lifecycles/operation.py:282-290 |
| The durable operation record captures candidate/approval identity, mutation evidence, and recovery outputs. | "class LifecycleOperationRecord(" | mcp/src/agents_remember/models/lifecycles/operation.py:311-403 |
| The public projection intentionally omits private execution identifiers. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:38-38 |
| The R03 dependency vocabulary used by these record types. | `EvidenceRecordType`, `EvidenceDependencies`, `build_evidence_dependencies` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:21-54; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:99-122; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:228-239 |

## Cross-Repo References

No cross-repository vocabulary is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The closeout input names one config and task contract for the lifecycle operation. | "class CloseoutOperationInput(" | mcp/src/agents_remember/models/lifecycles/operation.py:282-290 |
| The task-addressed public lifecycle envelope is defined in operation_projection and re-exported by this module. | "class LifecycleOperationProjection(" | mcp/src/agents_remember/models/lifecycles/operation_projection.py:341-394 |

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
| Recovery evidence records the exact code, memory-content, and ledger commits. | "class LifecycleOperationRecoveryCommits(" | mcp/src/agents_remember/models/lifecycles/operation.py:50-57 |
| Organizational publication intent records and validates accepted/intended task-document bytes and digests. | "class OrganizationalTaskPublicationIntent(" | mcp/src/agents_remember/models/lifecycles/operation.py:60-90 |
| Integration publication intent captures the claimed source operation and checks completeness of that identity. | "class IntegrationPublicationIntent(" | mcp/src/agents_remember/models/lifecycles/operation.py:93-131 |

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

## 260831-CCR-R03 Declared Operation Dependencies

The lifecycle record now carries `dependencies`; every claim, direct-landing, door-intent, and
queued-integrate writer recomputes the exact declaration from the admitted candidate, door, plan,
and input before persistence, and launch/currentness gates re-require it (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).


## 260831-CCR-L15 Meaningful-State Revision

The durable record now carries a second monotonic revision: `meaningfulRevision`
(defaults to 1, ge=1) is the CCR-R15 wait cursor that advances exactly once per
accepted store mutation whose meaningful projection subset changed, while
`recordRevision` still advances on every durable write (heartbeats, unchanged
current commands, log growth, and append-only histories advance only
`recordRevision`). `_MEANINGFUL_STATE_FIELDS` names exactly the durable
journal fields that move the cursor (generation, generationDisposition, status,
phase, attempt, approval claim, irreversible boundary, cancellation evidence,
worker termination, mutation evidence, recovery commits, finalization,
publication/direct-landing/legacy cells, result, and typed failure); the digest
and comparison helpers `meaningful_state_payload` and
`meaningful_state_changed` give the store, adapters, and waiters one shared
rule, so a waiter compares this field and never `recordRevision`.

## Update History

- 2026-09-05T07:19:22+00:00 — L31-MR-02 history recovery: restored the original dated L18 entry verbatim from memory commit fd41221f11dfe5ac2993520c0d7176ada59ce2ba (its recorded code provenance: f93ac631ca161e5880db3a937728cb256686b13b). This preserves sibling curation history; current body and verification metadata are unchanged.


- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 3 declined citation claims against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Chose the concrete input and record definitions instead of neighboring integration fields and annotations. Repointed public projection evidence to its actual definition owner while retaining the task-boundary claim. Separated three durable-evidence models and corrected ranges to their exact definitions. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `LifecycleOperationProjection` repointed to mcp/src/agents_remember/models/lifecycles/operation.py:38-38. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `require_lifecycle_operation_dependencies` repointed to mcp/src/agents_remember/models/lifecycles/operation.py:464-479. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the durable `meaningfulRevision` wait cursor on `LifecycleOperationRecord`, the `_MEANINGFUL_STATE_FIELDS` subset, and the `meaningful_state_payload`/`meaningful_state_changed` digest helpers shared by the store and waiters.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the generation-coherent projection split — status/phase vocabulary moved to `operation_kinds.py`, the public envelope moved to `operation_projection.py` (re-exported here), and `LifecycleOperationRecord.recordRevision` added as the monotonic journal revision. Re-anchored the projection references off the deleted in-file class. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the typed direct-dependency declaration on lifecycle operation records, the per-kind dependency builders, and the launch/currentness refusal; prior input/record/projection prose preserved.

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
