# dashboard/src/panels/file-viewer/markGutter.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

**Marks on file lines of a read-only CodeMirror pane (added by MIK-L34 for the reviewer's per-hunk intent markers,
MIK-R34).** One gutter whose markers are React content, placed on the pane's own file line numbers, so an excerpt keeps
its file's numbering. `DiffPane` and `FilePane` take an optional `marks` and hand it to `useMarkedPane`; without marks
there is no gutter at all and the pane is exactly the landed one. The pane only places what it is given: which line a
mark sits on is the caller's decision (the reviewer places each mark on the classification owner's side lines, in
`review/hunkMarkers.ts`). Besides placing, this module exposes the marks to assistive technology, keeps a marked line
out of a collapsed run, and brings a returned-to mark back into view with focus on it, without ever fighting the
reader.

## Code Commentary

### Logic

- **Types.** `PaneMark` is `{ id, side: 'before' | 'after', line, label, compact?, node }`: the editor it sits in, the
  file line, the text that sizes the gutter (and the shorter one a phone-width gutter uses) and the React content.
  `PaneMarks` is the list plus `reveal` (a mark to bring into view and focus once drawn: a return) and `onRevealed`.
- **Hosts and portals.** `useMarkedPane(marks)` owns one host element (`span.cm-paneMarkHost`, `hostEntry`) per mark
  id for the life of that id, and portals each mark's `node` into its host, so a mark stays one React tree while
  CodeMirror draws and drops gutter elements as lines scroll. `HostMarker` (a `GutterMarker`) wraps the host in a
  fresh `div.cm-paneMark` every time it is drawn, so CodeMirror removes the node it drew, never a host a later draw
  moved elsewhere.
- **The gutter.** `markGutter(marks, hosts, first)` returns `[]` for no marks; otherwise one `gutter` with class
  `cm-paneMarks` whose marker set (`markerSet`, cached per document) places each mark on `docLine(line, first)`, and a
  theme sizing it to the widest label (at most `MARK_WIDTH`, 12 characters, plus `MARK_CHROME`). **Below 40rem it is
  sized to the widest compact text** (at most `NARROW_MARK_WIDTH`, 5, plus `NARROW_MARK_CHROME`; review R1 F2), so a
  side-by-side diff at 390 px keeps a code column (the review measured 17 px of marks gutter where it had been 74).
  `gutterFor(side, first)` filters the marks for one editor (`'all'` for a single-editor pane).
- **After the build (`drawn`).** The pane calls `drawn({ before?, after })` once its editors exist (`null` at
  teardown). It exposes the marks (`exposeMarks`: CodeMirror marks its whole gutter column `aria-hidden`; with a marks
  gutter present the column is exposed and the other gutters, line numbers and the change bar, are hidden
  individually), expands every collapsed run that holds a mark (`expandMarkedRuns`, below), and runs the reveal.
- **No mark in a collapsed run (ruling 2026-09-30T16:19:34 Q4).** "Changed regions" collapses runs of lines the
  diff's own chunks leave unchanged, and the owner's hunks are not those chunks. `collapsedRunAt` finds a mark's line
  inside a collapsed-run widget (`collapsed-unchanged-code`); `expandMarkedRuns` dispatches the merge package's own
  `uncollapseUnchanged` there and, in a side-by-side diff, in the sibling editor at the position `siblingPos` maps over
  `getChunks`, as the merge view's own expand control does. A run holding no mark stays collapsed.
