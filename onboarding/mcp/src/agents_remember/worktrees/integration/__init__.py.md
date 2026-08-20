# mcp/src/agents_remember/worktrees/integration/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/integration route overview](overview.md)

## Purpose

Package marker for the integration-branch authority and ref-transaction modules (260815-DAG master
full-gate repair): a one-line docstring only — the package has no re-export surface.

## Code Commentary

The module is a single docstring (`"""Integration-branch authority and ref-transaction
modules."""`); the package's modules are imported by their full paths
(`agents_remember.worktrees.integration.integration_branch_authority`, etc.), not re-exported here.

### Invariants And Boundaries

- No `__all__` and no re-exports: importers name the module explicitly.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package marker docstring. | "Integration-branch authority and ref-transaction modules." | mcp/src/agents_remember/worktrees/integration/__init__.py:1-1 |

## Cross-Repo References

No cross-repo boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-21T00:45+02:00 — Created for 260815-DAG master full-gate repair: the
  `worktrees/integration` package marker. Verified at code commit e5cb139f.
