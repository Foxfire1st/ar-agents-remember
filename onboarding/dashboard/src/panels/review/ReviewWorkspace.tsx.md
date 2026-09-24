# dashboard/src/panels/review/ReviewWorkspace.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewWorkspace.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The family-centered review workspace: scope header, family tree, the unified central reading path, and —
through the centre — the complete source change explorer. The module states its own ownership in its
header comment: **the three things the accepted layout treats as one composition** are which family or
member is selected, the reader's display preferences (diff layout, full-file disclosure, and which listed
path is expanded) and the narrow-screen route from the tree to the selected review. The payload's own
panes stay in `ReviewSurface.tsx`, which mounts this workspace **inside the read cycle it already owns**:
one read, one question, one outcome region, one page control.

**Why the preferences live here rather than in the components below.** `ICR-R24@v3` requires the reader's
full-file disclosure and current selection to survive a diff-layout switch and a change of selection.
State owned by the tree, by the centre or by the explorer would be reset by exactly the interaction the
requirement is about, so it is lifted to the one component whose lifetime spans them. The preferences are
display facts only: they change no request and no stored value.

**Why the state is exported and owned one level higher still (fix round 5, V10).** A page request changes
the read's question, so the payload is `null` while it is in flight and this whole subtree — including
`ReviewPanes`, which returns `null` for a null payload — unmounts and mounts again. State owned here would
therefore be destroyed and re-initialised by every page read, which is what the round-4 verification
measured: the selection fell back to `none`, the filter to `""`, the diff layout to `split`, full-file to
`true`, and the centre's own continuation control became single-use because its selection was gone by the
time the page arrived. `useWorkspaceState()` is therefore exported, the surface calls it **once above the
pane switch**, and this file receives the value as a prop.

**Verification stamp.** `lastVerifiedCommitHash` names the leaf's base commit
`5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`; this workspace and the layout it belongs to exist only in the
leaf's **uncommitted working tree**, so the stamp means "leaf base commit plus this leaf's working-tree
delta" and does not claim that the commit holds this content. Governed closeout owns the real stamp.

## Code Commentary

### Logic

**The header band is two components, because the roster-walk line is about the page and the rest is about
the question.** `WorkspaceHeader` mounts `ScopeHeader` and then `RosterWalkNotice`. `ScopeHeader` prints,
in order: the title, the task context and subject line (`whole task (no subject selected)` when neither
selector is present), the record line (`record: the leaf's recorded comparison` or `the live candidate`,
plus `source inventory: <state>`, its `(partial)` marker and `changed paths listed: <listed_total>`), the
comparison line (reference, policy version, and both exact endpoints with `not recorded` for an absent
one) or the sentence that no knowledge comparison was made and the inventory below is the review
population, and finally the family line — either `${state}: ${families_returned} of ${families_total}
recorded family context(s) composed.` or the statement that this body carries no family context at all.
That last sentence is load-bearing: a body with no family context is **not** a measured zero.

**`RosterWalkNotice` names which family revision's walk the displayed page is a position in.** It reads the
payload through `carriedPage(payload)`, returns `null` unless the page's collection is `family_members`,
and otherwise prints the page's own `scope` (or `the page published no scope` when the scope is empty)
and whether it was `continued from the cursor this walk published` or `the walk's first page`. It exists
so a reader never has to guess which family a continuation cursor belongs to.

**`FamilyNotComposed` renders the three absent-ish states apart, and says which one it is.** It always
renders the `review-family-tree` section, carrying `data-family-state={context?.state ?? "absent"}`, and
the `review-family-context` paragraph carries `data-context-state` the same way. For an `undefined`
context it prints the body's own sentence — no family context was read into this body, nothing here is
shown as a family population, this is not a measured zero and not an unavailable read, and the complete
source explorer below is unaffected — plus the recorded limitations when the context does carry any.
`composed(context)` is the one gate: the interactive `FamilyTree` is mounted only for `recorded` or
`partial`, and `FamilyColumn` mounts `FamilyNotComposed` otherwise.

