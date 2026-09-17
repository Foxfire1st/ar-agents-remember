# mcp/src/agents_remember/package_data/runtime/eve-runtime/README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/README.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |
| The installed application root is `<coordination_root>/runtime/eve-agent`, reached through the documented override. | `install_eve_application`; `resolve_runtime_root` | mcp/src/agents_remember/install/runtime.py:537-563; mcp/src/agents_remember/serving/eve_runtime_launch.py:168-203 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged application
  mirror this leaf adds as a new `scripts/sync-runtime.py` target. The card records generated
  content, its authored source and the generator as the edit route. The leaf's second sync
  regenerated the mirror after L17 changed the authored `eve_runtime/agent/agent.ts`, so the bytes
  at this tip are L17's authored content through this leaf's generator. The verification metadata
  names the leaf base commit because the whole candidate (mirror included) is **uncommitted**; the
  real stamp is closeout-owned.
