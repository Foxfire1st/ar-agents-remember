# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |

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

## Evidence

### Docs And Boundary References

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

- The bounded read-only observer validates the cursor, polls the exact generation, and returns change or timeout. [1]

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## CCR-R12@v5 Current Transaction Boundary

The lifecycle application route starts and observes closeout/integration transactions with explicit
approval, candidate/source identity, and ref safety. The transaction runs in-process through the
public `worktree_closeout_apply` and `worktree_integrate` tools and does not invoke strict code
quality, memory quality, selected certification, curator coherence, or independent review. Full
suites are an explicit developer request. The detached worker and its lease, described in earlier
revisions of this section, no longer exist.
