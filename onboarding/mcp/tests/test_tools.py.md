# test_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_tools.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_tools.py` verifies public MCP tool payloads and server registration
behavior.

## Code Commentary

### Logic

The tests cover ping and server info payloads, FastMCP server construction,
context-packet delegation, runtime install payload authority, the Phase 04 tool
surface, Codex benchmark executable resolution through `PATH`, benchmark-only
Codex execution policy reporting, skills install copy-only behavior,
replacement of legacy symlink/junction-style skill
installations, Codex `.codex` harness-root inference, configured
harness-root requirements, memory init behavior,
route index refresh behavior, memory quality check exposure, and provider/tool
payload delegation.

The CGC assertions verify that the generic `cgc_query` name stays absent from
`PUBLIC_TOOLS`, and that typed CGC payloads build fixed native command suffixes
for symbol search, callers, callees, dependencies, and complexity.

The typed CGC payload test also patches `lifecycle.main()` to fail if
the MCP provider path regresses from `lifecycle_service` back to CLI capture.
Command-style artifact coverage verifies service-backed MCP tools do not expose
`argv`, `stdout`, `stderr`, or parsed `payload` wrapper fields.

Provider operation integrity coverage creates a provider runner file without a
manifest and asserts CGC query and watcher-start payloads return
`runnerIntegrityFailed` before lifecycle settings are written or lifecycle
services execute. The integrity coverage now uses a CodeGraphContext venv file
for the blocking case and separately asserts that current or historically
recorded `providers/_bin` entries are ignored when `grepai-memory` is
Docker-owned.

### Invariants And Boundaries

The public tool surface should remain typed and package-owned. Tests should not
permit arbitrary executable selection for benchmarks, arbitrary skill install
roots, raw shell wrappers, or reintroduced script-era tool names.

Codex benchmark tests should protect both failure recovery and policy
visibility: missing-Codex payloads should name `PATH` resolution and include
the benchmark-only execution policy, including whether the sandbox argument is
passed or omitted for `default` mode.

CGC tests should check fixed command construction rather than broad native
argument forwarding.

Provider MCP tests should protect that provider lifecycle calls use the typed
service layer, not `main(argv)`.

Provider MCP tests should also protect that runner-integrity failures block
provider operations before lifecycle execution, while legacy `_bin` artifacts do
not block Docker-mode `grepai-memory`.

Service-backed MCP tool tests should protect stable domain payloads rather than
command-capture response wrappers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public tool metadata and payload builders live in `tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Server registration lives in `server.py`. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Controller facades convert public MCP payloads into service calls. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider runner integrity now ignores legacy `_bin` entries while still watching non-Docker runner files. | [integrity.py](agents-remember-md/mcp/src/agents_remember/providers/integrity.py) |

## Update History

- 2026-05-25T19:16+02:00: Updated after service tests patched `providers.lifecycle.main` directly and the `provider_lifecycle.py` compatibility module was deleted.
- 2026-05-25T18:07+02:00: Updated after provider integrity removed `_bin` from current runner authority and kept old `_bin` manifest entries ignored.
- 2026-05-25T17:40+02:00: Updated after provider integrity tests switched the blocking case to CGC runner state and added Docker-mode legacy GrepAI binary/current-manifest ignore coverage.
- 2026-05-24T19:25+02:00: Added regression coverage that provider runner integrity failures block CGC query and watcher execution before lifecycle services run.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` covered `.codex` skill roots and benchmark sandbox payloads.
- 2026-05-24T09:23+02:00: Updated after MCP tool tests moved normal harness-root fixtures from `.agents` to Codex `.codex`.
- 2026-05-24T08:56+02:00: Updated after missing-Codex benchmark payload coverage began asserting `sandboxArgument` for fixed and default sandbox modes.
- 2026-05-24T06:57+02:00: Updated after missing-Codex benchmark payload tests began asserting explicit benchmark-only `PATH` resolution policy.
- 2026-05-24T02:47+02:00: Updated after public tool expectations added `memory_quality_check`.
- 2026-05-24T00:35+02:00: Added regression coverage that service-backed MCP tools no longer expose command-capture artifacts.
- 2026-05-23T20:56+02:00: Added regression coverage that MCP provider tools do not route through the provider lifecycle CLI main.
- 2026-05-23T20:42+02:00: Added typed CGC public-tool and fixed command-shape coverage.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for public MCP tool test coverage.
