# dashboard/src/panels/review/ReviewSurface.lane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.lane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R32 on real data through the real review surface (7 cases).** The real `ReviewSurface` renders the real
served bodies of the MIK-L32 worker's converted scratch leaf (`laneReview.*.captured.json`, receipt
`laneReview.capture-provenance.json`; comparison `review:trees:2`), with only `fetch` stubbed. The seven changed
files are three with no entry (a new module, `CONTRIBUTING.md`, a new binary), an attributed file with a linked edit
and an appended helper (`review_comparison_retention.py`), an attributed file whose only change is its mode
(`review_family_rosters.py`), a test a proof links, and `review_source_admission.py`, whose converted entries were
recorded at an older blob. The one synthetic body is the empty subject catalogue.

## Code Commentary

### Logic

- `answer(url)` serves the task review, the leaf-wide `/trees` read, the lane (`lane=`), the one per-file body (for
  the retention file) and the source content; any other request throws. `serve(hold)` can hold the leaf-wide read
  (the gate's worklist) or the lane read unanswered.
- **Case 1:** the destinations read "Unexplained changes5 files · 3 hunks · 2 non-text" and "Unknown attribution1
  file · 1 hunk", follow the family tree in the document, and there is exactly one lane read, pinned to comparison
  `2`, and no file read unasked.
- **Case 2:** the `Unexplained changes` rows are the three unexplained files then the two attributed files; the
  mode-only file reads "non-text (text, mode) · gate unexplained"; opening the retention file shows one focused
  hunk (`unexplained`, "none (after L571)" → `L572–577`) drawn in a `DiffPane`, the facts "2 hunk(s): 1 linked · 1
  unexplained · 0 attribution unknown", the `Full file` control, and the gate's own item for the file.
- **Case 3:** the `Unknown attribution` row is `review_source_admission.py` with "RLZ-CXH58B4W
  (recorded_blob_mismatch)", and the destination is the tree's current node.
- **Case 4:** with the leaf-wide read held, the focused file says the gate's items are being read, never "none".
- **Case 5 (ruling Q1):** every explorer label equals the label of the path's lane bucket; the admission file is
  `Attribution unknown` and the proof-linked test `Mapped`, although the payload's landed lists call both
  unregistered.
- **Case 6 (ruling Q1):** with the lane held, every explorer label is `Attribution pending`, and the technical
  details say pending too.
- **Case 7 (review R1 F1):** the technical details read `unattributed_changed_paths: 3` and
  `unknown_attribution_changed_paths: 1` (`data-attribution-source="lane"`), list the three unexplained files and
  neither the proof-linked test nor the admission file, and list the admission file as of unknown attribution.

### Conventions

- Like `ReviewSurface.gitTrees.test.tsx`, only `fetch` is stubbed and every body but the empty catalogue is captured.

### Invariants And Boundaries

- Proves, through the real surface, the candidate invariant "on tree comparisons, the explorer and the technical
  details take their attribution from the lane, so no two surfaces disagree" (recorded on
  `review_unexplained_lane.py.md`), and rule 10's destinations, order, totals and focused diff on real data.
- Mutations caught: the explorer ignoring the lane (3 cases), the details ignoring the lane or not being handed it
  (3 each), and a second lane read by the workspace (the one-read assertion of case 1).

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
| The real bodies and the scratch leaf they describe. | "captured<ReviewResult>('laneReview.task.captured.json')" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:1-30 |
| The fetch stub, with a held read. | "function answer(url: URL): unknown {"; "function serve(hold?" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:39-65 |
| Case 1: destinations after the families, one lane read. | "offers the two lane destinations after the families, with their file and hunk totals" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:85-99 |
| Case 2: rows in the server's order and a focused hunk. | "lists unexplained files first, then attributed files, and opens one on its unexplained hunk" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:101-139 |
| Case 3: the unknown file with its reason. | "lists the file of unknown attribution with the reason no range is supplied" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:141-156 |
| Case 4: the gate's items still being read. | "says the gate's items are still being read, never that the gate raised none" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:158-173 |
| Cases 5 and 6: the explorer labels from the lane, or pending (ruling Q1). | "labels the source explorer with the lane's bucket for every changed file"; "labels the explorer pending while the lane is read, never with a guessed bucket" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:188-229 |
| Case 7: the technical details from the lane (review F1). | "lists the lane's unexplained and unknown files in the technical details" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:231-258 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new surface test module (7 cases), recording ruling 2026-09-30T12:19:20 Q1 (cases 5 and 6) and review R1 F1 (case 7, fixed at 13:07:38). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