- **The reveal.** When `marks.reveal` names a mark, `revealMark` scrolls its editor to the line
  (`EditorView.scrollIntoView`, centred), waits up to `REVEAL_FRAMES` (30) animation frames for CodeMirror to draw the
  host, focuses the mark's button without scrolling, scrolls the host into view, calls `onRevealed`, and starts the
  hold. `placement` (every mark's id, side, line, label and compact text) changes exactly when a mark moves, so a pane
  rebuilds only then.
- **The hold (review R2-F1, R3-F1, R3-F2).** For at most `REVEAL_HOLD_FRAMES` (45) frames `holdRevealed` runs
  `keepRevealed`: an undrawn mark's line is scrolled to again; a drawn mark is refocused if a redraw left focus on the
  body, and scrolled back into view if it left its diff's own scroll box (`.cm-mergeView` or `.cm-scroller`) or the
  window (`inView`). CodeMirror measures wrapped lines and a side-by-side view realigns its editors after the first
  scroll, which at 390 px moved the mark out of view or blurred it. The hold ends at the reader's own `pointerdown`,
  `keydown` or `wheel` (`HOLD_RELEASES`: capture, `once`, **passive** listeners; the wheel was added by R3-F1 because
  a wheel or trackpad scroll fires neither of the others), when focus moves elsewhere, when the pane is torn down, or
  at the frame cap; it then asks for no more frames and removes the three listeners.
- **Focus kept across a redraw (review R2-F1).** A redraw moves a mark between gutter elements, and moving or
  detaching a focused element blurs it. `HostMarker.destroy` remembers the control that held focus (`carried`) for the
  rest of that update (a microtask); `toDOM` gives focus back to it once the host is attached again
  (`refocusWhenAttached`), and only while focus is on the body (`focusLost`), so a reader's own move is never undone.

### Conventions

- CodeMirror's own API (`gutter`, `GutterMarker`, `RangeSet`, `EditorView.theme`, the merge package's
  `uncollapseUnchanged` and `getChunks`) and React portals; no diff framework of its own (MIK-R34 Exclusions).
- `HostMarker`, `holdRevealed`, `Revealed` and `REVEAL_HOLD_FRAMES` are exported for their frame-by-frame tests
  (jsdom cannot drive CodeMirror's element reassignment); `Revealed.view` needs only the editor's `dom`.
- No fetch and no knowledge of hunks, links or families.

### Invariants And Boundaries

- An unmarked pane is exactly the landed pane: `markGutter` returns no extension, `exposeMarks` returns early, and
  the pane's effect dependencies are stable.
- **A marked line is never hidden in a collapsed run**, and a run holding no mark keeps its landed collapse (part of
  the candidate invariant "every hunk drawn in any diff surface carries its mark", recorded on `IntentMarkers.tsx.md`).
- **The reveal and its hold never take focus or scroll away from the reader** (part of the candidate invariant "Back
  returns focus to the originating marker with its hunk in view", recorded on `MarkerTargetState.tsx.md`): the hold
  is bounded (45 frames), passive, ends at the reader's first pointer, key or wheel, at focus moved elsewhere and at
  teardown, and the redraw carry acts only while focus is on the body. Proved by `markGutter.test.tsx`'s hold and
  redraw cases (the reviewer's mutations H1–H10 are all caught) and the R2 and R3 browser checks at 390 and 1600 px.
- Marks outside CodeMirror's drawn viewport are not in the DOM, so not in the tab order (review R1 N2, accepted).

### Todos

No additional work is asserted by this card. The collapsed-run expansion expands the whole run, which the ruling
allows; a narrower window around the mark would need a collapse of its own.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: React content in one gutter, on the pane's own file lines; the caller decides the line; a fresh wrapper per draw. [1]
- A mark and a pane's marks, with the reveal a return asks for. [2]
- The gutter widths (the phone-width compact gutter, review R1 F2) and the reveal and hold frame counts. [3]
- Focus kept across a redraw, only while focus is on the body (review R2-F1). [4]
- The marker set on the pane's own file lines, and the gutter that is absent without marks. [5]
- The hold: bounded, released by the reader's pointer, key or wheel (passive), by focus moved elsewhere and by teardown; listeners removed. [6]
- The reveal: scroll to the line, focus the mark once drawn, then hold. [7]
- The marks exposed to assistive technology; line numbers and change bar stay hidden. [8]
- A collapsed run holding a mark is expanded, in the sibling editor too (ruling Q4). [9]
- What a pane gets: portals, placement, the gutter per editor and `drawn`. [10]
- The two panes that host it. [11]
- The collapsed-run, redraw and hold cases. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
