# mcp/tests/test_memory_citation_migration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_migration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6-R27: converting a memory tree from the superseded citation format to the anchored one.

## Code Commentary

### Logic

Module-level surface:

- `card` (function, lines 70-71)
- `link` (function, lines 74-76) — A Source Path cell in the superseded spelling, repo-name prefixed as the tree writes it.
- `Tree` (class, lines 79-123) — A memory repository and the code repository it documents, both on disk.
- `TreeCase` (class, lines 126-137)
- `TableShapeTests` (class, lines 140-234) — The header, the delimiter and the rows move together or the table stops being one.
- `SourcePathTests` (class, lines 237-336) — Four live spellings of a markdown link, all resolved rather than rewritten.
- `AnchorSelectionTests` (class, lines 339-390) — Where an anchor comes from, and the exact point at which choosing one is a judgement.
- `NoInventedFactTests` (class, lines 393-510) — Every case here is a row a reader must decide. The required outcome is a work order.
- `RangeProvenanceTests` (class, lines 513-633) — The range is generated. The old one votes only once it has been proven correct.
- `ProseMigrationTests` (class, lines 636-767) — ``X (L47)`` becomes ``cit:([X], path:start-end)``, on one line, path always explicit.
- `IdempotenceTests` (class, lines 770-816) — L6-R16: a second pass over a converted tree is a byte-for-byte no-op.
- `WorkOrderTests` (class, lines 819-898) — L6-R28: one work order per DOCUMENT, so a parallel dispatch takes one each.
- `ParserSplitTests` (class, lines 901-948) — Which numbers are final and which move when the extent layer does.
- `WalkTests` (class, lines 951-1010) — What the tree walk does and does not treat as a document.
- `OldFormTests` (class, lines 1013-1068) — The reader for the format being replaced, at the edges the tree actually holds.
- `WriteGuardTests` (class, lines 1071-1133) — L6-R27: the migration writes into a leaf's memory worktree or it does not write.
- `CommandLineTests` (class, lines 1136-1202) — One command per mode, and no argument list that names the official memory repo.

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
| Defines the function `card` (lines 70-71). | "def card(path: str" | mcp/tests/test_memory_citation_migration.py:54-54 |
| Defines the function `link` (lines 74-76) — A Source Path cell in the superseded spelling, repo-name prefixed as the tree writes it.. | `link` | mcp/tests/test_memory_citation_migration.py:58-60 |
| Defines the class `Tree` (lines 79-123) — A memory repository and the code repository it documents, both on disk.. | `Tree` | mcp/tests/test_memory_citation_migration.py:79-123 |
| Defines the class `TreeCase` (lines 126-137). | `TreeCase` | mcp/tests/test_memory_citation_migration.py:110-121 |
| Defines the class `TableShapeTests` (lines 140-234) — The header, the delimiter and the rows move together or the table stops being one.. | `TableShapeTests` | mcp/tests/test_memory_citation_migration.py:124-218 |
| Defines the class `SourcePathTests` (lines 237-336) — Four live spellings of a markdown link, all resolved rather than rewritten.. | `SourcePathTests` | mcp/tests/test_memory_citation_migration.py:221-320 |
| Defines the class `AnchorSelectionTests` (lines 339-390) — Where an anchor comes from, and the exact point at which choosing one is a judgement.. | `AnchorSelectionTests` | mcp/tests/test_memory_citation_migration.py:323-374 |
| Defines the class `NoInventedFactTests` (lines 393-510) — Every case here is a row a reader must decide. The required outcome is a work order.. | `NoInventedFactTests` | mcp/tests/test_memory_citation_migration.py:14-14 |
| Defines the class `RangeProvenanceTests` (lines 513-633) — The range is generated. The old one votes only once it has been proven correct.. | `RangeProvenanceTests` | mcp/tests/test_memory_citation_migration_ops.py:127-247 |
| Defines the class `ProseMigrationTests` (lines 636-767) — ``X (L47)`` becomes ``cit:([X], path:start-end)``, on one line, path always explicit.. | `ProseMigrationTests` | mcp/tests/test_memory_citation_migration_forms.py:7-138 |
| Defines the class `IdempotenceTests` (lines 770-816) — L6-R16: a second pass over a converted tree is a byte-for-byte no-op.. | `IdempotenceTests` | mcp/tests/test_memory_citation_migration_forms.py:141-187 |
| Defines the class `WorkOrderTests` (lines 819-898) — L6-R28: one work order per DOCUMENT, so a parallel dispatch takes one each.. | `WorkOrderTests` | mcp/tests/test_memory_citation_migration_forms.py:190-269 |
| Defines the class `ParserSplitTests` (lines 901-948) — Which numbers are final and which move when the extent layer does.. | `ParserSplitTests` | mcp/tests/test_memory_citation_migration_forms.py:272-319 |
| Defines the class `WalkTests` (lines 951-1010) — What the tree walk does and does not treat as a document.. | `WalkTests` | mcp/tests/test_memory_citation_migration_forms.py:322-381 |
| Defines the class `OldFormTests` (lines 1013-1068) — The reader for the format being replaced, at the edges the tree actually holds.. | `OldFormTests` | mcp/tests/test_memory_citation_migration_guard.py:20-75 |
| Defines the class `WriteGuardTests` (lines 1071-1133) — L6-R27: the migration writes into a leaf's memory worktree or it does not write.. | "class WriteGuardTests(unittest.TestCase):" | mcp/tests/test_memory_citation_fix_operations.py:238-238 |
| Defines the class `CommandLineTests` (lines 1136-1202) — One command per mode, and no argument list that names the official memory repo.. | "class CommandLineTests(unittest.TestCase):" | mcp/tests/test_memory_citation_fix_operations.py:540-540 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
