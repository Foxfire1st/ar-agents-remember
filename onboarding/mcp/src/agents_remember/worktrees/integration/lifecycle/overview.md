# Lifecycle Operation Integration Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

The durable lifecycle-operation authority: enclosure location, journal storage, generation start
and retry, public projection, legal controls, cancellation, and completed-disposition checks.

## Hot Path Summary

Store recovery cells and public operation controls follow code and memory-content evidence only. Cache refresh has no operation leg, immutable ledger intent, third commit or recoverable ledger publication state; genuine Git/ref/worker evidence remains authoritative.

Read `lifecycle_operations.py` for start/resume/retry and `lifecycle_operation_location.py` for the locator-to-enclosure chain. `lifecycle_operation_store.py` owns record and meaningful revisions; `observation/status_wait.py` waits for meaningful change, while `lifecycle_operation_projection.py` and the control projector derive one generation-coherent public view.

## Generation Construction And Retained Resume

[The generation route](generation/overview.md) owns queued-record construction, integration-authority snapshots and the pure same-generation resume transition. `creation.py` returns an in-memory candidate; the lifecycle store/coordinator still own durable initial certification selection, claims and launch. `resume.py` preserves the existing worker-exit, mutation-history and retained closeout-claim rules after its path move. Use the concrete child cards before changing these boundaries.

## Operating Model

An independent locator addresses one enclosure manifest; that manifest addresses one canonical
journal. Operations are generation-scoped. Projection is derived from durable
evidence and legal controls are calculated without mutating the journal.

## De-Entanglement Cut Removals

The lock, door, operation and journal planes were deleted by the de-entanglement cut. On this route
that removed `lifecycle_operation_lease.py` (commit `1a0919c1`, "delete the lock plane"): operations
are no longer lease-owned, nothing takes a lock to prove a claim, and the accepted cost is that two
concurrent writers of the same record may lose one write. The claims elsewhere on this page that
name **leases**, the **contract-owned waiting door**, **door rows**, or **worker-exit proof** were
written against that deleted plane and were not re-derived in this pass; re-read them against the
synchronous closeout/integration route before relying on them. The surviving members listed in the
File-Level Onboarding Map above are unaffected — the map carries no deleted card.

## Local Invariants And Traps

- The enclosure-root journal remains readable even when task documents are broken or edited.
- A failed generation is retryable through an explicit successor/replacement; exact duplicates
  converge rather than wedging a lane.
- Cancellation and cleanup require typed terminal evidence and cannot silently destroy commit or
  worker state.
- A failed quality gate may leave its accepted candidate staged, and a later repair may create a
  distinct working-tree candidate. Output-free cancellation preserves both states while proving
  the protected branch ref, HEAD/tree, and reflog identity unchanged; an unattributed protected-ref
  move is a developer decision, not a same-generation retry or recovery.
- Public tools translate the shared read/refusal API; callers do not enumerate lower-level failure
  families independently.
- A cancelled closeout successor is admitted from the current contract-owned waiting door, the
  cancelled journal disposition, and proven worker exit. Publication history is retained for audit
  but is not searched for a unique predecessor that could reject an otherwise exact successor.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `lifecycle_operations.py` | [lifecycle_operations.py.md](lifecycle_operations.py.md) | covered |
| `lifecycle_operation_location.py` | [lifecycle_operation_location.py.md](lifecycle_operation_location.py.md) | covered |
| `lifecycle_operation_store.py` | [lifecycle_operation_store.py.md](lifecycle_operation_store.py.md) | covered |
| `lifecycle_operation_projection.py` | [lifecycle_operation_projection.py.md](lifecycle_operation_projection.py.md) | covered |
| `lifecycle_operation_control_projection.py` | [lifecycle_operation_control_projection.py.md](lifecycle_operation_control_projection.py.md) | covered |
| `lifecycle_operation_control_evidence.py` | [lifecycle_operation_control_evidence.py.md](lifecycle_operation_control_evidence.py.md) | covered |
| `lifecycle_completed_disposition.py` | [lifecycle_completed_disposition.py.md](lifecycle_completed_disposition.py.md) | covered |
| `control/cancellation.py` | [control/cancellation.py.md](control/cancellation.py.md) | covered |

## Docs And Boundary References

No configured Domain Documentation or cross-repository source applies. The model/lifecycle and
integration overviews are same-repository context.

## CCR-R18@v1 Generation-Coherent Projection And Revision

