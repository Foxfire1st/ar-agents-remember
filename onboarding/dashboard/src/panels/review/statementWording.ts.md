# dashboard/src/panels/review/statementWording.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/statementWording.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T09:59:20+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The "wording unchanged" rule of MIK-R31 rule 3 (the ICR master decision of 2026-09-28T13:40, as written).** Two
revisions' wording is unchanged only when every authored text field is identical: the statement, the
applicability, each condition and each exclusion (or, for a family, the guarantee). Then the text is shown once,
with `revision <before> → <after>` as compact metadata and the record IDs in details. `SubjectReview.tsx`'s
`SelectedStatement` and `FamilyReviewCenter.tsx`'s identical-guarantee block use it.

## Code Commentary

### Logic

- `wordingComparison(before, after, sameRevision)` answers `same_revision` for one recorded revision, `changed` with
  every field that differs, `not_comparable` with every field that was not carried (`undefined`) when nothing
  differs, and `wording_unchanged` only when all four fields are carried and identical. A revision that changes only
  a condition is `changed` with `conditions`, never "wording unchanged".
- `same` compares by JSON text and returns `undefined` when either side was not carried, so an unknown is never
  promoted to identical (an empty value is a carried value, distinct from "not carried").
- `revisionMeta(before, after)` prints `revision <before> → <after>`.

### Conventions

- `AuthoredWording` marks a field that was not carried as `undefined` and an applicability recorded as none as
  `null`.

### Invariants And Boundaries

- The rule applies to dataset reviews too (review F8): "Wording unchanged · revision a → b", one-sided prose and an
  identical guarantee shown once are rule 3's intended rendering on every review; only the code and test
  expressions differ between a dataset and a tree comparison.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` and the ICR master decision of
2026-09-28T13:40 live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the 13:40 rule. | "A revision that changes only a condition is NOT"; "never promoted" | dashboard/src/panels/review/statementWording.ts:1-8 |
| The four fields and the carried/uncarried distinction. | `WordingField`; `AuthoredWording` | dashboard/src/panels/review/statementWording.ts:10-18 |
| The comparison: an uncarried field is never identical. | `same`; `wordingComparison` | dashboard/src/panels/review/statementWording.ts:28-31; dashboard/src/panels/review/statementWording.ts:33-45 |
| The compact metadata. | `revisionMeta` | dashboard/src/panels/review/statementWording.ts:47-49 |
| The statement label and body that use it. | `statementLabel`; `StatementBody` | dashboard/src/panels/review/SubjectReview.tsx:59-74; dashboard/src/panels/review/SubjectReview.tsx:155-195 |
| The cases. | "renders two revisions with identical authored text once, with the revisions as metadata"; "never labels a condition-only revision unchanged: the changed condition is named" | dashboard/src/panels/review/statementWording.test.tsx:54-84 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new module MIK-R31 adds (rule 3), recording review F8 (datasets change in statement rendering as rule 3 intends). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
