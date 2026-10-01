# mcp/src/agents_remember/serving/codex_mcp_readiness.py

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

## Evidence

### Docs References

No Domain Documentation source is configured. The native app-server response consumed by this module
is the runtime authority for the current client.

- Readiness depends on the current app-server's complete MCP status inventory. [1]

### Repo-Internal References

The Codex adapter is the sole consumer of this gate for role launches; roleless sessions retain their
existing startup path.

- Connected exact-tool evidence is returned as one typed result. [2]
- Server status and tool maps are parsed centrally and fail on malformed shape. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

- The readiness gate receives the in-process Codex transport abstraction instead of starting a second client. [4]
