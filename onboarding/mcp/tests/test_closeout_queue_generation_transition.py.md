# mcp/tests/test_closeout_queue_generation_transition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_generation_transition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Pins the current queue-facing regression in which conflict resolution clears an obsolete generation and later admits a newly truthful closeout candidate.

## Code Commentary

### Logic

The scenario opens a conflicting integration, performs the sanctioned reset/cancel/sync/task-rewrite sequence, closes and certifies the new candidate, then integrates it. The final assertion proves the old candidate is absent from the current queue surface. This is a transition regression for the existing implementation, not a claim that queue state owns task truth or closeout lifecycle evidence.

### Invariants And Boundaries

- A stale candidate cannot survive conflict reset as current schedulable work.
- The next candidate is derived from refreshed contract/task facts.
- Queue absence is scheduling evidence only; journal and contract owners retain lifecycle facts.
- L3 owns the projection/invalidation redesign beyond this L1 forcing seam.

## Docs References

See task `260821-CLIVE-L1` L1-R5 and the deferred queue work in L3.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Conflict reset admits a truthful new closeout generation and removes the obsolete candidate. | `test_conflict_reset_admits_a_truthful_new_closeout_generation` | mcp/tests/test_closeout_queue_generation_transition.py:47-80 |
| Scenario helpers close, certify, and assert candidate absence using production surfaces. | `_close_and_certify_candidate`; `_assert_candidate_absent` | mcp/tests/test_closeout_queue_generation_transition.py:138-187; mcp/tests/test_closeout_queue_generation_transition.py:190-195 |

## Cross-Repo References

External-memory scratch repositories are used only to model the task’s configured topology.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_conflict_reset_admits_a_truthful_new_closeout_generation`. This is a transitional pre-L3 queue-generation regression. L2's durable successor/recovery generation lives in the root journal; L3 owns retiring queue-row generation repair in favor of door truth and waiting-only rebuild.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_conflict_reset_admits_a_truthful_new_closeout_generation`. | L47-L80 | `mcp/tests/test_closeout_queue_generation_transition.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
