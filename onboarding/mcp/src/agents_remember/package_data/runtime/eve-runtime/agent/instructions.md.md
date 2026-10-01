# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions.md

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions.md`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### The eve application's own instruction entry

This is the top-level instruction document of the AR-owned eve application — the text the agent
definition loads — and it is distinct from, and not a substitute for, the **capsule** instruction
corpus the compiler delivers. The capsule corpus is resolved by
`application/skill_resources` from `packaged_source_root()/runtime/skills`; this file belongs to the
eve application and travels with it into `<coordination_root>/runtime/eve-agent`.

The distinction matters for the cutover: withholding the legacy coordinator `AGENTS.md` chain does
not touch this file, and installing the eve application does not deliver the capsule corpus.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions.md` is the authored source.
- It is the eve application's instruction entry, not the capsule corpus and not a legacy startup
  target.

## Evidence

### Repo-Internal References

- The compiler resolves its corpus from the packaged skills tree, not from this application's instructions. [1]
- The startup targets the capsule mode withholds are the coordinator `AGENTS.md` chain, not this file. [2]
- The generator declares the `eve-runtime` target with its per-target ignore set. [3]
