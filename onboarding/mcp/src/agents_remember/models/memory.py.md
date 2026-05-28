# mcp/src/agents_remember/models/memory.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/memory.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`memory.py` defines response models for drift, memory quality, route index,
memory initialization, baseline, and carryover MCP tools.

## Code Commentary

`DriftCheckResponse` is strict because drift summaries have a stable status,
count, report, and actionable-sample shape. Memory quality, route index,
initialization, baseline, and carryover responses use flexible tool envelopes
because their underlying service payloads still carry operation-specific
details.

## Invariants And Boundaries

- Drift status is constrained to checked/not-checked/error tool states.
- Flexible memory-service responses should still include the public operation
  name and shared token metadata.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory MCP controllers route these tools to drift, quality, route-index, init, baseline, and carryover services. | [memory_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/memory_tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for memory and onboarding response contracts.
