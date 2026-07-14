# claude_stream_startup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_startup.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Negotiates startup through structured initialize, system/init, and synthetic no-query frames.

## Code Commentary
Validates vendor identity, cwd, exact version, and capabilities; timeout bounds startup but never substitutes for readiness.

## Invariants And Boundaries
No pane, prompt, log, or timing fallback; only pinned 2.1.207 can become ready.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Called by adapter facade. | `L1-L25` | [harness_control_claude.py](harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
