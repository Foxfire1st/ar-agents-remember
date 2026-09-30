# dashboard/src/panels/review/laneReview.source.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneReview.source.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/source-content` body of the MIK-L32 scratch leaf: both exact blobs of
`review_comparison_retention.py` at the listed generation** (53,371 bytes; test evidence for `ReviewSurface.lane.test.tsx`,
where the focused hunk's window is cut from it).

## Code Commentary

### Logic

- `state: "content"`, admission `changed`, currentness `current`, language `python`; the before blob `87c7c5dc…`
  (24,801 bytes) and the after blob `99f7742a…` (24,961 bytes), both `present` and not truncated.

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
| Both sides' exact blobs, complete. | "\"object_id\": \"99f7742aa7822bbb2aa54c46ba72113e1f12c602\""; "\"object_id\": \"87c7c5dcefcbaf93baf68a0c8eec34ad2dd11703\"" | dashboard/src/panels/review/laneReview.source.captured.json:2-33 |
| The receipt row for this body. | "src/panels/review/laneReview.source.captured.json" | dashboard/src/panels/review/laneReview.capture-provenance.json:82-82 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new captured source-content body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
