# mcp/tests/test_observer_projection_ledger.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_projection_ledger.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_observer_projection_ledger.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `LedgerReaderTests`
- `LedgerCommitMetaTests`
- `DriftSnapshotProducerTests`
- `ProjectAndWriteAnalyticsTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_observer_projection_ledger.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## 260821-CLIVE-L2 Addressable Projection Fixture

The active enclosure fixture now publishes its lifecycle locator and immutable manifest before the
observer projects ledger analytics. The test therefore exercises normal root-journal discovery and
keeps a deleted worktree snapshot distinct from an unaddressable contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The active contract becomes lifecycle-addressable before analytics projection. | `test_project_and_write_prunes_orphaned_worktree_drift_snapshots` | mcp/tests/test_observer_projection_ledger.py:430-472 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
