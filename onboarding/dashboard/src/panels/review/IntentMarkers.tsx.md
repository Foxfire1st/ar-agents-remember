# dashboard/src/panels/review/IntentMarkers.tsx

## Governing Overview

[Review route overview](overview.md)

## Purpose

Draw per-hunk intent markers from the supplied per-file classification, list the intersecting realization and proof entries separately, and follow a selected occurrence through the review page's marker scope. This module's active source reader is the card-excerpt hook. The former whole-source reader and bounded-past-text note are removed.

## Code Commentary

`usePaneMarking` takes a path, pane identity, classification, layout and drawn window. A file-level classification supplies its file note; otherwise `fileMarks` and `markAnchor` place each owner hunk that this window draws. The pane identity pairs a return with its original hunk, reopens its list and passes the return to the gutter's reveal/settle protocol. The old `whole` input and `PastTextNote` branch no longer exist.

`MarkButton` keeps the full hunk label, side spans, title and accessible name. Below 40rem its visual text is compact. `MarkPanel` keeps Intents and Tests as separate groups; proof facets, entry IDs, revisions and each family occurrence remain visible. A linked-range intersection does not assert coverage, correctness or preservation. The module delegates intersection and tone computation to `hunkMarkers.ts`.

`useExcerptMarking` requests classification only for a changed file while its `visible` input is true. Each drawn resolved side supplies an excerpt window; `drawnSidesMatch` checks only those drawn sides' blobs against the classification, so an unreadable opposite side does not discard the drawn side's marks. The pane identity is `card-excerpt:<key>`. The old `useSourceMarking`, `describesDrawn` and `sourceInput` exports are absent; this module no longer supplies a full-file source-content hook.

A changed excerpt that has a scope and is listed, or is unlisted under a partial inventory, reserves `MarkStateRow` from its first render. Its fixed 1.5rem height and single-line ellipsis keep loading, ready, unavailable and other-content transitions from adding height to this status row. `MarkStateRow` copies its whole current text into the title and removes an empty title. This local row mechanism is not a fresh browser-layout result or a proof of every surrounding editor's geometry.

`MarkReadNote` distinguishes unlisted, loading, unavailable-with-code/detail and drawn-content mismatch. Excerpt loading says `intent marks loading…`; its retained non-excerpt branch has different wording. The row can be empty after a successful read. `sideMarks` filters marks to one editor side. `MarkerReturn` offers the scope's Back action while an origin remains; selection restoration and actual gutter focus are owned elsewhere.

## Invariants And Boundaries

No marker is synthesized from source prose, and no intersection is computed here. A missing scope or pane input yields no marking. Visibility is a caller input: this hook gates its request from that value and does not itself observe the viewport. Its fixed status row supports stable reading position without certifying the separately ruled browser checks.

The current card owner passes visibility into all three excerpt renderers and draws the returned marker note/panel beside the excerpt. Stored renderer cases that use whole-file fixture text still draw a card excerpt; they do not restore the removed full-file API. Collapsed-run expansion belongs to the gutter: it opens the marked run and, when present, its mapped sibling run.

## Evidence

- Markers are read from the per-file classification and drawn in the diff gutter. [1]
- The pane input names path, pane, classification, layout and window; whole-source state is absent. [2]
- Pane placement and returning-hunk matching reopen the originating list and pass reveal/settle to the gutter. [3]
- The hunk control exposes label, ranges, expansion and compact visual text through its declared styles and attributes. The hunk button retains its full accessible name and title. [4]
- The panel and entry lists retain separate realization/proof groups, facets, occurrence targets and intersection-only wording. [5]
- File-level notes distinguish confirmed unexplained from unreadable attribution; the old past-text component is removed. [6]
- Excerpt windows check only drawn side blobs and classify a changed card only when visible. [8]
- Unlisted, loading, unavailable and mismatched-content reasons remain explicit. [9]
- Side filtering and the scope Back control remain exported. [10]
- A potentially meaningful marker-status row is reserved before the read, with fixed height, ellipsis and full current text in its title. [15]
- Stored card-renderer tests cover owner-side hunk placement, separate proof lists, explicit unavailable/mismatch states and marker return. Whole-file fixture texts are supplied as card excerpts; the removed full-file reader is not exercised. [12]
- Unchanged, changed and separate-side card excerpts pass their visibility input to useExcerptMarking and render its note/panel with the excerpt; no SourceContent full-file caller remains in this card owner. [13]
- A marker inside a collapsed run dispatches uncollapseUnchanged for that run and its mapped sibling run where both editors exist. [14]

