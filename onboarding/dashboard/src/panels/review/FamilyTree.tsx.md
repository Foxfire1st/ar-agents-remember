# dashboard/src/panels/review/FamilyTree.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Present the recorded family, its independent guarantee and full member statements, including unchanged siblings, as a navigable hierarchy. On a tree comparison (MIK-R33) it also shows what kind of recorded change brings each family and member occurrence into review, lists the changes first without hiding unchanged siblings, and lets the reviewer move between changes with `j`/`k`.

## Code Commentary

### Logic

`RosterLine` distinguishes the read owner's cumulative returned/total/remaining item counts from the number of unique loaded membership contexts. A final continuation completes the walk; retained earlier pages may contribute its loaded context. The published cursor remains the only continuation address.

FamilyNode leads with the family control and authored guarantee, exposes member rows directly, and puts candidate identities, side states, history and roster protocol in a details block. memberRows unions carried before/after rows by exact invariant revision. The search keeps full sibling context for matching families and reports the visible filter scope. Arrow-key navigation and aria-current express selection; roster continuation comes only from the selected family side published cursor.

**Labels on a tree comparison compare text bytes (MIK-L35; review R1 F2, ruled 2026-09-30T12:16:39).** The navigator is mounted by the workspace outside the review centre, so it takes a `tree` prop (default `false`; `ReviewWorkspace.FamilyRailContext` passes whether the payload declares `review:trees:<n>`) and wraps `FamilyList` in `TreeComparisonScope`. On a tree comparison one text record's revision can carry different bytes on its two sides (MIK-R21), so:
- `guaranteesOf` shows one guarantee revision once as "Joint guarantee · unchanged" only when its two texts are the same (`sameGuaranteeText`); otherwise it shows both texts, labelled "Joint guarantee · before · same revision, text differs" and "… after · same revision, text differs".
- `memberRows` records, for a revision listed on both sides, whether the two carried texts are the same, differ, or cannot be compared because a side's content is not on the page (`wording`, from `sidesWording` over `rowWording` and `wordingComparison`). `memberSideTag` then reads "· unchanged revision" only when they are the same, "· same revision · text differs" when they differ, and "· same revision" when a side is unknown.
- A dataset review (`tree` false) keeps the landed labels: there one revision id is one immutable text.

**A followed intent marker's unknown membership on its member row (MIK-L34; ruling 2026-09-30T16:19:34 Q3).**
`MemberNode` renders `MarkerTargetState.MemberTargetNote` inside the member button, after the side tag. It draws
"Attribution unknown" and the reason only when the workspace's marker scope holds a followed target whose family and
member revision are this row's and whose membership is `membership_unknown`; for every other row, and outside a
tree comparison's workspace, it draws nothing, so a reader who follows such a marker lands on a row that says so,
never on a plain row that reads like a confirmed membership. **Since MIK-L33** the note is drawn only on a row without
change facts (a dataset review), and it is the row's accessible description, not part of its name (review R3-1); on
a tree comparison's row the change badge states the same target once, as below.

