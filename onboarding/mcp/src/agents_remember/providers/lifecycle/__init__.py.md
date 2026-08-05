# mcp/src/agents_remember/providers/lifecycle/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/overview.md](overview.md)

## Purpose

`providers.lifecycle` is the public provider lifecycle package facade. It
re-exports provider-owned CGC and GrepAI lifecycle modules, shared lifecycle
helper modules, CLI functions, and aggregate watcher actions.

## Code Commentary

### Logic

The facade imports `ContextProviderError`, `stable_provider_id`, all CGC and
GrepAI lifecycle exports, shared helper modules by responsibility, watcher
operations, and the CLI `main()` function. `__all__` is generated from the
public global names so tests and service callers can keep using the former
monolithic public surface.

### Invariants And Boundaries

- Keep the facade import-only; provider-specific implementation belongs in
  provider-owned lifecycle packages.
- Keep `main()` sourced from `lifecycle.cli`.
- Callers import this facade directly; there is no `provider_lifecycle.py`
  compatibility module.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The CLI parser and dispatcher live in the lifecycle package. | `build_parser` | mcp/src/agents_remember/providers/lifecycle/cli.py:172-267 |
| CGC exports are grouped behind the CGC package facade. | `_EXPORT_MODULES` | mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py:8-17 |
| GrepAI exports are grouped behind the Docker-owned GrepAI package facade. | `_EXPORT_MODULES` | mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py:8-15 |

## Update History

- 2026-08-04T18:43+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the three malformed rows —
  `build_parser` (cli.py:172-359, covering the dispatcher and `main`), and the two package facades
  bound to their `_EXPORT_MODULES` tuples. Spurious `agents-remember/` prefixes dropped; claim
  wording unchanged.
- 2026-05-25T21:14+02:00: Updated after `providers.lifecycle` became a package facade and shared lifecycle helpers were split by responsibility.
- 2026-05-25T19:16+02:00: Updated after the `provider_lifecycle.py` compatibility shim was deleted and callers wired directly to this facade.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI lifecycle exports moved into `cgc/` and `grepai/` subpackages.
- 2026-05-25T19:01+02:00: Created when provider lifecycle was split into modules and the public facade was renamed to `lifecycle.py`.
