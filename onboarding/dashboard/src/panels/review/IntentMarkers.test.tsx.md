# dashboard/src/panels/review/IntentMarkers.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R34 at the retained renderers: full diffs, no-mark states, marker returns, a card's Full file and card excerpts.** The file contains 18 `it` declarations. Captured hunk classifications and source texts feed `SourceContent`; the scope is a plain test value, and excerpt entries/read states are constructed explicitly where needed. The original MIK-L32 lane-fixture provenance and `gitTrees.cards`/`gitTrees.family` capture identities remain historical inputs, but the lane-window/full-lane test block is gone.

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
**Historical pre-R86 card account — superseded, not current assertion evidence.**

> - **The lane's windows (3).** The `lines.txt` L4 window draws the L2 replace and the L6 delete as context and carries
>   three marks, and a neighbour's list follows from that window's pane (the L32 F5 carry); the more-hunks wording for
>   both kinds of file; the lane's full file reopens on a return with its list and focus.
- **Card Full file and excerpts.** Full file reopens the originating card rather than the first same-path card. Excerpts keep the readable drawn side's mark when the other memory side is unavailable; differing drawn blobs suppress marks and explain other content. The unchanged-file excerpt case flushes effects and asserts no classification call and no marks-state note.

### Conventions

- `serve` answers source content from the constructed expansion and can answer an explicitly supplied per-file body; `open` mounts `SourceContent` under a plain `IntentMarkerScope.Provider`. This helper capability is not a surviving lane-window UI assertion.
- Marks are read in the owner's hunk order (`inHunkOrder`), with `described` giving label, spans and editor.

### Invariants And Boundaries

**Historical pre-R86 card account — superseded, not current assertion evidence.**

> - Proves the candidate invariant recorded on `IntentMarkers.tsx.md` (every drawn hunk carries its mark) and part of
>   the return invariant recorded on `MarkerTargetState.tsx.md`. The worker's final mutation sets (M1–M17, Q3-1 to
>   Q4-4, N1, N3, N11, F1, F2, F3a, F3b, F5, R2-1 to R2-7) are each caught by these files; the reviewer sampled them at
>   R2 and R3.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real bodies, the transport and the scope stand-in. [1]
- A full diff's marks, lists, follow, proofs and the unread side. [2]
- Files without per-hunk marks, the partial inventory and past-text notes. [3]
- The return: list, view and focus; the hold never against the reader. [4]
**Historical pre-R86 card account — superseded, not current assertion evidence.**

> - The lane's windows: every drawn hunk marked (F5), the wording, the full file's return. [5]
- Cards: the exact card reopened; excerpts with an unreadable side, other content, an unchanged file. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.


### Clock And Settlement Evidence

- The return-focus hold controls `requestAnimationFrame` with fake time: after blur another frame restores the returned mark, while Escape ends the hold and a subsequent 250 ms fake advance leaves focus on the body. The unchanged excerpt case flushes mounted effects before asserting that classification was not read. [7]
- Per-side expansion builder for mark scenarios [8]
- Scope builder for files under test [9]
- Hunk-order helpers for mark assertions [10]
- Shown-mark extraction from the rendered diff [11]
- Unchanged-file classifier for no-mark shapes [12]
