# Structural Application Services Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/application/structural/` |
| onboardingRoute | `mcp/src/agents_remember/application/structural/overview.md` |
| parentOverview | [`application/overview.md`](../overview.md) |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash |  `b523f53b193e9783e7c7e6410c772e7d64d8df17`|
| lastVerifiedCommitDate |  2026-08-19T21:54:50+02:00|

## What This Area Is

The structural application boundary translates an ambient hosted seat's intent into authorized
document-and-role operations. It owns dispatch, parent/child messaging, retirement, rename, and
delegated gate operations without accepting runtime session, lifecycle, inbox, or gate identifiers
from an agent.

## Hot Path Summary

`agent_tools.py` resolves the caller and target structural seats before invoking the existing
plane-owned spawn, inbox, retire, and rename machinery. `gate_tools.py` applies the same boundary to
delegated gates. Public response models expose task-document and role outcomes only.

For L23, dispatch additionally validates transitive task-derived code and external-memory lineage
before host creation. Curator dispatch requires the manager's current-lineage preflight and a
passing independent route-review record bound to the exact candidate tree; the structural boundary
rechecks both rather than trusting brief prose or model-carried commit identities.

## What Belongs Here

| Path | Role |
|---|---|
| `agent_tools.py` | Structural dispatch, messaging, retirement, and rename orchestration |
| `gate_tools.py` | Structural lifecycle-gate creation, decision, and listing |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
|---|---|
| Catalog qualification and hierarchy walking | `serving/structural_seats.py` |
| Ambient caller resolution | `serving/ambient_seat.py` |
| Strict agent-facing request/response schemas | `models/structural/` |
| Runtime-id administration | Internal serving/control-plane surfaces, never public structural tools |

## Operating Model

1. Resolve the caller from trusted hosted-process context.
2. Authorize the requested parent or child relationship from canonical task containment and role.
3. Resolve exactly one current target occupant or return a typed structural failure.
4. Invoke the existing plane-owned mutation using runtime ids internally.
5. Return only structural work-domain identity to the model.

## Main Flows

### Dispatch

1. Validate the requested child role and contained task document.
2. Spawn and bind the child occupant.
3. Persist an internally exact-pinned initial dispatch brief.
4. Retire an unbriefed child if that transaction fails.

### Ordinary relationship traffic

1. Persist a document-and-role structural address.
2. Re-resolve its current occupant immediately before delivery.
3. Preserve the same address across parent or child replacement.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `agent_tools.py` | application boundary | Prevents model-supplied runtime addressing | covered |
| `gate_tools.py` | authorization boundary | Prevents exact lifecycle/gate targeting by agents | covered |

## Local Invariants And Traps

- No public structural request or response carries a runtime id.
- Initial dispatch remains exact-pinned internally; ordinary relationship traffic remains rebindable.
- Missing or ambiguous seats fail closed; no same-role global fallback is permitted.
- This package composes existing primitives and must not create a second lifecycle implementation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public structural operations are registered through one adapter module. | `dispatch_agent_payload` | mcp/src/agents_remember/mcp/tools/structural_agent.py:31-114 |
| Structural resolution qualifies document+role seats and refuses ambiguity. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:14-160 |

## Cross-Repo References

No cross-repository runtime dependency governs this package.


## Docs References

The resolved memory source registry has no configured Domain Documentation entry. The implementation
contract is therefore evidenced by repository source, tests, and the approved task design.


## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `application/structural/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Package marker |
| `application/structural/agent_tools.py` | [`agent_tools.py.md`](agent_tools.py.md) | covered | Agent structural boundary |
| `application/structural/gate_tools.py` | [`gate_tools.py.md`](gate_tools.py.md) | covered | Gate structural boundary |

## Child Overviews

No child overview is needed for this bounded package.

## How To Use This Area

Read this overview, the target file card, `serving/structural_seats.py.md`, and the strict model
card before changing a structural operation.

## Needs Verification

None.

## 260815-DAG-L4 L4 Organizational And Atomic Dispatch

Structural dispatch distinguishes organizational masters, whose leaves start directly from the sprint super, from atomic masters, whose task-owned series refs are journaled before child admission. Dispatch never creates a universal master branch for organizational work.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: manager series bootstrap in
  `agent_tools.py` gates on the effective execution nature (nature-less masters default atomic;
  organizational semantics only under an authored graph) and surfaces an atomic-sequential
  lane-blocked bootstrap as a failed `StructuralOutcome` carrying the ordering payload; the
  structural-route model is unchanged. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-14T06:20+02:00 — L23 curator: documented pre-host lineage and candidate-bound route-review
  admission for curator dispatch. Verification provenance remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the new structural application package.
