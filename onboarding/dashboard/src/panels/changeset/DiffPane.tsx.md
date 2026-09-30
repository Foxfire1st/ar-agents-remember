# dashboard/src/panels/changeset/DiffPane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/changeset/DiffPane.tsx`      |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-09-30T20:14:26+02:00                          |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`         |
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`DiffPane` is the **read-only before/after diff pane** — the one genuinely new CodeMirror primitive L4
adds. It renders a changed file's `before` vs `after` content with `@codemirror/merge`: `split` mounts a
side-by-side `MergeView`, `inline` mounts `unifiedMergeView` over a single `EditorView`. It deliberately
reuses `FilePane`'s exact read-only extension set + `codeTheme` + `langExtension` so tokens are identical
across the L2 plain code pane and this diff.

## Code Commentary

### Logic

Props are `{ before, after, language, mode: "split" | "inline", collapse? = true, firstLine?, fit? = false, marks? }`.
**`marks` was added by MIK-L34 for the reviewer's per-hunk intent markers** and changes nothing when omitted: the pane
takes `useMarkedPane(marks)` from `file-viewer/markGutter.tsx` and gets back `portals`, `placement`, `gutterFor` and
`drawn`. Each editor's first extension is `gutterFor(side, first)`, which is `[]` without marks, so an unmarked pane
builds exactly the landed extensions; with marks it is one exposed gutter whose markers are React content placed on
the pane's own file line numbers. Once the editors exist the pane calls `drawn({ before: { view: merge.a, first },
after: { view: merge.b, first } })` (split) or `drawn({ after: { view, first } })` (inline), which exposes the marks
gutter to assistive technology, expands a collapsed run that holds a mark, and reveals a mark a return asks for;
cleanup calls `drawn(null)` before destroying the view. `placement` (and the two stable callbacks) join the effect's
dependencies, so the editors are rebuilt exactly when a mark moves, and the render is the host `div` followed by the
marks' `portals`. To keep the component under the function-size rule the two view builders were extracted
unchanged into `splitView` and `inlineView`, which share a `DiffBuild` (parent, the two documents, each side's first
line, the `common` extensions, the collapse setting and the marked-pane hooks).
**`firstLine` and `fit` were added by MIK-L31 for the reviewer's focused expression cards** and change nothing when
omitted: `firstLine` gives each side's first line in its file (an excerpt), so the before editor numbers from
`firstLine.before` and the after editor (and the inline editor) from `firstLine.after` through
`file-viewer/lineNumbering.ts`'s `numberedFrom`, which is the plain `lineNumbers()` for line 1; `fit` swaps the
`host` css for `fitHost`, which sizes the editors to their content (`height: auto`, the merge view capped at
`32rem`) so the card, not the pane, scrolls, and keeps the same full-height change highlights. A `ref` points at a
host div; an effect builds the editor: **`langExtension(language)`** is awaited (the `@codemirror/lang-*`
packs are code-split), guarded by a `disposed` flag against a late resolve after teardown. The shared
`common` extension array is `EditorState.readOnly.of(true)`, `EditorView.editable.of(false)`,
`EditorView.lineWrapping`, `codeTheme`, plus the resolved language when one exists.
`collapseUnchanged` is `{ margin: 3 }` when `collapse` (the change-set view) else `undefined`
(full-file view shows everything). For `split` (`splitView`): `new MergeView({ a: {doc: before, extensions:
[gutterFor("before", beforeFirst), numberedFrom(beforeFirst), ...common]}, b: {doc: after, extensions:
[gutterFor("after", afterFirst), numberedFrom(afterFirst), ...common]}, parent, gutter: true, collapseUnchanged })`
— **no `revertControls`**, so the diff is read-only. For `inline` (`inlineView`): `new EditorView({ parent, state
})` whose doc is `after` and whose extensions are `gutterFor("after", afterFirst)`, `unifiedMergeView({ original:
before, mergeControls: false, gutter: true, collapseUnchanged })`, `numberedFrom(afterFirst)` and `common`. Cleanup
sets `disposed = true`, calls `drawn(null)` and `view?.destroy()`. The effect deps are `[before, after, language,
mode, collapse, beforeFirst, afterFirst, placement, gutterFor, drawn]`, so the editor is recreated wholesale when any
change. Render is the `<div ref className={fit ? fitHost : host} data-testid="diff-pane" />` followed by the marks'
portals (none without marks). The `host` css scopes the
editor-fill to the **direct** `.cm-editor` (inline/single-editor mode scrolls via its own `.cm-scroller`)
and makes `.cm-mergeView` the bounded scroll container in split mode — the merge theme grows its inner
editors to content height and forces their scrollers to `overflow:visible`, so a long split diff scrolls
as a whole instead of clipping at the panel edge. The `host` css also overrides `@codemirror/merge`'s
default thin bottom-underline on `.cm-changedText` into a **full-height highlight rectangle** (L4a). Two
parts make it a box: the **height** — a `linear-gradient(...) bottom / 100% 16px no-repeat` band fills the
line box (the library default is ~2px → a line) — and the **colour** — a dark, muted fill, low-lightness
green (`#255a25aa`) for additions (the general rule, covering split `b` + inline) and red (`#5a2525aa`)
for deletions (the more specific `.cm-merge-a .cm-changedText` rule). The fills are intentionally **not**
the `--mint`/`--amber` tokens: those are bright foreground tones and, as a background behind the light
diff text, would wash the glyphs out (a bright fill would need dark text). `!important` is required —
`@codemirror/merge`'s own runtime-injected rule (`.ͼN.cm-merge-b .cm-changedText`) outranks a plain
host-scoped selector.

