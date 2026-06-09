# mcp/src/agents_remember/providers/cgc/lifecycle/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T22:10+02:00                     |
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03` |
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`core.py` owns CodeGraphContext lifecycle settings and layout derivation.

## Code Commentary

### Logic

The module resolves CGC runtime layout from either settings-backed provider
roots or manual CLI overrides, validates configured roots, selects the active
root by repo ID, and derives managed backend settings such as FalkorDB image,
ports, data roots, container name, and image lock path. It also derives Docker
runner image/build/lock/container settings for CGC command execution.

### Invariants And Boundaries

- Settings-backed CGC commands must select configured roots from provider
  settings rather than guessing repository paths.
- Backend settings must be concrete before Docker lifecycle code uses them.
- Runner image settings must be concrete before Docker lifecycle code uses
  them.
- This module should not start processes or containers.
- Layout parameters and layout lists are typed as `CgcRuntimeLayout` (imported
  from `agents_remember.providers.context`), not bare `Any`; the same type is
  the return of `cgc_layout_from_args` and the list element of the
  `*_layouts_from_settings` helpers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend container lifecycle consumes backend settings from this module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| CGC lifecycle actions consume the selected runtime layout from this module. | [process_control.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py); [refresh.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py); [query.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/query.py) |
| CGC Docker runner helpers consume runner image/build/lock/container fields from this layout. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-06-09T22:10+02:00 — `cgc_backend_settings()` gained `dataDestination` (default `/var/lib/falkordb/data`, mirroring the GrepAI `dataDestination` pattern): the container path the FalkorDB data volume binds to, fixing graph persistence across container recreates.

- 2026-05-31T12:50+02:00 — Re-typed `layout` params, `layouts` lists, and the `cgc_layout_from_args` / `*_layouts_from_settings` return types from bare `Any` to `CgcRuntimeLayout` (newly imported from `agents_remember.providers.context`); behavior-preserving, added a layout-type note to Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-26T12:51+02:00: Updated after CGC layouts gained Docker runner image/build/lock/container fields and stopped creating provider venv directories.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC settings and layout logic extracted out of provider lifecycle.
