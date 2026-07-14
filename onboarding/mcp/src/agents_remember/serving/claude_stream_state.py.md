# claude_stream_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_state.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Reduces Claude frames into normalized snapshots, transcripts, interactions, receipts, and terminal outcomes.

## Code Commentary
Maintains bounded correlation history, separates replay acceptance from result completion, routes permissions
and questions, and reconciles late frames without resend. API-429 frames remain failed with safe metadata.

## Invariants And Boundaries
Disconnected sessions are reconciliation-only; no new writes, automatic resend, or sensitive diagnostic retention.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| State is hosted by the adapter. | `L1-L35` | [harness_control_claude.py](harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
