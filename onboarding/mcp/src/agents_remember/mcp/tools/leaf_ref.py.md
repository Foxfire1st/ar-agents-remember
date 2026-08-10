# mcp/src/agents_remember/mcp/tools/leaf_ref.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/mcp/tools/leaf_ref.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-07T20:50+02:00                          |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded`      |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[mcp/tools overview](overview.md)

## Purpose

`leaf_ref.py` contains MCP-tool response helpers for leaf-ref validation refusals. It keeps shared
`leaf-ref-not-found` / `leaf-ref-ambiguous` payload construction out of the already-large terminal tool
module.

## Code Commentary

`leaf_ref_refusal_payload(operation, leaf_key, error, kind=None)` maps a `LeafRefResolutionError` into
the strict `_tool_payload` envelope with `ok: false`, the resolver status, original requested `leafKey`,
and human-readable `detail` naming the expected form and candidates. Spawn refusals also echo the requested
session `kind` when it is one of the modeled values.

## Invariants And Boundaries

- This module has no resolver policy; it only adapts resolver errors to strict MCP payloads.
- Refusals are normal tool responses, not exceptions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared resolver error facts. | `LeafRefStatus`; `LeafRefResolutionError` | mcp/src/agents_remember/worktrees/leaf_refs.py:30-30; mcp/src/agents_remember/worktrees/leaf_refs.py:45-72 |
| `terminal.py` imports `LeafRefStatus` and declares the `LeafAssignmentStatus` and `SpawnAgentSessionStatus` aliases. | "LeafAssignmentStatus = Literal["; "SpawnAgentSessionStatus = Literal["; "from agents_remember.worktrees.leaf_refs import LeafRefStatus" | mcp/src/agents_remember/models/terminal.py:8-8; mcp/src/agents_remember/models/terminal.py:21-21; mcp/src/agents_remember/models/terminal.py:47-47 |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: rebound resolver and strict-model references;
  narrowed the terminal row to its import and alias declarations and deleted the unsupported
  terminal-consumer row because no consumer/import exists.

- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created as the strict MCP payload adapter for leaf-ref
  validation refusals. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
