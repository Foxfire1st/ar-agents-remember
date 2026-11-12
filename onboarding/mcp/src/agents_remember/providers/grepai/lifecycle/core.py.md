# mcp/src/agents_remember/providers/grepai/lifecycle/core.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`core.py` owns GrepAI settings, layout, workspace, runner, backend, and
embedder derivation shared by the Docker-owned GrepAI modules.

## Code Commentary

### 260731-EFA-L2 Workspace And Port Objects

Two frozen parameter objects are defined here and used across the GrepAI lifecycle:

- **`GrepaiWorkspaceConfig(dsn, embedder_settings=None, project_paths=None)`** — what one
  `workspace.yaml` says: the store, the embedder, the projects. The three are only meaningful as
  one document, because the watcher reads them together to know where to write vectors, how to
  produce them, and which paths each indexed project lives at inside the container.
  `prepare_grepai_workspace(layout, provider_settings, config, *, dry_run=False)` takes it, and
  still falls back to `grepai_embedder_settings(provider_settings)` when `config.embedder_settings`
  is `None`.
- **`GrepaiServicePorts(postgres=None, ollama=None)`** — the host ports the stack publishes its
  dependencies on. `UNRESOLVED_SERVICE_PORTS` is the module-level empty instance meaning "nothing
  published yet", so each command falls back to the configured host port.

`grepai_layout_from_args` builds the layout through `grepai_runtime_layout(GrepaiWorkspace(...),
instance=GrepaiInstance(runtime_root=…))`.

### Logic

The module resolves settings-backed GrepAI runtime layout
(`grepai_settings_from_file(from_settings)` — since 260703-L14 the explicit
`--from-settings` path is REQUIRED even for manual `--root`/`--runtime-root`
layouts, because `grepai_layout_from_args` always reads provider settings for
workspace/embedder derivation and the implicit coordinator-settings fallback
was deleted), prepares workspace state, validates Docker mode, derives the managed Docker network name, maps
container-visible root paths, builds container DSNs and container-local
environment variables, selects a supported runner release architecture, and
derives PostgreSQL, Ollama, and runner image settings.

Root container paths resolve under the runner `rootsMount` (default
`/grepai/roots/<project_id>`) via `grepai_root_container_path`, where each live
memory root is bind-mounted; the prior host-path translator
(`grepai_container_path`) is gone. `prepare_grepai_workspace` no longer syncs a
mirror or scrubs artifacts -- it calls `ensure_grepai_root_gitignore` so each
root's `.gitignore` ignores grepai's `.grepai/` working dir.

`grepai_embedder_backend_settings` now conditionally propagates
`seedFromContainer` from the embedder backend settings into the resolved dict.
The key is present only when the raw backend settings carry a non-empty
`seedFromContainer` string (populated by `isolated.py` for worktree embedders
to name the workspace Ollama container); it is absent for the workspace embedder
itself. This lets `embedder.py`'s `_seed_ollama_model_from_source` find the
seed target without the caller needing to pass it separately.

### Invariants And Boundaries

- Settings-backed GrepAI lifecycle must use Docker mode.
- Workspace config must use container-visible project paths, the Postgres
  container DSN, and the Ollama container endpoint.
- Containerized GrepAI watcher environment must point at mounted container
  paths such as `/grepai/runtime/home`, not host runtime paths.
- This module derives configuration only; container start/status logic belongs
  in backend, embedder, and runner modules. It no longer runs commands itself:
  the `grepai_run_checked_command` helper and the `run_command` import were
  removed, so command execution lives solely in the lifecycle command runner.
- Layout-consuming helpers (`grepai_layout_from_args` return value,
  `prepare_grepai_workspace`, runner/backend/embedder/container/template-vars
  builders) are typed against the `GrepaiRuntimeLayout` dataclass, not an
  opaque `Any`.
- Imports come from the leaf modules (`grepai.context`, `context.common`),
  never the `providers.context` aggregator: the aggregator star-imports this
  provider's context back, so routing through it is a circular import that
  breaks any entry point touching grepai modules first.

## Evidence

### Repo-Internal References

- GrepAI PostgreSQL backend lifecycle consumes backend settings from this module through `grepai_backend_start`. [1]
- GrepAI Ollama lifecycle consumes embedder settings from this module through `grepai_embedder_backend_start`. [2]
- GrepAI runner image/container lifecycle consumes runner settings and workspace config from this module through `grepai_watcher_container_start` and `grepai_runner_image_build`. [3]
