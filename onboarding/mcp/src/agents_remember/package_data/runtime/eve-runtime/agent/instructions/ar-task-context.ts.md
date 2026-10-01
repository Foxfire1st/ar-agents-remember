# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-task-context.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions/ar-task-context.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The seat's task-context instruction module

This module supplies the application-side task-context material for a running seat. It travels with
the application image into `<coordination_root>/runtime/eve-agent`; it is not a second copy of the
task document, and the durable task surface remains the JSON-primary task document the control plane
owns.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions/ar-task-context.ts` is the
  authored source.
- Instruction material for the seat, not task-document authority.

## Evidence

### Repo-Internal References

- The task document is the JSON-primary authoring surface; instruction material does not replace it. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
