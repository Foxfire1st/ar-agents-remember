# mcp/src/agents_remember/providers/context_modules/cgc/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context_modules/cgc/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/core.py` owns CodeGraphContext runtime layout derivation, provider-owned config writing, source artifact detection, and stale runtime cleanup.

## Code Commentary

### Logic

It defines `CgcRuntimeLayout`, builds layouts from direct parameters or provider settings, derives FalkorDB host/port from provider settings plus backend state, writes managed `.cgcignore`, config, and `.env` files, detects source-tree CGC artifacts, and removes only generated or obsolete provider runtime artifacts inside validated provider roots.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Lifecycle CGC modules use these layout and cleanup helpers before running or installing CGC. | [lifecycle_modules/cgc/core.py; lifecycle_modules/cgc/installation.py; lifecycle_modules/cgc/process.py](lifecycle_modules/cgc/core.py; lifecycle_modules/cgc/installation.py; lifecycle_modules/cgc/process.py) |

## Update History

- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
