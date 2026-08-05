# mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `45214435fd2de65765a8230ceb1dcfe188d1944d` |
| lastVerifiedCommitDate | 2026-05-27T00:09:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`__init__.py` is the Docker-owned GrepAI lifecycle export facade. It groups the
split GrepAI implementation modules behind one import surface for
`providers.lifecycle`.

## Code Commentary

### Logic

The lazy GrepAI lifecycle facade searches core, compose, backend, embedder, runner,
and actions in that order and keeps the provider Docker-owned.

### Invariants And Boundaries

- Keep this module import-only.
- GrepAI remains Docker-or-bust; implementation modules must not add host binary
  or host Ollama fallbacks.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parent lifecycle facade lists the GrepAI lifecycle package among its lazy exports. | `grepai` | mcp/src/agents_remember/providers/lifecycle/__init__.py:12-12 |
| The lazy GrepAI facade searches core, compose, backend, embedder, runner, and actions in order, imports a matching module, caches the symbol, and raises if none exists. | `_EXPORT_MODULES`; `__getattr__` | mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py:8-15; mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py:18-25 |

## Update History

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: corrected the lifecycle facade name and captured the ordered lazy-import/cache/error behavior plus current compose export.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created as the Docker-owned GrepAI lifecycle export facade.