**`SelectionColumn` is the narrow-screen route and the centre column it leads to, in one unit.**
`jump` is a real `<button data-testid="review-jump-to-selection">` rather than a styled anchor because
there is no URL to change; its click calls `center.current?.focus()`. Its stylesheet rule hides it above
`60.01rem`, where the centre is already beside the tree: on a narrow screen the reader scrolls a long tree
and then needs one control that reaches the selected review. `CenterColumn` renders
`<div ref={center} tabIndex={-1} data-testid="review-center-column">`, which is what makes the focus
target real, and it holds `FamilyReviewCenter`, then `DisplayControls`, then the `review-display-state`
line (`display: <layout> diff · full file | changed regions only · expanded: <path> | no entry expanded`).
`CenterColumn` now also carries `onRosterNext`, so the centre's own continuation control reaches the
workspace's one roster handler.

**`useWorkspaceState()` is the workspace's whole local state, and it is exported for one reason.** It
holds the selection (`FamilySelection | null`, starting `null`), the filter (`""`), the diff layout
(`"split"`), the full-file disclosure (`true`) and `openPath` (`null`), plus two refs: `opener`, the
control that opened the current expansion, and `center`, the column the narrow-screen route focuses.
`openFromCenter(path)` stores `document.activeElement` before opening; `closePath(null)` restores focus to
that opener, so closing an expansion returns the reader to where they were rather than to the top of the
document. `WorkspaceState` is the exported interface the surface types its prop with.

**`rosterWalk(onPageSelect)` is the one handler the tree's control and the centre's control share.** Both
are the same `RosterNext` component over the same value, so a factory that ignores the family and side it
is handed and sends only `{ of: "family_members", continuation }` is what makes it impossible for them to
ask different questions: a roster cursor names the one walk it continues, so the family and the side are
the page's own scope rather than the request's. `ReviewWorkspace` builds it once as
`const walkRoster = rosterWalk(onPageSelect)` and threads it into `FamilyColumn` and `SelectionColumn`
alike. `onPageSelect` is the **surface's** page control — a family roster continuation is a page request
like any other and goes through the read cycle the surface already owns rather than a second reader.

**`DisplayControls` is mounted twice on purpose.** The same two values are reachable from the centre column
as well as from the explorer's own bar, because a reader looking at a diff should not have to scroll to the
explorer to change how it is drawn. Both copies write the one pair of values this workspace owns; both
publish machine-readable state (`data-testid`, `data-diff-layout`, `data-full-file`, `aria-pressed`).

### Conventions

Styles come from `../../../styled-system/css` as module-level constants (`workspace`, `fullWidth`, `shell`,
`title`, `muted`, `mono`, `jump`), matching the cockpit panels' idiom. Imports are split by kind: React
hooks from `react`; the payload types (`ReviewPayload`, `ReviewFamilyContext`, `ReviewFamilySideName`,
`ReviewSelectorKind`) as type-only imports from `../../data/review`; `carriedPage` as the module's one
value import from that entry; `ReviewPageRequest` as a type-only import from `./ReviewReadCycle`;
`FamilyReviewCenter`, `FamilyTree`/`FamilySelection` and the type-only `DiffLayout` from their own modules.
Every sub-component is a plain function taking the values it renders; props are threaded rather than
re-derived, so two mount points of the same control cannot drift. Test ids are the contract
(`review-workspace`, `review-scope-header`, `review-scope-task`, `review-scope-record`,
`review-scope-comparison`, `review-scope-families`, `review-roster-walk`, `review-family-tree`,
`review-family-context`, `review-family-limitation`, `review-jump-to-selection`, `review-center-column`,
`review-display-state`, `review-center-display-controls`, `review-center-diff-layout`,
`review-center-full-file`), and the workspace root publishes `data-diff-layout` and `data-full-file` so a
case can read the live preferences off the element. No `useEffect` and no fetch appear in this file.

### Invariants And Boundaries

- **This file owns three things and nothing else.** Selection, the reader's display preferences and the
  narrow-screen route. The payload's panes, the read, the question's identity, the outcome region and the
  page control all belong to `ReviewSurface.tsx`; `onPageSelect` is the surface's one page control, passed
  down rather than re-created.
- **The display preferences are display facts.** `layout`, `fullFile` and `openPath` change no request and
  no stored value; they exist so that a diff-layout switch or a selection change cannot collapse an
  expansion or reset the reader's disclosure.
