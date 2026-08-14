# claude_stream_limits.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_limits.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-11T15:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
| Finding | Anchor | Source |
| --- | --- | --- |
| Consumed by the adapter facade. | "from agents_remember.serving.claude_stream_limits import ClaudeAdapterLimits"; "limits: ClaudeAdapterLimits" | mcp/src/agents_remember/serving/harness_control_claude.py:22-22; mcp/src/agents_remember/serving/harness_control_claude.py:147-163 |

## Update History

- 2026-08-11T15:20+02:00 — Replaced the multiply occurring type-name anchor with the exact import
  and constructor parameter that consume the limits object.
- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 1 citation row: the adapter facade consumption (harness_control_claude.py import L13 and `ClaudeStreamJsonAdapter.__init__` L145-L160, anchor `ClaudeAdapterLimits`). Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
