# mcp/src/agents_remember/models/lifecycles/operation.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

This module defines typed operation inputs and the strict durable record. Direct landing retains an executable journal generation. Older closeout and integration records remain readable for audit. The task-addressed public projection is a separate model.

## Current Transaction Boundary

Ordinary closeout and integration return their result inside their respective calls. The journal model retains typed closeout and integration inputs, publication evidence and certification fields for decoding earlier records. A retained field does not register or execute a lifecycle route.

## Code Commentary

### Logic

Recovery, integration authority/conflicts, and organizational repair records bind only
`codeCommit` and `memoryContentCommit`. The operation has no direct-ledger intent, ledger message,
or ledger recovery field. Expected mutation legs derive solely from enabled code/memory input;
integration publication compares those actual outputs with accepted authority.

The stored closeout and integration inputs retain their typed decisions, including corrective dispositions, normalized closeout input and gate policy. LifecycleOperationRecord retains the fingerprint, candidate tree, gate snapshot, boundary, outcome and failure evidence. Its validator drops former worker ownership fields and old leg commands before strict decode. The public projection carries no declared worker-observation component.

The record has separate `certification` and `integrationCertification` cells for closeout and integration selections. Each selected state belongs to the exact operation kind, key, and generation. `qualityCertification` is the completed organizational integration proof: it requires a frozen-run reference and the original, complete G1–4 terminal prefix. Its references must equal the journal-selected references, its completion fingerprint/comparison base/memory cap must match that selection, and its code commit must equal `integrationAuthority.codeCandidateCommit`.

The integration evidence vocabulary includes `IntegrationQualityCertification` (durable exact
full-Dagger code-prefix proof with result-hash revalidation and original selected references) and
`OrganizationalCompletionRepairEvidence` (immutable reset-generation identity). CLIVE L2 removes
the former queue-completion evidence model; integration claim/publication evidence now lives in the
journal-owned operation fields rather than a queue-removal lifecycle cell.

The retained dependency builder describes the stored operation candidate, normalized input, gate plan and validator. When applied to a closeout or direct-landing record bearing door authority, it requires the candidate tree, digest-bearing task intent and that door generation. The current direct-landing builder admits its own canonical leaf reference and exact pair without a closeout door. The dependency verifier checks supplied dependencies against its recomputed declaration.

### Conventions

The record forbids unexpected fields after the compatibility decoders run. The input union is discriminated by `kind`. Public status uses the separate strict projection model and camel-case wire names.

### Invariants And Boundaries

- Operation identity is plane-owned and private.
- Task, operation kind, accepted input, state fingerprint, and candidate tree are immutable across retry.
- Only the public projection crosses the MCP/dashboard boundary.
- A completed integration result cannot replace its selected frozen run, terminal references, completion identity, or admitted code commit.
- Selecting or advancing either certification cell changes the meaningful-state projection; heartbeat-only writes still do not.
- The retained door-evidence dependency builder applies its declared policy when called. Current ordinary transactions do not publish a new journal generation. The current direct-landing input binds its canonical leaf reference and accepted candidate separately.

### Todos

None.

### CCR private preparation boundary

Private preparation belongs to the exact stored closeout operation key and generation with its original certification. The cancellation validator matches generation and kind, requires the compatibility `workerExitProven` marker and binds every retained preparation intent digest. Same-generation direct cancellation proves no Git output and populates that marker without any process exit observation.


- The current `_require_altitude_authority` boundary implements the preparation contract above. [1]

- The record validator binds cancellation evidence to the cancelled generation and its retained preparation intent digests. Direct proof supplies the historical marker from the no-output check. [2]

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


- The reader drops retired worker fields and preparation commands. The projections of retained closeout and integration rows preserve audit evidence without offering journal controls. [10]




### Cross-Repo References

No cross-repository vocabulary is defined here. Config/contract input and the public operation projection are same-repository contracts documented above.

No separate cross-repository source is required for these model-local claims.

