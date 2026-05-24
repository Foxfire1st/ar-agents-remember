# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T10:06+02:00                     |
| lastVerifiedCommitHash | `f48a34619fbe37c405419acfa60580b95ed8812c` |
| lastVerifiedCommitDate | 2026-05-24T10:04:28+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`server.py` wires the stdio FastMCP server and registers the model-visible
Agents Remember tools.

## Code Commentary

### Logic

`create_server()` builds the FastMCP instance and registers typed tool functions
that delegate to payload builders. Phase 04 adds context, drift, route index,
memory init, skill install, provider, worktree, memory baseline/carryover, and
benchmark tools.

The registered `memory_quality_check` tool accepts a repo id plus optional
check names/detail limits and forwards them to the payload/controller layer. It
is the full closeout quality gate; task-start guidance continues to use
`drift_check` for the maintenance worklist.

The public CGC provider surface is typed at registration time. The server
registers `cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, and `cgc_complexity` instead of a generic `cgc_query`
endpoint.

`codex_benchmark_run` exposes an optional `codex_sandbox` argument with the
same default as the benchmark service. The server only forwards the value; the
runner validates it against its allowlist and maps `default` to an omitted
`--sandbox` CLI argument.

### Invariants And Boundaries

- Server functions should perform registration and argument forwarding only.
- Tool behavior and safety checks belong in payload builders/controllers.
- Do not add a raw shell or arbitrary command tool to this server.
- Do not turn benchmark sandbox selection into a generic Codex argument surface.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders are defined in `tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| The config loader rejects coordinator `system/settings.json` as MCP authority. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` exposed benchmark sandbox options through the MCP server.
- 2026-05-24T08:56+02:00: Updated after `codex_benchmark_run` registered the optional `codex_sandbox` forwarding argument.
- 2026-05-24T02:47+02:00: Updated after registering `memory_quality_check` as the closeout quality gate.
- 2026-05-23T20:42+02:00: Updated CGC registration from generic `cgc_query` to typed CGC tools.
- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
