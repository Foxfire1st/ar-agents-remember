# dashboard/src/data/highlights.ts

## Governing Overview

[data/ overview](overview.md)

## Purpose

Defines the TypeScript wire types for server-computed tree-sitter UTF-16 syntax highlights consumed across all dashboard code, diff, note, role-report, knowledge-reader, and review viewers.

## Code Commentary

`HighlightKind` enumerates the eleven styled token families emitted by the backend (`keyword`, `string`, `comment`, `number`, `function`, `type`, `operator`, `punctuation`, `tag`, `attribute`, `heading`), mirroring `mcp/src/agents_remember/models/highlights.py`. `SyntaxHighlights` carries the schema `version`, a deterministic 16-hex-character `digest` used by CodeMirror 6 compartments to skip redundant decoration rebuilds on unchanged polls, the ordered `kinds` palette array, and the flat `spans` array of `(startUtf16, endUtf16, kindIndex)` triples.

## Relationships

Imported by dashboard data clients (`files.ts`, `changeset.ts`, `notes.ts`, `roleReport.ts`, `knowledgeReader.ts`, `review.ts`, `reviewTrees.ts`) and by `dashboard/src/panels/file-viewer/serverHighlights.ts`, which validates `kinds` against `HighlightKind` and maps spans onto CodeMirror 6 `Decoration.mark` classes.

## Evidence

- Declares the eleven backend-aligned `HighlightKind` token families. [1]
- Defines the immutable `SyntaxHighlights` wire shape (`version`, `digest`, `kinds`, `spans`). [2]
- Mirrors the Pydantic `SyntaxHighlights` contract in `models/highlights.py`. [3]
