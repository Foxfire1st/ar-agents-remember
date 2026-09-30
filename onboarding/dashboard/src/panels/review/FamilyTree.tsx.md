# dashboard/src/panels/review/FamilyTree.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/FamilyTree.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:23:08+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9` |
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Present the recorded family, its independent guarantee and full member statements, including unchanged siblings, as a navigable hierarchy.

## Code Commentary

### Logic

`RosterLine` distinguishes the read owner's cumulative returned/total/remaining item counts from the number of unique loaded membership contexts. A final continuation completes the walk; retained earlier pages may contribute its loaded context. The published cursor remains the only continuation address.

FamilyNode leads with the family control and authored guarantee, exposes member rows directly, and puts candidate identities, side states, history and roster protocol in a details block. memberRows unions carried before/after rows by exact invariant revision. The search keeps full sibling context for matching families and reports the visible filter scope. Arrow-key navigation and aria-current express selection; roster continuation comes only from the selected family side published cursor.

**Labels on a tree comparison compare text bytes (MIK-L35; review R1 F2, ruled 2026-09-30T12:16:39).** The navigator is mounted by the workspace outside the review centre, so it takes a `tree` prop (default `false`; `ReviewWorkspace.FamilyRailContext` passes whether the payload declares `review:trees:<n>`) and wraps `FamilyList` in `TreeComparisonScope`. On a tree comparison one text record's revision can carry different bytes on its two sides (MIK-R21), so:
- `guaranteesOf` shows one guarantee revision once as "Joint guarantee · unchanged" only when its two texts are the same (`sameGuaranteeText`); otherwise it shows both texts, labelled "Joint guarantee · before · same revision, text differs" and "… after · same revision, text differs".
- `memberRows` records, for a revision listed on both sides, whether the two carried texts are the same, differ, or cannot be compared because a side's content is not on the page (`wording`, from `sidesWording` over `rowWording` and `wordingComparison`). `memberSideTag` then reads "· unchanged revision" only when they are the same, "· same revision · text differs" when they differ, and "· same revision" when a side is unknown.
- A dataset review (`tree` false) keeps the landed labels: there one revision id is one immutable text.

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
`data-continuation`, `data-roster-complete` — so the tree's behaviour is inspectable without reading
its text. `FamilySelection` is exported so the workspace and the centre share one selection type, and
the tree takes its selection and its query from the caller rather than owning them.

### Invariants And Boundaries

A guarantee is not summarized from members. On a tree comparison, no rail label calls one revision unchanged unless its carried texts are identical (MIK-L35; the candidate invariant recorded on `IntentWordDiff.tsx.md`). Ambiguous revisions remain candidates and missing content remains named. Partial pages do not justify whole-snapshot absence or complete-member claims. Repeated membership references a canonical invariant revision without creating a duplicate identity.

### Todos

None recorded. The tree's own sentences are the ones the family route needs; a state this vocabulary
cannot yet carry would arrive as a new server fact rather than as a rendering-side default.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The current ownership and boundaries above are grounded in these source declarations.