### Conventions

Panda `css` from `../../../styled-system/css`. `@codemirror/merge` (`MergeView` / `unifiedMergeView`);
the shared theme + language map are reused from the sibling File Viewer (`codemirrorTheme`,
`langByExtension`), so a single highlighter drives both panes. `data-testid="diff-pane"`.

### Invariants And Boundaries

**Read-only** — both editors are `readOnly` + non-editable, `MergeView` omits `revertControls`, and
`unifiedMergeView` sets `mergeControls: false`, so there are no accept/reject affordances. Imperative
lifecycle: exactly one view per `(before, after, language, mode, collapse)`; the `disposed` guard
prevents mounting after teardown when the async language pack resolves late. Presentational: no data
fetching — the caller (`ChangeSetPane`) supplies already-fetched content from the L3 file-diff endpoint. Which line
a mark sits on is the caller's decision (the reviewer's markers use the classification owner's side lines); the pane
only draws what it is given. Every caller that passes no `marks` (`ChangeSetPane`, `KnowledgeStatements`, the family
guarantee diff) renders exactly as before.
`@codemirror/merge` is imported statically (it is in the main bundle).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reuses FilePane's read-only extension set + theme + lang so tokens match plain vs diff. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:25-78 |
| The shared CodeMirror theme (chrome + syntax `HighlightStyle`). | `codeTheme` | dashboard/src/panels/file-viewer/codemirrorTheme.ts:49-49 |
| The lazy language-by-extension map it awaits. | `langExtension` | dashboard/src/panels/file-viewer/langByExtension.ts:8-49 |
| `split` = MergeView (a=before, b=after, no revertControls); `inline` = unifiedMergeView (mergeControls:false); each side numbered from its own first line when an excerpt is shown. | `DiffPane`; `splitView`; `inlineView` | dashboard/src/panels/changeset/DiffPane.tsx:123-193; dashboard/src/panels/changeset/DiffPane.tsx:77-98; dashboard/src/panels/changeset/DiffPane.tsx:100-121 |
| What both builders share, including the marked pane's gutter and `drawn` hooks (MIK-L34). | `DiffBuild` | dashboard/src/panels/changeset/DiffPane.tsx:64-75 |
| The optional `marks` prop, the marked pane, and the teardown that tells it the editors are gone. | "marks?: PaneMarks;"; "const { portals, placement, gutterFor, drawn } = useMarkedPane(marks);"; "drawn(null);" | dashboard/src/panels/changeset/DiffPane.tsx:141-148; dashboard/src/panels/changeset/DiffPane.tsx:179-192 |
| The marks gutter, its portals and the reveal this pane hosts. | `useMarkedPane` | dashboard/src/panels/file-viewer/markGutter.tsx:321-372 |
| The content-sized host an expression card uses (MIK-L31). | `fitHost` | dashboard/src/panels/changeset/DiffPane.tsx:50-60 |
| The gutter that keeps a file's own numbering for an excerpt. | `numberedFrom` | dashboard/src/panels/file-viewer/lineNumbering.ts:7-11 |
| The focused card that passes `firstLine` and `fit`. | `ChangedExcerpt` | dashboard/src/panels/review/ExpressionCards.tsx:463-496 |
| The column wrapper that mounts it and supplies `mode`/`collapse`. | `ChangeSetPane` | dashboard/src/panels/changeset/ChangeSetPane.tsx:177-218 |
| The `FileDiff` (before/after content) the caller passes through. | `FileDiff` | dashboard/src/data/changeset.ts:51-58 |

