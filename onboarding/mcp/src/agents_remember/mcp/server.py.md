# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T20:42+02:00                     |
| lastVerifiedCommitHash | `4ad9686b20334d36308a05d615bccde204b11d7e` |
| lastVerifiedCommitDate | 2026-05-23T21:18:05+02:00|
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

The public CGC provider surface is typed at registration time. The server
registers `cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, and `cgc_complexity` instead of a generic `cgc_query`
endpoint.

### Invariants And Boundaries

- Server functions should perform registration and argument forwarding only.
- Tool behavior and safety checks belong in payload builders/controllers.
- Do not add a raw shell or arbitrary command tool to this server.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders are defined in `tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| The config loader rejects coordinator `system/settings.json` as MCP authority. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
- 2026-05-23T20:42+02:00: Updated CGC registration from generic `cgc_query` to typed CGC tools.
