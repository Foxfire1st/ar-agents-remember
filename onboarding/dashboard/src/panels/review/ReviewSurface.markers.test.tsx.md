# dashboard/src/panels/review/ReviewSurface.markers.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.markers.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real bodies of comparison 2, the routing and the held leaf-wide read. | "markerReturn.task.captured.json"; `answer`; `serve` | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:23-23; dashboard/src/panels/review/ReviewSurface.markers.test.tsx:44-55; dashboard/src/panels/review/ReviewSurface.markers.test.tsx:57-71 |
| Case 1: two marks from one classification read. | "opens a changed file with one marker per hunk, from the one classification" | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:92-109 |
| Case 2: follow to the member row, card excerpt marks, and the return with layout, list and focus. | "selects the tree position a marker names, and returns to the hunk with focus on the marker" | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:111-190 |
| Comparison 3's bodies and the focused element's announcement. | "markerUnknown.memberUnknown.captured.json"; `focusedAnnouncement` | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:206-206; dashboard/src/panels/review/ReviewSurface.markers.test.tsx:258-271 |
| Case 3: unknown membership in its own state, apart from no family. | "opens an unknown membership in its own Attribution unknown state, apart from no family" | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:280-382 |
| Case 3's member-row step: the membership line in the description, the comparison's reason, nothing named twice (MIK-L33). | "(MIK-L33 review R3-1: a member row is named by its subject only, and described by its facts)." | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:311-312 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-L33's merge round** (review R3-1, ruling 2026-09-30T21:55:02; R3-3): case 3's member-row step now expects the tagged membership line with the comparison's reason in the row's accessible description, no fact in any button's name, and no L34 note or marker-worded reason on the row; the bodies are MIK-L33's re-capture. Purpose and Logic updated, one row added. The other moved rows were re-pointed by the installed fixer or the exact base-to-staged line shift.
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new surface test module MIK-R34 adds (3 cases), recording rulings Q3 and Q4 and review R1 F3. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
