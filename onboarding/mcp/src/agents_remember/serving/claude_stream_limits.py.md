# claude_stream_limits.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_limits.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Immutable positive bounds for startup, acceptance, retained correlation history, and event queues.

## Code Commentary
`ClaudeAdapterLimits` validates external-process and bounded-resource settings; limits are never semantic
or readiness fallbacks.

## Invariants And Boundaries
Keep bounds explicit and reject non-positive values.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Consumed by the adapter facade. | `L1-L22` | [harness_control_claude.py](harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
