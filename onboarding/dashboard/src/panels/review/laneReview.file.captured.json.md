# dashboard/src/panels/review/laneReview.file.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneReview.file.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&file=mcp/src/agents_remember/application/review_comparison_retention.py`
body of the MIK-L32 scratch leaf: one per-file classification** (5,098 bytes; test evidence for `laneFocus.test.ts`
and `ReviewSurface.lane.test.tsx`).

## Code Commentary

### Logic

- `attributed`, 2 hunks: the edit inside `_side_binding` (before 418,1 / after 418,1) is `linked` through
  `RLZ-D2SEVSM9` on both sides (range 410-435; `INV-9BH2BNCT` revision 2 with its keys; `FAM-XZ5BR65G` revision 3,
  `member`); the appended helper (before 571,0 / after 572,6) is `unexplained` (post-curation: the entries were
  re-recorded at the candidate blob).
- Both sides list the three entries at their recorded blobs with their ranges.

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
| The per-file response. | "file_classification" | dashboard/src/panels/review/laneReview.file.captured.json:42-182 |
| The linked edit and its link with revision and family occurrence. | "\"classification\": \"linked\"" | dashboard/src/panels/review/laneReview.file.captured.json:52-103 |
| The unexplained appended helper. | "\"start\": 572"; "\"classification\": \"unexplained\"" | dashboard/src/panels/review/laneReview.file.captured.json:104-116 |
| The receipt row for this body. | "src/panels/review/laneReview.file.captured.json" | dashboard/src/panels/review/laneReview.capture-provenance.json:67-67 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new captured per-file classification body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
