# mcp/tests/test_memory_citation_grammars.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_grammars.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6-R17/R28: one parser for every language a citation points into.

## Code Commentary

### Logic

Module-level surface:

- `spans` (function, lines 41-42)
- `names` (function, lines 45-46)
- `node_of` (function, lines 49-54) — The first ``kind`` node in ``source``, for asserting on a reader's floor.
- `PinnedDependencyTests` (class, lines 57-94) — Parser measurements remain compatible with declared and installed dependencies.
- `numbered` (function, lines 97-98)
- `TypeScriptPureMoveTests` (class, lines 101-173) — L6-R16, both directions: the grammar is what turns this decline into a repair.
- `MentionNeverResolvesAMoveTests` (class, lines 176-206) — The safety rule the ``--fix`` probe bought, now carried by every parsed language.
- `PythonExtentTests` (class, lines 209-257) — Tree-sitter's Python extents, pinned against the constructs ``ast`` used to read.
- `ScriptDefinitionTests` (class, lines 260-321) — Every construct the TypeScript, TSX and JavaScript rule calls a definition.
- `NotADefinitionTests` (class, lines 324-367) — L6-R18: the known-good constructs this rule must not call a declaration.
- `UnparsedLanguageTests` (class, lines 370-385) — The stated ceiling: a language with no grammar binds nothing, and says so.
- `GrammarLoadingTests` (class, lines 388-422) — A grammar that will not load is fatal, and never a quiet change of parser.
- `OfflineParseTests` (class, lines 463-484) — The closeout gate runs where there is no egress, so the parse path must too.
- `SymbolIndexLanguageTests` (class, lines 487-536) — The tree-wide index, on the languages this leaf added to it.
- `ExtentBoundaryTests` (class, lines 539-559) — The two ways a construct's last line is spelled as a tree-sitter Point.
- `FallbackVolumeTests` (class, lines 562-597) — R18's other half: the fallback still works, and it is not disguised as a parse.
- `TypeScriptAnchorGrammarTests` (class, lines 600-706) — R32 modes 1, 2, 3 and 5, plus the nearby shapes that stay negative.
- `TypeScriptInterfacePoolRepairTests` (class, lines 709-735) — R32 mode 4: pooled members repair to their defining interface file.
- `PackageJsonQuotedPinTests` (class, lines 738-752) — R32 mode 5 through the checker, not only the anchor tokenizer.

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
| Defines the function `spans` (lines 41-42). | `spans` | mcp/tests/test_memory_citation_grammars.py:41-42 |
| Defines the function `names` (lines 45-46). | `names` | mcp/tests/test_memory_citation_grammars.py:45-46 |
| Defines the function `node_of` (lines 49-54) — The first ``kind`` node in ``source``, for asserting on a reader's floor.. | `node_of` | mcp/tests/test_memory_citation_grammars.py:49-54 |
| Defines the class `PinnedDependencyTests` (lines 57-94) — Parser measurements remain compatible with declared and installed dependencies.. | `PinnedDependencyTests` | mcp/tests/test_memory_citation_grammars.py:57-94 |
| Defines the function `numbered` (lines 97-98). | `numbered` | mcp/tests/test_memory_citation_grammars.py:97-98 |
| Defines the class `TypeScriptPureMoveTests` (lines 101-173) — L6-R16, both directions: the grammar is what turns this decline into a repair.. | `TypeScriptPureMoveTests` | mcp/tests/test_memory_citation_grammars.py:101-173 |
| Defines the class `MentionNeverResolvesAMoveTests` (lines 176-206) — The safety rule the ``--fix`` probe bought, now carried by every parsed language.. | `MentionNeverResolvesAMoveTests` | mcp/tests/test_memory_citation_grammars.py:176-206 |
| Defines the class `PythonExtentTests` (lines 209-257) — Tree-sitter's Python extents, pinned against the constructs ``ast`` used to read.. | `PythonExtentTests` | mcp/tests/test_memory_citation_grammars.py:209-257 |
| Defines the class `ScriptDefinitionTests` (lines 260-321) — Every construct the TypeScript, TSX and JavaScript rule calls a definition.. | `ScriptDefinitionTests` | mcp/tests/test_memory_citation_grammars.py:260-321 |
| Defines the class `NotADefinitionTests` (lines 324-367) — L6-R18: the known-good constructs this rule must not call a declaration.. | `NotADefinitionTests` | mcp/tests/test_memory_citation_grammars.py:324-367 |
| Defines the class `UnparsedLanguageTests` (lines 370-385) — The stated ceiling: a language with no grammar binds nothing, and says so.. | `UnparsedLanguageTests` | mcp/tests/test_memory_citation_grammars.py:370-385 |
| Defines the class `GrammarLoadingTests` (lines 388-422) — A grammar that will not load is fatal, and never a quiet change of parser.. | `GrammarLoadingTests` | mcp/tests/test_memory_citation_grammars.py:388-422 |
| Defines the class `OfflineParseTests` (lines 463-484) — The closeout gate runs where there is no egress, so the parse path must too.. | `OfflineParseTests` | mcp/tests/test_memory_citation_grammars.py:463-484 |
| Defines the class `SymbolIndexLanguageTests` (lines 487-536) — The tree-wide index, on the languages this leaf added to it.. | `SymbolIndexLanguageTests` | mcp/tests/test_memory_citation_grammars.py:487-536 |
| Defines the class `ExtentBoundaryTests` (lines 539-559) — The two ways a construct's last line is spelled as a tree-sitter Point.. | `ExtentBoundaryTests` | mcp/tests/test_memory_citation_grammars.py:539-559 |
| Defines the class `FallbackVolumeTests` (lines 562-597) — R18's other half: the fallback still works, and it is not disguised as a parse.. | `FallbackVolumeTests` | mcp/tests/test_memory_citation_grammars.py:562-597 |
| Defines the class `TypeScriptAnchorGrammarTests` (lines 600-706) — R32 modes 1, 2, 3 and 5, plus the nearby shapes that stay negative.. | `TypeScriptAnchorGrammarTests` | mcp/tests/test_memory_citation_grammars.py:600-706 |
| Defines the class `TypeScriptInterfacePoolRepairTests` (lines 709-735) — R32 mode 4: pooled members repair to their defining interface file.. | `TypeScriptInterfacePoolRepairTests` | mcp/tests/test_memory_citation_grammars.py:709-735 |
| Defines the class `PackageJsonQuotedPinTests` (lines 738-752) — R32 mode 5 through the checker, not only the anchor tokenizer.. | `PackageJsonQuotedPinTests` | mcp/tests/test_memory_citation_grammars.py:738-752 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
