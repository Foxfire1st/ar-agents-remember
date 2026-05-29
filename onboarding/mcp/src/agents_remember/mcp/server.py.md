# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T08:53+02:00                     |
| lastVerifiedCommitHash | `a06bfa65dcee3c8b82652085c69f2a20f163e306` |
| lastVerifiedCommitDate | 2026-05-29T09:05:12+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`server.py` wires the stdio FastMCP server and registers the model-visible
Agents Remember tools.

## Code Commentary

### Logic

`create_server()` first calls `install_compact_content()` (idempotent) so the
JSON text mirror of every tool result is emitted without FastMCP's hardcoded
indentation, then builds the FastMCP instance and registers typed tool functions
that delegate to payload builders. The current public surface includes context,
drift, route index, memory init, skill install, provider status, provider
diagnostics, provider watcher, GrepAI, CodeGraphContext, worktree, memory
baseline/carryover, and benchmark tools.

The registered `memory_quality_check` tool accepts a repo id plus optional
check names/detail limits and forwards them to the payload/controller layer. It
is the full closeout quality gate; task-start guidance continues to use
`drift_check` for the maintenance worklist.

The public CGC provider surface is typed at registration time. The server
registers `cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, and `cgc_complexity` instead of a generic `cgc_query`
endpoint.

The public GrepAI provider surface is typed at registration time as well.
`grepai_search` registers `repo_ids`, `all_repos`, `limit`, and
`output_format` around the required query, while `grepai_trace` registers
`trace_action`, `symbol`, optional repo scoping, optional graph depth, and
output format. The server only forwards these fields to the payload layer.

`codex_benchmark_run` exposes an optional `codex_sandbox` argument with the
same default as the benchmark service. The server only forwards the value; the
runner validates it against its allowlist and maps `default` to an omitted
`--sandbox` CLI argument.

`provider_diagnostics` is registered as the explicit detail tool for raw
provider state, keeping `context_packet` and `provider_status` focused on
compact readiness summaries.

### Invariants And Boundaries

- Server functions should perform registration and argument forwarding only.
- Tool behavior and safety checks belong in payload builders/controllers.
- `install_compact_content()` must run before tools are exercised; keep the call
  at the top of `create_server()`. It only affects text-mirror serialization, not
  `structuredContent` or tool behavior.
- Do not add a raw shell or arbitrary command tool to this server.
- Do not collapse GrepAI back into free-form query/native argument forwarding;
  the registration should mirror the supported MCP contract.
- Do not turn benchmark sandbox selection into a generic Codex argument surface.
- Keep detailed provider troubleshooting behind `provider_diagnostics`; do not
  hide raw provider internals in `context_packet`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders are defined in `tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Provider diagnostics payloads are modeled separately from compact provider summaries. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| The config loader rejects coordinator `system/settings.json` as MCP authority. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The compact-content shim installed at server creation minifies tool-result text. | [compact_content.py](agents-remember-md/mcp/src/agents_remember/mcp/compact_content.py) |

## Update History

- 2026-05-29T08:53+02:00: Updated after `create_server()` began installing the FastMCP compact-content shim to minify tool-result text mirrors.
- 2026-05-28T19:52+02:00: Updated after registering the dedicated `provider_diagnostics` MCP tool.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI search and trace registration.
- 2026-05-26T22:54+02:00: Updated after GrepAI search and trace registration gained typed scope, output, and trace-action arguments.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` exposed benchmark sandbox options through the MCP server.
- 2026-05-24T08:56+02:00: Updated after `codex_benchmark_run` registered the optional `codex_sandbox` forwarding argument.
- 2026-05-24T02:47+02:00: Updated after registering `memory_quality_check` as the closeout quality gate.
- 2026-05-23T20:42+02:00: Updated CGC registration from generic `cgc_query` to typed CGC tools.
- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
