# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/channels/eve.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/channels/eve.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/channels/eve.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's channel binding

This module binds the AR-owned eve application's channel surface. It is part of the application the
`install_eve_application` step copies into `<coordination_root>/runtime/eve-agent`, and it is not on
the instruction-delivery path the cutover changes: withholding the coordinator `AGENTS.md` chain
leaves this file untouched, and installing the application never delivers the capsule corpus.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/channels/eve.ts` is the authored source.
- The AR agent controls eve exclusively through eve's documented HTTP session protocol; nothing in
  this application reimplements eve's tool loop, compaction engine or session store.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application's own README states the HTTP-session-protocol boundary and the exact dependency pins. | `# Agents Remember eve runtime` | eve_runtime/README.md:1-40 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
