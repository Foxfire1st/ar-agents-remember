# claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_transport.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
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

### 260713-PHA-L6 Boundary

Transport startup and framing remain strict and bounded. Compatibility validation belongs to the
correlated structured protocol messages, not a separate CLI version subprocess or pane/log
fallback.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented that production startup no longer performs an
  exact CLI-version preflight; the transport remains the structured stream boundary.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
