# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
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
