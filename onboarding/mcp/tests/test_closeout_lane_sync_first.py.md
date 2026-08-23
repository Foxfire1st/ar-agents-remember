# mcp/tests/test_closeout_lane_sync_first.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_lane_sync_first.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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
| Sync-first recovery and stale-sibling reporting forcing. | `CloseoutLaneSyncFirstTests` | mcp/tests/test_closeout_lane_sync_first.py:114-190 |
| Lane serialization and effective-nature forcing. | `CloseoutLaneSerializationTests` | mcp/tests/test_closeout_lane_sync_first.py:193-292 |
| The recovery naming and stale-sibling facts under test. | `_boundary_recovery`; `_stale_sibling_facts` | mcp/src/agents_remember/worktrees/queue/closeout_queue_blocker.py:208-218; mcp/src/agents_remember/worktrees/queue/closeout_queue_blocker.py:221-264 |
| The integration lane-ownership refusal under test. | `test_integration_claim_refuses_when_another_candidate_owns_the_lane` | mcp/tests/test_closeout_lane_sync_first.py:203-241 |
| The graph-less queue-free series edge under test. | `_publish_atomic_series_edge` | mcp/src/agents_remember/worktrees/series_closeout.py:80-134 |

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved this suite's imports to the restructured packages:
queue owners (including `closeout_queue_blocker`, `closeout_queue_candidate_evidence`,
`closeout_queue_errors`, and `closeout_queue_lifecycle`) now import from `worktrees/queue/`, while
the lifecycle-operation store and dispatch imports come from `worktrees/integration/`; the
`__main__` runner was removed. No assertions changed.

## 260821-CLIVE-L1 Fixture Migration

The close-and-certify fixture now creates closeout through canonical validated admission rather than constructing the retired raw durable input. The suite continues to own sync-first lane behavior; it does not make queue state the owner of closeout messages or mutation evidence.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_moved_source_names_worktree_sync_as_the_recovery`, `test_boundary_recovery_suffix_names_worktree_sync`, `test_lane_release_reports_stale_siblings_by_evidence`, `test_unreadable_sibling_contract_is_reported_not_swallowed`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_moved_source_names_worktree_sync_as_the_recovery`, `test_boundary_recovery_suffix_names_worktree_sync`, `test_lane_release_reports_stale_siblings_by_evidence`, `test_unreadable_sibling_contract_is_reported_not_swallowed`. | L122-L132; L134-L143; L145-L157; L159-L179 | `mcp/tests/test_closeout_lane_sync_first.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: queue imports moved under
  `worktrees/queue/` and lifecycle-operation imports under `worktrees/integration/`; the `__main__`
  runner was removed. Verified at code commit e5cb139f.
- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the sync-first recovery and lane
  serialization forcing suite. Verification remains closeout-owned.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
