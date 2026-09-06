# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T15:08:14+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
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
The detached worker reads the configured repository certification profile and passes it to
the existing closeout/integration service; direct landing remains a distinct route. The
terminal-envelope telemetry helper is available, but does not by itself wire ordinary
R16 telemetry production callers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The application adapter owns the public read-only wait request and outcome. | "class LifecycleStatusWaitRequest(BaseModel):"; "def worktree_status_wait_tool(" | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:66-109 |
| The observer validates the cursor, polls the exact generation, and returns change or timeout. | "def validate_wait_cursor(after_revision: int)"; "def wait_for_lifecycle_change(" | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:87-146 |

## Update History

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
