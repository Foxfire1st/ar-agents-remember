# mcp/src/agents_remember/models/lifecycles/ — Lifecycle Models

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/lifecycles/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-13T08:40+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Hot Path Summary

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
| Asynchronous operation records keep private identity out of the public projection. | `LifecycleOperationRecord`; `LifecycleOperationProjection` | mcp/src/agents_remember/models/lifecycles/operation.py:243-283; mcp/src/agents_remember/models/lifecycles/operation.py:347-362 |

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

## Update History

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added organizational-completion wire models to the lifecycles route; the route purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final candidate review: the validated operation record carries
  exact candidate and recovery-commit evidence used by monotonic restart reconciliation; no private
  operation identity entered agent-facing projections. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — Created for the L23 move that groups lifecycle response, finalizer, and asynchronous-operation models under one cohesive route. Verification metadata remains closeout-owned.
