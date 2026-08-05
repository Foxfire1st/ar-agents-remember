# mcp/tests/test_memory_citation_migration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_migration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
| Defines the function `card` (lines 70-71). | `card` | mcp/tests/test_memory_citation_migration.py:70-71 |
| Defines the function `link` (lines 74-76) — A Source Path cell in the superseded spelling, repo-name prefixed as the tree writes it.. | `link` | mcp/tests/test_memory_citation_migration.py:74-76 |
| Defines the class `Tree` (lines 79-123) — A memory repository and the code repository it documents, both on disk.. | `Tree` | mcp/tests/test_memory_citation_migration.py:79-123 |
| Defines the class `TreeCase` (lines 126-137). | `TreeCase` | mcp/tests/test_memory_citation_migration.py:126-137 |
| Defines the class `TableShapeTests` (lines 140-234) — The header, the delimiter and the rows move together or the table stops being one.. | `TableShapeTests` | mcp/tests/test_memory_citation_migration.py:140-234 |
| Defines the class `SourcePathTests` (lines 237-336) — Four live spellings of a markdown link, all resolved rather than rewritten.. | `SourcePathTests` | mcp/tests/test_memory_citation_migration.py:237-336 |
| Defines the class `AnchorSelectionTests` (lines 339-390) — Where an anchor comes from, and the exact point at which choosing one is a judgement.. | `AnchorSelectionTests` | mcp/tests/test_memory_citation_migration.py:339-390 |
| Defines the class `NoInventedFactTests` (lines 393-510) — Every case here is a row a reader must decide. The required outcome is a work order.. | `NoInventedFactTests` | mcp/tests/test_memory_citation_migration.py:393-510 |
| Defines the class `RangeProvenanceTests` (lines 513-633) — The range is generated. The old one votes only once it has been proven correct.. | `RangeProvenanceTests` | mcp/tests/test_memory_citation_migration.py:513-633 |
| Defines the class `ProseMigrationTests` (lines 636-767) — ``X (L47)`` becomes ``cit:([X], path:start-end)``, on one line, path always explicit.. | `ProseMigrationTests` | mcp/tests/test_memory_citation_migration.py:636-767 |
| Defines the class `IdempotenceTests` (lines 770-816) — L6-R16: a second pass over a converted tree is a byte-for-byte no-op.. | `IdempotenceTests` | mcp/tests/test_memory_citation_migration.py:770-816 |
| Defines the class `WorkOrderTests` (lines 819-898) — L6-R28: one work order per DOCUMENT, so a parallel dispatch takes one each.. | `WorkOrderTests` | mcp/tests/test_memory_citation_migration.py:819-898 |
| Defines the class `ParserSplitTests` (lines 901-948) — Which numbers are final and which move when the extent layer does.. | `ParserSplitTests` | mcp/tests/test_memory_citation_migration.py:901-948 |
| Defines the class `WalkTests` (lines 951-1010) — What the tree walk does and does not treat as a document.. | `WalkTests` | mcp/tests/test_memory_citation_migration.py:951-1010 |
| Defines the class `OldFormTests` (lines 1013-1068) — The reader for the format being replaced, at the edges the tree actually holds.. | `OldFormTests` | mcp/tests/test_memory_citation_migration.py:1013-1068 |
| Defines the class `WriteGuardTests` (lines 1071-1133) — L6-R27: the migration writes into a leaf's memory worktree or it does not write.. | `WriteGuardTests` | mcp/tests/test_memory_citation_migration.py:1071-1133 |
| Defines the class `CommandLineTests` (lines 1136-1202) — One command per mode, and no argument list that names the official memory repo.. | `CommandLineTests` | mcp/tests/test_memory_citation_migration.py:1136-1202 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
