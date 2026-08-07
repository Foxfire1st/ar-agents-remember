# dashboard/src/panels/changeset/DiffPane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/changeset/DiffPane.tsx`      |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-29T23:00+02:00                             |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`         |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

Props are `{ before, after, language, mode: "split" | "inline", collapse? = true }`. A `ref` points at a
host div; an effect builds the editor: **`langExtension(language)`** is awaited (the `@codemirror/lang-*`
packs are code-split), guarded by a `disposed` flag against a late resolve after teardown. The shared
`base` extension array is `lineNumbers()`, `EditorState.readOnly.of(true)`,
`EditorView.editable.of(false)`, `EditorView.lineWrapping`, `codeTheme`, plus the resolved language when
one exists. `collapseUnchanged` is `{ margin: 3 }` when `collapse` (the change-set view) else `undefined`
(full-file view shows everything). For `split`: `new MergeView({ a: {doc: before, extensions: base}, b:
{doc: after, extensions: base}, parent, gutter: true, collapseUnchanged })` — **no `revertControls`**, so
the diff is read-only. For `inline`: `new EditorView({ parent, state })` whose doc is `after` and whose
extensions are `unifiedMergeView({ original: before, mergeControls: false, gutter: true, collapseUnchanged
})` plus `base`. Cleanup sets `disposed = true` and calls `view?.destroy()`. The effect deps are
`[before, after, language, mode, collapse]`, so the editor is recreated wholesale when any change. Render
is a single `<div ref className={host} data-testid="diff-pane" />`. The `host` css scopes the
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
fetching — the caller (`ChangeSetPane`) supplies already-fetched content from the L3 file-diff endpoint.
`@codemirror/merge` is imported statically (it is in the main bundle).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reuses FilePane's read-only extension set + theme + lang so tokens match plain vs diff. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:20-50 |
| The shared CodeMirror theme (chrome + syntax `HighlightStyle`). | `codeTheme` | dashboard/src/panels/file-viewer/codemirrorTheme.ts:49-49 |
| The lazy language-by-extension map it awaits. | `langExtension` | dashboard/src/panels/file-viewer/langByExtension.ts:8-49 |
| `split` = MergeView (a=before, b=after, no revertControls); `inline` = unifiedMergeView (mergeControls:false). | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-118 |
| The column wrapper that mounts it and supplies `mode`/`collapse`. | `ChangeSetPane` | dashboard/src/panels/changeset/ChangeSetPane.tsx:177-218 |
| The `FileDiff` (before/after content) the caller passes through. | `FileDiff` | dashboard/src/data/changeset.ts:34-41 |

## Update History

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
