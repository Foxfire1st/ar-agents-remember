# mcp/src/agents_remember/providers/cgc/context/ - CGC Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/context/` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`cgc/context/` owns CodeGraphContext provider context layout, materialization, cleanup, constants, and patch helpers. Since L12 materialization writes the enriched `.cgcignore` into the HOME-scoped global context file the live watch actually reads, constants carry per-repo managed exclusions (`CGC_REPO_CGCIGNORE_EXTRAS`) plus the watcher timer-pop patch snippets, and the runner image layer revision is `ar2`.

## Hot Path Summary

Use `core.py` for `CgcRuntimeLayout` and settings-derived layout construction. Use `materialize.py` for `ensure_cgc_runtime_layout` (managed dirs/config-file creation). Use `cleanup.py` for source-artifact checks and stale provider runtime cleanup. Use `constants.py` for pins, backend names, env exclusions, default `.cgcignore`, and patch snippets. Use `patches.py` for upstream CGC module discovery and marker-based patch application.

`core.py`'s public `cgc_runner_image()` is the single source of truth for the
runner image tag (`repository:version-layerrevision`); `providers/settings.py`
imports it rather than deriving the tag independently (the 2.5.0 upgrade-path
bug, GitHub #50). Bump `constants.py`'s `CGC_RUNNER_IMAGE_LAYER_REVISION`
whenever the runner Docker layer changes without a cgc version change, because
`runtime_install` skips building image tags that already exist.

## Layout Construction Is Now Four Named Things

`cgc_runtime_layout` used to take nineteen keyword arguments in one flat list, which made the
deployment shape of a CGC instance unreadable. It is now
`cgc_runtime_layout(repo, *, instance=, watcher=, backend=)` over four frozen dataclasses in
`core.py`, and the split is by *subject*, not by convenience:

| Bundle | What it describes | Note |
| --- | --- | --- |
| `CgcRepo` | The repository this instance indexes and the root that owns it — `coordination_root`, `repo_id`, `code_repo_root`, `cgcignore_patterns`. | Positional and required. `cgcignore_patterns` belongs here because it is about which parts of *this* repository the graph covers, not how the provider is deployed. |
| `CgcInstance` | Where the instance lives on disk — `runtime_root`, `requirements_file`, `patches_root`, `state_file`. | Every field optional. |
| `CgcWatcher` | The watcher as *one process* — the runner `image`, the `build_root`/`lock_file` it is produced from, the `container_name` it runs as, its `process_env_template`, and the `watch_cwd`/`watch_log_file` of the `cgc watch` it hosts. | Every field optional. |
| `CgcBackend` | The managed FalkorDB the instance connects to — `root`, `data_root`, `state_file`, `container_name`, `network_name`. | Every field optional. |

**Every field of the three keyword bundles is an override of the conventional placement under
`providers/runners/codegraphcontext/<repoId>`, so the empty instance IS the convention.** That is
why `DEFAULT_CGC_INSTANCE` / `DEFAULT_CGC_WATCHER` / `DEFAULT_CGC_BACKEND` are module-level frozen
singletons used as defaults rather than `None` sentinels. A new pinnable path is a new optional
field on the bundle that owns the subject; it is not a new `cgc_runtime_layout` keyword.

`CgcRuntimeLayout` itself — the returned value, its field names, and the resolution rules that
produce them — is unchanged, so every reader of a layout is unaffected. Only construction moved.

## 260731-EFA-L6 Instance-Bundle Extraction

`cgc_runtime_layout_from_provider_settings` now builds the `CgcInstance` bundle through a
dedicated `_cgc_instance` helper. Its `requirements_file` and `patches_root` go through
`_unresolved_template_path` — template expansion deliberately **without** `.resolve()`, because
those two settings are read back and compared against what the runtime installer wrote, and
resolving them would turn an equal pair into an unequal one on a checkout reached through a
symlink. The defaults
(`<coordination_root>/providers/requirements/codegraphcontext.txt` and
`<coordination_root>/providers/patches/codegraphcontext`), the produced `CgcRuntimeLayout`, and
the runner-image/layer-revision doctrine are unchanged.
