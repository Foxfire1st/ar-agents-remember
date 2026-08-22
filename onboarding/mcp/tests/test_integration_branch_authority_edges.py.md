# mcp/tests/test_integration_branch_authority_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Covers direct helper bypasses, tag and alias collisions, configured identity, carryover fencing,
final CAS races, and exact series closeout/integration. The focused atomic bootstrap
crash/revalidation slice lives in `test_integration_branch_authority_bootstrap_edges.py`; the
atomic source-drift/replay refusal lives in `test_integration_branch_authority_series_drift.py`.

## Code Commentary

The suite now also covers the organizational-completion direct-super and final-leaf branch-authority edges.

Tests bind real journal/queue/config facts and explicitly exercise no-ambient-checkout and contract-before-lane-release recovery edges. Its shared fixture imports now come directly from `integration_branch_authority_test_support.py`, eliminating the former test-module dependency.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `IntegrationBranchAuthorityEdgeTests` | mcp/tests/test_integration_branch_authority_edges.py:74-1149 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Admission Migration

Affected edge cases use canonical effective closeout input and contract publication rather than the retired raw operation-input fields. The suite continues to force integration branch authority and terminal edges; lifecycle compatibility is now called explicitly under the pure serialization lease.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 added an isinstance narrowing to the recovered contract assertion after the bootstrap union; documented authority behavior is unchanged. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:35+02:00 — 260815-DAG-L5: extended the suite for the organizational-completion direct-super and final-leaf branch-authority edges. Verification remains closeout-owned.

- 2026-08-16T08:12+02:00 — Dagger repair: configured-memory mismatch forcing now preserves an external contract while removing only runtime memory authority. Moved the final preparation race verbatim to the focused operation-authority suite so this file remains below the 1,200-line gate without duplication.
- 2026-08-16T07:46+02:00 — Test-size split: moved the atomic source-drift/replay refusal verbatim into `test_integration_branch_authority_series_drift.py`; no test, assertion, or compatibility path is duplicated.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: foreign-repository candidates use a contract-owned linked worktree, carryover uses a coordination-confined source worktree, and synthetic closeout completion uses the typed lifecycle phase.
- 2026-08-16T04:43+02:00 — Test-size split: moved the three contiguous atomic bootstrap journal/source/topology revalidation tests into `test_integration_branch_authority_bootstrap_edges.py`; no test or helper is duplicated, and this file is now 1,155 lines under the 1,200 hard limit.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: edge forcing now supplies real runtime config, exact atomic child landing facts, canonical task-doc reads, and a structurally external carryover contract whose memory side aliases the code Git common-dir.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: redirected shared fixture imports to the dedicated support owner; test behavior and assertions are unchanged. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration authority edge forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
