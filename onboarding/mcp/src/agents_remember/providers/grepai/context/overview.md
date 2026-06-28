# mcp/src/agents_remember/providers/grepai/context/ - GrepAI Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-25T09:55+02:00|
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                  |

## Purpose

`grepai/context/` owns Docker-owned GrepAI provider context constants, runtime layout, live in-place root indexing, and workspace config generation.

## Hot Path Summary

Use `constants.py` for Docker/network/container defaults and preferred host ports, `layout.py` for `GrepaiRuntimeLayout`, provider settings expansion, live memory roots, and per-root `.gitignore` of grepai's `.grepai/` working dir, and `workspace.py` for workspace YAML rendering. The managed GrepAI provider prefers host `61432` for Postgres and host `61434` for Ollama so local dashboard/provider work does not claim common neighboring service ports. `core.py` and `__init__.py` are facades over those focused modules.

## Update History

- 2026-06-25T09:55+02:00: Context constants now record GrepAI's preferred auto host ports (`61432` Postgres, `61434` Ollama) separately from Docker container service ports.
- 2026-06-10T07:40+02:00 — No route impact: `layout.py` only updated the shared-helper import path to `providers/context_common.py` (GitHub #58).
- 2026-06-06T12:15: Re-verified against the current GrepAI context package; live memory-root indexing and per-root `.grepai/` ignores still match the source.
- 2026-06-02T01:15+02:00: Watch live memory roots in place; removed `artifacts.py` (the `.grepai/` artifact guard) and the mirror sync — grepai's `.grepai/` is now git-ignored per root.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/context/` route.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split into constants, layout, workspace, and artifact modules.
- 2026-05-25T19:16+02:00: Created when GrepAI provider context behavior moved into its own subpackage.
