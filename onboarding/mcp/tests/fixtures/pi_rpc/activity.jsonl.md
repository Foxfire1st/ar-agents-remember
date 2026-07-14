# mcp/tests/fixtures/pi_rpc/activity.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/pi_rpc/activity.jsonl` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview
[mcp/tests overview](../../overview.md)

## Purpose
Provides a compact event sequence covering agent start, retry, compaction, and `agent_settled`
activity for normalized settlement tests.

## Code Commentary
The ordering demonstrates that retry and compaction precede settlement and that the final event is
the stronger terminal boundary. It is consumed as one JSONL frame per line.

## Invariants And Boundaries
- Event ordering is meaningful test evidence, not a production event log.
- The fixture does not imply that `agent_end` alone is terminal idle.

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Event mapper. | [pi_rpc_events.py](../../../../src/agents_remember/serving/pi_rpc_events.py) |
| Fixture-driven tests. | [test_pi_rpc_adapter.py](../../test_pi_rpc_adapter.py) |

## Cross-Repo References
| Finding | Source Path |
| --- | --- |
| Upstream Pi RPC event semantics. | [Pi RPC](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/rpc.md) |

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the retry/compaction/
  settlement event fixture.
