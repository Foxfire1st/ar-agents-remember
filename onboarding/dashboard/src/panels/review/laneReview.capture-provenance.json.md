# dashboard/src/panels/review/laneReview.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneReview.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the six bodies MIK-L32 captured for its dashboard tests.** It names the capture time
(2026-09-30T11:17:05Z, after the review R1 fix round), the producer (`notes/reports/260928-MIK-L32-evidence/capture_ui_fixtures.py`,
task-local evidence outside the repository) and its command, the route (`create_app(config,
collaborators=serving_collaborators(config))` over a FastAPI `TestClient`), the source tree (the L32 worktree on base
`b54d1b03` with the leaf's changes), the scratch (`/tmp/mik-l32-real`: `--shared` clones, memory `58d016cb` converted with
the worktree's `knowledge-convert`; leaf `260928-MIK-L32` with seven changed files), comparison `2`, the attempts (one
capture per body, each the first answer), and one row per fixture with its route, parameters, status, seconds, sha256 and
bytes.

## Code Commentary

### Logic

- Six rows: the changed-intent summary (`GET /api/review/intent/summary`), the task review (`GET /api/review/intent`),
  the leaf-wide tree view (`GET /api/review/trees`, comparison 2), the lane (`lane=files`, 0.07 s), one file's
  classification (`file=` the retention module, 0.06 s) and that file's source content
  (`GET /api/review/intent/source-content`).
- The scratch leaf: `review_comparison_retention.py` edited inside `_side_binding` with a helper appended and its
  entries re-recorded at the candidate blob; `review_source_admission.py` edited in `_not_listed` (entries recorded at an
  older blob by the conversion); a new module, `CONTRIBUTING.md` and a new binary file with no entry;
  `review_family_rosters.py` made executable; a test body edited with a scratch-authored proof `PRF-7Q3M5K`.
- Review R1 F4 changed two reason strings, so the bodies were re-captured: only the lane body changed; the other five
  are byte-identical. The reviewer re-captured all six from the synced code at R2 and got identical bytes.

### Conventions

Keep the captured bytes and their receipt (`laneReview.capture-provenance.json`) intact; a recapture rewrites both.

### Invariants And Boundaries

These are scratch-copy captures, not current project knowledge or mounted-product acceptance. All six sha256 values
match the fixtures (checked by this curation).

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
| When, by what command and at which source tree the bodies were captured, and over which scratch leaf. | "captured_at"; "source_tree"; "scratch" | dashboard/src/panels/review/laneReview.capture-provenance.json:2-9 |
| One receipt row per captured body. | "\"fixtures\": [" | dashboard/src/panels/review/laneReview.capture-provenance.json:10-97 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new capture receipt (six bodies). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
