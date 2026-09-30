# dashboard/src/panels/review/laneFocus.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneFocus.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The lane's presentation rules over the real served bodies (3 cases).** It reads the captured per-file
classification (`laneReview.file.captured.json`, the attributed `review_comparison_retention.py`) and the captured
lane (`laneReview.lane.captured.json`) of the MIK-L32 scratch leaf and checks `laneFocus.ts`'s focus, windows and
totals.

## Code Commentary

### Logic

- **Case 1, focus.** The attributed file has a linked edit and an unexplained appended helper; the
  `Unexplained changes` destination opens it on the one unexplained hunk (`L572–577`), the `Unknown attribution`
  destination on none; a file of the destination's own bucket opens on every hunk.
- **Case 2, windows.** On eight lines, a replace of line 4 gives lines 1-7; an insertion after line 6 gives the gap
  between 6 and 7 (window from 4); an insertion before line 1 starts at 1; a hunk past the text held is `beyond`.
- **Case 3, totals.** `Unexplained changes` reads "5 files · 3 hunks · 2 non-text", its groups are three unexplained
  files then two attributed files, the buckets sum to the changed total, and `Unknown attribution` reads "1 file ·
  1 hunk".

### Conventions

- The bodies are read with `readFileSync` next to the test; nothing is synthesised except the one bucket override
  of case 1.

### Invariants And Boundaries

- Proves rule 8's window rule and rule 10's separate totals on real data. The mutations "focus shows every hunk"
  (2 cases fail) and "window ignores the insertion gap" (1) are caught.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real bodies read. | "laneReview.file.captured.json"; "laneReview.lane.captured.json" | dashboard/src/panels/review/laneFocus.test.ts:19-26 |
| Case 1: the destination's hunks of an attributed file. | "opens an attributed file on its hunks of the destination class, a bucket file on all of them" | dashboard/src/panels/review/laneFocus.test.ts:28-39 |
| Case 2: windows on the server's line numbers. | "cuts each window on the server side line numbers, with context, clamped to the text" | dashboard/src/panels/review/laneFocus.test.ts:41-57 |
| Case 3: file and hunk totals, in the server's order. | "reports a destination file total and hunk total separately, in the server order" | dashboard/src/panels/review/laneFocus.test.ts:59-68 |
| The rules under test. | `focusedHunks`; `hunkWindow`; `destinationTotals` | dashboard/src/panels/review/laneFocus.ts:83-89; dashboard/src/panels/review/laneFocus.ts:120-131; dashboard/src/panels/review/laneFocus.ts:71-79 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new unit test module (3 cases). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
