# mcp/src/agents_remember/mcp/tools/leaf_ref.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/mcp/tools/leaf_ref.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-07T20:50+02:00                          |
| lastVerifiedCommitHash | `52911a15091de8d065afc6cbc0f8d6ac34690039`      |
| lastVerifiedCommitDate | 2026-07-07T22:29:35+02:00|
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

| Finding | Source Path |
| --- | --- |
| Shared resolver error facts. | [../../worktrees/leaf_refs.py](../../worktrees/leaf_refs.py.md) |
| Terminal payload builders using the helper. | [terminal.py](terminal.py.md) |
| Strict response models accepting the leaf-ref refusal statuses. | [../../models/terminal.py](../../models/terminal.py.md) |

## Update History

- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created as the strict MCP payload adapter for leaf-ref
  validation refusals. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
