# mcp/src/agents_remember/models/highlights.py

## Governing Overview

[models/ overview](overview.md)

## Purpose

Defines the strict immutable `SyntaxHighlights` wire contract, closed `HighlightKind` vocabulary, and payload size/span ceilings shared by all backend code-serving endpoints and knowledge models.

## Code Commentary

Sets three module-level constants: `HIGHLIGHT_PAYLOAD_VERSION = 1`, `HIGHLIGHT_MAX_BYTES = 512 * 1024` (512 KiB), and `HIGHLIGHT_MAX_SPANS = 20_000`. `HighlightKind` is a closed 11-member `Literal` (`keyword`, `string`, `comment`, `number`, `function`, `type`, `operator`, `punctuation`, `tag`, `attribute`, `heading`) aligned with the dashboard CSS classes in `codemirrorTheme.ts`.

`SyntaxHighlights` is a frozen Pydantic model with `extra="forbid"`. Its `after` model validator `_validate_span_triples` enforces that `spans` has length divisible by 3, that every `(start, end, kind_index)` triple is strictly non-empty (`end > start`) and monotonically non-overlapping (`start >= prev_end`), and that every `kind_index` lies within `0 <= kind_index < len(kinds)`. `to_wire()` emits a plain JSON-serializable dict for `JSONResponse` handlers.

## Relationships

Produced by `highlights_engine.py` and `highlights_service.py`; embedded in `serving/response_contract.py` (`FileContents`, `DiffSide`, `NoteContents`), `models/knowledge/review_source_content.py` (`ReviewSourceSide`), and `models/knowledge/review_tree_entries.py` (`ReviewTreeEntrySide`); mirrored in TypeScript by `dashboard/src/data/highlights.ts`.

## Evidence

- Defines payload version, 512 KiB byte ceiling, 20,000-span ceiling, and the 11-member `HighlightKind` union. [1]
- Enforces immutable flat non-overlapping UTF-16 span triples with in-range kind indices and plain JSON serialization. [2]
