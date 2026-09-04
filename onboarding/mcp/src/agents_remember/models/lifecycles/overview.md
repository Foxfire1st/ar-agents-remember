# mcp/src/agents_remember/models/lifecycles/ — Lifecycle Models

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/lifecycles/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Hot Path Summary

This route is the strict vocabulary for root-journal operations: generations, closeout-door and successor publication, worker termination, direct landing, legacy migration proof, and public legal controls.

Use `responses.py` for lifecycle signal vocabularies and tool responses, `finalize.py` for the
terminal finalizer response, and `operation.py` for asynchronous closeout/integration inputs,
durable records, and public projections.

## What Belongs Here

Strict lifecycle wire and durable-operation models. Lifecycle behavior, persistence, status
projection, and tool payload assembly remain in observer, worktree, application, and MCP layers.

## Operating Model

The package centralizes related model definitions without introducing a package facade.
`responses.py` owns the lifecycle state/phase vocabularies consumed by observer code;
`operation.py` separates private durable execution identity from the task-addressed public view.

## Local Invariants And Traps

- One module owns each vocabulary; consumers import it rather than copying literal sets.
- AR-owned response and operation records reject unexpected fields.
- Operation keys, worker PIDs, fingerprints, and candidate trees remain private record state.

## File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`responses.py.md`](responses.py.md) — lifecycle signal vocabularies and responses.
- [`finalize.py.md`](finalize.py.md) — terminal task-finalization response.
- [`operation.py.md`](operation.py.md) — asynchronous lifecycle operation inputs, record, and projection.

## Child Overviews

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle response vocabularies and models are owned together. | `LiveState`; `LifecycleResponse` | mcp/src/agents_remember/models/lifecycles/responses.py:16-35 |
| Finalization exposes edge proof and completion-seat result sets. | `LifecycleFinalizeTaskResponse` | mcp/src/agents_remember/models/lifecycles/finalize.py:13-37 |
| Asynchronous operation records keep private identity out of the public projection. | `LifecycleOperationRecord`; `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:311-399; mcp/src/agents_remember/models/lifecycles/operation_projection.py:341-388 |

## Docs References

No Domain Documentation source is configured.

## Cross-Repo References

No cross-repository implementation dependency governs this route.

## How To Use This Area

Read the focused model card first, then its producer/consumer references. Use the parent models
overview for registry-wide response conventions.

## L23 Final Candidate Route Disposition

This route owns the validated durable-operation record, including accepted candidate and monotonic
recovery-commit evidence. Agent-facing lifecycle responses remain task-addressed and deliberately
exclude operation keys, PIDs, leases, and resume tokens.

## 260815-DAG-L4 L4 Integration Journal Schema

Lifecycle operation records bind integration to canonical contract and repository identities, exact source and target refs, accepted commits, conflict provenance, irreversible recovery facts, and worker ownership. Legacy or incomplete integration authority fails closed rather than being synthesized.

## 260821-CLIVE-L1 Evidence And Strict Schema

Closeout lifecycle records are strict schema 3.0 and carry normalized effective input plus per-leg mutation evidence. `mutation_evidence.py` defines pre-mutation, mutation-intent, reconciled-unchanged, and commit-proven states over exact Git snapshots. Recovery cells are a derived projection, and the exact finalized-contract publication hash retains verified-existing/no-op generations without inventing Git mutation evidence. Compatibility readers and runtime bypasses are intentionally absent.

## 260821-CLIVE-L2 Current Architecture

The journal record is the durable authority after scheduling claim transfer. Retry preserves accepted input; recovery reconciles the same generation; cancellation requires exact Git/process evidence; revision publishes one linked successor. Direct landing has its own accepted input and ledger intent. Schema-1 proof is isolated and removable.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Current journal record and projection. | `_require_quality_certification_memory`; `CloseoutOperationInput`; `IntegrateOperationInput` | mcp/src/agents_remember/models/lifecycles/operation.py:263-279; mcp/src/agents_remember/models/lifecycles/operation.py:282-293; mcp/src/agents_remember/models/lifecycles/operation.py:293-309 |
| Enclosure address models. | `EnclosurePublicationState`; `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:20-25; mcp/src/agents_remember/models/lifecycles/enclosure.py:28-42 |
| Worker termination evidence. | `WorkerTerminationEvidence`; `LifecycleCancellationEvidence` | mcp/src/agents_remember/models/lifecycles/termination.py:12-33; mcp/src/agents_remember/models/lifecycles/termination.py:36-53 |

