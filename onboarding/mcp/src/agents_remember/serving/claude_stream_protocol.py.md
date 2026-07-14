# claude_stream_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_protocol.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Encodes and parses the exact Claude Code 2.1.207 stream-json protocol.

## Code Commentary
Builds launch flags, validates initialization and capabilities, and extracts safe terminal metadata. A
`success` subtype with `is_error=true` and API 429 remains failed; result text and credentials are not retained.

## Invariants And Boundaries
Protocol pin and structured evidence are exact; no pane/log/timing fallback. `/cost` is a local advertised command.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| 429 normalization regression. | `L1-L40` | [test_harness_control_claude.py](../../../tests/test_harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
