# mcp/src/agents_remember/providers/context_modules/cgc/patches.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context_modules/cgc/patches.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/patches.py` owns CodeGraphContext upstream module discovery and marker-based patch application.

## Code Commentary

### Logic

It locates installed CGC modules inside Linux and Windows venv layouts and applies idempotent patches for `.cgcignore` handling, Windows delete-prefix cleanup, C++/TableGen discovery, and visualizer routing/query behavior.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup and lifecycle install paths call these patch helpers after CGC is installed. | [provider_setup.py; lifecycle_modules/cgc/installation.py](provider_setup.py; lifecycle_modules/cgc/installation.py) |

## Update History

- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
