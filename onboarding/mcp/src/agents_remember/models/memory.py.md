# mcp/src/agents_remember/models/memory.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/memory.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`memory.py` defines response models for drift, memory quality, route index,
memory initialization, baseline, and carryover MCP tools.

## Code Commentary

`DriftCheckResponse` is strict because drift summaries have a stable status,
count, report, and actionable-sample shape. Memory quality, route index,
initialization, baseline, and carryover responses use flexible tool envelopes
because their underlying service payloads still carry operation-specific
details. The carryover models document the 2.5.2 compact wire shape: both
declare optional `decisions` (source paths grouped by carryover decision) and
`reportPath` (the temp report holding the full candidate records), and the
apply model adds `carriedPaths` (paths whose onboarding actually carried).

## Invariants And Boundaries

- Drift status is constrained to checked/not-checked/error tool states.
- Flexible memory-service responses should still include the public operation
  name and shared token metadata.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory MCP controllers route these tools to drift, quality, route-index, init, baseline, and carryover services. | [memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/models/memory.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T09:00+02:00 — Carryover plan/apply models gained documented optional `decisions`/`reportPath` (plus `carriedPaths` on apply) for the 2.5.2 response compaction (GitHub #52).
- 2026-05-28T19:52+02:00: Created for memory and onboarding response contracts.
