# dashboard/src/panels/review/statementWording.ts

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` and the ICR master decision of
2026-09-28T13:40 live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of the 13:40 rule. [1]
- The four fields and the carried/uncarried distinction. [2]
- The comparison: an uncarried field is never identical. [3]
- A member row's authored fields, shared by the statement and the navigator. [4]
- The tree comparison's text-first decision: the bytes decide even at one revision. [5]
- The compact metadata. [6]
- The guarantee's compact revision labels, moved here and shared. [7]
- The statement label and body that use it. [8]
- The cases. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
