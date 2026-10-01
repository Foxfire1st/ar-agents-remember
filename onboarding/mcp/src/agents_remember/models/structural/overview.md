# Structural Wire Models Overview

| Field | Value |
|---|---|
| sourceRoute | `mcp/src/agents_remember/models/structural/` |
| onboardingRoute | `mcp/src/agents_remember/models/structural/overview.md` |
| parentOverview | [`models/overview.md`](../overview.md) |

## What This Area Is

This package is the strict structural vocabulary. Agent requests express a child task document,
role, label, message, reason, or decision; public responses return structural task and role
outcomes. It also owns the internal durable activation record for atomic-series work, and that record
is now keyed by the canonical series contract — not by a normalized protected source pair — so two
atomic masters that share one sprint's code and memory branches hold independent records. The record
binds canonical `TaskDocumentRef` identity and the canonical contract path without becoming a public
runtime address. Internal exact-id gate responses remain separate so control-plane correlation does
not leak into model cognition.

## Hot Path Summary

Read `agent.py` for dispatch/message/retire/rename schemas, `gates.py` for structural delegated
gate schemas plus the deliberately separate internal response family, and
`atomic_series_activation.py` for the closed selector/archive vocabulary.

## What Belongs Here

| Path | Role |
|---|---|
| `agent.py` | Agent-facing structural operation DTOs |
| `atomic_series_activation.py` | Internal per-contract activation selector and corrupt-entry archive records |
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
| `atomic_series_activation.py` | internal structural record | Separates the selected master and canonical contract identity from queue and lifecycle evidence | covered |
| `gates.py` | public/internal split | Prevents gate/lifecycle ids leaking to agents | covered |

## Local Invariants And Traps

- Adding a public runtime-id field is an architectural regression, not a convenience.
- Internal response models may carry correlation ids only when they are never registered as agent tools.
- No compatibility alias may restore the removed exact-id agent API.
- The activation record is keyed by the canonical series contract, never by a protected source pair or
  a repository/branch identity: two atomic masters that share one pair keep independent records, and a
  snapshot that is not the addressed contract is refused rather than adopted.

## Evidence

### Repo-Internal References

- Current dispatch caller resolution owns the structural boundary; removed doctrine/relationship tests provide no current execution evidence. [1]
- The route's activation vocabulary is contract-scoped: the record carries the contract fingerprint, the canonical contract path, the selected master, the writable selection state, a monotonic revision, and selection time. [2]
- The store derives the fingerprint from the canonical resolved contract path and refuses any record that is not this exact contract. [3]

### Cross-Repo References


### Docs References

The resolved source registry contains no Domain Documentation entry.


## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `models/structural/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Package marker |
| `models/structural/agent.py` | [`agent.py.md`](agent.py.md) | covered | Agent structural schemas |
| `models/structural/atomic_series_activation.py` | [`atomic_series_activation.py.md`](atomic_series_activation.py.md) | covered | Contract-scoped selector/archive vocabulary |
| `models/structural/gates.py` | [`gates.py.md`](gates.py.md) | covered | Structural gate schemas and relocated gate model knowledge |

## Child Overviews

No child overview is needed.

## How To Use This Area

Read this overview and the exact file card before modifying public structural or activation
identity vocabulary.

## Needs Verification

- Commit-derived verification metadata awaits governed closeout; the activation-model path,
  contract-scoped vocabulary, and citations are reconciled to the frozen candidate.
