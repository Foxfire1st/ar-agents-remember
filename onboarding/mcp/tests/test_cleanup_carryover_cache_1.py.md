# mcp/tests/test_cleanup_carryover_cache_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_cleanup_carryover_cache_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_cleanup_carryover_cache_1.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `CitationCacheLifecycleTests1`
- Terminal cleanup cases use a real contract-derived mutation authority and assert the exact
  owned code and memory branch results; the retired synthesized
  `<memory-work-branch>-integration` result is not part of terminal cleanup.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_cleanup_carryover_cache_1.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## 260821-CLIVE-L2 Pre-L5 Cache Test Setup

This split cache suite installs the shared test-only terminal archive permit after the base setup.
The tests therefore continue to cover downstream cleanup cache semantics while production cleanup
remains fail-closed pending L5 archive evidence.

| Finding | Source |
| --- | --- |
| Subclass setup explicitly installs the downstream-unit archive permit. | mcp/tests/test_cleanup_carryover_cache_1.py:20-28 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: reused the real repositories already created by the citation-cache contract helper so the intended post-preflight ref-query failure remains production-bound.
- 2026-08-16T02:51+02:00 — L4 terminal authority: documented the real contract-derived cleanup
  fixture and the exact terminal branch result after retirement of the synthesized memory replay
  branch.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
