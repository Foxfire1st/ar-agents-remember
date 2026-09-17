# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/agent.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/agent.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../overview.md`            |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged-application probe reads this file together with `package.json`. | `probe_capabilities` | mcp/src/agents_remember/install/experiment.py:479-566 |
| The installed application root is `<coordination_root>/runtime/eve-agent`, reached through `AR_EVE_RUNTIME_ROOT`. | `install_eve_application`; `resolve_runtime_root` | mcp/src/agents_remember/install/runtime.py:537-563; mcp/src/agents_remember/serving/eve_runtime_launch.py:168-203 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The leaf's second sync regenerated it after L17 changed the authored
  `agent.ts` (the eve effort consumer), so the bytes at this tip are L17's authored content through
  this leaf's generator; the card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
