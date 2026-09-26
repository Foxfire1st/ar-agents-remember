# dashboard/src/panels/review/SourceExplorer.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SourceExplorer.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

List the complete measured source-change population independently of family or invariant selection, with every textual or byte-named path retained.

## Code Commentary

### Logic

InventoryRows renders all entries and unrepresentable byte names. Each textual entry carries the backend-derived mapped, unmapped or unknown attribution label. With showContent=false the workspace rail owns navigation while ReviewExpressions opens the actual diff in the center; otherwise SourceContent can expand the row at the listing bound trees. Layout and full-file preferences are caller-owned. Inventory details retain the owner explanation, reproducing command and exact tree IDs.

### Conventions

Styles come from `../../../styled-system/css` as module-level constants (`shell`, `bar`, `sectionLabel`,
`muted`, `rows`, `rowButton`), matching the cockpit panels' idiom. Types come as type-only imports from
`../../data/review` (`ReviewChangedFile`, `ReviewSourceInventory`, `ReviewUnrepresentablePath`), and the
entry renderer comes from `./SourceContent`. Everything else is a plain function: `inventoryEntry`,
`byteNamedEntry`, `DisplayControls` and `InventoryRows` take the values they render and hold no state —
`SourceExplorer` is the only component in the file, and it holds no state either, because `open`,
`layout` and `fullFile` are all caller-owned. `DiffLayout = "split" | "inline"` is exported from here and
imported by the workspace and the centre. Every list item carries a `key` derived from the record's own
identity (`entry.path`, `entry.path_bytes`). Test ids are the contract (`review-source-explorer`,
`review-display-controls`, `review-diff-layout`, `review-full-file`, `review-inventory`,
`review-population-scope`, `review-inventory-entry`, `review-inventory-open`, `review-inventory-byte-path`,
`review-byte-path-not-addressable`, `review-inventory-unclassified`, `review-inventory-command`), and the
machine-readable facts ride data attributes (`data-inventory-state`, `data-status`, `data-path`,
`data-diff-layout`, `data-full-file`, `aria-expanded`, `aria-pressed`). No `useEffect`, no fetch and no
request construction appear in this file: the expansion is a child component's read.

### Invariants And Boundaries

Unavailable inventory is not a measured zero. Partial and unclassified entries remain visible. Byte-named paths remain listed even when the request vocabulary cannot address them for expansion. Semantic selection never narrows this population.

### Todos

