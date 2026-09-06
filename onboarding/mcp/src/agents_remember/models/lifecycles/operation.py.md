# mcp/src/agents_remember/models/lifecycles/operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

This module defines the strict input, durable-record, and public-projection vocabularies for asynchronous closeout and integration. It separates private operation identity and recovery evidence from the task-addressed status exposed to agents.

## Code Commentary

### Logic

The closeout and integration inputs capture every accepted decision needed for retry. Closeout input retains explicit corrective red-catalog dispositions alongside normalized input and gate policy. `LifecycleOperationRecord` persists the immutable operation fingerprint, candidate tree, gate snapshot, worker progress, boundary, terminal result, and failure evidence. `LifecycleOperationProjection` exposes task state without leaking the operation key or worker PID.

The record has separate `certification` and `integrationCertification` cells for closeout and integration selections. Each selected state belongs to the exact operation kind, key, and generation. `qualityCertification` is the completed organizational integration proof: it requires a frozen-run reference and the original, complete G1–4 terminal prefix. Its references must equal the journal-selected references, its completion fingerprint/comparison base/memory cap must match that selection, and its code commit must equal `integrationAuthority.codeCandidateCommit`.

The integration evidence vocabulary includes `IntegrationQualityCertification` (durable exact
full-Dagger code-prefix proof with result-hash revalidation and original selected references) and
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
cit:([`lifecycle_operation_dependencies`], mcp/src/agents_remember/models/lifecycles/operation.py:435-490).
`require_lifecycle_operation_dependencies` refuses `lifecycle-operation-dependencies-stale` when the
record's declared edges differ from its admitted immutable inputs
cit:([`require_lifecycle_operation_dependencies`], mcp/src/agents_remember/models/lifecycles/operation.py:493-508).

### Conventions

All models forbid extra fields. The input union is discriminated by `kind`; public status uses `StrictResponseModel` and camel-case wire names. Operation dependency edges reuse the shared evidence-dependency encoding and are recomputed before persistence and every launch/currentness gate.

### Invariants And Boundaries

- Operation identity is plane-owned and private.
- Task, operation kind, accepted input, state fingerprint, and candidate tree are immutable across retry.
- Only the public projection crosses the MCP/dashboard boundary.
- A completed integration result cannot replace its selected frozen run, terminal references, completion identity, or admitted code commit.
- Selecting or advancing either certification cell changes the meaningful-state projection; heartbeat-only writes still do not.
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

The operation model owns strict serialization and cross-field identity checks. The selected-state models own their reference shapes; the store and execution owners perform publication readback and transition checks. The public projection remains a separate same-repository model.

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout input retains the contract, effective input, approval, policy and corrective dispositions. | `CloseoutOperationInput` | mcp/src/agents_remember/models/lifecycles/operation.py:308-317 |
| The durable record carries both selected certification states and the completed quality proof. | `LifecycleOperationRecord` | mcp/src/agents_remember/models/lifecycles/operation.py:338-432 |
| Completed integration requires an exact original full code prefix and a matching result digest. | `IntegrationQualityCertification` | mcp/src/agents_remember/models/lifecycles/operation.py:205-242 |
| Attestation, passing result, comparison base and memory policy are checked together. | `_require_quality_certification_attestation`; `_require_quality_certification_result`; `_require_quality_certification_memory` | mcp/src/agents_remember/models/lifecycles/operation.py:257-271; mcp/src/agents_remember/models/lifecycles/operation.py:274-286; mcp/src/agents_remember/models/lifecycles/operation.py:289-305 |
| Completed proof must match the selected operation generation, references and integration code authority. | `_require_integration_certification_authority` | mcp/src/agents_remember/models/lifecycles/operation.py:562-585 |
| Both certification cells participate in meaningful state; ordinary durable-write revision remains separate. | `_MEANINGFUL_STATE_FIELDS`; `meaningful_state_payload`; `meaningful_state_changed` | mcp/src/agents_remember/models/lifecycles/operation.py:518-544; mcp/src/agents_remember/models/lifecycles/operation.py:547-550; mcp/src/agents_remember/models/lifecycles/operation.py:553-559 |
| The public projection intentionally omits private execution identifiers. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:341-394 |
| The R03 dependency vocabulary is shared by these record types. | `EvidenceRecordType`; `EvidenceDependencies`; `build_evidence_dependencies` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:21-30; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:99-119; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:228-237 |

## Cross-Repo References

No cross-repository vocabulary is defined here. Config/contract input and the public operation projection are same-repository contracts documented above.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository source is required for these model-local claims. | N/A | N/A |

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
| Recovery evidence records the exact code, memory-content, and ledger commits. | "class LifecycleOperationRecoveryCommits(" | mcp/src/agents_remember/models/lifecycles/operation.py:61-68 |
| Organizational publication intent records and validates accepted/intended task-document bytes and digests. | "class OrganizationalTaskPublicationIntent(" | mcp/src/agents_remember/models/lifecycles/operation.py:71-101 |
| Integration publication intent captures the claimed source operation and checks completeness of that identity. | "class IntegrationPublicationIntent(" | mcp/src/agents_remember/models/lifecycles/operation.py:104-142 |

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
publication/direct-landing/legacy cells, both selected certification states, result, and typed failure); the digest
and comparison helpers `meaningful_state_payload` and
`meaningful_state_changed` give the store, adapters, and waiters one shared
rule, so a waiter compares this field and never `recordRevision`.

## L34 Current Implementation

The operation record separately retains private preparation state. Original command/output evidence remains distinct from published mutation, approval and certification selection; it cannot be rewritten into a new command or combined with a fabricated publication claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| `LifecycleOperationRecoveryCommits` owns the corresponding behavior described above. | `LifecycleOperationRecoveryCommits` | `mcp/src/agents_remember/models/lifecycles/operation.py:65-72` |
| `OrganizationalTaskPublicationIntent` owns the corresponding behavior described above. | `OrganizationalTaskPublicationIntent` | `mcp/src/agents_remember/models/lifecycles/operation.py:75-105` |
| `_require_cancellation_evidence` owns the corresponding behavior described above. | `_require_cancellation_evidence` | `mcp/src/agents_remember/models/lifecycles/operation.py:910-928` |
| `_require_organizational_repair_evidence` owns the corresponding behavior described above. | `_require_organizational_repair_evidence` | `mcp/src/agents_remember/models/lifecycles/operation.py:931-955` |
| `_require_integration_publication` owns the corresponding behavior described above. | `_require_integration_publication` | `mcp/src/agents_remember/models/lifecycles/operation.py:958-986` |
| `_require_canonical_cancellation_handoff` owns the corresponding behavior described above. | `_require_canonical_cancellation_handoff` | `mcp/src/agents_remember/models/lifecycles/operation.py:989-1024` |

## Update History

### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-09-06T14:55:31+00:00 — Completed source verification against actual commit c69d5171187fa1957025e393270db9f5a864ab14 after rechecking equality with the independently reviewed candidate source. Preserved the curated body, all citations and earlier history; certification remains pending.

- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Documented corrective input and separate selected certification cells, exact original completion-reference/identity binding, and meaningful-state changes; repaired same-repository source citations without altering recovered history. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.


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
