# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-binding.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-binding.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch path compiles the capsule and supplies it through the harness's own carrier. | `compile_launch_capsule` | mcp/src/agents_remember/serving/launch_capsule.py:1-60 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
