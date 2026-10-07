# dashboard/src/panels/review/FamilyReviewCenter.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The centre of the reviewer: for the selection of the family tree it renders the family guarantee, the
member context, the selected intent, the code and test expressions, the evidence, and for a tree
comparison the leaf's knowledge panel. Layout, the open path and the leaf-wide tree read are passed in by
the workspace; the file itself reads only the entries of the selected invariants, through
`useReviewTreeEntries`.

## Code Commentary

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

- `FamilyCenter`: the family's label with its comparison details, the guarantee comparison
  (`GuaranteeComparisonBlock`), the member context (`FamilyMemberContext`) with the distinct member
  revisions ordered by `orderMemberRows`, the expressions, a disclosure with the realization resolution
  details, the family's evidence, and the knowledge panel.
- `MemberCenter`: the member's label and family line (`MemberFamilyLabel`), the guarantee comparison when a
  family entry exists, the selected intent (`SelectedStatement`, with the subject's rows kept per side by
  `subjectRows`), the expressions, a disclosure with the independent facts and the roster revision
  context, the subject's evidence, the knowledge panel, and the roster continuation.
- `UnselectedCenter`: the selected statements, or the sentence that this is a source-only view, and the
  knowledge panel opened.
- `UnavailableMember`: the guarantee comparison, the member's statement, the sentence that this page
  did not supply the member's invariant identity, and the roster continuation. It shows no knowledge
  panel.

### Guarantee comparison

`GuaranteeComparisonBlock` renders, on a tree comparison whose two sides both carry a guarantee with
differing text, the word-diffed `GuaranteeTextChange`. Otherwise it renders by the kind `guaranteeComparison` returns: a sentence when
neither snapshot selected a family revision; a one-sided guarantee labelled "Added guarantee" or "Removed
guarantee" (on a tree comparison through `OneSidedGuaranteeLabel`); "Guarantee unchanged · same recorded
revision"; "Wording unchanged" with both revisions when two revisions carry identical text; and a diff of
the two texts when they differ.

### Expressions

`CenterExpressions` asks `useReviewTreeEntries` for the entries of `cardInvariants`, every member of the
selected family on both sides together with the selected invariant, sorted, at the comparison number
the payload names. When the payload names no tree comparison (a dataset review) or the selection names
no invariant, the hook returns `null` and `ReviewExpressions` renders the file view. Otherwise
`ExpressionCards` renders the cards with the planning marks of `pinnedWorklist`, which passes the
leaf-wide read's worklist only when that read answered for the comparison the payload was composed over.

### The knowledge panel

`knowledgePanel(leafTrees, payload, open)` decides what stands in the panel's place:

- no leaf-wide read at all (`null`, a dataset review): nothing;
- a read in the phase `trees`: `LeafKnowledgeChanges` with the trees and the payload's comparison number;
- a read in any other phase: `LeafKnowledgeNotice` with that read, which shows that the view is being
  computed or that it is unavailable, and nothing for `not-converted`.

The family, member and unselected centres all receive the panel from this one function; the unselected
centre receives it opened.

## Evidence

- The guarantee comparison by kind. [12]
- The unselected centre. [13]
- The completeness of a family entry's member context. [14]
- The family centre. [15]
- The independent facts of a member. [16]
- The member centre. [17]
- The exported wrapper sets the word-diff scope. [18]
- The body chooses one of four centres and passes the knowledge panel to each. [19]
- Planning marks only from a leaf-wide read of the same comparison. [20]
- The panel, the notice, or nothing. [21]
- Cards for a tree comparison, the file view for a dataset review. [22]
- The invariants one selection reads. [23]
- The selected entry, member, rows and listed paths. [24]
- The notice says that it is computing. [25]
