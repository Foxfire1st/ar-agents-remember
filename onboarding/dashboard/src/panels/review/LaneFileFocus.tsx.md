# dashboard/src/panels/review/LaneFileFocus.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/LaneFileFocus.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**One changed file opened from the unexplained-changes lane (MIK-R32 rules 8 and 10): the actual diff, focused on
the hunks the destination is about, with the full file one control away.** The hunks, their classes and their
reasons are the server's per-file classification (`useReviewFileClassification`); the text is the landed
source-content read of the listed generation, the exact side blobs the source explorer also reads and caches. The
gate's own items for the file (MIK-R10, with the history rows that answer them) are shown beside, through L31's
`UnexplainedGroups`. **Since MIK-R34** every window and the full file carry the per-hunk intent markers, from this
same one per-file read.

## Code Commentary

### Logic

- **The read.** `LaneFileFocus` asks the file's classification; it says "classifying …" while pending and shows the
  owner's problem on a failed read. It takes the destination's hunks (`focusedHunks`) and the inventory entry for
  the path (or `fallbackEntry` from the classification), and needs both code generations of the inventory, else it
  says no content can be opened.
- **Facts.** `FileFacts` shows the bucket and the per-class counts, the reason behind "Why this attribution", a
  non-text change's content, mode flag and the gate's linkage ("the gate holds it unexplained", or "of unknown
  linkage"), and each side whose knowledge is unavailable with its detail.
- **Focused diffs.** `FocusedDiffs` makes one `useSourceContentRead` (now exported by `SourceContent.tsx`), shows the
  owner's problem with a retry, and draws at most `FOCUSED_HUNK_LIMIT` (20) hunks, keyed by `hunkMarkers.hunkKey`.
  Above the windows it draws the file's one file-level mark (`IntentMarkers.FileMark`) when the file carries one: a
  confirmed-unregistered file, or one neither side of which has readable knowledge. **The note for the hunks it does
  not draw is accurate since MIK-L34 (the L32 review F5 carry):** it says that many hunks of this class are not drawn
  here, and that Full file draws every changed region of the text its read returns, each owner hunk with its own mark
  (or, for a file-level-marked file, under the one mark the file carries). It no longer says "the full file shows
  every one", which read as though every classified hunk carried a mark there.
  `FocusedHunk` heads each window with its class badge and "before L… → after L…" spans and lists its unknown
  reasons per side. `HunkExcerpt` cuts each side's window with `hunkWindow` on the server's line numbers
  (`sideWindow`) and draws a `DiffPane` (both sides as text) or a `FilePane` (one side), with `firstLine` so the
  gutter numbers are the file's; a hunk past the bounded text is named, never drawn from the wrong lines.
- **The marks of a window (MIK-L34, the L32 review F5 carry ruled 2026-09-30T13:07:38).** `useWindowMarking` gives
  each window its own pane (`lane-window:<hunkKey>`) and the file lines each side draws (`drawnLines`), and marks
  **every owner hunk whose changed lines the window draws**: the focused hunk and any neighbour its three context
  lines show, each on its own side lines, so a neighbour drawn as context is never an unmarked change. It marks only
  inside the workspace's marker scope, only for a file with per-hunk marks, and only when the classification's side
  blobs are the drawn objects (`IntentMarkers.describesDrawn`). A one-sided window places as a split pane and its
  `FilePane` receives only the drawn side's marks (`sideMarks`); the open marker's list renders below the window.
- **Full file.** `FullFile` toggles the landed `SourceContent` for the entry and generation, handing it the lane's own
  classification with the pane name `lane-full` (`markers`), so the one per-file read also marks the full file. A
  return to a marker followed from the full file opens it again (its initial state reads the scope's `returning`).
- **The gate's items.** `GateItems` takes a `GateRead`: `reading` ("Reading the gate's items for this file…",
  never "none" while the slower leaf-wide read has not answered), `none` with why, or `read` with the worklist, whose
  `worklistGroups(...).unexplained` groups for this path render through `UnexplainedGroups`; with none it says the
  gate raised no unexplained item for the file. The workspace builds the `GateRead` (`gateRead`) only from a
  leaf-wide read of the same comparison.

### Conventions

- One window per focused server hunk, and one mark per owner hunk a window draws: a displayed change region never
  merges two owner hunks under one mark (rule 8), and a neighbour shown as context keeps its own mark (MIK-L34).
- The gate may differ from the lane's classification; neither is changed by the other.

### Invariants And Boundaries

- Nothing here assesses, approves, waives or explains a change (the adopted Exclusions): the gate's items are shown
  with their answering rows, and no disposition control is offered.
- The content read is the landed one (same request type, same cache), so the lane opens exactly the bytes the source
  explorer would.

### Todos

- **Resolved by MIK-L34 (review R1 F5, carried by ruling 2026-09-30T13:07:38):** every owner hunk a window draws,
  including a neighbour shown only as context, now carries its own intent mark, and the more-hunks note says what
  the full file draws instead of "the full file shows every one". No work remains on this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused diff, the exact blobs, every drawn owner hunk's own intent mark (MIK-L34) and the gate's items beside, in the module's own words. | "so a displayed change region can never merge two of the server's hunks under one"; "carries its own intent marker in the window's gutter (MIK-R34)" | dashboard/src/panels/review/LaneFileFocus.tsx:1-11 |
| The gate read's three states and the task a file is opened in. | `GateRead`; `LaneTask` | dashboard/src/panels/review/LaneFileFocus.tsx:75-78; dashboard/src/panels/review/LaneFileFocus.tsx:80-85 |
| One opened file: its classification, facts, focused diffs, full file and gate items. | `LaneFileFocus`; `fallbackEntry` | dashboard/src/panels/review/LaneFileFocus.tsx:87-162; dashboard/src/panels/review/LaneFileFocus.tsx:164-171 |
| The bucket, counts, reason, non-text fact and unread sides. | `FileFacts` | dashboard/src/panels/review/LaneFileFocus.tsx:173-201 |
| One content read; the file-level mark once above at most twenty hunk windows; what the full file draws of the hunks not drawn here (MIK-L34, F5). | `FocusedDiffs`; "<FileMark file={file} />"; "more hunk(s) of this class are not drawn here" | dashboard/src/panels/review/LaneFileFocus.tsx:203-266 |
| One hunk's badge, spans, reasons and window on the server's line numbers. | `FocusedHunk`; `sideWindow`; `HunkExcerpt` | dashboard/src/panels/review/LaneFileFocus.tsx:268-307; dashboard/src/panels/review/LaneFileFocus.tsx:359-415; dashboard/src/panels/review/LaneFileFocus.tsx:310-318 |
| The full file one control away, marked from the lane's own classification and reopened by a return to a marker followed from it (MIK-L34). | "function FullFile({"; "markers={{ pane: 'lane-full', classification: file }}" | dashboard/src/panels/review/LaneFileFocus.tsx:417-460 |
| A window's marks: every owner hunk whose changed lines it draws, on its own pane, only for the drawn blobs (MIK-L34). | `drawnLines`; `useWindowMarking` | dashboard/src/panels/review/LaneFileFocus.tsx:321-325; dashboard/src/panels/review/LaneFileFocus.tsx:329-357 |
| The window cases: three marks in the one window whose context draws two neighbours, a neighbour's list from that window, the more-hunks wording, and the full file's return. | "marks every hunk a window draws: the focused one and each neighbour its context shows"; "says what the full file shows of the hunks a focused view does not draw"; "reopens the full file a marker was followed from, with its list and focus" | dashboard/src/panels/review/IntentMarkers.test.tsx:440-564 |
| The gate's items: reading, none, or the file's groups. | `GateItems` | dashboard/src/panels/review/LaneFileFocus.tsx:464-481 |
| The gate read, only from the same comparison's leaf-wide read. | `gateRead` | dashboard/src/panels/review/ReviewWorkspace.tsx:448-464 |
| The content read, exported for this file. | `useSourceContentRead` | dashboard/src/panels/review/SourceContent.tsx:210-250 |
| The file's groups, rendered as the leaf panel renders them. | `UnexplainedGroups` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:236-263 |
| A focused hunk, the full file control and the gate's item; "reading", never "none". | "lists unexplained files first, then attributed files, and opens one on its unexplained hunk"; "says the gate's items are still being read, never that the gate raised none" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:101-173 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`ReviewWorkspace.tsx`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept); 2 passing row(s) normalised by the fixer. The fixer's normalisation also re-measured ranges into files this leaf did not change (`LaneFileFocus.tsx`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:20:08+00:00: Generated citation repair: `gateRead` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:448-464. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **body updated for MIK-R34, and the carried L32 review F5 Todo resolved** (ruling 2026-09-30T13:07:38): every owner hunk a window draws, including a neighbour shown as context, carries its own intent mark (`useWindowMarking`, `drawnLines`), the file-level mark is drawn once above the windows, the more-hunks note now says what Full file draws instead of "the full file shows every one", and the full file is marked from the lane's own classification and reopened by a return (Purpose, Logic, Conventions, Todos). **Reopened claim:** the `FullFile` row, bound by this pass's generated bullet, is reworded and re-anchored on `"function FullFile({"` and the marker line, and that one generated bullet is removed; the `GateItems` bullet is kept. The header row is re-measured to `1-11` with the new sentence's quote; the `FocusedDiffs` row is reworded; two rows added. Other rows moved with the inserted lines: the fixer normalised them.
- 2026-09-30T18:06:01+00:00: Generated citation repair: `GateItems` repointed to dashboard/src/panels/review/LaneFileFocus.tsx:464-481. No content impact: mechanical anchor-range projection bound to citation source snapshot dd511ab0f1e150e6e017fdffb93a370d587225cb8c691b071ace179d457746ab; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new focused-file component MIK-R32 adds (rules 8 and 10), recording review R1 F5 (carried to L34). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
