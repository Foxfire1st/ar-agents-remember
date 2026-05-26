# mcp/src/agents_remember/providers/grepai/context/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/constants.py` centralizes Docker-owned GrepAI provider identifiers, pins, image/container names, default loopback ports, and root artifact names.

## Code Commentary

### Logic

The module is constant-only: it declares the GrepAI package pin, Docker network, runner/Postgres/Ollama container names, default host ports, image references, and disposable root artifact names used by the context and lifecycle GrepAI modules.

### Invariants And Boundaries

- GrepAI is Docker-owned; these constants do not point to a host `_bin` or `_venv` install path.
- `.grepai` is treated as provider runtime/cache state and must not remain in indexed roots.
- This file is imported through `providers.context`; there is no `context_providers.py` compatibility fallback.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI layout and artifact modules consume these constants for provider-owned runtime paths and root cleanup. | [layout.py](layout.py.md); [artifacts.py](artifacts.py.md) |
| GrepAI lifecycle modules consume Docker container/image constants through `providers.context`. | [core.py](../lifecycle/core.py.md) |

## Update History

- 2026-05-25T19:33+02:00: Created when GrepAI context constants were split out of `grepai/core.py`.
