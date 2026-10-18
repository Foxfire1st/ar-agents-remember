# dashboard/src/panels/review/FamilyTree.tsx

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Compact catalogue navigation for recorded families and invariants. It consumes an outline, catalogue identities, retained walk/view state and optional comparison-bound leaf-wide source facts; it does not render the guarantee/member statement reading area. Row badges are delegated outline facts, not an independent semantic or runtime judgment.

## Code Commentary

`FamilyTreeProps` accepts `treeRead` and `reviewComparison` alongside selection, query, catalogue and walked context. `admittedGroups` suppresses loading/failed catalogues and passes the supplied facts to `outlineGroups`. A missing tree read preserves that helper's default behavior; an explicit unavailable/mismatched facts read is not measured zero. `codeChangesCount` requires an admitted outline and facts, deduplicating unchanged invariant selector IDs whose delivered implementation is established.

`useTreeRows` combines saved order/view with catalogue admission. Changed view keeps actual changes and selected member rows; family context additionally retains walked/kept families. Search then matches row identifiers/titles, not statement prose or summaries; search can hide a nonmatching retained selection. Unavailable outlines resolve to All with the view switch disabled. The no-recorded-meaning-change sentence is emitted only for an available outline in Changed with no group carrying a real change.

`OutlineNode` renders the title with ellipsis and whole-title tooltip, primary badge, eligible meaning badge and kept tag. Its accessible name includes title and badges; an aggregate `N changed` family badge is explicitly marked unchanged for primary traversal. Full steps, guarantees and member statements stay in the reading area. The exported exact-revision roster helpers still serve that area; they are not sidebar disclosures.

`FamilyTree` derives traversal from the shown order/view/row badges. Arrow keys wrap focus within tree nodes; traversal ownership remains the shared hook. Late source facts add a polite count notice and pass through `CodeFactsScrollAnchor`, which restores captured same-comparison list/ancestor scroll positions on count changes without choosing or focusing another subject. This is the source mechanism, not a measured visual or browser execution result.

## Preserved earlier explanation

The quotation below is historical, not the current contract or active evidence. Current source corrections above supersede contradictory claims; the prior account is retained for custody.

