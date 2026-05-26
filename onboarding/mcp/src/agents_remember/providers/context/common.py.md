# mcp/src/agents_remember/providers/context/common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context/common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`common.py` contains shared provider context helpers that are not specific to CGC or GrepAI.

## Code Commentary

### Logic

It defines `ContextProviderError`, stable provider-id normalization, template expansion, copied requirements-file helpers, provider pin parsing, generic provider state JSON writing, file hashing, and guarded runtime-path removal.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC and GrepAI context modules import shared error, path, pin, and removal helpers from here. | [CGC core](../cgc/context/core.py.md); [GrepAI core](../grepai/context/core.py.md) |

## Update History

- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
