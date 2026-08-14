# mcp/tests/test_memory_citation_source_index_snapshot.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_memory_citation_source_index_snapshot.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_memory_citation_source_index_snapshot.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `SnapshotReuseTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_memory_citation_source_index_snapshot.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 SQLite Ownership

The metadata-corruption fixture now explicitly commits and closes its SQLite
connection before invoking the frozen-snapshot refusal. This removes implicit
context-manager connection lifetime from Python 3.14 cleanup behavior without
changing the snapshot contract under test.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented explicit commit/close ownership for the snapshot corruption fixture; verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
