# mcp/src/agents_remember/providers/context/common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context/common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`common.py` contains shared provider context helpers that are not specific to CGC or GrepAI.

## Code Commentary

### Logic

It defines `ContextProviderError` (subclass of `AgentsRememberError`), template expansion, copied requirements-file helpers, provider pin parsing, generic provider state JSON writing, file hashing, and guarded runtime-path removal. `stable_provider_id` is no longer defined here; it is re-exported from `agents_remember.providers.identity` (its canonical source) so the `providers.context` facade still exposes the name.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC and GrepAI context modules import shared error, path, pin, and removal helpers from here. | [CGC core](../cgc/context/core.py.md); [GrepAI core](../grepai/context/core.py.md) |

## Update History

- 2026-05-31T12:30+02:00 — `stable_provider_id` now re-exported from `providers.identity` (canonical source moved) and `ContextProviderError` rebased on `AgentsRememberError` (1.0.0 review remediation).
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
