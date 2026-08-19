# mcp/tests/test_closeout_lane_sync_first.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_lane_sync_first.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the 260815-DAG-L13-R2/R3 lane contract: stale-base refusals name `worktree_sync` as the
recovery, a lane release reports stale-by-evidence siblings (unreadable sibling contracts are fact
rows, never swallowed), and the landing lane serializes exactly one lane-occupying candidate.

## Code Commentary

### Logic

`CloseoutLaneSyncFirstTests` proves moved code/memory source bases and ledger remapping refuse with
`worktree_sync` named, the integration boundary appends the same recovery, a completed landing
returns the stale-by-evidence sibling facts, an unreadable sibling contract is reported as a
`contract-unreadable` fact, and a current sibling reports nothing. `CloseoutLaneSerializationTests`
proves an integration claim refuses while another candidate owns the lane, a graph-less sprint's
series edge publication skips the queue (the live series contract already owns the sequential
lane), and the series-closeout/terminal-authority refusals read the effective nature.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- Recovery naming is part of the refusal contract, asserted literally.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-first recovery and stale-sibling reporting forcing. | `CloseoutLaneSyncFirstTests` | mcp/tests/test_closeout_lane_sync_first.py:108-185 |
| Lane serialization and effective-nature forcing. | `CloseoutLaneSerializationTests` | mcp/tests/test_closeout_lane_sync_first.py:187-289 |
| The recovery naming and stale-sibling facts under test. | `_boundary_recovery`; `_stale_sibling_facts` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:208-264 |
| The integration lane-ownership check under test. | `_claim_integration` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:1080-1107 |
| The graph-less queue-free series edge under test. | `_publish_atomic_series_edge` | mcp/src/agents_remember/worktrees/series_closeout.py:78-133 |

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the sync-first recovery and lane
  serialization forcing suite. Verification remains closeout-owned.
