# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-08T16:05:21+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532` |
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Application overview](../overview.md)

## What This Area Is

Public application adapters for starting, observing, controlling, and executing durable lifecycle
operations. These modules translate configuration and caller context into typed worktree-domain
requests; they do not own journal transition policy.

## Hot Path Summary

Use `lifecycle_status_wait.py` for bounded read-only change waits, `direct_landing.py` for the public direct route, and `lifecycle_operation_worker.py` / `terminal_rail_failure.py` for typed detached-worker terminalization. Journal transition policy remains in the worktree lifecycle domain.

## Complete Admission Refusals

[`certification_refusal.py`](certification_refusal.py.md) renders all typed admission findings, including nested byte evidence, for public adapters. Its zero-start refusal shape reports the admission boundary; the renderer itself does not observe processes or alter journal state.

CCR-R25 also promotes a typed `routeReview` finding through the shared route-review refusal
projection, preserving the complete certification finding list while adding exact status and
contract-bound next-step guidance when a contract is available. The lifecycle adapter remains a
projection boundary; it does not record a review or mutate task state.

## Operating Model

Application tools admit configured contracts, resolve durable operation locations, invoke the
worktree lifecycle owners, and project typed refusals. The worker binds default services, owns one
lease, advances the durable record, and publishes a terminal result without inventing recovery.
Since CCR-R20 the detached worker's `OperationRuntime.fail` applies the typed terminal
rail-failure envelope (`terminal_rail_failure.py`) for otherwise-unclassified failures when a durable record exists (retained organizational
repair and ledger-recovery decisions take precedence), so
failed-rail facts reach the journal instead of a generic exception. Configured-contract admission
remains strict by default. Exact code-memory pair consumers may
delegate only candidate-worktree identity to the canonical pair validator; repository, task, and
enclosure authority remain at the application boundary.

## Local Invariants And Traps

- Application adapters translate lower-level failure families once; public callers must not
  reproduce the complete exception vocabulary.
- A delegated candidate check must have one explicit downstream owner; it must not become an
  unchecked permissive mode.
- Durable journal and enclosure state outrank task projections or stale in-memory observations.
- A direct operation is a distinct route, not an implicit fallback from queued closeout.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `direct_landing.py` | [direct_landing.py.md](direct_landing.py.md) | covered |
| `lifecycle_operation_worker.py` | [lifecycle_operation_worker.py.md](lifecycle_operation_worker.py.md) | covered |
| `terminal_rail_failure.py` | [terminal_rail_failure.py.md](terminal_rail_failure.py.md) | covered |
| `lifecycle_status_wait.py` | [lifecycle_status_wait.py.md](lifecycle_status_wait.py.md) | covered |

## Docs And Boundary References

No Domain Documentation or cross-repository source is configured for this route. Same-repository
authority is documented by the linked source sidecars and the worktrees integration overview.

## Read-Only Status Change Wait

`lifecycle_status_wait.py` admits a task-addressed `worktree_status_wait` request and delegates
to the bounded journal observer. The cursor is `meaningfulRevision`, not `recordRevision`: an
unchanged heartbeat must not manufacture progress. Timeout returns the unchanged snapshot;
generation/cursor mismatches return typed outcomes rather than searching for a nearby task.
The detached worker passes typed transaction inputs to the existing closeout/integration service;
direct landing remains a distinct route. Normal closeout/integration no longer selects or executes
repository certification or quality profiles as an automatic prerequisite. The terminal-envelope
telemetry helper is available, but does not by itself wire ordinary R16 telemetry production callers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The application adapter owns the public read-only wait request and outcome. | "class LifecycleStatusWaitRequest(BaseModel):"; "def worktree_status_wait_tool(" | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:66-109 |
| The observer validates the cursor, polls the exact generation, and returns change or timeout. | "def validate_wait_cursor(after_revision: int)"; "def wait_for_lifecycle_change(" | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:87-146 |

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## CCR-R12@v5 Current Transaction Boundary

The lifecycle application route starts and observes closeout/integration transactions with explicit
approval, candidate/source identity, leases, and ref safety. The detached worker delegates the
transaction to existing worktree owners without invoking strict code quality, memory quality,
selected certification, curator coherence, or independent review. Full suites are an explicit
developer request; retained model/profile fields do not change this normal worker boundary.


## Update History
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.

- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded route-review refusal promotion in the lifecycle certification adapter and preserved its no-mutation boundary. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-09-06T15:08:14+00:00 — Added the current selected-certification/refusal source routes and their precise fixture/model boundaries; corrected stale pending-candidate wording where present. Preserved broader prior verification stamps and all earlier history.

- 2026-09-05T07:05+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Qualified typed-failure precedence and documented configured profile propagation plus telemetry helper boundary. Current route claims were checked against the frozen candidate; this stamp records source verification, not execution or certification.


- 2026-09-05T06:12+00:00 — Combined typed terminal failure handling with bounded read-only wait routing and documented the meaningful-revision cursor.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds the `lifecycle_status_wait.py` read-only wait controller (CCR-R15 `worktree_status_wait`); route index regenerated.


- 2026-09-04T17:15+02:00 — 260831-CCR-L20 Gate-5 memory pass (code commit `ce7f10b5`):
  recorded CCR-R20 typed terminal rail-failure propagation on the detached worker boundary:
  `OperationRuntime.fail` routes unclassified outer failures through
  `terminal_rail_failure.py`, and the route's File-Level Onboarding Map gained the new module.
  Verification stamp is the full leaf code commit
  `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.


- 2026-08-30T06:26+02:00 — MCAR-L03 A005: documented the strict-by-default admission boundary
  and its narrow single-owner transfer of candidate identity to exact-pair validation.

- 2026-08-25T15:44+02:00 — Created for PDLS whole-system reconciliation and the public
  lifecycle-error translation boundary. Verification remains closeout-owned.
