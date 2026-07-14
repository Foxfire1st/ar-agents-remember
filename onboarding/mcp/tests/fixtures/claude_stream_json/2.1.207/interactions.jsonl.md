# interactions.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.207/interactions.jsonl` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| governingOverview | `../../../overview.md` |

## Governing Overview
[tests overview](../../../overview.md)

## Purpose
Pinned permission and AskUserQuestion control-request frames.

## Code Commentary
Exercises correlated durable interaction routing without credentials or model content.

## Invariants And Boundaries
Fixtures are bounded protocol evidence and do not authorize automatic responses.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Fixture consumer. | `L1-L10` | [test_harness_control_claude.py](../../../../test_harness_control_claude.py) |

## Update History
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
