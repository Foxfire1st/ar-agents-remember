# mcp/src/agents_remember/package_data/runtime/eve-runtime/package.json

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored `eve_runtime/package.json`,
produced by `scripts/sync-runtime.py` (the `eve-runtime` target). Edit `eve_runtime/package.json` and
re-run the generator; the read-only `--check` proves currency.

## Code Commentary

### Why this file is load-bearing rather than incidental

`package.json` is one of the two files `install/experiment.py` reads as the
`packaged-eve-application` capability: with `agent/agent.ts` it is what proves a packaged mirror is a
real application, and its dependency block is what the `pinned-eve-dependencies` probe compares
against `PINNED_DEPENDENCIES` (`eve 0.56.0`, `ai 7.0.102`, `@ai-sdk/openai-compatible 3.0.49`,
`zod 4.6.5`). Every dependency must stay **exact** — a range such as `"eve": "^0.56.0"` is reported
by name as a mismatch and **refuses the install before its first write**. The file also carries
`"private": true`, and nothing here publishes a package.

`install_eve_application` copies the mirror into `<coordination_root>/runtime/eve-agent`, and the
record the run returns carries `eveVersion` read from this file rather than from the product's own
output.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/package.json` is the authored source.
- The four dependency pins are exact versions with no ranges; a range is a refusal, not a warning.
- `node_modules/` is not committed and not part of the mirror.

## Evidence

### Repo-Internal References

- The pins this file is compared against, and the one-line install command recorded for the operator. [1]
- The packaged-application probe reads this file together with `agent/agent.ts`. [2]
- The generator declares the `eve-runtime` target with its per-target ignore set. [3]
