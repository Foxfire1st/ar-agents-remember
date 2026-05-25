# mcp/src/agents_remember/providers/lifecycle_service.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_service.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`lifecycle_service.py` is the typed provider lifecycle service boundary for MCP
callers. It lets MCP controllers run provider operations from trusted lifecycle
settings without building CLI `argv` or invoking `lifecycle.main()`.

## Code Commentary

### Logic

`ProviderLifecycleServiceConfig` carries the server-derived coordination root,
temporary lifecycle settings path, dry-run mode, timeout, and Python executable.
The service functions normalize those paths, build internal namespaces, and
dispatch to the provider lifecycle implementation functions:

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
- The dev/operator CLI facade is `lifecycle.py`; MCP provider tools should call
  this service layer instead of the CLI `main()` path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP provider tool controllers call this service layer. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| CLI/operator implementation functions remain behind the lifecycle facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| Tests verify service calls do not route through `lifecycle.main()`. | [test_tools.py](agents-remember-md/mcp/tests/test_tools.py) |

## Update History

- 2026-05-25T19:16+02:00: Updated after the `provider_lifecycle.py` compatibility shim was deleted and service imports wired to `providers.lifecycle` directly.
- 2026-05-23T20:56+02:00: Created for F-04 so MCP provider tools call a typed lifecycle service instead of the provider lifecycle CLI main.
