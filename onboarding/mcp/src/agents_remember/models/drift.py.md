# mcp/src/agents_remember/models/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/drift.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`drift.py` defines the compact drift summary embedded in `ContextPacketV2`.

## Code Commentary

`DriftSummary` is strict and exposes whether drift was checked, optional total
and actionable counts, an optional report path, and a bounded actionable sample.

## Invariants And Boundaries

- Context-packet drift is a summary, not the full drift report.
- Full memory quality workflows stay under the memory quality tools and reports.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packet construction validates drift output through this model. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for the context-packet drift summary model.
