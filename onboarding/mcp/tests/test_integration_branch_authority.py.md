# mcp/tests/test_integration_branch_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Exercises the repository-global surface census, exact operation authority, alias/default refusal, CAS and rollback, conflict handoff, crash recovery, and bootstrap WAL.

## Code Commentary

The broad production-bound matrix covers code and external memory, linked worktrees, missing/corrupt authority, duplicate workers, and hard-crash recovery without substituting ambient checkout facts. Shared configured-repository and closed-leaf builders live in `integration_branch_authority_test_support.py` so this file remains focused on assertions.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `IntegrationBranchAuthorityTests` | mcp/tests/test_integration_branch_authority.py:77-1029 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Contract Publication Migration

The affected authority case now writes its contract through the canonical publication helper used by closeout identity. Branch-authority semantics are unchanged; the relationship update ensures the fixture hashes and publishes the same normalized contract representation.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 added an isinstance narrowing to the recovered series-bootstrap assertion after `ensure_master_series_contract` gained the blocked-result union; documented authority behavior is unchanged. Verification remains closeout-owned.

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-16T05:18+02:00 — Dagger fixture repair: repository-global standalone census expectations include the concurrently commanded atomic sibling, and journaled candidate worktrees remain inside their contract-owned worktree group.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: exact authority tests now use recorded leaf worktrees, named atomic-memory checkouts, standalone default sources, active-task surface lifetime, and fresh paired bootstrap recovery facts.
- 2026-08-16T03:29+02:00 — No content impact: retargeted the injected Git-error mock to the extracted repository-facts owner so the same fail-closed public assertion remains executable after the size split. Verification remains closeout-owned.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: moved shared fixture builders to the dedicated support module without changing the production routes or assertions. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration branch authority forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
