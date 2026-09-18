# mcp/src/agents_remember/models/lifecycles/ — Lifecycle Models

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/lifecycles/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Hot Path Summary

Operation recovery and integration authority carry code and memory-content commits only. `mutation_evidence.py` keeps the actual `head`/`headTree` and adds `contentHeadTree` for memory comparisons with root `memory.md` excluded. Prepared state admits the ordered code/content prefix and separately proves the certified content tree when an existing raw memory output still contains a legacy cache.

This route is the strict vocabulary for root-journal operations: generations, closeout-door and successor publication, worker termination, direct landing, legacy migration proof, and public legal controls.

Use `responses.py` for lifecycle signal vocabularies and tool responses, `finalize.py` for the
terminal finalizer response, and `operation.py` for asynchronous closeout/integration inputs,
durable records, and public projections. The operation record separately retains closeout selection,
integration selection, and completed organizational certification. `certification.py` and
`integration_certification.py` own those selected-reference vocabularies; execution and physical
publication readback remain outside the model layer.

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
- Selected certification belongs to one exact operation key/generation. Completed integration binds
  the same original frozen run and G1–4 references, completion fingerprint, comparison base, memory
  cap, and admitted integration code commit.
- Selection advances meaningful state; model validity alone does not prove stored publication bytes.

## File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`responses.py.md`](responses.py.md) — lifecycle signal vocabularies and responses.
- [`finalize.py.md`](finalize.py.md) — terminal task-finalization response.
- [`operation.py.md`](operation.py.md) — asynchronous lifecycle operation inputs, record, and projection.

- [`certification.py.md`](certification.py.md) — exact closeout selection, retained memory observations and append-only original terminal history.
- [`integration_certification.py.md`](integration_certification.py.md) — full integration selection, original completion identity and retained interrupted terminals.

## Child Overviews

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle response vocabularies and models are owned together. | `LiveState`; `LifecycleResponse` | mcp/src/agents_remember/models/lifecycles/responses.py:16-16; mcp/src/agents_remember/models/lifecycles/responses.py:30-35 |
| Finalization exposes edge proof and completion-seat result sets. | `LifecycleFinalizeTaskResponse` | mcp/src/agents_remember/models/lifecycles/finalize.py:14-39 |
| Asynchronous operation records keep private identity out of the public projection. | "class LifecycleOperationRecord(BaseModel):"; "class LifecycleOperationProjection(StrictResponseModel):" | mcp/src/agents_remember/models/lifecycles/operation.py:340-340; mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-340 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Recovery records have two output commits. | `LifecycleOperationRecoveryCommits` | mcp/src/agents_remember/models/lifecycles/operation.py:66-72 |
| A filtered content head does not replace actual Git head/tree facts. | `contentHeadTree` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:26-26 |
| Prepared state has an ordered two-leg prefix. | `_LEG_ORDER` | mcp/src/agents_remember/models/lifecycles/preparation_state.py:19-19 |

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

The journal record is the durable authority after scheduling claim transfer. Retry preserves accepted input; recovery reconciles the same generation; cancellation requires exact Git/process evidence; revision publishes one linked successor. Direct landing has its own accepted input and memory-content mutation evidence; the ledger intent is retired. Schema-1 proof is isolated and removable.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout and integrate inputs retain their kind-specific accepted decisions. | `CloseoutOperationInput`; `IntegrateOperationInput` | mcp/src/agents_remember/models/lifecycles/operation.py:308-317; mcp/src/agents_remember/models/lifecycles/operation.py:320-329 |
| Organizational completion proof requires original full-prefix references and the exact selected integration authority. | `IntegrationQualityCertification`; `_require_integration_certification_authority` | mcp/src/agents_remember/models/lifecycles/operation.py:205-242; mcp/src/agents_remember/models/lifecycles/operation.py:562-585 |
| Enclosure address models. | `EnclosurePublicationState`; `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:20-25; mcp/src/agents_remember/models/lifecycles/enclosure.py:28-42 |
| Worker termination evidence. | `WorkerTerminationEvidence`; `LifecycleCancellationEvidence` | mcp/src/agents_remember/models/lifecycles/termination.py:12-33; mcp/src/agents_remember/models/lifecycles/termination.py:36-53 |

## 260821-CLIVE Final Door, Journal, And Enclosure Models

`door.py` is canonical scheduling intent with exactly waiting/deferred/withdrawn/claimed
dispositions and immutable task/repository/provenance identity. The public join result
`door_response.py` was deleted with the closeout-door tool entry point (commit `6982c6a7`); no door
response model remains on this route. `operation.py`
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
base, branch, onboarding root or contract structurally ineligible for the current leaf. The consumer cache path is excluded from candidate identity.

## CCR-R18@v1 Generation-Coherent Projection Contracts

260831-CCR-L18 added `models/lifecycles/operation_projection.py` to this route: the closed state matrix (status/phase/worker-state/result-class/control-action cells, versioned `lifecycle-operation-state-matrix/v1`) and the revision-bound public `LifecycleOperationProjection` envelope (identity, component bindings, worker/approval/recommendation cells). `operation_kinds.py` now centralizes `LifecycleOperationStatus` and `LifecycleOperationPhase`; `operation.py` gained the monotonic `recordRevision` field and re-exports the envelope. File-level detail lives in the three sidecars.

## Observation Cursor Contract

`operation_wait.py` declares the status-change wait vocabulary. `operation.py` retains both
`recordRevision` for durable writes and `meaningfulRevision` for meaningful state changes;
`operation_projection.py` carries the optional public wait cursor in the versioned coherent
envelope. These revisions have different purposes and must not be substituted for one another.

| Finding | Anchor | Source |
| --- | --- | --- |
| The durable record owns both revisions; its meaningful subset includes both selected certification cells. | `LifecycleOperationRecord`; `_MEANINGFUL_STATE_FIELDS`; `meaningful_state_payload`; `meaningful_state_changed` | mcp/src/agents_remember/models/lifecycles/operation.py:343-439; mcp/src/agents_remember/models/lifecycles/operation.py:525-553; mcp/src/agents_remember/models/lifecycles/operation.py:556-559; mcp/src/agents_remember/models/lifecycles/operation.py:562-568; mcp/src/agents_remember/models/lifecycles/operation.py:521-548 |
| The public envelope carries the wait cursor beside versioned identity and component bindings. | `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-393 |

