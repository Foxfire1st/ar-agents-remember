# dashboard/src/panels/file-viewer/FilePane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/file-viewer/FilePane.tsx`    |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-29T09:06+02:00                             |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`         |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                      |

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

Props are `{ content, language }`. A `ref` points at the host div; an effect builds the editor:
**`langExtension(language)`** is awaited (the `@codemirror/lang-*` packs are code-split, so a language is
loaded only when first opened), guarded by a `disposed` flag against a late resolve after teardown. The
extension set is `lineNumbers()`, `EditorState.readOnly.of(true)`, `EditorView.editable.of(false)`,
`EditorView.lineWrapping`, and `codeTheme`, plus the resolved language extension when one exists; then
`new EditorView({ parent, state })`. Cleanup sets `disposed = true` and calls `view?.destroy()`. The effect
deps are `[content, language]`, so the editor is **recreated wholesale** when either changes. Render is a
single `<div ref className={host} data-testid="file-pane" />` (the `host` style pins `.cm-editor` to full
height).

### Conventions

Panda `css` from `../../../styled-system/css` (relative import). CodeMirror 6 core (`@codemirror/state`,
`@codemirror/view`); the chrome+token theme and the language map are factored into sibling modules
(`codemirrorTheme`, `langByExtension`). `data-testid="file-pane"`.

### Invariants And Boundaries

**Read-only and non-editable** — set by both `EditorState.readOnly` and `EditorView.editable.of(false)`.
Imperative lifecycle: exactly one `EditorView` per `(content, language)`; the `disposed` guard prevents
mounting a view after teardown when the async language pack resolves late (no leak, no stale view). It is a
**viewer, not an editor** — content/language changes recreate the editor rather than dispatching
incremental edits. Presentational: no data fetching; the caller supplies already-fetched `content` and the
L1 `language` id.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The CodeMirror theme bundle (chrome + syntax `HighlightStyle`) it loads. | L9-L41 | [codemirrorTheme.ts](codemirrorTheme.ts) |
| The lazy language-by-extension map it awaits. | L8-L49 | [langByExtension.ts](langByExtension.ts) |
| The dual pane that mounts it on the code side. | L58-L70 | [DualPane.tsx](DualPane.tsx) |
| The route overview that governs this component. | — | [overview.md](overview.md) |

## Update History

- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the reusable read-only CodeMirror 6 code pane (read-only + non-editable, line numbers, line wrapping, the podracer theme, and lazily code-split language packs; imperative `EditorView` lifecycle with a `disposed` guard); reused by L4 via `@codemirror/merge`. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