| Finding | Anchor | Source |
| --- | --- | --- |
| `FamilyNode` owns the behavior described above. | `FamilyNode` | dashboard/src/panels/review/FamilyTree.tsx:500-550 |
| `memberRows` unions both sides by exact revision and, for a revision on both sides, records whether the carried texts are the same, differ or are unknown (MIK-L35). | `memberRows`; `sidesWording`; "existing.wording = sidesWording(existing.member, member);" | dashboard/src/panels/review/FamilyTree.tsx:116-151 |
| The rail's joint guarantee: one revision once only when its texts are the same on a tree comparison; otherwise both texts, noted "same revision, text differs". | "function sameGuaranteeText("; "function guaranteesOf("; "const note = oneRevision ? ' · same revision, text differs' : '';" | dashboard/src/panels/review/FamilyTree.tsx:301-339 |
| The member node's side tag: "unchanged revision" only for the same carried text on a tree comparison. | `memberSideTag`; "memberSideTag(row, tree)" | dashboard/src/panels/review/FamilyTree.tsx:395-401; dashboard/src/panels/review/FamilyTree.tsx:451-451 |
| `familyMatches` owns the behavior described above. | `familyMatches` | dashboard/src/panels/review/FamilyTree.tsx:565-582 |
| `filterScope` owns the behavior described above. | `filterScope` | dashboard/src/panels/review/FamilyTree.tsx:552-563 |
| `FamilyTree` owns the column; its `tree` prop (MIK-L35) sets the tree-comparison scope around the family list. | "export function FamilyTree({"; "<TreeComparisonScope tree={tree}>" | dashboard/src/panels/review/FamilyTree.tsx:624-693 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It renders the family records of one
repository namespace from a payload the server composed, and carries no identity that ranges beyond
it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): body update. Logic and Invariants record review R1 F2 (2026-09-30T12:16:39): the `tree` prop and scope, the rail's joint guarantee and the member tag comparing text bytes on a tree comparison, datasets unchanged. The `memberRows` and `FamilyTree` rows are reworded and re-measured (`FamilyTree` now on a line-exact quote); two rows added. The new joint-guarantee row is anchored on line-exact quotes rather than the bare `guaranteesOf`, which a committed 2026-09-25T22:19:46 generated bullet names; that bullet is left intact. The installed fixer's `familyMatches` and `filterScope` bullets are kept.
- 2026-09-30T11:14:38+00:00: Generated citation repair: `familyMatches` repointed to dashboard/src/panels/review/FamilyTree.tsx:565-582. No content impact: mechanical anchor-range projection bound to citation source snapshot 2597c838ec1e64a918943e8db9f63ef52ddf51fa320d55ca6abc370de5fa8b59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T11:14:38+00:00: Generated citation repair: `filterScope` repointed to dashboard/src/panels/review/FamilyTree.tsx:552-563. No content impact: mechanical anchor-range projection bound to citation source snapshot 2597c838ec1e64a918943e8db9f63ef52ddf51fa320d55ca6abc370de5fa8b59; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T00:59:43+00:00 — Clarified cumulative read items versus loaded exact member contexts and final-walk wording. Guarantee, exact member identity, navigation and user-driven continuation remain unchanged.
- 2026-09-26T19:49:05Z — Reconciled the visible guarantee/member hierarchy and disclosed roster diagnostics.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the row naming the shared components the centre re-mounts was re-anchored, and no claim wording changed.** The one-line import addition at the top of `panels/review/FamilyReviewCenter.tsx` moved that import block `:41-46` → `:42-47`; the anchors (`RosterLine`, `RosterNext`, `emptyRosterSentence`) still resolve inside it and this file's own contract is untouched. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `RosterLine`; `primary_items_remaining`; `members_total` repointed to dashboard/src/panels/review/FamilyTree.tsx:246-273; dashboard/src/panels/review/FamilyTree.tsx:264-264; dashboard/src/panels/review/FamilyTree.tsx:242-242. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `carriedOf`; "recorded membership row(s) it measured" repointed to dashboard/src/panels/review/FamilyTree.tsx:289-291; dashboard/src/panels/review/FamilyTree.tsx:290-290. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `emptyRosterSentence`; "the read measured zero memberships"; "The continuation beside each bounded roster reaches" repointed to dashboard/src/panels/review/FamilyTree.tsx:298-317; dashboard/src/panels/review/FamilyTree.tsx:296-296; dashboard/src/panels/review/FamilyTree.tsx:315-315. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `RosterNext`; "data-continuation"; "continue the" repointed to dashboard/src/panels/review/FamilyTree.tsx:338-369; dashboard/src/panels/review/FamilyTree.tsx:360-360; dashboard/src/panels/review/FamilyTree.tsx:363-363. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `familyLabel`; "entry.display_label ?? entry.family_id" repointed to dashboard/src/panels/review/FamilyTree.tsx:371-373; dashboard/src/panels/review/FamilyTree.tsx:372-372. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `guaranteesOf`; "side: \"both\"" repointed to dashboard/src/panels/review/FamilyTree.tsx:381-405; dashboard/src/panels/review/FamilyTree.tsx:392-392. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `FamilyCandidates`; "recorded head(s) this context declined" repointed to dashboard/src/panels/review/FamilyTree.tsx:438-446; dashboard/src/panels/review/FamilyTree.tsx:442-442. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `memberLabel`; `display_version` repointed to dashboard/src/panels/review/FamilyTree.tsx:453-458; dashboard/src/panels/review/FamilyTree.tsx:454-456. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `memberSidesNote`; "recorded on both snapshots" repointed to dashboard/src/panels/review/FamilyTree.tsx:460-464; dashboard/src/panels/review/FamilyTree.tsx:462-462. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `filterScope`; "the comparison's recorded totals are unchanged" repointed to dashboard/src/panels/review/FamilyTree.tsx:615-626; dashboard/src/panels/review/FamilyTree.tsx:625-625. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `treeArrow` repointed to dashboard/src/panels/review/FamilyTree.tsx:655-667. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2, **correction against the independent verifier** (same uncommitted change set; verifier `verify-l25-round2.md` first line `pass-with-findings`, sha256 `dd34cee2b5bc2068023ba9e7af1f7b037edc995bc6019d9bacbed9f00619870b`; finding F5): **the invariant above gained the precise form of the B1 fix, because the loose form is false as worded.** "Zero `oklch` users remain in the review surface" cannot hold while the dashboard's own tokens are defined in `oklch` (`styles/tokens.css:8-23`) and `getComputedStyle` resolves `var(--token)`: the verifier counted **739** computed-property hits inside the review workspace, **262** even restricted to testid-bearing elements. **What is true, and now what this card says:** the raw amber-wash literal is gone, the wash computes as `oklab(0.82 0.041411 0.154548 / 0.08)` through `var(--amber)`, and hue 215 is absent. **Source-level corroboration added in the same pass:** every `oklch` occurrence in this file is inside the comment block that documents the removal (`:88`, `:94`, `:95`) — the working code carries none. **What did not change:** the helper, the two percentages, the token indirection and the reason the interpolation space matters. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the selection wash is now `oklab` through the token, and this card gained the invariant and the row that state it.** This file carried the **only** raw colour literals in the review surface — `oklch(0.82 0.16 75 / 0.08)` (hover) and `oklch(0.82 0.16 75 / 0.16)` (current) — i.e. `--amber`'s channels copied by hand and mixed by hand, in the one place that did not use AR's own language; every other selection wash in this dashboard already states `color-mix(in oklab, var(--amber) N%, transparent)`. Both are now one `AMBER_WASH(percent)` helper (`:98`), through `var(--amber)`, mixing in `oklab` because an `oklch` mix interpolates the **hue** — which is how the accepted page's own selected row came out `oklch(0.324 0.048 215)`, visibly teal (register B1). Measured on the mounted product after the fix: the selected member row computes `oklab(0.82 0.041411 0.154548 / 0.08)`, and the review surface holds **zero** `oklch` users with a testid. **Scope, stated so the fix is not read as wider than it is:** raw `oklch` literals remain elsewhere in the dashboard (grammar, engine-room, detail-panel styles, `GateResponder`) — pre-existing, outside the review surface, and outside this criterion; they are not touched. **Citation accounting:** the new row cites `:87-121` from the constructs' own declaration. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the family tree column. It records that the file renders three separate levels — the family label, the family revision's own independently authored joint guarantee, and the complete member statements with the unchanged siblings included — and derives nothing across them; that `memberRows()` unions both sides by `invariant_revision_id` so a repeated membership never inflates the tree and the row's member value is the after side's only when that side carried content; that `RosterLine` prints the read owner's two different populations (`counts.primary_items_*` for the family revision's whole recorded selection against `members_total` for its membership rows) with `completionNote` distinguishing a one-page walk's first page from a multi-page walk's final page; that `emptyRosterSentence()` is the one sentence both this column and the centre mount and keeps no-family-revision, the measured zero and the bounded page apart; that `RosterNext` renders only the cursor the page published and is the family collection's only walk control; that selection is a roving-focus group with arrow-key traversal and `aria-current`; and that `filterScope()` states a display filter without restating the comparison's totals. Every row of the reference table was derived against this leaf's candidate, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
