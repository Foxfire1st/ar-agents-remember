# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-binding.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions/ar-binding.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The admitted-binding instruction module

This module supplies the application-side instruction material for the admitted AR binding the
launch hands the eve session. It travels with the application into
`<coordination_root>/runtime/eve-agent` and is separate from the capsule carrier: the capsule is
compiled and supplied by the launch path (`serving/launch_capsule.py`), while this file belongs to
the application image.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions/ar-binding.ts` is the
  authored source.
- Application-side instruction material only; it does not compile, carry or decide the capsule.

## Evidence

### Repo-Internal References

- The launch path compiles the capsule and supplies it through the harness's own carrier. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
