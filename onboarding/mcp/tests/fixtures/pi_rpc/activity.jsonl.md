# mcp/tests/fixtures/pi_rpc/activity.jsonl

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

## Evidence

### Repo-Internal References
- Event mapper. [1]
- Fixture-driven tests. [2]

### Cross-Repo References
