# dashboard/src/panels/review/FamilyTree.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Present recorded families and invariants as compact one-line navigation rows from the comparison's
catalogue outline. Full authored guarantees, statements, membership facts and roster continuation belong
to the selected subject's reading area, not this sidebar. Walked families retain their explicit kept
context; Changed/All controls visibility without making partial semantic rosters the navigation inventory.

- Rows come from the catalogue outline (`outlineGroups`); without an admitted outline the catalogue entries are listed without badges.
## Code Commentary

### The component

`FamilyTreeProps` carries context, selection, query/onQuery, optional walked context, catalogue
entries/loading/problem, outline, subject, onSubjectSelect and traversalEnabled. It owns neither subject
selection nor query. Loading/problem catalogue state admits no rows; an admitted outline drives compact
rows, while an unavailable outline falls back to catalogue identities without invented change badges.

`useTreeRows` resolves order and Changed/All preference. `TreeFilter`, `TriageControls`, the no-recorded-
meaning-change sentence when appropriate, and `TreeRows` compose the sidebar. `treeRowsKey` binds traversal
status to shown identity/badge rows. A query filters row identifiers/titles, not full statement prose.

### A family and its members

`OutlineNode` renders a button with one title, `OutlineChangeBadge`, and optional kept tag. It supplies
subject kind/id, family, revision, occurrence and primary-change attributes, `aria-current`, title+badge
accessible name and a kept-context description. An aggregate `N changed` family badge is marked unchanged
for traversal: its changed member, not an unchanged family record, is the real-change stop.

`KeptTag` displays "kept" with a tooltip and screen-reader description naming the subject last read.
Changed view retains selected rows and walked families; All exposes unchanged outline identities too.

Shared `memberRows`, `RosterLine`, `RosterNext` and `emptyRosterSentence` remain exported for the reading
area. Their exact-revision union, side completeness and cursor-based continuation still govern semantic
roster rendering there; `FamilyTree` itself no longer renders those details or continuation controls.

### Labels on a tree comparison

Outline titles and badges are navigation facts, not a substitute for before/after text equality.
Guarantee word diffs, revision labels and full member statements remain reading-area responsibilities.
No sidebar disclosure is a second semantic review surface.

### Change facts, order and traversal

`useTreeOrder` chooses authored/triage order; `useTreeView` chooses Changed/All. Without an admitted
outline, All is used and the view switch is unavailable. Traversal is enabled only on an available
outline and visits shown real changes, excluding unknown/unchanged and aggregate-only family badges.
Order, view and shown rows key its status; no partial-roster continuation is a navigation stop.

### The scope line

The surrounding `ReviewNavigation` owns changed-family/invariant and lane counts. The tree filter owns
query and view controls, catalogue/loading/walk/traversal status, and explicit no-match/no-change states.
It does not promise that Changed view displays every unchanged sibling's full text.

### Keyboard

`treeArrow` moves focus with the up and down arrow keys among the tree nodes of the family list and wraps at the ends. `aria-current` marks the selected node.

### Conventions

- Shared exported roster helpers retain reading-area use; compact navigation uses `OutlineNode`, not the former `FamilyNode`/`MemberNode` semantic tree.
- Styles are `css` objects hoisted to module constants; `cx` adds the current-selection class.
- Compact navigation emits `data-testid`, `data-tree-node`, `data-family`, `data-revision`, `data-subject-kind`, `data-subject-id`, `data-occurrence` and `data-change-primary` on row buttons, `data-family-kept` on groups, and `data-tree-order`/`data-tree-view` on the list. `data-side`, `data-continuation` and `data-family-label` belong to the retained exported `RosterNext` control in the reading area, not sidebar continuation.
- Hooks bind the root, reader view/order preferences, traversal and accessible kept-description identity.

### Invariants And Boundaries

- A guarantee is never summarized from members.
- Changed/All is explicit: unchanged identities remain accessible in All, not forcibly expanded in Changed.
- Walked/selected context survives navigation filtering with its kept provenance rather than being mistaken for new membership.
- Full semantic facts and selected-subject limitations belong in the reading area, not duplicated sidebar details.
- A partial page never justifies a claim about the whole snapshot: the roster lines state returned, total and remaining counts, and missing content is named.
- A roster continuation comes only from the cursor the family side's own page published.

- `OutlineNode` draws one row button (`data-tree-node` of `family` or `member`) with the title, an `OutlineChangeBadge` and, for kept families, the `KeptTag`; the aggregate `N changed` family badge is marked `unchanged` for traversal so it points at the member, not the unchanged family record. `treeArrow` moves focus with the arrow keys within the list.
- `useTreeRows` resolves `useTreeOrder` and the persisted `useTreeView` preference. With an admitted outline it honors Changed or All; Changed is the initial preference, not forced on every admission. Loading retains that preference, while an unavailable outline resolves to All with the switch disabled. `shownGroup` keeps selected rows and walked families visible and filters titles/summaries; `noChange` is stated only for an available outline in Changed with no real change.
- Traversal runs over the shown outline through `useChangeTraversal`, keyed by `treeRowsKey` (order, view and row badges), so the status is dropped when the shown rows change.
## Evidence

- What the caller passes for the walked tree: its entries, the kept families with the subject each was last read for, a notice and the selected subject's state. [16]

- Member rows are the union of both sides by exact revision, with the wording comparison for a revision on both sides. [28]

- The roster line states returned, total and remaining counts beside the loaded membership rows. [35]
- The continuation control: one per side with an incomplete page and a published cursor, named with its family. [36]
- Arrow keys move focus among the tree nodes. [37]

- The traversal the tree binds, with the rows it shows. [38]


- Tree section with filter, triage bar and row list [41]
- View and order resolution with the no-change sentence [42]
- One-line row button with badge and kept tag [43]
- Kept tag naming the subject the family was last read for [44]
- Selection matching for subjects and family selections [45]
- View filtering that keeps selection and walked rows [46]
- Traversal keyed to the shown rows [47]
