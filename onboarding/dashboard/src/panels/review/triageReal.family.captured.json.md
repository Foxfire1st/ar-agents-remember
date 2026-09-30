# dashboard/src/panels/review/triageReal.family.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/triageReal.family.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**FAM-R6R095RW's review ("Coherent intent and source review") on the real scratch leaf** (182,908 bytes; test
evidence for `FamilyTree.triageReal.test.tsx`).

## Code Commentary

### Logic

- All 24 members returned (the pages are `complete: false` because the read owner's page also counts realization
  items), guarantee `unchanged`, `members_total` 24: 2 `intent` (INV-2E8MG43K with `text_differs`; INV-ZS9ZS878 with
  `+impl`), 6 `implementation` (INV-BR5MTSTY, H8EM1VJR and VPX81HXV with `+unknown` for entries at an older recorded
  before-side blob; the stale-at-base repairs worded "re-anchored (stale at base)"), 1 `membership` (INV-2TQGXFAX), 15
  `unchanged` (INV-ZY0YMXMQ's carried entry among them).
- The limitations name `review:trees:2`.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the MIK-L33 worker's scratch copy under `/tmp/mik-l33-real` (memory `0b176f6b` converted with the worktree's `knowledge-convert` and committed as scratch `main` `0c3a0f83` with `Code-Commit` `904e804b`; the leaf's own code change and SCRATCH-AUTHORED knowledge edits), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The family context with its change facts. | "family_context"; "\"change_kinds\": {" | dashboard/src/panels/review/triageReal.family.captured.json:116-2082 |
| The comparison token. | "review:trees:2" | dashboard/src/panels/review/triageReal.family.captured.json:2496-2503 |
| The receipt row for this body. | "src/panels/review/triageReal.family.captured.json" | dashboard/src/panels/review/triageReal.capture-provenance.json:11-11 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new real family body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
