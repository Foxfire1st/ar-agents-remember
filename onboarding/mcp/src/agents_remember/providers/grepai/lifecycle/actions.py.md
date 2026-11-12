# mcp/src/agents_remember/providers/grepai/lifecycle/actions.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`actions.py` owns top-level GrepAI lifecycle action dispatch and the
Docker-only install/run/status composition.

## Code Commentary

### 260731-EFA-L2 Call Sites For The New Bundles

The action wrappers construct the parameter objects their callees now take (all defined in
`grepai/lifecycle/core.py` and `runner.py`):

- `prepare_grepai_workspace(layout, provider_settings, GrepaiWorkspaceConfig(dsn=…,
  project_paths=…, embedder_settings=…))` — in both `grepai_docker_workspace_state` and
  `grepai_install_workspace`.
- `grepai_watcher_container_start(..., ports=GrepaiServicePorts(postgres=…, ollama=…))` — the two
  published host ports read out of the backend and embedder results.
- `grepai_docker_state(layout, GrepaiStackResults(backend=…, embedder=…, watcher=…), action=…,
  runner=…)` — the per-container lifecycle results.

The written state file and every returned payload are unchanged.

### Logic

The module reports aggregate GrepAI status, validates bounded native GrepAI CLI
arguments, executes bounded commands through `docker exec ar-grepai-watcher`,
starts/stops/refreshes the Docker watcher, prepares the workspace after backend
and embedder startup, builds the runner image during install, and returns
structured unsupported results for non-Docker settings. Full Docker start
passes the backend and embedder host ports selected by their startup steps into
watcher startup so later Compose calls use the same dependency port mappings.

### Invariants And Boundaries

- Direct `grepai run` is for bounded CLI commands only; watcher commands route
  through lifecycle start/stop/refresh.
- Non-Docker GrepAI paths must report unsupported instead of installing host
  binaries or using host Ollama.
- Full install/start health is the composed state of Postgres, Ollama, runner
  image, watcher container, and workspace config. Presence of grepai's `.grepai/`
  working dir in a root is expected (roots are watched live) and no longer fails
  status.
- Watcher startup should receive the current backend/embedder port mappings
  from the same GrepAI start flow.
- The `layout` parameter throughout is the concrete `GrepaiRuntimeLayout`
  dataclass (re-exported via the `core` star-import), not an untyped `Any`.

## Evidence

### Repo-Internal References

- PostgreSQL, Ollama, and runner modules provide the Docker stack that this module composes. [1]
