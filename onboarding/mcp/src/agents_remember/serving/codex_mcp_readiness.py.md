# mcp/src/agents_remember/serving/codex_mcp_readiness.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_mcp_readiness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:29:54+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Provides the single bounded app-server MCP-readiness API used before a structurally spawned Codex
role seat is advertised as ready. It requires one connected configured server to advertise the exact
public `dispatch_agent` tool.

## Code Commentary

### Logic

`wait_for_codex_mcp_tool` validates its request, repeatedly reads the complete paginated
`mcpServerStatus/list` inventory, and returns typed server/tool evidence only for a connected match.
A settled inventory without the required tool refuses immediately; an unsettled inventory polls only
until its explicit deadline. Page, cursor, server, status, and tool shapes are validated centrally.

### Conventions

Timing dependencies travel in one immutable `CodexMcpReadinessTiming` value so deterministic tests can
substitute a clock without widening the production API. The stable result is a typed dataclass with a
small JSON projection for handshake evidence.

### Invariants And Boundaries

- Readiness is a role-seat startup gate, not a caller retry or compatibility fallback.
- Only `runtimeStatus == "connected"` plus the exact tool name admits the seat.
- Pagination is bounded; malformed or repeated cursors fail loudly.
- A settled absence and a timeout are distinct actionable errors with bounded inventory evidence.
- This API never searches alternate tool names, filenames, or transport surfaces.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The native app-server response consumed by this module
is the runtime authority for the current client.

| Finding | Anchor | Source |
| --- | --- | --- |
| Readiness depends on the current app-server's complete MCP status inventory. | `_read_server_statuses` | mcp/src/agents_remember/serving/codex_mcp_readiness.py:132-159 |

## Repo-Internal References

The Codex adapter is the sole consumer of this gate for role launches; roleless sessions retain their
existing startup path.

| Finding | Anchor | Source |
| --- | --- | --- |
| Connected exact-tool evidence is returned as one typed result. | `CodexMcpToolReadiness` | mcp/src/agents_remember/serving/codex_mcp_readiness.py:25-40; mcp/src/agents_remember/serving/codex_mcp_readiness.py:70-102 |
| Server status and tool maps are parsed centrally and fail on malformed shape. | `_server_status` | mcp/src/agents_remember/serving/codex_mcp_readiness.py:161-191 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| The readiness gate receives the in-process Codex transport abstraction instead of starting a second client. | `wait_for_codex_mcp_tool` | mcp/src/agents_remember/serving/codex_mcp_readiness.py:70-102 |

## Update History

- 2026-08-30T22:29:54+02:00 — 260821-ARSPAWN-L5 replaced an ambiguous type-name
  citation with the unique readiness-gate symbol.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created the canonical connected-`dispatch_agent` startup-readiness API. Verification metadata remains closeout-owned.
