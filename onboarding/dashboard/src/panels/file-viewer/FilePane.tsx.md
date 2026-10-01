# dashboard/src/panels/file-viewer/FilePane.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FilePane` is the reusable **read-only CodeMirror 6** pane — the shared code primitive of the File Viewer.
`DualPane` mounts it on the code side. L4's Change-Set Viewer reuses it by swapping the single `EditorView`
for `@codemirror/merge` (same editor core + the same `HighlightStyle`, so tokens are identical across plain
and diff views). The `EditorView` is created imperatively in an effect and torn down on unmount / content
change.

## Code Commentary

### Logic

Props are `{ content, language, firstLine? = 1, fit? = false, marks? }`. **`firstLine` and `fit` were added by MIK-L31 for
the reviewer's focused expression cards** and change nothing at their defaults: `firstLine` numbers the gutter from
the excerpt's first line in its file (`numberedFrom` in the sibling `lineNumbering.ts`, which is the plain
`lineNumbers()` for line 1), and `fit` swaps the `host` style for `fitHost`, which sizes the editor to its content
(capped at `32rem`) instead of pinning it to full height. **`marks` was added by MIK-L34 for the reviewer's per-hunk
intent markers** and changes nothing when omitted: the pane takes `useMarkedPane(marks)` from the sibling
`markGutter.tsx`, puts `gutterFor("all", firstLine)` first in its extensions (`[]` without marks), tells it
`drawn({ after: { view, first: firstLine } })` once the editor exists and `drawn(null)` at teardown, rebuilds when
`placement` changes (a mark moved), and renders the marks' `portals` after the host. A pane that draws one side of a
diff on its own receives only that side's marks from its caller (`IntentMarkers.sideMarks`). A `ref` points at the
host div; an effect builds the editor:
**`langExtension(language)`** is awaited (the `@codemirror/lang-*` packs are code-split, so a language is
loaded only when first opened), guarded by a `disposed` flag against a late resolve after teardown. The
extension set is `gutterFor("all", firstLine)`, `numberedFrom(firstLine)`, `EditorState.readOnly.of(true)`, `EditorView.editable.of(false)`,
`EditorView.lineWrapping`, and `codeTheme`, plus the resolved language extension when one exists; then
`new EditorView({ parent, state })`, then `drawn(...)`. Cleanup sets `disposed = true`, calls `drawn(null)` and
`view?.destroy()`. The effect deps are `[content, language, firstLine, placement, gutterFor, drawn]`, so the editor is
**recreated wholesale** when any changes. Render is the `<div ref className={fit ? fitHost : host}
data-testid="file-pane" />` (the `host` style pins `.cm-editor` to full height) followed by the marks' portals.

### Conventions

Panda `css` from `../../../styled-system/css` (relative import). CodeMirror 6 core (`@codemirror/state`,
`@codemirror/view`); the chrome+token theme and the language map are factored into sibling modules
(`codemirrorTheme`, `langByExtension`). `data-testid="file-pane"`.

### Invariants And Boundaries

**Read-only and non-editable** — set by both `EditorState.readOnly` and `EditorView.editable.of(false)`.
Imperative lifecycle: exactly one `EditorView` per `(content, language, firstLine)` and mark placement; the `disposed` guard prevents
mounting a view after teardown when the async language pack resolves late (no leak, no stale view). It is a
**viewer, not an editor** — content/language changes recreate the editor rather than dispatching
incremental edits. Presentational: no data fetching; the caller supplies already-fetched `content` and the
L1 `language` id, and the caller decides which file line a mark sits on.

## Evidence

### Repo-Internal References

- The sibling theme module defines the CodeMirror chrome plus syntax `HighlightStyle` bundle. [1]
- The `FilePane` module imports the sibling `codeTheme`. [2]
- `FilePane` installs `codeTheme` in the `EditorState` extension list. [3]
- The sibling language module defines the lazy language-by-extension map. [4]
- The `FilePane` module imports the sibling `langExtension`. [5]
- `FilePane` awaits `langExtension` for the requested language, appends a returned extension, and then creates the `EditorView`. [6]
- The optional first line and the content-sized host an expression card uses (MIK-L31). [7]
- The focused card excerpts that pass them (and, since MIK-L34, their drawn sides' intent marks). [8]
- The optional `marks`, the marked pane, the marks gutter first in the extensions, and `drawn` after the build and at teardown (MIK-L34). [9]
- The dual pane that mounts it on the code side. [10]
- The route overview that governs this component. [11]
