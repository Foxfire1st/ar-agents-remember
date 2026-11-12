# mcp/src/agents_remember/providers/grepai/lifecycle/compose.py

## Governing Overview

[GrepAI Lifecycle Overview](overview.md)

## Purpose

`compose.py` renders the GrepAI Docker Compose override from MCP-derived
provider settings, runtime layout, and runner/backend settings. It keeps
Postgres, Ollama, and watcher dynamic values out of Python `docker run`
assembly while still letting lifecycle code choose ports and paths.

## Code Commentary

### 260731-EFA-L2 Published Ports As One Value

`grepai_compose_render(provider_settings, layout, runner, backend, ports=UNRESOLVED_SERVICE_PORTS)`
takes the two published dependency ports as one `GrepaiServicePorts` (from
`grepai/lifecycle/core.py`) instead of the `postgres_port=` / `ollama_port=` keywords.
`UNRESOLVED_SERVICE_PORTS` is the module-level empty instance meaning **nothing published yet**,
which is what makes the existing fallback read honestly: `ports.postgres or
backend["postgresHostPort"]` and `ports.ollama or embedder["httpHostPort"]` — an unpublished port
falls back to the configured host port, exactly as before. The rendered compose files and their
hashes are unchanged.

### Logic

`grepai_compose_render()` derives Ollama embedder settings, chooses caller
provided or configured host ports, fills Postgres and Ollama images,
containers, ports, and data volumes, points the runner build context at the
committed GrepAI Docker asset, injects runner version/architecture build args,
and renders watcher runtime/log mounts plus a read-write bind-mount of each live
memory root at `/grepai/roots/<project_id>` (`WATCHER_ROOT_VOLUMES`), environment,
workspace name, and network name into the package override template. Port mappings go through the
shared Compose helper so configured `auto` host ports render as Compose's empty
published-port syntax instead of the literal string `auto`. The watcher
environment is rendered from container-local runtime paths, and the Compose
override includes a host UID/GID user block on POSIX hosts so watcher-created
runtime artifacts stay removable by the developer user.
`grepai_compose_summary()` returns the project, package base file, override
hash, and stdin override mode. GrepAI Compose rendering requires generated
`instance.labels` from MCP/provider settings and fails instead of rendering
legacy unlabeled provider resources.

### Invariants And Boundaries

- GrepAI override values must come from provider settings, lifecycle layout, and
  runner/backend derivation, not arbitrary tool input.
- Rendered overrides are fed to Compose through stdin by shared lifecycle
  helpers; this module only renders and summarizes.
- `auto` host ports must remain valid Compose input because every `docker
  compose` invocation parses the whole provider project, even when only one
  service is targeted.
- The watcher uses package-owned runner build assets and mounted runtime/log
  directories from the resolved provider layout.
- The watcher must not receive host-path `HOME`/XDG environment values inside
  the container; GrepAI discovers its workspace config through the mounted
  `/grepai/runtime/home/.grepai` tree.
- GrepAI Docker resources must render with generated Agents Remember ownership
  labels; missing `instance.labels` is an invalid settings shape.

## Evidence

### Repo-Internal References

- `grepai_compose_render()` fills the package override template and shared port mapping values. [1]
- The watcher user block is supplied by `host_user_block()`. [2]
- The summary reports Compose project, package base file, override SHA-256, and stdin override mode. [3]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is required beyond mounted runtime roots configured by provider settings.
