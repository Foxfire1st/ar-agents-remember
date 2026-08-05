# mcp/src/agents_remember/providers/cgc/context/ - CGC Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                                  |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                  |

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

## Update History

- 2026-08-05T03:47+02:00 — 260731-EFA-L6: extracted `CgcInstance` construction into
  `_cgc_instance` and documented why the two templated path fields are deliberately left
  unresolved (`_unresolved_template_path` — read-back comparison against the runtime installer on
  symlinked checkouts). Layout fields, defaults, and image doctrine unchanged. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: `cgc_runtime_layout`'s nineteen flat keywords became the
  `CgcRepo` / `CgcInstance` / `CgcWatcher` / `CgcBackend` bundles with frozen module-level defaults
  standing for conventional placement. The produced `CgcRuntimeLayout` is identical; the runner
  image rule and layer-revision doctrine below still hold. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-03T01:55+02:00 — L12 route impact: materialize targets the watch-context global .cgcignore; constants add per-repo exclusions + timer-pop patch (revision ar2); patches.py applies it idempotently.
- 2026-06-10T07:40+02:00 — No route impact: `core.py` re-exports `to_container_path` from its new canonical home `providers/context_common.py`; `cleanup.py`/`patches.py` only updated the import path (GitHub #58).
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.0/2.5.1: the single `cgc_runner_image()` derivation rule and the layer-revision bump doctrine (GitHub #50). Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-05-29T18:35+02:00: Split `core.py` (668 lines) — extracted `materialize.py` (runtime dir/config-file writers) and `cleanup.py` (stale-artifact removal); `core.py` (now 522) keeps the layout dataclass + construction (commit `01f503d`).
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/cgc/context/` route.
- 2026-05-25T19:16+02:00: Created when CGC provider context behavior moved into its own subpackage.
