# mcp/src/agents_remember/models/structural/__init__.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `f05ba167cd6dfb56b48a775f3da5d45528c09c82`|
| lastVerifiedCommitDate |  2026-09-18T17:19:31+02:00|
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
| Public agent and gate models live in explicit sibling modules. | `DispatchAgentRequest` | mcp/src/agents_remember/models/structural/agent.py:1-117; mcp/src/agents_remember/models/structural/gates.py:1-165 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created with the strict structural model package.
