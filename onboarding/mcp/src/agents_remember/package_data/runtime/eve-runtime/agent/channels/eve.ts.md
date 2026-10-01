# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/channels/eve.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/channels/eve.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's channel binding

This module binds the AR-owned eve application's channel surface. It is part of the application the
`install_eve_application` step copies into `<coordination_root>/runtime/eve-agent`, and it is not on
the instruction-delivery path the cutover changes: withholding the coordinator `AGENTS.md` chain
leaves this file untouched, and installing the application never delivers the capsule corpus.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/channels/eve.ts` is the authored source.
- The AR agent controls eve exclusively through eve's documented HTTP session protocol; nothing in
  this application reimplements eve's tool loop, compaction engine or session store.

## Evidence

### Repo-Internal References

- The application's own README states the HTTP-session-protocol boundary and the exact dependency pins. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
