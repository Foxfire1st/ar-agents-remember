# mcp/src/agents_remember/application/structural/gate_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/gate_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural application services](overview.md)

## Purpose

Provides lifecycle-gate creation, decision, and list operations addressed by structural seat
relationships instead of caller-supplied lifecycle or gate ids.

## Code Commentary

### Logic

The runtime resolves the ambient caller, qualifies the target seat, authorizes the relationship,
and then invokes internal gate tools. `_raise_payload` normalizes internal result models into
serializable payloads; the public response construction removes plane-only correlation ids.

### Conventions

Public gate responses use task-document and role identity. Internal response models remain confined
to the plane-facing call seam.

### Invariants And Boundaries

- Agents do not select lifecycle or gate records by id.
- A caller cannot decide a gate outside its authorized structural relation.
- List results redact plane-only correlation fields.

### Todos

None.

## Docs References

No Domain Documentation source is configured.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle-gate creation resolves a structural target before invoking internal gate creation. | `structural_lifecycle_gate_tool` | mcp/src/agents_remember/application/structural/gate_tools.py:77-109 |
| Gate decisions and listing authorize through the same ambient structural context. | `structural_gate_decide_tool` | mcp/src/agents_remember/application/structural/gate_tools.py:111-236 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural delegated-gate operations.
