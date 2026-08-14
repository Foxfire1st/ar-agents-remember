# mcp/tests/test_worktree_support_tests_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_worktree_support_tests_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`                                        |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
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

## Update History
- 2026-08-14T06:40+02:00 — L23 final candidate review: this split support suite retains start,
  status, and durable-operation regressions under canonical task identity. Verification remains
  closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented refusal of standalone build topology without a master edge; verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
