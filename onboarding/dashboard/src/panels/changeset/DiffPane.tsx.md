# dashboard/src/panels/changeset/DiffPane.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`DiffPane` is the **read-only before/after diff pane** — the one genuinely new CodeMirror primitive L4
adds. It renders a changed file's `before` vs `after` content with `@codemirror/merge`: `split` mounts a
side-by-side `MergeView`, `inline` mounts `unifiedMergeView` over a single `EditorView`. It deliberately
reuses `FilePane`'s exact read-only extension set + `codeTheme` + server-computed tree-sitter highlight
decorations (`serverHighlightsExtension`) through per-side `Compartment`s so tokens stay identical across
plain and diff views while preserving `INV-QK8XNM` DOM retention across unchanged polls.

## Code Commentary

### Logic

Props are `{ before, after, beforeHighlights?, afterHighlights?, language, mode: "split" | "inline", collapse? = true, firstLine?, fit? = false, marks? }`. Both `splitView` (read-only before/after `MergeView`) and `inlineView` (read-only after editor with `unifiedMergeView`) build synchronously in an effect without async language loading, retaining `codeTheme`, line wrapping, per-side file-relative numbering, independent per-side highlight `Compartment`s (`hlSlots.before`/`hlSlots.after` in split mode; `hlSlot` for after-side highlights in inline mode so widgetized deleted chunks stay untouched), and explicit teardown. No revert or accept/reject control is installed.

Ordinary panes fill their parent and retain the merge-view scrolling and muted word rectangles. A fitted review pane instead grows to its content without a height cap or inner scroller: its merge view and editor scrollers overflow visibly into the review reading column. Its diff uses red/green whole-row bands, a reserved −/+ marker column, alarm-red deletion text while syntax-token colours remain, hatched split spacers and a faint fold bar. It removes nested word boxes and the merge change gutter only in that fitted presentation. [8]

The unchanged-line collapse margin is three when collapse is enabled. `foldKeys` marks each collapse widget as a focusable button with an accessible expansion label; Enter or Space invokes the widget’s click, expanding that stretch in place. Full-context callers can disable collapse.

Each builder returns its editor identities, a dedicated `Compartment` for each marks gutter, and a dedicated `Compartment` for each side's server highlights (`Built.highlights`). `useMarkedPane` still supplies portals, placement, gutterFor and drawn; callers continue to own the marked line/side. For fitted panes a placement update reconfigures those mark compartments in the existing editors and reports them drawn, keeping the current content while marks arrive. For ordinary panes placement remains a rebuild dependency. `beforeHighlights` and `afterHighlights` are kept in `latestHighlights` (synced in `useLayoutEffect`) and deliberately excluded from the rebuild effect dependencies; a separate effect keyed on `beforeDigest` and `afterDigest` (`highlightDigest`) reconfigures each side's highlight `Compartment` in place so unchanged 2.5 s polls retain the mounted CodeMirror DOM node (`INV-QK8XNM`). Content/mode/collapse/first-line changes rebuild cleanly with explicit teardown calling `drawn(null)` and `destroy()`. [6]

### Conventions

Panda `css` from `../../../styled-system/css`. `@codemirror/merge` (`MergeView` / `unifiedMergeView`);
the shared theme and server-highlight decoration mapper are reused from the sibling File Viewer
(`codemirrorTheme`, `serverHighlights`), so a single server highlighter drives both panes. `data-testid="diff-pane"`.

### Invariants And Boundaries

**Read-only** — both editors are `readOnly` + non-editable, `MergeView` omits `revertControls`, and
`unifiedMergeView` sets `mergeControls: false`, so there are no accept/reject affordances. Synchronous
imperative lifecycle: exactly one view per `(before, after, mode, collapse, beforeFirst, afterFirst,
rebuildOn)`; per-side highlight `Compartment`s reconfigure in place by digest without destroying the
mounted DOM node (`INV-QK8XNM`). Presentational: no data fetching — the caller (`ChangeSetPane` or
`ExpressionCards`) supplies already-fetched content and optional per-side `SyntaxHighlights`. Which line
a mark sits on is the caller's decision (the reviewer's markers use the classification owner's side lines); the pane
only draws what it is given. The no-marks gutter remains empty. Fitted statement and guarantee callers still receive the new fitted sizing and diff presentation; ordinary ChangeSetPane retains the ordinary host.
`@codemirror/merge` is imported statically (it is in the main bundle).

## Evidence

### Repo-Internal References

- Reuses FilePane's read-only extension set, `codeTheme`, and server-highlight decorations so tokens match plain vs diff. [1]
- The shared CodeMirror theme (chrome + foreground-only `.cm-ar-tok-*` token classes). [2]
- The server-computed UTF-16 `Decoration.mark` extension and digest helper replacing `langByExtension.ts`. [3]
- `splitView` = MergeView (a=before, b=after, independent per-side highlight compartments, no revertControls); `inlineView` = unifiedMergeView (after-side highlight compartment, mergeControls:false); each side numbered from its own first line. [4]
- What both builders share (`DiffBuild`, `Built`, `commonExtensions`), including per-side mark and highlight compartments. [5]
- Synchronous build effect with per-side highlight `Compartment` reconfiguration by digest (`INV-QK8XNM`) and fitted mark-gutter reconfiguration. [6]
- The marks gutter, its portals and the reveal this pane hosts. [7]
- The content-sized host (`fitHost`) an expression card uses. [8]
- The gutter that keeps a file's own numbering for an excerpt. [9]
- The focused card that passes `firstLine`, `fit`, and per-side highlights. [10]
- The column wrapper that mounts it and supplies `mode`, `collapse`, and per-side highlights. [11]
- The FileDiff contract carries before and after sides with optional `SyntaxHighlights` on text sides and `null` on binary/media sides. [12]
- Folds expose native keyboard-equivalent expansion. [13]
- Fitted mark updates reconfigure dedicated gutter compartments without destroying current editors. [14]
