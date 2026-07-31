# mcp/src/agents_remember/providers/cgc/lifecycle/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`core.py` owns CodeGraphContext lifecycle settings and layout derivation.

## Code Commentary

### 260731-EFA-L2 Layout Call Site

`cgc_layout_from_args` now builds the layout as `cgc_runtime_layout(CgcRepo(coordination_root=…,
repo_id=…, code_repo_root=…))` — the three manual-override arguments the command requires, wrapped
in the repo bundle the layout builder takes. No instance/watcher/backend override is passed, which
is what selects conventional placement. Behaviour is unchanged, including the
`--repo-id`/`--code-repo-root` requirement check that precedes it.

### Logic

The module resolves CGC runtime layout from either settings-backed provider
roots (`cgc_settings_from_file(from_settings)` — since 260703-L13 the reader
takes the explicit path only; the manual `--repo-id`/`--code-repo-root`
override path stays settings-free), validates configured roots, selects the
active root by repo ID, and derives managed backend settings such as FalkorDB image,
ports, data roots, container name, `dataDestination` (the container path the
data volume binds to, default `/var/lib/falkordb/data` — where FalkorDB v4
actually writes), and image lock path. It also derives Docker
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
| CGC backend container lifecycle consumes backend settings from this module. | [backend.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| CGC lifecycle actions consume the selected runtime layout from this module. | [process_control.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py); [refresh.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py); [query.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/query.py) |
| CGC Docker runner helpers consume runner image/build/lock/container fields from this layout. | [runner.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update for `cgc_runtime_layout`'s new
  signature (`CgcRepo` bundle). Same resolved layout. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-07-06T22:36+02:00 — 260703-L13 ride-along: the three `cgc_settings_from_file` call
  sites dropped the `coordination_root` argument (the implicit coordinator-settings fallback
  was deleted; explicit `--from-settings` behavior unchanged, manual override path
  unaffected). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-06-10T06:20+02:00 — Body-quality pass: `dataDestination` now named in the Logic list of derived backend settings (documentation only).
- 2026-06-09T22:10+02:00 — `cgc_backend_settings()` gained `dataDestination` (default `/var/lib/falkordb/data`, mirroring the GrepAI `dataDestination` pattern): the container path the FalkorDB data volume binds to, fixing graph persistence across container recreates.
- 2026-05-31T12:50+02:00 — Re-typed `layout` params, `layouts` lists, and the `cgc_layout_from_args` / `*_layouts_from_settings` return types from bare `Any` to `CgcRuntimeLayout` (newly imported from `agents_remember.providers.context`); behavior-preserving, added a layout-type note to Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-26T12:51+02:00: Updated after CGC layouts gained Docker runner image/build/lock/container fields and stopped creating provider venv directories.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC settings and layout logic extracted out of provider lifecycle.
