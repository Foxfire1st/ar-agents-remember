# mcp/tests/test_interaction_retention.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_interaction_retention.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-25T13:20+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp tests overview](../overview.md)

## Purpose

Focused backend tests for the gate/operator-inbox interaction-retention policy.

## Code Commentary

The tests cover two behavior seams added for task 23/24. The gate-store TTL case
creates old interaction records and asserts compaction physically removes rows past
the 24-hour interaction TTL. The projection case writes pending operator-inbox
entries and asserts `read_agent_pickups` returns `waiting-for-agent` before the
5-minute pickup TTL and `check-chat` after it.

## Invariants And Boundaries

- Retention tests cover throwaway interaction data only; tasks, contracts, and ledger
  rows are intentionally outside this policy.
- The pickup projection test uses an explicit clock so UI TTL state is backend-owned.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Retention constants and policy helpers under test. | [controlplane/interaction_retention.py](agents-remember/mcp/src/agents_remember/controlplane/interaction_retention.py) |
| Gate store compaction exercised by the TTL test. | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| Agent-pickup projection exercised by the state test. | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |

## Update History

- 2026-06-25T13:20+02:00 — Created for task 23/24 TTL compaction and agent-pickup projection coverage.
