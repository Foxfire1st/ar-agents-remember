# mcp/src/agents_remember/mcp/tools/structural_agent.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/structural_agent.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Adapts strict structural request DTOs to application services for dispatch, parent/child messaging,
retirement, and rename. It replaces the removed public leaf/exact-id addressing adapter.

## Code Commentary

### Logic

Each payload function builds one structural runtime, receives its operation-specific typed request,
invokes the corresponding application tool, and validates an operation-specific structural response.

### Conventions

This module is intentionally thin; authorization and lifecycle behavior stay in the application
and serving layers.

### Invariants And Boundaries

- Do not accept runtime ids through `overrides` or request fields.
- Do not restore the deleted leaf-ref compatibility tool.
- Keep one payload adapter per public operation for registry introspection.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Six payload adapters expose the structural agent operation family. | `dispatch_agent_payload` | mcp/src/agents_remember/mcp/tools/structural_agent.py:31-114 |
| The application service owns authorization and mutation. | `dispatch_agent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:279-542 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created; supersedes the true-deleted `mcp/tools/leaf_ref.py` public adapter without a compatibility path.