- **State whose lifetime must span the pane switch is owned above it.** `useWorkspaceState` is exported
  and the surface calls it once, above `ReviewPanes`; anything owned below would be destroyed by every
  page read (fix round 5, V10).
- **The narrow-screen route is a button, not an anchor.** There is no URL to change; it moves focus to the
  centre column, which the centre renders as a real focus target (`tabIndex={-1}`).
- **The tree's control and the centre's control are one handler.** Both receive `walkRoster`; only the
  continuation travels, because the family and side are the page's own scope.
- **A body with no family context is neither a measured zero nor an unavailable read.** `FamilyNotComposed`
  states that fact, `composed()` gates the interactive tree, and the source explorer below is unaffected.
- **The scope header prints identities, not conclusions.** Task, record, comparison reference, policy
  version, tree ids and the measured listed-path count are printed because they are what a reader quotes to
  reproduce the read; nothing here summarises what the panes conclude, because they conclude nothing.
- **Boundary.** This module renders the tree (`FamilyTree.tsx`), the centre
  (`FamilyReviewCenter.tsx`) and the explorer (`SourceExplorer.tsx`); the sentences those owners print,
  the roving-focus traversal and the inventory's own population statement are theirs, not this file's.
  The `DiffLayout` type is taken from the explorer rather than declared here.

### Todos

