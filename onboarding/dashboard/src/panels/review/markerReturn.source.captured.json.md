# dashboard/src/panels/review/markerReturn.source.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerReturn.source.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/source-content` body for `serving/notes.py` of the MIK-L34 scratch leaf at trees
`59daf505` → `db68db54`** (28,595 bytes; test evidence for `ReviewSurface.markers.test.tsx`). Its bytes are identical
to `markerUnknown.source.captured.json` (the same content at the same trees).

## Code Commentary

### Logic

- `content`, status `modified`, `current`: the before blob `e3e6f8d4` (12,923 bytes) and the after blob `9019bea5`
  (12,848 bytes), both `present` with their whole texts, the exact objects the classification names, so
  `describesDrawn` holds and the marks are placed.

- **Re-captured in MIK-L33's merge round** over the merged tree (MIK-L34 landed; the review route now carries `change_kinds`). Against MIK-L34's capture it differs only by scratch paths, the converted memory commit, timestamps and comparison digests (the reviewer's structural diff, review R3 point 5).

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l33-merge`: MIK-L34's scenario, rebuilt by MIK-L33's merge round with MIK-L34's own scripts (code `59daf505` with the scratch leaf's edits and the same curated blobs `9019bea5` and `b6d07091`; memory `76f5e91e1` converted and committed as scratch `main` `31ab7016`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

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
| The expansion: both sides present with the object ids the classification names. | "\"object_id\": \"9019bea5a3b9ace22947a516a78718f1a2d8f123\""; "\"object_id\": \"e3e6f8d4c246e066532296e69563c435200ae08b\"" | dashboard/src/panels/review/markerReturn.source.captured.json:2-36 |
| The receipt row for this body. | "src/panels/review/markerReturn.source.captured.json" | dashboard/src/panels/review/markerReturn.capture-provenance.json:55-55 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-L33's merge round** (review R3-3): the body was re-captured over the merged tree from MIK-L34's scenario rebuilt under `/tmp/mik-l33-merge` (scratch `main` `31ab7016`); it differs from MIK-L34's capture only by scratch paths, the memory commit, timestamps and comparison digests; the byte count and the scratch sentence are updated. Its sha256 and byte count match the updated receipt (checked by this curation). The rows' ranges were normalised by the installed fixer (its bullets kept).
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured `notes.py` source content (comparison 2). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
