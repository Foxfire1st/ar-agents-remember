# mcp/src/agents_remember/mcp/__main__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/__main__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:47:44+00:00 |
| lastVerifiedCommitHash | `d445e83e7d28e3c34b15d8299d279d65ab9183b9` |
| lastVerifiedCommitDate | 2026-05-23T05:45:38+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[Governing route overview](../../../overview.md)

## Purpose

Provides the Python module entrypoint for the MCP server.

## Code Commentary

### Logic

Imports main from the sibling server module. Direct module execution calls main and raises SystemExit with its return value.

### Conventions

Argument parsing and server composition belong to the imported main function.

### Invariants And Boundaries

The call to main is guarded by the __main__ name check.

### Todos

None recorded.

## Docs References

No domain documentation is configured. This card describes repository source only.

## Repo-Internal References

These constructs establish the behavior described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Guarded delegation to the server entrypoint | `main`; `SystemExit`; "__main__" | mcp/src/agents_remember/mcp/__main__.py:1-8 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

## Update History

- 2026-09-05T06:47:44+00:00 — Created during L31 full-population memory recovery from frozen ea359649; verification records the actual source-touching commit. Documentation evidence only.