None recorded. The workspace adds no request of its own, no control that writes, and no second reader: the
one page control stays the surface's, the tree keeps its own keyboard traversal, and the centre keeps its
own statements. Any further layout work belongs to the owners named above rather than to this file.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no entries).
The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own statement of what it owns,
the two-column grid and its narrow reflow, the scope header and its five lines, the roster-walk notice, the
three absent-ish family states, the columns and their gates, the exported workspace state and its focus
memory, the one roster handler, the two mount points of the display controls, and the surface that calls
the hook once above the pane switch. Every anchor in a row below occurs on a line inside the range that row
cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it owns — which family or member is selected, the reader's display preferences (diff layout, full-file disclosure, which listed path is expanded) and the narrow-screen route from the tree to the selected review — with the payload's own panes left to `ReviewSurface`, which mounts this workspace inside the read cycle it already owns.** | "WHAT THIS OWNS"; "ICR-R24@v3"; `ReviewSurface` | dashboard/src/panels/review/ReviewWorkspace.tsx:1-18 |
| Why the preferences are lifted to this component rather than owned below it: the interaction the requirement is about is exactly what would reset them. | "lifted to the one component whose lifetime spans" | dashboard/src/panels/review/ReviewWorkspace.tsx:9-13 |
| The two-column grid, and the one-column reflow that is the narrow layout the route exists for. | `workspace`; "@media (max-width: 60rem)" | dashboard/src/panels/review/ReviewWorkspace.tsx:35-41 |
| The imports that fix the boundary: one value from the data layer and the layout type taken from the explorer. | `carriedPage`; `DiffLayout` | dashboard/src/panels/review/ReviewWorkspace.tsx:20-33 |
| The narrow-screen route's own style: hidden above `60.01rem`, where the centre already sits beside the tree. | `jump`; "@media (min-width: 60.01rem)" | dashboard/src/panels/review/ReviewWorkspace.tsx:70-84 |
| The route itself: a real button because there is no URL to change, moving focus into the centre column. | "review-jump-to-selection"; "center.current?.focus()" | dashboard/src/panels/review/ReviewWorkspace.tsx:258-265 |
| `ScopeHeader`: the task context, the subject or `whole task (no subject selected)`, and the test ids of the three context lines. | `ScopeHeader`; "review-scope-header"; "review-scope-task"; "whole task (no subject selected)" | dashboard/src/panels/review/ReviewWorkspace.tsx:90-117 |
| The header's record line: which record the panes below are read from, the inventory's state and partial flag, and the measured count of listed changed paths. | "review-scope-record"; "inventory.listed_total"; "inventory.partial" | dashboard/src/panels/review/ReviewWorkspace.tsx:118-122 |
| The comparison line with the policy and both exact endpoints, and the sentence a body with no comparison gets instead. | "review-scope-comparison"; "no knowledge comparison was made" | dashboard/src/panels/review/ReviewWorkspace.tsx:123-134 |
| The family line: the composed counts, or the fact that this body carries no family context and no family reading may be made from it. | "review-scope-families"; `families_returned`; "that is not a measured zero" | dashboard/src/panels/review/ReviewWorkspace.tsx:135-139 |
| **`RosterWalkNotice`: which family revision's walk this response is a page of, from the page's own scope, or `null` when the page is not a `family_members` walk.** | `RosterWalkNotice`; `family_members`; `review-roster-walk`; `continued_from` | dashboard/src/panels/review/ReviewWorkspace.tsx:144-160 |
| **`FamilyNotComposed`, which renders the body's own no-family-context state and the recorded limitations, carrying the state on two data attributes.** | `FamilyNotComposed`; `review-family-tree`; `data-family-state`; `review-family-limitation` | dashboard/src/panels/review/ReviewWorkspace.tsx:162-189 |
| A body with no family context at all is neither a measured zero nor an unavailable read, and the complete source explorer below is unaffected by it. | "not a measured zero and not an unavailable read" | dashboard/src/panels/review/ReviewWorkspace.tsx:178-181 |
| The tree column's gate: the interactive tree only when the body composed one. | `composed`; `FamilyColumn`; `FamilyNotComposed` | dashboard/src/panels/review/ReviewWorkspace.tsx:191-223; dashboard/src/panels/review/ReviewWorkspace.tsx:165-165|
| `SelectionColumn`: the narrow-screen route and the centre column it leads to, in one component, forwarding the member selection as a `FamilySelection`. | `SelectionColumn`; `CenterColumn`; `onOpenMember` | dashboard/src/panels/review/ReviewWorkspace.tsx:225-284; dashboard/src/panels/review/ReviewWorkspace.tsx:288-288; dashboard/src/panels/review/ReviewWorkspace.tsx:311-311|
| The centre column: a real focus target holding the centre component and the workspace's roster handler. | `CenterColumn`; `review-center-column`; `onRosterNext` | dashboard/src/panels/review/ReviewWorkspace.tsx:286-349 |
| The display-state line: the layout, the full-file disclosure, and the expanded path or the fact that no entry is expanded. | "review-display-state"; "no entry expanded" | dashboard/src/panels/review/ReviewWorkspace.tsx:336-346 |
| **Why the state is exported and owned by the surface: a page request nulls the payload, so this subtree unmounts, and the round-4 verification measured every value falling back and the centre's control becoming single-use.** | "IT IS EXPORTED"; "ICR-L24 fix round 5, V10"; "single-use" | dashboard/src/panels/review/ReviewWorkspace.tsx:351-361 |
| The exported state's shape: the selection, the filter, the three display preferences and the focus memory. | `WorkspaceState` | dashboard/src/panels/review/ReviewWorkspace.tsx:362-375 |
| The one hook that creates it, with the defaults the round-4 measurement saw reset (`split`, full file on, nothing expanded). | `useWorkspaceState`; `useState<DiffLayout>("split")`; `useState(true)` | dashboard/src/panels/review/ReviewWorkspace.tsx:377-382 |
| The focus memory: the control that opened an expansion is remembered, and closing restores focus rather than sending the reader to the top of the document. | `openFromCenter`; `document.activeElement`; `closePath`; `opener.current?.focus()` | dashboard/src/panels/review/ReviewWorkspace.tsx:383-394 |
| The header band: the scope header plus the roster-walk notice. | `WorkspaceHeader`; `RosterWalkNotice` | dashboard/src/panels/review/ReviewWorkspace.tsx:411-444; dashboard/src/panels/review/ReviewWorkspace.tsx:147-147|
| **One roster-walk handler for the whole workspace: the family and the side are the page's own scope, so only the continuation travels — the single `{ of: "family_members", continuation }` page request.** | `rosterWalk`; "of: \"family_members\"" | dashboard/src/panels/review/ReviewWorkspace.tsx:446-455 |
| The component's whole input: the payload, the three task identifiers, the optional selector and record, the surface's one page control, and the surface-owned state. | `ReviewWorkspace`; `onPageSelect`; "state: WorkspaceState" | dashboard/src/panels/review/ReviewWorkspace.tsx:457-480 |
| The one place the handler is built, and the state it destructures rather than re-deriving. | "walkRoster = rosterWalk(onPageSelect)" | dashboard/src/panels/review/ReviewWorkspace.tsx:481-495 |
| The workspace root, publishing the two display preferences as data attributes a case can read. | "review-workspace"; "data-diff-layout={layout}"; "data-full-file" | dashboard/src/panels/review/ReviewWorkspace.tsx:497-503 |
| The composition itself: header, family column, and the selection column carrying the centre's continuation handler. | `WorkspaceHeader`; `FamilyColumn`; `SelectionColumn` | dashboard/src/panels/review/ReviewWorkspace.tsx:504-534; dashboard/src/panels/review/ReviewWorkspace.tsx:413-413; dashboard/src/panels/review/ReviewWorkspace.tsx:197-197; dashboard/src/panels/review/ReviewWorkspace.tsx:229-229|
| The centre's own copy of the two display controls, so a reader looking at a diff need not scroll to the explorer to change how it is drawn. | `DisplayControls`; `review-center-display-controls`; `review-center-diff-layout`; `review-center-full-file` | dashboard/src/panels/review/ReviewWorkspace.tsx:539-575 |
| The explorer's exported layout type, which this workspace takes rather than declaring its own. | `DiffLayout` | dashboard/src/panels/review/SourceExplorer.tsx:29-29 |
| The tree the family column mounts when this body composed one. | "export function FamilyTree(" | dashboard/src/panels/review/FamilyTree.tsx:681-703 |
| The centre component the workspace mounts. | "export function FamilyReviewCenter(" | dashboard/src/panels/review/FamilyReviewCenter.tsx:800-800 |
| The explorer the centre mounts at the payload's own inventory, receiving the caller-owned preferences and the workspace-owned open path. | `SourceExplorer`; `open={openPath}`; `onOpen={onOpenPath}` | dashboard/src/panels/review/FamilyReviewCenter.tsx:861-872 |
| The page request a roster continuation builds is the read cycle's own type, so it is a page request like any other. | `ReviewPageRequest` | dashboard/src/panels/review/ReviewReadCycle.ts:62-66 |
| The one page reading this file delegates to the data layer: the payload's page, with both spellings of "no page" collapsed into one value. | `carriedPage` | dashboard/src/data/review.ts:641-643 |
| **The surface calls the hook once, above the pane switch — the fix round's own wiring.** | `useWorkspaceState` | dashboard/src/panels/review/ReviewSurface.tsx:837-841 |
| The pane switch's own declaration of why the state may not live below it: this function returns `null` while a page read is in flight. | "workspace: ReturnType<typeof useWorkspaceState>" | dashboard/src/panels/review/ReviewSurface.tsx:733-736 |
| The mount: the workspace receives the surface's one page control and the surface-owned state. | "onPageSelect={onSelect}"; "state={workspace}" | dashboard/src/panels/review/ReviewSurface.tsx:742-752 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The workspace renders one repository namespace's
records, and carries no identity that ranges beyond it; the repository id it displays is the one the
payload's own candidate published.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the family-centered review workspace. It records the three things the accepted layout treats as one composition — which family or member is selected, the reader's display preferences (diff layout, full-file disclosure, which listed path is expanded) and the narrow-screen route from the tree to the selected review — the two-component header band (`ScopeHeader` plus `RosterWalkNotice`), `FamilyNotComposed`'s rule that a body with no family context is neither a measured zero nor an unavailable read, `composed()` as the one gate on the interactive tree, the `jump`/`SelectionColumn` narrow-screen control that is hidden above `60.01rem` and moves focus to the centre, `CenterColumn` as the real focus target that now also carries `onRosterNext`, the exported `useWorkspaceState()` that the surface calls **once above the pane switch** (fix round 5, V10, because a page read unmounts this subtree), `rosterWalk`/`walkRoster` as the single `{ of: "family_members", continuation }` page request shared by the tree's and the centre's identical control, and `DisplayControls` mounted twice over the one pair of values. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
