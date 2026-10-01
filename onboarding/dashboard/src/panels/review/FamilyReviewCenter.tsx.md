# dashboard/src/panels/review/FamilyReviewCenter.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render the independently authored family guarantee, complete carried member context, selected intent, actual linked source/test diffs and bound evidence in one reading path.

## Code Commentary

### Logic

`membersComplete` requires every recorded side to have a completed page, all measured member contexts and recorded member content; an explicit not-recorded side is a different valid absence. It drives both the main expression notice and family-detail scope. The detail verdict counts only loaded resolved/unmeasured claims and never infers unchanged or complete expression coverage from an empty excerpt set. `memberContextCounts` separately states recorded membership totals and loaded context counts.

MemberCenter receives an explicit selected subject and delegates the authoritative statement/evidence account to SubjectReview. The selected roster revision remains inspectable context, while the source owner selected before/after revisions drive the actual statement comparison. An invariant with no family still renders its own central statement, expressions and evidence. UnavailableMember names a missing invariant identity and claims no assessment absence. **The member centre's family line is `MarkerTargetState.MemberFamilyLabel` (MIK-L34; ruling 2026-09-30T16:19:34 Q3).** It prints the review's own label as before (`<family> · Member review`, `No recorded family`, or `Family context unavailable`; the one-use `memberContextLabel` moved with it), except for the invariant an intent marker opened on an unknown membership that has no row in this tree: then it reads "Attribution unknown — <invariant>: <reason>. The review's family context reads: <its own label>.", so a marker's unknown membership never reads as the confirmed "No recorded family", and the review's own reading is kept beside it.

FamilyCenter presents the guarantee comparison, carried exact member revisions, the code and test expressions (`CenterExpressions`), then family evidence and, for a tree comparison, the leaf's knowledge panel. Realization-resolution summaries remain available in a disclosure; their pure grouping is owned by familyExpressions. MemberCenter keeps the family guarantee beside the selected statement, then renders actual expressions and the selected subject execution evidence/assessment. Statement, membership, source, guarantee and authored-judgment facts are separate. A missing side is interpreted from that side roster state and page completeness, never diffed against invented blank content.

**Focused expression cards for a tree comparison (MIK-R31, MIK-L31).** `CenterExpressions` asks `useReviewTreeEntries` for the entries of `cardInvariants` (every member of the selected family on both sides, or the selected invariant alone when it has no family on this page; sorted, so one selection is one read) at the payload's own comparison (`treeComparisonNumber`). A dataset review declares no `review:trees:<n>`, so the hook returns `null` and the landed `ReviewExpressions` renders unchanged; otherwise `ExpressionCards` renders one card per (path, range) with the selected invariant as the MIK-R01 seed, `cardScope(entry)` as the bounded-roster scope (review F2), and a path the reader opens from a card routed through `onOpenFromCenter`. **Planning marks come from one comparison only (review F11, R2-3):** `pinnedWorklist` passes the leaf-wide read's worklist to `planningMarks` only when that read's `comparison.number` equals the payload's; otherwise the cards carry no mark. `knowledgePanel` mounts `LeafKnowledgeChanges` (MIK-R25 rules 2-3, carried from L25 Q2) after the evidence in the family, member and unselected centres, and states a comparison mismatch there.