None recorded. The byte-form rows stay identification-only until this vocabulary can carry a path as bytes,
and no control in this file writes or re-measures anything: the two display preferences are the reader's,
and the inventory is the server's.

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
| `SourceExplorer` owns the behavior described above. | `SourceExplorer` | dashboard/src/panels/review/SourceExplorer.tsx:224-302 |
| `InventoryRows` owns the behavior described above. | `InventoryRows` | dashboard/src/panels/review/SourceExplorer.tsx:170-222 |
| `inventoryEntry` owns the behavior described above. | `inventoryEntry` | dashboard/src/panels/review/SourceExplorer.tsx:58-116 |
| `byteNamedEntry` owns the behavior described above. | `byteNamedEntry` | dashboard/src/panels/review/SourceExplorer.tsx:118-130 |
| `InventoryDetails` owns the behavior described above. | `InventoryDetails` | dashboard/src/panels/review/SourceExplorer.tsx:312-325 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The explorer lists one repository namespace's
changed paths and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T19:49:05Z — Reconciled rail-only navigation, explicit attribution labels and retained inventory details.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "const expandable"; "const isOpen" repointed to dashboard/src/panels/review/SourceExplorer.tsx:106-106; dashboard/src/panels/review/SourceExplorer.tsx:107-107. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "not openable through this surface" repointed to dashboard/src/panels/review/SourceExplorer.tsx:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "review-population-scope"; "it never removes one from this list" repointed to dashboard/src/panels/review/SourceExplorer.tsx:299-299; dashboard/src/panels/review/SourceExplorer.tsx:301-301. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "owned by the workspace rather than by this component" repointed to dashboard/src/panels/review/SourceExplorer.tsx:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `useWorkspaceState`; `openFromCenter` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:392-424; dashboard/src/panels/review/ReviewWorkspace.tsx:387-387. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T00:15:00+02:00 — 260921-ICR-L25 curator, round 3 (same uncommitted change set, now also carrying `ReviewSurface.tsx` + the new `ReviewSurface.narrow.test.tsx`; round-3 report `report-l25-round3.md` = `cf6fb86e4d20cf5a1baf6bd093e4d9b1ccbf017062503da23edbf40d44e52b86`): **body update — the B7 residual sentences this card carried from round 2 are superseded, because round 3 fixed both halves in the reviewer's own code.** The invariant now carries the whole history of one sentence rather than only its latest state: the round-2 "residual is outside the review surface" claim was **false as worded** (classified against the inner `review-workspace` root), round 3 fixed the reviewer's own overflow and its own scrollport, and the numbers are re-measured — descendants of `review-surface` past the edge **51 → 0**, total **64 → 13** (all 13 in neither review root), panes **565 → 294 px** in a 294 px column, the root's own **311/294 → 294/294**, `userScrollableCount` **0 → 1**, and a wheel over the review moving the surface **0 → 800 px**. **The two sentences that were false are quoted in the corrected text so a later reader can see what changed and why** — a correction that only states the new number would leave the next reader unable to tell whether the old one was wrong or merely stale. **What remains routed and is no longer the reviewer's:** the shell's deliberate `MAIN: overflow: hidden` decision (`cockpit/Cockpit.tsx:323`) and its 13 cockpit-chrome elements, owned by R24. **Citation accounting:** this module's own rows are unchanged — its `rowButton` fix was never the disputed part — and the corrected text cites the reviewer root's own current line. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2, **correction against the independent verifier** (same uncommitted change set; verifier `verify-l25-round2.md` first line `pass-with-findings`, file sha256 `dd34cee2b5bc2068023ba9e7af1f7b037edc995bc6019d9bacbed9f00619870b`; its findings F1/F2, §4): **the B7 sentence this card first carried was FALSE AS WORDED and is corrected in place.** The round-2 claim — `inReviewSurface: 0`, with the 64 residual elements being the cockpit's own chrome "outside the review surface" — classified membership against the **inner** `[data-testid="review-workspace"]` root (`ReviewWorkspace.tsx:515`) rather than the Intent Reviewer's own root `[data-testid="review-surface"]` (`ReviewSurface.tsx:866`, mounted by `Cockpit.tsx:585`). Re-measured by the verifier against both roots at 320 px: **64 total overflowing · 0 descendants of `review-workspace` · 51 descendants of `review-surface` · 13 neither** — so 51 of the 64 are **inside** the reviewer, including `review-refresh`, `diff-pane`, `review-selection`, `review-conditions`, `review-locations`, `review-field-changes`, `review-unassessed`, `review-applicability`, `review-expansion` and `review-source-explorer-pointer` (565 px wide in a 294 px column, `pannableCount 0` of 64, the reviewer root's own `scrollWidth 311 > clientWidth 294`). **F2 makes the vertical half worse:** at 320 px **no element in the document is user-scrollable** — `MAIN` is `overflow-y: hidden` with 5 375–7 620 px of content in a 706 px box, the window is exactly viewport-height, and three wheel trials move nothing, so the review is reachable only by programmatic focus scroll. **What this card still states, because it is measured and true:** this module's own fix is real — the path button is 252 px in a 252 px container with `scrollWidth == clientWidth`, and the page no longer overflows horizontally at 1600 or at 320. **What changed:** B7 is not fully fixed, the residual is inside B7's own criterion and inside the reviewer, and it is **routed to the cockpit/R24 owner as a named residual rather than placed outside the surface.** No verification stamp was advanced. No commit was made.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the path button now wraps instead of being clipped, and this card gained the invariant and the row that record it.** `rowButton` gained `overflowWrap: "anywhere"` and `maxWidth: "100%"`. The discriminating property is that `anywhere`, unlike `break-word`, also lowers the element's **min-content** width — the property that was forcing the grid track to grow — so the column shrinks instead of overflowing. Measured on the mounted product at 320 px: before, one `review-inventory-open` button was 556 px wide inside a 294 px column with its right 262 px cut off by the shell's `overflow-x: hidden` and no pannable ancestor (neither visible nor reachable); after, 252 px in a 252 px container (register B7). **The residual sentence this entry first carried is superseded by the correction above, which is dated and stands on the verifier's own measurement.** **Citation accounting:** the two rows this file's own insertion moved were re-derived from their constructs' declarations (`rowButton` `:70-89`, `inventoryEntry` `:90-148`), and the new row cites `:60-89` for the comment block plus the style it explains. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the complete source change explorer. It records that the module is the comparison's whole changed-path population (the family navigation is an attribution lens and never an exclusion filter), that `layout`, `fullFile` and `open` are owned by the caller so neither a diff-layout switch nor a family/member selection can collapse an expansion, that `inventoryEntry` prints the published path exactly and opens it at the inventory's own two tree ids through `SourceContent`, that `byteNamedEntry` lists a byte-carried path and marks it not addressable with no expansion control, that `InventoryRows` renders the measured entries and the byte-form paths as two lists, that `DisplayControls` carries the two preferences as controls with `data-*`/`aria-*` state, and that `SourceExplorer` renders the inventory's own population sentence and the statement that a selection never removes a change from the list. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
