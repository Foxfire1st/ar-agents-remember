# mcp/src/agents_remember/providers/context_modules/cgc/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context_modules/cgc/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/constants.py` owns CGC provider identifiers, pins, backend defaults, source artifact names, env exclusion keys, default `.cgcignore` text, and upstream patch snippets.

## Code Commentary

### Logic

CGC runtime and patch modules import this file for stable names and marker text. It also reads source `.gitignore` patterns for managed `.cgcignore` generation.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC runtime layout uses provider constants and default ignore text from this module. | [context_modules/cgc/core.py](context_modules/cgc/core.py) |
| CGC patch application uses marker and snippet constants from this module. | [context_modules/cgc/patches.py](context_modules/cgc/patches.py) |

## Update History

- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
