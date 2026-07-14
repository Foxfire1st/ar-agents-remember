# initialization.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.207/initialization.jsonl` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| governingOverview | `../../../overview.md` |

## Governing Overview
[tests overview](../../../overview.md)

## Purpose
Pinned initialize/system-init and capability frames for fake Claude 2.1.207 startup.

## Code Commentary
Deterministic structured readiness evidence for protocol tests.

## Invariants And Boundaries
Test evidence only; no production configuration or registry implication.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Fixture consumer. | `L1-L10` | [test_harness_control_claude.py](../../../../test_harness_control_claude.py) |

## Update History
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