## Update History
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **body updated for the optional `marks` prop MIK-R34 adds** (Logic, Invariants): `useMarkedPane`, one marks gutter per editor, `drawn` after the build and `drawn(null)` at teardown, `placement` in the effect's dependencies, and the portals after the host; the two view builders extracted unchanged into `splitView` and `inlineView` over a `DiffBuild`, which also retires the removed `base` array from the Logic text. The `DiffPane` row now also names the two builders; three rows added. An unmarked pane is the landed one.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Logic records the optional `firstLine` and `fit` props MIK-L31 adds for the focused expression cards (per-side numbering through `numberedFrom`, the content-sized `fitHost`); the defaults are unchanged. The `DiffPane` row is reworded; three rows added. The file was not prettier-clean on base and was left in its existing style (review R1 F9).
- 2026-09-25T22:19:46+00:00: Generated citation repair: `FileDiff` repointed to dashboard/src/data/changeset.ts:51-58. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-03T02:32:19+02:00 — Curator W3-B02: anchored 5 Repo-Internal citation rows with exact
  CodeMirror/component identifiers, including the `DiffPane` implementation for split/inline
  construction; the existing `FileDiff` citation and verification metadata remain unchanged.

- 2026-06-29T23:00+02:00 — L4a (diff-highlight polish): the `host` css overrides `@codemirror/merge`'s
  default thin underline on `.cm-changedText` into a full-height highlight **rectangle** — a
  `bottom / 100% 16px` band (the height is what makes it a box, not a line) with a dark, muted fill (green
  `#255a25aa` for additions, red `#5a2525aa` for deletions via `.cm-merge-a`), NOT the bright
  `--mint`/`--amber` foreground tokens (which would wash out the light diff text), `!important` to beat the
  library's injected theme. Developer preference. Verification metadata pinned until closeout stamps the
  L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up (scroll fix): the `host` css scopes the `height:100%` editor-fill
  to the DIRECT `.cm-editor` (inline mode) and makes `.cm-mergeView` the bounded scroll container in split
  mode, so a split diff taller than the pane scrolls (the merge theme makes its inner editors grow + their
  scrollers `overflow:visible`) instead of clipping. Verification metadata pinned until closeout stamps the
  L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): the read-only
  `@codemirror/merge` diff pane (split `MergeView` / inline `unifiedMergeView`, collapse toggle, no
  revert/merge controls), reusing FilePane's extension set + theme + lazy language packs via an
  imperative `EditorView`/`MergeView` lifecycle with a `disposed` guard. Verification metadata pinned to
  the task base until closeout stamps the L4 code commit.
