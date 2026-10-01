# dashboard/src/panels/review/ReviewSurface.markers.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R34 on real data through the real `ReviewSurface` (3 cases): following a per-hunk intent marker in the review
workspace, returning, and an unknown membership's own state.** The bodies are the real served answers of the reviewer
routes for the MIK-L34 worker's converted scratch leaf, re-captured in MIK-L33's merge round over the merged tree
(MIK-L34's scenario rebuilt under `/tmp/mik-l33-merge`): comparison 2 (`markerReturn.*`) and comparison 3, whose leaf
FAM-4V4GSQCS record does not parse on the after side (`markerUnknown.*`). The one synthetic body is the empty subject
catalogue, so the surface opens on the task-context review; the leaf-wide tree read is held, as a slow one is. Only
`fetch` is stubbed.

## Code Commentary

### Logic

- **Case 1.** Opening `serving/notes.py` from the explorer draws two marks from one classification read
  (`file=…notes.py`, `comparison=2`): `124:1:124:1` `2 intents` on L124 and `210:1:209:0` `3 intents` for the deleted
  docstring line.
- **Case 2 (rules 2 and 3).** Inline, the L124 marker's FAM-4V4GSQCS occurrence reads INV-Z66EMHMH's review and makes
  its member row current; the opened file is closed and `← Back to notes.py` shows. The target's card excerpts mark
  their hunks (`124:1:124:1 2 intents` in the `_confined_stat` card, `210:1:209:0 3 intents` in the shared
  `list_notes` card, none in an unchanged card; ruling Q4). After the layout is switched at the target, Back restores
  `inline`, reopens the list, scrolls the marker's host into view and focuses the marker; the Back control is gone,
  and the file was classified once.
- **Case 3 (ruling Q3, review R1 F3).** On comparison 3 the L124 list names four occurrences. The family-named unknown
  target puts "Attribution unknown" and its reason in the current member row, which receives focus, with no "No
  recorded family" heading. **Since MIK-L33's merge round and review R3-1** this step expects the tree comparison's
  one membership statement: the change facts' membership line tagged "Attribution unknown", "opened from an intent
  marker · membership unknown: the after memory tree has family records that do not parse: …FAM-4V4GSQCS-…" (the
  comparison's reason, not the marker's), in the row's accessible **description**; no button is named with
  "Attribution unknown" or "membership unknown"; no `review-member-target-state` and no marker-worded reason on the
  row. Only this assertion moved (from the row's name to its description, and to the comparison's reason); the rest of
  L34's test is unchanged. The confirmed-no-family target shows that heading and no unknown state. The family-less
  target of INV-413DC8XE shows the rail's "Attribution unknown" state (the review's `no_family_recorded` kept in its
  details) and the centre line naming the review's reading, and focus lands on the state, announced by name and
  described by its reason; for INV-Z66EMHMH, whose review composes a tree, the state sits above the tree and receives
  focus instead of the tree's auto-selected row.

### Conventions

- `answer(url)` routes each request to its captured body; `focusedAnnouncement` reads the focused element's accessible
  name and description from its labelling ids.

### Invariants And Boundaries

- Proves on real data the candidate invariants recorded on `MarkerTargetState.tsx.md` (unknown membership apart from
  no family; Back returns focus to the marker) and part of those on `hunkMarkers.ts.md` (one read per changed file)
  and `IntentMarkers.tsx.md` (card excerpts marked). Mutations M8–M10, M13, M16 and Q3-1 to Q3-5 fail here.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real bodies of comparison 2, the routing and the held leaf-wide read. [1]
- Case 1: two marks from one classification read. [2]
- Case 2: follow to the member row, card excerpt marks, and the return with layout, list and focus. [3]
- Comparison 3's bodies and the focused element's announcement. [4]
- Case 3: unknown membership in its own state, apart from no family. [5]
- Case 3's member-row step: the membership line in the description, the comparison's reason, nothing named twice (MIK-L33). [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
