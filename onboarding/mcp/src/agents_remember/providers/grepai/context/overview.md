# mcp/src/agents_remember/providers/grepai/context/ - GrepAI Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/context/` |

## Governing Overview

[overview.md](../overview.md)

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
