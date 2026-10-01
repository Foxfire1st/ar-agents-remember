# mcp/src/agents_remember/providers/cgc/lifecycle/core.py

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

## Evidence

### Repo-Internal References

- CGC backend container lifecycle consumes backend settings from this module through `cgc_backend_start`. [1]
- CGC lifecycle actions consume the selected runtime layout through `cgc_start`, `cgc_refresh`, and `cgc_run`. [2]
- CGC Docker runner helpers consume runner image/build/lock/container fields from this layout through `cgc_runner_image_build`. [3]
