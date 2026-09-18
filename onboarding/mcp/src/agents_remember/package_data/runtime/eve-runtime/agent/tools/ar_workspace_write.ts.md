# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/tools/ar_workspace_write.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/tools/ar_workspace_write.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/tools/ar_workspace_write.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's write tool

One of the AR-owned eve application's own tools: the write half of the application's workspace
access. It travels with the application into `<coordination_root>/runtime/eve-agent`. It confers no
authority of its own — commit, closeout and integration authority stay with the MCP-owned
transaction tools.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/tools/ar_workspace_write.ts` is the
  authored source.
- Application tool only: it does not commit, integrate or close out anything.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registered install/skill tools in the server's own registration module; closeout and integration are transaction-owned elsewhere, not by an application write helper. | `_register_installation_tools` | mcp/src/agents_remember/mcp/registration/core.py:123-165 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
