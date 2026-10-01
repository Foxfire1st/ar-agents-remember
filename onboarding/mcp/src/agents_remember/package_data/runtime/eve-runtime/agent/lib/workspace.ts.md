# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/workspace.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/lib/workspace.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### Application-side workspace helper

A library helper of the AR-owned eve application that locates the agent's workspace for the
application's tools. It is application code inside the installed image
(`<coordination_root>/runtime/eve-agent`); the admitted workspace address remains the launch's and
the control plane's, not an application-side invention.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/lib/workspace.ts` is the authored source.
- Helper only: the admitted workspace address stays launch- and control-plane-owned.

## Evidence

### Repo-Internal References

- The launch records the admitted workspace and seat rather than letting a consumer re-derive them. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
