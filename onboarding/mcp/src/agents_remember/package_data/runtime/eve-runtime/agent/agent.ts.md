# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/agent.ts

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/agent.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime` target). Edit
`eve_runtime/agent/agent.ts` and re-run the generator; the read-only `--check` is the only currency
proof.

## Code Commentary

### The application entry eve launches, and the file the probe measures

This is the authored eve application's entry point: it defines the agent, its instructions
(`instructions.md` plus the `instructions/` modules) and its tool surface (`tools/`), and it is what
`install_eve_application` copies into `<coordination_root>/runtime/eve-agent` so a launch resolves a
real application instead of nothing.

It is also **one of the two files the `packaged-eve-application` capability probe reads** (with
`package.json`), which is why the mirror must equal the authored tree byte for byte rather than
merely resemble it: the live-eve readiness probe measures the `agent.ts` of the runtime root it
points at, so a staged copy that drifted from the authored source would be probed as if it were the
authored one. Byte identity between `eve_runtime/` and this mirror is what that rule requires.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/agent.ts` is the authored source.
- The mirror must be byte-identical to the authored tree for the runtime probe to mean anything.
- The packaged path of this mirror (`runtime/eve-runtime`) is deliberately not the launch path's
  packaged probe path (`runtime/eve-agent`), so a source checkout keeps resolving its own
  `eve_runtime/`.

## Evidence

### Repo-Internal References

- The packaged-application probe reads this file together with `package.json`. [1]
- The installed application root is `<coordination_root>/runtime/eve-agent`, reached through `AR_EVE_RUNTIME_ROOT`. [2]
- The generator declares the `eve-runtime` target with its per-target ignore set. [3]
