# pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `pyproject.toml`                           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T12:28+02:00                     |
| lastVerifiedCommitHash | `11f28a2035f06f8bc33f11b0617b41cda1122c1f` |
| lastVerifiedCommitDate | 2026-06-06T13:01:33+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Root `pyproject.toml` holds source-checkout quality-tool configuration shared
by the MCP package source and tests.

## Code Commentary

The file configures Ruff linting, Radon reporting thresholds, and Pyright. The
Pyright configuration includes `mcp/src/agents_remember` and `mcp/tests`, uses
Python 3.11, points at the repo-local `.venv`, and sets execution environments
so tests can import package code through `mcp/src`.

## Invariants And Boundaries

- Root quality-tool config governs source-checkout development checks; install
  package metadata stays in `mcp/pyproject.toml`.
- Pyright should remain wired to the existing source and test roots rather than
  being scoped down to only files touched in one task.
- Ruff owns style/import/static hygiene; Radon reports complexity and
  maintainability pressure.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The source quality wrapper invokes Pyright through this project configuration. | [check.py](agents-remember-md/mcp/src/agents_remember/code_quality/check.py) |
| Source-checkout instructions tell agents to run Ruff, Pyright, and Radon after Python changes. | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Update History

- 2026-06-06T12:28+02:00: Re-verified against current HEAD after the Pyright configuration landed; the existing Ruff, Pyright, and Radon commentary still matches.
- 2026-05-28T19:52+02:00: Created after Pyright was added to source-checkout quality configuration.
