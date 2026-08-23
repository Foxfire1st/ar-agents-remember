# mcp/tests/test_cleanup_carryover_terminal.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_cleanup_carryover_terminal.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_cleanup_carryover_terminal.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `TerminalPreflightFailureTests` constructs real code and external-memory repositories, checks
  out the contract-recorded leaf memory branch, and proves terminal cleanup refuses dirty,
  unmerged, missing, or otherwise unsafe worktree state before deleting refs or worktrees.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_cleanup_carryover_terminal.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## 260821-CLIVE-L2 Pre-L5 Terminal Test Setup

Terminal-preflight failure tests explicitly pass the test-only archive gate before driving the
lower cleanup owner. This preserves the tested failure ordering without weakening production's
fail-closed requirement for future L5 external archive proof.

| Finding | Source |
| --- | --- |
| Terminal-preflight setup installs the bounded downstream-unit archive permit. | mcp/tests/test_cleanup_carryover_terminal.py:15-25 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: the external-memory terminal preflight now checks out the exact recorded leaf memory branch before exercising cleanup refusal.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
