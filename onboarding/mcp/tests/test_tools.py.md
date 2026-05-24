# test_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_tools.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00|
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
route index refresh behavior, memory quality check exposure, and provider/tool
payload delegation.

The CGC assertions verify that the generic `cgc_query` name stays absent from
`PUBLIC_TOOLS`, and that typed CGC payloads build fixed native command suffixes
for symbol search, callers, callees, dependencies, and complexity.

The typed CGC payload test also patches `provider_lifecycle.main()` to fail if
the MCP provider path regresses from `lifecycle_service` back to CLI capture.
Command-style artifact coverage verifies service-backed MCP tools do not expose
`argv`, `stdout`, `stderr`, or parsed `payload` wrapper fields.

### Invariants And Boundaries

The public tool surface should remain typed and package-owned. Tests should not
permit arbitrary executable selection for benchmarks, arbitrary skill install
roots, raw shell wrappers, or reintroduced script-era tool names.

CGC tests should check fixed command construction rather than broad native
argument forwarding.

Provider MCP tests should protect that provider lifecycle calls use the typed
service layer, not `main(argv)`.

Service-backed MCP tool tests should protect stable domain payloads rather than
command-capture response wrappers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public tool metadata and payload builders live in `tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Server registration lives in `server.py`. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Controller facades convert public MCP payloads into service calls. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-24T02:47+02:00: Updated after public tool expectations added `memory_quality_check`.
- 2026-05-24T00:35+02:00: Added regression coverage that service-backed MCP tools no longer expose command-capture artifacts.
- 2026-05-23T20:56+02:00: Added regression coverage that MCP provider tools do not route through `provider_lifecycle.main()`.
- 2026-05-23T20:42+02:00: Added typed CGC public-tool and fixed command-shape coverage.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for public MCP tool test coverage.