>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The compact tree consumes the catalogue outline and retained walk/view state, not family guarantee/member statement blocks. One primary change-kind badge preserves existing intent/code/membership precedence and real-change traversal facts; the separately permitted recorded-effect sequence adds no grouping weight, count or stop. Open rows stay one flex line with title ellipsis, the whole-title tooltip and kept-family tag where applicable. Changed/All preference, title/summary filtering, retained selections/walked families and arrow/j/k handling remain owned by the existing tree hooks. Its accessible name includes title, the change badge and eligible recorded labels; full steps/reasons live in the reading area.
>
> ## Code Commentary
>
> ### Outline navigation, not semantic roster content
>
> Recorded meaning labels are an additional compact badge only for added, removed or changed record rows with steps. rowMeaningBadge uses the row’s own outline answer; nodeBadges adds the label sequence to the accessible name without changing the primary change fact or traversal stop. More than three steps abbreviate first/ellipsis/last; complete steps stay in the reading area. none carries no badge. The navigation remains one line and contains no guarantee/statement block or per-row disclosure.
>
> - The compact tree consumes the catalogue outline and retained walk/view state, not family guarantee/member statement blocks. One primary change-kind badge preserves existing intent/code/membership precedence and real-change traversal facts; the separately permitted recorded-effect sequence adds no grouping weight, count or stop. Open rows stay one flex line with title ellipsis, the whole-title tooltip and kept-family tag where applicable. Changed/All preference, title/summary filtering, retained selections/walked families and arrow/j/k handling remain owned by the existing tree hooks. Its accessible name includes title, the change badge and eligible recorded labels; full steps/reasons live in the reading area. Recorded meaning labels are an additional compact badge only for added, removed or changed record rows with steps. rowMeaningBadge uses the row’s own outline answer; nodeBadges adds the label sequence to the accessible name without changing the primary change fact or traversal stop. More than three steps abbreviate first/ellipsis/last; complete steps stay in the reading area. none carries no badge. The navigation remains one line and contains no guarantee/statement block or per-row disclosure. (historical reference 49)
>
> <details>
> <summary>Historical prior account (not the current contract)</summary>
>
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> Present recorded families and invariants as compact one-line navigation rows from the comparison's
> catalogue outline. Full authored guarantees, statements, membership facts and roster continuation belong
> to the selected subject's reading area, not this sidebar. Walked families retain their explicit kept
> context; Changed/All controls visibility without making partial semantic rosters the navigation inventory.
>
> - Rows come from the catalogue outline (`outlineGroups`); without an admitted outline the catalogue entries are listed without badges.
> ## Code Commentary
>
> ### Recorded reviewer judgments
>
> Recorded meaning labels are an additional compact badge only for added, removed or changed record rows with steps. rowMeaningBadge uses the row’s own outline answer; nodeBadges adds the label sequence to the accessible name without changing the primary change fact or traversal stop. More than three steps abbreviate first/ellipsis/last; complete steps stay in the reading area. none carries no badge. The navigation remains one line and contains no guarantee/statement block or per-row disclosure.
>
> - Recorded meaning labels are an additional compact badge only for added, removed or changed record rows with steps. (historical reference 48)
>
> ### The component
>
> `FamilyTreeProps` carries context, selection, query/onQuery, optional walked context, catalogue
> entries/loading/problem, outline, subject, onSubjectSelect and traversalEnabled. It owns neither subject
> selection nor query. Loading/problem catalogue state admits no rows; an admitted outline drives compact
> rows, while an unavailable outline falls back to catalogue identities without invented change badges.
>
> `useTreeRows` resolves order and Changed/All preference. `TreeFilter`, `TriageControls`, the no-recorded-
> meaning-change sentence when appropriate, and `TreeRows` compose the sidebar. `treeRowsKey` binds traversal
> status to shown identity/badge rows. A query filters row identifiers/titles, not full statement prose.
>
> ### A family and its members
>
> `OutlineNode` renders a button with one title, `OutlineChangeBadge`, an eligible recorded-effect badge, and optional kept tag. It supplies
> subject kind/id, family, revision, occurrence and primary-change attributes, `aria-current`, title+badge
> accessible name and a kept-context description. An aggregate `N changed` family badge is marked unchanged
> for traversal: its changed member, not an unchanged family record, is the real-change stop.
>
> `KeptTag` displays "kept" with a tooltip and screen-reader description naming the subject last read.
> Changed view retains selected rows and walked families; All exposes unchanged outline identities too.
>
> Shared `memberRows`, `RosterLine`, `RosterNext` and `emptyRosterSentence` remain exported for the reading
> area. Their exact-revision union, side completeness and cursor-based continuation still govern semantic
> roster rendering there; `FamilyTree` itself no longer renders those details or continuation controls.
>
> ### Labels on a tree comparison
>
> Outline titles and badges are navigation facts, not a substitute for before/after text equality.
> Guarantee word diffs, revision labels and full member statements remain reading-area responsibilities.
> No sidebar disclosure is a second semantic review surface.
>
> ### Change facts, order and traversal
>
> `useTreeOrder` chooses authored/triage order; `useTreeView` chooses Changed/All. Without an admitted
> outline, All is used and the view switch is unavailable. Traversal is enabled only on an available
> outline and visits shown real changes, excluding unknown/unchanged and aggregate-only family badges.
> Order, view and shown rows key its status; no partial-roster continuation is a navigation stop.
>
> ### The scope line
>
> The surrounding `ReviewNavigation` owns changed-family/invariant and lane counts. The tree filter owns
> query and view controls, catalogue/loading/walk/traversal status, and explicit no-match/no-change states.
> It does not promise that Changed view displays every unchanged sibling's full text.
>
> ### Keyboard
>
> `treeArrow` moves focus with the up and down arrow keys among the tree nodes of the family list and wraps at the ends. `aria-current` marks the selected node.
>
> ### Conventions
>
> - Shared exported roster helpers retain reading-area use; compact navigation uses `OutlineNode`, not the former `FamilyNode`/`MemberNode` semantic tree.
> - Styles are `css` objects hoisted to module constants; `cx` adds the current-selection class.
> - Compact navigation emits `data-testid`, `data-tree-node`, `data-family`, `data-revision`, `data-subject-kind`, `data-subject-id`, `data-occurrence` and `data-change-primary` on row buttons, `data-family-kept` on groups, and `data-tree-order`/`data-tree-view` on the list. `data-side`, `data-continuation` and `data-family-label` belong to the retained exported `RosterNext` control in the reading area, not sidebar continuation.
> - Hooks bind the root, reader view/order preferences, traversal and accessible kept-description identity.
>
> ### Invariants And Boundaries
>
> - A guarantee is never summarized from members.
> - Changed/All is explicit: unchanged identities remain accessible in All, not forcibly expanded in Changed.
> - Walked/selected context survives navigation filtering with its kept provenance rather than being mistaken for new membership.
> - Full semantic facts and selected-subject limitations belong in the reading area, not duplicated sidebar details.
> - A partial page never justifies a claim about the whole snapshot: the roster lines state returned, total and remaining counts, and missing content is named.
> - A roster continuation comes only from the cursor the family side's own page published.
>
> - `OutlineNode` draws one row button (`data-tree-node` of `family` or `member`) with the title, an `OutlineChangeBadge`, the eligible recorded-effect badge and, for kept families, the `KeptTag`; the aggregate `N changed` family badge is marked `unchanged` for traversal so it points at the member, not the unchanged family record. `treeArrow` moves focus with the arrow keys within the list.
> - `useTreeRows` resolves `useTreeOrder` and the persisted `useTreeView` preference. With an admitted outline it honors Changed or All; Changed is the initial preference, not forced on every admission. Loading retains that preference, while an unavailable outline resolves to All with the switch disabled. `shownGroup` keeps selected rows and walked families visible and filters titles/summaries; `noChange` is stated only for an available outline in Changed with no real change.
> - Traversal runs over the shown outline through `useChangeTraversal`, keyed by `treeRowsKey` (order, view and row badges), so the status is dropped when the shown rows change.
> ## Evidence
>
> - What the caller passes for the walked tree: its entries, the kept families with the subject each was last read for, a notice and the selected subject's state. (historical reference 16)
>
> - Member rows are the union of both sides by exact revision, with the wording comparison for a revision on both sides. (historical reference 28)
>
> - The roster line states returned, total and remaining counts beside the loaded membership rows. (historical reference 35)
> - The continuation control: one per side with an incomplete page and a published cursor, named with its family. (historical reference 36)
> - Arrow keys move focus among the tree nodes. (historical reference 37)
>
> - The traversal the tree binds, with the rows it shows. (historical reference 38)
>
>
> - Tree section with filter, triage bar and row list (historical reference 41)
> - View and order resolution with the no-change sentence (historical reference 42)
> - One-line row button with badge and kept tag (historical reference 43)
> - Kept tag naming the subject the family was last read for (historical reference 44)
> - Selection matching for subjects and family selections (historical reference 45)
> - View filtering that keeps selection and walked rows (historical reference 46)
> - Traversal keyed to the shown rows (historical reference 47)
>
> </details>

## Evidence

### Docs References

No domain documentation is configured for this repository; the current account is grounded in its actual source.

### Repo-Internal References

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
- Case-insensitive query matches row identifiers and titles; view selection first retains real changes, selected rows and walked family context. A nonmatching query can still filter those retained rows. [46]
- Traversal keyed to the shown rows [47]
- Recorded meaning labels are an additional compact badge only for added, removed or changed record rows with steps. [48]
- Compact catalogue navigation delegates outline grouping and badges, filters row identifiers and titles, preserves selected/walked context within the selected view, and renders one-line title/badge/kept buttons rather than semantic statement disclosures. Recorded meaning labels are supplementary, eligible only for changed record rows; aggregate-only family badges are not primary traversal changes. [49]
- Optional leaf-wide source facts enter outline grouping only through the supplied tree read and comparison. The exact count is distinct unchanged outline invariant identities whose delivered implementation fact is established; unavailable or mismatched facts stay unknown rather than zero. [50]
- Late delivered code facts enrich existing rows with a polite count notice. The same-comparison count-change wrapper snapshots list/ancestor scroll positions before mutation and restores them after update; it does not select or focus a new row. [51]

### Cross-Repo References

No separate cross-repository implementation boundary is claimed.
