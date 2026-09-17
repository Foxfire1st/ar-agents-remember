# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-task-context.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-task-context.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions/ar-task-context.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The seat's task-context instruction module

This module supplies the application-side task-context material for a running seat. It travels with
the application image into `<coordination_root>/runtime/eve-agent`; it is not a second copy of the
task document, and the durable task surface remains the JSON-primary task document the control plane
owns.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions/ar-task-context.ts` is the
  authored source.
- Instruction material for the seat, not task-document authority.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The task document is the JSON-primary authoring surface; instruction material does not replace it. | `runtime_install_payload` | mcp/src/agents_remember/mcp/tools/core.py:80-106 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
