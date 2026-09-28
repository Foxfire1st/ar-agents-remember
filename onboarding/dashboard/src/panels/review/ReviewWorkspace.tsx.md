# dashboard/src/panels/review/ReviewWorkspace.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewWorkspace.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:44:14+02:00 |
| lastVerifiedCommitHash | `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6` |
| lastVerifiedCommitDate | 2026-09-28T22:11:57+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Own the family-centered review layout and its transient inspection state: one scope header, one combined rail and the unified intent/source/evidence center. Since `260921-ICR-L48` (`ICR-R24@v3`) the workspace also **stays mounted across subject selection**: while the selected subject has no answer, only its reading area changes, to a status bound to the requested subject.

## Code Commentary

### Logic

Member navigation calls the existing subject reader using the member invariant identity while retaining its family/roster context. The narrow jump focuses the center without the browser default scroll, then scrolls to its start so the selected heading and guarantee remain visible. Layout, full-file disclosure and open path are unchanged by the jump.

useWorkspaceState holds selected family/member, search, diff layout, full-file disclosure, expanded path and focus references above paged reads. Changed regions are the initial display. WorkspaceRail combines recorded catalogue navigation, the loaded guarantee/member subtree and the complete source inventory. sourceAttribution uses only the backend mapped and unmapped partitions; everything else is unknown. The scope header (and its `recordLabelOf`, which distinguishes reconstructed recorded endpoints from frozen historical and live comparisons) moved to `ReviewScopeHeader.tsx` in L48; the workspace mounts it with a `status` derived from `reading`. The center reuses FamilyReviewCenter and ReviewExpressions; desktop rail scrolling is independent.

**The unanswered subject (L48).** `ReviewWorkspace` takes an optional `reading: ReadingStatus | null`. The surface sets it only when the subject on screen has no answer and the task context has a `frame`; `payload` is then that frame, used for the shell only. `ReadingStatus` carries the read cycle's key for the requested question, the requested subject (`kind:id`), its label and, for a failed or refused read, the owner's problem block (`problem`; `null` while pending). `WorkspaceCenter` is the reading-area column — one DOM node (`review-center-column`) for the life of the workspace — and swaps only its content: `ReadingStatusCenter` renders `review-reading-pending` (`aria-busy`, `role="status"`, "Reading <label>…") or `review-reading-problem` ("<label> could not be read" plus the owner block, with `data-problem-key`/`data-problem-subject`), else the answered subject's `FamilyReviewCenter` and roster note. While unanswered, the tree marks only the reader's explicit choice (`state.chosen`) — deriving one from the frame would mark the previous subject's family as the requested subject's context.

**Focus after a selection (L48-R1-F2).** `focusSelection` holds `{ from }`, the element that had focus when the reader selected. `useSelectionFocus` runs on the next payload, clears the request, and moves focus to the selected tree node (or the center) only if focus is still on `from` or has fallen to `body`; focus the reader moved while the subject was pending is kept.

### Conventions

Styles come from `../../../styled-system/css` as module-level constants (`workspace`, `fullWidth`, `shell`,
`title`, `muted`, `mono`, `jump`), matching the cockpit panels' idiom. Imports are split by kind: React
hooks from `react`; the payload types (`ReviewPayload`, `ReviewFamilyContext`, `ReviewFamilySideName`,
`ReviewSelectorKind`) as type-only imports from `../../data/review`; `carriedPage` as the module's one
value import from that entry; `ReviewPageRequest` as a type-only import from `./ReviewReadCycle`;
`FamilyReviewCenter`, `FamilyTree`/`FamilySelection`, `ReviewScopeHeader` and the type-only `DiffLayout` from their own modules.
Every sub-component is a plain function taking the values it renders; props are threaded rather than
re-derived, so two mount points of the same control cannot drift. Test ids are the contract
(`review-workspace`, the `review-scope-*` ids now rendered by `ReviewScopeHeader.tsx`, `review-reading-pending`,
`review-reading-problem`, `review-roster-walk`, `review-family-tree`,
`review-family-context`, `review-family-limitation`, `review-jump-to-selection`, `review-center-column`,
`review-display-state`, `review-center-display-controls`, `review-center-diff-layout`,
`review-center-full-file`), and the workspace root publishes `data-diff-layout` and `data-full-file` so a
case can read the live preferences off the element. No fetch appears in this file; its one `useEffect` is
`useSelectionFocus`.

