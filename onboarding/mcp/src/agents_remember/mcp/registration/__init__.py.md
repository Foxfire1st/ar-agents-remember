# mcp/src/agents_remember/mcp/registration/__init__.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/__init__.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-31T15:31+02:00                                       |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                   |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## Purpose

The package door for the MCP tool surface. It declares the one registrar signature every family
module is called with and the ordered tuple `create_server` loops over.

## Code Commentary

### Logic

Two public names:

- `ToolRegistrar = Callable[[FastMCP, McpRuntimeConfig], None]` — the shape of a family module's
  `register_*_tools`.
- `TOOL_REGISTRARS: tuple[ToolRegistrar, ...]` — the twelve registrars in advertise order: core,
  sessions, memory, providers, code_search, worktrees, closeout, tasks, benchmarks, lifecycle,
  gates, orchestration.

`__all__` exports both. The module docstring states the division this package exists to enforce:
`create_server` owns process wiring (the compact-content shim, the ambient lifecycle, the `FastMCP`
instance) and nothing else; every `@server.tool()` definition lives in a family module here.

### Invariants And Boundaries

- Adding a tool means editing one family module. Adding a family means a new module plus one entry
  in this tuple — `create_server` should never grow a special case.
- The tuple's order is the order the server advertises tools in. `mcp/tools/base.py::PUBLIC_TOOLS`
  is the authority on the advertised name set; `mcp/tests/test_tools.py` compares it against a live
  server's `list_tools()` and against `server_info`'s exact list.
- Importing this package imports every family module, which imports every payload builder. Keep it
  free of side effects beyond those imports.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The only consumer: `create_server` iterates `TOOL_REGISTRARS`. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The advertised tool-name list the registrars must produce. | [tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. Records `TOOL_REGISTRARS`
  as the single place that decides which families a server advertises. Verification metadata pinned
  to the pre-change commit until closeout stamps the L2 code commit.
