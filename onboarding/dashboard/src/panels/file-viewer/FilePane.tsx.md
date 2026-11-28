# dashboard/src/panels/file-viewer/FilePane.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FilePane` is the reusable **read-only CodeMirror 6** pane — the shared code primitive of the File
Viewer. `DualPane` mounts it on the code side. L4's Change-Set Viewer reuses it by swapping the single
`EditorView` for `@codemirror/merge` (same editor core + the same `codeTheme` and server-computed
tree-sitter `Decoration.mark` spans, so tokens are identical across plain and diff views). The
`EditorView` is created synchronously in an effect and torn down on unmount or content change, while
`highlights` updates reconfigure a `Compartment` in place without rebuilding the DOM node. MIK-R79 rule 9
uses the same pane for the Knowledge reader's cited code, with the cited lines marked.

## Code Commentary

### Logic

Props are `{ content, language, highlights?, firstLine? = 1, fit? = false, marks?, highlightedLines?, trayLines? }`.
**`highlights`** accepts optional server-computed `SyntaxHighlights | null` and is applied via
`serverHighlightsExtension` inside a dedicated `Compartment` (`slot`). **`firstLine` and `fit`** (MIK-L31, focused expression cards) number the gutter from the excerpt's
first line in its file and let the editor grow to its content without an inner scroll box or height cap; the fitted review reading column owns scrolling.  **`marks`**
(MIK-L34) draws the reviewer's per-hunk intent markers; omitted, no mark gutter exists. **`highlightedLines`**
(MIK-R79) takes a one-based inclusive `[first, last]` pair on the file's own numbering; the pane adds a
`citationHighlight` decoration over those lines (`cm-citedLine`, `data-located`, `data-line`) and
scrolls the first one to the top of the pane, so a citation opens at its cited lines. An absent pair
changes nothing.

A `ref` points at the host div; the build effect creates `EditorView` synchronously with a fresh
`Compartment` (`slot`), reading `latestHighlights.current` (synced in `useLayoutEffect`) without
putting `highlights` in the rebuild dependency array. The extension set is built by `buildExtensions`:
the marks gutter, `numberedFrom(firstLine)`, an optional `trayLineGutter` when repository, scope and path
are all supplied, `EditorState.readOnly.of(true)`, `EditorView.editable.of(false)`,
`EditorView.lineWrapping`, `codeTheme`, `slot.of(serverHighlightsExtension(highlights, doc.length))`, and
the citation highlight when asked. A separate effect keyed solely on `highlightDigest(highlights)`
dispatches `slot.reconfigure(...)` in place so unchanged 2.5 s polls retain the mounted `EditorView`
(`INV-QK8XNM`). Cleanup calls `drawn(null)`, destroys the view, and clears `built.current`. The build
effect deps include `highlightedLines`, so a new citation range rebuilds the editor.

### Conventions

Panda `css` from `../../../styled-system/css` (relative import). CodeMirror 6 core; the chrome+token
theme (`codemirrorTheme.ts`) and server-highlight decoration mapper (`serverHighlights.ts`) are sibling
modules. `data-testid="file-pane"`.

### Invariants And Boundaries

**Read-only and non-editable** — set by both `EditorState.readOnly` and `EditorView.editable.of(false)`.
Exactly one `EditorView` per `(content, firstLine, placement, highlightedLines, trayTarget)`. It is a
**viewer, not an editor** — content or citation-range changes recreate the editor, while `highlights`
updates reconfigure the highlight `Compartment` in place by digest so the CodeMirror DOM node stays
mounted across polls. Presentational: no data fetching; the caller supplies already-fetched content, the
language id, optional server-computed `highlights`, and the citation range on the file's own line numbers.

### Todos

No additional work is asserted by this card.

`trayLines` supplies a repository/scope/path target. The File Viewer passes it through DualPane; absent or incomplete identity supplies no tray gutter, so other callers retain their existing pane. The effect tracks those three primitive target values and rebuilds if the target changes. FilePane delegates line collection to the gutter; it creates no chat or message body.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 9); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The pane marks the cited lines and scrolls the first into view. [12]
- The Knowledge reader's text-code view renders FilePane and passes the resolved cited line range as highlightedLines alongside server highlights. Media citations use the separate media view. [13]
- The optional range joins the editor's dependencies and rebuilds the view, while `highlights` updates reconfigure `slot` in place by digest. [14]
- The dual pane that mounts the same primitive on the code side. [15]
- The File Viewer-only optional tray target enables the line gutter; other panes omit it. [16]
- Fitted review source grows into the reading column without an inner scroller. [17]
