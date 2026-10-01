# mcp/src/agents_remember/package_data/runtime/eve-runtime/README.md

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

**Generated file — do not edit.** This is the package-owned copy of the authored
`eve_runtime/README.md`, produced by `scripts/sync-runtime.py` (the `eve-runtime` target) into
`mcp/src/agents_remember/package_data/runtime/eve-runtime/`. It tracks the authored tree byte for
byte; the read-only `--check` of the generator is its only currency proof, and the source edit
belongs in `eve_runtime/README.md` followed by the generator run.

The content is the pinned AR-owned eve application's own README: the dependency pins with no ranges
(`eve 0.56.0`, `ai 7.0.102`, `@ai-sdk/openai-compatible 3.0.49`, `zod 4.6.5`), the once-per-checkout
`npm install`, the Node 24 requirement with the adapter's nvm-then-PATH resolution and the
`AR_EVE_NODE` override, and the environment contract the adapter passes through.

## Code Commentary

### What it is, and how it reaches a runtime

The generator copies the authored `eve_runtime/` tree into this mirror; `install/runtime.py`'s
`install_eve_application` copies **this mirror** into `<coordination_root>/runtime/eve-agent`, which
the launch path reaches through the documented `AR_EVE_RUNTIME_ROOT` override. The mirror's own path
under `package_data/runtime/eve-runtime` is deliberately **not** the launch path's packaged probe
path (`package_data/runtime/eve-agent`): populating that probe path would make every source checkout
resolve the packaged copy ahead of `eve_runtime/` and find no installed dependencies.
`node_modules`, `.eve`, `.output` and `.vercel` are ignored **per target**, so no other canonical
runtime tree loses a same-named directory.

### Invariants And Boundaries

- Generated content, never hand-edited; the generator's `--check` is the currency proof.
- The authored source is `eve_runtime/README.md`; a content change starts there.
- `node_modules/` is not committed and is never part of the mirror.

## Evidence

### Repo-Internal References

- The generator declares the `eve-runtime` target with its per-target ignore set. [1]
- The installed application root is `<coordination_root>/runtime/eve-agent`, reached through the documented override. [2]
