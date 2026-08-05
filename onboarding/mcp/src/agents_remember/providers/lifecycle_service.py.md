# mcp/src/agents_remember/providers/lifecycle_service.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_service.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../overview.md`                     |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP provider tool application entry points call this service layer. | ["from agents_remember.providers import lifecycle_service"] | mcp/src/agents_remember/application/provider_tools.py:18-18 |
| CLI/operator implementation functions remain behind the lifecycle facade. | `_EXPORT_MODULES`, `__getattr__` | mcp/src/agents_remember/providers/lifecycle/__init__.py:9-24; mcp/src/agents_remember/providers/lifecycle/__init__.py:27-34 |
| Tests verify service calls do not route through `lifecycle.main()`. | `test_typed_cgc_payloads_build_fixed_native_commands` | mcp/tests/test_tools.py:581-661 |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 3 repository-internal application, facade, and service-boundary test references; final scoped result 0 (checker-clean).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `run_cgc_lifecycle` was re-signed from five keywords to `(service_config, request:
  CgcLifecycleRequest)`. The supported actions, the refusal and the returned payload are unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-26T12:51+02:00: Updated after removing the CGC provider Python executable from the typed service config.
- 2026-05-25T19:16+02:00: Updated after the `provider_lifecycle.py` compatibility shim was deleted and service imports wired to `providers.lifecycle` directly.
- 2026-05-23T20:56+02:00: Created for F-04 so MCP provider tools call a typed lifecycle service instead of the provider lifecycle CLI main.
