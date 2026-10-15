# dashboard/src/panels/review/FamilyReviewCenter.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The centre of the reviewer: for the selection of the family tree it renders the family guarantee, the
member context, the selected intent, the code and test expressions, the evidence, and for a tree
comparison the worklist items about the selected record. Layout, the open path and the leaf-wide tree read are passed in by
the workspace; the file itself reads only the entries of the selected invariants, through
`useReviewTreeEntries`.

The centre of the reviewer renders the family guarantee, the member context, the selected intent, the code and test expressions, and the evidence for the selected family or member. It carries the catalogue outline for member rows and draws planning marks only from a leaf-wide worklist that belongs to the comparison on screen. Layout, the open path and the leaf-wide tree read arrive by props; the file reads only the entries of the selected invariants.
## Code Commentary

Family expression membership uses the already-shown family's member set, adding a standalone invariant identity only when no family is shown. The extracted guarantee component retains exact authored before/after text and styles; pending subject selection does not imply another same-set cards read.


### Recorded reviewer judgments

The selected family/member reading area joins MeaningBlock to its own canonical record beside the guarantee or intent content, never to a kept family’s history. The no-subject and member-without-identity branches use MeaningFieldGuard: a missing field is failure while a present empty collection remains valid. Recorded steps are open content outside disclosures, preserve own row revisions and reasons, and do not replace the before/after wording diff or the independent source/evidence owners.


### Which centre

- `FamilyReviewCenter` wraps the body in `IntentWordDiffScope`, which marks a tree comparison for the
  word-level wording diff. `ReviewCenterBody` reads the selection with `centerSelection` and renders one
  of four centres: `MemberCenter` when the addressed subject is an invariant; otherwise `UnselectedCenter`
  when no family entry is selected, `UnavailableMember` when a member row is selected (a row that names
  no invariant identity addresses no subject), and `FamilyCenter` for a family.
- `centerSelection` finds the selected family entry and member row; the member rows to show (the
  subject's rows for an invariant subject, every row of the entry otherwise, none for a row without an
  invariant identity); the set of listed source paths; and `linksIncomplete`, which is true when the
  entry's member context is not complete (`membersComplete`).
- `membersComplete` requires, for each side, either the state `not_recorded`, or `recorded` with a
  complete page, as many loaded members as the side's total, and every member row `recorded`.

### What each centre shows

- `FamilyCenter`: the family label with open comparison details, the guarantee comparison
  (`GuaranteeComparisonBlock`), `FamilyMemberContext` with distinct member revisions ordered by
  `orderedCenterMembers`, the expressions, an open realization-resolution section, the family evidence
  and the selected record's worklist items.
- `MemberCenter`: the member label and `MemberFamilyLabel`, the family guarantee when present,
  `SelectedStatement` with `subjectRows` kept per side, the expressions, open independent facts and
  selected roster-revision context, subject evidence, selected-record worklist items and the roster
  continuation. These semantic facts are not behind a disclosure.
- `UnselectedCenter`: selected statements or an explicit unselected/source-only sentence; the leaf's
  complete worklist is a separate workspace destination, not an automatically embedded patch panel.
- `UnavailableMember`: the guarantee comparison, the member's statement, the sentence that this page
  did not supply the member's invariant identity, and the roster continuation. It shows no knowledge
  panel.

### Member order

The center retains distinct member revisions from both sides. Where the served outlined comparison covers the family, `displayedMemberRanks` takes invariant positions from the same `outlineGroups` call the sidebar uses, under the stored triage/authored preference. Both revisions of one invariant occupy its sidebar position. Members without a position remain last with stable relative order. Without an outlined group, `orderedCenterMembers` falls back to `orderMemberRows`; it does not invent an outline, reclassify change facts or discard semantic siblings. The tree is one row per invariant, while the center remains one row per revision.

### Guarantee comparison

`GuaranteeComparisonBlock` renders, on a tree comparison whose two sides both carry a guarantee with
differing text, the word-diffed `GuaranteeTextChange`. Otherwise it renders by the kind `guaranteeComparison` returns: a sentence when
neither snapshot selected a family revision; a one-sided guarantee labelled "Added guarantee" or "Removed
guarantee" (on a tree comparison through `OneSidedGuaranteeLabel`); "Guarantee unchanged · same recorded
revision"; "Wording unchanged" with both revisions when two revisions carry identical text; and a diff of
the two texts when they differ.

### Expressions

`CenterExpressions` asks `useReviewTreeEntries` for the entries of `cardInvariants`, every member of the
selected family on both sides, or the selected invariant alone when no family is shown, sorted, at the comparison number
the payload names. When the payload names no tree comparison (a dataset review) or the selection names
no invariant, the hook returns `null` and `ReviewExpressions` renders the file view. Otherwise
`ExpressionCards` renders the cards with the planning marks of `pinnedWorklist`, which passes the
leaf-wide read's worklist only when that read answered for the comparison the payload was composed over.

### Record worklist items

The selected family/member receives `SubjectWorklistItems` bound to its canonical record identity and
the payload's comparison. A missing/mismatched/unavailable read remains explicit; no subject filter is
invented from labels. The complete worklist belongs to `LeafWorklistView` in the workspace's own view.
Neither subject review nor that worklist embeds knowledge-file patches.

## Evidence








- Guarantee rendering for one side or a compared pair [26]

- The guarantee comparison by kind. [12]
- The unselected centre. [13]
- The completeness of a family entry's member context. [14]
- The family centre. [15]
- The independent facts of a member. [16]
- The member centre. [17]
- The exported wrapper sets the word-diff scope. [18]
- Builds expressions and selected-record SubjectKnowledge, then chooses member, unselected, unavailable-member or family content; the unavailable-member branch receives expressions but not the knowledge panel. [19]
- Planning marks only from a leaf-wide read of the same comparison. [20]
- Cards for a tree comparison, the file view for a dataset review. [22]
- The invariants one selection reads. [23]
- The selected entry, member, rows and listed paths. [24]
- One expression row per collection with verdict and occurrences [27]
- Member review centre with subject rows and states [28]
- Card read assembly for the selected centre [31]
- The selected family/member reading area joins MeaningBlock to its own canonical record beside the guarantee or intent content, never to a kept family’s history. [32]
- Member revisions follow outline positions under the stored order, with stable unknown-last and no-outline fallback. [33]
