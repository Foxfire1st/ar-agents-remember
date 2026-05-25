# mcp/src/agents_remember/providers/context_modules/cgc/ - CGC Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/context_modules/cgc/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../overview.md`                  |

## Purpose

`context_modules/cgc/` owns CodeGraphContext provider context layout, cleanup, constants, and patch helpers.

## Hot Path Summary

Use `core.py` for `CgcRuntimeLayout`, settings-derived layout, managed config file creation, source artifact checks, and stale provider runtime cleanup. Use `constants.py` for pins, backend names, env exclusions, default `.cgcignore`, and patch snippets. Use `patches.py` for upstream CGC module discovery and marker-based patch application.

## Update History

- 2026-05-25T19:16+02:00: Created when CGC provider context behavior moved into its own subpackage.
