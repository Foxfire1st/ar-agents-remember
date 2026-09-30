# dashboard/src/panels/review/statementWording.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/statementWording.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:23:08+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The "wording unchanged" rule of MIK-R31 rule 3 (the ICR master decision of 2026-09-28T13:40, as written).** Two
revisions' wording is unchanged only when every authored text field is identical: the statement, the
applicability, each condition and each exclusion (or, for a family, the guarantee). Then the text is shown once,
with `revision <before> → <after>` as compact metadata and the record IDs in details. `SubjectReview.tsx`'s
`SelectedStatement` and `FamilyReviewCenter.tsx`'s identical-guarantee block use it.

**Since MIK-L35 it also holds the tree comparison's text-first decision and two shared helpers:**
`textFirstComparison` (MIK-R35 rule 1: on a tree comparison the bytes decide, even at one revision), `rowWording`
(a member row's authored fields, shared by `SubjectReview.authoredSides` and the family navigator's member tag), and
`guaranteeRevisionLabels` (moved here from `FamilyReviewCenter.tsx` so the landed guarantee block and
`IntentWordDiff.GuaranteeTextChange` share one label rule).

## Code Commentary

### Logic

- `wordingComparison(before, after, sameRevision)` answers `same_revision` for one recorded revision, `changed` with
  every field that differs, `not_comparable` with every field that was not carried (`undefined`) when nothing
  differs, and `wording_unchanged` only when all four fields are carried and identical. A revision that changes only
  a condition is `changed` with `conditions`, never "wording unchanged".
- `same` compares by JSON text and returns `undefined` when either side was not carried, so an unknown is never
  promoted to identical (an empty value is a carried value, distinct from "not carried").
- `revisionMeta(before, after)` prints `revision <before> → <after>`.
- `textFirstComparison(before, after, sameRevision)` (MIK-L35) compares the fields as if the revisions differed, and
  answers `same_revision` only when the revisions are one **and** no carried field differs; otherwise the fields'
  own answer stands. A text record's revision increments only when its meaning changes (MIK-R21), so one revision can
  carry different bytes on its two sides; there the answer is `changed`, and `SubjectReview` adds "the same revision
  on both sides; its text differs" (ruling Q1, 2026-09-30T11:53:13). Only the tree-comparison path uses it; a dataset
  review keeps `wordingComparison`, where one revision id is one immutable text.
- `rowWording(row)` reads a member row's statement, applicability (`null` when the row recorded none), conditions
  and exclusions (review R1 F1: `SubjectReview` and `FamilyTree` share it).
- `guaranteeRevisionLabels(before, after)` gives the display versions, or the revisions' short identities when the
  display versions read alike, so two authored revisions never read as one.

### Conventions

- `AuthoredWording` marks a field that was not carried as `undefined` and an applicability recorded as none as
  `null`.

### Invariants And Boundaries

- The rule applies to dataset reviews too (review F8): "Wording unchanged · revision a → b", one-sided prose and an
  identical guarantee shown once are rule 3's intended rendering on every review; only the code and test
  expressions differ between a dataset and a tree comparison. **Since MIK-L35** a tree comparison also differs in
  its statement and guarantee rendering: its changed fields are word-diffed (MIK-R35), and `textFirstComparison`
  decides there. The dataset path keeps this rule unchanged (ruling Q3).

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
| The four fields and the carried/uncarried distinction. | `WordingField`; `AuthoredWording` | dashboard/src/panels/review/statementWording.ts:10-10; dashboard/src/panels/review/statementWording.ts:12-18 |
| The comparison: an uncarried field is never identical. | `same`; `wordingComparison` | dashboard/src/panels/review/statementWording.ts:43-46; dashboard/src/panels/review/statementWording.ts:48-60 |
| A member row's authored fields, shared by the statement and the navigator. | `rowWording` | dashboard/src/panels/review/statementWording.ts:20-33 |
| The tree comparison's text-first decision: the bytes decide even at one revision. | `textFirstComparison`; "one revision can" | dashboard/src/panels/review/statementWording.ts:62-73 |
| The compact metadata. | `revisionMeta` | dashboard/src/panels/review/statementWording.ts:75-77 |
| The guarantee's compact revision labels, moved here and shared. | `guaranteeRevisionLabels` | dashboard/src/panels/review/statementWording.ts:79-89 |
| The statement label and body that use it. | `statementLabel`; `StatementBody` | dashboard/src/panels/review/SubjectReview.tsx:62-77; dashboard/src/panels/review/SubjectReview.tsx:193-233 |
| The cases. | "renders two revisions with identical authored text once, with the revisions as metadata"; "never labels a condition-only revision unchanged: the changed condition is named" | dashboard/src/panels/review/statementWording.test.tsx:54-84 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): body update. Purpose, Logic and Invariants record `textFirstComparison` (MIK-R35 rule 1; ruling Q1 of 2026-09-30T11:53:13, datasets unchanged by Q3), `rowWording` (review R1 F1 and F2, 12:16:39) and `guaranteeRevisionLabels` (moved here from `FamilyReviewCenter.tsx`). Three rows added. The `same`/`wordingComparison` row, which the installed fixer declined (`same` is ambiguous), was re-pointed by the exact base-to-staged line shift (`28-31` → `43-46`, `33-45` → `48-60`); the fixer's `revisionMeta` bullet is kept.
- 2026-09-30T11:15:42+00:00: Generated citation repair: `revisionMeta` repointed to dashboard/src/panels/review/statementWording.ts:75-77. No content impact: mechanical anchor-range projection bound to citation source snapshot 2597c838ec1e64a918943e8db9f63ef52ddf51fa320d55ca6abc370de5fa8b59; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new module MIK-R31 adds (rule 3), recording review F8 (datasets change in statement rendering as rule 3 intends). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
