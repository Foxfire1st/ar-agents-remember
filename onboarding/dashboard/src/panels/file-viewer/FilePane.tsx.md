# dashboard/src/panels/file-viewer/FilePane.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FilePane` is the reusable **read-only CodeMirror 6** pane — the shared code primitive of the File
Viewer. `DualPane` mounts it on the code side. L4's Change-Set Viewer reuses it by swapping the single
`EditorView` for `@codemirror/merge` (same editor core + the same `HighlightStyle`, so tokens are
identical across plain and diff views). The `EditorView` is created imperatively in an effect and torn
down on unmount or content change. MIK-R79 rule 9 uses the same pane for the Knowledge reader's cited
code, with the cited lines marked.

## Code Commentary

### Logic

Props are `{ content, language, firstLine? = 1, fit? = false, marks?, highlightedLines? }`.
**`firstLine` and `fit`** (MIK-L31, focused expression cards) number the gutter from the excerpt's
first line in its file and let the editor size to its content instead of full height. **`marks`**
(MIK-L34) draws the reviewer's per-hunk intent markers; omitted, no mark gutter exists. **`highlightedLines`**
(MIK-R79) takes a one-based inclusive `[first, last]` pair on the file's own numbering; the pane adds a
`citationHighlight` decoration over those lines (`cm-citedLine`, `data-located`, `data-line`) and
scrolls the first one to the top of the pane, so a citation opens at its cited lines. An absent pair
changes nothing.

A `ref` points at the host div; an effect awaits `langExtension(language)` (the `@codemirror/lang-*`
packs are code-split, so a language is loaded only when first opened), guarded by a `disposed` flag
against a late resolve after teardown. The extension set is the marks gutter, `numberedFrom(firstLine)`,
`EditorState.readOnly.of(true)`, `EditorView.editable.of(false)`, `EditorView.lineWrapping`,
`codeTheme`, the resolved language when one exists and the citation highlight when asked. Cleanup sets
`disposed`, calls `drawn(null)` and destroys the view. The effect deps include `highlightedLines`, so a
new citation range rebuilds the editor.

### Conventions

Panda `css` from `../../../styled-system/css` (relative import). CodeMirror 6 core; the chrome+token
theme and language map are sibling modules. `data-testid="file-pane"`.

### Invariants And Boundaries

**Read-only and non-editable** — set by both `EditorState.readOnly` and `EditorView.editable.of(false)`.
Exactly one `EditorView` per `(content, language, firstLine)` and mark placement; the `disposed` guard
prevents mounting a view after teardown. It is a **viewer, not an editor** — content, language or
highlight changes recreate the editor rather than dispatching incremental edits. Presentational: no
data fetching; the caller supplies already-fetched content, the language id, and the citation range on
the file's own line numbers.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 9); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The pane marks the cited lines and scrolls the first into view. [12]
- The Knowledge reader's code view passes the resolved cited range here. [13]
- The optional range joins the editor's dependencies and rebuilds the view. [14]
- The dual pane that mounts the same primitive on the code side. [15]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
