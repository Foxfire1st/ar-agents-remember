# dashboard/src/panels/review/laneReview.lane.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneReview.lane.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&lane=files` body of the MIK-L32 scratch leaf: the lane's two
destinations** (6,595 bytes; test evidence for `laneFocus.test.ts` and `ReviewSurface.lane.test.tsx`).

## Code Commentary

### Logic

- `measured`: 7 changed = 3 attributed + 3 unexplained + 1 of unknown attribution, and `paths` with every path's
  bucket (ruling Q1).
- `Unexplained changes` (5 files · 3 hunks · 2 non-text): `CONTRIBUTING.md`, `docs/scratch-lane.bin` (binary, gate
  `unexplained`) and the new module, then the attributed retention module (1 unexplained of 2 hunks) and
  `review_family_rosters.py` (mode-only, gate `unexplained`).
- `Unknown attribution` (1 file · 1 hunk): `review_source_admission.py`, whose four entries are all
  `recorded_blob_mismatch` on both sides.
- Re-captured after review R1 F4: only the admission row's reason and its two `unknown_reasons` changed wording (the
  count-then-list form).

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
| The totals and every path's bucket. | "paths"; "\"state\": \"measured\"" | dashboard/src/panels/review/laneReview.lane.captured.json:58-94 |
| The `Unexplained changes` destination and its totals. | "unexplained_changes"; "\"non_text\": 2" | dashboard/src/panels/review/laneReview.lane.captured.json:95-182 |
| The `Unknown attribution` destination, with the entries recorded at an older blob. | "unknown_attribution"; "after: 4 entries recorded here supply no range" | dashboard/src/panels/review/laneReview.lane.captured.json:183-207 |
| The receipt row for this body. | "src/panels/review/laneReview.lane.captured.json" | dashboard/src/panels/review/laneReview.capture-provenance.json:52-52 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new captured lane body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
