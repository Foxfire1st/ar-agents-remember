# mcp/src/agents_remember/providers/cgc/context/ - CGC Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-10T07:40+02:00|
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0`                                  |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `../overview.md`                  |

## Purpose

`cgc/context/` owns CodeGraphContext provider context layout, materialization, cleanup, constants, and patch helpers.

## Hot Path Summary

Use `core.py` for `CgcRuntimeLayout` and settings-derived layout construction. Use `materialize.py` for `ensure_cgc_runtime_layout` (managed dirs/config-file creation). Use `cleanup.py` for source-artifact checks and stale provider runtime cleanup. Use `constants.py` for pins, backend names, env exclusions, default `.cgcignore`, and patch snippets. Use `patches.py` for upstream CGC module discovery and marker-based patch application.

`core.py`'s public `cgc_runner_image()` is the single source of truth for the
runner image tag (`repository:version-layerrevision`); `providers/settings.py`
imports it rather than deriving the tag independently (the 2.5.0 upgrade-path
bug, GitHub #50). Bump `constants.py`'s `CGC_RUNNER_IMAGE_LAYER_REVISION`
whenever the runner Docker layer changes without a cgc version change, because
`runtime_install` skips building image tags that already exist.

## Update History

- 2026-06-10T07:40+02:00 — No route impact: `core.py` re-exports `to_container_path` from its new canonical home `providers/context_common.py`; `cleanup.py`/`patches.py` only updated the import path (GitHub #58).
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.0/2.5.1: the single `cgc_runner_image()` derivation rule and the layer-revision bump doctrine (GitHub #50). Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-05-29T18:35+02:00: Split `core.py` (668 lines) — extracted `materialize.py` (runtime dir/config-file writers) and `cleanup.py` (stale-artifact removal); `core.py` (now 522) keeps the layout dataclass + construction (commit `01f503d`).
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/cgc/context/` route.
- 2026-05-25T19:16+02:00: Created when CGC provider context behavior moved into its own subpackage.
