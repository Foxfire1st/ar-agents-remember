# mcp/src/agents_remember/providers/lifecycle_service.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`lifecycle_service.py` is the typed provider lifecycle service boundary for MCP
callers. It lets MCP application entry points run provider operations from trusted lifecycle
settings without building CLI `argv` or invoking `lifecycle.main()`.

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

`ProviderLifecycleServiceConfig` carries the server-derived coordination root,
temporary lifecycle settings path, dry-run mode, and timeout. The service
functions normalize those paths, build internal namespaces, and dispatch to the
provider lifecycle implementation functions:

- `run_cgc_lifecycle()` supports `run`, `visualize`, and `refresh-all`.
- `run_grepai_lifecycle()` supports `run` and `refresh`.
- `run_watchers_lifecycle()` supports `status`, `start`, `stop`, and
  `shutdown-all`.

The service API catches provider lifecycle operational errors and returns
structured `ok: false` payloads for MCP callers.

### Invariants And Boundaries

- MCP callers should pass only server-owned settings, not caller-selected roots.
- This module is not a generic shell wrapper and does not expose arbitrary
  provider CLI parsing to MCP.
- CGC service calls do not carry a Python executable because Docker runner
  lifecycle owns provider execution.
- The dev/operator CLI facade is `lifecycle.py`; MCP provider tools should call
  this service layer instead of the CLI `main()` path.

## Evidence

### Repo-Internal References

- MCP provider tool application entry points call this service layer. [1]
- CLI/operator implementation functions remain behind the lifecycle facade. [2]
