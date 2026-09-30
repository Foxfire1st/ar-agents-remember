# dashboard/src/panels/review/triage.family.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/triage.family.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**FAM-F00001's review on the store-authored comparison** (`selectorKind=family`, 147,276 bytes; test evidence for
`changeTriage.test.ts`, `FamilyTree.triage.test.tsx` and `ReviewSurface.triage.test.tsx`).

## Code Commentary

### Logic

- One family, FAM-F00001, with all nine members returned and `change_kinds`: guarantee `unchanged`, `members_total`
  9, and one occurrence per member: INV-AAAAAA `intent` `+impl +unknown`, INV-BBBBBB and INV-CCCCCC `implementation`,
  INV-DDDDDD `implementation` `+test +unknown`, INV-GGGGGG `unknown` (its reasons name RLZ-G00001's blobs),
  INV-HHHHHH `intent` `+membership`, and INV-EEEEEE, INV-FFFFFF and INV-KKKKKK `unchanged`; each with
  `authored_position`, `evidence`, `unknown_reasons` and `membership_reasons`.
- The limitations name `review:trees:1`.

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
| The family context with its change facts. | "family_context"; "\"change_kinds\": {" | dashboard/src/panels/review/triage.family.captured.json:116-1165 |
| The comparison token. | "review:trees:1" | dashboard/src/panels/review/triage.family.captured.json:1399-1405 |
| The receipt row for this body. | "src/panels/review/triage.family.captured.json" | dashboard/src/panels/review/triage.capture-provenance.json:24-24 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new store-authored family body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
