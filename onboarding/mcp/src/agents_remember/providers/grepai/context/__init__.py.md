# mcp/src/agents_remember/providers/grepai/context/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T01:15+02:00                     |
| lastVerifiedCommitHash | `ab8dda6269c2f8a69c341ae950c2e74d4ab3fe44` |
| lastVerifiedCommitDate | 2026-06-02T01:10:22+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/__init__.py` is the Docker-owned GrepAI context provider subpackage facade.

## Code Commentary

### Logic

It re-exports GrepAI constants, layout, and workspace-config helpers from the focused GrepAI context modules for the public `providers.context` facade.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: removed the unanchorable star-import facade row under the R27/R28 max-reviewer correction. The three exact star imports remain visible in the frozen source and the Logic prose, but no citation row is retained without an allowed anchor.

- 2026-06-02T01:15+02:00: Dropped the `artifacts.py` re-export after the module was removed (roots are watched live; `.grepai/` is git-ignored instead of guarded).
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split from `core.py` into `constants.py`, `layout.py`, `workspace.py`, and `artifacts.py`.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
