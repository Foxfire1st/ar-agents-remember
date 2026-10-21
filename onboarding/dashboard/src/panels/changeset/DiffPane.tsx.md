# dashboard/src/panels/changeset/DiffPane.tsx

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

Props are `{ before, after, language, mode: "split" | "inline", collapse? = true, firstLine?, fit? = false, marks? }`. The split builder makes a read-only before/after MergeView; the inline builder makes a read-only after editor with unifiedMergeView. Both retain shared theme, async language resolution, wrapping, per-side file-relative numbering and explicit teardown. No revert or accept/reject control is installed.

Ordinary panes fill their parent and retain the merge-view scrolling and muted word rectangles. A fitted review pane instead grows to its content without a height cap or inner scroller: its merge view and editor scrollers overflow visibly into the review reading column. Its diff uses red/green whole-row bands, a reserved −/+ marker column, alarm-red deletion text while syntax-token colours remain, hatched split spacers and a faint fold bar. It removes nested word boxes and the merge change gutter only in that fitted presentation. [8]

The unchanged-line collapse margin is three when collapse is enabled. `foldKeys` marks each collapse widget as a focusable button with an accessible expansion label; Enter or Space invokes the widget’s click, expanding that stretch in place. Full-context callers can disable collapse.

Each builder now returns its editor identities and a dedicated Compartment for each marks gutter. `useMarkedPane` still supplies portals, placement, gutterFor and drawn; callers continue to own the marked line/side. For fitted panes a placement update reconfigures those compartments in the existing editors and reports them drawn, keeping the current content while marks arrive. For ordinary panes placement remains a rebuild dependency. Content/language/mode/collapse/first-line changes still rebuild; the disposed guard prevents a late language load from mounting after cleanup, which reports drawn(null) and destroys the current construction. [6]

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
only draws what it is given. The no-marks gutter remains empty. Fitted statement and guarantee callers still receive the new fitted sizing and diff presentation; ordinary ChangeSetPane retains the ordinary host.
`@codemirror/merge` is imported statically (it is in the main bundle).

## Evidence

### Repo-Internal References

- Reuses FilePane's read-only extension set + theme + lang so tokens match plain vs diff. [1]
- The shared CodeMirror theme (chrome + syntax `HighlightStyle`). [2]
- The lazy language-by-extension map it awaits. [3]
- `split` = MergeView (a=before, b=after, no revertControls); `inline` = unifiedMergeView (mergeControls:false); each side numbered from its own first line when an excerpt is shown. [4]
- What both builders share, including the marked pane's gutter and `drawn` hooks (MIK-L34). [5]
- The marks gutter, its portals and the reveal this pane hosts. [7]
- The gutter that keeps a file's own numbering for an excerpt. [9]
- The focused card that passes `firstLine` and `fit`. [10]
- The column wrapper that mounts it and supplies `mode`/`collapse`. [11]
- The `FileDiff` (before/after content) the caller passes through. [12]

- Fitted panes reconfigure marks in existing editors; content changes and ordinary mark changes rebuild with guarded teardown. [6]
- The content-sized host an expression card uses (MIK-L31). [8]
- Folds expose native keyboard-equivalent expansion. [13]
- Fitted mark updates reconfigure dedicated gutter compartments without destroying current editors. [14]
