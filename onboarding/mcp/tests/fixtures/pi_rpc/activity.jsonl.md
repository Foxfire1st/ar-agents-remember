# mcp/tests/fixtures/pi_rpc/activity.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/pi_rpc/activity.jsonl` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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
| Finding | Anchor | Source |
| --- | --- | --- |
| Event mapper. | `PiRpcEventMapper` | mcp/src/agents_remember/serving/pi_rpc_events.py:55-358 |
| Fixture-driven tests. | `test_retry_compaction_and_agent_settled_are_not_early_idle` | mcp/tests/test_pi_rpc_adapter_ops_2.py:79-110 |

## Cross-Repo References
| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-08-02T22:10+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 2 local citation rows; deleted 1 unsupported external-source row under the 2026-08-02 14:10 ruling; scoped citation check now passes.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the retry/compaction/
  settlement event fixture.
