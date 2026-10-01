# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/tools/ar_workspace_write.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/tools/ar_workspace_write.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's write tool

One of the AR-owned eve application's own tools: the write half of the application's workspace
access. It travels with the application into `<coordination_root>/runtime/eve-agent`. It confers no
authority of its own — commit, closeout and integration authority stay with the MCP-owned
transaction tools.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/tools/ar_workspace_write.ts` is the
  authored source.
- Application tool only: it does not commit, integrate or close out anything.

## Evidence

### Repo-Internal References

- The registered install/skill tools in the server's own registration module; closeout and integration are transaction-owned elsewhere, not by an application write helper. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
