# mcp/tests/test_closeout_queue_blockers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_blockers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T13:18+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
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
drift classes, and waiting reasons for lanes, atomic barriers, predecessors, and admission.

### Invariants And Boundaries

- Projection compares every persisted candidate fact with the same current fact used by lifecycle
  admission.
- Certified external candidates require exact code, memory-content, and ledger commits.
- Waiting facts remain distinct from malformed or stale blockers.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pre- and post-closeout blocker sets are separately forced. | `test_pre_closeout_blockers_name_lifecycle_tree_memory_and_source_changes` | mcp/tests/test_closeout_queue_blockers.py:109-134 |
| Closed external trees and commits are exact. | `test_closed_tree_and_certified_commit_blockers_are_exact` | mcp/tests/test_closeout_queue_blockers.py:161-202 |
| Waiting reasons cover graph and barrier logistics. | `test_waiting_reasons_cover_lane_barrier_atomic_and_admission_facts` | mcp/tests/test_closeout_queue_blockers.py:350-416 |

## Update History

- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  every blocker input and expected result is unchanged.
- 2026-08-15T12:53+02:00 — Created for L3's focused blocker-composition coverage after the first
  full targeted Dagger artifact identified CRAP and changed-branch gaps.
