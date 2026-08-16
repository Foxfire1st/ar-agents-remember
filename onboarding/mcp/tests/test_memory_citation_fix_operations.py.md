# mcp/tests/test_memory_citation_fix_operations.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_memory_citation_fix_operations.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-16T02:51+02:00                                            |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`                                        |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_memory_citation_fix_operations.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

L23 proves the public `citation_fix_payload` preserves the leaf guard, targets the leaf onboarding root, and exposes the expected dry-run repair count.

The frozen-refusal cases use `_frozen_no_source_discovery` to poison filesystem walking, source
tree-state inspection, legacy-cache reclamation, index build/publish fallback, and database
integrity traversal. A rejected frozen snapshot therefore cannot silently scan, rebuild, or fall
back before refusing the write.

- `SymbolIndexTests`
- `ExtentTests`
- `WriteGuardTests`
- `CommandLineTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_memory_citation_fix_operations.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-16T02:51+02:00 — L4 frozen-source authority: expanded the refusal poison seam across
  every source discovery, cache recovery, rebuild, and integrity path so a rejected frozen
  operation proves zero fallback traversal.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
