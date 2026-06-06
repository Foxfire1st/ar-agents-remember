# mcp/src/agents_remember/providers/grepai/context/ - GrepAI Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-06T12:15                           |
| lastVerifiedCommitHash | `11f28a2035f06f8bc33f11b0617b41cda1122c1f` |
| lastVerifiedCommitDate | 2026-06-06T13:01:33+02:00|
| governingOverview      | `../overview.md`                  |

## Purpose

`grepai/context/` owns Docker-owned GrepAI provider context constants, runtime layout, live in-place root indexing, and workspace config generation.

## Hot Path Summary

Use `constants.py` for Docker/network/container defaults, `layout.py` for `GrepaiRuntimeLayout`, provider settings expansion, live memory roots, and per-root `.gitignore` of grepai's `.grepai/` working dir, and `workspace.py` for workspace YAML rendering. `core.py` and `__init__.py` are facades over those focused modules.

## Update History

- 2026-06-06T12:15: Re-verified against the current GrepAI context package; live memory-root indexing and per-root `.grepai/` ignores still match the source.
- 2026-06-02T01:15+02:00: Watch live memory roots in place; removed `artifacts.py` (the `.grepai/` artifact guard) and the mirror sync — grepai's `.grepai/` is now git-ignored per root.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/context/` route.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split into constants, layout, workspace, and artifact modules.
- 2026-05-25T19:16+02:00: Created when GrepAI provider context behavior moved into its own subpackage.
