# mcp/tests/test_closeout_queue_blockers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_blockers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns the queue projection's complete pre-closeout, post-closeout, source, ledger, grade, and
dependency blocker vocabulary.

## Code Commentary

### Logic

The suite drives each blocker composer directly with canonical contracts and queue records. It
proves exact early-return boundaries, external-memory commit and ledger requirements, evidence
drift classes, and waiting reasons for lanes, atomic blockers, predecessors, and admission. Since
260815-DAG-L13 the source/ledger blocker strings carry the `run worktree_sync, then retry`
recovery suffix, and `BlockerLifetimeExclusivityTests` forces the blocker lane contract: a second
block is refused with structured owner facts, idempotent same-master re-acquisition, and a
certified sibling reported as an acquisition fact rather than a hard drain.

### Invariants And Boundaries

- Projection compares every persisted candidate fact with the same current fact used by lifecycle
  admission.
- Certified external candidates require exact code, memory-content, and ledger commits.
- Source and ledger blocker tests read the exact named source refs through `branch_commit`; ambient
  checkout `HEAD` is not scheduling authority.
- Waiting facts remain distinct from malformed or stale blockers.
- The lane-drain refusal applies only to lane-occupying states; certified candidates are facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pre- and post-closeout blocker sets are separately forced. | `test_pre_closeout_blockers_name_lifecycle_tree_memory_and_source_changes` | mcp/tests/test_closeout_queue_blockers.py:119-144 |
| Closed external trees and commits are exact. | `test_closed_tree_and_certified_commit_blockers_are_exact` | mcp/tests/test_closeout_queue_blockers.py:171-212 |
| Waiting reasons cover graph and blocker logistics. | `test_waiting_reasons_cover_lane_blocker_atomic_and_admission_facts` | mcp/tests/test_closeout_queue_blockers.py:367-437 |
| Blocker lifetime exclusivity and structured refusal facts. | `BlockerLifetimeExclusivityTests` | mcp/tests/test_closeout_queue_blockers.py:440-583 |

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: source/ledger blocker expectations gained the
  `worktree_sync` recovery suffix; added `BlockerLifetimeExclusivityTests` (structured refusal
  facts, idempotent re-acquisition, certified-sibling drain narrowing). Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T02:51+02:00 — L4 named-ref authority: moved source and ledger blocker forcing to the
  exact branch-commit seam so an unrelated ambient checkout cannot satisfy queue evidence.

- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  every blocker input and expected result is unchanged.
- 2026-08-15T12:53+02:00 — Created for L3's focused blocker-composition coverage after the first
  full targeted Dagger artifact identified CRAP and changed-branch gaps.
