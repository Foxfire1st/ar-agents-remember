# mcp/tests/test_memory_citation_fix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_fix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6-R27/R28: what ``--fix`` repairs, what it refuses, and where it is allowed to write.

## Code Commentary

### Logic

Module-level surface:

- `_frozen_no_discovery` (function, lines 82-115)
- `document` (function, lines 118-120)
- `filler` (function, lines 123-124)
- `Tree` (class, lines 127-168) — A memory repository and the code repository it documents, both on disk.
- `TreeCase` (class, lines 171-187)
- `PureMoveTests` (class, lines 190-248) — A symbol that kept its name and changed file. The only class that auto-repairs.
- `ReflowTests` (class, lines 251-317) — The bulk of the churn: the file changed shape and the number went stale.
- `NoSimilarityMatchingTests` (class, lines 320-352) — Refuse similarity guesses when an anchor is absent.
- `DeletionAndAmbiguityTests` (class, lines 355-434) — The other two refusals, each with the work order R28 requires.
- `MultiAnchorRangeTests` (class, lines 437-482) — Several anchors pool, so the generated source list is a UNION, never a span.
- `AnchorKindTests` (class, lines 485-532) — One extent rule per anchor kind: AST construct, markdown section, quoted lines.
- `SourcePreservationTests` (class, lines 535-571) — What `--fix` must not delete, and the one thing it must.
- `UnresolvableOnlyClaimTests` (class, lines 574-634) — A claim whose every source is a dependency is SATISFIED, not permanently failing.
- `DocumentScopeTests` (class, lines 637-748) — `--document` exists because a curator wave shares one memory worktree.
- `CoreOperationScopeTests` (class, lines 751-876) — The deepest exported operations enforce acquisition and leased-index authority.
- `DuplicateCitationTests` (class, lines 879-945) — Exact source repetition gates within one Claim, never across separate Claims.
- `ScopedNormalisationTests` (class, lines 948-1090) — A curator's provisional passing range is generated away inside its one document.
- `ProseSerialisationTests` (class, lines 1093-1153) — `cit:` in running text shares every rule, and says so when it cannot be rewritten.
- `TreeShapeTests` (class, lines 1156-1186) — Shapes the memory tree really holds that the rewriter must walk past.
- `FindingEnrichmentTests` (class, lines 1189-1223) — L6-R28: the CHECK names every location in the tree, not only the row's own files.
- `SymbolIndexTests` (class, lines 1226-1319) — The one walk both halves share: what it reads, what it skips, what it counts.
- `ExtentTests` (class, lines 1322-1423) — The generator, on the shapes a whole-tree run meets.
- `WriteGuardTests` (class, lines 1426-1709) — L6-R27: the fixer writes into a leaf's memory worktree or it does not write.
- `CommandLineTests` (class, lines 1712-2000) — Command-line scope and write-mode contract.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_frozen_no_discovery` (lines 82-115). | `_frozen_no_discovery` | mcp/tests/test_memory_citation_fix.py:59-93 |
| Defines the function `document` (lines 118-120). | `document` | mcp/tests/test_memory_citation_fix.py:96-98 |
| Defines the function `filler` (lines 123-124). | `filler` | mcp/tests/test_memory_citation_fix.py:101-102 |
| Defines the class `Tree` (lines 127-168) — A memory repository and the code repository it documents, both on disk.. | `Tree` | mcp/tests/test_memory_citation_fix.py:127-168 |
| Defines the class `TreeCase` (lines 171-187). | `TreeCase` | mcp/tests/test_memory_citation_fix.py:149-165 |
| Defines the class `PureMoveTests` (lines 190-248) — A symbol that kept its name and changed file. The only class that auto-repairs.. | `PureMoveTests` | mcp/tests/test_memory_citation_fix.py:168-226 |
| Defines the class `ReflowTests` (lines 251-317) — The bulk of the churn: the file changed shape and the number went stale.. | `ReflowTests` | mcp/tests/test_memory_citation_fix.py:229-295 |
| Defines the class `NoSimilarityMatchingTests` (lines 320-352) — Refuse similarity guesses when an anchor is absent.. | `NoSimilarityMatchingTests` | mcp/tests/test_memory_citation_fix.py:298-330 |
| Defines the class `DeletionAndAmbiguityTests` (lines 355-434) — The other two refusals, each with the work order R28 requires.. | `DeletionAndAmbiguityTests` | mcp/tests/test_memory_citation_fix.py:333-412 |
| Defines the class `MultiAnchorRangeTests` (lines 437-482) — Several anchors pool, so the generated source list is a UNION, never a span.. | `MultiAnchorRangeTests` | mcp/tests/test_memory_citation_fix.py:415-460 |
| Defines the class `AnchorKindTests` (lines 485-532) — One extent rule per anchor kind: AST construct, markdown section, quoted lines.. | `AnchorKindTests` | mcp/tests/test_memory_citation_fix.py:463-510 |
| Defines the class `SourcePreservationTests` (lines 535-571) — What `--fix` must not delete, and the one thing it must.. | `SourcePreservationTests` | mcp/tests/test_memory_citation_fix.py:513-549 |
| Defines the class `UnresolvableOnlyClaimTests` (lines 574-634) — A claim whose every source is a dependency is SATISFIED, not permanently failing.. | `UnresolvableOnlyClaimTests` | mcp/tests/test_memory_citation_fix.py:552-612 |
| Defines the class `DocumentScopeTests` (lines 637-748) — `--document` exists because a curator wave shares one memory worktree.. | `DocumentScopeTests` | mcp/tests/test_memory_citation_fix_scopes.py:17-128 |
| Defines the class `CoreOperationScopeTests` (lines 751-876) — The deepest exported operations enforce acquisition and leased-index authority.. | `CoreOperationScopeTests` | mcp/tests/test_memory_citation_fix_scopes.py:131-256 |
| Defines the class `DuplicateCitationTests` (lines 879-945) — Exact source repetition gates within one Claim, never across separate Claims.. | `DuplicateCitationTests` | mcp/tests/test_memory_citation_fix_scopes.py:259-325 |
| Defines the class `ScopedNormalisationTests` (lines 948-1090) — A curator's provisional passing range is generated away inside its one document.. | `ScopedNormalisationTests` | mcp/tests/test_memory_citation_fix_scopes.py:328-470 |
| Defines the class `ProseSerialisationTests` (lines 1093-1153) — `cit:` in running text shares every rule, and says so when it cannot be rewritten.. | `ProseSerialisationTests` | mcp/tests/test_memory_citation_fix_scopes.py:473-533 |
| Defines the class `TreeShapeTests` (lines 1156-1186) — Shapes the memory tree really holds that the rewriter must walk past.. | `TreeShapeTests` | mcp/tests/test_memory_citation_fix_scopes.py:536-566 |
| Defines the class `FindingEnrichmentTests` (lines 1189-1223) — L6-R28: the CHECK names every location in the tree, not only the row's own files.. | `FindingEnrichmentTests` | mcp/tests/test_memory_citation_fix_scopes.py:569-603 |
| Defines the class `SymbolIndexTests` (lines 1226-1319) — The one walk both halves share: what it reads, what it skips, what it counts.. | `SymbolIndexTests` | mcp/tests/test_memory_citation_fix_operations.py:36-129 |
| Defines the class `ExtentTests` (lines 1322-1423) — The generator, on the shapes a whole-tree run meets.. | `ExtentTests` | mcp/tests/test_memory_citation_fix_operations.py:132-234 |
| Defines the class `WriteGuardTests` (lines 1426-1709) — L6-R27: the fixer writes into a leaf's memory worktree or it does not write.. | `WriteGuardTests` | mcp/tests/test_memory_citation_fix.py:16-16 |
| Defines the class `CommandLineTests` (lines 1712-2000) — Command-line scope and write-mode contract.. | "class CommandLineTests(unittest.TestCase):" | mcp/tests/test_memory_citation_fix_operations.py:540-540 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
