# dashboard/src/panels/file-viewer/FilePane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/file-viewer/FilePane.tsx`    |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-09-30T10:05:09+02:00                          |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`         |
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
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

Props are `{ content, language, firstLine? = 1, fit? = false }`. **`firstLine` and `fit` were added by MIK-L31 for
the reviewer's focused expression cards** and change nothing at their defaults: `firstLine` numbers the gutter from
the excerpt's first line in its file (`numberedFrom` in the sibling `lineNumbering.ts`, which is the plain
`lineNumbers()` for line 1), and `fit` swaps the `host` style for `fitHost`, which sizes the editor to its content
(capped at `32rem`) instead of pinning it to full height. A `ref` points at the host div; an effect builds the editor:
**`langExtension(language)`** is awaited (the `@codemirror/lang-*` packs are code-split, so a language is
loaded only when first opened), guarded by a `disposed` flag against a late resolve after teardown. The
extension set is `numberedFrom(firstLine)`, `EditorState.readOnly.of(true)`, `EditorView.editable.of(false)`,
`EditorView.lineWrapping`, and `codeTheme`, plus the resolved language extension when one exists; then
`new EditorView({ parent, state })`. Cleanup sets `disposed = true` and calls `view?.destroy()`. The effect
deps are `[content, language, firstLine]`, so the editor is **recreated wholesale** when any changes. Render is a
single `<div ref className={fit ? fitHost : host} data-testid="file-pane" />` (the `host` style pins `.cm-editor`
to full height).

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
| The sibling theme module defines the CodeMirror chrome plus syntax `HighlightStyle` bundle. | `chrome`; `"HighlightStyle.define"`; `codeTheme` | dashboard/src/panels/file-viewer/codemirrorTheme.ts:9-27; dashboard/src/panels/file-viewer/codemirrorTheme.ts:49-49; dashboard/src/panels/file-viewer/codemirrorTheme.ts:29-29 |
| The `FilePane` module imports the sibling `codeTheme`. | "import { codeTheme }" | dashboard/src/panels/file-viewer/FilePane.tsx:10-10 |
| `FilePane` installs `codeTheme` in the `EditorState` extension list. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:24-64 |
| The sibling language module defines the lazy language-by-extension map. | `langExtension` | dashboard/src/panels/file-viewer/langByExtension.ts:8-49 |
| The `FilePane` module imports the sibling `langExtension`. | "import { langExtension }" | dashboard/src/panels/file-viewer/FilePane.tsx:12-12 |
| `FilePane` awaits `langExtension` for the requested language, appends a returned extension, and then creates the `EditorView`. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:24-64 |
| The optional first line and the content-sized host an expression card uses (MIK-L31). | `fitHost`; "numberedFrom(firstLine)," | dashboard/src/panels/file-viewer/FilePane.tsx:22-22; dashboard/src/panels/file-viewer/FilePane.tsx:47-47 |
| The focused card excerpts that pass them. | `UnchangedExcerpt`; `SeparateSides` | dashboard/src/panels/review/ExpressionCards.tsx:420-430; dashboard/src/panels/review/ExpressionCards.tsx:467-483 |
| The dual pane that mounts it on the code side. | `CodeSide`; `DualPane` | dashboard/src/panels/file-viewer/DualPane.tsx:59-71; dashboard/src/panels/file-viewer/DualPane.tsx:90-134 |
| The route overview that governs this component. | `# dashboard/src/panels/file-viewer/ — File Viewer Overview` | onboarding/dashboard/src/panels/file-viewer/overview.md:1-118 |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Logic records the optional `firstLine` and `fit` props MIK-L31 adds for the focused expression cards (the gutter through `numberedFrom`, the content-sized `fitHost`); the defaults are unchanged. Two rows added. The file was not prettier-clean on base and was left in its existing style (review R1 F9).
- 2026-09-30T07:50:28+00:00: Generated citation repair: "import { langExtension }" repointed to dashboard/src/panels/file-viewer/FilePane.tsx:12-12. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

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
