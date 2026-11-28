# dashboard/src/panels/file-viewer/serverHighlights.test.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

Verifies CodeMirror 6 rendering of server-computed UTF-16 highlight decorations across `FilePane`, split and inline `DiffPane`, and `ChangeSetPane`, including `citationHighlight` layering, malformed/clamped span safety, `INV-QK8XNM` DOM retention across unchanged-digest polls, and plain-mode suppression.

## Code Commentary

Five Vitest cases exercise the frontend highlighting pipeline end to end:
1. `FilePane` renders `.cm-ar-tok-keyword`, `.cm-ar-tok-function`, and `.cm-ar-tok-string` spans alongside `.cm-citedLine` citation highlighting.
2. `buildHighlightDecorations` returns empty decorations for `null`/`undefined`, safely ignores malformed/out-of-range/unknown-kind/`NaN` spans, and clamps spans when `drawnText` strips a trailing newline.
3. Split `DiffPane` applies independent `beforeHighlights` and `afterHighlights` through per-side `Compartment`s (string on left, number on right), retains the exact `.cm-mergeView` DOM node across rerenders with cloned equal-digest payloads (`INV-QK8XNM`), and reconfigures in place when highlights clear to `null`.
4. Inline `DiffPane` applies `afterHighlights` without breaking `.cm-deletedChunk` widgets.
5. `ChangeSetPane` renders token highlights in change-set view and suppresses all `.cm-ar-tok-*` classes when switched to full-file plain mode (`highlight` off).

## Relationships

Directly exercises `serverHighlights.ts`, `FilePane.tsx`, `DiffPane.tsx`, and `ChangeSetPane.tsx` using the shared `SyntaxHighlights` and `FileDiff` wire types. Complements `ChangeSetViewer.cache.test.tsx` (poll retention) and `mcp/tests/test_unified_tree_sitter_highlights.py` (backend spans and route contracts).

## Evidence

- Proves `FilePane` renders `.cm-ar-tok-*` decorations layered with `.cm-citedLine` and clamps malformed or trailing-newline-stripped spans safely. [1]
- Proves split and inline `DiffPane` per-side highlight compartments, `.cm-mergeView` DOM node retention on unchanged/cleared digests, and `.cm-deletedChunk` compatibility. [2]
- Proves `ChangeSetPane` suppresses token highlights in full-file plain mode when `highlight` is toggled off. [3]
