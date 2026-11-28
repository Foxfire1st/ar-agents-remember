# dashboard/src/panels/file-viewer/serverHighlights.ts

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

Converts server-computed UTF-16 `SyntaxHighlights` triples into ordered, document-length-clamped CodeMirror 6 `Decoration.mark` extensions without loading any client-side language parser or Lezer grammar.

## Code Commentary

`KNOWN_KINDS` is typed as `ReadonlySet<string>` populated from `HighlightKind` so unrecognized token kinds are skipped rather than emitting arbitrary CSS class names. `markForKind` caches one `Decoration.mark({ class: "cm-ar-tok-<kind>" })` instance per known kind in `MARKS`. `clampSpan` guards against non-finite numbers, negative or out-of-range offsets, stripped trailing newlines (such as `drawnText`), and overlapping/out-of-order inputs by clamping each span to `[prevEnd, docLength]` and discarding empty ranges so `RangeSetBuilder` never throws.

`highlightDigest` returns `highlights?.digest ?? ""` so viewers can reconfigure a `Compartment` only when the span sequence actually changes while keeping `EditorView` / `MergeView` mounted across unchanged 2.5 s polls (`INV-QK8XNM`). `buildHighlightDecorations` returns `Decoration.none` for null/empty payloads and builds the `DecorationSet` in one linear pass. `serverHighlightsExtension` wraps the resulting `DecorationSet` in `EditorView.decorations.of(...)`.

## Relationships

Consumes `HighlightKind` and `SyntaxHighlights` from `dashboard/src/data/highlights.ts`, pairs with the foreground-only `.cm-ar-tok-*` CSS classes in `dashboard/src/panels/file-viewer/codemirrorTheme.ts`, and is imported by `FilePane.tsx` and `DiffPane.tsx` (replacing the removed client-side `langByExtension.ts`). Verified by `dashboard/src/panels/file-viewer/serverHighlights.test.tsx`.

## Evidence

- Restricts emitted mark classes to the eleven `HighlightKind` values cached in `MARKS`. [1]
- Clamps span endpoints monotonically within `[prevEnd, docLength]` so truncated excerpts or stripped trailing newlines never throw. [2]
- Builds ordered CodeMirror 6 `Decoration.mark` ranges and exports the `EditorView.decorations` extension plus `highlightDigest`. [3]