### Invariants And Boundaries

Semantic selection never filters the full changed-file population. Confirmed no-family, unselected, absent and unreadable context remain different states. Display preferences do not change knowledge or comparison identity.

**R26 isolation under a retained shell (L48).** While `reading` is set, nothing of the frame's subject is rendered as the requested subject's reading: the center shows only the requested subject's status, the scope header replaces its subject-bound lines, and the tree marks only the explicit choice. The rail's tree and source explorer keep the frame's attribution labels while the subject is pending or unavailable (A2 observation A2-O3): those are comparison-level labels of the task's source changes, not the new subject's intent. A selection never unmounts the workspace, its navigation, tree or open disclosures; only a read with no frame at all (the reviewer's first) has no workspace to keep.

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
| `useWorkspaceState` owns the behavior described above. | `useWorkspaceState` | dashboard/src/panels/review/ReviewWorkspace.tsx:147-184 |
| `ReviewWorkspace` owns the behavior described above. | "export function ReviewWorkspace({" | dashboard/src/panels/review/ReviewWorkspace.tsx:196-275 |
| **The unanswered subject's status and its two renderings in the reading area.** | `ReadingStatus`; `ReadingStatusCenter`; `review-reading-pending`; `review-reading-problem` | dashboard/src/panels/review/ReviewWorkspace.tsx:85-127 |
| **The reading-area column: one DOM node, only its content swapped.** | `WorkspaceCenter`; `review-center-column` | dashboard/src/panels/review/ReviewWorkspace.tsx:277-326 |
| **Selection focus lands only if the reader has not moved it.** | `useSelectionFocus`; `focusSelection` | dashboard/src/panels/review/ReviewWorkspace.tsx:473-487; dashboard/src/panels/review/ReviewWorkspace.tsx:129-145 |
| `WorkspaceRail` owns the behavior described above. | `WorkspaceRail` | dashboard/src/panels/review/ReviewWorkspace.tsx:345-415 |
| `recordLabelOf` (moved to the scope header's module by L48) owns the behavior described above. | `recordLabelOf` | dashboard/src/panels/review/ReviewScopeHeader.tsx:108-112 |
| `sourceAttribution` owns the behavior described above. | `sourceAttribution` | dashboard/src/panels/review/ReviewWorkspace.tsx:495-508 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The workspace renders one repository namespace's
records, and carries no identity that ranges beyond it; the repository id it displays is the one the
payload's own candidate published.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T21:55:52+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **re-citation of rows whose earlier range arrived by generated projection.** The memory-quality check reopened the component row because an older *Generated citation repair* bullet in this card names `ReviewWorkspace`, so a range written there was never shown to be reviewed. Each row was re-read against the construct it is about in this candidate, the claim still holds, and its anchor was re-bound from the bare name to the exact declaration text the curator read (`export function ReviewWorkspace({`), which is the check's own remedy (re-cite the location the claim is about). The generated bullets below are left untouched as the dated record of the projection. No stamp advanced.
- 2026-09-28T21:44:14+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — the workspace stays mounted across selection (`ICR-R24@v3`; L48-R1-F1/F2 rulings; `ICR-R26` preserved).** New: `ReadingStatus`, `ReadingStatusCenter` (pending or could-not-be-read, labelled with the requested subject), `WorkspaceCenter` (one reading-area column whose content alone is swapped), and the moved-focus guard in `useSelectionFocus` (`focusSelection` now `{ from }`). `ScopeHeader` and `recordLabelOf` moved to `ReviewScopeHeader.tsx` (L47-R1-F5 file budget). The implementation **extends** the card's layout contract and **supersedes** the implicit expectation that a subject change remounts the workspace. Purpose, Logic, Conventions (including the wrong pre-existing "no `useEffect`" statement) and Invariants updated; the three reopened claims were re-read; rows re-derived, three rows added. No stamp advanced.
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
