# test_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_tools.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T18:05+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_tools.py` verifies public MCP tool payloads and server registration
behavior.

## Code Commentary

### Logic

The tests cover ping and server info payloads, FastMCP server construction,
context-packet delegation, runtime install payload authority, the Phase 04 tool
surface, Codex benchmark executable resolution through `PATH`, skills install
copy-only behavior, replacement of legacy symlink/junction-style skill
installations, configured harness-root requirements, memory init behavior,
route index refresh behavior, and provider/tool payload delegation.

### Invariants And Boundaries

The public tool surface should remain typed and package-owned. Tests should not
permit arbitrary executable selection for benchmarks, arbitrary skill install
roots, raw shell wrappers, or reintroduced script-era tool names.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public tool metadata and payload builders live in `tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Server registration lives in `server.py`. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |

## Update History

- 2026-05-23T18:05+02:00: Created during direct closeout prep for public MCP tool test coverage.
