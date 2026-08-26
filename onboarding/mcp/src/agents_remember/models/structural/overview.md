# Structural Wire Models Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/models/structural/` |
| onboardingRoute | `mcp/src/agents_remember/models/structural/overview.md` |
| parentOverview | [`models/overview.md`](../overview.md) |
| lastUpdated | 2026-08-26T08:55+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|

## What This Area Is

This package is the strict structural vocabulary. Agent requests express a child task document,
role, label, message, reason, or decision; public responses return structural task and role
outcomes. It also owns the internal durable source-pair activation record because that record binds
canonical `TaskDocumentRef` identity to a selected contract and source pair without becoming a
public runtime address. Internal exact-id gate responses remain separate so control-plane
correlation does not leak into model cognition.

## Hot Path Summary

Read `agent.py` for dispatch/message/retire/rename schemas, `gates.py` for structural delegated
gate schemas plus the deliberately separate internal response family, and
`atomic_series_activation.py` for the closed selector/archive vocabulary.

## What Belongs Here

| Path | Role |
|---|---|
| `agent.py` | Agent-facing structural operation DTOs |
| `atomic_series_activation.py` | Internal source-pair selector and corrupt-entry archive records |
| `gates.py` | Agent-facing structural gate DTOs and isolated internal gate DTOs |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
|---|---|
| Catalog/runtime correlation models | Existing control-plane and terminal model modules |
| Address resolution behavior | `serving/structural_seats.py` and `application/structural/` |

## Operating Model

The public dataclasses and response models contain only structural work-domain fields. Registration
adapters and wire-contract tests guard that surface; application services turn those stable requests
into plane-internal exact operations.

## Main Flows

### Public operation decode

1. Parse only work-domain fields.
2. Keep session/lifecycle/inbox/gate address fields absent from the registered wire surface.
3. Resolve runtime identity behind the boundary.
4. Serialize a structural response without internal identifiers.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `agent.py` | public schema | Pins the runtime-id ban for agent operations | covered |
| `atomic_series_activation.py` | internal structural record | Separates selected master/source identity from queue and lifecycle evidence | covered |
| `gates.py` | public/internal split | Prevents gate/lifecycle ids leaking to agents | covered |

## Local Invariants And Traps

- Adding a public runtime-id field is an architectural regression, not a convenience.
- Internal response models may carry correlation ids only when they are never registered as agent tools.
- No compatibility alias may restore the removed exact-id agent API.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Machine doctrine tests scan public instructions for forbidden control-plane address cognition. | `test_agent_doctrine_contains_no_control_plane_address_instructions` | mcp/tests/test_agent_doctrine_plane_identity.py:41-50 |
| Structural tool tests reject ambiguity and exercise relationship operations. | `StructuralAgentToolTests` | mcp/tests/test_structural_agent_tools.py:134-241 |

## Cross-Repo References


## Docs References

The resolved source registry contains no Domain Documentation entry.


## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `models/structural/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Package marker |
| `models/structural/agent.py` | [`agent.py.md`](agent.py.md) | covered | Agent structural schemas |
| `models/structural/atomic_series_activation.py` | [`atomic_series_activation.py.md`](atomic_series_activation.py.md) | covered | Source-pair selector/archive vocabulary |
| `models/structural/gates.py` | [`gates.py.md`](gates.py.md) | covered | Structural gate schemas and relocated gate model knowledge |

## Child Overviews

No child overview is needed.

## How To Use This Area

Read this overview and the exact file card before modifying public structural or activation
identity vocabulary.

## Needs Verification

- Commit-derived verification metadata awaits governed closeout; the activation-model path,
  vocabulary, and citations are reconciled to the frozen candidate.

## Update History

- 2026-08-26T08:55+02:00 — Promoted the activation model from provisional to frozen covered
  status after pass 13.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the structural activation model route;
  verification metadata remains closeout-owned.

- 2026-08-26T06:05+02:00 — Added the moved atomic-series activation model as the route's internal
  structural selector vocabulary; no compatibility model remains at the old flat path.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: structural gate requests gain an optional
  `caller` (`DeclaredCaller`) used only when no plane seat exists; public response models are
  unchanged. Verified at code commit a9d50e08.


- 2026-08-11T14:29+02:00 — Re-read the agent-doctrine boundary test and widened its citation to
  include the parametrized declaration; verification metadata remains pending for governed closeout.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the public structural model package; absorbed the relevant `models/gates.py` card during its behavior relocation.
