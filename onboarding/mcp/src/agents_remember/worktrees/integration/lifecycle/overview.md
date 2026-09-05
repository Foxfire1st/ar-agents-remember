# Lifecycle Operation Integration Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-05T07:12+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

The durable lifecycle-operation authority: enclosure location, journal storage, generation start
and retry, public projection, legal controls, cancellation, and completed-disposition checks.

## Hot Path Summary

Read `lifecycle_operations.py` for start/resume/retry and `lifecycle_operation_location.py` for the locator-to-enclosure chain. `lifecycle_operation_store.py` owns record and meaningful revisions; `observation/status_wait.py` waits for meaningful change, while `lifecycle_operation_projection.py` and the control projector derive one generation-coherent public view.

## Operating Model

An independent locator addresses one enclosure manifest; that manifest addresses one canonical
journal. Operations are generation-scoped and lease-owned. Projection is derived from durable
evidence and legal controls are calculated without mutating the journal.

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
| Store validation and transition construction distinguish durable-write and meaningful-state revisions. | "expected_meaningful = current.meaningfulRevision + int(" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:317-322; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:373-393 |
| The exact-generation observer returns bounded change/timeout outcomes. | "def wait_for_lifecycle_change(" | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:105-146 |

## Update History

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
