# dashboard/src/panels/review/ReviewSurface.markers.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R34 on real data through the real `ReviewSurface` (6 cases): hunk marks, marker navigation and Back, held-return keyboard navigation, source availability with an unreadable roster, and unknown-membership target states.** The bodies are the real served answers of the reviewer
routes for the MIK-L34 worker's converted scratch leaf, re-captured in MIK-L33's merge round over the merged tree
(MIK-L34's scenario rebuilt under `/tmp/mik-l33-merge`): comparison 2 (`markerReturn.*`) and comparison 3, whose leaf
FAM-4V4GSQCS has an unreadable after family record in the retained comparison-3 captures. Explicit synthetic catalogue and initial-family-question adapters expose the originating family card; marker targets use untouched served answers, and the leaf-wide read is held. The real component tree and client use the fetch replay, not a new backend capture.

## Code Commentary

### Logic

- **Case 1.** Opening `serving/notes.py` from its originating card's Full file draws the two captured hunk marks: `124:1:124:1` with 2 intents on L124 and `210:1:209:0` with 3 intents for the deletion, from one file-classification request pinned to comparison 2.
- **Case 2 (rules 2 and 3).** Inline, the L124 marker's FAM-4V4GSQCS occurrence reads INV-Z66EMHMH's review and makes
  its member row current; the opened file is closed and `← Back to notes.py` shows. The target's card excerpts mark
  their hunks (`124:1:124:1 2 intents` in the `_confined_stat` card, `210:1:209:0 3 intents` in the shared
  `list_notes` card, none in an unchanged card; ruling Q4). After the layout is switched at the target, Back restores
  `inline`, reopens the list, scrolls the marker's host into view and focuses the marker; the Back control is gone,
  and the file was classified once.
- **Case 3:** after Back restores a held marker, `j` selects and focuses the next measured changed tree row and releases the marker return.
- **Cases 4–6:** the selected invariant's Full file and marks remain available with an unreadable family roster. The hunk list preserves four unknown/confirmed-no-family occurrences. A family-named unknown occurrence focuses the separate `review-rail-target-state` with partial context and its native reason. Before-side confirmed absence does not establish a current no-family roster. After-side unknown occurrences focus their own partial or unavailable target state with the native reason; the target is outside a member row.

### Conventions

- `answer(url)` routes each request to its captured body; `focusedAnnouncement` reads the focused element's accessible
  name and description from its labelling ids.

### Invariants And Boundaries

- Proves on real data the candidate invariants recorded on `MarkerTargetState.tsx.md` (unknown membership apart from
  no family; Back returns focus to the marker) and part of those on `hunkMarkers.ts.md` (one read per changed file)
  and `IntentMarkers.tsx.md` (card excerpts marked). Historical mutation reports recorded failures for M8–M10, M13, M16 and Q3-1 to Q3-5; those reports do not establish results for the changed current journeys.

### Todos

No additional work is asserted by this card.

The captured marker world plus labelled synthetic catalogue/initial-family adapters opens the originating card's Full file. The retained journey follows exact captured occurrences, returns inline layout/list/marker focus with one classification read, and keeps unknown membership distinct from confirmed no family in open central content.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real bodies of comparison 2, the routing and the held leaf-wide read. [1]
- Comparison 3's bodies and the focused element's announcement. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- In-card Full file opening for the marked file [7]
- Per-hunk mark extraction for assertions [8]
- Unknown-membership world with unattributed links [9]
- Spoken announcement of the followed marker return [10]

- The first case checks two hunk marks from one classification read. [2]
- The retained marker journey checks member selection, excerpt marks and Back restoration; the following held-return case checks j selecting the next measured changed row. [3]
- Three current unknown-world cases check source availability, a focused named partial target, and before-side absence separated from partial/unavailable after-side unknown membership. [5]
- The named unknown occurrence focuses a partial target state containing its reason; it does not select a fabricated member row. [6]
- Central target content contains the native reason and excludes the no-family statement; replace the removed centerReview symbol target with the actual assertions. [11]