## 260821-CLIVE Final Door, Journal, And Enclosure Models

`door.py` is canonical scheduling intent with exactly waiting/deferred/withdrawn/claimed
dispositions and immutable task/repository/provenance identity. `door_response.py` is the public
join result and keeps disposable projection effects outside canonical door state. `operation.py`
owns the durable lifecycle after claim: running state, source-journal identity, commits,
certification, integration, cancellation, retirement, and supersession survive queue invalidation.

`enclosure.py` owns the terminal archive, external receipt, locator progression, and exact terminal
predecessor required for successor-enclosure publication. The former `successor.py` standalone
intent model is deleted: missing enclosure state and standalone successor WALs are not authority.
Cleanup may remove the enclosure root only after canonical entries have been externally archived,
receipted, and read back; a successor must cite that exact terminal predecessor.

## 260824-PDLS Final Lifecycle-Model Reconciliation

Operation and enclosure validation is split into named single-purpose checks for commit legs,
irreversible boundaries, recovery, legacy proof, mutation history, and worker authority. The split
preserves one strict journal-owned model surface; it does not add permissive readers, fallback
state, or queue-derived lifecycle evidence.

## 2026-08-26 Shared Operation And Control Vocabulary

`operation_kinds.py` is the single model owner for both `LifecycleOperationKind` and the closed `LifecycleControlAction` set. Worktree request DTOs, lifecycle controls, and public projections consume those types rather than declaring action literals at an effect layer. This keeps exhaustive request/response typing beside the lifecycle model vocabulary.

## MCAR-L02 Curator-Coherence Records

`curator_coherence.py` defines frozen strict source-candidate, judgment, recorded-evidence,
generation, stable-authority, snapshot, action-request, and response models. Requirement revision,
delivery attempt, candidate trees, attestation digest, record digest, and predecessor-authority
digest are different cells. Exact set validation prevents a report from silently covering eight
candidates while the current attestation contains ten.

## MCAR-L03 Pair-Bound Lifecycle Evidence

`CuratorQualityAttestation` and `CuratorCoherenceRecord` now require the complete frozen
`MemoryCandidatePairIdentity`, not merely independent code and memory tree strings. The public
coherence response carries that same pair on prepared, published, valid, and typed-refusal paths;
`pairField`, `expected`, `observed`, and `nextArgs` preserve exact mismatch and recovery facts
without exposing a second authority. This makes a record from another otherwise-valid checkout,
base, branch, onboarding root, ledger, or contract structurally ineligible for the current leaf.

## CCR-R18@v1 Generation-Coherent Projection Contracts

260831-CCR-L18 added `models/lifecycles/operation_projection.py` to this route: the closed state matrix (status/phase/worker-state/result-class/control-action cells, versioned `lifecycle-operation-state-matrix/v1`) and the revision-bound public `LifecycleOperationProjection` envelope (identity, component bindings, worker/approval/recommendation cells). `operation_kinds.py` now centralizes `LifecycleOperationStatus` and `LifecycleOperationPhase`; `operation.py` gained the monotonic `recordRevision` field and re-exports the envelope. File-level detail lives in the three sidecars.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the new `operation_projection.py` module, the centralized status/phase vocabulary, and the record revision field. File-level detail in the models/lifecycles sidecars.

- 2026-08-29T22:45+02:00 — MCAR-L03: bound quality attestations, coherence records, public
  responses, and mismatch recovery to the complete contract-derived code-memory pair identity.

- 2026-08-29T08:52+02:00 — Added the strict curator-coherence authority family and exact candidate
  judgment coverage. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — Added the centralized operation/control-action vocabulary boundary and refreshed exact lifecycle model evidence anchors.

- 2026-08-25T17:21+02:00 — Reconciled the final lifecycle validator and enclosure ownership split.
  Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled final door/journal/terminal-enclosure ownership and removed the obsolete successor model. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added organizational-completion wire models to the lifecycles route; the route purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final candidate review: the validated operation record carries
  exact candidate and recovery-commit evidence used by monotonic restart reconciliation; no private
  operation identity entered agent-facing projections. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — Created for the L23 move that groups lifecycle response, finalizer, and asynchronous-operation models under one cohesive route. Verification metadata remains closeout-owned.
