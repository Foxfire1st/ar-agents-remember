# mcp/src/agents_remember/providers/grepai/lifecycle/ - GrepAI Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/lifecycle/` |

## Governing Overview

[GrepAI Provider Overview](../overview.md)

## Purpose

`grepai/lifecycle/` contains the Docker-owned GrepAI provider lifecycle implementation, organized behind a GrepAI package facade with prefix-free filenames. It resolves provider configuration, prepares the workspace, and manages the PostgreSQL backend, Ollama embedder, runner image, and watcher container.

## Hot Path Summary

`__init__.py` lazily exposes the retained Python lifecycle functions. `core.py` derives settings, layout, workspace configuration, container DSNs, and Docker image settings. `compose.py` renders the Docker Compose configuration. `backend.py` manages PostgreSQL/pgvector, `embedder.py` manages Ollama and model readiness, `runner.py` manages the runner image and watcher container, and `actions.py` composes install/status/start/stop/refresh/run behavior.

In the retained Docker stack-start branch, backend and embedder startup precede container-facing workspace preparation and watcher startup; errors are returned rather than a promised running stack. The ordinary enabled-provider setup gate separately excludes `grepai-memory`, even if an old settings block says enabled. Settings-backed native commands use `grepai_docker_run_command`, which executes bounded GrepAI CLI commands in the Compose watcher service; native `watch` is rejected in favor of lifecycle start/stop/refresh.

Status combines backend, embedder, and watcher results. Managed container status includes normalized running state, health, and uptime for MCP current-state packets. The watcher reads Docker logs since its container start into `initialScan`: `Initial scan complete` means `complete`; otherwise `Indexing [`, `Initial scan`, or `Embedding` means `in-progress`; absent usable evidence means `unknown`. The current-state adapter maps those scan states to `indexed` and `indexing` when the watcher is up and a workspace is present, and retains `unknown` when neither marker state is established.

For new `auto` host-port allocations, backend and embedder startup prefer host `61432` for PostgreSQL and host `61434` for Ollama. Existing published ports are reused; if the preferred port is unavailable, the allocator selects an ephemeral port. Container service ports default to `5432` and `11434` and remain separate from host-port allocation.

## How It Is Built

`core.py` reads an explicit settings path and builds the runtime layout through `GrepaiWorkspace(...)` / `GrepaiInstance(...)` or the provider-settings layout constructor (see the [context route](../context/overview.md)). The parent lifecycle facade includes the GrepAI package facade in its lazy export modules.

Frozen dataclasses group the resolved values used by lifecycle operations:

| Type | Home | What it carries |
| --- | --- | --- |
| `GrepaiBackendContext` | `backend.py` | `settings_path`, `provider_settings`, `layout`, `backend`, `network_name`. `grepai_backend_start_context(args)` resolves it for backend startup. |
| `GrepaiEmbedderContext` | `embedder.py` | `settings_path`, `provider_settings`, `layout`, `embedder`, `network_name`. `grepai_embedder_start_context(args)` resolves it for embedder startup. |
| `GrepaiWatcherStart` | `runner.py` | `layout`, `runner`, `network`, `image`: prerequisites assembled before Compose brings up the watcher. |
| `GrepaiStackResults` | `runner.py` | Optional `backend`, `embedder`, and `watcher` lifecycle results passed to `grepai_docker_state(layout, stack, *, action, runner)`. |
| `GrepaiServicePorts` | `core.py` | The published dependency host ports: `postgres`, `ollama`. |
| `GrepaiWorkspaceConfig` | `core.py` | `dsn`, `embedder_settings`, `project_paths`: the store, embedding configuration, and container project paths written together to `workspace.yaml`. |

`backend.py`, `embedder.py`, and the CGC backend use `BackendStartReconciliation` from `providers/lifecycle/compose_runtime.py`. It groups the Compose-managed network result, unmanaged-project migration result, and optional forced removal of a container whose data mount does not match the requested layout. The network result identifies Compose management; it is not independent evidence that the network was already created or adopted before Compose runs.

## Invariants And Boundaries

- GrepAI installation and the main lifecycle actions are Docker-only; unsupported runtime modes return an unsupported result rather than installing or running host GrepAI. The managed backend requires PostgreSQL in Docker. The embedder helpers can return an external-embedder result for non-managed configurations; that does not install or start host Ollama.
- Settings-backed lifecycle resolution requires an explicit `--from-settings` path. There is no implicit coordination-root settings-file fallback.
- Container-visible project paths, service names, and the shared Docker network connect the workspace configuration to the Compose stack. Host-port preferences do not change container service ports.
- `UNRESOLVED_SERVICE_PORTS` is the frozen empty `GrepaiServicePorts` default. Compose rendering uses `ports.postgres or backend["postgresHostPort"]` and the corresponding Ollama expression; callers with resolved published ports pass them explicitly.
- `GrepaiWatcherStart` carries prerequisites resolved by `grepai_watcher_start_prerequisites`, not post-start observations. Normal and dry-run watcher-start results report its network and image values; an image-prerequisite failure returns a separate error result before Compose startup.
- Keep `__init__.py` as the package export facade.
- Lifecycle modules import provider context helpers through `grepai.context` and `providers.context_common`, avoiding direct imports from the `providers.context` aggregator. That aggregator star-imports provider context packages back; the shared helper module lives outside it to avoid initialization cycles.

## Evidence

- The parent lifecycle facade imports the GrepAI package facade. [1]

- The GrepAI lifecycle facade exposes configuration, Compose rendering, backend, embedder, runner, and actions. [2]
- Settings-backed native commands execute bounded GrepAI CLI commands through the Compose watcher service. [3]
- Watcher scan markers yield complete, in-progress, or unknown; the current-state adapter maps them with watcher and workspace guards. [4]
- Container status reports normalized running state, health, and uptime. [5]
- Dependency host ports reuse existing mappings and prefer 61432/61434 for new auto allocations; container ports are separate configurable defaults. [6]
- Lifecycle configuration requires an explicit settings path and constructs the runtime layout. [7]
- Frozen backend and embedder contexts carry resolved startup values. [8]
- Frozen service-port and workspace records group their respective configuration values; Compose rendering retains configured-port expressions. [9]
- Watcher-start prerequisites remain distinct from post-start observations and prerequisite errors; stack results carry optional lifecycle outcomes. [10]
- BackendStartReconciliation groups migration, optional forced removal, and a Compose-managed network result for GrepAI and CGC startup. [11]
- Main GrepAI lifecycle actions reject host runtime modes; managed backend startup requires Docker PostgreSQL; external embedder results do not launch host Ollama. [12]
- Container paths, service names, and shared network connect workspace configuration to the Compose stack. [13]
- Shared context helpers reside outside the aggregator package to avoid provider initialization cycles. [14]
