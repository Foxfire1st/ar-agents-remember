# dashboard/src/panels/review/markerReturn.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerReturn.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of five of the six real served bodies of the MIK-L34 worker's converted scratch leaf, comparison 2.** It
names the capture time (2026-09-30T13:48:07Z), the producer (`notes/reports/260928-MIK-L34-evidence/capture_ui_fixtures.py`)
and its command, the route (`create_app(config, collaborators=serving_collaborators(config))` over a FastAPI
`TestClient`), the source tree (the L34 worktree on base `59daf505` with its uncommitted changes; no server file
changed), the scratch (`/tmp/mik-l34-real`, `--shared` clones of the live repositories; memory `76f5e91e1` converted
and committed as scratch `main` with `Code-Commit` `59daf505`; the leaf's edits and `curate`), comparison `2`, the
attempts (one capture per body, each the first answer), and one row per body with route, parameters, status,
seconds, sha256 and bytes. The sixth comparison-2 body, `markerReturn.cards.captured.json`, was captured in the
rulings round and is receipted in `markerUnknown.capture-provenance.json`.

## Code Commentary

### Logic

- Five rows: the task-context review (`GET /api/review/intent`, 4.99 s), the lane (`lane=files`, 0.11 s), `notes.py`'s
  classification (`file=`, 0.07 s), `notes.py`'s source content (`GET /api/review/intent/source-content` at trees
  `59daf505` → `db68db54`, 3.3 s) and INV-Z66EMHMH's review (`selectorKind=invariant`, 5.54 s).
- The scratch leaf: `serving/notes.py` edited inside `_confined_stat` (two recorded ranges) and `list_notes`'s
  docstring line deleted (three recorded ranges); `review_comparison_retention.py` edited inside `_side_binding`
  with a helper appended; a new module with no entry; a test body edited with a scratch-authored proof `PRF-7Q3M5K`;
  INV-ZJS1XY4R reassigned out of FAM-4V4GSQCS on the after side; the `notes.py` and retention entries re-recorded at
  the candidate blob.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

These are scratch-copy captures, not current project knowledge or mounted-product acceptance. All five sha256 values match the fixtures (checked by this curation).

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
| When, by what command and at which source tree the bodies were captured, and over which scratch leaf. | "captured_at"; "source_tree"; "scratch" | dashboard/src/panels/review/markerReturn.capture-provenance.json:2-9 |
| One receipt row per captured body. | "\"fixtures\": [" | dashboard/src/panels/review/markerReturn.capture-provenance.json:10-85 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new capture receipt of five comparison-2 bodies. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
