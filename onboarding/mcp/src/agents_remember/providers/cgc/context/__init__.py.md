# mcp/src/agents_remember/providers/cgc/context/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/__init__.py` is the CGC context provider subpackage facade.

## Code Commentary

### Logic

It re-exports CGC constants, runtime-layout helpers, cleanup helpers, module discovery helpers, and patch applicators so `providers.context` can keep the old public symbol surface without a monolithic implementation file.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public context facade imports CGC exports through this subpackage facade. | [context facade](../../context/__init__.py.md) |

## Update History

- 2026-05-29T18:35+02:00: Added `materialize` and `cleanup` to the package star-imports after `core.py` was split; behavior-preserving (commit `01f503d`).
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
