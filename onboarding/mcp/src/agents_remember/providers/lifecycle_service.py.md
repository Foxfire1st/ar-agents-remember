# mcp/src/agents_remember/providers/lifecycle_service.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`lifecycle_service.py` retains typed provider lifecycle services for internal consumers.
The former MCP provider application entrypoints and lifecycle CLI were removed; these
service definitions do not restore either callable surface.

## Code Commentary

### 260731-EFA-L2 Typed Request Object

`run_cgc_lifecycle(service_config, request)` takes the frozen
**`CgcLifecycleRequest(action, repo_id=None, native_args=(), port=8000, context=None)`**. The
action and its inputs are only meaningful together: `native_args` carry a `run` query, while
`port`/`context` carry where a `visualize` server binds and which graph it serves. `native_args` is
a tuple because the request is frozen, and is expanded with `list(request.native_args)` at the CLI
boundary. The allowed-action check (`run`, `visualize`, `refresh-all`) and its `ValueError` are
unchanged.

### Logic

`ProviderLifecycleServiceConfig` carries the trusted coordination root,
temporary lifecycle settings path, dry-run mode, and timeout. The service
functions normalize those paths, build internal namespaces, and dispatch to the
provider lifecycle implementation functions:

- `run_cgc_lifecycle()` supports `run`, `visualize`, and `refresh-all`.
- `run_grepai_lifecycle()` supports `run` and `refresh`.
- `run_watchers_lifecycle()` supports `status`, `start`, `stop`, and
  `shutdown-all`.

The service API catches provider lifecycle operational errors and returns
structured `ok: false` payloads for internal callers.

### Invariants And Boundaries

- Internal service callers must supply trusted lifecycle settings, not treat these helpers as public provider tools.
- This module is not a generic shell wrapper and does not parse arbitrary provider CLI arguments.
- CGC service calls do not carry a Python executable because Docker runner
  lifecycle owns provider execution.
- The retained `lifecycle` package is a lazy backend facade; its CLI and `main()` execution
  adapter were deleted. Do not prescribe a CLI or public MCP provider-tool replacement.

## Evidence

### Repo-Internal References


- Retained backend implementation functions are exported lazily through the lifecycle facade, not an active CLI parser. [2]
