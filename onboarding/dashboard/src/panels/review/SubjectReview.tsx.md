# dashboard/src/panels/review/SubjectReview.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render only the server-selected subject's statement comparison, using that subject's exact revision selection and side-specific authored wording.

## Code Commentary

`selectedRevision` admits revision_selection only when record kind and identity match the requested subject. Without it, SelectedStatement states that no comparison was supplied. `authoredSides` first looks for each selected revision in that side's own recorded member rows; otherwise it uses the knowledge pane's statement/conditions and only field-change rows keyed to the selected revisions. Projected exclusions remain marked, and a missing field stays uncarried.

`textFirstComparison` examines those actual authored words, including a same revision whose text differs. Compared/added/removed selections delegate to IntentStatementBody; ambiguous or unresolved selection states show explicit operand states without inventing a diff. Statement labels identify which authored fields changed, one-sided recording, unchanged wording or missing fields. Display labels use carried revision display versions, never raw revision IDs as a replacement; two distinct revisions are not labelled as one.

The label is passed into the wording renderer beside its layout control. Record origin and revision identifiers belong to Technical details. This module re-exports SubjectJudgment while keeping that owner's exact subject matching and outcome/proof rendering separate.

## Evidence

- SubjectReview.tsx current behavior at this source owner. [20]
- SubjectReview.tsx current behavior at this source owner. [21]
- SubjectReview.tsx current behavior at this source owner. [22]
