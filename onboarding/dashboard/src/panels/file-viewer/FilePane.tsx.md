# dashboard/src/panels/file-viewer/FilePane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/file-viewer/FilePane.tsx`    |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-04T03:03+02:00                             |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`         |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The sibling theme module defines the CodeMirror chrome plus syntax `HighlightStyle` bundle. | `chrome`; `"HighlightStyle.define"`; `codeTheme` | dashboard/src/panels/file-viewer/codemirrorTheme.ts:9-27; dashboard/src/panels/file-viewer/codemirrorTheme.ts:49-49 |
| The `FilePane` module imports the sibling `codeTheme`. | "import { codeTheme }" | dashboard/src/panels/file-viewer/FilePane.tsx:10-10 |
| `FilePane` installs `codeTheme` in the `EditorState` extension list. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:20-50 |
| The sibling language module defines the lazy language-by-extension map. | `langExtension` | dashboard/src/panels/file-viewer/langByExtension.ts:8-49 |
| The `FilePane` module imports the sibling `langExtension`. | "import { langExtension }" | dashboard/src/panels/file-viewer/FilePane.tsx:11-11 |
| `FilePane` awaits `langExtension` for the requested language, appends a returned extension, and then creates the `EditorView`. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:20-50 |
| The dual pane that mounts it on the code side. | `CodeSide`; `DualPane` | dashboard/src/panels/file-viewer/DualPane.tsx:59-71; dashboard/src/panels/file-viewer/DualPane.tsx:90-134 |
| The route overview that governs this component. | `# dashboard/src/panels/file-viewer/ — File Viewer Overview` | onboarding/dashboard/src/panels/file-viewer/overview.md:1-109 |

## Update History

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the four whole-claim ranges (4 repairs, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: split both
  underbound import-plus-behavior groups into source-local import claims and whole-`FilePane`
  behavioral claims. All four changed bindings are provisional `:1-1` inputs for the fresh Luna
  curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: source-first separated the
  sibling theme/language definitions from `FilePane`'s actual imports and consumption. Preserved
  the already-correct generated definition ranges and added only honest `:1-1` bindings for the
  component-owned install/await relationships; no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired and normalized the scoped file-viewer citation claims; final exact frozen-snapshot check is clean.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the reusable read-only CodeMirror 6 code pane (read-only + non-editable, line numbers, line wrapping, the podracer theme, and lazily code-split language packs; imperative `EditorView` lifecycle with a `disposed` guard); reused by L4 via `@codemirror/merge`. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
