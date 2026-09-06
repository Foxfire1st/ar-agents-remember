# mcp/tests/test_memory_citation_fix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_fix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6-R27/R28: what ``--fix`` repairs, what it refuses, and where it is allowed to write.

## Code Commentary

### Logic

The local `Tree` and `TreeCase` fixtures drive the real fixer over temporary code/memory files. `PureMoveTests`, `ReflowTests`, `NoSimilarityMatchingTests`, `DeletionAndAmbiguityTests`, `MultiAnchorRangeTests`, `AnchorKindTests`, `SourcePreservationTests` and `UnresolvableOnlyClaimTests` protect exact resolution, complete evidence preservation, range repair and deterministic refusal. `_frozen_no_discovery` makes forbidden scans/rebuilds explicit in reused lease scenarios.

`ReflowTests.test_a_dry_run_reports_the_rewrite_and_writes_nothing` checks the prospective replacement and exact unchanged document bytes while requiring `documentsWritten == 0`. Repeat repair is a no-op, and source-cell padding survives.

Document-scope, duplicate and pooled-normalization suites live in `test_memory_citation_fix_scopes.py`. Source-index/extents, write guards and CLI suites live in `test_memory_citation_fix_operations.py`. They are related evidence owners, not classes defined by this file.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

Current file ownership and the preserved related scope/operation contracts are explicit below.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pure moves follow the same exact-name symbol into its new file. | `PureMoveTests` | mcp/tests/test_memory_citation_fix.py:168-226 |
| Range repair, actual zero-write previews, repeat no-ops and source-cell padding are forced. | `ReflowTests` | mcp/tests/test_memory_citation_fix.py:229-295 |
| Absent anchors never acquire similarity guesses. | `NoSimilarityMatchingTests` | mcp/tests/test_memory_citation_fix.py:298-330 |
| Deleted or ambiguous anchors produce actionable refusals. | `DeletionAndAmbiguityTests` | mcp/tests/test_memory_citation_fix.py:333-412 |
| Multiple anchors produce their evidence union rather than an invented broad span. | `MultiAnchorRangeTests` | mcp/tests/test_memory_citation_fix.py:415-460 |
| AST, Markdown and literal anchors preserve their distinct extent rules. | `AnchorKindTests` | mcp/tests/test_memory_citation_fix.py:463-510 |
| Unrelated source evidence remains intact. | `SourcePreservationTests` | mcp/tests/test_memory_citation_fix.py:513-549 |
| External dependency evidence does not become a permanent local failure. | `UnresolvableOnlyClaimTests` | mcp/tests/test_memory_citation_fix.py:552-612 |
| Preview reports the proposed source change but zero completed document writes. | `test_a_dry_run_reports_the_rewrite_and_writes_nothing` | mcp/tests/test_memory_citation_fix.py:270-279 |
| The related `DocumentScopeTests` group is owned by this companion module. | `DocumentScopeTests` | mcp/tests/test_memory_citation_fix_scopes.py:17-128 |
| The related `CoreOperationScopeTests` group is owned by this companion module. | `CoreOperationScopeTests` | mcp/tests/test_memory_citation_fix_scopes.py:131-256 |
| The related `DuplicateCitationTests` group is owned by this companion module. | `DuplicateCitationTests` | mcp/tests/test_memory_citation_fix_scopes.py:259-325 |
| The related `ScopedNormalisationTests` group is owned by this companion module. | `ScopedNormalisationTests` | mcp/tests/test_memory_citation_fix_scopes.py:328-470 |
| The related `ProseSerialisationTests` group is owned by this companion module. | `ProseSerialisationTests` | mcp/tests/test_memory_citation_fix_scopes.py:473-533 |
| The related `TreeShapeTests` group is owned by this companion module. | `TreeShapeTests` | mcp/tests/test_memory_citation_fix_scopes.py:536-566 |
| The related `FindingEnrichmentTests` group is owned by this companion module. | `FindingEnrichmentTests` | mcp/tests/test_memory_citation_fix_scopes.py:569-603 |
| The related `SymbolIndexTests` group is owned by this companion module. | `SymbolIndexTests` | mcp/tests/test_memory_citation_fix_operations.py:72-165 |
| The related `ExtentTests` group is owned by this companion module. | `ExtentTests` | mcp/tests/test_memory_citation_fix_operations.py:168-270 |
| The related `WriteGuardTests` group is owned by this companion module. | `WriteGuardTests` | mcp/tests/test_memory_citation_fix_operations.py:273-567 |
| The related `CommandLineTests` group is owned by this companion module. | `CommandLineTests` | mcp/tests/test_memory_citation_fix_operations.py:570-858 |

## Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No new cross-repository protocol. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Corrected dry-run write accounting and reconciled the pre-existing split-test inventory with its actual source owners while preserving the related behavioral routes. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
