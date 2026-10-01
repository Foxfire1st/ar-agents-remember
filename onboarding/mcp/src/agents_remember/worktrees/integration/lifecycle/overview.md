# Lifecycle Operation Integration Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

The durable lifecycle-operation authority: enclosure location, journal storage, generation start
and retry, public projection, legal controls, cancellation, and completed-disposition checks.

## Hot Path Summary

Store recovery cells and public operation controls follow code and memory-content evidence only. Cache refresh has no operation leg, immutable ledger intent, third commit or recoverable ledger publication state; genuine Git/ref/worker evidence remains authoritative.

Read `lifecycle_operations.py` for start/resume/retry and `lifecycle_operation_location.py` for the locator-to-enclosure chain. `lifecycle_operation_store.py` owns record and meaningful revisions; `observation/status_wait.py` waits for meaningful change, while `lifecycle_operation_projection.py` and the control projector derive one generation-coherent public view.

## 260928-MIK-L09 Cancellation Restores A Direct Landing's Closing

**Route impact (MIK-R09@v2, leaf 260928-MIK-L09; review R1 F3 and R2-5).** A direct landing on converted memory
closes the leaf's history file before its journal generation exists and keeps the closing in a per-generation receipt
(`worktrees/knowledge_gate.keep_direct_closing`). For a `direct-landing` record, `control/cancellation.cancel_operation`
now checks every receipt before anything is terminated or published (an unreadable receipt is
`direct-landing-closing-receipt-unreadable`, next action `developer-decision`), and once the cancelled outcome is
published, or on a repeated cancel, settles the generation's receipt as `cancelled`: the file is restored to its
previous bytes, never over a later edit. Cancellation's no-output proof means no memory commit exists at that point.
Other operation kinds are untouched; unconverted direct landings keep no closing. Tested by
`test_cancelling_the_generation_restores_the_file_it_closed_but_never_a_later_edit` and
`test_an_unreadable_closing_receipt_is_a_named_refusal_at_apply_and_at_cancel`.

- The receipt check before anything moves, and the restore after publication. [1]

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

## Evidence

### Docs And Boundary References

No configured Domain Documentation or cross-repository source applies. The model/lifecycle and
integration overviews are same-repository context.

### Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

- Recovery state contains the actual two commit outputs. [2]

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

- Store transition validation requires recordRevision to advance once and meaningfulRevision to advance only when semantic state changes. [3]
- The exact-generation observer returns bounded change/timeout outcomes. [4]

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## CCR-R12@v5 Current Lifecycle Integration Boundary

Lifecycle integration controls start, observe, cancel, resume, and recover task-addressed
transactions under fresh leases and current provenance. They preserve explicit approval, candidate
identity, source movement refusal, and ref safety while leaving strict code quality, memory quality,
selected certification, curator coherence, and independent review outside normal execution. Full
suites are an explicit developer request.
