# SubjectReview.tsx

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

**Word-level intent diff on a tree comparison (MIK-R35, MIK-L35).** `SelectedStatement` reads the tree-comparison
scope (`useTreeComparison`, set by `FamilyReviewCenter`). On a tree comparison the decision is
`textFirstComparison` (`statementWording.ts`): the fields decide, and "Statement unchanged · same recorded revision"
is said only of one revision whose carried fields do not differ, because a text record's revision increments only
when its meaning changes (MIK-R21). One revision whose text differs reads **"Changed statement · revision r2 → r2 ·
the same revision on both sides; its text differs"** (`sameRevisionNote`; ruling Q1, 2026-09-30T11:53:13). For a
compared, added or removed selection the body is `IntentStatementBody` (`IntentWordDiff.tsx`): one word-diffed
passage per changed field. Ambiguous and unresolved selections keep the landed "no statement diff" body. A dataset
review keeps `wordingComparison` and the landed `StatementBody` (ruling Q3).

**Each side's text from its own row (review R1 F1, ruled 2026-09-30T12:16:39).** `members` is `MemberSides`
(`{ before, after }`, built by `FamilyReviewCenter.subjectRows` from each side's own roster), and `authoredSides`
looks up the before row only among the before rows and the after row only among the after rows, so one revision's
two texts are never both read from one side's row. A side with no recorded row of its own falls back to the pane
(statement, conditions) and to the comparison's `field_changes` **filtered to the selected before and after revision
ids** (`item_id`): the page's field rows also report other records' changes, and those are never this subject's
(ruling Q4, applied on tree and dataset reviews alike). When a side had no row and the `exclusions` field row
answered, the list is `projected` (the joined report), which the renderer shows as reported rather than aligning.
`revisionLabels` prints the display versions when both are carried and differ, **one revision's own version on both
sides** (it is one number, whichever side carried it), else the revisions' short identities, so two revisions never
read as one.

### Conventions

The browser renders the existing server revision selection and record-channel fields. It does not select a latest head or derive an assessment from a roster row.

### Invariants And Boundaries

A family-selected payload cannot establish a member's assessment absence. A roster row identifies navigation/context; it is not the authoritative statement comparison. Missing selected-subject data makes no before/after or unassessed claim. Ambiguous revision selection is not reduced to a first/last guess. A confirmed no-family invariant retains its statement, expressions and own evidence.

**Candidate invariant (not ingested): each side's text comes only from that side's own row, or from its pane or
filtered field rows** (MIK-L35; review R1 F1 and ruling Q4). Realized by `authoredSides` over `MemberSides` and the
`selected.includes(change.item_id)` filter; proved by the three F1 probe cases and the Q4 case of
`IntentWordDiff.test.tsx` (the mutations G1, G2, R1 and R2 fail them). On a tree comparison no statement label calls a
changed text unchanged: `textFirstComparison` lets the bytes decide even at the same revision (the candidate
invariant recorded on `IntentWordDiff.tsx.md`). For datasets the per-side lookup renders as before in every
realistic configuration (the reviewer's R2 differential: 8 of 9 configurations byte-identical, the ninth needs an
unrealistic roster).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The behavior is the existing repository review contract.

No configured domain source could be checked.

### Repo-Internal References

The selected subject is checked before either central statement or evidence is presented.

- `selectedRevision` binds the central account to the supplied subject read. [1]
- The selected statement: the two revisions' authored wording compared by the 13:40 rule (text-first on a tree comparison), labelled with compact revision metadata, and word-diffed by `IntentStatementBody` on a tree comparison. [2]
- The state, the label, and the same-revision note for one revision whose text differs (ruling Q1). [3]
- Each side's authored wording from that side's own member row, else the pane and the field rows filtered to the selected revisions (F1, Q4), with the projected exclusions marked. [4]
- The revision labels: one revision's own version on both sides, two revisions never as one. [5]
- Changed fields named; prose once only with both sides present (F5); one-sided statements as labelled prose (the dataset path). [6]
- The tree-comparison statement body and its cases. [7]
- The rule 3 cases. [8]
- `SubjectEvidence` binds the central account to the supplied subject read. [9]
- `AssessmentAbsence` binds the central account to the supplied subject read. [10]

### Cross-Repo References

No independent cross-repository interface is introduced.

No additional cross-repository evidence is required.
