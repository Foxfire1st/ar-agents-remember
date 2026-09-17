# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/workspace.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/workspace.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/lib/workspace.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### Application-side workspace helper

A library helper of the AR-owned eve application that locates the agent's workspace for the
application's tools. It is application code inside the installed image
(`<coordination_root>/runtime/eve-agent`); the admitted workspace address remains the launch's and
the control plane's, not an application-side invention.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/lib/workspace.ts` is the authored source.
- Helper only: the admitted workspace address stays launch- and control-plane-owned.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch records the admitted workspace and seat rather than letting a consumer re-derive them. | `compile_launch_capsule` | mcp/src/agents_remember/serving/launch_capsule.py:1-60 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
