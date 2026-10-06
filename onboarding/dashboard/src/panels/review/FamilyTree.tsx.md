# dashboard/src/panels/review/FamilyTree.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Present recorded families as a navigable hierarchy: each family with its independently authored joint guarantee and the full statements of its members, unchanged siblings included.

- The families drawn are the walked tree's when the caller passes one (`walked`), else the families of the context it was given. A family of the walked tree that is not in the selected subject's context is drawn with a "kept" tag (requirement MIK-R39).
- On a tree comparison (MIK-R33) the tree also shows what kind of recorded change brings each family and member occurrence into review, lists the changes first without hiding unchanged siblings, and lets the reader move between changes with `j`/`k`.

## Code Commentary

### The component

`FamilyTree` takes the selected subject's `context`, the `selection` to mark, `onSelect`, `onRosterNext`, the search `query` with `onQuery`, and three optional props: `embedded`, `tree` (a tree comparison; default `false`) and `walked` (a `WalkedTree`). It owns neither the selection nor the query.

It renders, in this order:

1. `FamilyFilter`: the search field (`Escape` clears it) and the scope line from `filterScope`.
2. `WalkNotes`: the walk's notice as a polite status (`review-family-walk-notice`) and the selected subject's state (`review-family-subject-state`), each only when the walked tree carries one.
3. `FamilyContextDetails`: the state, detail, counts and limitations of `context`. It describes the selected subject's context only, never a kept family.
4. `TriageControls` (the sticky triage bar), only when the families carry change facts.
5. `FamilyList` inside `TreeComparisonScope`, or, when no family is shown, the sentence of `noneShown`.

`treeParts` chooses the families and the kept map: the walked tree's `entries` and `kept` when `walked` is given, else `context.entries` and an empty map. `filtered` applies the search: a family is shown when the query is empty or `familyMatches` finds the query in the family's identifier, label, guarantees, candidate guarantees, or its members' revision identifiers, labels and statements. A matching family keeps all its member rows.

### A family and its members

`FamilyList` orders the shown families with `orderFamilies` and draws one `FamilyNode` each, handing it the kept label of that family when the kept map has one.

`FamilyNode` draws:

- the family button (`data-tree-node="family"`) with the family's label and `GuaranteeChangeBadge`; it selects `{ familyId }`;
- for a kept family, the tag "kept · last read for …" (`review-family-kept`) directly under the button. `keptMarks` also sets `data-family-kept="true"` on the family's list item and makes the tag the button's `aria-describedby`, so the tag is both visible and the row's accessible description. A family that is not kept gets none of the three;
- `FamilyBreakdown`, then `FamilyGuarantees`;
- a details block ("N member revisions · roster details") with the label's side, the candidate heads the context declined to choose between, side states, recorded revisions and one `RosterLine` per side;
- `MemberRoster`: the member rows in `orderMemberRows` order, or the sentence of `emptyRosterSentence` when the page carried none;
- `RosterNext`: one continuation button per side whose roster page is incomplete and published a cursor. The button names its family (`data-family-label`) and carries the cursor (`data-continuation`); it calls `onRosterNext` with the family, the side and that cursor.

`memberRows` unions the before and after rows by exact invariant revision. For a revision listed on both sides it records whether the two carried texts are the same, differ, or cannot be compared because a side's content is not on the page (`sidesWording`).

