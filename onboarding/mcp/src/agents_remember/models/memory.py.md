# mcp/src/agents_remember/models/memory.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/memory.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:00+02:00                     |
| lastVerifiedCommitHash | `9b25740b5b373b410c270e14913f5a220c63c795` |
| lastVerifiedCommitDate | 2026-06-10T02:38:07+02:00|
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

- 2026-06-10T09:00+02:00 — Carryover plan/apply models gained documented optional `decisions`/`reportPath` (plus `carriedPaths` on apply) for the 2.5.2 response compaction (GitHub #52).
- 2026-05-28T19:52+02:00: Created for memory and onboarding response contracts.
