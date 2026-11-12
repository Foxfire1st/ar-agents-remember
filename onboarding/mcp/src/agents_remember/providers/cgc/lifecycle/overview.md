# mcp/src/agents_remember/providers/cgc/lifecycle/ - CGC Lifecycle Modules Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/providers/cgc/lifecycle/` |

## Governing Overview

[CodeGraphContext Provider Overview](../overview.md)

## Purpose

`cgc/lifecycle/` implements the CodeGraphContext provider lifecycle behind a CGC package facade, using prefix-free module filenames. It separates settings and runtime layout, the shared FalkorDB backend, runner images, watcher-container inspection, installation and status, and process stop. There is no index-refresh module and no native query or visualizer module: those operations are not part of the current lifecycle surface.

## Hot Path Summary

`__init__.py` lazily resolves exports from the lifecycle modules through the package facade, over exactly six modules: `core`, `compose`, `backend`, `runner`, `installation` and `process_control`. `core.py` resolves settings and layouts; `compose.py` renders the shared backend, runner, and repository watcher services; `backend.py` manages FalkorDB; `runner.py` builds the runner image, exposes the packaged patch script, and inspects watcher containers; `installation.py` implements installation, layout initialization, status, and doctor checks; and `process_control.py` stops watcher containers. There is no `refresh.py` and no `query.py` in the package.

The parent lifecycle facade resolves CGC exports through this package and imports exactly `cgc_stop_all` from it. Watcher aggregation maps only `stop` and `shutdown-all` for CGC, both onto that all-root handler, and requires a durable process namespace for either; there is no start action and no status aggregation through this route. The typed service's admitted action set is the stop family — `{"stop", "shutdown-all"}` — because `status` and `start` were admitted only while a generic facade parameter was mistaken for a caller (L192-F01). No `run`, `visualize` or `refresh-all` dispatcher exists in this package to receive such a call.

## How It Is Built

Settings-backed layouts read an explicit settings path through `cgc_settings_from_file`; there is no implicit coordination-root settings lookup. The provider entry supplies configured repository roots, and root selection validates their shape and resolves repository identity. The separate manual layout branch constructs `CgcRepo(...)` with the coordination root, repository ID, and code repository root; see the [context route](../context/overview.md). These internal argument shapes and retained settings vocabulary do not establish a public provisioning command.

`core.py` also applies configured layout and backend state and invokes runtime-artifact cleanup. It is therefore more than configuration and layout calculation alone.

`compose.py` owns service rendering, network selection, mounts, environment, ownership labels, and host-user execution blocks. Repository mounts are read-only; runtime mounts hold provider artifacts. Runner and watcher environments address FalkorDB by its backend container name. `runner.py` builds the runner through Compose, records its image lock, exposes the packaged patch script, and reports image and watcher state. Patching is represented as part of the Docker image rather than a separate lifecycle patch operation.

`installation.py` owns runner installation and doctor checks. Provider status reports watcher container state, runner-image availability, source artifacts, process namespace, `lastRefresh`, and indexing state. Shared backend status separately reports container state, network attachment, ports, data-mount agreement, and readiness.

`backend.py` represents a resolved invocation with frozen `CgcBackendContext`, carrying `settings_path`, `provider_settings`, `layouts`, and `backend`. Both `cgc_primary_backend_context(args)` and `cgc_backend_start_context(args)` return this value. Its `layout` property returns `layouts`: FalkorDB is shared across configured repository layouts, and backend commands act through the first selected layout.

`CgcBackendPort` identifies a published port through the keys used in recorded state, resolved backend settings, and container inspection. `FALKORDB_PORT` and `BROWSER_PORT` are its two instances. `cgc_backend_endpoint(state, backend, inspect_data, port)` accepts this value, while `CgcHostPorts` carries the two published host ports together. An additional published port belongs in a new `CgcBackendPort` constant rather than another parallel group of endpoint keywords.

`process_control.py` owns watcher stop independently of backend lifecycle: `cgc_stop`, `cgc_stop_all` and their dry-run, preflight, mark-stopped and layout-action-result helpers, with no start operation to pair with. Index refresh, bounded native runs and visualization are not operations of this package — no refresh, query or visualizer module exists — so nothing here constructs them; status still reports any `lastRefresh` persisted in state, which no current code writes.

## Invariants And Boundaries

- Keep `__init__.py` as the CGC package export facade and keep GrepAI behavior outside this package.
- Settings-backed lifecycle resolution requires an explicit settings path and a valid `codegraphcontext-code` provider entry. Missing input must not silently become empty configuration.
- Managed backend startup requires the `falkordb-remote` backend type and `docker` mode. Backend lifecycle remains separate from watcher stop.
- Managed CGC execution uses Docker Compose rather than a host Python environment or host `cgc` executable. Runner and watcher containers reach FalkorDB through the shared Docker network and backend container name, rather than host loopback.
- Live watcher stop, including the all-root actions, retains the durable process-namespace check; live visualization does not exist in this package and has no check to retain.
- Settings-backed lifecycle reads select a root by repository ID; there is no native-run or visualizer command in this package for such a rule to constrain.
- Preserve backend and watcher container state in status reporting so callers can describe the running provider; status reads persisted state and does not imply a watcher is running.

## Evidence

- The parent lifecycle facade imports the CGC package facade. [1]
- Watcher aggregation imports exactly `cgc_stop_all` from this package; both admitted CGC watcher actions (`stop`, `shutdown-all`) resolve to it, and no start or status aggregation is imported. [2]
