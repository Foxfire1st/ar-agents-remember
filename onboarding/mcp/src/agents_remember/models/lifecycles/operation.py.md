# mcp/src/agents_remember/models/lifecycles/operation.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

This module defines the strict input, durable-record, and public-projection vocabularies for asynchronous closeout and integration. It separates private operation identity and recovery evidence from the task-addressed status exposed to agents.

## CCR-R12@v5 Current Transaction Boundary

Normal closeout/integration records carry the typed operation input, explicit approval and gate
policy snapshot, candidate/source identity, progress, mutation evidence, and terminal result needed
for a recoverable Git transaction. The retained `certification`, `integrationCertification`, and
`qualityCertification` model vocabulary remains available for explicit or historical callers, but
the normal worker does not select, execute, or require those fields for closeout or integration.
Their presence in this strict schema must not be read as a normal closeout quality or certification
gate.

## Code Commentary

### Logic

Recovery, integration authority/conflicts, and organizational repair records bind only
`codeCommit` and `memoryContentCommit`. The operation has no direct-ledger intent, ledger message,
or ledger recovery field. Expected mutation legs derive solely from enabled code/memory input;
integration publication compares those actual outputs with accepted authority.

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
operation input, gate-policy rail plan, and validator; the **closeout** operation additionally binds the exact
code tree, digest-bearing task intent, and admitted closeout-door generation, refusing
`lifecycle-operation-candidate-dependencies-missing` or
`lifecycle-operation-door-dependency-missing` when absent
cit:([`lifecycle_operation_dependencies`], mcp/src/agents_remember/models/lifecycles/operation.py:438-493).
Since the closeout-door cut (commit `fad9808e`) a **direct landing** binds neither a leaf task intent
nor a door: `LifecycleOperationRecord` requires the task-intent state for `closeout` only, because a
direct landing is a series-contract, branch-addressed delivery with no leaf task document to bind and
no closeout door to state one for it.
`require_lifecycle_operation_dependencies` refuses `lifecycle-operation-dependencies-stale` when the
record's declared edges differ from its admitted immutable inputs
cit:([`require_lifecycle_operation_dependencies`], mcp/src/agents_remember/models/lifecycles/operation.py:496-511).

### Conventions

All models forbid extra fields. The input union is discriminated by `kind`; public status uses `StrictResponseModel` and camel-case wire names. Operation dependency edges reuse the shared evidence-dependency encoding and are recomputed before persistence and every launch/currentness gate.

### Invariants And Boundaries

- Operation identity is plane-owned and private.
- Task, operation kind, accepted input, state fingerprint, and candidate tree are immutable across retry.
- Only the public projection crosses the MCP/dashboard boundary.
- A completed integration result cannot replace its selected frozen run, terminal references, completion identity, or admitted code commit.
- Selecting or advancing either certification cell changes the meaningful-state projection; heartbeat-only writes still do not.
- The declared dependencies are the admitted door (closeout only), certifying plan, and acceptance candidate; a
  record never binds a universal candidate tuple, and dependencies are omitted only when the
  record-type policy proves the record never reads them. A direct-landing record declares no door edge.

### Todos

None.

### CCR private preparation boundary

Preparation is meaningful operation state and belongs only to the exact closeout operation key/generation with certification authority. Cancellation evidence must bind every selected preparation intent digest as well as prove this generation’s worker exit. Retained private work is separate from approval consumption and published mutation evidence.

- The current `_require_altitude_authority` boundary implements the preparation contract above. [1]
- The current `_require_cancellation_evidence` boundary implements the preparation contract above. [2]

## Evidence

### Docs References

No external Domain Documentation source is configured for these internal wire models.

No configured external source governs this strict project vocabulary.

### Repo-Internal References

The operation model owns strict serialization and cross-field identity checks. The selected-state models own their reference shapes; the store and execution owners perform publication readback and transition checks. The public projection remains a separate same-repository model.

- Recovery and integration authority retain real code/memory outputs and validate those outputs against accepted publication. [3]
- Closeout input retains the contract, effective input, approval, policy and corrective dispositions. [4]
- The durable record carries both selected certification states and the completed quality proof. [5]
- Completed integration requires an exact original full code prefix and a matching result digest. [6]
- Attestation, passing result, comparison base and memory policy are checked together. [7]
- Completed proof must match the selected operation generation, references and integration code authority. [8]
- Both certification cells participate in meaningful state; ordinary durable-write revision remains separate. [9]
- The public projection intentionally omits private execution identifiers. [10]
- The R03 dependency vocabulary is shared by these record types. [11]

### Cross-Repo References

No cross-repository vocabulary is defined here. Config/contract input and the public operation projection are same-repository contracts documented above.

No separate cross-repository source is required for these model-local claims.

### 260821-CLIVE Journal-Owned Source And Door Evidence

`IntegrationPublicationIntent` still models the exact claimed door plus source operation kind,
generation, fingerprint, key, and source-journal digest; queue candidate identity is absent.
Operation generations retain bounded door history and per-scope projection effects. Supersede
declarations have their own immutable fingerprint. Direct landing no longer carries a proven door
publication at all — that field was removed from its record builder by the closeout-door cut
(commit `fad9808e`), and `integrate.py` no longer constructs an `IntegrationPublicationIntent`. The
operation journal is the durable owner of running, commit, certification,
integration, cancellation, retirement, and supersession evidence even when a projection is emptied.


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

- Recovery evidence records the exact code and memory-content commits. [12]
- Organizational publication intent records and validates accepted/intended task-document bytes and digests. [13]
- Integration publication intent captures the claimed source operation and checks completeness of that identity. [14]

## PDLS Reconciliation

Lifecycle record validation was decomposed into single-purpose commit-leg, irreversible-boundary, recovery, legacy-migration, mutation-history, and worker-authority validators while preserving one strict model boundary.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.

## 260831-CCR-R03 Declared Operation Dependencies

The lifecycle record now carries `dependencies`; every claim, closeout door-intent, and
queued-integrate writer recomputes the exact declaration from the admitted candidate, door, plan,
and input before persistence, and launch/currentness gates re-require it (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md). A direct-landing writer recomputes the same
declaration from its candidate, plan, and input, without a door edge.


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

- `LifecycleOperationRecoveryCommits` owns the corresponding behavior described above. [15]
- `OrganizationalTaskPublicationIntent` owns the corresponding behavior described above. [16]
- `_require_cancellation_evidence` owns the corresponding behavior described above. [17]
- `_require_organizational_repair_evidence` owns the corresponding behavior described above. [18]
- `_require_integration_publication` owns the corresponding behavior described above. [19]
- `_require_canonical_cancellation_handoff` owns the corresponding behavior described above. [20]
