# mcp/tests/test_worktree_support_tests_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_worktree_support_tests_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da`                                        |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_worktree_support_tests_1.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `WorktreeSupport1`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_worktree_support_tests_1.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 No Standalone Build Regression

The former standalone-light-task case now asserts fail-closed behavior when no
master lineage exists: return code 2, blocked state, projected lineage evidence,
and no leaf enclosure created. Tiny work still uses a leaf under a master.

## L23 Final Candidate Disposition

This support split exercises canonical start/status and durable-operation observation. Repeated calls
address the task and observe the accepted operation; they do not select a private job or process.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L1 Support Fixture Migration

Affected worktree-support cases now consume the shared normalized closeout arguments. Their lifecycle behavior remains unchanged; the migration removes test-only blank message defaults below validation.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: memory-start previews patch the sole production `start.ensure_worktree` owner after its public-facade export was retired.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: this split support suite retains start,
  status, and durable-operation regressions under canonical task identity. Verification remains
  closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented refusal of standalone build topology without a master edge; verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
