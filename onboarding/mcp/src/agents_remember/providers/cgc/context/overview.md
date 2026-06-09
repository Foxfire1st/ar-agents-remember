# mcp/src/agents_remember/providers/cgc/context/ - CGC Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `04f736d5fdaf23002b0e4172b7475a1108da0d9e`                                  |
| lastVerifiedCommitDate | 2026-06-09T22:16:49+02:00|
| governingOverview      | `../overview.md`                  |

## Purpose

`cgc/context/` owns CodeGraphContext provider context layout, materialization, cleanup, constants, and patch helpers.

## Hot Path Summary

Use `core.py` for `CgcRuntimeLayout` and settings-derived layout construction. Use `materialize.py` for `ensure_cgc_runtime_layout` (managed dirs/config-file creation). Use `cleanup.py` for source-artifact checks and stale provider runtime cleanup. Use `constants.py` for pins, backend names, env exclusions, default `.cgcignore`, and patch snippets. Use `patches.py` for upstream CGC module discovery and marker-based patch application.

## Update History

- 2026-05-29T18:35+02:00: Split `core.py` (668 lines) — extracted `materialize.py` (runtime dir/config-file writers) and `cleanup.py` (stale-artifact removal); `core.py` (now 522) keeps the layout dataclass + construction (commit `01f503d`).
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/cgc/context/` route.
- 2026-05-25T19:16+02:00: Created when CGC provider context behavior moved into its own subpackage.
