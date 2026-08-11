# Structural Wire Models Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/models/structural/` |
| onboardingRoute | `mcp/src/agents_remember/models/structural/overview.md` |
| parentOverview | [`models/overview.md`](../overview.md) |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|

## What This Area Is

This package is the strict public structural wire vocabulary. Agent requests express a child task
document, role, label, message, reason, or decision; public responses return structural task and
role outcomes. Internal exact-id gate responses remain separate so control-plane correlation does
not leak into model cognition.

## Hot Path Summary

Read `agent.py` for dispatch/message/retire/rename schemas and `gates.py` for structural delegated
gate schemas plus the deliberately separate internal response family.

## What Belongs Here

| Path | Role |
|---|---|
| `agent.py` | Agent-facing structural operation DTOs |
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
| `models/structural/gates.py` | [`gates.py.md`](gates.py.md) | covered | Structural gate schemas and relocated gate model knowledge |

## Child Overviews

No child overview is needed.

## How To Use This Area

Read this overview and both file cards before modifying public structural wire vocabulary.

## Needs Verification

None.

## Update History

- 2026-08-11T14:29+02:00 — Re-read the agent-doctrine boundary test and widened its citation to
  include the parametrized declaration; verification metadata remains pending for governed closeout.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the public structural model package; absorbed the relevant `models/gates.py` card during its behavior relocation.
