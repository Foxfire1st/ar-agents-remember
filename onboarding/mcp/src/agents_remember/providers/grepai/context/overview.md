# mcp/src/agents_remember/providers/grepai/context/ - GrepAI Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/context/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../overview.md`                  |

## Purpose

`grepai/context/` owns Docker-owned GrepAI provider context constants, runtime layout, mirrored root syncing, workspace config generation, and disposable `.grepai/` artifact cleanup.

## Hot Path Summary

Use `constants.py` for Docker/network/container defaults, `layout.py` for `GrepaiRuntimeLayout`, provider settings expansion, provider-owned mirrored roots, and mirror sync, `workspace.py` for workspace YAML rendering, and `artifacts.py` for root artifact validation/removal. `core.py` and `__init__.py` are facades over those focused modules.

## Update History

- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/context/` route.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split into constants, layout, workspace, and artifact modules.
- 2026-05-25T19:16+02:00: Created when GrepAI provider context behavior moved into its own subpackage.
