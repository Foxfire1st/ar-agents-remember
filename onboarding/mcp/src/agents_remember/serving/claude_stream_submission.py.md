# claude_stream_submission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_submission.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Stores compact per-request correlation and terminal state for reconciliation.

## Code Commentary
Preserves identity and transition evidence when replay/disconnect ordering makes immediate certainty impossible.

## Invariants And Boundaries
Records are evidence, not resend authorization; whole-message order and ambiguity are preserved.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Reduced by stream state. | `L1-L30` | [claude_stream_state.py](claude_stream_state.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
