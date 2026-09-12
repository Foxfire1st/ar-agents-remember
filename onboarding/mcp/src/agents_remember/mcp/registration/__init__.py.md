# mcp/src/agents_remember/mcp/registration/__init__.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/__init__.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-09-12T22:55+02:00                                       |
| lastVerifiedCommitHash | `5a7bd5779935d1a7e24e978b52638edfd300ac4d`                   |
| lastVerifiedCommitDate | 2026-09-12T23:26:17+02:00|
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
- The tuple's order is the order the server advertises tools in. `PUBLIC_TOOLS`
  (defined at `mcp/src/agents_remember/models/tools/public_roster.py:22-85`, re-exported by
  `mcp/tools/base.py`)
  is the authority on the advertised name set; `mcp/tests/test_tools.py` compares it against a live
  server's `list_tools()` and against `server_info`'s exact list.
- Importing this package imports every family module, which imports every payload builder. Keep it
  free of side effects beyond those imports.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `create_server` consumer iterates `TOOL_REGISTRARS`. | `create_server` | mcp/src/agents_remember/mcp/server.py:58-70 |
| The advertised tool-name list's one definition, re-exported unchanged by the adapter. | "PUBLIC_TOOLS = ("; "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/models/tools/public_roster.py:22-22; mcp/src/agents_remember/mcp/tools/base.py:19-19 |

## Update History

- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: renamed the roster's home. `PUBLIC_TOOLS` is no
  longer declared in `mcp/tools/base.py`; its one definition is the zero-import leaf
  `models/tools/public_roster.py:22-85`, which the adapter re-exports unchanged (same object, same
  order, same 62 names), so this package's exact-order comparison is unaffected. Repointed the
  invariant prose and the reference row; no behavioral claim changed. Verification metadata remains
  closeout-owned; no acceptance claim.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. Records `TOOL_REGISTRARS`
  as the single place that decides which families a server advertises. Verification metadata pinned
  to the pre-change commit until closeout stamps the L2 code commit.
