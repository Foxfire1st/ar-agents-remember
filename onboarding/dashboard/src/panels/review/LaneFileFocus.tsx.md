# dashboard/src/panels/review/LaneFileFocus.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/LaneFileFocus.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**One changed file opened from the unexplained-changes lane (MIK-R32 rules 8 and 10): the actual diff, focused on
the hunks the destination is about, with the full file one control away.** The hunks, their classes and their
reasons are the server's per-file classification (`useReviewFileClassification`); the text is the landed
source-content read of the listed generation, the exact side blobs the source explorer also reads and caches. The
gate's own items for the file (MIK-R10, with the history rows that answer them) are shown beside, through L31's
`UnexplainedGroups`.

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
  owner's problem with a retry, and draws at most `FOCUSED_HUNK_LIMIT` (20) hunks, saying how many more there are.
  `FocusedHunk` heads each window with its class badge and "before L… → after L…" spans and lists its unknown
  reasons per side. `HunkExcerpt` cuts each side's window with `hunkWindow` on the server's line numbers
  (`sideWindow`) and draws a `DiffPane` (both sides as text) or a `FilePane` (one side), with `firstLine` so the
  gutter numbers are the file's; a hunk past the bounded text is named, never drawn from the wrong lines.
- **Full file.** `FullFile` toggles the landed `SourceContent` for the entry and generation.
- **The gate's items.** `GateItems` takes a `GateRead`: `reading` ("Reading the gate's items for this file…",
  never "none" while the slower leaf-wide read has not answered), `none` with why, or `read` with the worklist, whose
  `worklistGroups(...).unexplained` groups for this path render through `UnexplainedGroups`; with none it says the
  gate raised no unexplained item for the file. The workspace builds the `GateRead` (`gateRead`) only from a
  leaf-wide read of the same comparison.

### Conventions

- One window and one mark per server hunk: a displayed change region never merges two owner hunks under one mark
  (rule 8).
- The gate may differ from the lane's classification; neither is changed by the other.

### Invariants And Boundaries

- Nothing here assesses, approves, waives or explains a change (the adopted Exclusions): the gate's items are shown
  with their answering rows, and no disposition control is offered.
- The content read is the landed one (same request type, same cache), so the lane opens exactly the bytes the source
  explorer would.

### Todos

- **Carried to L34 (review R1 F5):** a window's context can show a neighbouring hunk without its own mark; the
  sentence "the full file shows every one" means diff regions, not classified marks.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused diff, the exact blobs and the gate's items beside, in the module's own words. | "so a displayed change region can never merge two of the server's hunks under one" | dashboard/src/panels/review/LaneFileFocus.tsx:1-9 |
| The gate read's three states and the task a file is opened in. | `GateRead`; `LaneTask` | dashboard/src/panels/review/LaneFileFocus.tsx:68-80 |
| One opened file: its classification, facts, focused diffs, full file and gate items. | `LaneFileFocus`; `fallbackEntry` | dashboard/src/panels/review/LaneFileFocus.tsx:82-164 |
| The bucket, counts, reason, non-text fact and unread sides. | `FileFacts` | dashboard/src/panels/review/LaneFileFocus.tsx:166-194 |
| One content read; at most twenty hunk windows. | `FocusedDiffs` | dashboard/src/panels/review/LaneFileFocus.tsx:196-249 |
| One hunk's badge, spans, reasons and window on the server's line numbers. | `FocusedHunk`; `sideWindow`; `HunkExcerpt` | dashboard/src/panels/review/LaneFileFocus.tsx:251-332 |
| The full file one control away. | `FullFile` | dashboard/src/panels/review/LaneFileFocus.tsx:334-370 |
| The gate's items: reading, none, or the file's groups. | `GateItems` | dashboard/src/panels/review/LaneFileFocus.tsx:374-391 |
| The gate read, only from the same comparison's leaf-wide read. | `gateRead` | dashboard/src/panels/review/ReviewWorkspace.tsx:385-401 |
| The content read, exported for this file. | `useSourceContentRead` | dashboard/src/panels/review/SourceContent.tsx:180-220 |
| The file's groups, rendered as the leaf panel renders them. | `UnexplainedGroups` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:236-263 |
| A focused hunk, the full file control and the gate's item; "reading", never "none". | "lists unexplained files first, then attributed files, and opens one on its unexplained hunk"; "says the gate's items are still being read, never that the gate raised none" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:101-173 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new focused-file component MIK-R32 adds (rules 8 and 10), recording review R1 F5 (carried to L34). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