**Change kinds, triage order and `j`/`k` on a tree comparison (MIK-L33, MIK-R33 adopting ICR-R32@v1).** When the
context carries change facts (`changeTriage.hasChangeFacts`: only a tree comparison's server-composed `change_kinds`),
the tree:
- orders families (`orderFamilies`) and each roster's member rows (`orderMemberRows`) by the delivered weights, then
  authored order, under the browser-local `useTreeOrder` preference ("Order: changes first" by default, or pure
  authored order); the rows of one occurrence stay together and no sibling is removed;
- badges the family button with its guarantee fact (`GuaranteeChangeBadge`) and prints the `FamilyBreakdown` under it,
  marking the family `data-members-unreturned` while members are unreturned;
- gives each member button `data-family`, `data-occurrence` (the roster's `member_id`, so a revised member's two
  revision rows are one stop) and `data-change-primary` (`memberChangeAttributes`), the family button
  `data-occurrence="family:<id>"` with its guarantee fact (`familyChangeAttributes`), and each continuation control
  `data-family-label` for the traversal's message;
- mounts `TriageControls` (the sticky triage bar) above the list and binds `j`/`k` through
  `useChangeTraversal(root, triaged)` on the enclosing reviewer zone.

A dataset review (no facts) renders exactly the landed tree: authored order, no badge, breakdown or controls, and
`j`/`k` inert.

**One statement per fact on a member (ruling 2026-09-30T17:47:43; the merge round; review R3-1).** The merge with
MIK-L34 had one conflict, in `MemberNode`, resolved by keeping both elements: after the side tag the button draws the
change badge (`ChangeBadges.MemberChangeBadge`) when the row has facts, else L34's `MemberTargetNote`. With facts the
badge's "same revision; text differs" note replaces the side tag's "· same revision · text differs" (`textNoted`,
`memberSideTag(row, tree, noted)`), and the guarantee block's label is "Joint guarantee" because the family's badge
already says "guarantee unchanged" (`guaranteesOf`'s `unchangedNote`). The node's accessible name is its subject only:
`aria-labelledby` names `MemberSubject`'s statement span and the side-tag span (`useMemberNodeIds`), and
`aria-describedby` names the facts in the ruled order (the badge, the change-kind reason, the membership) or, on a
dataset row opened by a marker, L34's note. The sides note ("recorded on the before snapshot only") is in neither the
name nor the description; the side tag beside it (" · before only") carries the same fact (review R4, pass, an
observation needing no action).

### Conventions

The module is one default-free file of small function components plus two exported pure helpers
(`memberRows`, `familyMatches`) and three exported presentational components reused elsewhere
(`RosterLine`, `RosterNext`, `emptyRosterSentence`) — the centre mounts the same three rather than
declaring a second roster line, a second continuation control or a second empty-roster sentence.
Styling uses the `styled-system/css` `css` helper with inline style objects hoisted to module
constants (`shell`, `sectionLabel`, `searchInput`, `muted`, `statements`, `node`, `current`,
`guaranteeText`, `memberText`, `sideTag`, `familyBlock`), matching the cockpit panels' idiom; the
`cx` helper composes the base node class with the amber current-selection class. Every list item and
every per-side element carries a stable `key` (`entry.family_id`, `row.invariantRevisionId`, the
member revision, the side name, `${side}:${revision_id}`). Sub-components take the entry (or the side
context) and the handlers they need, hold no state at all, and expose machine-readable facts as data
attributes — `data-testid`, `data-side`, `data-side-state`, `data-family`, `data-family-state`,
`data-guarantee-side`, `data-guarantee-revision`, `data-tree-node`, `data-revision`, `data-sides`,
`data-continuation`, `data-roster-complete`, and since MIK-L33 `data-occurrence`, `data-change-primary`,
`data-members-unreturned`, `data-family-label` and the list's `data-tree-order` — so the tree's behaviour is
inspectable without reading its text. The file is 858 lines (MIK-L33's badge, order and traversal pieces live in
`ChangeBadges.tsx`, `changeTriage.ts`, `changeTraversal.ts` and `triageOrderPreference.ts`; this file keeps render
hooks only). `FamilySelection` is exported so the workspace and the centre share one selection type, and
the tree takes its selection and its query from the caller rather than owning them.

### Invariants And Boundaries

A guarantee is not summarized from members. A member row opened from an intent marker whose membership is unknown
carries "Attribution unknown" with its reason (MIK-L34), distinct from any confirmed state: since MIK-L33 in its
accessible description, stated once (on a tree comparison as the tag on the change facts' membership line). On a tree
comparison, triage order never hides an unchanged sibling and a partial family's continuation is a `j` stop that is
never activated (the candidate invariant recorded on `changeTriage.ts.md`), and each fact is stated once per node,
visually and to assistive technology (the candidate invariant recorded on `ChangeBadges.tsx.md`). On a tree comparison, no rail label calls one revision unchanged unless its carried texts are identical (MIK-L35; the candidate invariant recorded on `IntentWordDiff.tsx.md`). Ambiguous revisions remain candidates and missing content remains named. Partial pages do not justify whole-snapshot absence or complete-member claims. Repeated membership references a canonical invariant revision without creating a duplicate identity.

### Todos

- **Resolved by MIK-L33's merge round (rulings 2026-09-30T17:39:21 and 17:47:43; accepted 21:41:02; R3-1 at
  21:55:02).** Built as ruled: `MemberNode` keeps both elements, the change badge when the row has facts and L34's
  note otherwise. On a named family's member the change facts' membership line is the standing line and L34's state
  is an **Attribution unknown** tag on it ("opened from an intent marker"), drawn first when the tag applies; the
  reasons are labelled "change kind unknown" and "membership unknown", and `aria-describedby` orders them change kind
  first, then membership. The name is the subject only (statement and side tag through `aria-labelledby`), so
  assistive technology hears each fact once.

Otherwise none recorded. The tree's own sentences are the ones the family route needs; a state this vocabulary
cannot yet carry would arrive as a new server fact rather than as a rendering-side default.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current ownership and boundaries above are grounded in these source declarations.

- The family node: the family button with its guarantee badge (MIK-L33), the breakdown, the guarantees, the roster details, the ordered member roster and the continuation. [1]
- `memberRows` unions both sides by exact revision and, for a revision on both sides, records whether the carried texts are the same, differ or are unknown (MIK-L35). [2]
- The rail's joint guarantee: one revision once only when its texts are the same on a tree comparison; otherwise both texts, noted "same revision, text differs". [3]
- The member node's side tag: "unchanged revision" only for the same carried text on a tree comparison; with change facts the badge's note states a text difference instead (MIK-L33). [4]
- After its side tag the member button draws the change badge when the row has facts, else a followed marker's unknown-membership note, which is then the row's description (MIK-L34; MIK-L33 merge round and R3-1). [5]
- The note: only on the exact family and member revision of an unknown-membership target. [6]
- `familyMatches` owns the behavior described above. [7]
- `filterScope` owns the behavior described above. [8]
- `FamilyTree` owns the column; its `tree` prop (MIK-L35) sets the tree-comparison scope around the family list. [9]
- Change facts order the tree and drive `j`/`k`; a dataset review keeps the landed tree (MIK-L33). [10]
- Families and member rows in triage or authored order, siblings kept (MIK-L33). [11]
- The traversal's attributes on member and family nodes (MIK-L33). [12]
- The member node's name is its subject and its description its facts (review R3-1). [13]
- The guarantee block does not repeat the badge's "guarantee unchanged" (MIK-L33). [14]
- The badge, the tagged membership line and the description order. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It renders the family records of one
repository namespace from a payload the server composed, and carries no identity that ranges beyond
it.

No meaningful cross-repo references found.
