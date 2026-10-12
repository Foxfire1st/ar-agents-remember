# mcp/src/agents_remember/providers/cgc/lifecycle/ - CGC Lifecycle Modules Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/providers/cgc/lifecycle/` |

## Governing Overview

[CodeGraphContext Provider Overview](../overview.md)

## Purpose

`cgc/lifecycle/` implements the CodeGraphContext provider lifecycle behind a CGC package facade, using prefix-free module filenames. It separates settings and runtime layout, the shared FalkorDB backend, runner images, watcher containers, index refresh, and native queries and visualization.

## Hot Path Summary

`__init__.py` lazily resolves exports from the lifecycle modules through the package facade. `core.py` resolves settings and layouts; `compose.py` renders the shared backend, runner, and repository watcher services; `backend.py` manages FalkorDB; and `runner.py` builds and inspects runner images and inspects watcher containers. `installation.py` implements installation, layout initialization, status, and doctor checks. `process_control.py` starts and stops watcher containers, `refresh.py` refreshes indexes, and `query.py` runs bounded native commands and the visualizer.

The parent lifecycle facade resolves CGC exports through this package. Watcher aggregation routes start, stop, and shutdown actions to all-root handlers and combines shared backend status with per-root provider status. The typed CGC lifecycle service dispatches `run`, `visualize`, and `refresh-all` from its settings-owned service configuration.

## How It Is Built

Settings-backed layouts read an explicit settings path through `cgc_settings_from_file`; there is no implicit coordination-root settings lookup. The provider entry supplies configured repository roots, and root selection validates their shape and resolves repository identity. The separate manual layout branch constructs `CgcRepo(...)` with the coordination root, repository ID, and code repository root; see the [context route](../context/overview.md). These internal argument shapes and retained settings vocabulary do not establish a public provisioning command.

`core.py` also applies configured layout and backend state and invokes runtime-artifact cleanup. It is therefore more than configuration and layout calculation alone.

`compose.py` owns service rendering, network selection, mounts, environment, ownership labels, and host-user execution blocks. Repository mounts are read-only; runtime mounts hold provider artifacts. Runner and watcher environments address FalkorDB by its backend container name. `runner.py` builds the runner through Compose, records its image lock, exposes the packaged patch script, and reports image and watcher state. Patching is represented as part of the Docker image rather than a separate lifecycle patch operation.

`installation.py` owns runner installation and doctor checks. Provider status reports watcher container state, runner-image availability, source artifacts, process namespace, `lastRefresh`, and indexing state. Shared backend status separately reports container state, network attachment, ports, data-mount agreement, and readiness.

`backend.py` represents a resolved invocation with frozen `CgcBackendContext`, carrying `settings_path`, `provider_settings`, `layouts`, and `backend`. Both `cgc_primary_backend_context(args)` and `cgc_backend_start_context(args)` return this value. Its `layout` property returns `layouts[0]`: FalkorDB is shared across configured repository layouts, and backend commands act through the first selected layout.

`CgcBackendPort` identifies a published port through the keys used in recorded state, resolved backend settings, and container inspection. `FALKORDB_PORT` and `BROWSER_PORT` are its two instances. `cgc_backend_endpoint(state, backend, inspect_data, port)` accepts this value, while `CgcHostPorts` carries the two published host ports together. An additional published port belongs in a new `CgcBackendPort` constant rather than another parallel group of endpoint keywords.

`process_control.py` owns watcher start and stop independently of backend lifecycle. Refresh uses a Docker runner to force indexing and records its result in `lastRefresh`; all-root refresh first starts watchers, then refreshes repository layouts. Native runs use an ephemeral Compose runner and check backend readiness independently of watcher availability. Visualization has its own command construction and status checks.

## Invariants And Boundaries

- Keep `__init__.py` as the CGC package export facade and keep GrepAI behavior outside this package.
- Settings-backed lifecycle resolution requires an explicit settings path and a valid `codegraphcontext-code` provider entry. Missing input must not silently become empty configuration.
- Managed backend startup requires the `falkordb-remote` backend type and `docker` mode. Backend lifecycle remains separate from watcher start and stop.
- Managed CGC execution uses Docker Compose rather than a host Python environment or host `cgc` executable. Runner and watcher containers reach FalkorDB through the shared Docker network and backend container name, rather than host loopback.
- Live watcher start and stop, including all-root actions, and live visualization retain durable process-namespace checks.
- Settings-backed native runs and visualization require a repository ID. Native runs reject `visualize`; the visualizer is a separate long-running operation.
- Preserve backend and watcher container state in status reporting so callers can describe the running provider. A bounded native run needs backend readiness and does not require a running watcher.

## Evidence

- The parent lifecycle facade imports the CGC package facade. [1]
- Watcher aggregation imports CGC all-root start/status/stop behavior from this package; status combines shared backend status with per-root provider results. [2]
