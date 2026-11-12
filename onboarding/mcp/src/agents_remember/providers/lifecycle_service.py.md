# mcp/src/agents_remember/providers/lifecycle_service.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`lifecycle_service.py` retains typed provider lifecycle services for internal consumers.
The former MCP provider application entrypoints and lifecycle CLI were removed; these
service definitions do not restore either callable surface.

## Code Commentary

### 260731-EFA-L2 Typed Request Object

`CgcLifecycleRequest` and `run_cgc_lifecycle` are gone with the provider start,
visualize and query surface. `ProviderLifecycleServiceConfig` is the module's only
typed input: no request object, action allow-list or CLI boundary remains here.

### Logic

`ProviderLifecycleServiceConfig` carries the trusted coordination root, lifecycle
settings path, dry-run mode, and timeout. `run_watchers_lifecycle()` normalizes that
config, builds the internal namespace, and dispatches to the watcher lifecycle
implementation:

- `WATCHER_SERVICE_ACTIONS` admits `stop` and `shutdown-all` only.
- Any other action raises `ValueError` before dispatch.

No CGC or GrepAI service entrypoint remains in this module.

The service API catches provider lifecycle operational errors and returns
structured `ok: false` payloads for internal callers.

### Invariants And Boundaries

- Internal service callers must supply trusted lifecycle settings, not treat these helpers as public provider tools.
- This module is not a generic shell wrapper and does not parse arbitrary provider CLI arguments.
- No service call here carries a Python executable; the Docker runner
  lifecycle owns provider execution.
- The retained `lifecycle` package is a lazy backend facade; its CLI and `main()` execution
  adapter were deleted. Do not prescribe a CLI or public MCP provider-tool replacement.

## Evidence

### Repo-Internal References


- Retained backend implementation functions are exported lazily through the lifecycle facade, not an active CLI parser. [2]