## L34 Preparation Ownership

The L34 private-output vocabulary is owned by [preparation.py](preparation.py.md), [preparation_state.py](preparation_state.py.md) and [prepared_memory.py](prepared_memory.py.md). Intent and raw-output identity, append-only command evidence and physical/logical execution views remain separate. None of these models makes a private commit a published mutation.


## Integrated IAS Recovery Contract

`preparation_state.py` separates output-command validation and command-terminal observation into focused helpers. An output still requires its original observed commit command; command history cannot be removed or restarted, and late terminal observation requires the original worker authority. The model remains a validator of selected journal facts, not a producer of Git proof.

## CCR-R12@v5 Current Model Boundary

The lifecycle model route records typed transaction inputs, explicit approval/gate-policy snapshots,
candidate/source identity, mutation evidence, recovery facts, and terminal results. Retained
certification and quality fields remain strict vocabulary for explicit or historical callers, but
normal closeout/integration workers do not select, populate, or require them. Model presence is not
normal transaction acceptance evidence.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "class LifecycleOperationRecord(BaseModel):"; "class LifecycleOperationProjection(StrictResponseModel):" repointed to mcp/src/agents_remember/models/lifecycles/operation.py:340-340; mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-340. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `LifecycleOperationProjection` repointed to mcp/src/agents_remember/models/lifecycles/operation_projection.py:340-393. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Removed ledger intent/output authority and documented raw versus filtered memory snapshot identities. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `mcp/src/agents_remember/models/lifecycles/` route changed since the recorded verification commit.
  Re-read the card against the frozen on-disk source and re-checked its claims and cited ranges:
  nothing this card asserts is falsified by the change, so no wording changed. Verification metadata
  remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the route's files last
  moved before this task line. Re-read the route card and spot-checked its cited anchors against the
  current source: they still resolve. No wording changed; verification metadata remains
  closeout-owned.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: recorded that `door_response.py` was deleted with the closeout-door tool entry point (commit `6982c6a7`) and dropped the stale "public join result" claim. Only this cut-affected claim was reconciled; the rest of this route was not re-read in this pass, so verification metadata remains pinned. Source documentation only; no acceptance or certification claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/models/lifecycles`, so no route/member/prose/invariant change is required. route-member-count=24; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-09-06T15:08:14+00:00 — Added the current selected-certification/refusal source routes and their precise fixture/model boundaries; corrected stale pending-candidate wording where present. Preserved broader prior verification stamps and all earlier history.

- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Added selected versus completed certification vocabulary and exact integration identity invariants; repaired affected operation/model source anchors. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.




- 2026-09-05T06:21+00:00 — Re-read the reopened affected citation claims against the frozen source, corrected their current wording/ranges, and replaced ambiguous symbols with exact declaration anchors. Verification records this source-backed claim review; it is not a code acceptance or final Gate-5 verdict.

- 2026-09-05T06:12+00:00 — Combined coherent projection and status-wait vocabularies; corrected current source anchors and distinguished record from meaningful revisions.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds the typed status-change wait vocabulary (`operation_wait.py`) and refreshes `operation.py` / `operation_projection.py` with the CCR-R15 `meaningfulRevision` cursor; route index regenerated.


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
