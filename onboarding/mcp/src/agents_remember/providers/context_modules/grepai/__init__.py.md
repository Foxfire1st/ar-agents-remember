# mcp/src/agents_remember/providers/context_modules/grepai/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context_modules/grepai/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/__init__.py` is the Docker-owned GrepAI context provider subpackage facade.

## Code Commentary

### Logic

It re-exports GrepAI constants, layout, workspace-config, sync, and artifact helpers from the focused GrepAI context modules for the public `providers.context` facade.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public context facade imports GrepAI exports through this subpackage facade. | [context.py](../../context.py.md) |

## Update History

- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split from `core.py` into `constants.py`, `layout.py`, `workspace.py`, and `artifacts.py`.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