260831-CCR-L18 made this route's projection and store generation-coherent: `lifecycle_operation_projection.py` now builds the coherent/incoherent envelope with revision-bound identity, component bindings, worker/approval observations, recommended-action derivation, and the `bind_projection_result`/`bind_projection_decision` rebinding helpers; `lifecycle_operation_store.py` owns the monotonic `recordRevision` advance (exactly once per accepted mutation, revision-1 create gate); `lifecycle_operation_control_projection.py` adds the explicit `termination-required` cancel cell; `worker/termination.py` projects durable-termination evidence only; and `observation/projection.py` routes location/unreadable decisions through the binder. File-level detail lives in the route sidecars.

Current closeout and direct-landing journal writes require canonical `taskIntent`. A
terminal legacy generation without intent is archived byte-for-byte before an intent-bound
successor is published; active missing-intent generations refuse reuse and require a
developer decision. Closeout claim and launch verify the same intent/dependency authority
as the waiting door. No currentness check silently rewrites a live legacy record.

## Meaningful Revision And Wait Ownership

The store increments `recordRevision` on durable mutations and advances `meaningfulRevision`
only when the canonical meaningful state changes. The bounded `observation/status_wait.py`
observer consumes the latter cursor and never mutates the journal. A timeout is an unchanged
snapshot, while changed generation, invalid cursor and unreadable state remain typed outcomes.

This journal and projection work does not itself wire the R05 certificate-admission/finalization
library into the production closeout transaction. Preserve that distinction when diagnosing a
recovered legacy operation or planning certificate reuse.

| Finding | Anchor | Source |
| --- | --- | --- |
| Store transition validation requires recordRevision to advance once and meaningfulRevision to advance only when semantic state changes. | "def _validate_identity_and_evidence_transition" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:306-306 |
| The exact-generation observer returns bounded change/timeout outcomes. | "def wait_for_lifecycle_change(" | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:105-146 |

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## CCR-R12@v5 Current Lifecycle Integration Boundary

Lifecycle integration controls start, observe, cancel, resume, and recover task-addressed
transactions under fresh leases and current provenance. They preserve explicit approval, candidate
identity, source movement refusal, and ref safety while leaving strict code quality, memory quality,
selected certification, curator coherence, and independent review outside normal execution. Full
suites are an explicit developer request.

## Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

| Finding | Anchor | Source |
| --- | --- | --- |
| Recovery state contains the actual two commit outputs. | `LifecycleOperationRecoveryCommits` | mcp/src/agents_remember/models/lifecycles/operation.py:66-72 |

## Update History
- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def _validate_identity_and_evidence_transition" repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:306-306. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def _validate_identity_and_evidence_transition" repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:306-306. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Reconciled journal/store/control routing to removal of ledger recovery authority. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-11T22:39:01+00:00: Generated citation repair: "def _validate_identity_and_evidence_transition" repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:315-315. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: removed the `lifecycle_operation_lease.py` card with the deleted lock plane (commit `1a0919c1`) and added a removal note flagging the lease/door/worker-exit claims elsewhere on this page as written against the deleted plane and not re-derived. The File-Level Onboarding Map needed no change — it carried no deleted card. Verification metadata remains pinned because only the cut-affected claims were reconciled. Source documentation only; no acceptance or certification claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.

- 2026-09-06T14:48:58+00:00 — Routed the extracted generation constructors and unchanged resume transition at `c69d5171187fa1957025e393270db9f5a864ab14`; other journal/projection contracts are not reverified by this routing update. Prior verification stamps and all earlier history are preserved.


- 2026-09-05T07:12+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Added intent-bound journal writes, exact legacy retirement, and claim/launch dependency checks. Verification records source review, not execution or acceptance.


- 2026-09-05T06:12+00:00 — Combined coherent projection and status-wait ownership; clarified that journal recovery does not establish R05 certificate integration.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds the read-only status-change wait observer (`observation/status_wait.py`) and refreshes store/adapter/observation cards for the CCR-R15 `meaningfulRevision` cursor; route index regenerated.


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the generation-coherent projection envelope, store revision discipline, termination/control/observation updates. File-level detail in the lifecycle sidecars.


- 2026-08-29T10:16+02:00 — Separated failed-gate staging and successor repair bytes from protected
  Git output identity so an output-free generation can be cancelled without discarding later work.
- 2026-08-28T14:15+02:00 — PDLS closeout: reconciled the direct-recovery translator split. Typed
  direct-landing failures are reclassified against current evidence; invariant runtime errors stay
  loud instead of entering the public translation family. Stamped committed provenance.

- 2026-08-26T19:27+02:00 — Reconciled the IAS cancelled-closeout successor rule: replacement
  validates the current waiting door plus cancelled disposition and worker-exit proof; historical
  door rows remain audit evidence rather than a uniqueness authority.

- 2026-08-25T15:44+02:00 — Created for the enclosure-root journal, retry, cancellation, and legal
  control architecture. Verification remains closeout-owned.