**Decluttered guarantees (MIK-R31 rule 3).** Identical guarantee text on two revisions is "Wording unchanged · revision a → b" (`revisionMeta` over `guaranteeRevisionLabels`: the display versions, or the revisions' short identities when those read alike), the guarantee shown once, with both revision IDs under "Revision records"; a guarantee recorded on one side is labelled "Added guarantee" or "Removed guarantee". `MemberCenter` passes the selected subject's member rows (`subjectRows`) to `SelectedStatement` so the 13:40 rule can compare every authored field. Since MIK-L35, `guaranteeRevisionLabels` lives in `statementWording.ts`, shared with the word-diffed guarantee.

**Word-level intent diff (MIK-R35, MIK-L35).** `FamilyReviewCenter` is now a thin exported wrapper that sets the tree-comparison scope (`IntentWordDiffScope`, from the payload's `review:trees:<n>`) around the unchanged body, renamed `ReviewCenterBody` and not re-indented (a small diff beside L32). Inside the scope:
- `GuaranteeComparisonBlock` first asks `guaranteeTextChange`: whenever both sides carry a guarantee and its text differs, **including one revision whose two texts differ** (MIK-R21; ruling Q1), it returns the word-diffed `GuaranteeTextChange` ("Changed guarantee · revision a → b" as one passage). On the tree path a one-sided guarantee carries `OneSidedGuaranteeLabel`, with the R06 known-absent line only when the other side records none. Otherwise, and always on a dataset review, the landed branches answer (ruling Q3: the dataset guarantee keeps its `DiffPane`).
- `IndependentFacts` prints the guarantee fact through `guaranteeFact`: `same_revision_text_changed` instead of `unchanged_revision` for one revision whose texts differ on a tree comparison (review R1 F2, 2026-09-30T12:16:39).
- `subjectRows` returns the subject's rows **per side** (`MemberSides`, from `entry.before.members` and `entry.after.members`), so `SelectedStatement` reads each side's text only from that side's own row (review R1 F1).

**The centre's member list follows the tree (MIK-L33; review R1 note, ruling 2026-09-30T17:47:43).** `FamilyCenter`
orders its distinct member revisions with `changeTriage.orderMemberRows(entry, …, useTreeOrder())`, the same rule and
the same browser-local order preference the tree uses, so on a tree comparison the centre lists the members in the
tree's displayed order, in triage and in authored order (`ReviewSurface.triage.test.tsx` checks both). A dataset
review's entry carries no change facts, so its order is unchanged. The centre draws no change badge of its own: the
badges, the breakdown and `j`/`k` are the tree's (`FamilyTree.tsx`, `ChangeBadges.tsx`), and a `j` move selects a
subject exactly as a click does, so the centre shows that subject's review. **The member centre's family line is
unchanged by MIK-L33** (review R3-3): it is still MIK-L34's `MemberFamilyLabel`; only the tree's member row states a
followed marker's unknown membership through the change facts.

### Conventions

The module is one default-free file of small function components plus private predicates
(`membersComplete`, `memberContextHeading`), private sentence builders (`missingRowNote`,
`memberContextCounts`, `familyExpressionVerdict`) and private pure helpers (`unlistedPathNote`,
`carriedMembership`, `excerptKey`, `claimClass`, `absorbClaim`, `tallyChangedExcerpts`,
`recordSideResolutions`, `orderExcerpts`, `occurrenceName`, `listedOrPlainPath`) that are pure functions of
their arguments. Its **exported surface is deliberately three names wide and one of them is the arithmetic
alone** — `familyExpressionExcerpts`, `FamilyMembershipRow`, and the `FamilyExcerptOccurrence` /
`FamilyExpressionExcerpt` / `FamilyExpressionCollection` result types — because the unit lane
(`familyExpressions.test.ts`) holds the arithmetic without a DOM while the mounted lane holds the rendering
over captured bodies. `carriedMembership`, `excerptKey` and `claimClass` stay private helpers even though a
test could reach them, so the arithmetic has one entry point. It imports its family values from
`../../data/review` (the public entry that re-exports the mirror module), the shared roster
components and the `FamilySelection` type from `./FamilyTree`, the diff renderer from
`../changeset/DiffPane`, and `SourceExplorer` with its `DiffLayout` type from `./SourceExplorer` —
one implementation of each, never a second. Styling uses the `styled-system/css` `css` helper with
module-level constants (`shell`, `sectionLabel`, `card`, `muted`, `prose`, `rows`, `linkButton`),
matching the cockpit panels' idiom. Every list item and block carries a stable `key`
(`assessment.assessment_id`, `observation.observation_id`, `claim.claim_id`,
`${location.claim_id}:${location.path}`, the member revision, and the excerpt's own dedup `key`) and a
machine-readable `data-testid`, with the owner's own values beside them where a case or a reader needs them
(`data-revision`, `data-family`, `data-family-state`, `data-side`, `data-binding`, `data-evidence-state`,
`data-change-state`, `data-fact`, `data-selection-kind`, `data-path`, and on each excerpt row the
arithmetic itself: `data-dedup-key`, `data-collapsed-rows`, `data-membership-rows`, `data-member-revisions`,
`data-sides`). Layout, full-file and open-path state are owned by the caller and threaded down, so switching
the diff layout while a file is open is the caller's state change rather than this component's; the only
state this file holds is none at all.

### Invariants And Boundaries

Only the same recorded revision may be described as unchanged; identical text on different revisions is a different fact, rendered as "Wording unchanged" with both revisions named. **On a tree comparison, one revision is unchanged only when its two texts are too** (MIK-L35; ruling Q1 and review R1 F2): the guarantee block, the details fact and the member statement compare the bytes, and a same-revision text change reads "the same revision on both sides; its text differs" (the candidate invariant recorded on `IntentWordDiff.tsx.md`). **Candidate invariant (not ingested): card planning marks come only from a leaf-wide read of the same comparison** (`pinnedWorklist`; proved by the gitTrees R2-3 case, where a leaf-wide body for comparison 2 against a payload for comparison 1 gives the panel's mismatch sentence and no planned or unplanned mark on any voice, and removing the `same` check fails it). **Candidate invariant (not ingested): dataset reviews make no tree read** (`CenterExpressions` falls back to `ReviewExpressions` when `useReviewTreeEntries` returns `null`; proved by the gitTrees dataset case, which asserts no `/trees` request, no cards and no knowledge panel). Partial member pages retain owner counts and continuation, and a missing row on one page proves no snapshot-wide absence. The selected-subject reader owns evidence applicability and currentness; the center preserves those bindings and labels unrelated records as context. Family or member changes do not create a semantic assessment. The complete source inventory is owned by the workspace rail.

### Todos

None recorded. The centre renders what the payload and the owners' records carry; the two known
limits of the surrounding family route — the browser-class journeys and the state a served bundle
would have to exercise — belong to the read/refresh and interaction increments rather than to this
rendering. **Size (MIK-L35):** the file is 1,111 lines, 89 under the 1,200 bound; L35 kept its growth to the scope
wrapper and two hooks, and further centre work should extract rather than grow it. **MIK-L34** changed one label
expression and moved `memberContextLabel` out (into `MarkerTargetState.tsx`), so the file is now 1,102 lines.
**MIK-L33** added two imports and the ordered member list, so it is 1,112 lines, 88 under the bound.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current ownership and boundaries above are grounded in these source declarations.

- The family centre: guarantee, carried members, the expressions slot, family evidence, then the leaf's knowledge panel. [1]
- The member centre: guarantee, the selected statement with the subject's member rows kept per side (MIK-L35, review R1 F1), the expressions slot, evidence, then the knowledge panel. [2]
- The centre entry: a thin wrapper that sets the tree-comparison scope (MIK-L35) around the body, which wires selection, the expressions slot and the knowledge panel for every centre from the workspace's leaf-wide read. [3]
- Planning marks only from the same comparison, and the knowledge panel only from a tree read. [4]
- Cards for a tree comparison, the landed file view for a dataset review, and the invariants one selection reads. [5]
- Identical guarantee text shown once as wording unchanged, with compact revision labels; on a tree comparison a changed guarantee text, even at one revision, is the word-diffed block first, and a one-sided guarantee carries its R06 label (MIK-L35). [6]
- The centre details print the independent facts; on a tree comparison the guarantee fact names one revision whose texts differ `same_revision_text_changed` (MIK-L35, review R1 F2). [7]
- The member centre's family line: the review's label, or a followed marker's unknown membership with the review's reading beside it (MIK-L34). [8]
- The label component and the moved review label. [9]
- `FamilyMemberContext` owns the behavior described above. [10]
- On a tree comparison the family centre's member list follows the tree's order (MIK-L33). [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It renders records of one repository
namespace from a payload the server composed, and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
