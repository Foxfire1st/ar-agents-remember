# dashboard/src/panels/review/ReviewWorkspace.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewWorkspace.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
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

**`NarrowJump` is the narrow-screen route to the review, and it is composed ABOVE the family tree.**
`jump` is a real `<button data-testid="review-jump-to-selection">` rather than a styled anchor because
there is no URL to change; its click calls `center.current?.focus()`. Its stylesheet rule hides it above
`60.01rem`, where the centre is already beside the tree: on a narrow screen the reader scrolls a long tree
and then needs one control that reaches the selected review. **Its placement is the whole point
(260921-ICR-L25, register B3, the accepted design's finding P2-3):** the accepted page puts the
affordance "near the top" at `y≈307` so a narrow reader reaches the review **without first scrolling
the tree** — the same finding records the rail at 2,298 px pushing the review to y=2,821 px. It was
previously rendered immediately before the centre column, i.e. **below** the tree, where it sat at
`y=1183` in a 900 px viewport: visible only after the scroll it exists to avoid. It is now one
`NarrowJump` component mounted once, between the header and `FamilyColumn`, so the tree keeps exactly
what it shows and only the control's composition changed. `CenterColumn` renders
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
| The narrow-screen route's own style: hidden above `60.01rem`, where the centre already sits beside the tree. | `jump`; "@media (min-width: 60.01rem)" | dashboard/src/panels/review/ReviewWorkspace.tsx:79-95 |
| **The narrow-screen route itself, now extracted into one `NarrowJump` component: a real button because there is no URL to change, moving focus into the centre column.** | `NarrowJump`; "review-jump-to-selection"; "center.current?.focus()" | dashboard/src/panels/review/ReviewWorkspace.tsx:96-112 |
| `ScopeHeader`: the task context, the subject or `whole task (no subject selected)`, and the test ids of the three context lines. | `ScopeHeader`; "review-scope-header"; "review-scope-task"; "whole task (no subject selected)" | dashboard/src/panels/review/ReviewWorkspace.tsx:113-165 |
| The header's record line: which record the panes below are read from, the inventory's state and partial flag, and the measured count of listed changed paths. | "review-scope-record"; "inventory.listed_total"; "inventory.partial" | dashboard/src/panels/review/ReviewWorkspace.tsx:141-141; dashboard/src/panels/review/ReviewWorkspace.tsx:144-144 |
| The comparison line with the policy and both exact endpoints, and the sentence a body with no comparison gets instead. | "review-scope-comparison"; "no knowledge comparison was made" | dashboard/src/panels/review/ReviewWorkspace.tsx:147-154; dashboard/src/panels/review/ReviewWorkspace.tsx:153-154 |
| The family line: the composed counts, or the fact that this body carries no family context and no family reading may be made from it. | "review-scope-families"; `families_returned`; "that is not a measured zero" | dashboard/src/panels/review/ReviewWorkspace.tsx:158-158; dashboard/src/panels/review/ReviewWorkspace.tsx:160-161 |
| **`RosterWalkNotice`: which family revision's walk this response is a page of, from the page's own scope, or `null` when the page is not a `family_members` walk.** | `RosterWalkNotice`; `family_members`; `review-roster-walk`; `continued_from` | dashboard/src/panels/review/ReviewWorkspace.tsx:96-177; dashboard/src/panels/review/ReviewWorkspace.tsx:167-177; dashboard/src/panels/review/ReviewWorkspace.tsx:170-177; dashboard/src/panels/review/ReviewWorkspace.tsx:172-177; dashboard/src/panels/review/ReviewWorkspace.tsx:177-209; dashboard/src/panels/review/ReviewWorkspace.tsx:177-229; dashboard/src/panels/review/ReviewWorkspace.tsx:177-267; dashboard/src/panels/review/ReviewWorkspace.tsx:177-273 |
| **`FamilyNotComposed`, which renders the body's own no-family-context state and the recorded limitations, carrying the state on two data attributes.** | `FamilyNotComposed`; `review-family-tree`; `data-family-state`; `review-family-limitation` | dashboard/src/panels/review/ReviewWorkspace.tsx:162-189 |
| A body with no family context at all is neither a measured zero nor an unavailable read, and the complete source explorer below is unaffected by it. | "not a measured zero and not an unavailable read" | dashboard/src/panels/review/ReviewWorkspace.tsx:202-202 |
| The tree column's gate: the interactive tree only when the body composed one. | `composed`; `FamilyColumn`; `FamilyNotComposed` | dashboard/src/panels/review/ReviewWorkspace.tsx:220-251; dashboard/src/panels/review/ReviewWorkspace.tsx:216-218 |
| The centre column: a real focus target holding the centre component and the workspace's roster handler. | `CenterColumn`; `review-center-column`; `onRosterNext` | dashboard/src/panels/review/ReviewWorkspace.tsx:303-390 |
| The display-state line: the layout, the full-file disclosure, and the expanded path or the fact that no entry is expanded. | "review-display-state"; "no entry expanded" | dashboard/src/panels/review/ReviewWorkspace.tsx:351-361 |
| **Why the state is exported and owned by the surface: a page request nulls the payload, so this subtree unmounts, and the round-4 verification measured every value falling back and the centre's control becoming single-use.** | "IT IS EXPORTED"; "ICR-L24 fix round 5, V10"; "single-use" | dashboard/src/panels/review/ReviewWorkspace.tsx:366-376 |
| The exported state's shape: the selection, the filter, the three display preferences and the focus memory. | `WorkspaceState` | dashboard/src/panels/review/ReviewWorkspace.tsx:377-390 |
| The one hook that creates it, with the defaults the round-4 measurement saw reset (`split`, full file on, nothing expanded). | `useWorkspaceState`; `useState<DiffLayout>("split")`; `useState(true)` | dashboard/src/panels/review/ReviewWorkspace.tsx:392-424 |
| The focus memory: the control that opened an expansion is remembered, and closing restores focus rather than sending the reader to the top of the document. | `openFromCenter`; `document.activeElement`; `closePath`; `opener.current?.focus()` | dashboard/src/panels/review/ReviewWorkspace.tsx:402-409 |
| The header band: the scope header plus the roster-walk notice. | `WorkspaceHeader`; `RosterWalkNotice` | dashboard/src/panels/review/ReviewWorkspace.tsx:170-464; dashboard/src/panels/review/ReviewWorkspace.tsx:170-456 |
| **One roster-walk handler for the whole workspace: the family and the side are the page's own scope, so only the continuation travels — the single `{ of: "family_members", continuation }` page request.** | `rosterWalk`; "of: \"family_members\"" | dashboard/src/panels/review/ReviewWorkspace.tsx:465-470 |
| The component's whole input: the payload, the three task identifiers, the optional selector and record, the surface's one page control, and the surface-owned state. | `ReviewWorkspace`; `onPageSelect`; "state: WorkspaceState" | dashboard/src/panels/review/ReviewWorkspace.tsx:472-495 |
| The one place the handler is built, and the state it destructures rather than re-deriving. | "walkRoster = rosterWalk(onPageSelect)" | dashboard/src/panels/review/ReviewWorkspace.tsx:496-510 |
| The workspace root, publishing the two display preferences as data attributes a case can read. | "review-workspace"; "data-diff-layout={layout}"; "data-full-file" | dashboard/src/panels/review/ReviewWorkspace.tsx:512-518 |
| **The composition itself: header, the narrow jump route ABOVE the tree, then the tree column, then the selection column carrying the centre's continuation handler.** | `WorkspaceHeader`; `NarrowJump`; `FamilyColumn`; `SelectionColumn` | dashboard/src/panels/review/ReviewWorkspace.tsx:519-554; dashboard/src/panels/review/ReviewWorkspace.tsx:428-464; dashboard/src/panels/review/ReviewWorkspace.tsx:96-112; dashboard/src/panels/review/ReviewWorkspace.tsx:220-251; dashboard/src/panels/review/ReviewWorkspace.tsx:252-302 |
| The centre's own copy of the two display controls, so a reader looking at a diff need not scroll to the explorer to change how it is drawn. | `DisplayControls`; `review-center-display-controls`; `review-center-diff-layout`; `review-center-full-file` | dashboard/src/panels/review/ReviewWorkspace.tsx:559-592 |
| The explorer's exported layout type, which this workspace takes rather than declaring its own. | `DiffLayout` | dashboard/src/panels/review/SourceExplorer.tsx:29-29 |
| The tree the family column mounts when this body composed one. | "export function FamilyTree(" | dashboard/src/panels/review/FamilyTree.tsx:695-770 |
| The centre component the workspace mounts. | "export function FamilyReviewCenter(" | dashboard/src/panels/review/FamilyReviewCenter.tsx:818-818 |
| The explorer the centre mounts at the payload's own inventory, receiving the caller-owned preferences and the workspace-owned open path. | `SourceExplorer`; `open={openPath}`; `onOpen={onOpenPath}` | dashboard/src/panels/review/FamilyReviewCenter.tsx:879-890 |
| The page request a roster continuation builds is the read cycle's own type, so it is a page request like any other. | `ReviewPageRequest` | dashboard/src/panels/review/ReviewReadCycle.ts:62-66 |
| The one page reading this file delegates to the data layer: the payload's page, with both spellings of "no page" collapsed into one value. | `carriedPage` | dashboard/src/data/review.ts:641-643 |
| **The surface calls the hook once, above the pane switch — the fix round's own wiring.** | `useWorkspaceState` | dashboard/src/panels/review/ReviewSurface.tsx:58-58; dashboard/src/panels/review/ReviewSurface.tsx:749-749; dashboard/src/panels/review/ReviewSurface.tsx:881-881 |
| The pane switch's own declaration of why the state may not live below it: this function returns `null` while a page read is in flight. | "workspace: ReturnType<typeof useWorkspaceState>" | dashboard/src/panels/review/ReviewSurface.tsx:749-749 |
| The mount: the workspace receives the surface's one page control and the surface-owned state. | "onPageSelect={onSelect}"; "state={workspace}" | dashboard/src/panels/review/ReviewSurface.tsx:764-765 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The workspace renders one repository namespace's
records, and carries no identity that ranges beyond it; the repository id it displays is the one the
payload's own candidate published.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-25T22:19:46+00:00: Generated citation repair: `ScopeHeader`; "review-scope-header"; "review-scope-task"; "whole task (no subject selected)" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:113-165; dashboard/src/panels/review/ReviewWorkspace.tsx:133-133; dashboard/src/panels/review/ReviewWorkspace.tsx:135-135; dashboard/src/panels/review/ReviewWorkspace.tsx:139-139. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "review-scope-record"; "inventory.listed_total"; "inventory.partial" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:141-141; dashboard/src/panels/review/ReviewWorkspace.tsx:144-144; dashboard/src/panels/review/ReviewWorkspace.tsx:144-144. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `families_returned`; "review-scope-families"; "that is not a measured zero" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:161-161; dashboard/src/panels/review/ReviewWorkspace.tsx:158-158; dashboard/src/panels/review/ReviewWorkspace.tsx:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "not a measured zero and not an unavailable read" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `DiffLayout` repointed to dashboard/src/panels/review/SourceExplorer.tsx:29-29. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "workspace: ReturnType<typeof useWorkspaceState>" repointed to dashboard/src/panels/review/ReviewSurface.tsx:749-749. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "onPageSelect={onSelect}"; "state={workspace}" repointed to dashboard/src/panels/review/ReviewSurface.tsx:764-764; dashboard/src/panels/review/ReviewSurface.tsx:765-765. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the narrow-screen route moved above the family tree, and this card's account of it was corrected rather than left describing the old composition.** The control used to be rendered inside `SelectionColumn`, i.e. **below** the tree, where it sat at `y=1183` in a 900 px viewport: reachable only after the scroll it exists to avoid. It is now one `NarrowJump` component (`:96-112`) mounted once between the header and `FamilyColumn` (`:529`), which is the accepted design's finding P2-3 requirement that the affordance sit "near the top" so a narrow reader reaches the review without scrolling the tree first; the tree itself is untouched. The `### Logic` paragraph that described "`SelectionColumn` is the narrow-screen route and the centre column it leads to, in one unit" was rewritten, and the invariant bullet now names the placement as the point. **Citation accounting:** the rows this file's own insertion displaced were re-derived from each construct's own declaration at this tip — `jump` `:70-84` → `:79-95`, the route row → `NarrowJump` `:96-112`, `FamilyColumn` `:191-223` → `:220-251`, `SelectionColumn` `:225-284` → `:252-302`, `CenterColumn` `:286-349` → `:303-390`, the state comment `:351-361` → `:366-376`, `WorkspaceState` `:362-375` → `:377-390`, `useWorkspaceState` `:377-382` → `:392-424`, the focus memory `:383-394` → `:402-409`, the header band `:411-444` → `:428-464`, `rosterWalk` `:446-455` → `:465-470`, the props `:457-480` → `:472-495`, the root `:497-503` → `:512-518`, the composition `:504-534` → `:519-554`, `DisplayControls` `:539-575` → `:559-592` — and the cross-file rows were re-derived too (`FamilyTree` `:681-703` → `:695-770`, `FamilyReviewCenter` `:800` → `:818`, its explorer mount `:861-872` → `:879-890`, `DiffLayout` `:29` → `:31`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the family-centered review workspace. It records the three things the accepted layout treats as one composition — which family or member is selected, the reader's display preferences (diff layout, full-file disclosure, which listed path is expanded) and the narrow-screen route from the tree to the selected review — the two-component header band (`ScopeHeader` plus `RosterWalkNotice`), `FamilyNotComposed`'s rule that a body with no family context is neither a measured zero nor an unavailable read, `composed()` as the one gate on the interactive tree, the `jump`/`SelectionColumn` narrow-screen control that is hidden above `60.01rem` and moves focus to the centre, `CenterColumn` as the real focus target that now also carries `onRosterNext`, the exported `useWorkspaceState()` that the surface calls **once above the pane switch** (fix round 5, V10, because a page read unmounts this subtree), `rosterWalk`/`walkRoster` as the single `{ of: "family_members", continuation }` page request shared by the tree's and the centre's identical control, and `DisplayControls` mounted twice over the one pair of values. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
