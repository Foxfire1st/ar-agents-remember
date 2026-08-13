# mcp/src/agents_remember/application/runtime/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/runtime/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T08:40+02:00 |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[runtime overview](overview.md)

## Purpose

Marks the cohesive application package for runtime startup, installation, and skill deployment.

## Code Commentary

The initializer carries only the package docstring. Public operations remain defined in
`install.py`, `startup.py`, and `skills.py`; adding re-exports here would create a second facade and
blur the direct domain imports used by MCP registration and payload builders.

## Invariants And Boundaries

- Keep this initializer declarative and free of process startup or installation side effects.
- Import the focused runtime module that owns an operation rather than routing through this file.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring names the three owned runtime concerns. | "Application operations for runtime startup, installation, and skill deployment." | mcp/src/agents_remember/application/runtime/__init__.py:1-1 |

## Cross-Repo References

No cross-repository implementation dependency governs this package marker.

## Update History

- 2026-08-13T08:40+02:00 — Created for the L23 integration-gate repair's cohesive runtime application package. Verification metadata remains closeout-owned.
