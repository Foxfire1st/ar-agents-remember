# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-capsule.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions/ar-capsule.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's capsule-facing instruction module

This module is the application side of the capsule path: it is where the eve application consumes the
capsule material the launch supplies. It is **not** the capsule compiler and **not** the canonical
corpus — the compiler lives in `application/role_capsules` and resolves its corpus from
`packaged_source_root()/runtime/skills`, and the launch supplies the compiled capsule through the
harness's own carrier.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions/ar-capsule.ts` is the
  authored source.
- Application-side consumer only: it neither compiles the capsule nor owns the instruction corpus.

## Evidence

### Repo-Internal References

- The compiler resolves its corpus from the packaged skills tree. [1]
- The launch path compiles the capsule and supplies it through the harness's own carrier. [2]
- The generator declares the `eve-runtime` target with its per-target ignore set. [3]