### 260821-CLIVE Journal-Owned Source And Door Evidence

> **Historical source account:**
>
> `IntegrationPublicationIntent` still models the exact claimed door plus source operation kind,
> generation, fingerprint, key, and source-journal digest; queue candidate identity is absent.
> Operation generations retain bounded door history and per-scope projection effects. Supersede
> declarations have their own immutable fingerprint. Direct landing no longer carries a proven door
> publication at all — that field was removed from its record builder by the closeout-door cut
> (commit `fad9808e`), and `integrate.py` no longer constructs an `IntegrationPublicationIntent`. The
> operation journal is the durable owner of running, commit, certification,
> integration, cancellation, retirement, and supersession evidence even when a projection is emptied.


## L23 Final Candidate Disposition

Validated lifecycle-operation records carry accepted candidate identity and the monotonic recovery
commit tuple needed after post-claim crashes. Public projections derive bounded phase/report facts
from that record without exposing the private operation key or worker lease.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L1 Durable Operation Model

Schema `3.0` remains strict after compatibility decoding. The reader strips the enumerated retired worker fields and old leg commands. Stored closeout records retain typed effective input, per-leg mutation evidence and optional exact finalized-contract publication proof.

## 260821-CLIVE-L2 Current Contract

The strict record retains generation, revisions and accepted input, typed code and memory mutation facts, outcome history and bounded legacy evidence. Active legal controls are derived separately by the direct-landing control projector. The scheduling projection does not supply record authority.

### Reconciled Source Evidence

- Recovery evidence records the exact code and memory-content commits. [12]
- Organizational publication intent records and validates accepted/intended task-document bytes and digests. [13]
- Integration publication intent captures the claimed source operation and checks completeness of that identity. [14]

## PDLS Reconciliation

> **Historical source account:**
>
> Lifecycle record validation was decomposed into single-purpose commit-leg, irreversible-boundary, recovery, legacy-migration, mutation-history, and worker-authority validators while preserving one strict model boundary.
>
> This change preserves the file's existing authority boundary. No threshold exception, silent
> fallback, or compatibility reader was added.

## 260831-CCR-R03 Declared Operation Dependencies

> **Historical source account:**
>
> The lifecycle record now carries `dependencies`; every claim, closeout door-intent, and
> queued-integrate writer recomputes the exact declaration from the admitted candidate, door, plan,
> and input before persistence, and launch/currentness gates re-require it (worker handover:
> notes/reports/260902-CCR-L03-worker-delivery.md). A direct-landing writer recomputes the same
> declaration from its candidate, plan, and input, without a door edge.


## 260831-CCR-L15 Meaningful-State Revision

The durable record now carries a second monotonic revision: `meaningfulRevision`
(defaults to 1, ge=1) is the CCR-R15 wait cursor that advances exactly once per
accepted store mutation whose meaningful projection subset changed, while
`recordRevision` still advances on every durable write (heartbeats, unchanged
current commands, log growth, and append-only histories advance only
`recordRevision`). The meaningful subset is the model's declared tuple. It includes cancellation evidence, mutation and recovery, both selected certification states, applicable publication and legacy cells, result and failure. The store and read-only observer use this subset and the resulting cursor.

## L34 Current Implementation

Retained preparation state binds the exact selected intent and optional output for each leg. The journal decoder drops the former command list. The store distinguishes selected private work from approval and published mutation evidence.

- `LifecycleOperationRecoveryCommits` owns the corresponding behavior described above. [15]
- `OrganizationalTaskPublicationIntent` owns the corresponding behavior described above. [16]
- `_require_cancellation_evidence` owns the corresponding behavior described above. [17]
- `_require_organizational_repair_evidence` owns the corresponding behavior described above. [18]
- `_require_integration_publication` owns the corresponding behavior described above. [19]
- `_require_canonical_cancellation_handoff` owns the corresponding behavior described above. [20]

- The R03 dependency vocabulary is shared by these record types. [11]
