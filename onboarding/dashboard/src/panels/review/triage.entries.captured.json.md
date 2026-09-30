# dashboard/src/panels/review/triage.entries.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/triage.entries.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The store-authored comparison's subject catalogue** (`GET /api/review/intent/entries`, 2,922 bytes; test evidence
for `ReviewSurface.triage.test.tsx`, the catalogue the mounted surface lists).

## Code Commentary

### Logic

- `state` `entries`: 18 subjects (3 families, 15 invariants) of leaf `260101-TRV-L1`.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body is served over the SYNTHETIC store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: a live leaf `260101-TRV-L1` of master `260101_tree_review` over four real Git trees), not current project knowledge; its identities, blobs and scratch paths are that world's.

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
| The catalogue's entries and totals. | "list_knowledge_review_entries"; "\"total_subjects\": 18" | dashboard/src/panels/review/triage.entries.captured.json:112-119 |
| The receipt row for this body. | "src/panels/review/triage.entries.captured.json" | dashboard/src/panels/review/triage.capture-provenance.json:11-11 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new store-authored catalogue body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
