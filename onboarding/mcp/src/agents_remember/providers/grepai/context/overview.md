# mcp/src/agents_remember/providers/grepai/context/ - GrepAI Context Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/context/` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`grepai/context/` supplies the Docker-owned GrepAI provider's constants, runtime layout construction, live memory-root settings, root ignore maintenance, and workspace configuration rendering. The lifecycle modules use these helpers to prepare the provider and index the live roots in place.

## Hot Path Summary

Use `constants.py` for Docker/network/container defaults and preferred host ports, `layout.py` for `GrepaiRuntimeLayout`, provider settings expansion, live memory roots, and per-root `.gitignore` maintenance for GrepAI's `.grepai/` working directory, and `workspace.py` for workspace YAML rendering. The managed provider prefers host `61432` for Postgres and host `61434` for Ollama when allocating automatic ports; an existing published port or an explicitly configured port can take precedence. `core.py` and `__init__.py` re-export these focused modules.

## How It Is Built

`grepai_runtime_layout(workspace, *, instance=, backend=)` constructs a frozen `GrepaiRuntimeLayout` from three frozen input dataclasses:

- `GrepaiWorkspace` describes what GrepAI indexes: the required `coordination_root`, a `name` defaulting to `agents-remember-memory`, and a `roots` tuple of `GrepaiMemoryRoot` defaulting to empty. The workspace argument is required; each memory root carries a project ID and path.
- `GrepaiInstance` supplies optional overrides for `runtime_root`, `logs_root`, `requirements_file`, and `state_file`.
- `GrepaiBackend` supplies optional overrides for the managed PostgreSQL backend's `root`, `data_root`, and `state_file`.

The frozen module-level `DEFAULT_GREPAI_INSTANCE` and `DEFAULT_GREPAI_BACKEND` provide the empty override bundles used by the constructor. Its conventional runtime root is `<coordination_root>/providers/runners/grepai`; logs and provider state default beneath that root. Requirements default to `<coordination_root>/providers/requirements/grepai.txt`. The backend defaults to `<coordination_root>/providers/data/grepai/postgres`, with its data directory and backend state file beneath that backend root.

The returned layout contains coordination and provider roots, the normalized workspace name and memory roots, requirements and workspace configuration paths, provider state and logs, home/run/cache directories, and backend paths. The constructor resolves the coordination root and selected path overrides, normalizes the workspace name through `stable_provider_id`, and carries the supplied memory roots into a tuple.

`grepai_runtime_layout_from_provider_settings` expands configured paths and builds the same three input bundles. Its default watch log directory is `<coordination_root>/logs/providers/grepai`, which differs from the direct constructor's runtime-local log default. The lifecycle's argument-based caller also supplies its selected runtime root explicitly.

`workspace.py` renders a workspace YAML document with the layout's workspace name, PostgreSQL DSN, embedder configuration, and one project entry per memory root. Project paths can be supplied explicitly for the container view; otherwise rendering uses each root's path. The writer stores the rendered document at the layout's workspace configuration path.

## Invariants And Boundaries

Keep workspace identity and indexed roots in `GrepaiWorkspace`, instance placement in `GrepaiInstance`, and PostgreSQL placement in `GrepaiBackend`; an additional instance or backend path override belongs to the bundle that owns that subject.

The direct layout constructor permits an empty roots tuple. The provider-settings reader requires a non-empty roots array, normalizes project IDs, and rejects duplicate IDs. Root paths must have no unresolved angle-bracket placeholders and must exist as directories unless `allowMissingRoots` is explicitly true. The workspace's roots describe the multi-root indexing shape; this constructor alone does not establish a broader isolation guarantee.

The lifecycle prepares the workspace using the live memory roots, and the Compose renderer bind-mounts those paths into the runner. `ensure_grepai_root_gitignore` appends `.grepai/` to each existing root directory's `.gitignore` when the entry is absent, protecting the provider working directory from ordinary Git staging. Workspace preparation skips both ignore maintenance and configuration writing during a dry run.

Layout construction returns paths without creating directories. `ensure_grepai_runtime_layout` creates the provider-owned directories and writes the GrepAI requirement pin only when the requirements file is absent. Container startup and indexing execution belong to the lifecycle callers.

## Evidence

- Provider constants and preferred host ports [1]
- Context facades re-export the focused modules [2]
- Frozen workspace, instance, backend and returned layout shapes [3]
- Constructor placement defaults and workspace-name normalization [4]
- Settings expansion, live roots and caller-supplied placement [5]
- Workspace YAML rendering and writing [6]
- Settings-root validation and duplicate-ID rejection [7]
- Directory and requirements creation is separate from layout construction [8]
- Live-root ignore maintenance, workspace preparation and bind mounts [9]
