# mcp/src/agents_remember/models/structural/__init__.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Marks the strict structural model package without re-exporting legacy exact-id schemas.

## Code Commentary

### Logic

Package marker only.

### Conventions

Import the concrete model module that owns the wire family.

### Invariants And Boundaries

Do not add compatibility exports for removed public exact-id models.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public agent and gate models live in explicit sibling modules. | `DispatchAgentRequest` | mcp/src/agents_remember/models/structural/agent.py:1-107; mcp/src/agents_remember/models/structural/gates.py:1-165 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created with the strict structural model package.
