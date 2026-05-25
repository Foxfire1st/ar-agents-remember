# mcp/src/agents_remember/providers/lifecycle_modules/grepai/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/grepai/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`grepai.py` is the Docker-owned GrepAI lifecycle export facade. It groups the
split GrepAI implementation modules behind one import surface for
`providers.lifecycle`.

## Code Commentary

### Logic

The module re-exports GrepAI action dispatch, shared GrepAI settings helpers,
PostgreSQL backend lifecycle, Ollama embedder lifecycle, and runner
image/container lifecycle.

### Invariants And Boundaries

- Keep this module import-only.
- GrepAI remains Docker-or-bust; implementation modules must not add host binary
  or host Ollama fallbacks.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports this GrepAI facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| GrepAI core, backend, embedder, runner, and action modules make up the exported surface. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/core.py); [backend.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/backend.py); [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/embedder.py); [runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/runner.py); [actions.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/actions.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created as the Docker-owned GrepAI lifecycle export facade.
