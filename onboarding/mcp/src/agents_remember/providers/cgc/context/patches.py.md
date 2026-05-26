# mcp/src/agents_remember/providers/cgc/context/patches.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/patches.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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
| Provider setup and lifecycle install paths call these patch helpers after CGC is installed. | [provider_setup.py](../../provider_setup.py.md); [installation.py](../lifecycle/installation.py.md) |

## Update History

- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
