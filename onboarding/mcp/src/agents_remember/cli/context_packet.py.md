# mcp/src/agents_remember/cli/context_packet.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/context_packet.py` is the JSON-only CLI adapter for the context packet
application entry point: it parses arguments, loads trusted MCP settings, calls
`build_context_packet`, and prints the packet (or an `ok:false` error object)
as JSON.

## Code Commentary

### Logic

`main(argv)` requires `--config` (trusted MCP settings JSON) and `--repo`
(repository id from those settings), with `--skip-providers`,
`--include-drift`, `--include-freshness` (issue #54: requests the branch
freshness section, which fetches remote-tracking refs), `--provider-detail-limit`,
`--drift-detail-limit`, and `--fetch-timeout` shaping the
`ContextPacketRequest`. `ConfigError`/`ContextPacketError`/`ValueError` become
a single-line `{"ok": false, ...}` JSON with exit code 1; success prints the
indented packet and returns 0.

### Conventions

Thin adapter: no behavior beyond argument-to-request mapping and JSON output.
Flag surface mirrors the MCP `context_packet` tool registration.

### Invariants And Boundaries

- Keep the flag set in lockstep with `ContextPacketRequest` and the MCP tool
  registration; the CLI must not grow behavior the application entry point does not own.

### Todos

No file-local todos.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No relevant external documentation found.

### Repo-Internal References

- The application entry point that builds the printed packet and owns request semantics. [1]
- CLI JSON output is covered by the context packet tests. [2]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
