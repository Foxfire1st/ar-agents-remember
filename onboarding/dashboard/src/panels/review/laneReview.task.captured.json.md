# dashboard/src/panels/review/laneReview.task.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneReview.task.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` body of the MIK-L32 scratch leaf: the task-context review of tree comparison 2**
(16,922 bytes; test evidence for `ReviewSurface.lane.test.tsx`).

## Code Commentary

### Logic

- The payload's limitations include `review:trees:2`, so the surface reads the lane of comparison 2.
- Its source inventory lists the seven changed paths. The landed R04 accounting in the payload lists
  `attributed_changed_paths` (the retention and rosters modules) and `unattributed_changed_paths` (five paths, including
  `review_source_admission.py` and the proof-linked test) and counts 0 unknown: the lists the lane's classification
  replaces on a tree comparison (ruling Q1 for the explorer, review R1 F1 for the technical details). The surface test
  asserts these landed lists to prove the rendered labels do not come from them.

### Conventions

Keep the captured bytes and their receipt (`laneReview.capture-provenance.json`) intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l32-real` (code at `b54d1b03` with the scratch leaf's edits;
memory `58d016cb` converted), not current project knowledge; its line numbers and blobs are the scratch tree's.

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
| The tree comparison this review names. | "review:trees:2" | dashboard/src/panels/review/laneReview.task.captured.json:188-188 |
| The landed accounting's lists and counts. | "\"attributed_changed_paths\": ["; "\"unattributed_changed_paths\": ["; "\"unknown_attribution_changed_paths\": []" | dashboard/src/panels/review/laneReview.task.captured.json:195-373 |
| The receipt row for this body. | "src/panels/review/laneReview.task.captured.json" | dashboard/src/panels/review/laneReview.capture-provenance.json:25-25 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new captured task review body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
