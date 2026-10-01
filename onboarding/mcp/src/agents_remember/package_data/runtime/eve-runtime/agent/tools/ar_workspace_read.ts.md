# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/tools/ar_workspace_read.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/tools/ar_workspace_read.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's read tool

One of the AR-owned eve application's own tools: the read half of the application's workspace access.
It travels with the application into `<coordination_root>/runtime/eve-agent` and is independent of
the MCP tool surface — the MCP tools belong to the server, not to this application image.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/tools/ar_workspace_read.ts` is the
  authored source.
- Application tool only; the MCP tool surface is owned and registered by the server.

## Evidence

### Repo-Internal References

- The MCP tool surface is registered by the server's own registration modules. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
