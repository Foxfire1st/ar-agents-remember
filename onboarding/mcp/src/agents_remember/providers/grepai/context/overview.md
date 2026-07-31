# mcp/src/agents_remember/providers/grepai/context/ - GrepAI Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                  |

## Purpose

`grepai/context/` owns Docker-owned GrepAI provider context constants, runtime layout, live in-place root indexing, and workspace config generation.

## Hot Path Summary

Use `constants.py` for Docker/network/container defaults and preferred host ports, `layout.py` for `GrepaiRuntimeLayout`, provider settings expansion, live memory roots, and per-root `.gitignore` of grepai's `.grepai/` working dir, and `workspace.py` for workspace YAML rendering. The managed GrepAI provider prefers host `61432` for Postgres and host `61434` for Ollama so local dashboard/provider work does not claim common neighboring service ports. `core.py` and `__init__.py` are facades over those focused modules.

## Layout Construction Is Now Three Named Things

`grepai_runtime_layout` used to take eleven flat keyword arguments. It is now
`grepai_runtime_layout(workspace, *, instance=, backend=)` over three frozen dataclasses in
`layout.py`:

- **`GrepaiWorkspace`** — what GrepAI indexes: `coordination_root`, `name` (defaulting to
  `agents-remember-memory`), and the `roots` tuple of `GrepaiMemoryRoot`. Positional and required.
  This is the multi-root shape the isolation invariant is stated over.
- **`GrepaiInstance`** — where the instance lives: `runtime_root`, `logs_root`,
  `requirements_file`, `state_file`. Every field optional.
- **`GrepaiBackend`** — the managed PostgreSQL: `root`, `data_root`, `state_file`. Every field
  optional.

**Every field of the two keyword bundles is an override of the conventional placement under
`providers/runners/grepai`, so the empty instance IS the convention** — hence the frozen
module-level `DEFAULT_GREPAI_INSTANCE` / `DEFAULT_GREPAI_BACKEND` used as defaults rather than
`None` sentinels. A newly pinnable path is a new optional field on the bundle that owns the
subject, not a new `grepai_runtime_layout` keyword.

`GrepaiRuntimeLayout` — the returned value, its fields, and the resolution rules including the
`stable_provider_id` normalization of the workspace name — is unchanged. Only construction moved,
so every reader of a layout is unaffected.

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: `grepai_runtime_layout`'s eleven flat keywords became
  the `GrepaiWorkspace` / `GrepaiInstance` / `GrepaiBackend` bundles with frozen module-level
  defaults standing for conventional placement. The produced layout, the preferred host ports and
  the live-root/`.grepai/`-ignore behaviour below are unchanged. Verification metadata pinned
  until closeout stamps the L2 commit.
- 2026-06-25T09:55+02:00: Context constants now record GrepAI's preferred auto host ports (`61432` Postgres, `61434` Ollama) separately from Docker container service ports.
- 2026-06-10T07:40+02:00 — No route impact: `layout.py` only updated the shared-helper import path to `providers/context_common.py` (GitHub #58).
- 2026-06-06T12:15: Re-verified against the current GrepAI context package; live memory-root indexing and per-root `.grepai/` ignores still match the source.
- 2026-06-02T01:15+02:00: Watch live memory roots in place; removed `artifacts.py` (the `.grepai/` artifact guard) and the mirror sync — grepai's `.grepai/` is now git-ignored per root.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/context/` route.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split into constants, layout, workspace, and artifact modules.
- 2026-05-25T19:16+02:00: Created when GrepAI provider context behavior moved into its own subpackage.
