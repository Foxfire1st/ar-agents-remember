# dashboard/src/panels/review/IntentMarkers.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/IntentMarkers.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R34 at the real renderers (21 cases): the landed source-content view (the explorer's opened file, `Expand full
file`, a card's and the lane's full file), the lane's focused windows, and the card excerpts.** Every classification
is a real served per-file body of MIK-L32's lane fixture world (`hunkMarkers.classifier.captured.json`), and every diff
draws the exact blob texts that body names; only `fetch` is stubbed. The workspace's marker scope is a plain value
(`scopeOf`), so each case asserts what the reader sees and what a followed marker asks the workspace to select. The card
cases use the landed `gitTrees.cards` and `gitTrees.family` captures.

## Code Commentary

### Logic

- **A full diff (5).** Each owner hunk is marked on the owner's side lines, the deletion in the before editor; inline,
  every mark is on an after line with the deletion below its removed lines; a hunk's list shows its intents with their
  family occurrences and following one calls `follow` with the target; a proof is listed as a test with its facet,
  apart from the intents; `before_unread` keeps the readable side's marks and names the unread side's lines unknown.
- **No per-hunk marks (5).** A confirmed-unregistered file has one file-level `unexplained` mark; a file with no
  readable side one `attribution unknown` note; nothing outside a tree comparison, for an unchanged file (no read), or
  for other content (the `other-content` note, including a case where only the before object differs: review R1 N3);
  a changed file a partial inventory does not list says so, with `classify` never called (review R1 F5); hunks past a
  bounded text are named.
- **The return (3).** A return reopens the list, brings the hunk into view and focuses the mark; after a return a blur
  leaves focus on the body and the hold gives it back, while after the reader's key it does not (review R2-F1); a pane
  the marker was not followed from is not reopened.
- **The lane's windows (3).** The `lines.txt` L4 window draws the L2 replace and the L6 delete as context and carries
  three marks, and a neighbour's list follows from that window's pane (the L32 F5 carry); the more-hunks wording for
  both kinds of file; the lane's full file reopens on a return with its list and focus.
- **Cards (5).** The card a marker was followed from reopens, not the first card of its path; an excerpt keeps its
  drawn side's marks when the other memory side cannot be read (`2:1:2:1 · 1 intent · unknown`, review R1 F1);
  no mark when either drawn side is other content though the other matches (review R2); an unchanged file's card never
  reads nor speaks (review R2); a drawn side of other content says why.

### Conventions

- `serve` answers the content read with `expansionOf(body)` (the exact texts and object ids) and a lane file read with
  the body; `open` mounts `SourceContent` inside `IntentMarkerScope.Provider`.
- Marks are read in the owner's hunk order (`inHunkOrder`), with `described` giving label, spans and editor.

### Invariants And Boundaries

- Proves the candidate invariant recorded on `IntentMarkers.tsx.md` (every drawn hunk carries its mark) and part of
  the return invariant recorded on `MarkerTargetState.tsx.md`. The worker's final mutation sets (M1–M17, Q3-1 to
  Q4-4, N1, N3, N11, F1, F2, F3a, F3b, F5, R2-1 to R2-7) are each caught by these files; the reviewer sampled them at
  R2 and R3.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real bodies, the transport and the scope stand-in. | "hunkMarkers.classifier.captured.json"; `scopeOf`; `expansionOf` | dashboard/src/panels/review/IntentMarkers.test.tsx:1-178 |
| A full diff's marks, lists, follow, proofs and the unread side. | "marks each owner hunk on the owner's side lines, a deletion in the before editor"; "lists a proof entry as a test with its facet, apart from the intents" | dashboard/src/panels/review/IntentMarkers.test.tsx:180-293 |
| Files without per-hunk marks, the partial inventory and past-text notes. | "gives a confirmed-unregistered file one file-level unexplained mark"; "says why a changed file a partial inventory does not list carries no marks" | dashboard/src/panels/review/IntentMarkers.test.tsx:295-391 |
| The return: list, view and focus; the hold never against the reader. | "reopens its list, brings its hunk into view and focuses it"; "keeps the returned mark focused while the pane settles, never against the reader" | dashboard/src/panels/review/IntentMarkers.test.tsx:393-438 |
| The lane's windows: every drawn hunk marked (F5), the wording, the full file's return. | "marks every hunk a window draws: the focused one and each neighbour its context shows" | dashboard/src/panels/review/IntentMarkers.test.tsx:440-564 |
| Cards: the exact card reopened; excerpts with an unreadable side, other content, an unchanged file. | "reopens the card a marker was followed from, not the first card of its path"; "never reads, nor speaks for, an unchanged file's card" | dashboard/src/panels/review/IntentMarkers.test.tsx:566-770 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new renderer test module MIK-R34 adds (21 cases), recording the L32 F5 carry, rulings Q2 and Q4, review R1 F1, F4 (N1, N3, N11) and F5, and the review R2 gaps. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