## Historical predecessor account

The former account is retained below as provenance. Removed exports, old restoration fields and old test-world identities are historical where the current account differs; earlier execution statements are not fresh results.

> # dashboard/src/panels/review/IntentMarkers.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **The reviewer's per-hunk intent markers in its diffs (MIK-R34, adopting ICR-R34@v1): each hunk of a changed text file
> names the invariants whose recorded ranges meet its changed lines; following one opens that invariant at its tree
> position, and `Back to <file>` returns to the hunk with focus on its marker.** Every mark comes from the one per-file
> classification (MIK-R32) through `hunkMarkers.ts`, placed on the side line numbers it names, and sits in the diff's own
> gutter (`file-viewer/markGutter.tsx`); a mark's list opens below the pane. The module serves every diff surface of a
> tree comparison's workspace that still use these readers: the cards' full-file source-content view and
> card excerpts. The retired explorer/lane full-file and focused-window callers are not current integration
> surfaces. Nothing here
> edits, comments on or assesses a change (the adopted Exclusions).
>
> ## Code Commentary
>
> ### Logic
>
> - **One pane's marks (`usePaneMarking`).** Given `{ path, pane, file, layout, window, whole? }` inside the workspace's
>   scope: a file with a file-level mark gets only that note (`FileMarkNote`); otherwise every owner hunk is placed by
>   `markAnchor`, and each placed hunk becomes a `PaneMark` whose node is its `MarkButton`. The pane name
>   (including `card:<key>` and `card-excerpt:<key>`) makes a return land in the
>   pane the marker was followed from: `returningHunk` picks the scope's `returning` hunk for this path and pane, which
>   becomes the gutter's `reveal` and reopens its list (initial state and effect), and `onRevealed` is the scope's
>   `settle`. A whole-text pane names the hunks it could not place (`PastTextNote`: past the bounded text) instead of
>   dropping them.
> - **The mark (`MarkButton`).** A button with `data-mark` (tone), `data-hunk`, `data-before`/`data-after` spans and
>   `data-compact`; `aria-expanded`, `aria-controls` while open, and `aria-label`/`title` `<label> · hunk before L…,
>   after L…`. **Below 40rem it shows the compact text** through `::after` from `data-compact`, with the full label kept
>   as its hidden text, name and title (review R1 F2).
> - **The list (`MarkPanel`, `EntryList`).** The label and spans, a Close control, "Intents (n)" for realization
>   entries and "Tests (n)" for proof entries (each marked `· test` with its facets), each entry with its revisions and
>   entry ids and one button per family occurrence (`occurrenceLabel`, its sides and revision) that follows the target
>   through the scope (`follow({ path, pane, hunk }, target)`); the per-side unknown lines; and one sentence per tone,
>   for a linked hunk "Listed because a recorded range meets a changed line of this hunk; that asserts no coverage,
>   correctness or preservation." (ICR-R34 rule 5).
> - **File-level mark.** `FileMark` and
>   `FileMarkNote`: one mark for the whole file of a confirmed-unregistered path, or one note that neither side's
>   knowledge could be read; nothing for a file with per-hunk marks or outside a workspace.
> - **The source-content view (`useSourceMarking`).** For a changed file it uses
>   `useMarkClassification`, accepting a classification if its caller already holds one. The current
>   card Full file caller supplies the pane name and uses the shared scope read, not a lane Full file
>   owner. Marks are placed only when the classification describes the drawn blobs, over each whole
>   side in the shown layout, prefixed by `MarkReadNote`.
> - **Never silence (`MarkReadNote`).** A changed file shows why it has no marks: `unlisted` ("the change inventory is
>   partial and does not list this path, so its classification is not read"; review R1 F5), `loading`, `unavailable`
>   with the owner's code and detail, or `other-content` ("the classification describes other content of this path
>   than the text drawn here"). Card excerpts request excerpt presentation and show `intent marks loading…` while pending. The full-file default remains `reading this file's intent marks…`; unavailable and drawn-content mismatch states remain explicit.
> - **Card excerpts (`useExcerptMarking`; ruling Q4, review R1 F1).** Active only for a card whose two blobs differ (an
>   unchanged file's card asks nothing; review R2). `excerptWindow` gives the lines each drawn side's resolved range
>   covers; `drawnSidesMatch` compares **only the sides the excerpt draws** with the classification's blobs, so an
>   unreadable memory side, which serves no blob, never removes the drawn side's marks, and a drawn side of other
>   content says so. The pane is `card-excerpt:<key>`. `useExcerptMarking` passes the `excerpt` flag to `MarkReadNote`. An unchanged-range excerpt of a changed file is distinct from a genuinely unchanged file, which requests no classification.
> - **Helpers and the return.** `sideMarks` gives a one-sided pane its side's marks. `MarkerReturn` renders
>   `← Back to <file name>` (with `data-return-path`, `-pane`, `-hunk`, the full path as title) while a followed marker
>   has not been returned to; its click is the scope's `back`.
>
> ### Conventions
>
> - Test ids: `review-hunk-mark`, `review-hunk-mark-panel`, `review-hunk-mark-group`, `review-hunk-mark-entry`,
>   `review-hunk-mark-facet`, `review-hunk-mark-occurrence`, `review-hunk-mark-unknown`, `review-file-mark`,
>   `review-marks-past-text`, `review-marks-state` (with `data-marks-state`), `review-marker-return`.
> - Panda `css` constants in the file; the tones reuse the lane's colours (cyan linked, amber unexplained, dashed muted
>   unknown).
> - The mark button carries `data-path`, which also keeps the surface's generic button chrome off a gutter mark.
>
> ### Invariants And Boundaries
>
> - **Candidate invariant (not ingested): surviving card full-file/excerpt surfaces mark the owner hunks
>   they draw, including hunks inside collapsed runs.** Realized by `usePaneMarking` (every owner hunk a
>   pane draws is placed), `useSourceMarking` (full files), `useExcerptMarking` (card excerpts, only the drawn sides
>   compared) and `markGutter.expandMarkedRuns` (no mark in a collapsed run, ruling Q4); a mark is
>   withheld only when the drawn text is not the classified text, and then the pane says so. Proved by
>   `IntentMarkers.test.tsx` (retained full-file/card cases and card excerpts with an unreadable
>   memory side, the other-content and unchanged cases), `markGutter.test.tsx` (collapsed runs), the surface case's card
>   excerpts, and the mutation sets (M7, Q4-1 to Q4-4, F1, N3 and R2-3 all caught).
> - Nothing here computes an intersection: marks and lists are `hunkMarkers.ts`'s reading of the owner's response.
> - Outside a tree comparison's workspace there is no scope, and every surface renders exactly as landed.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ### By-design rationale — Collapsed runs expand whole
>
> The full hunk context and neighbouring marks must remain visible; expanding only the clicked line would hide adjacent attribution. This is the chosen boundary, not a Todo or missing feature.
>
> ## Evidence
>
> - Collapsed runs expand whole: The full hunk context and neighbouring marks must remain visible; expanding only the clicked line would hide adjacent attribution. (historical reference 14)
>
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - Why a changed file has no drawn marks: unlisted, visible pending, unavailable or other content; excerpt pending text is intent marks loading…, while full-file default wording is unchanged. (historical reference 9)
> - Excerpt windows use only resolved drawn sides; drawnSidesMatch compares their blobs, and useExcerptMarking reads only changed files and requests excerpt pending presentation. (historical reference 8)
>
>
> - The module's own statement: marks from the one classification, in the diff's own gutter; no editing, commenting or assessment. (historical reference 1)
> - A pane's input, named so a return lands in the pane a marker was followed from. (historical reference 2)
> - Placing every owner hunk a pane draws, the reveal and list reopened on a return, and hunks past a bounded text named. (historical reference 3)
> - The mark: tone, spans, compact text below 40rem, and its accessible name (review R1 F2). (historical reference 4)
> - The list: intents and tests apart, occurrences that follow their target, unknown lines, and the intersection-only sentence. (historical reference 5)
> - The file-level mark and the past-text note. (historical reference 6)
> - The source-content view: marks only on the drawn blobs the classification names. (historical reference 7)
>
>
> - One side's marks, and `Back to <file>`. (historical reference 10)
>
> - Surviving cards render excerpt markers and their full-file SourceContent markers; removed lane/explorer callers are not integration evidence. (historical reference 13)
>
> - The renderer cases. (historical reference 12)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
