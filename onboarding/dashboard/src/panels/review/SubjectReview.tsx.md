# SubjectReview.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SubjectReview.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Render statements and evidence for the server-selected subject in the central review, including an invariant with confirmed no-family context.

## Code Commentary

### Logic

selectedRevision checks the payload's revision_selection against the requested subject kind and identity. SelectedStatement uses those exact before/after revisions and the owner's statement operands; unchanged, distinct successor, one-sided, ambiguous and unresolved states remain different. KnowledgeStatements renders the actual available operands using the chosen diff layout.

SubjectEvidence requires that same selected-subject match before rendering the read owner's observations, assessments and evidence claims. Records keep their authored disposition, currentness, applicability and provenance. Candidate-level execution is labelled as input rather than subject judgment. AssessmentAbsence distinguishes an unreadable/unmeasured channel from no returned authored judgment, while unrelated context records remain attributed to their own subjects.

**Decluttered statements (MIK-R31 rule 3, the 13:40 decision; MIK-L31).** `SelectedStatement` takes the
selected subject's member rows (`members`, from the centre's `subjectRows`) and `authoredSides` builds each
revision's authored wording: from the member row of that exact revision when the page carried it (statement,
applicability, conditions, exclusions), else from the knowledge pane (statement, conditions) plus the comparison's
own `field_changes`; a field neither carries stays uncarried. `wordingComparison` (`statementWording.ts`) then
decides, and `statementLabel` prints: "Statement unchanged · same recorded revision" for one revision, **"Wording
unchanged · revision a → b"** only when every authored field is identical, "Changed conditions · revision a → b"
(the changed fields named, with `ChangedFields` listing each non-statement field's before and after), or
"Statement revised · … not carried here" when a field could not be compared. The revision labels are the display
versions when both are carried and differ, else the revisions' own short identities, so two revisions never read as
one. `StatementBody` shows the prose once only when the statement did not change and **both** sides are present
(review F5); otherwise `KnowledgeStatements` keeps each side's own state line. An added or removed statement
(`OneSidedStatement`) is labelled prose ("Added statement · recorded on the after side only"), not a split code
editor. These rules apply to dataset reviews too, as rule 3 intends (review F8).

### Conventions

The browser renders the existing server revision selection and record-channel fields. It does not select a latest head or derive an assessment from a roster row.

### Invariants And Boundaries

A family-selected payload cannot establish a member's assessment absence. A roster row identifies navigation/context; it is not the authoritative statement comparison. Missing selected-subject data makes no before/after or unassessed claim. Ambiguous revision selection is not reduced to a first/last guess. A confirmed no-family invariant retains its statement, expressions and own evidence.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. The behavior is the existing repository review contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The selected subject is checked before either central statement or evidence is presented.

| Finding | Anchor | Source |
| --- | --- | --- |
| `selectedRevision` binds the central account to the supplied subject read. | `selectedRevision` | dashboard/src/panels/review/SubjectReview.tsx:33-41 |
| The selected statement: the two revisions' authored wording compared by the 13:40 rule, labelled with compact revision metadata. | "export function SelectedStatement({" | dashboard/src/panels/review/SubjectReview.tsx:217-280 |
| The state, the label, and each revision's authored wording from its member row or the pane. | `statementState`; `statementLabel`; `authoredSides` | dashboard/src/panels/review/SubjectReview.tsx:43-50; dashboard/src/panels/review/SubjectReview.tsx:59-74; dashboard/src/panels/review/SubjectReview.tsx:79-123 |
| Changed fields named; prose once only with both sides present (F5); one-sided statements as labelled prose. | `ChangedFields`; `StatementBody`; `OneSidedStatement` | dashboard/src/panels/review/SubjectReview.tsx:131-153; dashboard/src/panels/review/SubjectReview.tsx:155-195; dashboard/src/panels/review/SubjectReview.tsx:199-215 |
| The rule 3 cases. | "describe('wording unchanged'" | dashboard/src/panels/review/statementWording.test.tsx:53-135 |
| `SubjectEvidence` binds the central account to the supplied subject read. | `SubjectEvidence` | dashboard/src/panels/review/SubjectReview.tsx:356-426 |
| `AssessmentAbsence` binds the central account to the supplied subject read. | `AssessmentAbsence` | dashboard/src/panels/review/SubjectReview.tsx:339-354 |

## Cross-Repo References

No independent cross-repository interface is introduced.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Logic records MIK-R31 rule 3 (the 13:40 decision): "Wording unchanged · revision a → b" only when every authored field is identical, changed fields named, one-sided statements as labelled prose, prose once only with both sides present (review F5 at 06:10:21), and the rule applying to dataset reviews (review F8). **Reopened claim reworded and re-anchored:** the `SelectedStatement` row, now on a line-exact quote; this pass's generated bullet for it was removed. Three rows added.
- 2026-09-30T07:51:10+00:00: Generated citation repair: `SubjectEvidence` repointed to dashboard/src/panels/review/SubjectReview.tsx:356-426. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:51:10+00:00: Generated citation repair: `AssessmentAbsence` repointed to dashboard/src/panels/review/SubjectReview.tsx:339-354. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:11:42+00:00: Generated citation repair: `SubjectEvidence` repointed to dashboard/src/panels/review/SubjectReview.tsx:190-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:11:42+00:00: Generated citation repair: `AssessmentAbsence` repointed to dashboard/src/panels/review/SubjectReview.tsx:173-188. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-26T20:20:54Z — Created the owner for authoritative subject statements and evidence, preserving no-family and ambiguous selection states.
