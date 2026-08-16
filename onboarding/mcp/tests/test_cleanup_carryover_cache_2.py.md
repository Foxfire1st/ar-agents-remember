# mcp/tests/test_cleanup_carryover_cache_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_cleanup_carryover_cache_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-16T02:51+02:00                                            |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`                                        |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_cleanup_carryover_cache_2.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `CitationCacheLifecycleTests2`
- Cleanup and abandonment cache cases assert only the exact contract-owned code and memory branch
  results; the retired synthesized `<memory-work-branch>-integration` result is absent.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_cleanup_carryover_cache_2.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-16T02:51+02:00 — L4 terminal authority: reconciled cache lifecycle expectations with
  the exact contract-owned terminal branch set after removal of the synthesized replay branch.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
