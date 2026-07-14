# claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_transport.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Provides bounded stdio subprocess transport and exact version probing for Claude Code.

## Code Commentary
Starts stream-json, reads frames, drains/discards stderr, probes `--version`, and force-cleans blocked readers.

## Invariants And Boundaries
Process bounds prevent hangs/deadlocks but never infer readiness or terminal meaning; sensitive process output is not retained.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Transport lifecycle. | `L1-L30` | [harness_control_claude.py](harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
