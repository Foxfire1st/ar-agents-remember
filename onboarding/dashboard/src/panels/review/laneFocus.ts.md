# dashboard/src/panels/review/laneFocus.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneFocus.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The unexplained-changes lane's presentation rules (MIK-R32), kept apart from its components.** Nothing here
classifies: every bucket, hunk and class comes from the server's response. These pure functions choose which of those
hunks a destination focuses on, cut the text window each focused diff shows on the server's side line numbers (rule
8: a mark always sits on the owner's hunk), write the totals lines, and turn the lane into the labels the source
explorer (ruling Q1) and the technical details (review R1 F1) show on a tree comparison.

## Code Commentary

### Logic

- **Destinations.** `DESTINATION_TITLES` (`Unexplained changes`, `Unknown attribution`, the latter named apart from
  the per-member `Attribution unknown` membership state), `GROUP_TITLES` and `GROUP_NOTES` (one line per group saying
  what puts a file there). `destinationOf` picks `unexplained_changes` or `unknown_attribution`;
  `destinationGroups` splits the files at `bucket_files` into the bucket's own files and the attributed files, in the
  server's order; `destinationTotals` writes "5 files · 3 hunks · 2 non-text", file and hunk totals separately.
- **Focus.** `focusedHunks(file, destination)` opens a file of the destination's own bucket on every hunk, and an
  attributed file on its hunks of the destination's class only.
- **Windows.** `spanLabel` gives "L4", "L4–6" or "none (after L5)" for a side where the hunk changes nothing.
  `sideLines` splits a side's text. `hunkWindow(span, lines, context = 3)` returns the window's first line, its text
  and `beyond`: the changed lines (or, on a side with none, the gap after `start`) plus `HUNK_CONTEXT_LINES` (3) on
  each side, clamped to the text; `beyond` is true when the hunk lies past a bounded prefix, so it is never drawn
  from the wrong lines. `FOCUSED_HUNK_LIMIT` (20) caps the windows a focused view draws.
- **The explorer's labels (ruling Q1, 2026-09-30T12:19:20).** `EXPLORER_LABELS` maps each bucket to the explorer's
  landed words (`attributed` → `Mapped`, `unexplained` → `Unmapped`, `attribution_unknown` → `Attribution unknown`).
  `explorerAttribution(read, paths)` labels every changed path `Attribution pending` (`EXPLORER_PENDING`) while the
  lane is read, and otherwise by its bucket in `paths`; a path the lane does not list, or an unread lane, is
  `Attribution unknown`, never a guessed bucket.
- **The technical details' facts (review R1 F1, ruling 13:07:38).** `laneAttributionFacts(read)` is `pending`,
  `unknown` (an unread or unavailable lane), or `read` with `partial`, the unexplained paths and the unknown paths.
  `laneCountText(name, facts)` states the landed remaining counts `unattributed_changed_paths` and
  `unknown_attribution_changed_paths` from the lane (the count of each list, marked `(partial)`), or pending or
  unknown; other counts return `undefined` and keep the landed text.

### Conventions

- Pure functions over the served shapes; no fetch, no state.
- The explorer keeps its landed vocabulary; only the source of the label changes on a tree comparison.

### Invariants And Boundaries

- **Part of the candidate invariant "on tree comparisons, the explorer and the technical details take their
  attribution from the lane, so no two surfaces disagree"** (recorded on `review_unexplained_lane.py.md`): realized
  here by `explorerAttribution` and `laneAttributionFacts`; proved by `ReviewSurface.lane.test.tsx` and the gitTrees
  cases; making the explorer ignore the lane fails 3 cases, and forcing the lane facts off fails 3.
- A window's marks sit on the owner's hunks: every window is cut on the server's side line numbers, one per focused
  hunk (rule 8).

### Todos

- **Carried to L34 (review R1 F5):** a window's context lines can show a neighbouring hunk without its own mark
  (for example `lines.txt`'s delete window also draws the adjacent replace); per-hunk markers are L34's.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Nothing here classifies; marks sit on the owner's hunks. | "Nothing here classifies" | dashboard/src/panels/review/laneFocus.ts:1-6 |
| The context and focus bounds; the destination titles. | `HUNK_CONTEXT_LINES`; `FOCUSED_HUNK_LIMIT`; `DESTINATION_TITLES` | dashboard/src/panels/review/laneFocus.ts:19-26 |
| One note per group. | `GROUP_TITLES`; `GROUP_NOTES` | dashboard/src/panels/review/laneFocus.ts:38-53 |
| The two groups in the server's order, and the totals line. | `destinationOf`; `destinationGroups`; `destinationTotals` | dashboard/src/panels/review/laneFocus.ts:55-79 |
| The hunks a destination opens a file on. | `focusedHunks` | dashboard/src/panels/review/laneFocus.ts:83-89 |
| Span labels, side lines and the window on the server's line numbers. | `spanLabel`; `sideLines`; `hunkWindow` | dashboard/src/panels/review/laneFocus.ts:98-131 |
| The explorer's labels from the lane (ruling Q1). | `EXPLORER_LABELS`; `EXPLORER_PENDING`; `explorerAttribution` | dashboard/src/panels/review/laneFocus.ts:135-156 |
| The technical details' facts and counts from the lane (review F1). | `laneAttributionFacts`; `laneCountText` | dashboard/src/panels/review/laneFocus.ts:161-193 |
| The workspace's explorer source by kind of review. | "return explorerAttribution(" | dashboard/src/panels/review/ReviewWorkspace.tsx:596-617 |
| The details' counts and lists from the lane. | "const lane = laneRead ? laneAttributionFacts(laneRead) : null;" | dashboard/src/panels/review/ReviewRecordPanes.tsx:292-301 |
| The window, focus and totals cases. | "cuts each window on the server side line numbers, with context, clamped to the text" | dashboard/src/panels/review/laneFocus.test.ts:41-57 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new presentation module MIK-R32 adds, recording ruling 2026-09-30T12:19:20 Q1 (the explorer's labels), review R1 F1 (the details' facts) fixed at 13:07:38, and F5 carried to L34. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
