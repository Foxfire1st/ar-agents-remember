# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-11T10:26:37+02:00 |
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2` |
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Application overview](../overview.md)

## What This Area Is

Public application adapters for admitting configured contracts, locating and controlling durable
lifecycle operations, and exposing the direct-landing route. These modules translate configuration
and caller context into typed worktree-domain requests; they do not own journal transition policy.

## Hot Path Summary

Use `configured_contract_admission.py` for the one total mutation-admission boundary, `direct_landing.py` for the public direct route, and `terminal_rail_failure.py` for typed terminal-failure projection. Journal transition policy remains in the worktree lifecycle domain. The detached lifecycle worker (`lifecycle_operation_worker.py`), the public read-only wait adapter (`lifecycle_status_wait.py`), and the legacy-bridge and enclosure tool entry points (`legacy_operation_tool.py`, `lifecycle_enclosure_tools.py`) were all deleted with the door/operation plane; closeout and integration now run on the in-process synchronous route and the route owns no detached execution surface.

## Complete Admission Refusals

[`certification_refusal.py`](certification_refusal.py.md) renders all typed admission findings, including nested byte evidence, for public adapters. Its zero-start refusal shape reports the admission boundary; the renderer itself does not observe processes or alter journal state.

CCR-R25 also promotes a typed `routeReview` finding through the shared route-review refusal
projection, preserving the complete certification finding list while adding exact status and
contract-bound next-step guidance when a contract is available. The lifecycle adapter remains a
projection boundary; it does not record a review or mutate task state.

## Operating Model

Application tools admit configured contracts, resolve durable operation locations, invoke the
worktree lifecycle owners, and project typed refusals. `terminal_rail_failure.py` still supplies the
typed rail-failure envelope for otherwise-unclassified failures (retained organizational repair and
ledger-recovery decisions take precedence). Configured-contract admission remains strict by default.
Exact code-memory pair consumers may delegate only candidate-worktree identity to the canonical pair
validator; repository, task, and enclosure authority remain at the application boundary.

The former `OperationRuntime`/detached-worker path is gone: `lifecycle_operation_worker.py` was
deleted by commit `173bb01e` ("delete the detached lifecycle worker and drive every fixture on the
synchronous path"), and the MCP tools now drive `worktree_closeout_apply` and `worktree_integrate`
in-process. There is no worker lease, worker composition root, or detached terminal publication on
this route.

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
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `certification_refusal.py` | [certification_refusal.py.md](certification_refusal.py.md) | covered |
| `configured_contract_admission.py` | [configured_contract_admission.py.md](configured_contract_admission.py.md) | covered |
| `direct_landing.py` | [direct_landing.py.md](direct_landing.py.md) | covered |
| `lifecycle_control_authority.py` | [lifecycle_control_authority.py.md](lifecycle_control_authority.py.md) | covered |
| `lifecycle_operation_location.py` | [lifecycle_operation_location.py.md](lifecycle_operation_location.py.md) | covered |
| `lifecycle_tools.py` | [lifecycle_tools.py.md](lifecycle_tools.py.md) | covered |
| `terminal_rail_failure.py` | [terminal_rail_failure.py.md](terminal_rail_failure.py.md) | covered |

## Docs And Boundary References

No Domain Documentation or cross-repository source is configured for this route. Same-repository
authority is documented by the linked source sidecars and the worktrees integration overview.

## Read-Only Status Change Wait — public wait surface removed

The task-addressed `worktree_status_wait` tool and its application adapter
(`lifecycle_status_wait.py`) were deleted with the door/operation plane by commit `41b0812e`
("delete the two detached operation-plane entry points and their stale tool surface"); the tool is
no longer registered. The bounded read-only observer below survives and remains the only wait
implementation on the route, but it is currently unreachable from the public tool surface.
Direct landing remains a distinct route. Normal closeout/integration does not select or execute
repository certification or quality profiles as an automatic prerequisite.

| Finding | Anchor | Source |
| --- | --- | --- |
| The bounded read-only observer validates the cursor, polls the exact generation, and returns change or timeout. | "def validate_wait_cursor(after_revision: int)"; "def wait_for_lifecycle_change(" | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:87-146 |

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## CCR-R12@v5 Current Transaction Boundary

The lifecycle application route starts and observes closeout/integration transactions with explicit
approval, candidate/source identity, and ref safety. The transaction runs in-process through the
public `worktree_closeout_apply` and `worktree_integrate` tools and does not invoke strict code
quality, memory quality, selected certification, curator coherence, or independent review. Full
suites are an explicit developer request. The detached worker and its lease, described in earlier
revisions of this section, no longer exist.


## Update History
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: removed the four cards whose source files the cut deleted (`lifecycle_operation_worker.py` by `173bb01e`; `lifecycle_status_wait.py` and `lifecycle_enclosure_tools.py` by `41b0812e`; `legacy_operation_tool.py` by `a583beb8`) and dropped their stale links from the File-Level Onboarding Map. The map now lists every surviving card on the route. Recorded that the detached worker, its lease, and the public read-only wait tool are gone while the bounded observer at `worktrees/integration/lifecycle/observation/status_wait.py` survives unreachable. This records source documentation only; it makes no acceptance or certification claim.
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
