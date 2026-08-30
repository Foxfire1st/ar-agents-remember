# mcp/tests/test_serving_cli.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_serving_cli.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-30T17:08:05+02:00 |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`|
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_serving_cli.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `BuildInfoTests`
- `StaticTests`
- `CliTests`
- `CliRunTests`
- `SimFixtureTests`
- `SimReplayTests`
- `CliSimTests`

ARSPAWN-L4 extends `BuildInfoTests` with the shared wire fields and a forcing content-address test:
identical Python source in different roots has one digest, `__pycache__` is ignored, and changed
source changes identity. Off-checkout identity omits facts it cannot prove.
An unreadable package tree also returns honest unknown rather than leaking the probe failure.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_serving_cli.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: added the unreadable-tree source-digest
  forcing case. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — ARSPAWN-L4 added content-addressed source and shared wire-payload
  forcing cases. Verification remains closeout-owned.

- 2026-08-24T21:23+02:00 — No content impact: the owned-state context manager moved from the test
  tree to `agents_remember_test_support.testing.global_state`; serving CLI behavior is unchanged.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
