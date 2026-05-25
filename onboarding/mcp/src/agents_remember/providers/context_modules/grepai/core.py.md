# mcp/src/agents_remember/providers/context_modules/grepai/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context_modules/grepai/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/core.py` is a compatibility-free package-local facade for the focused Docker-owned GrepAI context modules.

## Code Commentary

### Logic

It imports public names from `artifacts.py`, `constants.py`, `layout.py`, and `workspace.py`. It keeps `grepai.core` as a local organization point inside the new subpackage, while the public API remains `providers.context`.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI layout and constants now live in focused sibling modules. | [layout.py](layout.py.md); [constants.py](constants.py.md) |
| GrepAI lifecycle modules consume these exports through `providers.context`. | [lifecycle_modules/grepai/core.py](../../lifecycle_modules/grepai/core.py.md) |

## Update History

- 2026-05-25T19:33+02:00: Reduced to a facade after GrepAI context responsibilities were split into constants, layout, workspace, and artifact modules.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
