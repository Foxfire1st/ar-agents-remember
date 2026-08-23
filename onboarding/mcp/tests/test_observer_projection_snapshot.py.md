# mcp/tests/test_observer_projection_snapshot.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_projection_snapshot.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_observer_projection_snapshot.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `SnapshotReaderTests`
- `StoreIOTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_observer_projection_snapshot.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## 260821-CLIVE-L2 Root-Journal Snapshot Addressing

Snapshot tests now share `_write_addressable_contract`, which writes the contract and then publishes
the enclosure-root locator/manifest. Reopened contracts retain their lifecycle identity; a cleanup
field change no longer erases the address required to rediscover the same operation.

| Finding | Source |
| --- | --- |
| The fixture helper makes every relevant contract addressable through the lifecycle location chain. | mcp/tests/test_observer_projection_snapshot.py:68-78 |
| Enclosure reads use the helper and preserve lifecycle identity across reopen. | mcp/tests/test_observer_projection_snapshot.py:432-506 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
