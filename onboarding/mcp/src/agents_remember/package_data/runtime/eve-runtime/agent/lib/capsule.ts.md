# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/capsule.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/lib/capsule.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime` target).
Edit the authored file and re-run the generator.

## Code Commentary

### Application-side capsule helper

A library helper of the AR-owned eve application, used by the application's instruction modules. It
is application code, not the capsule compiler and not the corpus: the compiler is
`application/role_capsules`, its corpus is `packaged_source_root()/runtime/skills`, and the launch
supplies the compiled capsule through the harness's own carrier.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/lib/capsule.ts` is the authored source.
- No corpus ownership and no compilation duty on the application side.

## Evidence

### Repo-Internal References

- The compiler owns capsule compilation and resolves its corpus from the packaged skills tree. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
