# dashboard/src/panels/review/ReviewWorkspace.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewWorkspace.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T20:20:54Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Own the family-centered review layout and its transient inspection state: one scope header, one combined rail and the unified intent/source/evidence center.

## Code Commentary

### Logic

Member navigation calls the existing subject reader using the member invariant identity while retaining its family/roster context. The narrow jump focuses the center without the browser default scroll, then scrolls to its start so the selected heading and guarantee remain visible. Layout, full-file disclosure and open path are unchanged by the jump.

useWorkspaceState holds selected family/member, search, diff layout, full-file disclosure, expanded path and focus references above paged reads. Changed regions are the initial display. WorkspaceRail combines recorded catalogue navigation, the loaded guarantee/member subtree and the complete source inventory. sourceAttribution uses only the backend mapped and unmapped partitions; everything else is unknown. recordLabelOf distinguishes reconstructed recorded endpoints from frozen historical and live comparisons. The center reuses FamilyReviewCenter and ReviewExpressions; desktop rail scrolling is independent.

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

Semantic selection never filters the full changed-file population. Confirmed no-family, unselected, absent and unreadable context remain different states. Display preferences do not change knowledge or comparison identity.

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

The current ownership and boundaries above are grounded in these source declarations.

| Finding | Anchor | Source |
| --- | --- | --- |
| `useWorkspaceState` owns the behavior described above. | `useWorkspaceState` | dashboard/src/panels/review/ReviewWorkspace.tsx:159-196 |
| `ReviewWorkspace` owns the behavior described above. | `ReviewWorkspace` | dashboard/src/panels/review/ReviewWorkspace.tsx:208-287 |
| `WorkspaceRail` owns the behavior described above. | `WorkspaceRail` | dashboard/src/panels/review/ReviewWorkspace.tsx:306-376 |
| `recordLabelOf` owns the behavior described above. | `recordLabelOf` | dashboard/src/panels/review/ReviewWorkspace.tsx:378-382 |
| `sourceAttribution` owns the behavior described above. | `sourceAttribution` | dashboard/src/panels/review/ReviewWorkspace.tsx:457-470 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The workspace renders one repository namespace's
records, and carries no identity that ranges beyond it; the repository id it displays is the one the
payload's own candidate published.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T21:11:04+00:00: Generated citation repair: `ReviewWorkspace` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:208-287. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:11:04+00:00: Generated citation repair: `sourceAttribution` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:457-470. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T20:20:54Z — Reconciled authoritative subject reads, exact revision comparison and accessible selection behavior.
- 2026-09-26T19:49:05Z — Reconciled single-rail ownership, source attribution labels, changed-region default and historical reconstruction labeling.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, second move:** the F1 fix round added 30 net lines to `panels/review/FamilyReviewCenter.tsx` (1419 lines, was 1389), so this card's two rows into it were re-derived from each construct's own declaration at the new tip — `FamilyReviewCenter` `:1306-1306` → `:1336-1336`, the explorer mount it resolves `:1375-1386` → `:1405-1416`. No claim wording changed. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the two rows this card carries into `panels/review/FamilyReviewCenter.tsx` were re-anchored, and no claim wording changed.** L36 inserted ~449 lines into that file above the centre root, so `FamilyReviewCenter` moved `:818-818` → `:1306-1306` and the explorer mount it resolves moved `:879-890` → `:1375-1386`. Both new ranges were derived from each construct's own declaration at this tip, not by arithmetic on the old ones. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `ScopeHeader`; "review-scope-header"; "review-scope-task"; "whole task (no subject selected)" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:113-165; dashboard/src/panels/review/ReviewWorkspace.tsx:133-133; dashboard/src/panels/review/ReviewWorkspace.tsx:135-135; dashboard/src/panels/review/ReviewWorkspace.tsx:139-139. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "review-scope-record"; "inventory.listed_total"; "inventory.partial" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:141-141; dashboard/src/panels/review/ReviewWorkspace.tsx:144-144; dashboard/src/panels/review/ReviewWorkspace.tsx:144-144. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `families_returned`; "review-scope-families"; "that is not a measured zero" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:161-161; dashboard/src/panels/review/ReviewWorkspace.tsx:158-158; dashboard/src/panels/review/ReviewWorkspace.tsx:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "not a measured zero and not an unavailable read" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `DiffLayout` repointed to dashboard/src/panels/review/SourceExplorer.tsx:29-29. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "workspace: ReturnType<typeof useWorkspaceState>" repointed to dashboard/src/panels/review/ReviewSurface.tsx:749-749. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "onPageSelect={onSelect}"; "state={workspace}" repointed to dashboard/src/panels/review/ReviewSurface.tsx:764-764; dashboard/src/panels/review/ReviewSurface.tsx:765-765. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the narrow-screen route moved above the family tree, and this card's account of it was corrected rather than left describing the old composition.** The control used to be rendered inside `SelectionColumn`, i.e. **below** the tree, where it sat at `y=1183` in a 900 px viewport: reachable only after the scroll it exists to avoid. It is now one `NarrowJump` component (`:96-112`) mounted once between the header and `FamilyColumn` (`:529`), which is the accepted design's finding P2-3 requirement that the affordance sit "near the top" so a narrow reader reaches the review without scrolling the tree first; the tree itself is untouched. The `### Logic` paragraph that described "`SelectionColumn` is the narrow-screen route and the centre column it leads to, in one unit" was rewritten, and the invariant bullet now names the placement as the point. **Citation accounting:** the rows this file's own insertion displaced were re-derived from each construct's own declaration at this tip — `jump` `:70-84` → `:79-95`, the route row → `NarrowJump` `:96-112`, `FamilyColumn` `:191-223` → `:220-251`, `SelectionColumn` `:225-284` → `:252-302`, `CenterColumn` `:286-349` → `:303-390`, the state comment `:351-361` → `:366-376`, `WorkspaceState` `:362-375` → `:377-390`, `useWorkspaceState` `:377-382` → `:392-424`, the focus memory `:383-394` → `:402-409`, the header band `:411-444` → `:428-464`, `rosterWalk` `:446-455` → `:465-470`, the props `:457-480` → `:472-495`, the root `:497-503` → `:512-518`, the composition `:504-534` → `:519-554`, `DisplayControls` `:539-575` → `:559-592` — and the cross-file rows were re-derived too (`FamilyTree` `:681-703` → `:695-770`, `FamilyReviewCenter` `:800` → `:818`, its explorer mount `:861-872` → `:879-890`, `DiffLayout` `:29` → `:31`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the family-centered review workspace. It records the three things the accepted layout treats as one composition — which family or member is selected, the reader's display preferences (diff layout, full-file disclosure, which listed path is expanded) and the narrow-screen route from the tree to the selected review — the two-component header band (`ScopeHeader` plus `RosterWalkNotice`), `FamilyNotComposed`'s rule that a body with no family context is neither a measured zero nor an unavailable read, `composed()` as the one gate on the interactive tree, the `jump`/`SelectionColumn` narrow-screen control that is hidden above `60.01rem` and moves focus to the centre, `CenterColumn` as the real focus target that now also carries `onRosterNext`, the exported `useWorkspaceState()` that the surface calls **once above the pane switch** (fix round 5, V10, because a page read unmounts this subtree), `rosterWalk`/`walkRoster` as the single `{ of: "family_members", continuation }` page request shared by the tree's and the centre's identical control, and `DisplayControls` mounted twice over the one pair of values. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
