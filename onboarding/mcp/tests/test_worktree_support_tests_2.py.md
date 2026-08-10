# mcp/tests/test_worktree_support_tests_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_worktree_support_tests_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b537abe20cf2498ef38e86e29ca586b5eec38466`                                        |
| lastVerifiedCommitDate | 2026-08-10T08:37:35+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_worktree_support_tests_2.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `WorktreeSupport2`
- ARG-L1 keeps the successful closeout phase report honest: citations appear in both the
  before-refresh preflight and the after-refresh no-fallback verification phase.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_worktree_support_tests_2.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-10T08:20+02:00 — 260805-ARG-L1: updated the closeout phase assertion to require the
  post-refresh citation repetition. Verification metadata remains pinned until closeout stamps
  ARG-L1.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