`MemberNode` draws one member row as a button (`data-tree-node="member"`) that selects `{ familyId, memberRevisionId }`. It shows the statement (`MemberSubject`; "statement not carried on this page" when the page did not carry it), the sides note, the side tag, and then one of two things: the change badge (`MemberChangeBadge`) when the row has change facts, or `MemberTargetNote` (a followed intent marker's unknown membership) when it has none. A member recorded under other family revisions gets a "Shared member" disclosure.

### Labels on a tree comparison

On a tree comparison one revision can carry different text on its two sides, so labels compare text, not revision identity alone:

- `guaranteesOf` shows one guarantee revision once only when its two texts are the same (`sameGuaranteeText`); otherwise it shows both texts, noted "same revision, text differs" when the revision is the same. When the family carries change facts the single block is labelled "Joint guarantee", because the family row's badge already states the guarantee's change kind; without change facts it is "Joint guarantee · unchanged".
- For a revision listed on both sides, `memberSideTag` reads "· unchanged revision" only when the carried texts are the same, "· same revision · text differs" when they differ, and "· same revision" when a side is unknown. When the change badge already notes the text difference (`textNoted`), the side tag leaves it out. A revision listed on one side reads "· before only" or "· after only".
- A dataset review (`tree` false) keeps "· unchanged revision" for one revision on both sides.

### Change facts, order and traversal

When the drawn families carry change facts (`hasChangeFacts`):

- families and member rows are listed in the order of the reader's preference (`useTreeOrder`): triage order or authored order. Without change facts the list is always in authored order;
- each member button carries `data-family`, `data-occurrence` (the roster's `member_id`, so the two revision rows of a revised member are one stop) and `data-change-primary` (`memberChangeAttributes`); the family button carries `data-occurrence="family:<id>"` and its guarantee's change kind (`familyChangeAttributes`); the family's list item carries `data-members-unreturned` while `familyTriage` reports unreturned members;
- `useChangeTraversal(root, triaged, rowsShown(shown, order))` gives the triage bar its `move` and `status`. `rowsShown` names what the tree shows: the order, and each shown family with its number of member rows. The traversal drops its status when that string changes.

A member node's accessible name is its subject only (the statement and the side tag, `aria-labelledby`), and its description is its facts (`aria-describedby`): the change badge's description when the row has change facts, else the marker note when a followed marker targets the row (`useMemberNodeIds`).

### The scope line

`filterScope` counts the families of the selected subject's context and the kept families apart:

- no query, no kept family: "N families · M member revisions shown · full sibling context";
- no query, K kept: "(N−K) families · K kept · M member revisions shown · full sibling context";
- with a query: "Filter “q”: shown/total families · shown/total member revisions. Matching families retain all siblings.", with " ((N−K) of this subject · K kept)" after the family counts when K is not zero.

A filter hides kept families and others alike; clearing it shows them again.

### Keyboard

`treeArrow` moves focus with the up and down arrow keys among the tree nodes of the family list and wraps at the ends. `aria-current` marks the selected node.

### Conventions

- Exports: the types `FamilySelection` and `WalkedTree`; the helpers `memberRows`, `emptyRosterSentence` and `familyMatches`; the components `RosterLine`, `RosterNext` and `FamilyTree`. The review center mounts the same `RosterLine`, `RosterNext` and `emptyRosterSentence`.
- Styles are `css` objects hoisted to module constants; `cx` adds the current-selection class.
- Machine-readable facts are data attributes: `data-testid`, `data-family`, `data-family-state`, `data-family-kept`, `data-members-unreturned`, `data-family-label`, `data-side`, `data-side-state`, `data-sides`, `data-member`, `data-revision`, `data-tree-node`, `data-tree-order`, `data-occurrence`, `data-change-primary`, `data-continuation`, `data-roster-complete`, `data-guarantee-side`, `data-guarantee-revision` and `data-context-state`.
- The file declares no `useState` and no `useEffect`. It uses `useRef` for the tree's root and `useId` for the ids of labels and descriptions.
- The file is 974 lines.

### Invariants And Boundaries

- A guarantee is never summarized from members.
- Neither order hides an unchanged sibling.
- A kept family is drawn whole, with its tag; the scope line never counts it as a family of the selected subject.
- "Family context details" and the tree's `data-family-state` describe the selected subject's context only.
- A partial page never justifies a claim about the whole snapshot: the roster lines state returned, total and remaining counts, and missing content is named.
- A roster continuation comes only from the cursor the family side's own page published.

## Evidence

- What the caller passes for the walked tree: its entries, the kept families with the subject each was last read for, a notice and the selected subject's state. [16]
- The component: the filter, the walk's notes, the selected subject's context details, the triage bar when there are change facts, and the family list. [17]
- The families drawn are the walked tree's when there is one, else the context's own. [18]
- A kept family's tag: a data attribute on the item, the button's accessible description, and the visible text. [19]
- The family node: the button with its guarantee badge, the kept tag, the breakdown, the guarantees, the roster details, the member roster and the continuation. [20]
- The scope line counts the families of the selected subject and the kept ones apart, with and without a query. [21]
- The list orders the shown families and hands each node its kept label. [22]
- What the tree shows, for the traversal status: the order and each shown family with its member-row count. [23]
- The walk's notice as a status and the selected subject's state. [24]
- The context details describe the context passed in: state, detail, counts and limitations. [25]
- The search field and its scope line. [26]
- What a query is matched against. [27]
- Member rows are the union of both sides by exact revision, with the wording comparison for a revision on both sides. [28]
- One guarantee revision is shown once only when its texts are the same on a tree comparison. [29]
- The member row's side tag. [30]
- The member row: its subject, sides note, side tag, and the change badge or the marker note. [31]
- The member node's name is its subject and its description its facts. [32]
- The traversal's attributes on a member node. [33]
- The family node's own stop. [34]
- The roster line states returned, total and remaining counts beside the loaded membership rows. [35]
- The continuation control: one per side with an incomplete page and a published cursor, named with its family. [36]
- Arrow keys move focus among the tree nodes. [37]

- The traversal the tree binds, with the rows it shows. [38]

- The family order the tree applies: in triage order by weight and then by position in the list given; in authored order the list as given. [39]

- The mounted cases of the kept tag, the scope line and the context details. [40]
