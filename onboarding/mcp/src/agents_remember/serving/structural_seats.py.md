# mcp/src/agents_remember/serving/structural_seats.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/structural_seats.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Qualifies current structural seats from canonical task-document containment and role. It is the one
resolver used by structural operations and replacement-aware routing.

## Code Commentary

### Logic

`StructuralSeatResolver` reads task topology and catalog bindings, enforces the role's natural
altitude, derives authorized parents/children, and selects exactly one live occupant. Missing,
ambiguous, wrong-level, and out-of-scope cases become typed `StructuralSeatError`s.

### Conventions

The resolver uses structural task references for identity and runtime ids only as internal catalog
occupant/provenance evidence.

### Invariants And Boundaries

- Exactly one live occupant may satisfy a singular document+role seat.
- Parent and child lookup never escapes the containing sprint/master.
- Spawn ancestry is neither public identity nor a fallback resolver here; topology plus role
  establishes the authorized relation.
- No first-running-role or workspace-global fallback exists.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolver and error family centralize structural qualification. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:14-160 |
| Task containment resolves real sprint/master/leaf documents. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:35-252 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created; absorbs qualified binding behavior formerly split across leaf validation and sprint-role binding helpers.
