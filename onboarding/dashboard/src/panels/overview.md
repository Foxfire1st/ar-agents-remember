# dashboard/src/panels/ — Cockpit Panels Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/`                          |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3` |
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview      | `../overview.md`                                 |

## 260921-ICR-L44 Two Family Bodies Re-Captured Under A Receipt, Five Still At Their Earlier Capture

The review cases' captured route bodies are no longer one provenance generation. `familyReview.complete`
and `familyReview.identical` (and `subjectReview.family` / `subjectReview.invariant`) were re-captured
over HTTP from the real review route so their member sources carry `locator`, `resolved_ranges` and
`locator_state`; each re-capture is recorded in a receipt beside the fixtures —
`review/familyReview.capture-provenance.json` (new) and `review/subjectReview.capture-provenance.json`.
`familyReview.truncated`, `.continued`, `.oneSided`, `.walkFinal` and `.emptyRoster` still hold their
capture at `63b47629`, and `familyPaging` its capture at `a5bec6c3`: the current route resolves roster
members from content and claim items too, so it cannot reproduce the first states, and several cases
assert those older states. The receipt's worker-stated `not_recaptured` section and the case headers say
so; their re-capture or retirement is open work that belongs with the change moving those cases to the
current route.

| Finding | Anchor | Source |
| --- | --- | --- |
| The receipt's not-re-captured section. | "not_recaptured" | dashboard/src/panels/review/familyReview.capture-provenance.json:36-52 |
| The case header stating which bodies were re-captured. | "familyReview.capture-provenance.json" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:8-19 |

## Current family-centered review ownership

SubjectReview owns central statements and evidence from the exact server-selected subject. Member selection uses the ordinary invariant read while preserving family context; confirmed no-family and ambiguous revision states retain their own truthful rendering.

ReviewSurface composes the shared catalogue and existing comparison read cycle. ReviewWorkspace owns one family/subject/source rail and the unified center; ReviewExpressions opens actual bound diffs after intent, while familyExpressions owns the existing pure grouping. FamilyTree preserves full statements and unchanged siblings. The complete source inventory remains independent of attribution; diagnostics remain inspectable through disclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| `ReviewWorkspace` owns the behavior described above. | `ReviewWorkspace` | dashboard/src/panels/review/ReviewWorkspace.tsx:208-287 |
| `WorkspaceRail` owns the behavior described above. | `WorkspaceRail` | dashboard/src/panels/review/ReviewWorkspace.tsx:306-376 |

## 260921-ICR-L32 The Change-Set Control Renders The Refusal It Receives

`detail-panel/changeSetBar.tsx`'s `ChangeSetButton` for `mode: "committed"` used to clear its counters on a
rejected read and show nothing else, so a **refused** read and a **pending** one were the same pixels. Since
`260921-ICR-L32` the control renders the refusal's own code and reason (`data-review-code`, the owner's
detail text) beside a `data-review-state` marker, keeps the pending state distinct, and still opens the
change set it names when clicked — the case that pins it drives the click and asserts the rendered reason,
not merely the absence of counters. The transport half of the same change is recorded on the
`dashboard/src/data` route.

## 260921-ICR-L33 A Landed Master's Leaves, And What A Closed Row Still Says

Three of this route's panels changed, and they change one story: **a master whose work has all landed is
readable, bounded, and attributable.**

> **WITHDRAWN by `a9a1a41b`, recorded by the `260921-ICR-L34` curation — the two paragraphs below about
> `LifecycleList.tsx` and `useCollapsedTaskGroups.ts` describe code that is in no tree.** Commit
> **`a9a1a41b`** (*"Revert L33's operations-list change; clear the pre-existing ruff-format red"*) is a
> **direct emergency commit with no curator pass behind it**: it deleted
> `panels/lifecycle-list/landedLeaves.ts` (its sidecar was deleted by this curation and is not listed
> below any more), removed 250 lines from `LifecycleList.tsx` (1189 now), deleted 366 lines from
> `hierarchy.test.tsx` (355 now), and restored `useCollapsedTaskGroups.ts` to its 28-line pre-L33 shape
> with one collapse set and `toggleCollapsed(key)`. `leafRecordsLandedWork`, `childFactsByParent`,
> `enclosureForDoc`, `markAutoCollapsed`, `rowIsCollapsed`, `landedLeafDocs`, `openedKeys`,
> `setCollapsed` and `CollapseState` **exist nowhere in the code tree**. The *third* panel
> (`panels/changeset/`) is not affected by the revert and its paragraphs stand.

**`lifecycle-list/LifecycleList.tsx`** *(withdrawn — see the banner above)* admits a landed leaf — a non-master task document whose status is
`Completed` — as a row under its OPEN master, instead of only ever admitting a leaf whose worktree
physically exists. The supporting rules moved into a new sibling module,
`lifecycle-list/landedLeaves.ts`: `leafRecordsLandedWork`, `childFactsByParent`/`rowChildFacts`,
`enclosureForDoc` (the one join, moved so admission and the row builders cannot disagree),
`markAutoCollapsed`, `rowIsCollapsed` and `landedLeafDocs`. The bounds are two, and both are measured:
a row whose only children are its own landed leaves is closed by default and prints `N landed`
(`Tasks · 57 → 167` on the live projection, with 110 landed rows carried at first paint and 19 masters
held closed); and a row that carries OTHER rows is never closed by that rule, because one orchestration
row owns a 161-row subtree. The list's header count still counts task ENTRIES rather than projected
documents, and now says so in its own tooltip.

**`panels/useCollapsedTaskGroups.ts`** gained the second half of the reader's collapse state —
`operations.tasks.opened.v1`, the keys opened past a row's default, beside the unchanged
`operations.tasks.collapsed.v1` — and its public signature changed from `toggleCollapsed(key)` to
`setCollapsed(key, collapsed)`, because only the caller knows the row's default.

**`panels/changeset/ChangeSetViewer.tsx`** is governed by the `changeset/` child route, so its own record
lives there; what belongs here is the panel-level fact: both of the dashboard's master-net readers pass
`includeLeaves: true`, superseding the `includeLeaves: false` optimisation commit `a1521685` introduced.

| Finding | Anchor | Source |
| --- | --- | --- |
| The header count itself. **Withdrawn in part:** the tooltip this row cited stated *what* the count counts, and the L33 revert removed it with the landed-leaf change — the h2 is again a bare `Tasks · {count}`. | "Tasks · {count}" | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:574-574 |
| The bar's request for the net's per-leaf attribution. | `includeLeaves` | dashboard/src/panels/detail-panel/changeSetBar.tsx:98-98 |

## 260921-ICR-L25 The Change-Set Bar Names An Unrecorded Range, And The Jump Sits Above The Tree

Two panels on this route changed, and each change is the same shape: **a surface stopped describing a
state it was not in.**

**`detail-panel/changeSetBar.tsx` — an unrecorded change-set range is named, not printed as a zero
(register B6).** A `committed` read of a live leaf has no landed commit to read yet. The route used to
answer that state with a `404`, which the browser logs as a console error on the page whose accepted
criterion is **zero** — and the bar probes that view as soon as a leaf document is opened. The route
now answers it in the body (`state: "unrecorded"` plus its own sentence naming the missing endpoint
and the two views that produce it), and the bar renders it as the control's **own** state
(`data-review-state="unrecorded"`, distinct from `known-empty`) while **withholding the `+0 −0`
total**: a zero of nothing is not a measurement. The three genuinely distinct refusals are untouched —
an unknown leaf is still a `404`, a bad or absent `mode` a `400`, an enclosure `scope` its own `404`.

**`review/ReviewWorkspace.tsx` and `review/FamilyReviewCenter.tsx` — the narrow-screen route moved
above the tree, and the empty column names its own plane (register B3).** The accepted design's finding
P2-3 puts the "jump to the selected review" affordance **near the top** precisely because the family
tree's height is why it exists; rendered immediately before the centre column instead, it sat at
`y=1183` in a 900 px viewport — reachable only after the scroll it exists to avoid. It is now one
`NarrowJump` mounted between the header and the tree, and the tree itself is unchanged. The centre's
empty sentence used to read "No family or member is selected", which collided with the **server's** own
"selected" on the same screen (the header's composed-context count, the tree's "this review selected
<revision>", a roster line's "the page is the whole selection"), so a reader comparing them read a
contradiction that was a collision of vocabularies; it now says a family or member has not been
**chosen in this column** yet and states that the header's composition and the tree's revision selection
are not choices made here. **The sentence was not false about its own state** — the measured
`data-selection-kind` is `none`, with no `aria-current` in the tree, until the reader chooses — so this
is a wording fix and the layout of the centre was deliberately not changed. **One caveat the round-2
verifier measured, and round 3 then removed (its F2):** at 320 px the reviewer had supplied no scrollport
of its own, so with `MAIN` at `overflow-y: hidden` its 7 620 px of content were reachable only by
programmatic focus scroll — the narrow reader's route to the review was not one they could scroll. That
is fixed on the reviewer's own side (`ReviewSurface.tsx`'s root is now the scrollport, `userScrollableCount`
0 → 1); the composition requirement and the wording fix are unchanged by it.

**Two further lines of the same accepted design were addressed on this route, and the second one is
only half fixed — stated here as the independent verifier measured it.** `review/FamilyTree.tsx`
carried the review surface's **only** raw colour literals (`oklch(0.82 0.16 75 / 0.08)` and
`… / 0.16` — `--amber`'s channels copied by hand); both are now one `AMBER_WASH(percent)` helper
stating `color-mix(in oklab, var(--amber) N%, transparent)`, because an `oklch` mix interpolates the
**hue** and that is how the accepted page's own row first came out visibly teal (register B1).
**The form of that claim which is true, and the form which is not:** the raw amber-wash literal is
gone, the wash computes as `oklab` through `var(--amber)`, and hue 215 is absent — but "zero `oklch`
users remain in the review surface" is **false as worded**, because `getComputedStyle` resolves
`var(--token)` and this dashboard's tokens are themselves defined in `oklch`
(`styles/tokens.css:8-23`), so token-resolved `oklch` values are everywhere in the surface by design.
A reader scanning computed styles for the word `oklch` will conclude the fix failed unless this is
said. `review/SourceExplorer.tsx`'s path button gained `overflow-wrap: anywhere` and
`max-width: 100%`, which is what lets the column shrink: measured at 320 px, one
`review-inventory-open` button was 556 px wide inside a 294 px column with its right 262 px neither
visible nor reachable, and it now wraps inside its container (register B7).

**B7 needed a second round, and the two readings of its residual are both worth keeping.** Round 2
claimed the residual was *"the cockpit's own status bar, outside the review surface"*; that was
**false as worded** — the count had been classified against the **inner**
`[data-testid="review-workspace"]` root (`ReviewWorkspace.tsx:515`) while the Intent Reviewer's own
root is `[data-testid="review-surface"]` (`ReviewSurface.tsx:906`, mounted by `Cockpit.tsx:585`).
Against the reviewer's own root, **51 of the 64** elements past the right edge at 320 px were **inside**
the reviewer (13 were cockpit chrome), the pane sections were **565 px wide in a 294 px column** with
`pannableCount 0`, and the vertical half was worse: **nothing in the document was user-scrollable**,
because `MAIN` is `overflow-y: hidden` carrying 7 620 px in a 706 px box. **Round 3 fixed both halves in
the reviewer's own code** (`ReviewSurface.tsx`): the panes got `min-width: 0` +
`overflow-wrap: anywhere`, the disclosure track became `minmax(0, 1fr)`, the header row wraps, and the
surface root took `height: 100%` / `minHeight: 0` / `overflowY: auto`. Re-measured: descendants of
`review-surface` past the edge **51 → 0**, total **64 → 13**, panes **565 → 294 px** in a 294 px column,
the root's own **311/294 → 294/294**, `userScrollableCount` **0 → 1**, and a wheel over the review moves
the surface **0 → 800 px**. **The number was not improved by changing the root** — the inner root's
count was 0 in both rounds, which is precisely why F1 was a classification defect. **What remains
routed, and it is the shell's rather than the reviewer's:** `MAIN`'s deliberate `overflow: hidden`
(`cockpit/Cockpit.tsx:323`, *"the viewport does not scroll — its panel scrolls on its own"*, shared by
every view) and the **13** cockpit-chrome elements, owned by R24's cockpit takeover.

## Update History

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): added the route section recording that two family bodies (and two subject bodies) were re-captured under receipts while five family bodies and `familyPaging` keep their earlier captures, and added the new receipt to the file onboarding map.

- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No route impact: `review/SourceContent.test.tsx`'s `expansion` builder only gained the two now-required fields (`admission: "changed"`, `admission_detail`); no panel, case or rendered behavior changed, and labelling attributed unchanged context is L49's. Two rows citing displaced lines were re-pointed (verified at base and candidate). No stamp advanced.
- 2026-09-27T01:16:27+00:00 — Re-resolved only the changed review-source references. The helper-pair citation names both actual definitions, and the central renderer, read cycle and mounted case retain their specific subject. Unrelated normalization and inherited ambiguous anchors were left outside this repair.

- 2026-09-27T00:59:43+00:00 — Updated the review child-route contract for exact bounded continuation, coherent failure retention and truthful loaded scope. No source/knowledge selection authority, route ownership or store is added.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `ReviewWorkspace` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:208-287. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `includeLeaves` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `leafIsLive` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:560-572. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: "onClick={() => onOpen(generation ? { ...target, generation } : target)}" repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:140-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `SourcePane` repointed to dashboard/src/panels/review/ReviewSurface.tsx:299-354. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `refusalBlock` repointed to dashboard/src/panels/review/SourceContent.tsx:112-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `fieldValue` repointed to dashboard/src/panels/review/ReviewSurface.tsx:166-167. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: "function KnowledgePane" repointed to dashboard/src/panels/review/ReviewSurface.tsx:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: "function SourcePane" repointed to dashboard/src/panels/review/ReviewSurface.tsx:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `RosterNext` repointed to dashboard/src/panels/review/FamilyTree.tsx:250-282. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `FamilyReviewCenter` repointed to dashboard/src/panels/review/FamilyReviewCenter.tsx:804-878. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: `SourceExplorer` repointed to dashboard/src/panels/review/SourceExplorer.tsx:224-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:59+00:00: Generated citation repair: "renders the family's changed expression excerpts, deduplicated, over the captured family" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:701-769. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled current route ownership and retained existing source and history boundaries.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `includeLeaves` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:109-109. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `App` repointed to dashboard/src/App.tsx:10-19. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `Cockpit` repointed to dashboard/src/cockpit/Cockpit.tsx:366-390. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `SessionComposer` repointed to dashboard/src/panels/SessionComposer.tsx:57-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "onClick={() => onOpen(generation ? { ...target, generation } : target)}" repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `fieldValue` repointed to dashboard/src/panels/review/ReviewSurface.tsx:182-183. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T00:15:00+02:00 — 260921-ICR-L25 curator, round 3 (uncommitted change set, now also carrying `panels/review/ReviewSurface.tsx` and the new `panels/review/ReviewSurface.narrow.test.tsx`; round-3 report `report-l25-round3.md` = `cf6fb86e4d20cf5a1baf6bd093e4d9b1ccbf017062503da23edbf40d44e52b86`): **route body updated — B7's residual is superseded a second time, and this route now records both readings of it.** Round 2 said the residual was cockpit chrome "outside the review surface"; the round-2 verifier showed that was false as worded (classified against the inner `review-workspace` root, while the reviewer's own root is `review-surface`: 51 of 64 inside); **round 3 then fixed the reviewer's own overflow and its own scrollport**, so the section states the measurement that was wrong, the measurement that replaced it, and the fix that closed it — 51 → 0 inside the reviewer root, 64 → 13 total, panes 565 → 294 px, `userScrollableCount` 0 → 1 — rather than only the final number. **The B3 caveat was corrected too:** its "nothing is user-scrollable at 320 px" note described the pre-round-3 state and now records that round 3 fixed it on the reviewer's side while the composition requirement and the wording fix are unchanged. **Named as routed, and now the shell's rather than the reviewer's:** `MAIN`'s deliberate `overflow: hidden` and the 13 cockpit-chrome elements, owned by R24's cockpit takeover. **What remains the shell's consequence, stated so it is not lost:** any other panel in this shell that renders taller than the viewport without its own scrollport has the same defect — the change-set takeover shares it. **Citation accounting:** the new section's rows cite the reviewer root's own current line (`ReviewSurface.tsx:906`) and the shell's decision line (`cockpit/Cockpit.tsx:323`); no earlier row was weakened to fit. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2, **correction against the independent verifier** (same uncommitted change set; verifier `verify-l25-round2.md` first line `pass-with-findings`, sha256 `dd34cee2b5bc2068023ba9e7af1f7b037edc995bc6019d9bacbed9f00619870b`; findings F1/F2/F5): **two sentences this route's L25 section carried were false as worded and are corrected in place.** (1) "The overflow that remains at that width is the cockpit's own status bar, outside this route" — the count was classified against the **inner** `[data-testid="review-workspace"]` root, but the Intent Reviewer's own root is `[data-testid="review-surface"]`; re-measured against both, **51 of the 64** overflowing elements at 320 px are **inside** the reviewer and 13 are cockpit chrome, `pannableCount 0` of 64 — so the residual is inside B7's own criterion and inside this route, **routed as a named residual rather than placed outside it**. The verifier's F2 adds the vertical half: at 320 px **nothing in the document is user-scrollable** (`MAIN` `overflow-y: hidden`, 5 375–7 620 px of content, window exactly viewport-height). (2) The B1 claim is narrowed to the form that is true — the raw amber-wash literal is gone, the wash computes as `oklab` through `var(--amber)`, hue 215 absent — because "zero `oklch` users remain in the review surface" is false while the tokens themselves are defined in `oklch` (`styles/tokens.css:8-23`). **What did not change:** the path/explorer fix is real and measured (252 px in a 252 px container), the page no longer overflows **horizontally** at 1600 or 320, and the composition and wording fixes stand. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **route body updated — the section above records four accepted-design defects addressed on this route rather than re-measured.** The committed probe's unrecorded state is answered in the body and rendered as the control's own state with its total withheld (B6); the narrow jump route is composed above the family tree and the centre's empty sentence names its own plane (B3); the tree's hand-copied `oklch` washes become one token-derived `oklab` helper (B1); and the explorer's path button wraps instead of being clipped (B7). The section names what is **routed** rather than absorbed and states that the B3 sentence was a **wording** defect and not a false claim about the pane's own state. **The B1 and B7 sentences this entry first carried were corrected by the dated entry above, on the independent verifier's own measurement.** **Citation accounting:** every row this route's line movement displaced was re-derived from each construct's declaration at this candidate; the rows into `changeSetBar.tsx` moved with the file's own insertions (`useReviewCatalogue` `:337-384` → `:371-424`, `leafIsLive` `:607` → `:673-688`, `ReviewEntryState` `:391-429` → `:425-467`, `includeLeaves` `:85` → `:93`) and the rows into `SourceExplorer.tsx` moved with that file's own additions (`inventoryEntry` `:78-129` → `:90-148`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T22:50:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, memory worktree only; no code changed; leaf base `a9a1a41bba535803421470bd17d858657177cb5f`): **route body corrected — two of the three L33 panels are withdrawn because commit `a9a1a41b` reverted them.** A withdrawal banner now heads the L33 section and the two paragraphs about `lifecycle-list/LifecycleList.tsx` and `panels/useCollapsedTaskGroups.ts` carry their own marker; two reference rows citing the deleted `landedLeaves.ts` and the removed `openedKeys` were deleted rather than re-pointed, and every other row this pass touched had its range re-derived by locating the anchor literally in the candidate. The **third** panel's paragraphs (`panels/changeset/`, the per-leaf breakdown) are unaffected by the revert and were left standing, as was the header-count sentence the reverted list still carries. The revert was a direct emergency commit with no curator pass behind it, which is why this route described a module that exists in neither tree; the deleted module's own sidecar was removed by the same curation. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **route body updated — the landed-leaf admission, the collapse rule that bounds it, and the per-leaf attribution on both master readers.** The new section names the new `landedLeaves.ts` module and the rules it owns, the two bounds (auto-collapse by child facts; never close a row that carries rows), the live-projection numbers, the collapse hook's second storage key and changed signature, and the superseded `includeLeaves: false` optimisation with the option's retention recorded. **Citation accounting:** every row this leaf's line movement displaced on this route was re-derived against the candidate with the gate's own resolver. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **route body updated — the change-set control renders its refusal.** The new section records that `detail-panel/changeSetBar.tsx`'s `ChangeSetButton` renders the refusal's own code and reason beside a state marker while still opening what it names, with the case that drives the click and asserts the rendered reason. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

## Hot Path Summary

Task detail prose, `TaskNotes.tsx`, and the shared notes reader use `TaskArtifactReaderTarget` for notes or registered requirement packets. `detail-panel/taskReader.tsx` mounts the requirement-link context; `notes-reader/NotesReaderViewer.tsx` owns the kind-aware content transport and takeover.

## Governing Overview

[dashboard/src overview](../overview.md)

## Current Structural Panel Contract

Panels receive real task-document hierarchy and current occupant facts from the data route. RailChat
and the session cockpit select structural document+role seats; task assignment posts that identity,
and replacement changes only the occupant. No panel derives hierarchy from spawn ancestry or treats
a lifecycle/session id as the task address.

## 260713-TES-L5F2 Change

The shared `SessionComposer` and contextual `RailChat` regression suites now prove that composer
answer mode does not require a lifecycle or gate. Both follow the same session-owned protocol as
the canonical cockpit: read the hosted session's bridge epoch, POST the answer to that exact
session's `interaction-response` route, lock duplicate sends, and never route an adapter answer
through reliable `/submit`.

## 260731-EFA-L8 Split Layout

### 260713-TES-L1 Reviewed — Heartbeat Wording In Session Cockpit

Route body reviewed for the supervisor → agent-notifier rename: the session-cockpit heartbeat UI
(`BusPane`, `SeatInspector`, `SessionRail`, `sessionRailParts`, sessions-view) now uses
`AgentNotifierHeartbeat` / `agentNotifierHeartbeat` and "Agent notifier heartbeat" labels. No
panel-shape or layout change; per-file detail lives in the session-cockpit overview and the file
sidecars.

The frontend-rail size remediation (R4/R5) re-shaped this route: `DetailPanel.tsx`
→ `detail-panel/` (canonical entry + `state.ts`, `model.ts`, `lifecycleBody.tsx`,
`taskReader.tsx`, `taskDocPanels.tsx`, `changeSetBar.tsx`, `styles.ts`, seven
behavior-split test files + `test-utils.tsx`); `LifecycleList.tsx` →
`lifecycle-list/` (four behavior-split test files + `test-utils.tsx`);
`SessionsView.tsx` → `session-cockpit/sessions-view/` (controller/body/palette/
styles + six test files); `ConversationTimeline.tsx` →
`session-cockpit/conversation/conversation-timeline/` (12 machinery modules +
seven test files); `engineRoomStyles.ts` → engine-room style domains + `styles.ts`
barrel; `EnclosureCanvas.tsx` → eight engine-room sibling modules. Shared panels
also gained parts/styles modules (`sessionComposer*`, `terminalSession.ts`,
`interactionParts*`, `launchFlowParts*`, `sessionRailParts*`, `stageLayers.tsx`,
`conversationSurfaceParts*`, `chatsStageStyles.ts`). The naming rule
(kebab-case folder, one canonical entry, short responsibility-based siblings) is
now a repository guideline. Behavior is preserved.

## Purpose

### 260731-EFA-L23 Route Delta

L23 makes Hangar expose optional durable lifecycle-operation kind, status, phase, and
`currentCommand` as one compact enclosure badge without inventing an operation when none is
projected. The live command stays single-line and width-responsive through CSS ellipsis, with its
complete value retained in `title`; it is not truncated once by character count.

TES-L6 changes the command-seat panel boundary from one global spine to sprint-qualified groups.
`FlowTab` consumes bound fixtures, while the session cockpit delegates group derivation to the data
model and renders legacy unbound seats only as migration state.

This route contains reusable cockpit panels plus focused child routes. Its strategic UI owners are:

- [session-cockpit](session-cockpit/overview.md) — the sole full-page Chats destination.
- [engine-room](engine-room/overview.md) — the Engine Room process visualization.
- lifecycle-list/LifecycleList.tsx + detail-panel/DetailPanel.tsx — Operations task navigation and reader.
- RailChat.tsx — contextual task-side chat, not a second full-page chat product.
- Terminal.tsx, SessionComposer.tsx, and HighlightComposer.tsx — shared interactive surfaces
  consumed by the canonical cockpit.

Detailed session state, submission, withdrawal, cleanup, and authority behavior belongs in the
[data overview](../data/overview.md). This parent intentionally keeps only composition boundaries.

## FEUI-L9R Recovery Composition

The shared `Terminal` panel preserves its mounted xterm and scrollback while performing at most one
explicit socket reattach for each changed serving boot. The canonical Chats chooser owns a fixed,
bounded viewport dialog with explicit loading/empty/timeout/error states and operator Retry; it does
not render a pre-session adapter process or create a second catalog store. On an empty narrow
cockpit, responsive layout keeps the sole chat-creation entrance available.

## FEUI-MX-FIX-2 Open Failure Composition

Shared callers do not infer session creation from a completed request. `HighlightComposer.tsx`
shows a failed create before readiness or submit and sends no selected context. `RailChat.tsx`
shows the same typed failure and withholds contextual delivery. Both consume the accepted-row result
from the data route; neither writes a private row, focuses a requested id, or retries through paste.

## Route Model

### Canonical Chats

FEUI-L8 retires the legacy Chats.tsx and SessionList.tsx path. CockpitShell now exposes one
Chats destination backed by the persistent session-cockpit layer; Operations remains the default.
The right inspector is closed by default and toggleable. The replacement duty and deletion map lives
in the [session-cockpit overview](session-cockpit/overview.md).

- SessionRail + data/railModel replace SessionList + data/sessionGroups.
- ChatContextBar carries launch, task/leaf context, local lifecycle routing, and authoritative leaf
  attach/move duties.
- SessionsView owns smart focus, live action routing, persistent PTY composition, key/palette zones,
  and the optional inspector.
- LandedCleanupNotice and EndedSessionState retain unavailable cleanup and ended-row truth without
  pretending an empty PTY is a live conversation.

### Shared Interactive Panels

- Terminal.tsx is the xterm/socket wrapper. Since 260718-CHATS-L4 a controlled session's runner
  line-log appears only inside the read-only terminal-diagnostics drawer (the structured
  `ConversationSurface` is the controlled-session default); legacy raw sessions still host a vendor
  TUI. Terminal.tsx is not the structured conversation renderer — that lives in the
  [session-cockpit](session-cockpit/overview.md) `conversation/` grammar.
- SessionComposer.tsx is the shared CodeMirror reliable-submit surface. It consumes effective
  keymap/profile state and uses authoritative withdrawal for pop-back.
- HighlightComposer.tsx sends a selected context package only after acceptance; selection and target
  choice cannot move active route/focus on rejection or ambiguity. Its pre-projection task-document
  fallback is a stable module-level snapshot, so the always-mounted composer cannot force React into
  an external-store update loop while analytics is still absent.
- RailChat.tsx renders contextual task-side chat under the same registry, not a competing destination.

### Operations And Other Routes

Operations, Detail, Engine Room, notes reader, file viewer, changeset, and lifecycle-design retain
their existing responsibilities. Focused child overviews and one-to-one file cards are authoritative;
the Chats refactor does not move those routes.

## Invariants And Boundaries

- Exactly one full-page Chats destination; no legacy Chats layer and no Sessions navigation item.
- Operations is initial. The Chats inspector is supplementary, default closed, and toggleable.
- Shared panels consume canonical data stores and authority clients; they do not create private
  session catalogs, conversation indexes, or submission ledgers. The 260718-CHATS-L4 structured
  surface holds only a reconstructable projection — no durable browser conversation index.
- Create-dependent panel actions proceed only after the shared opener returns an accepted server
  row; visible failure precedes readiness, focus, and delivery.
- The structured conversation surface (260718-CHATS-L4) is the controlled-session default and
  consumes adapter-normalized history/index/resume from the landed L1/L2/L3 contracts; the PTY
  line-log is now the read-only diagnostics drawer + legacy-raw body, not the message renderer.
- Reliable submit, withdrawal, interaction answers, bus replies, and control actions remain separate
  channels and never fall back to shared paste.
- No Domain Documentation source is configured; direct same-repository source, tests, reviewed task
  evidence, and recovered project history govern this route.

## Child Route Onboarding Map

| Child route | Governing overview |
| --- | --- |
| `session-cockpit/` | [Canonical Chats](session-cockpit/overview.md) |
| `engine-room/` | [Engine Room](engine-room/overview.md) |
| `file-viewer/` | [File Viewer](file-viewer/overview.md) |
| `changeset/` | [Change-Set Viewer](changeset/overview.md) |
| `notes-reader/` | [Notes Reader](notes-reader/overview.md) |

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Review child route — the family tree and the central reading path | [FamilyTree.tsx](review/FamilyTree.tsx.md) · [FamilyReviewCenter.tsx](review/FamilyReviewCenter.tsx.md) |
| Review child route — the workspace and the source explorer | [ReviewWorkspace.tsx](review/ReviewWorkspace.tsx.md) · [SourceExplorer.tsx](review/SourceExplorer.tsx.md) |
| Review child route — the mounted family composition cases | [ReviewWorkspace.family.test.tsx](review/ReviewWorkspace.family.test.tsx.md) |
| Review child route — the captured family bodies those cases are driven with | [familyReview.complete.captured.json](review/familyReview.complete.captured.json.md) · [familyReview.continued.captured.json](review/familyReview.continued.captured.json.md) · [familyReview.emptyRoster.captured.json](review/familyReview.emptyRoster.captured.json.md) · [familyReview.identical.captured.json](review/familyReview.identical.captured.json.md) · [familyReview.oneSided.captured.json](review/familyReview.oneSided.captured.json.md) · [familyReview.truncated.captured.json](review/familyReview.truncated.captured.json.md) · [familyReview.walkFinal.captured.json](review/familyReview.walkFinal.captured.json.md) · [familyReview.capture-provenance.json](review/familyReview.capture-provenance.json.md) |

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured. This compact
parent was refreshed from its repository-local child overviews, source/tests, and reviewed L8 record.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for panels. | — | — |

## Cross-Repo References

No cross-repository implementation source governs the panels route; all production imports resolve
inside agents-remember.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `Cockpit` view map contains the declared view map. | `VIEWS` | dashboard/src/cockpit/Cockpit.tsx:76-84 |
| The Chats cockpit keeps its `SessionsView` mounted and toggles its display rather than unmounting it. | "The sole product-facing Chats cockpit is never unmounted"; "<SessionsView" | dashboard/src/cockpit/Cockpit.tsx:803-807; dashboard/src/cockpit/Cockpit.tsx:809-810 |
| The persistent Chats layer renders `SessionsView` with active, selected lifecycle/leaf, task-document, and context props. | "<SessionsView"; "active={view === \"chats\" && !takeover}"; "selectedLeafKey={viewedLeafKey}" | dashboard/src/cockpit/Cockpit.tsx:809-810; dashboard/src/cockpit/Cockpit.tsx:810-810; dashboard/src/cockpit/Cockpit.tsx:812-812 |
| Dashboard state authority is held by `DashboardState`, `dashboardStore`, and `applySnapshot`. | `DashboardState`; `dashboardStore`; `applySnapshot` | dashboard/src/data/store.ts:24-56; dashboard/src/data/store.ts:329-401; dashboard/src/data/store.ts:18-19 |
| The production application route is owned by `App`. | `App` | dashboard/src/App.tsx:10-19 |
| The production route returns `Cockpit`. | `Cockpit` | dashboard/src/cockpit/Cockpit.tsx:366-390 |
| `CockpitShell` defaults `initialView="operations"`. | "export function CockpitShell({ initialView = \"operations\"" | dashboard/src/cockpit/Cockpit.tsx:886-940 |
| The terminal panel owns the shared terminal surface. | `Terminal` | dashboard/src/panels/Terminal.tsx:110-202 |
| The shared composer surface is implemented by `SessionComposer`. | `SessionComposer` | dashboard/src/panels/SessionComposer.tsx:57-117 |
| Selection-send behavior builds context and submits it to a selected or routed target, committing only on accepted or queued delivery. | `HighlightComposerImpl`; `submitTo`; `successful` | dashboard/src/panels/HighlightComposer.tsx:715-787; dashboard/src/panels/HighlightComposer.tsx:602-603; dashboard/src/panels/HighlightComposer.tsx:254-256 |
| Contextual task-side chat builds a leaf context package and resolves the current occupant from structural task identity. | `buildLeafContextPackage`; `RailChatImpl`; `findSessionForTask` | dashboard/src/data/sessions.ts:596-608; dashboard/src/panels/RailChat.tsx:255-289; dashboard/src/panels/RailChat.tsx:469-537 |
| `LifecycleList` owns Operations navigation, row grouping, the selection callback, and hidden-list re-show behavior. | "function LifecycleListImpl({" | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:224-259 |
| `DetailPanel` resolves the selected task/lifecycle/series reader target and renders the task document content. | "function DetailPanelImpl({"; "export function displayedReaderDoc({"; "export function TaskReader({" | dashboard/src/panels/detail-panel/DetailPanel.tsx:18-70; dashboard/src/panels/detail-panel/model.ts:103-132; dashboard/src/panels/detail-panel/taskReader.tsx:638-674 |
| The lifecycle state vocabulary is the live/terminal partition consumed by the lifecycle panel; the `State`/`Phase` literals moved to `models/lifecycle.py` by 260731-EFA-L9 while the live/terminal sets stay in observer. | "State = Literal[LiveState"; "LIVE_STATES: tuple[LiveState"; "TERMINAL_STATES: frozenset[str] = frozenset(vocabulary_names(TerminalState, label=\"TerminalState\"))"; "export const LifecycleList = memo(LifecycleListImpl);" | mcp/src/agents_remember/models/lifecycles/responses.py:19-19; mcp/src/agents_remember/observer/lifecycle_state.py:105-107; mcp/src/agents_remember/observer/lifecycle_state.py:108-108; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:357-357 |
| The shared fixture builders seed lifecycle and projection nodes from served fixtures, with required lifecycle fields copied from the served lifecycle. Ranges re-derived: the `lifecycle` occurrences this row names are at `:90-90`, `:243-243` and `:257-257`. | `SERVED_LIFECYCLE`; `BASE_LIFECYCLE`; `lifecycle`; `projection` | dashboard/src/test/fixtures/wire.ts:331-347; dashboard/src/test/fixtures/wire.ts:78-78; dashboard/src/test/fixtures/wire.ts:95-107; dashboard/src/test/fixtures/wire.ts:243-248 |
| The typed fixture factories provide lifecycle and projection nodes. Ranges re-derived: the `lifecycle` occurrences this row names are at `:90-90`, `:243-243` and `:257-257`. | `lifecycle`; `projection` | dashboard/src/test/fixtures/wire.ts:331-347; dashboard/src/test/fixtures/wire.ts:78-78; dashboard/src/test/fixtures/wire.ts:243-248 |
| The hand-kept snapshot payload provides the generated timestamp. | "\"generatedAt\": \"2026-06-14T09:01:00+00:00\"" | dashboard/src/fixtures/snapshot.json:1790-1928 |
| `Dot` renders its state glyph inside `aria-hidden="true"`. | `Dot`; "aria-hidden=\"true\"" | dashboard/src/grammar/Dot.tsx:119-129; dashboard/src/grammar/Dot.tsx:125-125 |
## Current L5I Route State

The panels route now treats keep-alive shells as an explicit performance boundary: persistent
top-level panels memoize unchanged shell rerenders, while their own store subscriptions remain live.
Interactive controls also favor evidence-bounded wording, including reopened gate failures and
viewport-measured leaf-picker placement.

## 260727-CHATS-IM-L2 No Route-Model Impact

The Engine Room effects overlay and session-cockpit child-history behavior are internal to their
existing child routes. Panel inventory, cross-panel ownership, and the shared panel primitive are
unchanged.

## 260731-EFA-L4 Typed Vocabulary Route Impact

The panel inventory is unchanged. What changed is the vocabulary the panels consume, and four rules
now hold across the route rather than inside one file.

- **The state mark is named by the panel, never by `Dot`.** `grammar/Dot` renders `aria-hidden="true"`,
  so the accessible name for a severity or a lifecycle state is the wrapper's duty. `AttentionQueue.tsx`
  wraps it in a `severityMark` span carrying `role="img"` + `aria-label="Severity: <severity>"`;
  `LifecycleList.tsx`'s `data-testid="task-state"` span carries the same kind of label with NO role and
  is correct only because it sits inside React Aria's `role="option"`, whose name-from-content absorbs
  it. Drop the role from the AttentionQueue wrapper and the severity leaves the accessibility tree
  entirely — `aria-label` on a bare `<span>` names a `generic`, which ARIA prohibits (axe-core
  `aria-prohibited-attr`, `serious`) and no screen reader announces. Any new panel that renders a `Dot`
  inherits this: supply a role that can hold a name, or sit inside one.
- **Two vocabularies reach one dot, and only one of them is the document's.** Both Operations row
  builders compute `lifecycle?.state ?? statusVariant(doc.status)` (`LifecycleList.tsx` `docRow` L595,
  `seriesRow` L644; `lifecycleRow` L717 passes `lifecycle.state` straight through), so a bound lifecycle
  hands `Dot` the RAW server state string and `statusVariant` only ever sees `TaskDocNode.status` /
  `SeriesNode.status` — whose entire vocabulary is `models/task_document.py::DocStatus`
  (planning · inProgress · Completed), assigned verbatim by `snapshots.py` at both build sites. That is
  why L4 could delete its `blocked` / `paused` / `abandoned` arms with no behaviour change: they sat on
  the right of the `??` and no served payload could enter them. Adding an `awaiting-developer` arm here
  would repeat the same defect — the live state already arrives on the left.
- **`awaiting-developer` is a rendered Operations state.** The lifecycle vocabulary is six states
  composed from named halves server-side (`observer/lifecycle_state.py`: `LiveState` + `TerminalState`,
  with `State = Literal[LiveState, TerminalState]` and `check_state_partition` refusing at import any
  state filed on neither side); `awaiting-developer` is LIVE, not terminal. `LifecycleList.test.tsx`
  pins the handover rather than the paint: an `awaiting-developer` row's mark must equal a bare
  `<Dot variant="awaiting-developer">` and must NOT equal what an unrecognised variant renders, and a
  `paused` row's mark must differ from an `abandoned` row's in the same list.
- **Rollup buckets are derived, not restated.** `Metrics extends LifecycleStateCounts` in the mirror and
  the bucket field names come from `ACTIVE_STATES` through `StateCountField<>`, so a seventh state adds
  a REQUIRED field and every object claiming to be a `Metrics` stops compiling until it counts it. The
  panels suites stopped hand-listing buckets: `LifecycleList.test.tsx` and `DetailPanel.test.tsx` build
  metrics with `metricsFor(lifecycles)`, the client twin of `reducer.py::_metrics`.

`DetailPanel`'s sub-task index now renders two different server rows. `SubTaskIndex` takes
`SubTaskRow`, the union of `TaskSubTaskRefNode` and `SeriesSubTaskNode` — two `extra="forbid"` server
models that share the common task-row fields but have distinct optional navigation/time fields. Only `TaskSubTaskRefNode` declares
`linkedLifecycleId`, so the cross-series `→` jump is reachable only from a master task document; the
branch is guarded by
`"linkedLifecycleId" in ref` and is structurally unreachable for a series rendered through
`seriesAsMasterDoc`. Only `SeriesSubTaskNode` declares `createdAt`, so creation ordering moved OFF the
index — where it could never have sorted a master's rows — and onto `seriesAsMasterDoc`, the one path
whose rows carry the field; `snapshots.py::_series_subtask_nodes` has normally already applied it, and
both sides skip the sort unless every row carries a `createdAt`.

**What the fixture conversion does and does not pin.** `EventRiver.test.tsx`, `RailChat.test.tsx` and
`SessionComposer.test.tsx` no longer author wire nodes: every projection node comes from
`dashboard/src/test/fixtures/wire.ts`, whose bases are assembled from `dashboard/src/fixtures/snapshot.json`
and annotated with the mirror type, so a fixture that compiles is a shape the MIRROR can produce. Be
exact about the reach — `wire.ts` and `snapshot.json` are hand-maintained fixture/sample artifacts,
while `types/projection.ts` is generated and stale-checked from the Pydantic projection schema.
`tsc -b` binds `test/fixtures/wire.ts` to that generated mirror (annotated bases,
`Overrides<O, Node>` at every call site, `test/wireFixtureGuard.test.ts` refusing one-token opt-outs),
and `test/contract.test.ts` measures how completely `snapshot.json` exercises it in three type-level
directions plus runtime vocabulary assertions. The producer-to-TypeScript contract is held by the
generator and its stale check; the manual boundary is sample coverage.

## 260731-EFA-L7 — Conversation Split Absorbed

The panels route absorbed the L7 live-thinking change on top of the L8 split: the session-cockpit conversation family carries the coalesced live-thinking indicator and its pins; the over-limit dashboard files were split by L8 and the armed file-size rail now covers this route's TS/TSX.

## L23 Engine Room Admission Evidence

Panel-level operations now expose the control plane's source-lineage state as a
diagnostic fact. Rendering stays read-only and uses the projected summary for
operator context; recovery remains a backend worktree operation.

## 260815-DAG-L14 Detail-Panel Route

`detail-panel/` threads `docPathForRef` so typed `masterRef` sprint rows open their commanded
master document (the sprint → master leg of the drill-down); the reader renders `MasterRefIndexRow`
for projected targets and falls back for unprojected ones.


## 260815-DAG-L12 Route Impact

New child route [sprint-graph](sprint-graph/overview.md): the optional sprint execution graph wave-grid view (≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual predecessor labels, narrow single-column fallback). `detail-panel/taskReader.tsx` mounts graph content when present and mounts the sprint-scoped `CloseoutQueue` independently, so graph-less atomic-sequential sprints still expose scheduling state (L12-R5); `detail-panel/model.ts` `MasterDocView` carries optional `executionGraphView` (L12-R4).

## 260821-CLIVE Projection And Discard Panels

`CloseoutQueue` renders the producer's disposable service/source/problem/member projection. Typed
`invalid-empty` source problems include their repair action; the browser does not reconstruct
readiness or mutate queue state. Graph presence is not a prerequisite for this scoped projection.

The detail reader has a separate `Discarded before start` audit section with reason, timestamp, and
proof fingerprint. `LifecycleList` appends `N discarded` beside ordinary done/total progress. Both
surfaces preserve the same boundary: audited removal stays visible but never counts as completion.


## 260815-DAG Master Full-Gate Repair Route Impact

`session-cockpit` test suites (BusPane, ChatsStageBody, ConversationSurface, stageSurface) now flush the virtualizer scroll-observer debounce in an async `afterEach` before jsdom teardown.

## 260831-CCR-L23 Task-Artifact Reader Routing

L23 routed task-local requirement packets through the existing reader chrome: `DetailPanel.tsx`,
`taskReader.tsx`, `TaskNotes.tsx`, and the takeover now carry the shared discriminated
`TaskArtifactReaderTarget` (kind notes/requirements); the task reader mounts the
`TaskRequirementLinks` provider so task prose and References can open registered
`requirements/...` packets in the internal reader. The notes-reader child route owns the
viewer change; file-level detail lives in the panel sidecars.

## CCR-R18@v1 Hangar Fixture Versions

260831-CCR-L18 updated the Hangar render-test fixture so its hand-built `lifecycleOperation` sample carries the new `schemaVersion` and `stateMatrixVersion` literals required by the generated mirror. File-level detail lives in that sidecar.

## 260915-KS-L45 The Task-View Entry Into The Review Panel Is Reachable

The review panel existed before this leaf; what did not exist was a **navigation** into it on a live
leaf task. `detail-panel/changeSetBar.tsx` is where that is decided, and the decision is now made from
the server rather than from a prop:

- The bar renders an **Intent review** `ChangeSetButton` beside the working and committed change-set
  buttons — never in their place — and the gate is `live && subject`: the leaf's enclosure must be
  live (one extracted `leafIsLive` predicate, shared with the working action so the two entries cannot
  disagree about what "live" means) **and** a reviewed subject must have come back from the server.
- The subject catalogue comes from a new read. `useReviewCatalogue(live, repo, master, leaf)` calls
  `intentReviewEntries(repo, master, leaf)` — the `data/review.ts` client for
  `GET /api/review/intent/entries` — and keeps `result.entries?.[0]`. The `selectorKind`/`selectorId`
  **props are gone**, because no production caller ever supplied them: `taskReader.tsx` and the master
  header pass `kind`/`repo`/`master`/`leaf`/`onOpen` only, so the old `live && selectorId` gate could
  never hold on a real navigation and the panel was unreachable by design rather than by policy.
- The gate is not weakened by the swap. A refusal, an empty entry list, a rejected promise and a
  non-live leaf all leave the subject `undefined`, so **no subject means no button** — the same
  behaviour as before, now reached through a source that can actually produce a subject. The hook
  fetches nothing at all for a leaf that is not live, because there is no candidate to resolve.
- The button's target carries the subject's **recorded** identity
  (`review: { selectorKind: subject.selector_kind, selectorId: subject.selector_id }`), so the browser
  still never chooses the candidate: the id is a recorded identity inside the candidate the server
  resolved from canonical task context, and the client's `ReviewEntry` has no path field on purpose.

The entry is also still the only reviewer affordance in the bar, and it still reports no counters —
its counter effect reads the leaf or master change-set request only. It is display-only in the same
sense the panel is: the bar offers a navigation, and the surface it opens generates no semantic
judgment and publishes no assessment.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The gate: a live leaf and a server-returned subject, with the subject's own recorded kind and id carried into the target.** | "Intent review" | dashboard/src/panels/detail-panel/changeSetBar.tsx:2-4 |
| **The hook that asks the server for the leaf's reviewable subjects and keeps the first.** | `useReviewCatalogue` | dashboard/src/data/useReviewCatalogue.ts:63-110 |
| **The one liveness predicate both gated entries read.** | `leafIsLive` | dashboard/src/panels/detail-panel/changeSetBar.tsx:560-572 |
| The client the hook calls, whose `ReviewEntry` has no path field on purpose. | `intentReviewEntries`; `ReviewEntry` | dashboard/src/data/review.ts:721-727; dashboard/src/data/review.ts:692-697 |

## 260921-ICR-L13 The Change-Set Entry Threads The Published Generation

This route's change-set entry is now generation-bound for master nets. `ChangeSetButton`
stores the master read's published `generation` as pins and opens the viewer with
`{ ...target, generation }`, so the series view — and each file expansion inside it — reads
the listed generation rather than re-resolving the live tip. No panel was added and no
takeover dispatch changed; the reviewer entry, its liveness gate and its read are untouched
by this leaf.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The entry threading the published generation into the viewer target.** | "onClick={() => onOpen(generation ? { ...target, generation } : target)}" | dashboard/src/panels/detail-panel/changeSetBar.tsx:140-140 |
| **The generation state the button carries from a successful master read.** | `MasterNetPins` | dashboard/src/panels/detail-panel/changeSetBar.tsx:11-12 |

## 260921-ICR-L3 The Source Pane's Entries Open Into The Content Of Both Bound Code Trees

**Route meaning changed, narrowly: the Source pane stopped being display-only about *what* changed and
became the way into *the bytes*.** A listed inventory entry is now openable, and opening it reads the
file at the two code trees the inventory published and renders both endpoints' actual content in place.
That is ICR-R03's rendering half, and it is the defect the route had been carrying: an inventory row
labelled as an expansion showed a path, a status and a reproducing command, and **no bytes at all**, so
a reader had to leave the surface and run the command to learn what had changed.

`panels/review/SourceContent.tsx` is the new renderer (222 lines), a third component in the child route,
and `panels/review/ReviewSurface.tsx` grew 462 → **549 lines** to reach it:

- **`inventoryEntry` renders the published path as a button** — `data-testid="review-inventory-open"`,
  `data-path` carrying the path exactly as the server published it, `aria-expanded` carrying the open
  state — **only when the inventory named both of its code trees**; the same click closes the row. An
  inventory that named no pair has nothing to open, so it renders the path as text and no control.
- **`Inventory` holds the one piece of state this route's rendering now has** — `const [open, setOpen] =
  useState<string | null>(null)`, addressed by the published path — and derives the generation pair from
  its own `before_code_tree_id`/`after_code_tree_id`, which `inventoryEntry` then mounts `SourceContent`
  with. The two ids are the listing's, so a row opened after the branch moved still shows the generation
  the reader was looking at.
- **`SourcePane` forwards the task context** (`repo`/`master`/`leaf`) into `Inventory`, which is how the
  expansion request carries the same target the root's `data-review-target` stamps.
- **`byteNamedEntry` gained the explicit non-addressability note** (`data-testid=
  "review-byte-path-not-addressable"`): the byte-form row is listed by its exact bytes and carries **no**
  expansion control, because no request this text-carrying vocabulary can spell would address it. The
  pane states that rather than implying a click would open something.

**What the new renderer decides, and what it deliberately does not.** Every branch is decided by each
side's declared `state` and never by inspecting its text: both sides `present` → the shipped `DiffPane`
in split mode over the two files' own bytes; one side textual (a regular file's text, or a symlink's
recorded target) → that side drawn as content with the other side's own reason beside it, plus an
explicit `review-source-no-diff-claimed` line, because a diff there would claim the opposite endpoint is
a known-empty document; neither side textual → the two state lines alone. The state line carries the
declared state, the measured object identity and the byte count, and adds the long detail only when the
state is not a complete untruncated text. A bounded read is stated as a prefix of the object
(`review-source-truncated`), `currentness` says whether the listed generation is still the leaf's, the
leaf-change-set bound is stated only when that is what admitted the path, and a typed refusal renders
with its code, detail, next action and offending input and **no content** — a refusal is a normal answer
from this route, not a degraded success. `DiffPane` (from the change-set route) and `FilePane` (from the
file-viewer route) are reused rather than a third viewer being grown, and the module's header records
both, so the surface now names **two** reused renderers instead of one.

**`data/review.ts` grew 320 → 414 lines** and gained the expansion's wire types
(`ReviewSourceSideState`, `ReviewSourceSide`, `ReviewSourceExpansion`, `ReviewSourceContentResult`) and
`reviewSourceContent(...)`, which reads the typed refusal body **whatever the HTTP status** and throws
`FilesApiError` only for a body that is not this route's answer — the one function in that client that
deliberately does not go through `getJson`, because on this route a typed refusal arrives with a 400/404
status. `intentReview` and `intentReviewEntries` are unchanged.

The panel inventory is otherwise unchanged: no new route, no new takeover, no change to the reviewer
dispatch or its target shape, and no other panel touched. The server half of this contract — the
source-content route and the model the expansion mirrors — is recorded by the `mcp/` route's onboarding,
not here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Inventory rows preserve path/status and control state; optional inline content expansion uses the listed tree pair. | `inventoryEntry` | dashboard/src/panels/review/SourceExplorer.tsx:58-116 |
| Byte-named paths remain listed and explicitly cannot be addressed by this text request vocabulary. | `byteNamedEntry` | dashboard/src/panels/review/SourceExplorer.tsx:118-130 |
| Inventory rows receive their expansion state from the workspace and bind expansion to the inventory tree IDs. | `InventoryRows`; `useWorkspaceState` | dashboard/src/panels/review/SourceExplorer.tsx:170-222; dashboard/src/panels/review/ReviewWorkspace.tsx:159-196 |
| The pane that forwards the task context an expansion request carries. | `SourcePane` | dashboard/src/panels/review/ReviewSurface.tsx:299-354 |
| The central statement delegates to the existing statement renderer, and source expressions delegate to bound source content. | `SelectedStatement`; `ExpressionCard` | dashboard/src/panels/review/SubjectReview.tsx:53-114; dashboard/src/panels/review/ReviewExpressions.tsx:182-239 |
| Source operands are rendered from their declared states; unavailable content does not become an invented diff operand. | `Sides` | dashboard/src/panels/review/SourceContent.tsx:54-98 |
| The expansion states bounded content and the admitted path relation alongside the actual source rendering. | `boundedNote`; `Expansion` | dashboard/src/panels/review/SourceContent.tsx:100-110; dashboard/src/panels/review/SourceContent.tsx:126-165 |
| **The typed refusal rendered with its code, detail, next action and offending input, and with no content.** | `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:112-124 |
| **The client's expansion wire types and the request that reads the typed body whatever the status.** | `ReviewSourceSide`; `ReviewSourceExpansion`; `reviewSourceContent` | dashboard/src/data/review.ts:329-336; dashboard/src/data/review.ts:347-362; dashboard/src/data/review.ts:727-745 |
| **The cases that measure the whole route at the real surface over a stubbed transport: the addition, the two-sided modification, the binary/symlink/submodule sides, the superseded generation, the bounded prefix, the typed refusal, the exact request, the leaf-change-set bound, the byte-form row and the inventory with no pair.** | "the source pane opening a listed entry"; "lists a byte-form row without implying it can be opened"; "offers no expansion for an inventory that named no code trees" | dashboard/src/panels/review/SourceContent.test.tsx:268-589; dashboard/src/panels/review/SourceContent.test.tsx:522-560; dashboard/src/panels/review/SourceContent.test.tsx:562-588 |

## 260921-ICR-L6 The Review Panel's Statement Area Gets Its Own Component

The **review child route gained its second component**, and the route-level fact is that the Intent
Reviewer's pane 1 no longer decides its own statement rendering inline.
`dashboard/src/panels/review/KnowledgeStatements.tsx` owns the statement area — the two recorded
operands and the state of each side — and `ReviewSurface.tsx` delegates it (476 → **462 lines**, with
the `sideState` helper and the `DiffPane` import gone from that file).

**The rule the component implements is ICR-R06's, and the defect it closes is worth stating at this
altitude because no gate caught it.** The pane used to draw the shipped `DiffPane` only when *both*
statement sides were `present`, while the side line returned `null` for the side that *was* present —
so an added or a removed statement rendered as two muted state lines and **no statement text at all**.
The four branches now decided from a side's declared `state`, never from its text:

- both `present` → the shipped two-sided diff, unchanged (and, as before, naming no side);
- one `present`, the other `absent` → a **one-sided diff** with the present operand on its own side and
  the absent side named above it, so the empty half is a stated fact rather than a blank to interpret;
- one `present`, the other `binary`/`unresolved` → the available text as content with the unavailable
  side's own reason beside it, an explicit "no diff is drawn" line, and **no diff** — a diff there
  would claim the opposite operand is a known-empty document;
- neither `present` → both sides' own state lines and no diff and no content pane.

**The route's other half of the same rule is a mechanical field row.** `ReviewSurface.tsx` gained
`fieldValue`, which prints `(absent)` for a value the server did not send and `(recorded empty)` for a
value that is present and empty, so no field row is silently blank and no reader has to decide which of
the two a gap meant — the display counterpart of the data contract
`application/review_statement_sides.py` owns. The panel inventory is otherwise unchanged: no new
route, no takeover change, and the child's file cards are the authority for the rest.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The child route's statement-area component: the four branches, the one-sided diff, and the available-content path that claims no addition or removal.** | `KnowledgeStatements`; `unavailable`; `oneSidedDiff`; `availableContent` | dashboard/src/panels/review/KnowledgeStatements.tsx:34-35; dashboard/src/panels/review/KnowledgeStatements.tsx:67-78; dashboard/src/panels/review/KnowledgeStatements.tsx:81-92; dashboard/src/panels/review/KnowledgeStatements.tsx:94-121 |
| **The state line rendered for every non-two-sided area, carrying each side's own token in `data-side-state`.** | `sideLine` | dashboard/src/panels/review/KnowledgeStatements.tsx:37-45 |
| The technical knowledge pane delegates statement rendering to KnowledgeStatements. | `KnowledgePane` | dashboard/src/panels/review/ReviewSurface.tsx:272-297 |
| **The field-row words this leaf added: absent and recorded-empty as two different facts.** | `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:166-167 |
| The technical knowledge pane delegates statement rendering to KnowledgeStatements. | `KnowledgePane` | dashboard/src/panels/review/ReviewSurface.tsx:272-297 |
| **The renderer case that fails against the pre-fix pane: an added invariant's full after statement read out of the rendered diff DOM beside an absent-before label.** | "draws an added invariant's full after statement beside an absent-before label" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:195-213 |
| The cases for the removal, the unreadable opposite, and the three declared non-present states as their own tokens. | "draws a removed invariant's full before statement beside an absent-after label"; "keeps the available text and claims no diff when the other side is unreadable"; "renders a %s side as that state and never as another one" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:215-229; dashboard/src/panels/review/KnowledgeStatements.test.tsx:244-260; dashboard/src/panels/review/KnowledgeStatements.test.tsx:262-275 |

## 260915-KS-L22 The Review Panel Route And Its Three-Pane Surface

The L22 section below records the panel itself — the three panes, their prohibitions and the
display-only submission boundary — and remains current. What it did not record is a way to *reach* the
panel on a live leaf; the section above supplies that, and supersedes nothing below it.

`panels/review/` is this route's new child, and its entry component is `ReviewSurface.tsx`, mounted by
the cockpit takeover when a change-set target carries the review variant. It renders the Intent
Reviewer's three panes in one scrolling column — Knowledge, Source, Evidence and assessment — in the
order the payload declares them, and it is display-only: the module has no control that writes
anything, no submission button, and no place a conclusion of its own could be assembled. The one
renderer it reuses is the change-set route's `DiffPane`, reached through the statement area
`KnowledgeStatements.tsx` owns and fed the statements the comparison published: **both operands when
both sides recorded one, and the available operand beside the named absence when one side did not**
(the `260921-ICR-L6` section above records that rule and supersedes the "only when both sides are
`present`" reading this section was written with); a side that is `absent`, `binary` or `unresolved`
renders as its own named state rather than as an empty diff, and neither the statement area nor this
file declares a second differ.

The prohibitions are rendered, not merely intended. Authored effects, preservation claims and
unresolved questions are listed under their own heading and detection signals under a second one,
because the payload keeps those two collections apart by element type; a selected path with no
registered attribution is reported outside any claim instead of being folded into one; a count the
comparison could not measure prints as not measured with its stated reason rather than as a zero;
and both lists that could show an assessment print `UNASSESSED — no assessment is recorded against
this subject.` when the collection is empty, so no pane has a favourable default to fall into.

Failure is a state on this surface too. A typed refusal is rendered with its code, its detail, the
offending input and the next action, and a transport error is its own line; neither is a degraded
success, because a refused review shows no panes at all. The submission block states the increment's
own boundary in the same voice: submission is not offered (or disabled, for a stale comparison) with
the reason and a next action naming the existing curator authority, and the three dispositions it
prints are labelled as that authority's vocabulary — none of them publication approval. Every
rendered state carries a `data-testid`, which is how the surface's cases read each pane back.

| Finding | Anchor | Source |
| --- | --- | --- |
| The child route entry component. | `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:856-928 |
| Pane 1, and the two collections it keeps apart — **and, since `260921-ICR-L6`, the statement area it delegates.** | "function KnowledgePane" | dashboard/src/panels/review/ReviewSurface.tsx:272-272 |
| Pane 2, the selected locations and what the selection did not reach — **and, since `260921-ICR-L3`, the pane whose listed entries open into their own content.** | "function SourcePane" | dashboard/src/panels/review/ReviewSurface.tsx:299-299 |
| Pane 3, evidence and assessment with both absence states stated. | "function EvidencePane" | dashboard/src/panels/review/ReviewSurface.tsx:354-407 |
| The technical panes print the owner assessment state rather than deriving a favorable judgment. | `KnowledgePane`; `EvidencePane` | dashboard/src/panels/review/ReviewSurface.tsx:272-297; dashboard/src/panels/review/ReviewSurface.tsx:356-412 |
| The block that states the display-only submission boundary. | "function SubmissionBlock" | dashboard/src/panels/review/ReviewSurface.tsx:409-438 |
| The refusal rendering, which left the surface for the outcome owner: one block prints every field the owner published, and both the surface and the expansion pane render it. | `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:115-177 |
| **The one renderer this child reuses, fed both operands when both sides recorded one and the available operand beside a named absence when one side did not — reached through the statement area `260921-ICR-L6` gave its own component.** | `DiffPane`; `KnowledgeStatements` | dashboard/src/panels/review/KnowledgeStatements.tsx:29-29; dashboard/src/panels/review/KnowledgeStatements.tsx:94-121 |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **No route impact:** this route's own governed sources are unchanged by `ICR-R08@v1` (the recorded relationship union, its vocabulary, its five application owners and its three case modules). The only edit to this document is citation-coordinate regeneration: rows that cite the review adapter, the source inventory, the review vocabulary, the two evidence manifests or the review route by line were re-derived from the anchors' real positions after this leaf moved those lines. No claim, anchor, wording or table shape changed, no verification stamp was advanced, and the candidate is uncommitted.
- 2026-09-22T17:20:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **route body update for the subject catalogue (`ICR-R09@v1`).** The governed sources of this route changed (the entry half's catalogue rewrite and its client/picker consumers), so this overview's body rows naming the renamed constructs (`useReviewSubject` → `useReviewCatalogue`, `ReviewSubjectRead` → `ReviewCatalogueRead`, the selected-row target spelling) and the ranges this leaf's candidate moved were re-read and re-derived by hand; no route-level fact was otherwise changed. **Stamp accounting:** the verification pair names the leaf's base; closeout owns the stamp once the code commit exists.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **route body updated — the change-set entry threads the published generation (new section above).** No panel added, no takeover dispatch changed, reviewer entry untouched. The three KS-L45 rows into `changeSetBar.tsx` are re-derived against this candidate (`"Intent review"` `:160` → `:275`, `useReviewSubject` `:71-96` → `:116-158`, `leafIsLive` `:164-179` → `:288-301`); the `review.ts` row stands (that file is untouched by this leaf). One known-false prose paragraph is deliberately left for its owner (see report): the KS-L45 section still gates the reviewer entry on `live && subject`, while ICR-R16 made it liveness-alone — reviewer-entry behavior this leaf does not change. No verification stamp was advanced; the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T23:13+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by this leaf's second curation pass.** the same anchor repair for the three case-title anchors on this route's two rows: each became the case's exact `it(...)` title as a double-quoted literal inside the cited range. The route's own statement is unchanged by the repair — this leaf's code change is in `mcp/`, and no dashboard source moved. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout's metadata refresh owns the real one.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the Source pane's inventory rows became the way into their own content, and this route gained a third component for it.** Added the `260921-ICR-L3` section above: `panels/review/SourceContent.tsx` is new (222 lines) and renders one listed entry's actual content at the two bound code trees — the three rules decided from a side's declared `state`, the reused `DiffPane`/`FilePane`, the bounded read stated as a prefix, the leaf-change-set bound stated only when it is the fact, and the typed refusal rendered with no content; `panels/review/ReviewSurface.tsx` grew 462 → **549 lines**, with `inventoryEntry` rendering the published path as a `review-inventory-open` button (only when the inventory named both code trees), `byteNamedEntry` gaining `review-byte-path-not-addressable`, `Inventory` holding which row is open and deriving the generation pair from its own published tree ids, and `SourcePane` forwarding the task context; and `data/review.ts` grew 320 → **414 lines** with the expansion wire types and `reviewSourceContent`, which reads the typed body whatever the HTTP status. **No route-level fact changed**: no new or removed route, no change to the reviewer takeover dispatch, the target shape or the cookie, and no other panel touched. **Citation accounting:** the rows of this document that cite `ReviewSurface.tsx` were re-derived against this candidate — the L22 block (`ReviewSurface` `409-409` → `482-482`, `KnowledgePane` `172-208` → `182-182`, `SourcePane` `279-279` → `337-337`, `EvidencePane` `322-322` → `395-395`, the two unassessed literals `211-366` → `200`/`439`, `SubmissionBlock` `373-373` → `446-446`, `RefusalBlock` `395-395` → `468-468`), the L6 rows (`1-7`/`179-206` → `1-9`/`182-205`, `fieldValue` `70-77` → `78-79`) and the L2 rows (`27-37`/`409-476` → `30-39`/`482-549`; `252-277`/`221-237`/`238-251` → `291-335`/`214-260`/`270-282`; `279-320`/`178-220` → `337-393`/`182-205`), with the L2 and L6 prose re-pointed at the newest section that owns each construct. The nine rows of the L3 section above are the ones this leaf added. **Stamp accounting:** the verification pair now names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against — and this card records this leaf's uncommitted candidate beside the older one it still carries; no commit contains the new bytes, so closeout owns the real stamp.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "export function CockpitShell({ initialView = \"operations\"" repointed to dashboard/src/cockpit/Cockpit.tsx:877-877. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "\"generatedAt\": \"2026-06-14T09:01:00+00:00\"" repointed to dashboard/src/fixtures/snapshot.json:1790-1790. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`, base `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9`): **the review child route gained its second component, and the section above records the rule and the defect it closes.** Added the `260921-ICR-L6` section: `panels/review/KnowledgeStatements.tsx` owns the statement area (the four branches decided from a side's declared `state`, the one-sided diff with the absent side named above it, the available-content-with-reason path that draws no diff, and the neither-present case), `ReviewSurface.tsx` is 476 → **462 lines** and delegates it, and `fieldValue` now prints `(absent)` versus `(recorded empty)` so no mechanical field row is silently blank. **Two claims in the L22 section were corrected rather than carried**, because this leaf's change falsified them: the child is no longer "one component", and the reused `DiffPane` is no longer "fed … only when both sides are `present`" — the section now points at the L6 record above and says so. Its reference rows were **re-derived against this candidate** (`ReviewSurface` `409-409` → `395-395`, `KnowledgePane` `172-208` → `179-179`, `SourcePane` `279-279` → `265-265`, `EvidencePane` `322-322` → `308-308`, the unassessed state `211-366` → `193-193`/`352-352`, `SubmissionBlock` `373-373` → `359-359`, `RefusalBlock` `395-395` → `381-381`, and the reused-renderer row now points at `KnowledgeStatements.tsx`), as were the L2 section's three rows (`27-36`/`409-476` → `27-37`/`395-463`; `252-277`/`221-237`/`238-251` → `238-264`/`207-223`/`224-237`; `279-320`/`178-220` → `265-307`/`179-206`). No verification stamp was advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the task-view entry into the review panel is reachable now, and this route gained the section that records how.** The gate in `detail-panel/changeSetBar.tsx` is `live && subject`: the `selectorKind`/`selectorId` props are gone and a live leaf's subject is read from `GET /api/review/intent/entries` by a new `useReviewSubject` hook. The card records why the old prop gate could never hold — `taskReader.tsx` and the master header pass no selector — and why the swap is not a weakening: a refusal, an empty list, a rejected promise and a non-live leaf all leave the subject undefined, so no subject still means no button. It also records that liveness was extracted into one `leafIsLive` predicate shared with the working change-set action, and that the button's target carries the subject's recorded kind and id rather than a path, so the browser still never chooses the candidate. The L22 section on the panel itself is retained unchanged below. No verification stamp was advanced.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "The sole product-facing Chats cockpit is never unmounted"; "<SessionsView" repointed to dashboard/src/cockpit/Cockpit.tsx:792-792; dashboard/src/cockpit/Cockpit.tsx:798-798. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "<SessionsView"; "active={view === \"chats\" && !takeover}"; "selectedLeafKey={viewedLeafKey}" repointed to dashboard/src/cockpit/Cockpit.tsx:798-798; dashboard/src/cockpit/Cockpit.tsx:799-799; dashboard/src/cockpit/Cockpit.tsx:801-801. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "export function CockpitShell({ initialView = \"operations\"" repointed to dashboard/src/cockpit/Cockpit.tsx:875-875. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the L22 section** — the new `panels/review/` child and its one component, the three panes rendered in the payload's own order, the states each pane prints instead of defaulting (unassessed, none_recorded, not measured, unclassified, refusal), and the reused `DiffPane` fed only two present sides. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns that stamp.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "function DetailPanelImpl({"; "export function displayedReaderDoc({"; "export function TaskReader({" repointed to dashboard/src/panels/detail-panel/DetailPanel.tsx:18-18; dashboard/src/panels/detail-panel/model.ts:103-103; dashboard/src/panels/detail-panel/taskReader.tsx:638-638. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T06:49:47+00:00: Generated citation repair: "function DetailPanelImpl({"; "export function displayedReaderDoc({"; "export function TaskReader({" repointed to dashboard/src/panels/detail-panel/DetailPanel.tsx:18-18; dashboard/src/panels/detail-panel/model.ts:103-103; dashboard/src/panels/detail-panel/taskReader.tsx:638-638. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `dashboard/src/panels/` route changed since the recorded verification commit. Re-read the card
  against the frozen on-disk source and re-checked its claims and cited ranges: nothing this card
  asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.

  `dashboard/src/panels/` route changed since the recorded verification commit. Re-read the card
  against the frozen on-disk source and re-checked its claims and cited ranges: nothing this card
  asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.

  `dashboard/src/panels/` route changed since the recorded verification commit. Re-read the card
  against the frozen on-disk source and re-checked its claims and cited ranges: nothing this card
  asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.
  `dashboard/src/panels/` route changed since the recorded verification commit. Re-read the card
  against the frozen on-disk source and re-checked its claims and cited ranges: nothing this card
  asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): a route file moved since
  the recorded verification commit — `sprint-graph/styles.ts` gained the `abandoned` frontier
  variant in the dormant tone. Re-read the route card: it makes no claim about that variant, so no
  wording changed. The drift predates this task line (the change landed with an earlier route
  change, not with this master). Verification metadata remains closeout-owned.

  the recorded verification commit — `sprint-graph/styles.ts` gained the `abandoned` frontier
  variant in the dormant tone. Re-read the route card: it makes no claim about that variant, so no
  wording changed. The drift predates this task line (the change landed with an earlier route
  change, not with this master). Verification metadata remains closeout-owned.

  the recorded verification commit — `sprint-graph/styles.ts` gained the `abandoned` frontier
  variant in the dormant tone. Re-read the route card: it makes no claim about that variant, so no
  wording changed. The drift predates this task line (the change landed with an earlier route
  change, not with this master). Verification metadata remains closeout-owned.
  the recorded verification commit — `sprint-graph/styles.ts` gained the `abandoned` frontier
  variant in the dormant tone. Re-read the route card: it makes no claim about that variant, so no
  wording changed. The drift predates this task line (the change landed with an earlier route
  change, not with this master). Verification metadata remains closeout-owned.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `RailChatImpl`, `buildLeafContextPackage`, `findSessionForTask` repointed to dashboard/src/data/sessions.ts:596-608, dashboard/src/panels/RailChat.tsx:255-289, dashboard/src/panels/RailChat.tsx:469-537. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.























- 2026-09-05T07:24+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Corrected current panel paths, status ownership and distinct sub-task row shapes; verified requirement-reader composition. Verification records source review, not execution or acceptance.

- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.











- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.











- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the Hangar fixture gaining lifecycle envelope version literals.















- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the requirement-artifact routing through the detail panel, task reader, and TaskNotes (shared `TaskArtifactReaderTarget` + `TaskRequirementLinks` provider).















- 2026-08-31T09:06+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  the contextual-chat route citations after reviewed source movement; the panels-route ownership
  contract is unchanged. Verification remains closeout-owned.


  the contextual-chat route citations after reviewed source movement; the panels-route ownership
  contract is unchanged. Verification remains closeout-owned.

  the contextual-chat route citations after reviewed source movement; the panels-route ownership
  contract is unchanged. Verification remains closeout-owned.
  the contextual-chat route citations after reviewed source movement; the panels-route ownership
  contract is unchanged. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Recorded projection-only closeout rendering, typed invalid-empty repair
  evidence, graph-less sprint visibility, and distinct discard-before-start audit/progress behavior.


  evidence, graph-less sprint visibility, and distinct discard-before-start audit/progress behavior.

  evidence, graph-less sprint visibility, and distinct discard-before-start audit/progress behavior.
  evidence, graph-less sprint visibility, and distinct discard-before-start audit/progress behavior.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: session-cockpit tests gained async `afterEach` virtualizer-debounce flushes. Verified at code commit e5cb139f.



















- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 adds the sprint-graph child route; DetailPanel mounts the wave-grid view plus the scoped closeout queue on the sprint page. Verified at code commit b7f2c8e2.











- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: the detail panel opens commanded master
  documents from typed `masterRef` rows. Verified at code commit 8071a644.



  documents from typed `masterRef` rows. Verified at code commit 8071a644.

  documents from typed `masterRef` rows. Verified at code commit 8071a644.
  documents from typed `masterRef` rows. Verified at code commit 8071a644.

- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.











- 2026-08-15T02:16:50+02:00 — No route impact: panel test fixtures were extended with the required
  empty `executionWaves` cell after TaskDocNode gained the field. No panel behavior changed in L1.


  empty `executionWaves` cell after TaskDocNode gained the field. No panel behavior changed in L1.

  empty `executionWaves` cell after TaskDocNode gained the field. No panel behavior changed in L1.
  empty `executionWaves` cell after TaskDocNode gained the field. No panel behavior changed in L1.

- 2026-08-14T06:25+02:00 — No route impact: L23's final dashboard delta is confined to the
  session-cockpit child route (shared sprint/master/leaf fixture coverage, rail width containment,
  and deterministic fake-timer cleanup). The panels inventory and ownership remain unchanged;
  verification stays closeout-owned.


  session-cockpit child route (shared sprint/master/leaf fixture coverage, rail width containment,
  and deterministic fake-timer cleanup). The panels inventory and ownership remain unchanged;
  verification stays closeout-owned.

  session-cockpit child route (shared sprint/master/leaf fixture coverage, rail width containment,
  and deterministic fake-timer cleanup). The panels inventory and ownership remain unchanged;
  verification stays closeout-owned.
  session-cockpit child route (shared sprint/master/leaf fixture coverage, rail width containment,
  and deterministic fake-timer cleanup). The panels inventory and ownership remain unchanged;
  verification stays closeout-owned.

- 2026-08-13T12:26+02:00 — L23 live-progress clarification: Hangar now displays the plane-owned
  lifecycle `currentCommand` in the existing operation badge using responsive single-line ellipsis
  plus a full-value title; focused render coverage pins the projection boundary. Verification
  provenance remains closeout-owned.


  lifecycle `currentCommand` in the existing operation badge using responsive single-line ellipsis
  plus a full-value title; focused render coverage pins the projection boundary. Verification
  provenance remains closeout-owned.

  lifecycle `currentCommand` in the existing operation badge using responsive single-line ellipsis
  plus a full-value title; focused render coverage pins the projection boundary. Verification
  provenance remains closeout-owned.
  lifecycle `currentCommand` in the existing operation badge using responsive single-line ellipsis
  plus a full-value title; focused render coverage pins the projection boundary. Verification
  provenance remains closeout-owned.

- 2026-08-13T09:05+02:00 — No route impact: L23's current source delta changes backend lifecycle,
  lineage, runtime packaging, and tests only; `dashboard/src/panels/` has no changed source path and
  its eight-panel UI model remains unchanged. Verification provenance remains closeout-owned.

  lineage, runtime packaging, and tests only; `dashboard/src/panels/` has no changed source path and
  its eight-panel UI model remains unchanged. Verification provenance remains closeout-owned.

  lineage, runtime packaging, and tests only; `dashboard/src/panels/` has no changed source path and
  its eight-panel UI model remains unchanged. Verification provenance remains closeout-owned.
  lineage, runtime packaging, and tests only; `dashboard/src/panels/` has no changed source path and
  its eight-panel UI model remains unchanged. Verification provenance remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented panel routing of source-lineage admission evidence; verification remains closeout-owned.











- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 makes Hangar expose optional durable lifecycle-operation kind, status, and phase as a compact enclosure badge without inventing an operation when none is projected. Verification provenance remains closeout-owned.











- 2026-08-12T04:04+02:00 — Recorded the shared-panel startup invariant exposed by the live dashboard
  repair: an always-mounted Zustand consumer must return a referentially stable selector fallback
  before the first projection. Verification metadata remains pinned until governed closeout.


  repair: an always-mounted Zustand consumer must return a referentially stable selector fallback
  before the first projection. Verification metadata remains pinned until governed closeout.

  repair: an always-mounted Zustand consumer must return a referentially stable selector fallback
  before the first projection. Verification metadata remains pinned until governed closeout.
  repair: an always-mounted Zustand consumer must return a referentially stable selector fallback
  before the first projection. Verification metadata remains pinned until governed closeout.

- 2026-08-11T23:40+02:00 — No route impact: helper extractions in `HighlightComposer.tsx`,
  `RailChat.tsx`, and detail-panel state preserve explicit reliable submission, structural
  document-and-role selection, and pure selected-task projection. Verification metadata remains
  pinned until governed closeout.


  `RailChat.tsx`, and detail-panel state preserve explicit reliable submission, structural
  document-and-role selection, and pure selected-task projection. Verification metadata remains
  pinned until governed closeout.

  `RailChat.tsx`, and detail-panel state preserve explicit reliable submission, structural
  document-and-role selection, and pure selected-task projection. Verification metadata remains
  pinned until governed closeout.
  `RailChat.tsx`, and detail-panel state preserve explicit reliable submission, structural
  document-and-role selection, and pure selected-task projection. Verification metadata remains
  pinned until governed closeout.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the panels route with the
  document-and-role cockpit control surface; affected child overviews own the exact UI behavior.


  document-and-role cockpit control surface; affected child overviews own the exact UI behavior.

  document-and-role cockpit control surface; affected child overviews own the exact UI behavior.
  document-and-role cockpit control surface; affected child overviews own the exact UI behavior.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint-group panel projection and the legacy
  migration boundary. Verification metadata remains pinned until closeout.


  migration boundary. Verification metadata remains pinned until closeout.

  migration boundary. Verification metadata remains pinned until closeout.
  migration boundary. Verification metadata remains pinned until closeout.

- 2026-08-09T22:22+02:00 — No route impact: a test-only scroll-memory teardown repair is
  confined to the conversation timeline fixtures and suites. Panel production surfaces and
  hierarchy remain unchanged; detail lives in the conversation overview.


  confined to the conversation timeline fixtures and suites. Panel production surfaces and
  hierarchy remain unchanged; detail lives in the conversation overview.

  confined to the conversation timeline fixtures and suites. Panel production surfaces and
  hierarchy remain unchanged; detail lives in the conversation overview.
  confined to the conversation timeline fixtures and suites. Panel production surfaces and
  hierarchy remain unchanged; detail lives in the conversation overview.

- 2026-08-09T20:25+02:00 — 260713-TES-L5F2 route impact: replaced shared-panel lifecycle-gate
  answer fixtures with lifecycle-free exact-session interaction-response coverage.


  answer fixtures with lifecycle-free exact-session interaction-response coverage.

  answer fixtures with lifecycle-free exact-session interaction-response coverage.
  answer fixtures with lifecycle-free exact-session interaction-response coverage.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 route impact: route body reviewed and updated for the supervisor -> agent-notifier rename (see the route-specific body section above); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the conversation split absorption and the file-size rail coverage. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Split Layout section (kebab-case folders, canonical entries, parts/styles modules). Verification metadata stays pinned until closeout stamps the code commit.











- 2026-08-04T15:29:35+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound Chats mount/props, lifecycle navigation/reader ownership, and served-fixture seeding to the packet-specified operative spans. Verification metadata unchanged.











- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected panel-route provenance: panels
  consume a generated schema mirror, while fixture builders and the manual snapshot remain measured
  consumers of it. New ranges are explicit scoped fixer output.


  consume a generated schema mirror, while fixture builders and the manual snapshot remain measured
  consumers of it. New ranges are explicit scoped fixer output.

  consume a generated schema mirror, while fixture builders and the manual snapshot remain measured
  consumers of it. New ranges are explicit scoped fixer output.
  consume a generated schema mirror, while fixture builders and the manual snapshot remain measured
  consumers of it. New ranges are explicit scoped fixer output.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations inside the 12:20 entry below, after that module was
  restructured. `L542-L559` → `L552-L569` (`TaskSubTaskRefNode`, ending on `linkedLifecycleId`
  L569) and `L624-L639` → `L634-L649` (`SeriesSubTaskNode`, ending on `createdAt` L649). No body
  claim changed.


  `observer/projection.py` citations inside the 12:20 entry below, after that module was
  restructured. `L542-L559` → `L552-L569` (`TaskSubTaskRefNode`, ending on `linkedLifecycleId`
  L569) and `L624-L639` → `L634-L649` (`SeriesSubTaskNode`, ending on `createdAt` L649). No body
  claim changed.

  `observer/projection.py` citations inside the 12:20 entry below, after that module was
  restructured. `L542-L559` → `L552-L569` (`TaskSubTaskRefNode`, ending on `linkedLifecycleId`
  L569) and `L624-L639` → `L634-L649` (`SeriesSubTaskNode`, ending on `createdAt` L649). No body
  claim changed.
  `observer/projection.py` citations inside the 12:20 entry below, after that module was
  restructured. `L542-L559` → `L552-L569` (`TaskSubTaskRefNode`, ending on `linkedLifecycleId`
  L569) and `L624-L639` → `L634-L649` (`SeriesSubTaskNode`, ending on `createdAt` L649). No body
  claim changed.

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), body only. "What the fixture
  conversion does and does not pin" said *"`fixture ⊆ mirror` is what the dashboard tests enforce.
  `mirror ⊆ server` is enforced by nothing"* — the outer two nodes of a four-node chain, which reads as
  though nothing measures the mirror against the snapshot. It does: `test/contract.test.ts` measures
  `types/projection.ts` against `fixtures/snapshot.json` in three TYPE-level directions
  (`mirror ⊇ served`, `served ⊇ mirror`, `fixture ⊇ mirror` — L29-L53) plus runtime `VOCABULARIES`
  assertions (L269, L348, L368) for the string unions `resolveJsonModule` widens to `string`. The
  paragraph now names all three links and states the unheld one as **`snapshot.json` ↔
  `observer/projection.py`, by hand** rather than as "`mirror ⊆ server`" — one letter from
  "`mirror ⊆ served`", which *is* enforced. Also brought the no-generator claim to the strength the
  evidence carries: no in-repo generator **and no in-repo mechanism keeping the two sides in step**.
  Same correction applied to the 12:20 entry's restatement below. No component claim, table row, or
  verification field changed.


  conversion does and does not pin" said *"`fixture ⊆ mirror` is what the dashboard tests enforce.
  `mirror ⊆ server` is enforced by nothing"* — the outer two nodes of a four-node chain, which reads as
  though nothing measures the mirror against the snapshot. It does: `test/contract.test.ts` measures
  `types/projection.ts` against `fixtures/snapshot.json` in three TYPE-level directions
  (`mirror ⊇ served`, `served ⊇ mirror`, `fixture ⊇ mirror` — L29-L53) plus runtime `VOCABULARIES`
  assertions (L269, L348, L368) for the string unions `resolveJsonModule` widens to `string`. The
  paragraph now names all three links and states the unheld one as **`snapshot.json` ↔
  `observer/projection.py`, by hand** rather than as "`mirror ⊆ server`" — one letter from
  "`mirror ⊆ served`", which *is* enforced. Also brought the no-generator claim to the strength the
  evidence carries: no in-repo generator **and no in-repo mechanism keeping the two sides in step**.
  Same correction applied to the 12:20 entry's restatement below. No component claim, table row, or
  verification field changed.

  conversion does and does not pin" said *"`fixture ⊆ mirror` is what the dashboard tests enforce.
  `mirror ⊆ server` is enforced by nothing"* — the outer two nodes of a four-node chain, which reads as
  though nothing measures the mirror against the snapshot. It does: `test/contract.test.ts` measures
  `types/projection.ts` against `fixtures/snapshot.json` in three TYPE-level directions
  (`mirror ⊇ served`, `served ⊇ mirror`, `fixture ⊇ mirror` — L29-L53) plus runtime `VOCABULARIES`
  assertions (L269, L348, L368) for the string unions `resolveJsonModule` widens to `string`. The
  paragraph now names all three links and states the unheld one as **`snapshot.json` ↔
  `observer/projection.py`, by hand** rather than as "`mirror ⊆ server`" — one letter from
  "`mirror ⊆ served`", which *is* enforced. Also brought the no-generator claim to the strength the
  evidence carries: no in-repo generator **and no in-repo mechanism keeping the two sides in step**.
  Same correction applied to the 12:20 entry's restatement below. No component claim, table row, or
  verification field changed.
  conversion does and does not pin" said *"`fixture ⊆ mirror` is what the dashboard tests enforce.
  `mirror ⊆ server` is enforced by nothing"* — the outer two nodes of a four-node chain, which reads as
  though nothing measures the mirror against the snapshot. It does: `test/contract.test.ts` measures
  `types/projection.ts` against `fixtures/snapshot.json` in three TYPE-level directions
  (`mirror ⊇ served`, `served ⊇ mirror`, `fixture ⊇ mirror` — L29-L53) plus runtime `VOCABULARIES`
  assertions (L269, L348, L368) for the string unions `resolveJsonModule` widens to `string`. The
  paragraph now names all three links and states the unheld one as **`snapshot.json` ↔
  `observer/projection.py`, by hand** rather than as "`mirror ⊆ server`" — one letter from
  "`mirror ⊆ served`", which *is* enforced. Also brought the no-generator claim to the strength the
  evidence carries: no in-repo generator **and no in-repo mechanism keeping the two sides in step**.
  Same correction applied to the 12:20 entry's restatement below. No component claim, table row, or
  verification field changed.

- 2026-08-01T12:20+02:00 — 260731-EFA-L4 route impact (wire contracts and typed vocabularies): added
  the "Typed Vocabulary Route Impact" section. Both component changes in this route are real, not
  incidental. `AttentionQueue.tsx` gained the `role="img"` `severityMark` wrapper because `Dot` is
  `aria-hidden` and a bare-span `aria-label` names a `generic` (ARIA-prohibited; axe-core
  `aria-prohibited-attr`, `serious`) — recorded as a route-wide rule with the reason `LifecycleList`
  needs no role (React Aria `role="option"` name-from-content). `LifecycleList.tsx`'s `statusVariant`
  lost its `blocked`/`paused`/`abandoned` arms; I verified this is behaviour-identical by reading both
  call sites (`docRow` L595, `seriesRow` L644 — `lifecycle?.state ?? statusVariant(...)`, so the live
  state never reaches the map) and the input vocabulary end to end
  (`tasks/document.py::DocStatus` L30 = planning/inProgress/Completed → `snapshots.py` `status=doc.status`
  at L1304 for `SeriesNode` and L1398 for `TaskDocNode`). Recorded `awaiting-developer` as a LIVE state
  of the server-side partition (`observer/lifecycle_state.py`) with the two new `LifecycleList.test.tsx`
  handover regressions, `Metrics extends LifecycleStateCounts` with `metricsFor` replacing hand-listed
  buckets, and the `SubTaskRow` union with the two `extra="forbid"` server models it unions
  (`projection.py` L552-L569 `TaskSubTaskRefNode` — no `createdAt`; L634-L649 `SeriesSubTaskNode` — no
  `linkedLifecycleId`), which is why the `→` cross-series jump is master-task-doc-only and why the
  creation sort moved to `seriesAsMasterDoc`. Stated the fixture chain's honest reach: `wire.ts` and
  `snapshot.json` are hand-maintained with no generator anywhere in this repository, the fixture→mirror
  and mirror→snapshot links are both test-enforced, and the `snapshot.json` ↔ `observer/projection.py`
  crossing is held by nothing. (This bullet originally read "`fixture ⊆ mirror` is test-enforced and
  `mirror ⊆ server` is enforced by nothing", which dropped the middle link; corrected in the 14:05
  entry.) Added four two-cell
  `Repo-Internal References` rows (this table is two columns; no ranges added to it). Evidence: the six
  suites over this route's files run green (106 tests). Verification metadata pinned until closeout
  stamps the commit.


  the "Typed Vocabulary Route Impact" section. Both component changes in this route are real, not
  incidental. `AttentionQueue.tsx` gained the `role="img"` `severityMark` wrapper because `Dot` is
  `aria-hidden` and a bare-span `aria-label` names a `generic` (ARIA-prohibited; axe-core
  `aria-prohibited-attr`, `serious`) — recorded as a route-wide rule with the reason `LifecycleList`
  needs no role (React Aria `role="option"` name-from-content). `LifecycleList.tsx`'s `statusVariant`
  lost its `blocked`/`paused`/`abandoned` arms; I verified this is behaviour-identical by reading both
  call sites (`docRow` L595, `seriesRow` L644 — `lifecycle?.state ?? statusVariant(...)`, so the live
  state never reaches the map) and the input vocabulary end to end
  (`tasks/document.py::DocStatus` L30 = planning/inProgress/Completed → `snapshots.py` `status=doc.status`
  at L1304 for `SeriesNode` and L1398 for `TaskDocNode`). Recorded `awaiting-developer` as a LIVE state
  of the server-side partition (`observer/lifecycle_state.py`) with the two new `LifecycleList.test.tsx`
  handover regressions, `Metrics extends LifecycleStateCounts` with `metricsFor` replacing hand-listed
  buckets, and the `SubTaskRow` union with the two `extra="forbid"` server models it unions
  (`projection.py` L552-L569 `TaskSubTaskRefNode` — no `createdAt`; L634-L649 `SeriesSubTaskNode` — no
  `linkedLifecycleId`), which is why the `→` cross-series jump is master-task-doc-only and why the
  creation sort moved to `seriesAsMasterDoc`. Stated the fixture chain's honest reach: `wire.ts` and
  `snapshot.json` are hand-maintained with no generator anywhere in this repository, the fixture→mirror
  and mirror→snapshot links are both test-enforced, and the `snapshot.json` ↔ `observer/projection.py`
  crossing is held by nothing. (This bullet originally read "`fixture ⊆ mirror` is test-enforced and
  `mirror ⊆ server` is enforced by nothing", which dropped the middle link; corrected in the 14:05
  entry.) Added four two-cell
  `Repo-Internal References` rows (this table is two columns; no ranges added to it). Evidence: the six
  suites over this route's files run green (106 tests). Verification metadata pinned until closeout
  stamps the commit.

  the "Typed Vocabulary Route Impact" section. Both component changes in this route are real, not
  incidental. `AttentionQueue.tsx` gained the `role="img"` `severityMark` wrapper because `Dot` is
  `aria-hidden` and a bare-span `aria-label` names a `generic` (ARIA-prohibited; axe-core
  `aria-prohibited-attr`, `serious`) — recorded as a route-wide rule with the reason `LifecycleList`
  needs no role (React Aria `role="option"` name-from-content). `LifecycleList.tsx`'s `statusVariant`
  lost its `blocked`/`paused`/`abandoned` arms; I verified this is behaviour-identical by reading both
  call sites (`docRow` L595, `seriesRow` L644 — `lifecycle?.state ?? statusVariant(...)`, so the live
  state never reaches the map) and the input vocabulary end to end
  (`tasks/document.py::DocStatus` L30 = planning/inProgress/Completed → `snapshots.py` `status=doc.status`
  at L1304 for `SeriesNode` and L1398 for `TaskDocNode`). Recorded `awaiting-developer` as a LIVE state
  of the server-side partition (`observer/lifecycle_state.py`) with the two new `LifecycleList.test.tsx`
  handover regressions, `Metrics extends LifecycleStateCounts` with `metricsFor` replacing hand-listed
  buckets, and the `SubTaskRow` union with the two `extra="forbid"` server models it unions
  (`projection.py` L552-L569 `TaskSubTaskRefNode` — no `createdAt`; L634-L649 `SeriesSubTaskNode` — no
  `linkedLifecycleId`), which is why the `→` cross-series jump is master-task-doc-only and why the
  creation sort moved to `seriesAsMasterDoc`. Stated the fixture chain's honest reach: `wire.ts` and
  `snapshot.json` are hand-maintained with no generator anywhere in this repository, the fixture→mirror
  and mirror→snapshot links are both test-enforced, and the `snapshot.json` ↔ `observer/projection.py`
  crossing is held by nothing. (This bullet originally read "`fixture ⊆ mirror` is test-enforced and
  `mirror ⊆ server` is enforced by nothing", which dropped the middle link; corrected in the 14:05
  entry.) Added four two-cell
  `Repo-Internal References` rows (this table is two columns; no ranges added to it). Evidence: the six
  suites over this route's files run green (106 tests). Verification metadata pinned until closeout
  stamps the commit.
  the "Typed Vocabulary Route Impact" section. Both component changes in this route are real, not
  incidental. `AttentionQueue.tsx` gained the `role="img"` `severityMark` wrapper because `Dot` is
  `aria-hidden` and a bare-span `aria-label` names a `generic` (ARIA-prohibited; axe-core
  `aria-prohibited-attr`, `serious`) — recorded as a route-wide rule with the reason `LifecycleList`
  needs no role (React Aria `role="option"` name-from-content). `LifecycleList.tsx`'s `statusVariant`
  lost its `blocked`/`paused`/`abandoned` arms; I verified this is behaviour-identical by reading both
  call sites (`docRow` L595, `seriesRow` L644 — `lifecycle?.state ?? statusVariant(...)`, so the live
  state never reaches the map) and the input vocabulary end to end
  (`tasks/document.py::DocStatus` L30 = planning/inProgress/Completed → `snapshots.py` `status=doc.status`
  at L1304 for `SeriesNode` and L1398 for `TaskDocNode`). Recorded `awaiting-developer` as a LIVE state
  of the server-side partition (`observer/lifecycle_state.py`) with the two new `LifecycleList.test.tsx`
  handover regressions, `Metrics extends LifecycleStateCounts` with `metricsFor` replacing hand-listed
  buckets, and the `SubTaskRow` union with the two `extra="forbid"` server models it unions
  (`projection.py` L552-L569 `TaskSubTaskRefNode` — no `createdAt`; L634-L649 `SeriesSubTaskNode` — no
  `linkedLifecycleId`), which is why the `→` cross-series jump is master-task-doc-only and why the
  creation sort moved to `seriesAsMasterDoc`. Stated the fixture chain's honest reach: `wire.ts` and
  `snapshot.json` are hand-maintained with no generator anywhere in this repository, the fixture→mirror
  and mirror→snapshot links are both test-enforced, and the `snapshot.json` ↔ `observer/projection.py`
  crossing is held by nothing. (This bullet originally read "`fixture ⊆ mirror` is test-enforced and
  `mirror ⊆ server` is enforced by nothing", which dropped the middle link; corrected in the 14:05
  entry.) Added four two-cell
  `Repo-Internal References` rows (this table is two columns; no ranges added to it). Evidence: the six
  suites over this route's files run green (106 tests). Verification metadata pinned until closeout
  stamps the commit.

- 2026-07-30T12:51+02:00 — No route-model impact for 260727-CHATS-IM-L2. The
  Engine Room effects-root isolation is governed by the `engine-room/` child overview and the
  selected-child history surface by `session-cockpit/`; the panels inventory and ownership split
  remain unchanged. Verification metadata remains pinned until closeout.


  Engine Room effects-root isolation is governed by the `engine-room/` child overview and the
  selected-child history surface by `session-cockpit/`; the panels inventory and ownership split
  remain unchanged. Verification metadata remains pinned until closeout.

  Engine Room effects-root isolation is governed by the `engine-room/` child overview and the
  selected-child history surface by `session-cockpit/`; the panels inventory and ownership split
  remain unchanged. Verification metadata remains pinned until closeout.
  Engine Room effects-root isolation is governed by the `engine-room/` child overview and the
  selected-child history surface by `session-cockpit/`; the panels inventory and ownership split
  remain unchanged. Verification metadata remains pinned until closeout.

- 2026-07-24T13:17:17Z — Curator: documented cross-panel persistent-subtree memoization and the
  current evidence/placement conventions introduced by this route's owned sources. Verification
  metadata remains pre-commit.


  current evidence/placement conventions introduced by this route's owned sources. Verification
  metadata remains pre-commit.

  current evidence/placement conventions introduced by this route's owned sources. Verification
  metadata remains pre-commit.
  current evidence/placement conventions introduced by this route's owned sources. Verification
  metadata remains pre-commit.

- 2026-07-21T11:30+02:00 — No route impact: the `dashboard/src/panels` route model is unchanged by
  260718-CHATS-L5F (half-time functional fixes, PASS-WITH-NOTES). No DIRECT `panels/` child changed;
  the leaf's single panels-tree edit is `session-cockpit/SessionsView.tsx` (the R9 focused-seat
  live-turn merge), governed by the [session-cockpit/](session-cockpit/overview.md) child route and
  recorded there and in its sidecar. Verification metadata advances with closeout stamping only.
  260718-CHATS-L5P (cockpit chrome visual polish, PASS-WITH-NOTES; dashboard-only, zero backend edits).
  Two DIRECT `panels/` children got styling polish captured in their own sidecars, not this route body:
  `SessionComposer.tsx` — the editor frame joins the terminal `well` (FB7.1) + gains a `:focus-within`
  amber ring (V4), the footer hint is capability-derived on legacy-raw terminal seats (V9), `draft saved`
  is exception-only (V14), and the send button holds width/single-line under the inspector (V3);
  `Terminal.tsx` — the host `background` `#070b0f` literal migrated to the `well` token (V31). The bulk of
  the leaf's chrome polish lives under [session-cockpit/](session-cockpit/overview.md) (its "Cockpit chrome
  conventions" section). Verification metadata unchanged.

  260718-CHATS-L5F (half-time functional fixes, PASS-WITH-NOTES). No DIRECT `panels/` child changed;
  the leaf's single panels-tree edit is `session-cockpit/SessionsView.tsx` (the R9 focused-seat
  live-turn merge), governed by the [session-cockpit/](session-cockpit/overview.md) child route and
  recorded there and in its sidecar. Verification metadata advances with closeout stamping only.
  260718-CHATS-L5P (cockpit chrome visual polish, PASS-WITH-NOTES; dashboard-only, zero backend edits).
  Two DIRECT `panels/` children got styling polish captured in their own sidecars, not this route body:
  `SessionComposer.tsx` — the editor frame joins the terminal `well` (FB7.1) + gains a `:focus-within`
  amber ring (V4), the footer hint is capability-derived on legacy-raw terminal seats (V9), `draft saved`
  is exception-only (V14), and the send button holds width/single-line under the inspector (V3);
  `Terminal.tsx` — the host `background` `#070b0f` literal migrated to the `well` token (V31). The bulk of
  the leaf's chrome polish lives under [session-cockpit/](session-cockpit/overview.md) (its "Cockpit chrome
  conventions" section). Verification metadata unchanged.

  260718-CHATS-L5F (half-time functional fixes, PASS-WITH-NOTES). No DIRECT `panels/` child changed;
  the leaf's single panels-tree edit is `session-cockpit/SessionsView.tsx` (the R9 focused-seat
  live-turn merge), governed by the [session-cockpit/](session-cockpit/overview.md) child route and
  recorded there and in its sidecar. Verification metadata advances with closeout stamping only.
  260718-CHATS-L5P (cockpit chrome visual polish, PASS-WITH-NOTES; dashboard-only, zero backend edits).
  Two DIRECT `panels/` children got styling polish captured in their own sidecars, not this route body:
  `SessionComposer.tsx` — the editor frame joins the terminal `well` (FB7.1) + gains a `:focus-within`
  amber ring (V4), the footer hint is capability-derived on legacy-raw terminal seats (V9), `draft saved`
  is exception-only (V14), and the send button holds width/single-line under the inspector (V3);
  `Terminal.tsx` — the host `background` `#070b0f` literal migrated to the `well` token (V31). The bulk of
  the leaf's chrome polish lives under [session-cockpit/](session-cockpit/overview.md) (its "Cockpit chrome
  conventions" section). Verification metadata unchanged.
  260718-CHATS-L5F (half-time functional fixes, PASS-WITH-NOTES). No DIRECT `panels/` child changed;
  the leaf's single panels-tree edit is `session-cockpit/SessionsView.tsx` (the R9 focused-seat
  live-turn merge), governed by the [session-cockpit/](session-cockpit/overview.md) child route and
  recorded there and in its sidecar. Verification metadata advances with closeout stamping only.
  260718-CHATS-L5P (cockpit chrome visual polish, PASS-WITH-NOTES; dashboard-only, zero backend edits).
  Two DIRECT `panels/` children got styling polish captured in their own sidecars, not this route body:
  `SessionComposer.tsx` — the editor frame joins the terminal `well` (FB7.1) + gains a `:focus-within`
  amber ring (V4), the footer hint is capability-derived on legacy-raw terminal seats (V9), `draft saved`
  is exception-only (V14), and the send button holds width/single-line under the inspector (V3);
  `Terminal.tsx` — the host `background` `#070b0f` literal migrated to the `well` token (V31). The bulk of
  the leaf's chrome polish lives under [session-cockpit/](session-cockpit/overview.md) (its "Cockpit chrome
  conventions" section). Verification metadata unchanged.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 route impact (structured Chats renderer, reviewer FINAL
  PASS): corrected the stale shared-panel claims — the controlled-session runner line-log is now the
  read-only terminal-diagnostics drawer + legacy-raw body (the structured `ConversationSurface` is the
  controlled default), and UA-1 history/index/resume is landed as a reconstructable projection with no
  durable browser conversation index. The two new `conversation/` and `conversation-library/`
  grandchild routes are governed by the [session-cockpit](session-cockpit/overview.md) overview; this
  compact parent's route inventory is otherwise unchanged. `SessionComposer.tsx`'s L4 change is a
  presentation-only hint-line regrouping (no authority change). Verification metadata remains pinned
  pending L4 candidate closeout.


  PASS): corrected the stale shared-panel claims — the controlled-session runner line-log is now the
  read-only terminal-diagnostics drawer + legacy-raw body (the structured `ConversationSurface` is the
  controlled default), and UA-1 history/index/resume is landed as a reconstructable projection with no
  durable browser conversation index. The two new `conversation/` and `conversation-library/`
  grandchild routes are governed by the [session-cockpit](session-cockpit/overview.md) overview; this
  compact parent's route inventory is otherwise unchanged. `SessionComposer.tsx`'s L4 change is a
  presentation-only hint-line regrouping (no authority change). Verification metadata remains pinned
  pending L4 candidate closeout.

  PASS): corrected the stale shared-panel claims — the controlled-session runner line-log is now the
  read-only terminal-diagnostics drawer + legacy-raw body (the structured `ConversationSurface` is the
  controlled default), and UA-1 history/index/resume is landed as a reconstructable projection with no
  durable browser conversation index. The two new `conversation/` and `conversation-library/`
  grandchild routes are governed by the [session-cockpit](session-cockpit/overview.md) overview; this
  compact parent's route inventory is otherwise unchanged. `SessionComposer.tsx`'s L4 change is a
  presentation-only hint-line regrouping (no authority change). Verification metadata remains pinned
  pending L4 candidate closeout.
  PASS): corrected the stale shared-panel claims — the controlled-session runner line-log is now the
  read-only terminal-diagnostics drawer + legacy-raw body (the structured `ConversationSurface` is the
  controlled default), and UA-1 history/index/resume is landed as a reconstructable projection with no
  durable browser conversation index. The two new `conversation/` and `conversation-library/`
  grandchild routes are governed by the [session-cockpit](session-cockpit/overview.md) overview; this
  compact parent's route inventory is otherwise unchanged. `SessionComposer.tsx`'s L4 change is a
  presentation-only hint-line regrouping (no authority change). Verification metadata remains pinned
  pending L4 candidate closeout.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2: recorded visible create failures and accepted-row gates
  for HighlightComposer and RailChat, including zero context delivery and zero private row/focus
  mutation on failure. Verification metadata remains pinned pending candidate closeout.


  for HighlightComposer and RailChat, including zero context delivery and zero private row/focus
  mutation on failure. Verification metadata remains pinned pending candidate closeout.

  for HighlightComposer and RailChat, including zero context delivery and zero private row/focus
  mutation on failure. Verification metadata remains pinned pending candidate closeout.
  for HighlightComposer and RailChat, including zero context delivery and zero private row/focus
  mutation on failure. Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded xterm-preserving boot reattach, bounded chooser
  recovery, and empty-narrow entrance preservation. Verification metadata remains pinned pending
  candidate closeout.


  recovery, and empty-narrow entrance preservation. Verification metadata remains pinned pending
  candidate closeout.

  recovery, and empty-narrow entrance preservation. Verification metadata remains pinned pending
  candidate closeout.
  recovery, and empty-narrow entrance preservation. Verification metadata remains pinned pending
  candidate closeout.

- 2026-07-18T07:22+02:00 — 260715-FEUI-L8 strategic refactor: reduced this packed parent to
  composition boundaries, made session-cockpit the sole Chats owner, routed data-plane detail to
  the new data overview, and recorded legacy retirement without claiming the future structured
  conversation UI. Metadata remains pinned to the leaf base.


  composition boundaries, made session-cockpit the sole Chats owner, routed data-plane detail to
  the new data overview, and recorded legacy retirement without claiming the future structured
  conversation UI. Metadata remains pinned to the leaf base.

  composition boundaries, made session-cockpit the sole Chats owner, routed data-plane detail to
  the new data overview, and recorded legacy retirement without claiming the future structured
  conversation UI. Metadata remains pinned to the leaf base.
  composition boundaries, made session-cockpit the sole Chats owner, routed data-plane detail to
  the new data overview, and recorded legacy retirement without claiming the future structured
  conversation UI. Metadata remains pinned to the leaf base.

- 2026-07-18T00:08+02:00 — 260715-FEUI-L7 curator closeout delta: replaced the interim inspector
  scaffolding with the stable-mounted Evidence/Capabilities/Bus host, documented explicit mark-seen
  and post-removal residual behavior, separated exact-session capability truth, recorded fleet Bus
  sender-only reply and entry-state/virtualization invariants, and added the honest ordered StatusLine.
  Detailed component and test routing remains in the `session-cockpit/` child overview.

  scaffolding with the stable-mounted Evidence/Capabilities/Bus host, documented explicit mark-seen
  and post-removal residual behavior, separated exact-session capability truth, recorded fleet Bus
  sender-only reply and entry-state/virtualization invariants, and added the honest ordered StatusLine.
  Detailed component and test routing remains in the `session-cockpit/` child overview.

  scaffolding with the stable-mounted Evidence/Capabilities/Bus host, documented explicit mark-seen
  and post-removal residual behavior, separated exact-session capability truth, recorded fleet Bus
  sender-only reply and entry-state/virtualization invariants, and added the honest ordered StatusLine.
  Detailed component and test routing remains in the `session-cockpit/` child overview.
  scaffolding with the stable-mounted Evidence/Capabilities/Bus host, documented explicit mark-seen
  and post-removal residual behavior, separated exact-session capability truth, recorded fleet Bus
  sender-only reply and entry-state/virtualization invariants, and added the honest ordered StatusLine.
  Detailed component and test routing remains in the `session-cockpit/` child overview.

- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced current bracketed/draft-paste
  descriptions for SessionComposer, RailChat leaf context, and HighlightComposer with the shared
  epoch-bound reliable-submit path, provenance, create-ready handling, and the raw-PTY boundary.

  descriptions for SessionComposer, RailChat leaf context, and HighlightComposer with the shared
  epoch-bound reliable-submit path, provenance, create-ready handling, and the raw-PTY boundary.

  descriptions for SessionComposer, RailChat leaf context, and HighlightComposer with the shared
  epoch-bound reliable-submit path, provenance, create-ready handling, and the raw-PTY boundary.
  descriptions for SessionComposer, RailChat leaf context, and HighlightComposer with the shared
  epoch-bound reliable-submit path, provenance, create-ready handling, and the raw-PTY boundary.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 route impact: the `session-cockpit/` child route gains
  `ModelEffortControl`, `AcceptanceChip`, `CockpitLiveRegions`, and `SetOutcomeToasts` with their
  focused suites; existing HeaderStrip/SeatInspector/SessionRail/SessionsView surfaces gain the
  one control, collapsed acknowledging ledger, worded rail attention/named dots, cycle-effort,
  queued hint, watchers, and persistent outcome plumbing. Pure policy and I/O remain in the L4
  `data/` layer named above. No other panel or MCP package-data route changed because the worker
  did not run dashboard bundle sync. Verification metadata is pinned to the contract base until
  code commit.

  `ModelEffortControl`, `AcceptanceChip`, `CockpitLiveRegions`, and `SetOutcomeToasts` with their
  focused suites; existing HeaderStrip/SeatInspector/SessionRail/SessionsView surfaces gain the
  one control, collapsed acknowledging ledger, worded rail attention/named dots, cycle-effort,
  queued hint, watchers, and persistent outcome plumbing. Pure policy and I/O remain in the L4
  `data/` layer named above. No other panel or MCP package-data route changed because the worker
  did not run dashboard bundle sync. Verification metadata is pinned to the contract base until
  code commit.

  `ModelEffortControl`, `AcceptanceChip`, `CockpitLiveRegions`, and `SetOutcomeToasts` with their
  focused suites; existing HeaderStrip/SeatInspector/SessionRail/SessionsView surfaces gain the
  one control, collapsed acknowledging ledger, worded rail attention/named dots, cycle-effort,
  queued hint, watchers, and persistent outcome plumbing. Pure policy and I/O remain in the L4
  `data/` layer named above. No other panel or MCP package-data route changed because the worker
  did not run dashboard bundle sync. Verification metadata is pinned to the contract base until
  code commit.
  `ModelEffortControl`, `AcceptanceChip`, `CockpitLiveRegions`, and `SetOutcomeToasts` with their
  focused suites; existing HeaderStrip/SeatInspector/SessionRail/SessionsView surfaces gain the
  one control, collapsed acknowledging ledger, worded rail attention/named dots, cycle-effort,
  queued hint, watchers, and persistent outcome plumbing. Pure policy and I/O remain in the L4
  `data/` layer named above. No other panel or MCP package-data route changed because the worker
  did not run dashboard bundle sync. Verification metadata is pinned to the contract base until
  code commit.

- 2026-07-17T06:30+02:00 — 260715-FEUI-L3 route impact (capability catalog client and launch
  flow): the `session-cockpit/` child route gains its LAUNCH layer — `LaunchFlow.tsx` (the
  palette-opened catalog-driven launch overlay) + `FailedLaunchBanner.tsx` (verbatim failed-seat
  refusal surface) with their jsdom suites; `SessionsView` registers `session.launch` and mounts
  both (pure appends); `HeaderStrip`/`SeatInspector` derive the R7 evidence tier from row
  control-state truth and render `grammar/EvidenceBadge`; `SessionStage`'s empty-state copy
  points at the palette launcher. No OTHER panel changed in this leaf (Chats/Terminal untouched).
  Detail lives in the `session-cockpit/` overview and the touched sidecars. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.

  flow): the `session-cockpit/` child route gains its LAUNCH layer — `LaunchFlow.tsx` (the
  palette-opened catalog-driven launch overlay) + `FailedLaunchBanner.tsx` (verbatim failed-seat
  refusal surface) with their jsdom suites; `SessionsView` registers `session.launch` and mounts
  both (pure appends); `HeaderStrip`/`SeatInspector` derive the R7 evidence tier from row
  control-state truth and render `grammar/EvidenceBadge`; `SessionStage`'s empty-state copy
  points at the palette launcher. No OTHER panel changed in this leaf (Chats/Terminal untouched).
  Detail lives in the `session-cockpit/` overview and the touched sidecars. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.

  flow): the `session-cockpit/` child route gains its LAUNCH layer — `LaunchFlow.tsx` (the
  palette-opened catalog-driven launch overlay) + `FailedLaunchBanner.tsx` (verbatim failed-seat
  refusal surface) with their jsdom suites; `SessionsView` registers `session.launch` and mounts
  both (pure appends); `HeaderStrip`/`SeatInspector` derive the R7 evidence tier from row
  control-state truth and render `grammar/EvidenceBadge`; `SessionStage`'s empty-state copy
  points at the palette launcher. No OTHER panel changed in this leaf (Chats/Terminal untouched).
  Detail lives in the `session-cockpit/` overview and the touched sidecars. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.
  flow): the `session-cockpit/` child route gains its LAUNCH layer — `LaunchFlow.tsx` (the
  palette-opened catalog-driven launch overlay) + `FailedLaunchBanner.tsx` (verbatim failed-seat
  refusal surface) with their jsdom suites; `SessionsView` registers `session.launch` and mounts
  both (pure appends); `HeaderStrip`/`SeatInspector` derive the R7 evidence tier from row
  control-state truth and render `grammar/EvidenceBadge`; `SessionStage`'s empty-state copy
  points at the palette launcher. No OTHER panel changed in this leaf (Chats/Terminal untouched).
  Detail lives in the `session-cockpit/` overview and the touched sidecars. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 route impact (PTY stage surface, structured
  interactions, session lifecycle actions): the `session-cockpit/` child route gains
  `PtySurface`/`InteractionBar`/`WorkingLine`/`StopResidualNotes`/`lifecycleCopy` (+ four jsdom
  suites) — the stage body is filled with keep-alive real xterm panes (DOM renderer by
  measurement) and the gate-only interaction bar; `Terminal.tsx` gains additive optional props
  (renderer seam with lazy webgl escalation, screenReaderMode live options mutation, observe-only
  harvesting hooks, keyEventFilter, onResizeCols, ariaLabel) with byte-compatible defaults for
  the legacy call sites, plus a guaranteed named `role="group"` landmark (sessionId fallback);
  `Chats.tsx`/`RailChat.tsx` pass real `ariaLabel`s at their Terminal call sites (one prop per
  call site — review F6). No panel was removed; per-file detail lives in the sidecars and the
  `session-cockpit/` overview. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.

  interactions, session lifecycle actions): the `session-cockpit/` child route gains
  `PtySurface`/`InteractionBar`/`WorkingLine`/`StopResidualNotes`/`lifecycleCopy` (+ four jsdom
  suites) — the stage body is filled with keep-alive real xterm panes (DOM renderer by
  measurement) and the gate-only interaction bar; `Terminal.tsx` gains additive optional props
  (renderer seam with lazy webgl escalation, screenReaderMode live options mutation, observe-only
  harvesting hooks, keyEventFilter, onResizeCols, ariaLabel) with byte-compatible defaults for
  the legacy call sites, plus a guaranteed named `role="group"` landmark (sessionId fallback);
  `Chats.tsx`/`RailChat.tsx` pass real `ariaLabel`s at their Terminal call sites (one prop per
  call site — review F6). No panel was removed; per-file detail lives in the sidecars and the
  `session-cockpit/` overview. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.

  interactions, session lifecycle actions): the `session-cockpit/` child route gains
  `PtySurface`/`InteractionBar`/`WorkingLine`/`StopResidualNotes`/`lifecycleCopy` (+ four jsdom
  suites) — the stage body is filled with keep-alive real xterm panes (DOM renderer by
  measurement) and the gate-only interaction bar; `Terminal.tsx` gains additive optional props
  (renderer seam with lazy webgl escalation, screenReaderMode live options mutation, observe-only
  harvesting hooks, keyEventFilter, onResizeCols, ariaLabel) with byte-compatible defaults for
  the legacy call sites, plus a guaranteed named `role="group"` landmark (sessionId fallback);
  `Chats.tsx`/`RailChat.tsx` pass real `ariaLabel`s at their Terminal call sites (one prop per
  call site — review F6). No panel was removed; per-file detail lives in the sidecars and the
  `session-cockpit/` overview. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.
  interactions, session lifecycle actions): the `session-cockpit/` child route gains
  `PtySurface`/`InteractionBar`/`WorkingLine`/`StopResidualNotes`/`lifecycleCopy` (+ four jsdom
  suites) — the stage body is filled with keep-alive real xterm panes (DOM renderer by
  measurement) and the gate-only interaction bar; `Terminal.tsx` gains additive optional props
  (renderer seam with lazy webgl escalation, screenReaderMode live options mutation, observe-only
  harvesting hooks, keyEventFilter, onResizeCols, ariaLabel) with byte-compatible defaults for
  the legacy call sites, plus a guaranteed named `role="group"` landmark (sessionId fallback);
  `Chats.tsx`/`RailChat.tsx` pass real `ariaLabel`s at their Terminal call sites (one prop per
  call site — review F6). No panel was removed; per-file detail lives in the sidecars and the
  `session-cockpit/` overview. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.

- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 route impact (session data layer, rail, and stage
  container): the `session-cockpit/` child route is FILLED — `SessionRail`/`SessionStage`/
  `HeaderStrip`/`StateDot`/`SeatInspector` (+ two jsdom suites) land and `SessionsView` becomes
  the once-derived model/rollup seam with smart-default focus, focus handoff, and dynamic palette
  commands; `Chats.tsx` hands its 2.5s catalog poll to the shared `data/catalogPoll.ts` driver
  (consumer semantics byte-equivalent); `file-viewer/FileViewer.tsx` gains a reviewer-accepted
  one-line defensive repos-catalog guard. Detail lives in the `session-cockpit/` overview and the
  touched sidecars; no panel was removed. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.

  container): the `session-cockpit/` child route is FILLED — `SessionRail`/`SessionStage`/
  `HeaderStrip`/`StateDot`/`SeatInspector` (+ two jsdom suites) land and `SessionsView` becomes
  the once-derived model/rollup seam with smart-default focus, focus handoff, and dynamic palette
  commands; `Chats.tsx` hands its 2.5s catalog poll to the shared `data/catalogPoll.ts` driver
  (consumer semantics byte-equivalent); `file-viewer/FileViewer.tsx` gains a reviewer-accepted
  one-line defensive repos-catalog guard. Detail lives in the `session-cockpit/` overview and the
  touched sidecars; no panel was removed. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.

  container): the `session-cockpit/` child route is FILLED — `SessionRail`/`SessionStage`/
  `HeaderStrip`/`StateDot`/`SeatInspector` (+ two jsdom suites) land and `SessionsView` becomes
  the once-derived model/rollup seam with smart-default focus, focus handoff, and dynamic palette
  commands; `Chats.tsx` hands its 2.5s catalog poll to the shared `data/catalogPoll.ts` driver
  (consumer semantics byte-equivalent); `file-viewer/FileViewer.tsx` gains a reviewer-accepted
  one-line defensive repos-catalog guard. Detail lives in the `session-cockpit/` overview and the
  touched sidecars; no panel was removed. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
  container): the `session-cockpit/` child route is FILLED — `SessionRail`/`SessionStage`/
  `HeaderStrip`/`StateDot`/`SeatInspector` (+ two jsdom suites) land and `SessionsView` becomes
  the once-derived model/rollup seam with smart-default focus, focus handoff, and dynamic palette
  commands; `Chats.tsx` hands its 2.5s catalog poll to the shared `data/catalogPoll.ts` driver
  (consumer semantics byte-equivalent); `file-viewer/FileViewer.tsx` gains a reviewer-accepted
  one-line defensive repos-catalog guard. Detail lives in the `session-cockpit/` overview and the
  touched sidecars; no panel was removed. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.

- 2026-07-17T00:30+02:00 — 260715-FEUI-L1 route impact: the route gains the **`session-cockpit/`**
  child route — the Sessions cockpit view shell (rail/stage/inspector PanelGroup + narrow rules +
  ~80-col floor chip + rail calibration), the non-portal cmdk CommandPalette (commands/keys pages
  from one options source), and the useKeyboardZones tinykeys binding — registered in
  `cockpit/Cockpit.tsx` as the fourth keep-alive full-bleed layer. Panel content is labeled
  scaffolding for L2/L4/L5/L6/L7. Added the bullet + child-route link; no existing panel changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.

  child route — the Sessions cockpit view shell (rail/stage/inspector PanelGroup + narrow rules +
  ~80-col floor chip + rail calibration), the non-portal cmdk CommandPalette (commands/keys pages
  from one options source), and the useKeyboardZones tinykeys binding — registered in
  `cockpit/Cockpit.tsx` as the fourth keep-alive full-bleed layer. Panel content is labeled
  scaffolding for L2/L4/L5/L6/L7. Added the bullet + child-route link; no existing panel changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.

  child route — the Sessions cockpit view shell (rail/stage/inspector PanelGroup + narrow rules +
  ~80-col floor chip + rail calibration), the non-portal cmdk CommandPalette (commands/keys pages
  from one options source), and the useKeyboardZones tinykeys binding — registered in
  `cockpit/Cockpit.tsx` as the fourth keep-alive full-bleed layer. Panel content is labeled
  scaffolding for L2/L4/L5/L6/L7. Added the bullet + child-route link; no existing panel changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
  child route — the Sessions cockpit view shell (rail/stage/inspector PanelGroup + narrow rules +
  ~80-col floor chip + rail calibration), the non-portal cmdk CommandPalette (commands/keys pages
  from one options source), and the useKeyboardZones tinykeys binding — registered in
  `cockpit/Cockpit.tsx` as the fourth keep-alive full-bleed layer. Panel content is labeled
  scaffolding for L2/L4/L5/L6/L7. Added the bullet + child-route link; no existing panel changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.











- 2026-07-12T17:50+02:00 — 260712-TRH-L6 route impact: documented the new Operations chat-activity indicator,
  shared Chats catalog ownership, exact-leaf-first/lifecycle-fallback identity, deterministic multi-seat
  precedence, static inbox acknowledgment state, missing/landed/stale omission behavior, and the three
  independent signaling axes. No new dashboard route was introduced. Reviewer F1–F6 are recorded as
  follow-up residuals in the relevant sidecars.

  shared Chats catalog ownership, exact-leaf-first/lifecycle-fallback identity, deterministic multi-seat
  precedence, static inbox acknowledgment state, missing/landed/stale omission behavior, and the three
  independent signaling axes. No new dashboard route was introduced. Reviewer F1–F6 are recorded as
  follow-up residuals in the relevant sidecars.

  shared Chats catalog ownership, exact-leaf-first/lifecycle-fallback identity, deterministic multi-seat
  precedence, static inbox acknowledgment state, missing/landed/stale omission behavior, and the three
  independent signaling axes. No new dashboard route was introduced. Reviewer F1–F6 are recorded as
  follow-up residuals in the relevant sidecars.
  shared Chats catalog ownership, exact-leaf-first/lifecycle-fallback identity, deterministic multi-seat
  precedence, static inbox acknowledgment state, missing/landed/stale omission behavior, and the three
  independent signaling axes. No new dashboard route was introduced. Reviewer F1–F6 are recorded as
  follow-up residuals in the relevant sidecars.

- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the `DetailPanel` change-set entry and `panels/changeset` child-route refinements do not alter the broader panels inventory or navigation model. Verification metadata remains pinned until closeout.

- 2026-07-12T12:58+02:00 — 260712-TRH-L3 route impact: refreshed the existing `LifecycleList.tsx`
  route model for BY REPO-only persisted sprint/master disclosure, independent nested collapse,
  selection-safe native controls, and unchanged BY PHASE/total-count semantics. No new route or entity
  was introduced; the two concrete helper modules are covered by file sidecars.

  route model for BY REPO-only persisted sprint/master disclosure, independent nested collapse,
  selection-safe native controls, and unchanged BY PHASE/total-count semantics. No new route or entity
  was introduced; the two concrete helper modules are covered by file sidecars.

  route model for BY REPO-only persisted sprint/master disclosure, independent nested collapse,
  selection-safe native controls, and unchanged BY PHASE/total-count semantics. No new route or entity
  was introduced; the two concrete helper modules are covered by file sidecars.
  route model for BY REPO-only persisted sprint/master disclosure, independent nested collapse,
  selection-safe native controls, and unchanged BY PHASE/total-count semantics. No new route or entity
  was introduced; the two concrete helper modules are covered by file sidecars.

- 2026-07-12T12:55+02:00 — No additional route impact from 260712-TRH-L2: its `DetailPanel` change-set entry and `panels/changeset` child-route refinements do not alter the broader panels inventory or navigation model. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-07-12T12:07+02:00 — 260712-TRH-L1 route impact: added the body-state data hook and made
  `DetailPanel` defer notes plus reader/enclosure change-set requests until visible body hydration
  succeeds or fails. Summary fallback and panel inventory remain intact; verification metadata stays
  pinned until closeout.


  `DetailPanel` defer notes plus reader/enclosure change-set requests until visible body hydration
  succeeds or fails. Summary fallback and panel inventory remain intact; verification metadata stays
  pinned until closeout.

  `DetailPanel` defer notes plus reader/enclosure change-set requests until visible body hydration
  succeeds or fails. Summary fallback and panel inventory remain intact; verification metadata stays
  pinned until closeout.
  `DetailPanel` defer notes plus reader/enclosure change-set requests until visible body hydration
  succeeds or fails. Summary fallback and panel inventory remain intact; verification metadata stays
  pinned until closeout.

- 2026-07-10T21:52+02:00 — 260707-HFX2-L21 route impact: the existing Chats full-bleed layout now
  has a bounded, persisted, pointer/keyboard-resizable session-tree rail. Panel inventory and routing
  are unchanged; focused coverage pins restoration, ARIA values, drag, arrow steps, and persistence.
  Verification metadata remains pinned to the task base until closeout.


  has a bounded, persisted, pointer/keyboard-resizable session-tree rail. Panel inventory and routing
  are unchanged; focused coverage pins restoration, ARIA values, drag, arrow steps, and persistence.
  Verification metadata remains pinned to the task base until closeout.

  has a bounded, persisted, pointer/keyboard-resizable session-tree rail. Panel inventory and routing
  are unchanged; focused coverage pins restoration, ARIA values, drag, arrow steps, and persistence.
  Verification metadata remains pinned to the task base until closeout.
  has a bounded, persisted, pointer/keyboard-resizable session-tree rail. Panel inventory and routing
  are unchanged; focused coverage pins restoration, ARIA values, drag, arrow steps, and persistence.
  Verification metadata remains pinned to the task base until closeout.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 panels route impact: added explicit seat-role picker,
  pair-aware attach/move, and binding-first rail/fleet rendering; no route layout change.


  pair-aware attach/move, and binding-first rail/fleet rendering; no route layout change.

  pair-aware attach/move, and binding-first rail/fleet rendering; no route layout change.
  pair-aware attach/move, and binding-first rail/fleet rendering; no route layout change.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 route impact: refreshed the existing SessionList and
  DetailPanel responsibilities for complete spawn forests, manager-only collapse, bounded hover-
  recoverable rows, merged task bodies, explicit summary fallback, and one implementation-step list.
  Panel inventory/routing is unchanged. Verification metadata stays pinned until closeout.


  DetailPanel responsibilities for complete spawn forests, manager-only collapse, bounded hover-
  recoverable rows, merged task bodies, explicit summary fallback, and one implementation-step list.
  Panel inventory/routing is unchanged. Verification metadata stays pinned until closeout.

  DetailPanel responsibilities for complete spawn forests, manager-only collapse, bounded hover-
  recoverable rows, merged task bodies, explicit summary fallback, and one implementation-step list.
  Panel inventory/routing is unchanged. Verification metadata stays pinned until closeout.
  DetailPanel responsibilities for complete spawn forests, manager-only collapse, bounded hover-
  recoverable rows, merged task bodies, explicit summary fallback, and one implementation-step list.
  Panel inventory/routing is unchanged. Verification metadata stays pinned until closeout.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6 route impact: migrated `DetailPanel` to fetch only
  the displayed task body on demand, cache it by path/revision, and keep summary fallback behavior;
  test fetch doubles now serve that endpoint. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.


  the displayed task body on demand, cache it by path/revision, and keep summary fallback behavior;
  test fetch doubles now serve that endpoint. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.

  the displayed task body on demand, cache it by path/revision, and keep summary fallback behavior;
  test fetch doubles now serve that endpoint. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.
  the displayed task body on demand, cache it by path/revision, and keep summary fallback behavior;
  test fetch doubles now serve that endpoint. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact (landed chat archive + group cleanup):
  `Chats.tsx` and `SessionList.tsx` gain a collapsed "landed archive" group for `status:"landed"`
  rows (role/leaf/master/label/turn-state/landed-reason/timestamp/provenance surfaced, non-live but
  inspectable) plus a "Close landed archive" group-cleanup control (backend-rechecked, reports
  closed/skipped); `Terminal.tsx` gains a `readOnly` prop so a landed seat's terminal stays viewable
  without accepting input. No new panel module or routing change — per-file detail lives in each
  file's own sidecar. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.

  `Chats.tsx` and `SessionList.tsx` gain a collapsed "landed archive" group for `status:"landed"`
  rows (role/leaf/master/label/turn-state/landed-reason/timestamp/provenance surfaced, non-live but
  inspectable) plus a "Close landed archive" group-cleanup control (backend-rechecked, reports
  closed/skipped); `Terminal.tsx` gains a `readOnly` prop so a landed seat's terminal stays viewable
  without accepting input. No new panel module or routing change — per-file detail lives in each
  file's own sidecar. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.

  `Chats.tsx` and `SessionList.tsx` gain a collapsed "landed archive" group for `status:"landed"`
  rows (role/leaf/master/label/turn-state/landed-reason/timestamp/provenance surfaced, non-live but
  inspectable) plus a "Close landed archive" group-cleanup control (backend-rechecked, reports
  closed/skipped); `Terminal.tsx` gains a `readOnly` prop so a landed seat's terminal stays viewable
  without accepting input. No new panel module or routing change — per-file detail lives in each
  file's own sidecar. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
  `Chats.tsx` and `SessionList.tsx` gain a collapsed "landed archive" group for `status:"landed"`
  rows (role/leaf/master/label/turn-state/landed-reason/timestamp/provenance surfaced, non-live but
  inspectable) plus a "Close landed archive" group-cleanup control (backend-rechecked, reports
  closed/skipped); `Terminal.tsx` gains a `readOnly` prop so a landed seat's terminal stays viewable
  without accepting input. No new panel module or routing change — per-file detail lives in each
  file's own sidecar. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.

- 2026-07-08T04:25+02:00 — 260707-HFX-L12 route impact (docs-parity fold-in, master-exit Finding
  3): `SessionList`'s `ROLE_VALUES`/`roleChip` registry gains `designer` (gold) and
  `system-specialist` (cyan), matching the existing four-tier color convention (no new token) —
  both roles were already spawnable but rendered as the muted base chip; the panels route inventory
  itself is unchanged (same mechanism, two more registered Literal members). Verification metadata
  pinned until closeout stamps the HFX-L12 commit.

  3): `SessionList`'s `ROLE_VALUES`/`roleChip` registry gains `designer` (gold) and
  `system-specialist` (cyan), matching the existing four-tier color convention (no new token) —
  both roles were already spawnable but rendered as the muted base chip; the panels route inventory
  itself is unchanged (same mechanism, two more registered Literal members). Verification metadata
  pinned until closeout stamps the HFX-L12 commit.

  3): `SessionList`'s `ROLE_VALUES`/`roleChip` registry gains `designer` (gold) and
  `system-specialist` (cyan), matching the existing four-tier color convention (no new token) —
  both roles were already spawnable but rendered as the muted base chip; the panels route inventory
  itself is unchanged (same mechanism, two more registered Literal members). Verification metadata
  pinned until closeout stamps the HFX-L12 commit.
  3): `SessionList`'s `ROLE_VALUES`/`roleChip` registry gains `designer` (gold) and
  `system-specialist` (cyan), matching the existing four-tier color convention (no new token) —
  both roles were already spawnable but rendered as the muted base chip; the panels route inventory
  itself is unchanged (same mechanism, two more registered Literal members). Verification metadata
  pinned until closeout stamps the HFX-L12 commit.

- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: `SessionList`/`Chats`
  role rendering and the dormant `FlowTab` model now carry architect/curator seats, matching the
  architect/default developer-facing split and curator closeout chain while keeping the panels route
  inventory unchanged. Verification metadata pinned until closeout stamps the HFX-L6 commit.

  role rendering and the dormant `FlowTab` model now carry architect/curator seats, matching the
  architect/default developer-facing split and curator closeout chain while keeping the panels route
  inventory unchanged. Verification metadata pinned until closeout stamps the HFX-L6 commit.

  role rendering and the dormant `FlowTab` model now carry architect/curator seats, matching the
  architect/default developer-facing split and curator closeout chain while keeping the panels route
  inventory unchanged. Verification metadata pinned until closeout stamps the HFX-L6 commit.
  role rendering and the dormant `FlowTab` model now carry architect/curator seats, matching the
  architect/default developer-facing split and curator closeout chain while keeping the panels route
  inventory unchanged. Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T14:00+02:00 — agent-orchestration L17 route impact: the route gains the **`notes-reader/`**
  child route (the Notes Reader takeover — a notes-tree rail + a content pane that REUSES the File Viewer
  `DualPane`, over the unchanged L9 `/api/notes/*` API). `TaskNotes.tsx` becomes the compact ENTRY SURFACE
  only (its inline reader retired; list + references now call `onOpenNotes`), `DetailPanel.tsx` threads
  `onOpenNotes` to it, and `LifecycleList.tsx`'s `gateHint` drops the wait-loop `ask` fallback (durable gate
  kind only). Added the `notes-reader/` bullet + child-route link, rewrote the `TaskNotes` bullet, and
  de-staled the `DetailPanel`/`LifecycleList` bullets. Verification metadata pinned until closeout stamps the
  L17 commit.

  child route (the Notes Reader takeover — a notes-tree rail + a content pane that REUSES the File Viewer
  `DualPane`, over the unchanged L9 `/api/notes/*` API). `TaskNotes.tsx` becomes the compact ENTRY SURFACE
  only (its inline reader retired; list + references now call `onOpenNotes`), `DetailPanel.tsx` threads
  `onOpenNotes` to it, and `LifecycleList.tsx`'s `gateHint` drops the wait-loop `ask` fallback (durable gate
  kind only). Added the `notes-reader/` bullet + child-route link, rewrote the `TaskNotes` bullet, and
  de-staled the `DetailPanel`/`LifecycleList` bullets. Verification metadata pinned until closeout stamps the
  L17 commit.

  child route (the Notes Reader takeover — a notes-tree rail + a content pane that REUSES the File Viewer
  `DualPane`, over the unchanged L9 `/api/notes/*` API). `TaskNotes.tsx` becomes the compact ENTRY SURFACE
  only (its inline reader retired; list + references now call `onOpenNotes`), `DetailPanel.tsx` threads
  `onOpenNotes` to it, and `LifecycleList.tsx`'s `gateHint` drops the wait-loop `ask` fallback (durable gate
  kind only). Added the `notes-reader/` bullet + child-route link, rewrote the `TaskNotes` bullet, and
  de-staled the `DetailPanel`/`LifecycleList` bullets. Verification metadata pinned until closeout stamps the
  L17 commit.
  child route (the Notes Reader takeover — a notes-tree rail + a content pane that REUSES the File Viewer
  `DualPane`, over the unchanged L9 `/api/notes/*` API). `TaskNotes.tsx` becomes the compact ENTRY SURFACE
  only (its inline reader retired; list + references now call `onOpenNotes`), `DetailPanel.tsx` threads
  `onOpenNotes` to it, and `LifecycleList.tsx`'s `gateHint` drops the wait-loop `ask` fallback (durable gate
  kind only). Added the `notes-reader/` bullet + child-route link, rewrote the `TaskNotes` bullet, and
  de-staled the `DetailPanel`/`LifecycleList` bullets. Verification metadata pinned until closeout stamps the
  L17 commit.

- 2026-07-07T10:55+02:00 — L15 route impact (body): the four age panels' served-ages local-advance pattern documented. Verification metadata pinned until closeout stamps the L15 commit.











- 2026-07-07T05:40+02:00 — 260703-L15 route impact (small): the four age-display panels
  (`Hangar.tsx`, `AttentionQueue.tsx`, `MemoryMirror.tsx`, `LifecycleList.tsx`) now advance served
  ages locally — `servedAgeSeconds(node, …Seconds, nowMs)` + a panel-level `useNowMs()` 10 s tick
  (`data/servedAges.ts`) — because the L15 change gate stopped re-serving nodes whose only
  movement is their age. No layout/behavior change otherwise; the panels route model is unchanged.
  Verification metadata pinned until closeout stamps the L15 commit.

  (`Hangar.tsx`, `AttentionQueue.tsx`, `MemoryMirror.tsx`, `LifecycleList.tsx`) now advance served
  ages locally — `servedAgeSeconds(node, …Seconds, nowMs)` + a panel-level `useNowMs()` 10 s tick
  (`data/servedAges.ts`) — because the L15 change gate stopped re-serving nodes whose only
  movement is their age. No layout/behavior change otherwise; the panels route model is unchanged.
  Verification metadata pinned until closeout stamps the L15 commit.

  (`Hangar.tsx`, `AttentionQueue.tsx`, `MemoryMirror.tsx`, `LifecycleList.tsx`) now advance served
  ages locally — `servedAgeSeconds(node, …Seconds, nowMs)` + a panel-level `useNowMs()` 10 s tick
  (`data/servedAges.ts`) — because the L15 change gate stopped re-serving nodes whose only
  movement is their age. No layout/behavior change otherwise; the panels route model is unchanged.
  Verification metadata pinned until closeout stamps the L15 commit.
  (`Hangar.tsx`, `AttentionQueue.tsx`, `MemoryMirror.tsx`, `LifecycleList.tsx`) now advance served
  ages locally — `servedAgeSeconds(node, …Seconds, nowMs)` + a panel-level `useNowMs()` 10 s tick
  (`data/servedAges.ts`) — because the L15 change gate stopped re-serving nodes whose only
  movement is their age. No layout/behavior change otherwise; the panels route model is unchanged.
  Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-06T23:57:24+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): the tasks tab
  gained the orchestration tier (gold/purple V4 command rows over `TaskDocNode.orchestrates`, N-depth
  `BY REPO` hierarchy, 22px indent grammar, `grammar/RankBadge` insignia — see `LifecycleList.tsx`),
  and the Chats sidebar gained the G1 command tree (`SessionList` collapsible groups over the new
  `data/sessionGroups` model threaded by `Chats.tsx`, spawn-role chips from the catalog's
  AR_SPAWN_ROLE). The GOLD tier is orchestration-gated (D3): the orchestration row and the sprint deck appear only when an orchestration task exists; master grouping + the landed archive are the chats pane's BASELINE organization (grouping-always, owner-ratified at review L14R-1), mirroring the tasks tab's master>leaf nesting. The tasks tab itself renders flat runs exactly as before.
  Verification metadata pinned until closeout stamps the L14 commit.

  gained the orchestration tier (gold/purple V4 command rows over `TaskDocNode.orchestrates`, N-depth
  `BY REPO` hierarchy, 22px indent grammar, `grammar/RankBadge` insignia — see `LifecycleList.tsx`),
  and the Chats sidebar gained the G1 command tree (`SessionList` collapsible groups over the new
  `data/sessionGroups` model threaded by `Chats.tsx`, spawn-role chips from the catalog's
  AR_SPAWN_ROLE). The GOLD tier is orchestration-gated (D3): the orchestration row and the sprint deck appear only when an orchestration task exists; master grouping + the landed archive are the chats pane's BASELINE organization (grouping-always, owner-ratified at review L14R-1), mirroring the tasks tab's master>leaf nesting. The tasks tab itself renders flat runs exactly as before.
  Verification metadata pinned until closeout stamps the L14 commit.

  gained the orchestration tier (gold/purple V4 command rows over `TaskDocNode.orchestrates`, N-depth
  `BY REPO` hierarchy, 22px indent grammar, `grammar/RankBadge` insignia — see `LifecycleList.tsx`),
  and the Chats sidebar gained the G1 command tree (`SessionList` collapsible groups over the new
  `data/sessionGroups` model threaded by `Chats.tsx`, spawn-role chips from the catalog's
  AR_SPAWN_ROLE). The GOLD tier is orchestration-gated (D3): the orchestration row and the sprint deck appear only when an orchestration task exists; master grouping + the landed archive are the chats pane's BASELINE organization (grouping-always, owner-ratified at review L14R-1), mirroring the tasks tab's master>leaf nesting. The tasks tab itself renders flat runs exactly as before.
  Verification metadata pinned until closeout stamps the L14 commit.
  gained the orchestration tier (gold/purple V4 command rows over `TaskDocNode.orchestrates`, N-depth
  `BY REPO` hierarchy, 22px indent grammar, `grammar/RankBadge` insignia — see `LifecycleList.tsx`),
  and the Chats sidebar gained the G1 command tree (`SessionList` collapsible groups over the new
  `data/sessionGroups` model threaded by `Chats.tsx`, spawn-role chips from the catalog's
  AR_SPAWN_ROLE). The GOLD tier is orchestration-gated (D3): the orchestration row and the sprint deck appear only when an orchestration task exists; master grouping + the landed archive are the chats pane's BASELINE organization (grouping-always, owner-ratified at review L14R-1), mirroring the tasks tab's master>leaf nesting. The tasks tab itself renders flat runs exactly as before.
  Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T15:40+02:00 — 260703-L12 route impact (three-party loops, canvas ride-along): `flowModels.ts` gains the STRATEGIST model (FLOW_MODELS census 7 → 8; placed between designer and orchestrator) and loop-doctrine lines on the manager/worker/reviewer/comms/orchestrator drawings; `FlowTab.test.tsx` grows to 11 cases (strategist model + cross-model loop invariants). FlowTab.tsx itself is unchanged (pure renderer over the registry). Verification metadata pinned until closeout stamps the L12 commit.

- 2026-07-06T12:10+02:00 — 260703-L10 route impact (small): the FlowTab canvas was verified against the converged `l-01-agent-lifecycles` doctrine (S2 reduced to verification after L8 shipped the redraw); the one residual vocabulary drift fixed is the designer model's reframe-agreement node phase label, `"frame"` → `"reframe"`. Tests (41 files / 385) stay green — no invariant string changed. Verification metadata pinned until closeout stamps the L10 commit.

- 2026-07-06T10:30+02:00 — L11 adversarial-review follow-up: the anchor fallback annotation is deterministic (greatest lastEventTs), closing L11R-2. Verification metadata pinned until closeout stamps the L11 commit.

- 2026-07-06T02:50+02:00 — 260703-L9 route impact (friction F-M): the route gains `TaskNotes.tsx`
  (+ its component suite), the read-only coordination-notes surface — series notes list over
  `/api/notes/*`, opened notes rendered as formatted markdown (sidecar treatment), and task-doc
  references resolved into openable links; `DetailPanel.tsx`'s `TaskReader` delegates its
  References section to it and `MasterOverview` appends it. Verification metadata pinned until
  closeout stamps the L9 commit.

  (+ its component suite), the read-only coordination-notes surface — series notes list over
  `/api/notes/*`, opened notes rendered as formatted markdown (sidecar treatment), and task-doc
  references resolved into openable links; `DetailPanel.tsx`'s `TaskReader` delegates its
  References section to it and `MasterOverview` appends it. Verification metadata pinned until
  closeout stamps the L9 commit.

  (+ its component suite), the read-only coordination-notes surface — series notes list over
  `/api/notes/*`, opened notes rendered as formatted markdown (sidecar treatment), and task-doc
  references resolved into openable links; `DetailPanel.tsx`'s `TaskReader` delegates its
  References section to it and `MasterOverview` appends it. Verification metadata pinned until
  closeout stamps the L9 commit.
  (+ its component suite), the read-only coordination-notes surface — series notes list over
  `/api/notes/*`, opened notes rendered as formatted markdown (sidecar treatment), and task-doc
  references resolved into openable links; `DetailPanel.tsx`'s `TaskReader` delegates its
  References section to it and `MasterOverview` appends it. Verification metadata pinned until
  closeout stamps the L9 commit.

- 2026-07-06T02:45+02:00 — 260703-L11 route impact (tasks tab shows worktree truth): `Hangar` and
  `LifecycleList` visibility flipped from cleanup-state proxies to the shared `hasLiveWorktree`
  existence rule over the new `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags — a
  reopened contract stays hidden until `worktree_start` recreates its worktrees; `LifecycleList` adds
  the one-row-per-`enclosureId` identity rule with `lifecycleForEnclosure` annotating the single doc row (deterministically: greatest `lastEventTs` wins the anchor fallback, L11R-2)
  instead of duplicating the leaf as a lifecycle card. Verification metadata pinned until closeout
  stamps the L11 commit.

  `LifecycleList` visibility flipped from cleanup-state proxies to the shared `hasLiveWorktree`
  existence rule over the new `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags — a
  reopened contract stays hidden until `worktree_start` recreates its worktrees; `LifecycleList` adds
  the one-row-per-`enclosureId` identity rule with `lifecycleForEnclosure` annotating the single doc row (deterministically: greatest `lastEventTs` wins the anchor fallback, L11R-2)
  instead of duplicating the leaf as a lifecycle card. Verification metadata pinned until closeout
  stamps the L11 commit.

  `LifecycleList` visibility flipped from cleanup-state proxies to the shared `hasLiveWorktree`
  existence rule over the new `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags — a
  reopened contract stays hidden until `worktree_start` recreates its worktrees; `LifecycleList` adds
  the one-row-per-`enclosureId` identity rule with `lifecycleForEnclosure` annotating the single doc row (deterministically: greatest `lastEventTs` wins the anchor fallback, L11R-2)
  instead of duplicating the leaf as a lifecycle card. Verification metadata pinned until closeout
  stamps the L11 commit.
  `LifecycleList` visibility flipped from cleanup-state proxies to the shared `hasLiveWorktree`
  existence rule over the new `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags — a
  reopened contract stays hidden until `worktree_start` recreates its worktrees; `LifecycleList` adds
  the one-row-per-`enclosureId` identity rule with `lifecycleForEnclosure` annotating the single doc row (deterministically: greatest `lastEventTs` wins the anchor fallback, L11R-2)
  instead of duplicating the leaf as a lifecycle card. Verification metadata pinned until closeout
  stamps the L11 commit.

- 2026-07-05T19:55+02:00 — 260703-L8 route impact (cycle 7, AR4-3/AR4-4): the seam-channel sentence rescoped to what the canvas draws — the manager raise node now names `enclosure="<master task name>"` as the exact address integration enforcement matches the gate by (AR4-4), so the enclosure clause is true as-drawn; the cycle-6 owner follow-up's "exactly … integration enforces the verdict by master identity" overclaim is dropped (enforcement itself is not a drawn node). Verification metadata pinned until closeout stamps the L8 commit.

- 2026-07-05T19:25+02:00 — 260703-L8 route impact (cycle 6, owner follow-up): body de-staled — the FlowTab paragraph's leftover build-job/frame tail (deleted models, the "8 static models" reference row, the "other seven" phrasing) replaced with the converged 7-model census and the exact ruled seam channel (wait=false raise, enclosure address, packet-carried gateId, identity-addressed enforcement). Verification metadata pinned until closeout stamps the L8 commit.

- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): the flowModels seam nodes now draw the ruled channel exactly — the manager's raise carries wait=false with the returned gateId riding the packet, and the orchestrator decides by the packet-carried gateId; FlowTab tests pin the new prose. Verification metadata pinned until closeout stamps the L8 commit.

- 2026-07-05T16:32+02:00 — 260703-L8 route impact (small): the FlowTab registry now draws the converged lifecycle doctrine — ROUTER model (three conditions + D·P·O event loop + the invariant ladder) replaces the retired FRAME and BUILD-JOB models; worker/manager/orchestrator/reviewer/comms models redrawn to the ruled seam semantics; FlowTab tests rewritten (9). Verification metadata pinned until closeout stamps the L8 commit.

- 2026-07-04T12:31+02:00 - L3 route impact: task-row pickup feedback now
  mirrors message-kind and hosted-delivery metadata from `AgentPickupNode`.
  Verification metadata pinned until closeout stamps the L3 commit.

  mirrors message-kind and hosted-delivery metadata from `AgentPickupNode`.
  Verification metadata pinned until closeout stamps the L3 commit.

  mirrors message-kind and hosted-delivery metadata from `AgentPickupNode`.
  Verification metadata pinned until closeout stamps the L3 commit.
  mirrors message-kind and hosted-delivery metadata from `AgentPickupNode`.
  Verification metadata pinned until closeout stamps the L3 commit.

- 2026-07-04T09:40+02:00 — 260703-L0 (Canvas & playground) route impact: reworked the `FlowTab.tsx` bullet
  from the dormant single-model Lifecycle Flow diagnostic into the **lifecycle-design canvas** — a pure
  segment renderer + radiogroup model nav (still zero store reads) over the **new `flowModels.ts`**
  flow-model registry (8 static models: build-job · frame · designer · orchestrator · manager · worker ·
  reviewer · comms, encoding the orchestration series' agreed invariants). The build-job model preserves
  the task-26 chain and stays the `next_step.py` SPEC; the source is now **mounted dev-only at `/dev/flows`**
  via `dev/DevApp.tsx` (kept out of the cockpit `View` union per task 29) and covered by the new
  `FlowTab.test.tsx`. Added `panels/flowModels.ts.md` + `panels/FlowTab.test.tsx.md` sidecars. Verification
  metadata pinned until closeout stamps the L0 commit.

  from the dormant single-model Lifecycle Flow diagnostic into the **lifecycle-design canvas** — a pure
  segment renderer + radiogroup model nav (still zero store reads) over the **new `flowModels.ts`**
  flow-model registry (8 static models: build-job · frame · designer · orchestrator · manager · worker ·
  reviewer · comms, encoding the orchestration series' agreed invariants). The build-job model preserves
  the task-26 chain and stays the `next_step.py` SPEC; the source is now **mounted dev-only at `/dev/flows`**
  via `dev/DevApp.tsx` (kept out of the cockpit `View` union per task 29) and covered by the new
  `FlowTab.test.tsx`. Added `panels/flowModels.ts.md` + `panels/FlowTab.test.tsx.md` sidecars. Verification
  metadata pinned until closeout stamps the L0 commit.

  from the dormant single-model Lifecycle Flow diagnostic into the **lifecycle-design canvas** — a pure
  segment renderer + radiogroup model nav (still zero store reads) over the **new `flowModels.ts`**
  flow-model registry (8 static models: build-job · frame · designer · orchestrator · manager · worker ·
  reviewer · comms, encoding the orchestration series' agreed invariants). The build-job model preserves
  the task-26 chain and stays the `next_step.py` SPEC; the source is now **mounted dev-only at `/dev/flows`**
  via `dev/DevApp.tsx` (kept out of the cockpit `View` union per task 29) and covered by the new
  `FlowTab.test.tsx`. Added `panels/flowModels.ts.md` + `panels/FlowTab.test.tsx.md` sidecars. Verification
  metadata pinned until closeout stamps the L0 commit.
  from the dormant single-model Lifecycle Flow diagnostic into the **lifecycle-design canvas** — a pure
  segment renderer + radiogroup model nav (still zero store reads) over the **new `flowModels.ts`**
  flow-model registry (8 static models: build-job · frame · designer · orchestrator · manager · worker ·
  reviewer · comms, encoding the orchestration series' agreed invariants). The build-job model preserves
  the task-26 chain and stays the `next_step.py` SPEC; the source is now **mounted dev-only at `/dev/flows`**
  via `dev/DevApp.tsx` (kept out of the cockpit `View` union per task 29) and covered by the new
  `FlowTab.test.tsx`. Added `panels/flowModels.ts.md` + `panels/FlowTab.test.tsx.md` sidecars. Verification
  metadata pinned until closeout stamps the L0 commit.

- 2026-07-03T00:35+02:00 — L11 route impact: LifecycleList excludes abandoned enclosures from the active rows and drops the -rN startsWith doc-admission heuristic (task_reopen keeps leaf ids stable).

- 2026-07-02T21:45+02:00 — L10 route impact: `LifecycleList`'s `enclosureForDoc` admission is now
  case-insensitive on every leafId comparison (stem, doc id, and the lifecycle-guarded reopen-suffix
  rule) — enclosure leaf ids are slugified lowercase while doc ids are authored uppercase, so active
  series leaf docs failed the admission and rendered as doc-less runtime rows with no task content and
  no viewed-leaf chat chain. Verification metadata pinned until closeout stamps the L10 commit.

  case-insensitive on every leafId comparison (stem, doc id, and the lifecycle-guarded reopen-suffix
  rule) — enclosure leaf ids are slugified lowercase while doc ids are authored uppercase, so active
  series leaf docs failed the admission and rendered as doc-less runtime rows with no task content and
  no viewed-leaf chat chain. Verification metadata pinned until closeout stamps the L10 commit.

  case-insensitive on every leafId comparison (stem, doc id, and the lifecycle-guarded reopen-suffix
  rule) — enclosure leaf ids are slugified lowercase while doc ids are authored uppercase, so active
  series leaf docs failed the admission and rendered as doc-less runtime rows with no task content and
  no viewed-leaf chat chain. Verification metadata pinned until closeout stamps the L10 commit.
  case-insensitive on every leafId comparison (stem, doc id, and the lifecycle-guarded reopen-suffix
  rule) — enclosure leaf ids are slugified lowercase while doc ids are authored uppercase, so active
  series leaf docs failed the admission and rendered as doc-less runtime rows with no task content and
  no viewed-leaf chat chain. Verification metadata pinned until closeout stamps the L10 commit.

- 2026-07-02T20:55+02:00 — L8-r1 route correction (developer feedback): the direct leaf-chat paste is
  now triggered by the visible "Add to chat" pill CLICK instead of firing automatically on selection —
  the auto-paste made the interaction invisible and pasted unintended highlights. The pill stays for
  every selection with one consistent label; only the post-click routing differs (direct draft paste vs
  generic composer), and an unconfirmed direct paste opens the composer. Verification metadata pinned
  until closeout stamps the L8-r1 commit.

  now triggered by the visible "Add to chat" pill CLICK instead of firing automatically on selection —
  the auto-paste made the interaction invisible and pasted unintended highlights. The pill stays for
  every selection with one consistent label; only the post-click routing differs (direct draft paste vs
  generic composer), and an unconfirmed direct paste opens the composer. Verification metadata pinned
  until closeout stamps the L8-r1 commit.

  now triggered by the visible "Add to chat" pill CLICK instead of firing automatically on selection —
  the auto-paste made the interaction invisible and pasted unintended highlights. The pill stays for
  every selection with one consistent label; only the post-click routing differs (direct draft paste vs
  generic composer), and an unconfirmed direct paste opens the composer. Verification metadata pinned
  until closeout stamps the L8-r1 commit.
  now triggered by the visible "Add to chat" pill CLICK instead of firing automatically on selection —
  the auto-paste made the interaction invisible and pasted unintended highlights. The pill stays for
  every selection with one consistent label; only the post-click routing differs (direct draft paste vs
  generic composer), and an unconfirmed direct paste opens the composer. Verification metadata pinned
  until closeout stamps the L8-r1 commit.

- 2026-07-02T20:15+02:00 — L8 route impact: highlight handling split into a **direct leaf-chat draft
  paste** primary path (selection inside the viewed leaf's task reader + active rail chat + bound leaf
  chat → `pasteDraftToSession`, no popover, popover fallback on failed paste) with the generic
  `HighlightComposer` popover as fallback only; `GateResponder` lost its message-only **Chat** mode
  (durable approve/reject/dismiss remain); `DetailPanel` no longer raises the responder for proto
  `ask`-only items and tags the task-doc reader with `data-task-leaf-key`. Covered by the updated
  `HighlightComposer/DetailPanel/GateResponder` tests and `selection.test.ts`. Verification metadata
  pinned until closeout stamps the L8 commit.

  paste** primary path (selection inside the viewed leaf's task reader + active rail chat + bound leaf
  chat → `pasteDraftToSession`, no popover, popover fallback on failed paste) with the generic
  `HighlightComposer` popover as fallback only; `GateResponder` lost its message-only **Chat** mode
  (durable approve/reject/dismiss remain); `DetailPanel` no longer raises the responder for proto
  `ask`-only items and tags the task-doc reader with `data-task-leaf-key`. Covered by the updated
  `HighlightComposer/DetailPanel/GateResponder` tests and `selection.test.ts`. Verification metadata
  pinned until closeout stamps the L8 commit.

  paste** primary path (selection inside the viewed leaf's task reader + active rail chat + bound leaf
  chat → `pasteDraftToSession`, no popover, popover fallback on failed paste) with the generic
  `HighlightComposer` popover as fallback only; `GateResponder` lost its message-only **Chat** mode
  (durable approve/reject/dismiss remain); `DetailPanel` no longer raises the responder for proto
  `ask`-only items and tags the task-doc reader with `data-task-leaf-key`. Covered by the updated
  `HighlightComposer/DetailPanel/GateResponder` tests and `selection.test.ts`. Verification metadata
  pinned until closeout stamps the L8 commit.
  paste** primary path (selection inside the viewed leaf's task reader + active rail chat + bound leaf
  chat → `pasteDraftToSession`, no popover, popover fallback on failed paste) with the generic
  `HighlightComposer` popover as fallback only; `GateResponder` lost its message-only **Chat** mode
  (durable approve/reject/dismiss remain); `DetailPanel` no longer raises the responder for proto
  `ask`-only items and tags the task-doc reader with `data-task-leaf-key`. Covered by the updated
  `HighlightComposer/DetailPanel/GateResponder` tests and `selection.test.ts`. Verification metadata
  pinned until closeout stamps the L8 commit.

- 2026-07-02T17:04+02:00 — L9 route impact: extended the existing `Chats.tsx` / `RailChat.tsx` route model
  for hosted chat leaf reassignment. Attached chats keep the picker as a move control, successful moves
  emit `"leaf"` catalog invalidations and draft the destination leaf context, and out-of-session catalog
  changes live-refresh through BroadcastChannel or polling. Verification metadata pinned until closeout
  stamps the L9 commit.

  for hosted chat leaf reassignment. Attached chats keep the picker as a move control, successful moves
  emit `"leaf"` catalog invalidations and draft the destination leaf context, and out-of-session catalog
  changes live-refresh through BroadcastChannel or polling. Verification metadata pinned until closeout
  stamps the L9 commit.

  for hosted chat leaf reassignment. Attached chats keep the picker as a move control, successful moves
  emit `"leaf"` catalog invalidations and draft the destination leaf context, and out-of-session catalog
  changes live-refresh through BroadcastChannel or polling. Verification metadata pinned until closeout
  stamps the L9 commit.
  for hosted chat leaf reassignment. Attached chats keep the picker as a move control, successful moves
  emit `"leaf"` catalog invalidations and draft the destination leaf context, and out-of-session catalog
  changes live-refresh through BroadcastChannel or polling. Verification metadata pinned until closeout
  stamps the L9 commit.

- 2026-07-02T16:35+02:00 — Reopened L6 wheel-precedence route impact: the shared `Terminal` wrapper now
  defers wheel input to xterm's native mouse-report path whenever the attached app tracks the mouse
  (`term.modes.mouseTrackingMode !== "none"`). Combined with the backend's per-session tmux `mouse on`,
  wheel scrolling works for both normal-buffer TUIs (tmux copy-mode pane history — Codex) and
  mouse-aware alternate-screen TUIs (pass-through — Claude Code); synthesized PageUp/PageDown remains
  only as the mouse-less alternate-buffer fallback. `pasteDraftToSession` deliveries are now
  echo-confirmed with boot-deadline retries (`pasteAndConfirm`), fixing the leaf-context draft silently
  discarded by a booting Claude Code. Verification metadata pinned until closeout stamps the follow-up
  commit.

  defers wheel input to xterm's native mouse-report path whenever the attached app tracks the mouse
  (`term.modes.mouseTrackingMode !== "none"`). Combined with the backend's per-session tmux `mouse on`,
  wheel scrolling works for both normal-buffer TUIs (tmux copy-mode pane history — Codex) and
  mouse-aware alternate-screen TUIs (pass-through — Claude Code); synthesized PageUp/PageDown remains
  only as the mouse-less alternate-buffer fallback. `pasteDraftToSession` deliveries are now
  echo-confirmed with boot-deadline retries (`pasteAndConfirm`), fixing the leaf-context draft silently
  discarded by a booting Claude Code. Verification metadata pinned until closeout stamps the follow-up
  commit.

  defers wheel input to xterm's native mouse-report path whenever the attached app tracks the mouse
  (`term.modes.mouseTrackingMode !== "none"`). Combined with the backend's per-session tmux `mouse on`,
  wheel scrolling works for both normal-buffer TUIs (tmux copy-mode pane history — Codex) and
  mouse-aware alternate-screen TUIs (pass-through — Claude Code); synthesized PageUp/PageDown remains
  only as the mouse-less alternate-buffer fallback. `pasteDraftToSession` deliveries are now
  echo-confirmed with boot-deadline retries (`pasteAndConfirm`), fixing the leaf-context draft silently
  discarded by a booting Claude Code. Verification metadata pinned until closeout stamps the follow-up
  commit.
  defers wheel input to xterm's native mouse-report path whenever the attached app tracks the mouse
  (`term.modes.mouseTrackingMode !== "none"`). Combined with the backend's per-session tmux `mouse on`,
  wheel scrolling works for both normal-buffer TUIs (tmux copy-mode pane history — Codex) and
  mouse-aware alternate-screen TUIs (pass-through — Claude Code); synthesized PageUp/PageDown remains
  only as the mouse-less alternate-buffer fallback. `pasteDraftToSession` deliveries are now
  echo-confirmed with boot-deadline retries (`pasteAndConfirm`), fixing the leaf-context draft silently
  discarded by a booting Claude Code. Verification metadata pinned until closeout stamps the follow-up
  commit.

- 2026-07-02T15:03+02:00 — Reopened L6 served-page route impact: live 8770 inspection showed Codex-style
  chat panes in xterm's alternate buffer with no viewport scrollback, so the shared `Terminal` wrapper now
  keeps normal-buffer viewport scrolling but maps alternate-buffer wheel movement to PageUp/PageDown
  navigation. Verification metadata pinned until closeout stamps the follow-up commit.

  chat panes in xterm's alternate buffer with no viewport scrollback, so the shared `Terminal` wrapper now
  keeps normal-buffer viewport scrolling but maps alternate-buffer wheel movement to PageUp/PageDown
  navigation. Verification metadata pinned until closeout stamps the follow-up commit.

  chat panes in xterm's alternate buffer with no viewport scrollback, so the shared `Terminal` wrapper now
  keeps normal-buffer viewport scrolling but maps alternate-buffer wheel movement to PageUp/PageDown
  navigation. Verification metadata pinned until closeout stamps the follow-up commit.
  chat panes in xterm's alternate buffer with no viewport scrollback, so the shared `Terminal` wrapper now
  keeps normal-buffer viewport scrolling but maps alternate-buffer wheel movement to PageUp/PageDown
  navigation. Verification metadata pinned until closeout stamps the follow-up commit.

- 2026-07-02T14:28+02:00 — Reopened L6 route impact: the existing shared `Terminal` wrapper now captures
  wheel input, swallows partial pixel deltas, and routes accumulated movement to xterm viewport scrolling,
  preventing mouse wheel movement from becoming PTY up/down input in Chats and right-rail panes. No new
  route or panel surface was added; verification metadata pinned until closeout stamps the follow-up commit.

  wheel input, swallows partial pixel deltas, and routes accumulated movement to xterm viewport scrolling,
  preventing mouse wheel movement from becoming PTY up/down input in Chats and right-rail panes. No new
  route or panel surface was added; verification metadata pinned until closeout stamps the follow-up commit.

  wheel input, swallows partial pixel deltas, and routes accumulated movement to xterm viewport scrolling,
  preventing mouse wheel movement from becoming PTY up/down input in Chats and right-rail panes. No new
  route or panel surface was added; verification metadata pinned until closeout stamps the follow-up commit.
  wheel input, swallows partial pixel deltas, and routes accumulated movement to xterm viewport scrolling,
  preventing mouse wheel movement from becoming PTY up/down input in Chats and right-rail panes. No new
  route or panel surface was added; verification metadata pinned until closeout stamps the follow-up commit.

- 2026-07-02T13:07+02:00 — Reopened L6 route impact: leaf-context handoff remains in the existing
  `RailChat` route, but now pastes the packet as editable draft input instead of submitting it. The shared
  `Terminal` wrapper also enables xterm scrollback for Chats and right-rail panes. Verification metadata
  pinned until closeout stamps the follow-up commit.

  `RailChat` route, but now pastes the packet as editable draft input instead of submitting it. The shared
  `Terminal` wrapper also enables xterm scrollback for Chats and right-rail panes. Verification metadata
  pinned until closeout stamps the follow-up commit.

  `RailChat` route, but now pastes the packet as editable draft input instead of submitting it. The shared
  `Terminal` wrapper also enables xterm scrollback for Chats and right-rail panes. Verification metadata
  pinned until closeout stamps the follow-up commit.
  `RailChat` route, but now pastes the packet as editable draft input instead of submitting it. The shared
  `Terminal` wrapper also enables xterm scrollback for Chats and right-rail panes. Verification metadata
  pinned until closeout stamps the follow-up commit.

- 2026-07-01T01:19+02:00 — L6 route impact: extended the `Chats.tsx` / `RailChat.tsx` route-model
  description with bind-time leaf context handoff. The route still owns the existing hosted chat surfaces;
  `RailChat` now sends a projected context package only after start-on-leaf or successful free-chat attach,
  using `taskDocuments` plus `engineProcesses` for task/worktree facts. Verification metadata pinned until
  closeout stamps the L6 commit.

  description with bind-time leaf context handoff. The route still owns the existing hosted chat surfaces;
  `RailChat` now sends a projected context package only after start-on-leaf or successful free-chat attach,
  using `taskDocuments` plus `engineProcesses` for task/worktree facts. Verification metadata pinned until
  closeout stamps the L6 commit.

  description with bind-time leaf context handoff. The route still owns the existing hosted chat surfaces;
  `RailChat` now sends a projected context package only after start-on-leaf or successful free-chat attach,
  using `taskDocuments` plus `engineProcesses` for task/worktree facts. Verification metadata pinned until
  closeout stamps the L6 commit.
  description with bind-time leaf context handoff. The route still owns the existing hosted chat surfaces;
  `RailChat` now sends a projected context package only after start-on-leaf or successful free-chat attach,
  using `taskDocuments` plus `engineProcesses` for task/worktree facts. Verification metadata pinned until
  closeout stamps the L6 commit.

- 2026-06-30T00:00:00+02:00 — L5 follow-up route impact: reshaped the **`RailChat`** route-model description — it is now a
  per-(leaf, role) **chat (agent harness) + terminal (shell) vertical split** with a harness-choice start
  picker (`fetchHarnesses`), a separate ＋ Terminal, and an independent **terminate** per pane (replacing the
  pre-fix single "＋ Start chat for this leaf"); added `RailChat.test.tsx` coverage. The Chats/`SessionList`
  leaf key now comes from the **displayed** leaf via `DetailPanel.onViewLeaf` (not the master selection),
  and `SessionList` rows gained a hover `title` (full label + bound leaf, fix 4). Verification metadata
  pinned until closeout stamps the L5 commit.

  per-(leaf, role) **chat (agent harness) + terminal (shell) vertical split** with a harness-choice start
  picker (`fetchHarnesses`), a separate ＋ Terminal, and an independent **terminate** per pane (replacing the
  pre-fix single "＋ Start chat for this leaf"); added `RailChat.test.tsx` coverage. The Chats/`SessionList`
  leaf key now comes from the **displayed** leaf via `DetailPanel.onViewLeaf` (not the master selection),
  and `SessionList` rows gained a hover `title` (full label + bound leaf, fix 4). Verification metadata
  pinned until closeout stamps the L5 commit.

  per-(leaf, role) **chat (agent harness) + terminal (shell) vertical split** with a harness-choice start
  picker (`fetchHarnesses`), a separate ＋ Terminal, and an independent **terminate** per pane (replacing the
  pre-fix single "＋ Start chat for this leaf"); added `RailChat.test.tsx` coverage. The Chats/`SessionList`
  leaf key now comes from the **displayed** leaf via `DetailPanel.onViewLeaf` (not the master selection),
  and `SessionList` rows gained a hover `title` (full label + bound leaf, fix 4). Verification metadata
  pinned until closeout stamps the L5 commit.
  per-(leaf, role) **chat (agent harness) + terminal (shell) vertical split** with a harness-choice start
  picker (`fetchHarnesses`), a separate ＋ Terminal, and an independent **terminate** per pane (replacing the
  pre-fix single "＋ Start chat for this leaf"); added `RailChat.test.tsx` coverage. The Chats/`SessionList`
  leaf key now comes from the **displayed** leaf via `DetailPanel.onViewLeaf` (not the master selection),
  and `SessionList` rows gained a hover `title` (full label + bound leaf, fix 4). Verification metadata
  pinned until closeout stamps the L5 commit.

- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat) route impact: added **`RailChat.tsx`** (the single-instance right-rail
  leaf chat the cockpit `RailToggle` swaps in for the Event River, reusing the shared `Terminal` +
  `SessionComposer` + connection registry) to the Route Model, and extended the **Chats** bullet with
  leaf-keyed attachment — `Chats` gains an "Attach to leaf" control (`attach-leaf`, `200` bind / `409`
  "leaf already has a chat") + a bound-leaf badge, and `SessionList` gains a `leafNameFor` per-row leaf
  label (task-doc title, fallback leaf id). Verification metadata pinned until closeout stamps the L5
  commit.

  leaf chat the cockpit `RailToggle` swaps in for the Event River, reusing the shared `Terminal` +
  `SessionComposer` + connection registry) to the Route Model, and extended the **Chats** bullet with
  leaf-keyed attachment — `Chats` gains an "Attach to leaf" control (`attach-leaf`, `200` bind / `409`
  "leaf already has a chat") + a bound-leaf badge, and `SessionList` gains a `leafNameFor` per-row leaf
  label (task-doc title, fallback leaf id). Verification metadata pinned until closeout stamps the L5
  commit.

  leaf chat the cockpit `RailToggle` swaps in for the Event River, reusing the shared `Terminal` +
  `SessionComposer` + connection registry) to the Route Model, and extended the **Chats** bullet with
  leaf-keyed attachment — `Chats` gains an "Attach to leaf" control (`attach-leaf`, `200` bind / `409`
  "leaf already has a chat") + a bound-leaf badge, and `SessionList` gains a `leafNameFor` per-row leaf
  label (task-doc title, fallback leaf id). Verification metadata pinned until closeout stamps the L5
  commit.
  leaf chat the cockpit `RailToggle` swaps in for the Event River, reusing the shared `Terminal` +
  `SessionComposer` + connection registry) to the Route Model, and extended the **Chats** bullet with
  leaf-keyed attachment — `Chats` gains an "Attach to leaf" control (`attach-leaf`, `200` bind / `409`
  "leaf already has a chat") + a bound-leaf badge, and `SessionList` gains a `leafNameFor` per-row leaf
  label (task-doc title, fallback leaf id). Verification metadata pinned until closeout stamps the L5
  commit.

- 2026-06-29T23:00+02:00 — No route impact: L4a added change-set buttons on the task-document reader
  (`DetailPanel`'s `DocChangeSetBar` — series on a master, committed/working on a leaf) and refined the
  `changeset/` child route (leaf committed/working views + a diff-highlight rectangle). The `panels/`
  route model — the panel list + the `file-viewer/`/`changeset/` child routes — is unchanged; the detail
  lives in the `DetailPanel.tsx` sidecar and the `changeset/` overview. Verification metadata pinned until
  closeout stamps the L4a commit.

  (`DetailPanel`'s `DocChangeSetBar` — series on a master, committed/working on a leaf) and refined the
  `changeset/` child route (leaf committed/working views + a diff-highlight rectangle). The `panels/`
  route model — the panel list + the `file-viewer/`/`changeset/` child routes — is unchanged; the detail
  lives in the `DetailPanel.tsx` sidecar and the `changeset/` overview. Verification metadata pinned until
  closeout stamps the L4a commit.

  (`DetailPanel`'s `DocChangeSetBar` — series on a master, committed/working on a leaf) and refined the
  `changeset/` child route (leaf committed/working views + a diff-highlight rectangle). The `panels/`
  route model — the panel list + the `file-viewer/`/`changeset/` child routes — is unchanged; the detail
  lives in the `DetailPanel.tsx` sidecar and the `changeset/` overview. Verification metadata pinned until
  closeout stamps the L4a commit.
  (`DetailPanel`'s `DocChangeSetBar` — series on a master, committed/working on a leaf) and refined the
  `changeset/` child route (leaf committed/working views + a diff-highlight rectangle). The `panels/`
  route model — the panel list + the `file-viewer/`/`changeset/` child routes — is unchanged; the detail
  lives in the `DetailPanel.tsx` sidecar and the `changeset/` overview. Verification metadata pinned until
  closeout stamps the L4a commit.

- 2026-06-29T16:40+02:00 — Operations Integration L4 route impact: added the `changeset/` child route — the **Change-Set Viewer** screen (a task-scoped takeover over the L3 `/api/changeset/*` API; a read-only `@codemirror/merge` diff with split/inline/full-file/highlight-off toggles; a code↔sidecar partner column), opened from a `DetailPanel` change-set button as a Cockpit full-bleed takeover. See the new [changeset/ overview](changeset/overview.md). Verification metadata pinned to the task base until closeout stamps the L4 code commit.

- 2026-06-29T09:06+02:00 — Operations Integration L2 route impact: added the `file-viewer/` child route —
  the **File Viewer** centre tab (a read-only code + paired-onboarding browser over the L1 files API; a
  reusable CodeMirror dual-pane; bidirectional code↔onboarding pairing; kept mounted across tab switches).
  See the new [file-viewer/ overview](file-viewer/overview.md). Verification metadata pinned to the task
  base until closeout stamps the L2 code commit.

  the **File Viewer** centre tab (a read-only code + paired-onboarding browser over the L1 files API; a
  reusable CodeMirror dual-pane; bidirectional code↔onboarding pairing; kept mounted across tab switches).
  See the new [file-viewer/ overview](file-viewer/overview.md). Verification metadata pinned to the task
  base until closeout stamps the L2 code commit.

  the **File Viewer** centre tab (a read-only code + paired-onboarding browser over the L1 files API; a
  reusable CodeMirror dual-pane; bidirectional code↔onboarding pairing; kept mounted across tab switches).
  See the new [file-viewer/ overview](file-viewer/overview.md). Verification metadata pinned to the task
  base until closeout stamps the L2 code commit.
  the **File Viewer** centre tab (a read-only code + paired-onboarding browser over the L1 files API; a
  reusable CodeMirror dual-pane; bidirectional code↔onboarding pairing; kept mounted across tab switches).
  See the new [file-viewer/ overview](file-viewer/overview.md). Verification metadata pinned to the task
  base until closeout stamps the L2 code commit.

- 2026-06-28T16:17+02:00 — Task 35 route impact: `LifecycleList` now also admits a **reopened** leaf's
  suffixed-leaf enclosure (`leafId` = stem/`id` + cycle suffix, e.g. `…-s7`) on the combined shared-lifecycle
  + suffixed-leaf match (never a bare shared master lifecycle), and runtime-only enclosure-backed rows nest
  under their master via a computed parent key — so a re-opened/edited task no longer renders as a standalone
  phantom node. Verification metadata pinned until closeout stamps the code commit.

  suffixed-leaf enclosure (`leafId` = stem/`id` + cycle suffix, e.g. `…-s7`) on the combined shared-lifecycle
  + suffixed-leaf match (never a bare shared master lifecycle), and runtime-only enclosure-backed rows nest
  under their master via a computed parent key — so a re-opened/edited task no longer renders as a standalone
  phantom node. Verification metadata pinned until closeout stamps the code commit.

  suffixed-leaf enclosure (`leafId` = stem/`id` + cycle suffix, e.g. `…-s7`) on the combined shared-lifecycle
  + suffixed-leaf match (never a bare shared master lifecycle), and runtime-only enclosure-backed rows nest
  under their master via a computed parent key — so a re-opened/edited task no longer renders as a standalone
  phantom node. Verification metadata pinned until closeout stamps the code commit.
  suffixed-leaf enclosure (`leafId` = stem/`id` + cycle suffix, e.g. `…-s7`) on the combined shared-lifecycle
  + suffixed-leaf match (never a bare shared master lifecycle), and runtime-only enclosure-backed rows nest
  under their master via a computed parent key — so a re-opened/edited task no longer renders as a standalone
  phantom node. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-28T13:54+02:00 — Task 34 route impact: `EventRiver.tsx` now **virtualizes** the activity feed
  with `@tanstack/react-virtual` over the store's bounded sliding window (newest ~2000 rows), mounting
  only the visible rows (no hard display cap) while staying memory-bounded; the `/api/events` backend
  also now filters `lifecycle.heartbeat` out of the raw river, so the formatter's heartbeat hiding is
  belt-and-braces. Updated the `EventRiver.tsx` Route Model bullet. Verification metadata pinned until
  closeout stamps the task-34 code commit.

  with `@tanstack/react-virtual` over the store's bounded sliding window (newest ~2000 rows), mounting
  only the visible rows (no hard display cap) while staying memory-bounded; the `/api/events` backend
  also now filters `lifecycle.heartbeat` out of the raw river, so the formatter's heartbeat hiding is
  belt-and-braces. Updated the `EventRiver.tsx` Route Model bullet. Verification metadata pinned until
  closeout stamps the task-34 code commit.

  with `@tanstack/react-virtual` over the store's bounded sliding window (newest ~2000 rows), mounting
  only the visible rows (no hard display cap) while staying memory-bounded; the `/api/events` backend
  also now filters `lifecycle.heartbeat` out of the raw river, so the formatter's heartbeat hiding is
  belt-and-braces. Updated the `EventRiver.tsx` Route Model bullet. Verification metadata pinned until
  closeout stamps the task-34 code commit.
  with `@tanstack/react-virtual` over the store's bounded sliding window (newest ~2000 rows), mounting
  only the visible rows (no hard display cap) while staying memory-bounded; the `/api/events` backend
  also now filters `lifecycle.heartbeat` out of the raw river, so the formatter's heartbeat hiding is
  belt-and-braces. Updated the `EventRiver.tsx` Route Model bullet. Verification metadata pinned until
  closeout stamps the task-34 code commit.

- 2026-06-28T07:45+02:00 — Task 33 route impact: `Topology.tsx` now filters to active worktree groups via
  `activeTopologyInputs` (reading the store's `activeWorktreeGroups`) before `buildTopology`. Verification
  metadata pinned until closeout stamps the code commit.

  `activeTopologyInputs` (reading the store's `activeWorktreeGroups`) before `buildTopology`. Verification
  metadata pinned until closeout stamps the code commit.

  `activeTopologyInputs` (reading the store's `activeWorktreeGroups`) before `buildTopology`. Verification
  metadata pinned until closeout stamps the code commit.
  `activeTopologyInputs` (reading the store's `activeWorktreeGroups`) before `buildTopology`. Verification
  metadata pinned until closeout stamps the code commit.

- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: Event River no longer has a frontend newest-row
  cap and waits for the raw stream `ready` event before showing an empty feed, AttentionQueue
  dismiss/clear now optimistically suppresses lifecycle/gate/actionable-drift rows while writes are in
  flight, and `FlowTab.tsx` is documented as dormant because the Lifecycle Flow tab is hidden from the
  cockpit. Verification metadata pinned until closeout stamps the task-29 code commit.

  cap and waits for the raw stream `ready` event before showing an empty feed, AttentionQueue
  dismiss/clear now optimistically suppresses lifecycle/gate/actionable-drift rows while writes are in
  flight, and `FlowTab.tsx` is documented as dormant because the Lifecycle Flow tab is hidden from the
  cockpit. Verification metadata pinned until closeout stamps the task-29 code commit.

  cap and waits for the raw stream `ready` event before showing an empty feed, AttentionQueue
  dismiss/clear now optimistically suppresses lifecycle/gate/actionable-drift rows while writes are in
  flight, and `FlowTab.tsx` is documented as dormant because the Lifecycle Flow tab is hidden from the
  cockpit. Verification metadata pinned until closeout stamps the task-29 code commit.
  cap and waits for the raw stream `ready` event before showing an empty feed, AttentionQueue
  dismiss/clear now optimistically suppresses lifecycle/gate/actionable-drift rows while writes are in
  flight, and `FlowTab.tsx` is documented as dormant because the Lifecycle Flow tab is hidden from the
  cockpit. Verification metadata pinned until closeout stamps the task-29 code commit.

- 2026-06-28T05:38+02:00 — Task 29 route impact: Event River rendering now gates
  lifecycle-bound rows until lifecycle/enclosure/task-document context is available, while lifecycle-less
  workspace diagnostics can still render raw fallbacks. Verification metadata pinned until closeout
  stamps the task-29 code commit.

  lifecycle-bound rows until lifecycle/enclosure/task-document context is available, while lifecycle-less
  workspace diagnostics can still render raw fallbacks. Verification metadata pinned until closeout
  stamps the task-29 code commit.

  lifecycle-bound rows until lifecycle/enclosure/task-document context is available, while lifecycle-less
  workspace diagnostics can still render raw fallbacks. Verification metadata pinned until closeout
  stamps the task-29 code commit.
  lifecycle-bound rows until lifecycle/enclosure/task-document context is available, while lifecycle-less
  workspace diagnostics can still render raw fallbacks. Verification metadata pinned until closeout
  stamps the task-29 code commit.

- 2026-06-28T03:21+02:00 — Task 31 route impact: `LifecycleList` now matches active leaf task documents
  against either the file stem or the authored `TaskDocNode.id`, restoring browser-dashboard leaf 31 under
  its parent master in Operations; the Engine Room panel route also renders expected-but-missing provider
  roles using the new provider boot-node state. Verification metadata pinned until closeout stamps the
  task-31 code commit.

  against either the file stem or the authored `TaskDocNode.id`, restoring browser-dashboard leaf 31 under
  its parent master in Operations; the Engine Room panel route also renders expected-but-missing provider
  roles using the new provider boot-node state. Verification metadata pinned until closeout stamps the
  task-31 code commit.

  against either the file stem or the authored `TaskDocNode.id`, restoring browser-dashboard leaf 31 under
  its parent master in Operations; the Engine Room panel route also renders expected-but-missing provider
  roles using the new provider boot-node state. Verification metadata pinned until closeout stamps the
  task-31 code commit.
  against either the file stem or the authored `TaskDocNode.id`, restoring browser-dashboard leaf 31 under
  its parent master in Operations; the Engine Room panel route also renders expected-but-missing provider
  roles using the new provider boot-node state. Verification metadata pinned until closeout stamps the
  task-31 code commit.

- 2026-06-27T18:43+02:00 — Task 26 route impact: added the `FlowTab.tsx` **Lifecycle Flow** view to the
  panels inventory — a static (no-store) diagnostic of the build-job lifecycle in two regimes (a prose
  `RUNDOWN` front half emitted by `lifecycle_start` and a `LINEAR` worktree_start→lifecycle_end chain with
  gate `rides` annotations), wired as a full-bleed cockpit `flow` view and serving as the human-readable
  SPEC the task-27 `next_step.py` engine matches; dev frontend only (production bundle not rebuilt this
  task). Verification metadata pinned until closeout stamps the task-26 code commit.

  panels inventory — a static (no-store) diagnostic of the build-job lifecycle in two regimes (a prose
  `RUNDOWN` front half emitted by `lifecycle_start` and a `LINEAR` worktree_start→lifecycle_end chain with
  gate `rides` annotations), wired as a full-bleed cockpit `flow` view and serving as the human-readable
  SPEC the task-27 `next_step.py` engine matches; dev frontend only (production bundle not rebuilt this
  task). Verification metadata pinned until closeout stamps the task-26 code commit.

  panels inventory — a static (no-store) diagnostic of the build-job lifecycle in two regimes (a prose
  `RUNDOWN` front half emitted by `lifecycle_start` and a `LINEAR` worktree_start→lifecycle_end chain with
  gate `rides` annotations), wired as a full-bleed cockpit `flow` view and serving as the human-readable
  SPEC the task-27 `next_step.py` engine matches; dev frontend only (production bundle not rebuilt this
  task). Verification metadata pinned until closeout stamps the task-26 code commit.
  panels inventory — a static (no-store) diagnostic of the build-job lifecycle in two regimes (a prose
  `RUNDOWN` front half emitted by `lifecycle_start` and a `LINEAR` worktree_start→lifecycle_end chain with
  gate `rides` annotations), wired as a full-bleed cockpit `flow` view and serving as the human-readable
  SPEC the task-27 `next_step.py` engine matches; dev frontend only (production bundle not rebuilt this
  task). Verification metadata pinned until closeout stamps the task-26 code commit.

- 2026-06-27T03:04+02:00 — Task 22 follow-up: Chats removed the local Hide row action; End is now the
  only session-list action, and id-bearing terminate invalidations remove rows across tabs without
  allowing stale catalog echoes to repaint them.

  only session-list action, and id-bearing terminate invalidations remove rows across tabs without
  allowing stale catalog echoes to repaint them.

  only session-list action, and id-bearing terminate invalidations remove rows across tabs without
  allowing stale catalog echoes to repaint them.
  only session-list action, and id-bearing terminate invalidations remove rows across tabs without
  allowing stale catalog echoes to repaint them.

- 2026-06-27T01:25+02:00 — Task 22 follow-up: Chats now listens for cross-tab terminal catalog
  invalidations, re-fetches durable rows when another tab opens/ends sessions, and broadcasts after
  backend-confirmed End so multiple browser tabs stay in sync.

  invalidations, re-fetches durable rows when another tab opens/ends sessions, and broadcasts after
  backend-confirmed End so multiple browser tabs stay in sync.

  invalidations, re-fetches durable rows when another tab opens/ends sessions, and broadcasts after
  backend-confirmed End so multiple browser tabs stay in sync.
  invalidations, re-fetches durable rows when another tab opens/ends sessions, and broadcasts after
  backend-confirmed End so multiple browser tabs stay in sync.

- 2026-06-27T01:03+02:00 — Task 22 follow-up: Chats treats End/terminate as label release, so terminated
  Claude chats do not force the next Claude label upward.

  Claude chats do not force the next Claude label upward.

  Claude chats do not force the next Claude label upward.
  Claude chats do not force the next Claude label upward.

- 2026-06-27T00:25+02:00 — Task 22 follow-up: corrected the Chats route model for mount-on-first-selection
  after refresh; hidden restored xterms no longer initialize before they are selected, and visited tabs
  still keep their xterm buffers.

  after refresh; hidden restored xterms no longer initialize before they are selected, and visited tabs
  still keep their xterm buffers.

  after refresh; hidden restored xterms no longer initialize before they are selected, and visited tabs
  still keep their xterm buffers.
  after refresh; hidden restored xterms no longer initialize before they are selected, and visited tabs
  still keep their xterm buffers.

- 2026-06-26T23:15+02:00 — Task 22 route impact: `Chats.tsx` and `SessionList.tsx` now expose durable
  catalog sessions, status badges/panels, last-active restore, and backend terminate for dashboard-owned
  terminals. Verification metadata pinned until closeout stamps the code commit.

  catalog sessions, status badges/panels, last-active restore, and backend terminate for dashboard-owned
  terminals. Verification metadata pinned until closeout stamps the code commit.

  catalog sessions, status badges/panels, last-active restore, and backend terminate for dashboard-owned
  terminals. Verification metadata pinned until closeout stamps the code commit.
  catalog sessions, status badges/panels, last-active restore, and backend terminate for dashboard-owned
  terminals. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-26T20:18+02:00 — Task 21 route impact: `DetailPanel` master readers now show the
  server-projected `seriesTokenTotal` aggregate, with component coverage in `DetailPanel.test.tsx`.
  Verification metadata pinned until closeout stamps the code commit.

  server-projected `seriesTokenTotal` aggregate, with component coverage in `DetailPanel.test.tsx`.
  Verification metadata pinned until closeout stamps the code commit.

  server-projected `seriesTokenTotal` aggregate, with component coverage in `DetailPanel.test.tsx`.
  Verification metadata pinned until closeout stamps the code commit.
  server-projected `seriesTokenTotal` aggregate, with component coverage in `DetailPanel.test.tsx`.
  Verification metadata pinned until closeout stamps the code commit.

- 2026-06-26T19:40+02:00 — Task 20 reopened: Event River route model now records
  the task-document title fallback for retained event-history rows whose
  lifecycle id no longer has a live lifecycle projection. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.

  the task-document title fallback for retained event-history rows whose
  lifecycle id no longer has a live lifecycle projection. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.

  the task-document title fallback for retained event-history rows whose
  lifecycle id no longer has a live lifecycle projection. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.
  the task-document title fallback for retained event-history rows whose
  lifecycle id no longer has a live lifecycle projection. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.

- 2026-06-26T18:14+02:00 — Task 20 route impact: Event River now includes the
  new `eventSummary.ts` formatter module and renders a readable activity feed
  over known observer events while preserving raw-event diagnostics and trust
  provenance. Verification metadata pinned until closeout stamps the task-20
  code commit.

  new `eventSummary.ts` formatter module and renders a readable activity feed
  over known observer events while preserving raw-event diagnostics and trust
  provenance. Verification metadata pinned until closeout stamps the task-20
  code commit.

  new `eventSummary.ts` formatter module and renders a readable activity feed
  over known observer events while preserving raw-event diagnostics and trust
  provenance. Verification metadata pinned until closeout stamps the task-20
  code commit.
  new `eventSummary.ts` formatter module and renders a readable activity feed
  over known observer events while preserving raw-event diagnostics and trust
  provenance. Verification metadata pinned until closeout stamps the task-20
  code commit.

- 2026-06-25T14:02+02:00 — Task 24 reopened: `AttentionQueue` Clear now includes stale gate-only rows and sends gate-id-only cancel through the serving route.

- 2026-06-25T13:20+02:00 — Task 23/24: panels route now covers gate Dismiss/delete, attention Clear, and the `AgentPickupIndicator` waiting-for-agent/check-chat task-row feedback.

- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: `GateResponder` now has separate durable
  Yes/No decision paths and a message-only Chat path, renders readable gate previews with diagnostics
  behind details, and gives leaf prompt previews a 480px resizable area. `AttentionQueue` now renders
  lifecycle-bound rows with task id/title first. Verification metadata pinned until closeout stamps the
  code commit.

  Yes/No decision paths and a message-only Chat path, renders readable gate previews with diagnostics
  behind details, and gives leaf prompt previews a 480px resizable area. `AttentionQueue` now renders
  lifecycle-bound rows with task id/title first. Verification metadata pinned until closeout stamps the
  code commit.

  Yes/No decision paths and a message-only Chat path, renders readable gate previews with diagnostics
  behind details, and gives leaf prompt previews a 480px resizable area. `AttentionQueue` now renders
  lifecycle-bound rows with task id/title first. Verification metadata pinned until closeout stamps the
  code commit.
  Yes/No decision paths and a message-only Chat path, renders readable gate previews with diagnostics
  behind details, and gives leaf prompt previews a 480px resizable area. `AttentionQueue` now renders
  lifecycle-bound rows with task id/title first. Verification metadata pinned until closeout stamps the
  code commit.

- 2026-06-25T02:53+02:00 — Operations title-overflow correction: `LifecycleList` now constrains the
  listbox/section grid tracks, row minimum widths, and secondary metadata chips so long task titles
  ellipsize inside the left rail instead of creating a horizontal scrollbar or disappearing. Detail
  lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata pinned
  until closeout stamps the code commit.

  listbox/section grid tracks, row minimum widths, and secondary metadata chips so long task titles
  ellipsize inside the left rail instead of creating a horizontal scrollbar or disappearing. Detail
  lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata pinned
  until closeout stamps the code commit.

  listbox/section grid tracks, row minimum widths, and secondary metadata chips so long task titles
  ellipsize inside the left rail instead of creating a horizontal scrollbar or disappearing. Detail
  lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata pinned
  until closeout stamps the code commit.
  listbox/section grid tracks, row minimum widths, and secondary metadata chips so long task titles
  ellipsize inside the left rail instead of creating a horizontal scrollbar or disappearing. Detail
  lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata pinned
  until closeout stamps the code commit.

- 2026-06-24T21:49+02:00 — Task 17 route correction: cleanup-completed leaf enclosures no longer count
  as active sidebar enclosures; their task docs remain reachable through master/taskdoc navigation.
  Verification metadata pinned until closeout stamps the code commit.

  as active sidebar enclosures; their task docs remain reachable through master/taskdoc navigation.
  Verification metadata pinned until closeout stamps the code commit.

  as active sidebar enclosures; their task docs remain reachable through master/taskdoc navigation.
  Verification metadata pinned until closeout stamps the code commit.
  as active sidebar enclosures; their task docs remain reachable through master/taskdoc navigation.
  Verification metadata pinned until closeout stamps the code commit.

- 2026-06-24T18:13+02:00 — Empty-state backdrop zoom-stability pass: refreshed the
  `EmptyStateBackdrop.tsx` route-model bullet for the final static direct-video contract. The shared panel
  still provides the same effects-gated boomerang-video atmosphere, but runtime zoom layers are excluded;
  the 60fps MP4 assets own the slow zoom/cadence. Detail lives in the `EmptyStateBackdrop.tsx` and
  `EmptyStateBackdrop.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.

  `EmptyStateBackdrop.tsx` route-model bullet for the final static direct-video contract. The shared panel
  still provides the same effects-gated boomerang-video atmosphere, but runtime zoom layers are excluded;
  the 60fps MP4 assets own the slow zoom/cadence. Detail lives in the `EmptyStateBackdrop.tsx` and
  `EmptyStateBackdrop.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.

  `EmptyStateBackdrop.tsx` route-model bullet for the final static direct-video contract. The shared panel
  still provides the same effects-gated boomerang-video atmosphere, but runtime zoom layers are excluded;
  the 60fps MP4 assets own the slow zoom/cadence. Detail lives in the `EmptyStateBackdrop.tsx` and
  `EmptyStateBackdrop.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.
  `EmptyStateBackdrop.tsx` route-model bullet for the final static direct-video contract. The shared panel
  still provides the same effects-gated boomerang-video atmosphere, but runtime zoom layers are excluded;
  the 60fps MP4 assets own the slow zoom/cadence. Detail lives in the `EmptyStateBackdrop.tsx` and
  `EmptyStateBackdrop.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.

- 2026-06-24T18:11+02:00 — Task 17 route correction: Operations and Detail now label authored leaf rows
  from the child `TaskDocNode.id`, with parent sub-task `number` only as fallback data. Verification
  metadata pinned until closeout stamps the code commit.

  from the child `TaskDocNode.id`, with parent sub-task `number` only as fallback data. Verification
  metadata pinned until closeout stamps the code commit.

  from the child `TaskDocNode.id`, with parent sub-task `number` only as fallback data. Verification
  metadata pinned until closeout stamps the code commit.
  from the child `TaskDocNode.id`, with parent sub-task `number` only as fallback data. Verification
  metadata pinned until closeout stamps the code commit.

- 2026-06-24T18:02+02:00 — Task 17 route correction: Operations and Detail now display structured
  sub-task numbers for leaf labels, while creation metadata controls ordering/placement and no filename
  parsing is introduced. Verification metadata pinned until closeout stamps the code commit.

  sub-task numbers for leaf labels, while creation metadata controls ordering/placement and no filename
  parsing is introduced. Verification metadata pinned until closeout stamps the code commit.

  sub-task numbers for leaf labels, while creation metadata controls ordering/placement and no filename
  parsing is introduced. Verification metadata pinned until closeout stamps the code commit.
  sub-task numbers for leaf labels, while creation metadata controls ordering/placement and no filename
  parsing is introduced. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy route update: `LifecycleList` now nests
  admitted active leaves beneath their parent/root task in `BY REPO`, and `DetailPanel` gives directly
  opened leaf documents a structured parent/root backlink. Verification
  metadata pinned until closeout stamps the code commit.

  admitted active leaves beneath their parent/root task in `BY REPO`, and `DetailPanel` gives directly
  opened leaf documents a structured parent/root backlink. Verification
  metadata pinned until closeout stamps the code commit.

  admitted active leaves beneath their parent/root task in `BY REPO`, and `DetailPanel` gives directly
  opened leaf documents a structured parent/root backlink. Verification
  metadata pinned until closeout stamps the code commit.
  admitted active leaves beneath their parent/root task in `BY REPO`, and `DetailPanel` gives directly
  opened leaf documents a structured parent/root backlink. Verification
  metadata pinned until closeout stamps the code commit.

- 2026-06-24T17:20+02:00 — Task 17 sidebar/master navigation route correction: `LifecycleList` now scopes
  the Operations sidebar to root/master docs, enclosure-matched leaves, series fallbacks, and
  enclosure-backed runtime fallbacks, while `DetailPanel` keeps master sub-task navigation wired to the
  full projected sibling document pool. Verification metadata pinned until closeout stamps the code commit.

  the Operations sidebar to root/master docs, enclosure-matched leaves, series fallbacks, and
  enclosure-backed runtime fallbacks, while `DetailPanel` keeps master sub-task navigation wired to the
  full projected sibling document pool. Verification metadata pinned until closeout stamps the code commit.

  the Operations sidebar to root/master docs, enclosure-matched leaves, series fallbacks, and
  enclosure-backed runtime fallbacks, while `DetailPanel` keeps master sub-task navigation wired to the
  full projected sibling document pool. Verification metadata pinned until closeout stamps the code commit.
  the Operations sidebar to root/master docs, enclosure-matched leaves, series fallbacks, and
  enclosure-backed runtime fallbacks, while `DetailPanel` keeps master sub-task navigation wired to the
  full projected sibling document pool. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: `LifecycleList` is task-document-first
  with typed `taskdoc:` / `series:` / `lifecycle:` row keys, completed unarchived docs stay visible,
  and `DetailPanel` renders concrete selected documents before lifecycle/series fallbacks. Verification
  metadata pinned until closeout stamps the code commit.

  with typed `taskdoc:` / `series:` / `lifecycle:` row keys, completed unarchived docs stay visible,
  and `DetailPanel` renders concrete selected documents before lifecycle/series fallbacks. Verification
  metadata pinned until closeout stamps the code commit.

  with typed `taskdoc:` / `series:` / `lifecycle:` row keys, completed unarchived docs stay visible,
  and `DetailPanel` renders concrete selected documents before lifecycle/series fallbacks. Verification
  metadata pinned until closeout stamps the code commit.
  with typed `taskdoc:` / `series:` / `lifecycle:` row keys, completed unarchived docs stay visible,
  and `DetailPanel` renders concrete selected documents before lifecycle/series fallbacks. Verification
  metadata pinned until closeout stamps the code commit.

- 2026-06-24T15:37+02:00 — Task 17 follow-up route correction: live projection inspection showed
  `analytics.series` is the master surface while leaf rows carry parent `taskName`; the DetailPanel route
  now bridges to the master only for root task identity and otherwise requires projected leaf task docs
  for leaf reader content. Verification metadata pinned until closeout stamps the follow-up code commit.

  `analytics.series` is the master surface while leaf rows carry parent `taskName`; the DetailPanel route
  now bridges to the master only for root task identity and otherwise requires projected leaf task docs
  for leaf reader content. Verification metadata pinned until closeout stamps the follow-up code commit.

  `analytics.series` is the master surface while leaf rows carry parent `taskName`; the DetailPanel route
  now bridges to the master only for root task identity and otherwise requires projected leaf task docs
  for leaf reader content. Verification metadata pinned until closeout stamps the follow-up code commit.
  `analytics.series` is the master surface while leaf rows carry parent `taskName`; the DetailPanel route
  now bridges to the master only for root task identity and otherwise requires projected leaf task docs
  for leaf reader content. Verification metadata pinned until closeout stamps the follow-up code commit.

- 2026-06-24T15:23+02:00 — Task 17 follow-up route impact: clarified the DetailPanel identity rule
  that `taskName` is parent/root-series metadata for leaf lifecycles; direct leaf task documents render
  before the folder-keyed master bridge. Verification metadata pinned until closeout stamps the
  follow-up code commit.

  that `taskName` is parent/root-series metadata for leaf lifecycles; direct leaf task documents render
  before the folder-keyed master bridge. Verification metadata pinned until closeout stamps the
  follow-up code commit.

  that `taskName` is parent/root-series metadata for leaf lifecycles; direct leaf task documents render
  before the folder-keyed master bridge. Verification metadata pinned until closeout stamps the
  follow-up code commit.
  that `taskName` is parent/root-series metadata for leaf lifecycles; direct leaf task documents render
  before the folder-keyed master bridge. Verification metadata pinned until closeout stamps the
  follow-up code commit.

- 2026-06-24T13:59+02:00 — Task 17 follow-up route impact: refreshed the `DetailPanel.tsx` route model
  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.

  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.

  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.
  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.
  for root master rows that select an inferred task-id lifecycle; the panel now uses projected
  enclosure `taskName` to find the folder-keyed `analytics.series` master. Verification metadata pinned
  until closeout stamps the follow-up code commit.

- 2026-06-24T12:53+02:00 — Task 17 follow-up route impact: refreshed the `DetailPanel.tsx` route model
  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.

  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.

  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.
  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.
  for root master rows that select an inferred task-id lifecycle; the panel now uses projected
  enclosure `taskName` to find the folder-keyed `analytics.series` master. Verification metadata pinned
  until closeout stamps the follow-up code commit.

- 2026-06-24T12:37+02:00 — Operations title-overflow fix: refreshed the `LifecycleList.tsx` route model
  for single-line title ellipsis and native hover titles carrying the full task label plus row context.
  Detail lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata
  pinned until closeout stamps the code commit.

  for single-line title ellipsis and native hover titles carrying the full task label plus row context.
  Detail lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata
  pinned until closeout stamps the code commit.

  for single-line title ellipsis and native hover titles carrying the full task label plus row context.
  Detail lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata
  pinned until closeout stamps the code commit.
  for single-line title ellipsis and native hover titles carrying the full task label plus row context.
  Detail lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata
  pinned until closeout stamps the code commit.

- 2026-06-24T12:21+02:00 — Task 17 route impact: refreshed the `DetailPanel.tsx` route model for
  folder-keyed `analytics.series` master rendering, labelled master sub-task rows, structured
  creation-order sorting, and the new top Progress section in leaf readers. Verification metadata
  pinned until closeout stamps the code commit.

  folder-keyed `analytics.series` master rendering, labelled master sub-task rows, structured
  creation-order sorting, and the new top Progress section in leaf readers. Verification metadata
  pinned until closeout stamps the code commit.

  folder-keyed `analytics.series` master rendering, labelled master sub-task rows, structured
  creation-order sorting, and the new top Progress section in leaf readers. Verification metadata
  pinned until closeout stamps the code commit.
  folder-keyed `analytics.series` master rendering, labelled master sub-task rows, structured
  creation-order sorting, and the new top Progress section in leaf readers. Verification metadata
  pinned until closeout stamps the code commit.

- 2026-06-24T08:59+02:00 — Detail task-document correction: refreshed the `DetailPanel.tsx` route model
  for promoted leaf lifecycles whose visible title comes from enclosure metadata while readable content
  remains limited to matching JSON task documents. Verification metadata pinned until closeout stamps
  the code commit.

  for promoted leaf lifecycles whose visible title comes from enclosure metadata while readable content
  remains limited to matching JSON task documents. Verification metadata pinned until closeout stamps
  the code commit.

  for promoted leaf lifecycles whose visible title comes from enclosure metadata while readable content
  remains limited to matching JSON task documents. Verification metadata pinned until closeout stamps
  the code commit.
  for promoted leaf lifecycles whose visible title comes from enclosure metadata while readable content
  remains limited to matching JSON task documents. Verification metadata pinned until closeout stamps
  the code commit.

- 2026-06-24T08:40+02:00 — Operations label fix: refreshed the `LifecycleList.tsx` Route Model bullet
  for enclosure/task-backed row labels, covering promoted fleeting lifecycles that should display the
  leaf enclosure name rather than the stable raw lifecycle id. Detail lives in the `LifecycleList.tsx`
  and `LifecycleList.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.

  for enclosure/task-backed row labels, covering promoted fleeting lifecycles that should display the
  leaf enclosure name rather than the stable raw lifecycle id. Detail lives in the `LifecycleList.tsx`
  and `LifecycleList.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.

  for enclosure/task-backed row labels, covering promoted fleeting lifecycles that should display the
  leaf enclosure name rather than the stable raw lifecycle id. Detail lives in the `LifecycleList.tsx`
  and `LifecycleList.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.
  for enclosure/task-backed row labels, covering promoted fleeting lifecycles that should display the
  leaf enclosure name rather than the stable raw lifecycle id. Detail lives in the `LifecycleList.tsx`
  and `LifecycleList.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.

- 2026-06-24T06:26+02:00 — Engine Room official-strip aggregation: the route model now records that
  `EngineRoom.tsx` groups official workspace providers by provider label + runtime state, rendering duplicate
  same-state CGCs as counted chips with hover-title repo detail. Detail lives in the `EngineRoom.tsx` and
  `EngineRoom.test.tsx` sidecars. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.

  `EngineRoom.tsx` groups official workspace providers by provider label + runtime state, rendering duplicate
  same-state CGCs as counted chips with hover-title repo detail. Detail lives in the `EngineRoom.tsx` and
  `EngineRoom.test.tsx` sidecars. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.

  `EngineRoom.tsx` groups official workspace providers by provider label + runtime state, rendering duplicate
  same-state CGCs as counted chips with hover-title repo detail. Detail lives in the `EngineRoom.tsx` and
  `EngineRoom.test.tsx` sidecars. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.
  `EngineRoom.tsx` groups official workspace providers by provider label + runtime state, rendering duplicate
  same-state CGCs as counted chips with hover-title repo detail. Detail lives in the `EngineRoom.tsx` and
  `EngineRoom.test.tsx` sidecars. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.

- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: `GateResponder` now routes missing-hosted-session responses to the external operator inbox through `data/operatorInbox`, with queued/error status coverage in `GateResponder.test.tsx`. Verification metadata pinned until closeout stamps the task-10 code commit.

- 2026-06-23T13:45+02:00 — Task 11: added `GateResponder.tsx` / `.test.tsx` and updated the panel route
  model for chat-routed Gate Respond. `DetailPanel` now uses the responder for durable gates and proto
  asks; `LifecycleList` shows gate badges; `Chats` / `SessionList` / `HighlightComposer` carry hosted
  chat lifecycle identity; Hangar and Engine Room diagnostics use the responder as the secondary
  worktree-gate surface. Verification metadata pinned until closeout stamps the task-11 code commit.

  model for chat-routed Gate Respond. `DetailPanel` now uses the responder for durable gates and proto
  asks; `LifecycleList` shows gate badges; `Chats` / `SessionList` / `HighlightComposer` carry hosted
  chat lifecycle identity; Hangar and Engine Room diagnostics use the responder as the secondary
  worktree-gate surface. Verification metadata pinned until closeout stamps the task-11 code commit.

  model for chat-routed Gate Respond. `DetailPanel` now uses the responder for durable gates and proto
  asks; `LifecycleList` shows gate badges; `Chats` / `SessionList` / `HighlightComposer` carry hosted
  chat lifecycle identity; Hangar and Engine Room diagnostics use the responder as the secondary
  worktree-gate surface. Verification metadata pinned until closeout stamps the task-11 code commit.
  model for chat-routed Gate Respond. `DetailPanel` now uses the responder for durable gates and proto
  asks; `LifecycleList` shows gate badges; `Chats` / `SessionList` / `HighlightComposer` carry hosted
  chat lifecycle identity; Hangar and Engine Room diagnostics use the responder as the secondary
  worktree-gate surface. Verification metadata pinned until closeout stamps the task-11 code commit.

- 2026-06-23T13:35+02:00 — No route impact: slice-12 topology render fix — `Topology.tsx` made the constellation canvas absolutely-positioned (out of flow → no ResizeObserver growth loop) and rendered the `Panel` with `fill` (so it fills the slot). Behaviour-preserving layout fix; the panels route model is unchanged.

- 2026-06-23T07:25+02:00 — UI copy rename (user-facing lifecycle → task): refreshed the `LifecycleList.tsx`
  Route Model bullet for the operations panel's "Tasks" copy (header `Tasks · {n}`, empty state `No tasks.`,
  aria-labels "Group tasks by" / "Tasks") and the `DetailPanel.tsx` bullet for its task-facing placeholders
  ("Select a task to inspect…", "No task document bound to this task."). Display copy only — the unit is still
  the `lifecycle` under the hood; the eight-panel route inventory is unchanged. Detail lives in the
  `LifecycleList.tsx` / `DetailPanel.tsx` sidecars. Verification metadata pinned until closeout stamps the
  rename code commit.

  Route Model bullet for the operations panel's "Tasks" copy (header `Tasks · {n}`, empty state `No tasks.`,
  aria-labels "Group tasks by" / "Tasks") and the `DetailPanel.tsx` bullet for its task-facing placeholders
  ("Select a task to inspect…", "No task document bound to this task."). Display copy only — the unit is still
  the `lifecycle` under the hood; the eight-panel route inventory is unchanged. Detail lives in the
  `LifecycleList.tsx` / `DetailPanel.tsx` sidecars. Verification metadata pinned until closeout stamps the
  rename code commit.

  Route Model bullet for the operations panel's "Tasks" copy (header `Tasks · {n}`, empty state `No tasks.`,
  aria-labels "Group tasks by" / "Tasks") and the `DetailPanel.tsx` bullet for its task-facing placeholders
  ("Select a task to inspect…", "No task document bound to this task."). Display copy only — the unit is still
  the `lifecycle` under the hood; the eight-panel route inventory is unchanged. Detail lives in the
  `LifecycleList.tsx` / `DetailPanel.tsx` sidecars. Verification metadata pinned until closeout stamps the
  rename code commit.
  Route Model bullet for the operations panel's "Tasks" copy (header `Tasks · {n}`, empty state `No tasks.`,
  aria-labels "Group tasks by" / "Tasks") and the `DetailPanel.tsx` bullet for its task-facing placeholders
  ("Select a task to inspect…", "No task document bound to this task."). Display copy only — the unit is still
  the `lifecycle` under the hood; the eight-panel route inventory is unchanged. Detail lives in the
  `LifecycleList.tsx` / `DetailPanel.tsx` sidecars. Verification metadata pinned until closeout stamps the
  rename code commit.

- 2026-06-23T04:20+02:00 — Slice 07b polish: added the shared `EmptyStateBackdrop.tsx` panel — a faint,
  effects-gated boomerang-video atmosphere behind centered empty-state text (lifted from the engine-room
  G6 backdrop) — and wired it into `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s
  no-session state (adjutant); covered by `EmptyStateBackdrop.test.tsx`. Added a Route Model bullet for
  the new shared panel; detail lives in its sidecar + the `DetailPanel` / `Chats` sidecars. Verification
  metadata pinned until closeout stamps the slice-07b code commit.

  effects-gated boomerang-video atmosphere behind centered empty-state text (lifted from the engine-room
  G6 backdrop) — and wired it into `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s
  no-session state (adjutant); covered by `EmptyStateBackdrop.test.tsx`. Added a Route Model bullet for
  the new shared panel; detail lives in its sidecar + the `DetailPanel` / `Chats` sidecars. Verification
  metadata pinned until closeout stamps the slice-07b code commit.

  effects-gated boomerang-video atmosphere behind centered empty-state text (lifted from the engine-room
  G6 backdrop) — and wired it into `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s
  no-session state (adjutant); covered by `EmptyStateBackdrop.test.tsx`. Added a Route Model bullet for
  the new shared panel; detail lives in its sidecar + the `DetailPanel` / `Chats` sidecars. Verification
  metadata pinned until closeout stamps the slice-07b code commit.
  effects-gated boomerang-video atmosphere behind centered empty-state text (lifted from the engine-room
  G6 backdrop) — and wired it into `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s
  no-session state (adjutant); covered by `EmptyStateBackdrop.test.tsx`. Added a Route Model bullet for
  the new shared panel; detail lives in its sidecar + the `DetailPanel` / `Chats` sidecars. Verification
  metadata pinned until closeout stamps the slice-07b code commit.

- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1 gives `EventRiver.tsx` its one per-kind treatment (a `read.packet` renders "Read: <basename>" + the read's repo + full-path-on-hover, everything else generic) and adds `EventRiver.test.tsx`; no new panel enters the route inventory and the eight-panel route model this overview describes is unchanged — detail lives in the `EventRiver.tsx` / `EventRiver.test.tsx` sidecars. Verification metadata pinned until closeout stamps the slice-07b code commit.

- 2026-06-22T16:00+02:00 — Route refresh (05o review round): `EngineRoom.tsx` keys its process-map canvas by the store `gen` so a dev-bench scenario switch remounts it cleanly (no cross-scenario overlay bleed), and the right-panel `BootTimeline` now renders a THREE-WAY sequence — Boot / Steady state / Tear-down — with the contract anchor leading the boot order and the abandon/conflict tear-down step states corrected; detail lives in the per-file sidecars under `panels/` and `panels/engine-room/`. Verification metadata pinned until closeout stamps the 05o code commit.

- 2026-06-21T02:44+02:00 — slice 6g: `DetailPanel` became the task-document **master-series reader** — master overview + clickable sub-task index (pinned in the sticky head + in-section), in-panel drill-in into a slice reader with the back/parent up-link in the sticky panel header, markdown-rendered prose (`grammar/Markdown`), and cross-master "→" links + parent breadcrumb that jump lifecycles (`onOpenLifecycle`). Verification metadata pinned until closeout stamps the 6g code commit.

- 2026-06-19T15:59+02:00 — Task 6 slice 6f-1: added `HighlightComposer.tsx` (+ `data/selection.ts`) — a cockpit-wide composer a text selection raises to send a context package (selection + message) into a chat session (single/selector/create-on-Enter + ＋ new chat), reusing the live stdin channel. No silent action. Covered by `HighlightComposer.test.tsx` + `data/selection.test.ts`. Verification metadata pinned until closeout stamps the 6f-1 code commit.

- 2026-06-19T14:05+02:00 — Task 6 slice 6e-4: the **Chats** view's session registry moved into the `data/sessions` store, and every open session's `Terminal` now stays mounted (inactive ones hidden via CSS) so switching tabs no longer unmounts a live terminal; the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal (`os.login_tty`) so tmux honors resize. Persistence covered by `Chats.test.tsx` + the new `data/sessions.test.ts`. Verification metadata pinned until closeout stamps the 6e-4 code commit.

- 2026-06-19T06:39+02:00 — No route impact: an engine-room crash fix guards the `landing` read in `engine-room/EnclosureCanvas` (a node without the slice-5h `landing` field no longer crashes); the `panels/` route model this overview describes is unchanged — detail lives in the `engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-19T05:48+02:00 — Task 6 slice 6e-3: the **Chats** view gained a `SessionComposer` (context injection) docked below the terminal — it sends a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f); covered by `SessionComposer.test.tsx`. Verification metadata pinned until closeout stamps the 6e-3 code commit.

- 2026-06-19T04:38+02:00 — Task 6 slice 6e-2c: the **Chats** view's horizontal session tab strip became a left-rail **`SessionList`** switcher (extracted to a React Aria `GridList` component — single-select = active session, per-row close ✕; `SessionList.test.tsx`), and the per-harness launch buttons now share ＋ Terminal's golden look (the grey ones read as disabled). Refreshed the Chats Route Model bullet + the React Aria note. Verification metadata pinned until closeout stamps the 6e-2c code commit.

- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: the **Chats** view gained per-harness launch buttons — `fetchHarnesses` (`GET /api/harnesses`) renders a button per **detected** harness (Claude Code/Codex/Pi.dev, icon-left/name-right) beside ＋ Terminal; added `Chats.test.tsx` (detection-driven render). Refreshed the Chats Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2b code commit.

- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover threads `officialLedger` through `EngineRoom` → `EnclosureProcessMap` (resolved from `analytics.ledgers` by repo) for the official coupler; the `panels/` route model this overview describes is unchanged — detail lives in the `engine-room/` overview + the `EngineRoom.tsx` / `EnclosureProcessMap.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: the **Chats** view became a **create** surface — a "＋ Terminal" control spawns a dashboard-owned shell session via the `POST /api/terminal` opener (no longer attaching to a store lifecycle), rendered as a closable tab. Refreshed the Chats Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2a code commit.

- 2026-06-18T16:50+02:00 — Task 6 slice 6e-1: added the **Chats** view (`Chats.tsx` + the lazy `Terminal.tsx` xterm wrapper) — the visible Mode B2 surface, the panels' first bidirectional-interactive surface (keystrokes/resize ↔ PTY over the `data/terminal` WebSocket). Updated the Route Model + the near-read-only invariant. Verification metadata pinned until closeout stamps the 6e-1 code commit.

- 2026-06-18T15:00+02:00 — Task 6 slice 6c Part B: `DetailPanel`'s display-only gate banner became the **Gate Review drawer** — the durable gate's decision verbs POST to `/api/actions` via the new `data/actions.ts` (the panels' first write path); the proto-gate `ask` falls back to the display banner. Verification metadata pinned until closeout stamps the 6c Part B code commit.

- 2026-06-17T22:45+02:00 — No route impact: the engine-room visual-parity pass (the 5g G6 backdrop + the restored
  SVG decal layer + the `grammar/Panel` `fill` height fix) is internal to the `engine-room/` route and the
  `grammar/Panel` primitive; the panels route model (the eight panels + their roles) this overview describes
  is unchanged — detail lives in the `engine-room/` + `grammar/` overviews and the `EngineRoom` sidecar.

  SVG decal layer + the `grammar/Panel` `fill` height fix) is internal to the `engine-room/` route and the
  `grammar/Panel` primitive; the panels route model (the eight panels + their roles) this overview describes
  is unchanged — detail lives in the `engine-room/` + `grammar/` overviews and the `EngineRoom` sidecar.

  SVG decal layer + the `grammar/Panel` `fill` height fix) is internal to the `engine-room/` route and the
  `grammar/Panel` primitive; the panels route model (the eight panels + their roles) this overview describes
  is unchanged — detail lives in the `engine-room/` + `grammar/` overviews and the `EngineRoom` sidecar.
  SVG decal layer + the `grammar/Panel` `fill` height fix) is internal to the `engine-room/` route and the
  `grammar/Panel` primitive; the panels route model (the eight panels + their roles) this overview describes
  is unchanged — detail lives in the `engine-room/` + `grammar/` overviews and the `EngineRoom` sidecar.

- 2026-06-17T16:15+02:00 — No content impact: slice 5g G5 (Engine Room live/teardown overlays t12b/t14c/t18 +
  the green=active engine palette + the enclosure-rail scroll fix) is internal to the `engine-room/` route;
  the panels route model (the eight panels + their roles) this overview describes is unchanged — detail
  lives in the `engine-room/` overview + sidecars.

  the green=active engine palette + the enclosure-rail scroll fix) is internal to the `engine-room/` route;
  the panels route model (the eight panels + their roles) this overview describes is unchanged — detail
  lives in the `engine-room/` overview + sidecars.

  the green=active engine palette + the enclosure-rail scroll fix) is internal to the `engine-room/` route;
  the panels route model (the eight panels + their roles) this overview describes is unchanged — detail
  lives in the `engine-room/` overview + sidecars.
  the green=active engine palette + the enclosure-rail scroll fix) is internal to the `engine-room/` route;
  the panels route model (the eight panels + their roles) this overview describes is unchanged — detail
  lives in the `engine-room/` overview + sidecars.

- 2026-06-16T03:50+02:00 — No content impact: slice 5f S5 added the Engine Room header's lifecycle-phase pulse (the `phaseChip` animates while the selected enclosure is in a human-gated landing phase, T12–T18) + `EngineRoom.test.tsx`; the panels route model (the eight panels + their roles) this overview describes is unchanged.

- 2026-06-16T03:35+02:00 — No content impact: slice 5f S3 added `AttentionQueue.test.tsx` (a §9 blocked-start alarm-parity render test — no `AttentionQueue` source change; the panel renders items generically by severity) and the Engine Room T4 promotion morph (internal to `engine-room/`); the panels route model this overview describes is unchanged.

- 2026-06-16T02:30+02:00 — No content impact: slice 5f S1 gave `EngineRoom.tsx` a full-width 3-zone layout (header + stack list | pod stage | boot+diagnostics-right, §4.2); the panels route model (the eight panels + their roles) this overview describes is unchanged — detail lives in the `engine-room/` overview + sidecars.

- 2026-06-16T01:55+02:00 — No content impact: slice 5f S0's Engine Room motion foundations (the `useShouldAnimate` honest-motion gate, SVG conduits, and `worktreeGroup` keying) are internal to the `engine-room/` route — captured in its overview + file sidecars; the panels route model this overview describes is unchanged.

- 2026-06-15T19:35+02:00 — slice 5e: reworked `EngineRoom.tsx` into an enclosure-centered process map
  backed by the new `engine-room/` module (pure `buildEngineRoomModel` + Panda/React Aria
  components: stack list, process map, boot timeline, diagnostics); added the `engine-room/` child route.

  backed by the new `engine-room/` module (pure `buildEngineRoomModel` + Panda/React Aria
  components: stack list, process map, boot timeline, diagnostics); added the `engine-room/` child route.

  backed by the new `engine-room/` module (pure `buildEngineRoomModel` + Panda/React Aria
  components: stack list, process map, boot timeline, diagnostics); added the `engine-room/` child route.
  backed by the new `engine-room/` module (pure `buildEngineRoomModel` + Panda/React Aria
  components: stack list, process map, boot timeline, diagnostics); added the `engine-room/` child route.

- 2026-06-15T17:00+02:00 — Created for slice 5d: all eight panels migrated onto the `Panel` primitive +
  co-located Panda styling, with React Aria `ListBox` (LifecycleList) and `ToggleButtonGroup`
  (pivot). Verification metadata pinned until closeout stamps the 5d code commit.


  co-located Panda styling, with React Aria `ListBox` (LifecycleList) and `ToggleButtonGroup`
  (pivot). Verification metadata pinned until closeout stamps the 5d code commit.

  co-located Panda styling, with React Aria `ListBox` (LifecycleList) and `ToggleButtonGroup`
  (pivot). Verification metadata pinned until closeout stamps the 5d code commit.
  co-located Panda styling, with React Aria `ListBox` (LifecycleList) and `ToggleButtonGroup`
  (pivot). Verification metadata pinned until closeout stamps the 5d code commit.

## 260921-ICR-L2 The Review Panel Renders The Whole-Task Inventory

**Route meaning changed: the review panel can render a review that compared nothing, and its source pane
now opens with the complete change inventory.** `panels/review/ReviewSurface.tsx`: `ReviewTarget`'s two
selector fields became optional and the header prints `whole task (no subject selected)`; the Knowledge
pane prints the comparison identity when there is one and `no knowledge comparison was made` with the
server's own selection detail when there is not; and three render helpers were added — `Inventory` (all
three inventory states, never an empty list, with the count, the byte-form count, the server's own reason
and the reproducing command), `inventoryEntry` (the path exactly as published, with its status and its
renderability) and `byteNamedEntry` (a name this surface cannot carry as text, printed by its exact byte
form with the stated reason). `panels/detail-panel/changeSetBar.tsx` offers the entry for every live
leaf, and `panels/detail-panel/test-utils.tsx` answers the entry read with whatever answer a case wants
to exercise. `260921-ICR-L3` (recorded above) then changed what those three helpers do to a row: the
listing now opens into each entry's content, `Inventory` holds which row is open, and `byteNamedEntry`
states that its byte-form row cannot be opened — so the measurements below name this candidate's lines.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The target whose selectors are optional, and the header line that names the whole task when there is none.** | `ReviewTarget`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:60-74; dashboard/src/panels/review/ReviewSurface.tsx:40-47; dashboard/src/panels/review/ReviewSurface.tsx:856-928 |
| **The inventory rendering: all three states, the count, the byte-form rows and the reproducing command.** | `InventoryRows`; `inventoryEntry`; `byteNamedEntry` | dashboard/src/panels/review/SourceExplorer.tsx:58-116; dashboard/src/panels/review/SourceExplorer.tsx:118-130; dashboard/src/panels/review/SourceExplorer.tsx:170-222 |
| **The source pane that opens with the inventory, and the knowledge pane's selection line that survives an absent comparison identity — a pane that since `260921-ICR-L6` also delegates its statement area and since `260921-ICR-L3` opens each listed entry into its own content.** Ranges re-derived against this candidate. | `SourcePane`; `KnowledgePane` | dashboard/src/panels/review/ReviewSurface.tsx:299-354; dashboard/src/panels/review/ReviewSurface.tsx:272-297 |
| **The detail-panel entry that is offered for every live leaf, with the server's subject catalogue as a refinement.** | `useReviewCatalogue`; `DocChangeSetBar` | dashboard/src/data/useReviewCatalogue.ts:63-110; dashboard/src/panels/detail-panel/changeSetBar.tsx:506-555 |
| The fixture that answers the entry read with a subject, an empty list or a refusal. | `stubCounters` | dashboard/src/panels/detail-panel/test-utils.tsx:428-457 |
| The three cases those three answers are measured by. | `stubCounters` | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:11-12 |

## 260921-ICR-L16 The Review Surface Gets Its Outcome Owner, And The Entry Shows Its Own Answer

This leaf gives the Intent Reviewer's **non-payload states** one owner and makes the refusal reach the
reader on three surfaces.

**The outcome owner is new.** `panels/review/ReviewOutcome.tsx` (251 lines) owns the read's four phases
(`loading` | `reviewed` | `refused` | `failed`), the known-empty note, and **one** `ReviewProblemBlock`
that prints every field the owner published — code, reason, the offending input it named and the
next action it published, with an explicit sentence where the server published none. It renders a retry
**only** for `network`, the one token with no owner-published recovery route, and offers the task's source
change inventory only for a refusal that answers for the intent half alone. `ReviewSurface.tsx`'s inline
`RefusalBlock` and its generic `review-error` paragraph were **removed, not duplicated** (549 → 632 lines);
the surface is now the composition: it loads, keeps the last coherent payload, and renders the panes.

**The retained generation is keyed to the question it was read for.** `targetKeyOf` is the one identity a
read answers for — the task context **and** the question asked — and both the reset in `load` and the
render-time check read it, so a payload is never shown under a header it was not read for. A **failed**
read keeps the last coherent comparison on screen, labelled, and claims no empty review for it; a
**typed refusal** replaces the panes, because it is the owner's answer about the leaf's current state.

**The entry bar carries the entry read's own answer.** `changeSetBar.tsx` (186 → 280 lines) returns a
`ReviewSubjectRead` — `loading`, the first recorded subject, a known-empty flag, or the read's own
`ReviewFailure` — and `ReviewEntryState` prints it beside the entry in the owner's own words. The entry
itself is offered for every live leaf and still opens the task-context review on `review: {}`, so a
refusal here is a stated reason rather than a missing control.

**R03's expansion pane renders transported failures through the same block.** `SourceContent.tsx`
(222 → 241) keeps its own typed-refusal block untouched and routes everything else — an unwired process,
an unadmitted query, a socket that never answered — through the shared `ReviewProblemBlock`, so the 503
that used to read `503 unavailable` now carries the adapter's own instruction; the retry re-arms the read
through an `attempt` counter.

Two measured limits are recorded as **routed, not fixed**: an **in-flight** prop/question change can still
let an earlier read settle under a newer header (pre-existing at HEAD and on the round-1 bytes —
**R17**, with R24 for the interaction side; the retained-generation guarantee holds for every *settled*
change), and the **browser-class A01/A13 journeys** over a served dashboard are not verified by this leaf
(**R25**, with R24/R17).

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one place the non-payload states are decided, where the known-empty statement and the retained-generation label are mutually exclusive.** | `ReviewOutcomeRegion`; `knownEmpty`; `RetainedGenerationNote` | dashboard/src/panels/review/ReviewOutcome.tsx:86-94; dashboard/src/panels/review/ReviewOutcome.tsx:201-213; dashboard/src/panels/review/ReviewOutcome.tsx:226-260 |
| **The one failure renderer, with the retry gated on `network` and the inventory offer gated on an intent-only refusal.** | `ReviewProblemBlock`; `intentOnlyRefusal` | dashboard/src/panels/review/ReviewOutcome.tsx:115-177; dashboard/src/panels/review/ReviewOutcome.tsx:29-30 |
| The read key names the actual question, and retention is shown only for that same question. | `targetKeyOf`; `useSurface` | dashboard/src/panels/review/ReviewReadCycle.ts:73-91; dashboard/src/panels/review/ReviewSurface.tsx:778-854 |
| **The entry's own read state, printed beside a button that never disappears.** | `ReviewEntryState`; `useReviewCatalogue` | dashboard/src/panels/detail-panel/changeSetBar.tsx:316-350; dashboard/src/panels/detail-panel/changeSetBar.tsx:439-439; dashboard/src/panels/detail-panel/changeSetBar.tsx:371-424; dashboard/src/data/useReviewCatalogue.ts:63-110 |
| The source pane keeps shared transport failure rendering separate from the source owner typed refusal. | `SourceContent`; `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:167-227; dashboard/src/panels/review/SourceContent.tsx:112-124 |

## Update History
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **route body updated.** The section above records what this leaf changed on this route: a new outcome owner (`ReviewOutcome.tsx`), the surface's move from three outcome `useState`s to four phases with a retained generation keyed to the question it was read for (`ReviewSurface.tsx` 549 → 632), the entry bar's new `ReviewEntryState` carrying the entry read's own answer beside a button that never disappears (`changeSetBar.tsx` 186 → 280), and R03's expansion pane routing its transported failures through the shared block while its typed-refusal path stays untouched (`SourceContent.tsx` 222 → 241). It also records the two measured limits as **routed, not fixed**: the in-flight prop/question race (pre-existing; **R17** with R24) and the browser-class A01/A13 journeys (**R25** with R24/R17). **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation re-derivation in the L2 record above, forced by this leaf's changes to its cited files.** The paragraph and all three rows of the `260921-ICR-L2` section cite `panels/review/ReviewSurface.tsx` and nothing else that moved, so the whole section was re-derived against this candidate: `ReviewTarget`/`ReviewSurface` `27-37`/`395-462` → `30-39`/`482-549`, the three inventory helpers `238-264`/`207-223`/`224-237` → `291-335`/`214-260`/`270-282`, and `SourcePane`/`KnowledgePane` `265-307`/`179-206` → `337-393`/`182-205`. This leaf (`260921-ICR-L3`, whose own section is recorded in this route's narrative) made the inventory rows openable, added `SourceContent.tsx`, and grew `ReviewSurface.tsx` 462 → 549 lines, so the added sentence says which leaf changed what those helpers do to a row. No claim of the L2 record was falsified: the inventory is still rendered in all three states, the byte-form rows are still listed beside the named ones, and the target's selectors are still optional. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, code base `702714fc`): **route body updated.** The review panel renders the whole-task source inventory in all three of its states (including the byte-form rows for names it cannot carry as text), states that no comparison was made when the payload carries none, and survives a target with no selector; the detail-panel entry is offered for every live leaf. The section is appended at the end of this route's narrative, and the ten rows of this document that cited `ReviewSurface.tsx` by line were re-derived against the candidate in the same pass — this leaf moved every helper below the Knowledge pane. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.

## 260921-ICR-L10 The Page Control, And The Captured Body That Proves The Refusal Actually Reaches It

`260921-ICR-L10` (`ICR-R10@v1`) adds the reachable next page to this route's review surface. The surface
used to render a remainder with no control that reached the rest of the collection — the packet's own
non-conforming example — and it now renders the bounds, the scope and one action that advances the walk
with the cursor **the server published**, plus a first-page action when a cursor was refused.

The control is four small pieces over the page the client already carries (`PageControls`, `PagePicker`,
`PageActions`, `PageBoundsLine`) and a refusal block (`PageRefusalBlock`) that states the code, the
owner's two identities and a live first page of the collection that was asked for. The page is part of
the read's target key, so a page change is its own read rather than a re-render over the wrong payload.
No next action is offered for a body that published no cursor, whatever remainder it reported — a button
that fetches nothing is the defect this control exists to prevent.

**Two files on this route are new, and both are about proof rather than behavior.**
`ReviewSurface.paging.test.tsx` drives the real component over the real client with only `fetch` stubbed,
and `recordsPageRefusal.captured.ts` is the raw body of a real refused records page, exported verbatim
with a provenance header. The capture exists because the route omits the `page` key rather than sending
`null`: the mounted case asserts that absence before rendering the bytes, so the case cannot pass against
a body the route would never send.

Keyboard and focus traversal of the control, and the finished cockpit interaction, remain `ICR-R24@v1`'s;
the assembled acceptance remains `ICR-R25@v1`'s. This leaf records the boundary rather than claiming
either.

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-23T00:20:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **route body updated.** **the page control, and the captured server body that proves the refusal reaches it.** `ReviewSurface.tsx` gained the page control (`PageControls`, `PagePicker`, `PageActions`, `PageBoundsLine`), the refusal block, and the page as part of the read's target key; the route gained two files, `ReviewSurface.paging.test.tsx` (seven mounted cases over the real component and the real client, only `fetch` stubbed) and `recordsPageRefusal.captured.ts` (a real refused records page, exported with its provenance). The capture is the point: the mounted case asserts the `page` key is absent before rendering the bytes. Browser and keyboard traversal remain `ICR-R24@v1`'s. No verification stamp was advanced: nothing in this leaf is committed, so the merge/commit stamp is closeout's.
## 260921-ICR-L26 The Review Surface Mounts The Attribution On Both Panes

`260921-ICR-L26` (`ICR-R26@v1`) mounts the server's attribution facts on both review panes through three
renderers and no new component state: `ReviewSurface.tsx` (879 → 946 lines) gained `applicabilityNote`
(one record's treatment, the true subject its binding names, and the server's own detail — printed
**nothing** when the payload carries no label), `contextList` (the labelled context rows with the
relationship that reached each one, the record's kind and its references) and `applicabilityCounts` (the
six-way partition beside the collections it filtered). All three read the fields the server sent and
none derives a treatment, a relationship or a total.

**One record, one treatment, two panes.** `applicabilityNote` is called on the knowledge pane's
assessments, authored effects and signals **and** on the evidence pane's evidence links and
observations, and the context list and the counts block are mounted on both panes, so the same record
cannot read one way in one pane and another way in the other. A context row never renders the sibling's
finding: the row carries the record's kind, and that is the whole point of the value.

**The route gained one case module.** `ReviewSurface.applicability.test.tsx` (311 L, four mounted cases
over the real component and the real client with only `fetch` stubbed) asserts the treatment and the
true subject of a labelled context row, the absence of the sibling's finding from the document, the
six-way counts rendered as arithmetic, the historical label with the tree it examined, and that a
payload published **before** the vocabulary still renders. Browser and keyboard traversal remain
`ICR-R24@v1`'s, and the assembled A14/A15 acceptance remains `ICR-R25@v1`'s.

## Update History
- 2026-09-23T02:45:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **route body updated for the mounted attribution labels (`ICR-R26@v1`).** The section above records the three renderers and their mount points on both panes, the rule that a label is displayed rather than computed, the new mounted case module and its four properties, and the two boundaries left to R24 and R25. **Citation accounting:** every row on this overview that cited `ReviewSurface.tsx` by line was re-derived against this candidate, because this leaf's insertions moved the renderers below them (`assessmentBlock` `174-186`, `authoredEffect`/`signalBlock` `188-201`/`203-221`, `KnowledgePane` `278-303`, `EvidencePane` `493-546`, `SourcePane` `435-491`). **Stamp accounting:** no verification stamp was advanced — the header already names the leaf's base, and nothing in this leaf is committed, so the governed closeout owns the real stamp.
## 260921-ICR-L12 A Closed Leaf Keeps Its Intent Review, Bound To Its Record

`260921-ICR-L12` (`ICR-R12@v1`) changes what liveness means to the change-set bar and what the
review surface says about the record it is reading:

- **the Intent review entry is offered for every leaf.** It used to be gated on the enclosure being
  live, which is the intake defect's browser face — a cleaned leaf's worktree is gone and the review the
  packet exists to make openable could not be reached. `live` now selects **which record** the entry is
  addressed to (the live candidate, or the leaf's recorded comparison as `historical: true`, labelled
  "Intent review (recorded)") and it is not a gate. The **working** change-set stays live-gated, because
  "what is not committed yet" genuinely does not exist once the enclosure is closed, and the catalogue
  read is no longer live-gated either — it remains a refinement and never a gate, so a refusal beside
  the entry is a stated reason rather than a missing control.
- **the mounted surface states which record the panes are read from.** `history` joined the review
  target and the **target key** (`repo/master/leaf/<history ?? "live">/<question>/<position>`), so a
  response read for one record is never applied to a surface that asked for another; `ReviewHeader`
  mounts the provenance line and the root publishes `data-review-history`. The two extractions
  (`ReviewHeader`, `ReviewPanes`) cleared the surface's `max-lines-per-function` rail with no ignore
  added and no limit widened.
- **the new client case module** `ReviewSurface.history.test.tsx` pins both directions of the pair over
  the real component and the real client, stubbing only `fetch`: the recorded read asks for the record
  it was handed and says so, and the live read asks for none and claims none.

**Boundaries recorded, not closed.** `ICR-R24@v1` owns the leaf-history drill-down navigation — this
leaf provides the addressable target and adds no navigation — and `ICR-R25@v1` owns the assembled
browser acceptance; these cases are mounted components over the real client, not a real-browser run.

## Update History
- 2026-09-23T04:31:21+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **route body updated for the closed leaf's review entry (ICR-R12@v1).** The section above records
that liveness now selects which record the entry is addressed to instead of whether it exists, that the
working change-set stays live-gated, that the mounted surface states its record and keys on it, and that
the two extractions cleared the lint rail without widening it. **Citation accounting:** every row on
this overview that cited `changeSetBar.tsx`, `ReviewSurface.tsx`, `ChangeSetViewer.tsx` and
`Cockpit.tsx` by line was re-derived against this candidate, because this leaf moved them. **Stamp
accounting:** no verification stamp was advanced — the header already names this leaf's base as the
production line the reading was taken against, and nothing in this leaf is committed, so the governed
closeout owns the real stamp.

## 260921-ICR-L17 The Read Cycle And The Refresh Control Leave The Review Surface

`260921-ICR-L17` (`ICR-R17@v1`) adds **two components to the `panels/review/` child route** and rewrites
one read at the detail-panel entry. No route, takeover dispatch or target shape changed.

- [`panels/review/ReviewReadCycle.ts`](../panels/review/ReviewReadCycle.ts.md) owns the review surface's
  read cycle: the question's identity (`targetKeyOf`), one in-flight read per question with the newest
  read winning, the retained generation, and the reader's refresh as the single read that may carry the
  identity on screen. It exists because `ReviewSurface.tsx` is over the file-size rail and the component
  was over the per-function rail.
- [`panels/review/ReviewRefresh.tsx`](../panels/review/ReviewRefresh.tsx.md) owns the explicit refresh
  control and the one sentence that answers it. Its derivation renders **no claim** unless the read that
  carried the identity has answered, and the `superseded` sentence names both digests and says which one
  the panes below hold.
- `panels/review/ReviewSurface.tsx` is **462 lines of read logic and rendering lighter** and now wires
  the hook, the header's `refresh` node and the three regions.
- `panels/detail-panel/changeSetBar.tsx` gains the store-projection invalidation signal
  (`reviewDependencyFacts`), an always-offered refresh control (`ReviewCatalogueRefresh`) whose mark is
  derived from the facts recorded with the last answer, and the pure `catalogueAnswer` mapping.
- `data/review.ts` gains the ninth `intentReview` argument, the `reviewQuery` assembler and the single
  `PREVIOUS_BINDING_QUERY` spelling of the wire name.

**What a route reader should carry away.** The carried identity is `{readNumber, key, digest}` and it is
both **sent** and **described** only when the read number and the question key agree, so the identity a
notice describes is exactly the identity the request carried — a different subject, a different leaf, a
recorded read, and a later read of the same question all carry nothing.

## 260921-ICR-L24 The Family Reading Path And The Source Explorer

**Route meaning changed: the review child route gained the accepted family-centred composition, and the
surface became a composition of owners rather than the owner of everything.** Five modules are new in
`panels/review/`, and each one owns exactly what its neighbours must not:

- [`FamilyTree.tsx`](review/FamilyTree.tsx.md) — a recorded family is the semantic parent of the review
  population: the family label, then the family revision's own independently authored joint guarantee
  printed whole, then the complete member statements of the roster the page carried **including the
  unchanged siblings**. It is one roving-focus group with arrow-key traversal and `aria-current` on the
  current node, and it carries the route's **one** family-roster walk control (`RosterNext`), which
  continues the walk at the cursor the family's own roster page published.
- [`FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md) — the unified central reading path: for a
  **member** selection the family guarantee and the selected intent first, then the linked expressions, then
  the recorded execution evidence and the authored assessment; for a **family** selection the guarantee,
  then the complete recorded member context, then the family's deduplicated changed expression excerpts
  (**added by 260921-ICR-L36**, below) — in one column, so a reviewer never has to reconstruct the route by
  switching tabs or opening a detached inspector. This bullet read as one route for the whole column until
  L36; the two selection shapes are two different orders and both are complete.
- [`ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md) — which family or member is selected, the
  reader's display preferences (diff layout, full-file disclosure, the expanded path) and the
  narrow-screen route from the tree to the selected review. `useWorkspaceState()` is called once, by the
  surface **above** `ReviewPanes`, because that switch returns `null` while a page read is in flight: a
  page request can no longer reset the reader's selection or display choices.
- [`SourceExplorer.tsx`](review/SourceExplorer.tsx.md) — the complete source change explorer, moved out
  of `ReviewSurface.tsx` whole: every changed path of the comparison's bound pair, openable at the
  generation the listing named, with the inventory's three states, the byte-form rows and the reproducing
  command. The family navigation is an attribution lens over it and never an exclusion filter.
- [`ReviewWorkspace.family.test.tsx`](review/ReviewWorkspace.family.test.tsx.md) — the case module that
  drives the real surface over the real client with only `fetch` stubbed, against the seven
  `familyReview.*.captured.json` bodies the server published.

**`ReviewSurface.tsx` no longer owns the inventory.** It mounts the workspace and keeps the three
diagnostic panes — knowledge, source, evidence and assessment — inside one `<details>` disclosure, so
their content, controls, refusals and technical identities are unchanged and still in the DOM and the
keyboard's reach, reached deliberately instead of being the first thing a reviewer reads past. Its
`ReviewPanes` switch takes the workspace as a prop for the reason above, and the surface calls
`useWorkspaceState()` itself. `ReviewReadCycle.ts`'s `ReviewPageRequest.of` is typed as the server's own
`ReviewPagedCollection` rather than a narrowed copy, because a request naming `family_members` must be
representable for a truncated family roster to be continued.

| Finding | Anchor | Source |
| --- | --- | --- |
| The family hierarchy shows authored guarantees and member statements with full sibling context and keyboard traversal. | `FamilyNode`; `MemberRoster`; `treeArrow` | dashboard/src/panels/review/FamilyTree.tsx:434-464; dashboard/src/panels/review/FamilyTree.tsx:466-516; dashboard/src/panels/review/FamilyTree.tsx:550-562 |
| **The one family-roster walk control, continuing at the cursor the roster page published.** | `RosterNext` | dashboard/src/panels/review/FamilyTree.tsx:250-282 |
| **The unified central reading path, in one column and in the packet's order.** | `FamilyReviewCenter` | dashboard/src/panels/review/FamilyReviewCenter.tsx:819-898 |
| **The workspace's selection, preferences and narrow-screen route, and the one hook owned above the pane switch.** | `useWorkspaceState`; `ReviewWorkspace` | dashboard/src/panels/review/ReviewWorkspace.tsx:159-196; dashboard/src/panels/review/ReviewWorkspace.tsx:208-287 |
| **The complete source change explorer, and why it is its own module rather than part of the surface.** | `SourceExplorer` | dashboard/src/panels/review/SourceExplorer.tsx:224-302 |
| **The mounted family composition cases and the captured server bodies they are driven with.** | "familyReview.*.captured.json" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:8-9 |
| The surface mounts the workspace and retains technical records/paging panes in a disclosure; state is held above the read cycle. | `ReviewPanes`; `useSurface` | dashboard/src/panels/review/ReviewSurface.tsx:658-720; dashboard/src/panels/review/ReviewSurface.tsx:778-854 |
| **The page request whose `of` is the server's own collection union.** | `ReviewPageRequest` | dashboard/src/panels/review/ReviewReadCycle.ts:64-68 |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **route body updated for the accepted family-centred composition of the review child route.** The section above records what this leaf changed in the sources this route governs: the five new `panels/review/` modules (the family tree with the one roster walk control, the unified central reading path, the workspace whose state is owned above the pane switch, the source explorer moved out of `ReviewSurface.tsx` whole, and the mounted family case module over the seven captured bodies), the surface's move to mounting the workspace with the three diagnostic panes behind one `<details>` disclosure, and `ReviewPageRequest.of` following the server's own collection union. The new `## File Onboarding Map` links the five cards and the seven captures. **Citation accounting:** every row on this overview whose anchor no longer sat in its cited range was re-derived from that anchor's own declaration on the frozen candidate, including the three cited ranges that had run past the end of `ReviewSurface.tsx`; no claim wording changed and no row was dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **this route's surface changed, and two reference rows here were re-anchored.** `ReviewSurface.tsx` mounts the boundary's own sentence when `staleness.state === "not-measured"` (`:557-565`), and `ReviewSurface.outcomes.test.tsx` carries the case that pins it. The repaired rows are `ReviewEntry` (`613-618`, in the data client this route reads through) and `shownPayload` (`949`, the read that stores the payload with its target key). **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the `panels/review/` child route gained two modules and the surface lost its read cycle (`ICR-R17@v1`).** `ReviewReadCycle.ts` owns the question key, the one read path and the newest-read-wins guard; `ReviewRefresh.tsx` owns the refresh control and the generation notice; `ReviewSurface.tsx` delegates both; `changeSetBar.tsx` gains the projection-driven invalidation and its own refresh control; `data/review.ts` gains the ninth argument and the one query-parameter spelling. **No route-level fact changed**: no new or removed route, no change to the reviewer takeover dispatch, the target shape or the cookie. **Citation accounting:** the rows this document carries into the changed dashboard modules were re-derived from each construct's own declaration (`DocChangeSetBar` `:483`, `useReviewCatalogue` `:235`, `ReviewEntryState` `:289`, `Inventory` `:389`, `ReviewEntry` `data/review.ts:607`, `intentReviewEntries` `:636`, `reviewSourceContent` `:654`, `targetKeyOf` `ReviewReadCycle.ts:65`). **Stamp accounting:** the verification pair names this leaf's base; closeout owns the stamp.

## 260921-ICR-L36 The Family Column's Third Part: The Deduplicated Changed Expression Excerpts

**Route meaning changed on the review child route: a whole-family selection now presents the family's own
changed expression excerpts, deduplicated, between its member context and the shared source explorer.** The
accepted design's whole-family line asks for three things — the full guarantee, all members including the
unchanged sibling, and deduplicated changed expression excerpts — and the centre composed only the first
two, so a reader who selected a whole family saw no expressions at all. Three sources changed and no Python
did: the payload already carried every fact, so the whole change is client-side.
`review/FamilyReviewCenter.tsx` gains the collection and the helpers it needed;
`review/ReviewWorkspace.family.test.tsx` gains the mounted case over the real captured body; and
`review/familyExpressions.test.ts` is a **new unit lane** that holds the arithmetic with no DOM, because the
captures do not carry every shape the arithmetic must get right.

**The four decisions in the collection, stated here because each one is a fact a reader would otherwise have
to re-derive from the source.**

- **"Changed" is the read's own realization resolution, and it is not the comparison's measured change set.**
  A claim is a row when the read did **not** find the recorded bytes at the recorded address
  (`recorded_blob_mismatch`, `path_absent`, `unsupported_locator`, `entry_not_blob`); `exact_recorded_blob`
  is the resolved state and is not a change; `recorded_object_unavailable` and `not_requested` are **not
  measured** and are counted apart rather than called changes. On the family this surface serves, the two
  notions disagree in the direction that matters — both stale addresses resolve as `recorded_blob_mismatch`
  while neither is a changed path of the comparison's own change set — so the verdict sentence and every row
  say which of the two is being read.
- **The dedup key is the address together with the *recorded* source identity. The observed identity is
  deliberately NOT in it, and that is the F1 repair.** The accepted prototype's key is the excerpt's address
  (`path + ':' + start`), but the claims this surface receives carry no line range of their own — the range
  lives inside the read's own `detail` sentence — so the identity used is the path together with the
  **recorded** bytes, which is the only thing that keeps two different recorded blobs at one path apart
  (the verifier's over-collapse probe found none). The observed identity is what the read **found** at the
  address in one side's tree, so a divergent address has **one observed value per side**; folding it into
  the key split that address into two keys — one per side — so the pass that pairs the sides could never
  find the other one and the row printed a single side. It is now carried **per side** in
  `readingsBySide`, beside that side's resolutions, where a read result belongs.
- **The collection is built from the family's carried membership rows, not from the centre's first-wins
  `distinct` list.** A resolution is a fact about the address **in one side's tree**, so a collection built
  from one row per revision would hide a change: the captured `familyReview.walkFinal` body records member
  revision `d24e5187…` with `src/batch.py` under one recorded blob, resolved `exact_recorded_blob` on the
  before snapshot and `recorded_blob_mismatch` on the after one, and a `distinct`-built collection would
  have presented that address as resolved. **The second pass that joins the two sides is `recordSideReadings`
  (renamed from `recordSideResolutions` by the F1 repair), and it now carries a read result per side rather
  than a resolution per side:** each excerpt's `readingsBySide` holds that side's **resolutions** *and* the
  **observed identities** its read found, both read results and neither an identity. The verdict sentence's
  own clause was replaced outright, and **the F-V1-3 reword then replaced it again; the page now reads**
  *"every row below prints what each side's read made of its address — the resolution that side's claim
  carried — so an address both sides carried prints both readings whenever they differ, and an address only
  one side carried prints that side's alone."* **The superseded wording must not be quoted** (F-V1-3, low): it
  read *"…each side whose read resolved its address's recorded bytes…"*, and *"resolved"* **collides with the
  product's own name for `exact_recorded_blob`** — true under the reading the code implements, false under the
  literal one on every live row, where the changed sides are `recorded_blob_mismatch`. The reword names the
  reading explicitly, and the fix verifier asserted the row-by-row behaviour on the rendered page.
  The dedup arithmetic is unchanged
  by the repair and was re-measured: 8 membership rows, 8 changed row instances, 2 distinct keys with group
  sizes `[4,4]`, `8 − 2 = 6`.
- **One row per distinct excerpt, naming every membership row that recorded it, with the revision identity
  beside the label.** A display label alone is not a key: `ICR30-I-1` is recorded as **two** member
  revisions of its family, so a label-only row would name two different rows identically. On the live case
  the served family records 4 changed expression rows over 2 distinct addresses (8 rows counting both
  sides), and the mounted product renders **2** rows — `renderedDistinct: 2` against `renderedRowSum: 8`.

**The composition, and what it did not disturb.** The family column now runs guarantee → complete recorded
member context → the excerpt collection → the shared source explorer, which is the accepted design's
"lead with its own guarantee comparison and complete member context, then relevant expressions"; the
member-context card was **extracted** from `FamilyCenter` unchanged (`FamilyMemberContext`) so the column
reads as the three things it composes. **A3's member order is untouched** — the member selection's
`data-testid` blocks in document order are the same list before and after — and the three lines this leaf
re-measured on the new build (A5's unchanged-member expressions, A3's order, B4's full-file disclosure)
are present and unchanged. Two sentences the member-level attribution used to spell inline are now **one
owner each** (`unlistedPathNote`, `listedOrPlainPath`) because the collection needs the same two facts about
the same path, and two copies could drift into disagreeing about one path.

**The honest bound on the divergent rendering, and it travels with the claim.** The divergent case is
evidenced against the **captured `familyReview.walkFinal` body through a labelled fixture** — measured on the
fix round's build as `before exact_recorded_blob · after recorded_blob_mismatch`, with `data-sides =
"before,after"`. The divergence is exercised against the captured `familyReview.walkFinal` body through a **labelled
fixture**, and that label is the whole of its evidence. Live data was searched: **the search reached 3
families served by 1 leaf** (`260921-ICR-L34`, which returns `entries` with 3 families), and the other
**35 leaves refused `candidate_dataset_absent`** — each records no comparison generation, so no knowledge
operand exists for a subject to be listed from — and therefore **carry nothing to search. Absent is not
measured:** those 35 were not searched and found clean; they were unreachable, and a family that cannot
be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is one of those 35**, so this leaf's
own live data carries no divergent family either. Read from `f1/raw/live-truth.json` and reproduced
independently by the verifier in `f1v/raw/vf1-live-scan.json` (`leavesAttempted: 36`, `leavesResolved:
1`, `leavesRefused: 35`, `refusalCodes: ["candidate_dataset_absent"]`, `familiesServed: 3`,
`familiesWithDivergence: 0`, `totalDivergent: 0`). The
live family renders the same 2 excerpts as before, and nothing on this route may be read as a claim that live
data exercises the divergent path.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The family column's three parts and the collection mounted as the third, after the member context and before the shared explorer.** | `FamilyCenter`; `FamilyMemberContext`; `FamilyExpressionExcerpts`; `carriedMembership` | dashboard/src/panels/review/FamilyReviewCenter.tsx:455-500; dashboard/src/panels/review/FamilyReviewCenter.tsx:533-594; dashboard/src/panels/review/FamilyReviewCenter.tsx:596-658; dashboard/src/panels/review/familyExpressions.ts:21-26 |
| Family excerpt arithmetic groups recorded addresses and distinguishes changed, resolved and unmeasured realization readings. | `familyExpressionExcerpts`; `excerptKey`; `claimClass` | dashboard/src/panels/review/familyExpressions.ts:185-202; dashboard/src/panels/review/familyExpressions.ts:64-66; dashboard/src/panels/review/familyExpressions.ts:68-73 |
| Per-side resolution and observed identities attach to the same recorded-address key. | `recordSideReadings`; `FamilyExcerptSideReading` | dashboard/src/panels/review/familyExpressions.ts:147-168; dashboard/src/panels/review/familyExpressions.ts:34-38 |
| **The two hoisted owners the member attribution and the family collection share, so the two readers cannot drift.** | "function unlistedPathNote"; "function listedOrPlainPath" | dashboard/src/panels/review/FamilyReviewCenter.tsx:247-251; dashboard/src/panels/review/FamilyReviewCenter.tsx:440-451 |
| **The mounted case: the rendered count is the body's distinct excerpt set, every row's collapse count is the body's own group size, and EVERY rendered row's `data-sides` is checked against the sides the body resolves that excerpt on — the page's own both-sides sentence verified row by row against the body, not read from the page.** | "renders the family's changed expression excerpts, deduplicated, over the captured family"; `dataset.sides` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:700-768 |
| **The new unit lane for the same arithmetic, its own statement of which inputs are constructed, and the pair of cases that state the whole key contract between them (recorded keeps two blobs at one path apart; observed may not, because two sides of one address legitimately see different bytes).** | "WHY THIS FILE ASSEMBLES ITS OWN PAYLOAD"; "keeps two excerpts apart when one address carries two different recorded blobs"; "treats two different observed blobs at one address as one excerpt, read once per side" | dashboard/src/panels/review/familyExpressions.test.ts:1-16; dashboard/src/panels/review/familyExpressions.test.ts:86-121; dashboard/src/panels/review/familyExpressions.test.ts:202-247 |

## Update History
- 2026-09-26T04:00:00+02:00 — 260921-ICR-L36 curator, **the F-V1-3 reword has LANDED, and this document now carries the sentence the page actually prints.** The clause this pass quoted at 03:00 and 03:50 has been replaced in the source: the verdict's notion sentence now reads *"every row below prints what each side's read made of its address — the resolution that side's claim carried — so an address both sides carried prints both readings whenever they differ, and an address only one side carried prints that side's alone."* **The superseded wording — *"…names the resolution of each side whose read resolved its address's recorded bytes…"* — must not be quoted**: *"resolved"* collides with the product's own name for `exact_recorded_blob`, which made the clause true under the reading the code implements and false under the literal one on every live row. The reword removes the collision by naming the reading explicitly, and the fix verifier asserted the row-by-row behaviour on the rendered page. **The body was updated; the two history entries above that quote the superseded sentence are left standing as the record of what this pass wrote before the reword.** **Citation accounting:** the row into `FamilyReviewCenter.tsx` for the second pass now also cites `:682-697`, the interface that declares `readingsBySide` (the checker resolves that anchor to its declaration at `:689`, which the row's previous single range `:804-827` did not contain), and the verdict row's anchor was replaced with two strings that occur inside `:864-909` (`"no claim was left unmeasured"` and `"changed expression row(s) across the family's"`) because the old anchor's sentence no longer exists in that form anywhere in the tree. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:50:00+02:00 — 260921-ICR-L36 curator, **final wording pass (the last correction), and two round-1 sentences this seat repeats are corrected or bounded here.** (1) **The replacement clause is not to be quoted as self-evidently true** (F-V1-3, low; a reword is in flight). The page's notion sentence reads *"every row below prints what each side's read made of its address — the resolution
that side's claim carried — so an address both sides carried prints both readings whenever they differ, and
an address only one side carried prints that side's alone."* The phrase *"resolved its address's recorded bytes"* **collides with the product's own name for `exact_recorded_blob`**: the clause holds under the reading the code implements — a side's read result is printed for the side that produced it, which the fix verifier asserted **row by row on the rendered page** — and fails under the literal reading, where every changed side is `recorded_blob_mismatch` and has not "resolved" its recorded bytes. The body now quotes it **with the reading named**, and says so. (2) **"No claim in the leaf rests on a fixture" is falsified, and this card does not say it** (F-V1-4, low — the one round-1 sentence the corrected pass did not cover). The **divergent-rendering** claim rests on the captured `familyReview.walkFinal` body through a **labelled fixture**, because live data carries no divergent family: the search reached **3 families served by 1 leaf**, with **35 leaves refusing `candidate_dataset_absent`** and therefore **absent, not measured**, `260921-ICR-L36` among them. Every `CONSTRUCTED` label in the unit lane is about that module's own inputs and is **not** a claim about the leaf's evidence. (3) **Routed, not absorbed:** **F-V1-6** and **F-V1-7** are the verifier's remaining low findings and belong to the worker/verifier seats; the subject-catalogue route's deliberate `candidate_dataset_absent`, the shell-level scroll decision with its 13 chrome elements, and **D63**, **D64**, **D68**, **D70** remain routed exactly as before. (4) **One report-side caveat that is NOT a card fact and is deliberately not propagated as settled:** the report's `dashboard/src` digest `08de88e7…` does not reproduce under a stated method (the verifier measured `fb387272…`), and three B4 content heights differ between the two seats by 20–70 px. No card here quotes a digest or a height, and none should: those numbers were measured by one seat and may differ by seat. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:35:00+02:00 — 260921-ICR-L36 curator, **the authoritative statement of the divergent bound; it supersedes every earlier phrasing of it in this document, and the entry below is corrected in place for its refusal reason only (same seat, same uncommitted pass, minutes old, and a wrong reason code must not stand).** The orchestrator passed this seat a summary of the zero-divergence measurement whose scope was too wide — "scanned every family of all 36 leaves" — and the artifact does not support that scope. Measured from `temp/icr/f1/raw/live-truth.json` and reproduced independently by the verifier in `temp/icr/f1v/raw/vf1-live-scan.json`: **36 leaves attempted; 1 resolved (`260921-ICR-L34`, state `entries`, 3 families); 35 refused with code `candidate_dataset_absent`** (each records no comparison generation, so no knowledge operand exists for a subject to be listed from); **3 families served; 0 divergent addresses**. The rule this document now carries is the point of the correction: **absent is not measured.** The 35 were not searched and found clean — they were unreachable, and a family that cannot be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is itself one of those 35**, so this leaf's own live data carries no divergent family either. The bounded conclusion that stands: the divergence is exercised against the captured `familyReview.walkFinal` body through a **labelled fixture** — now verified: the divergent address renders `before exact_recorded_blob · after recorded_blob_mismatch` with `data-sides = "before,after"`, and reverting `excerptKey` fails the shipped suite at `ReviewWorkspace.family.test.tsx:777` — and live data reached 3 families of 1 leaf with none divergent. **Also settled by that verification:** the false sentence is gone from the shipped bundle, the rendered page and the report, and the replacement sentence the cards quote was checked for truth about every row the page renders and none was found untrue. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:20:00+02:00 — 260921-ICR-L36 curator, **same-pass correction of the entry below, which is left standing as the record of what this pass first wrote.** The entry below says the divergence scan "scanned every family of all 36 leaves and measured zero divergent addresses". **That is an over-claim about the population, and the artifact does not support it.** Read from the fix round's own `temp/icr/f1/raw/live-truth.json` and reproduced independently by the verifier in `temp/icr/f1v/raw/vf1-live-scan.json`, the measurement is: **36 leaves attempted, 35 refused `candidate_dataset_absent`** (each records no comparison generation, so no knowledge operand exists for a subject to be listed from — **absent is not measured**), **1 resolved** (`260921-ICR-L34`, which returns `entries` with **3 families**), and of those 3 families examined **0 carry a divergent address** (`familiesExamined: 3`, `familiesWithDivergence: 0`, `totalDivergent: 0`). **The zero is measured over 3 families, not over all 36 leaves** — 35 of them never answered — and the body of this document now says so, naming the examined population and citing both artifacts. The measured conclusion is unchanged and the bound it exists for is unchanged: no live family in the population the scan could reach records a divergence, so the divergent rendering is evidenced against the captured `familyReview.walkFinal` body through a fixture-backed API and is labelled as such. Only the population was overstated; no stamp was advanced; no commit was made.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **post-fix pass: the F1 repair round landed on this route, and the L36 section above is re-read against the fixed sources.** The section's dedup-key bullet now states the key the module actually uses — the address together with the **recorded** identity, with the observed identity **deliberately absent** and carried **per side** in `readingsBySide` — and the reason it matters: a divergent address has one observed value per side, so folding it into the key split that address into two keys, one per side, and the row printed a single side. The second pass is named as the repair renamed it, `recordSideReadings` (`recordSideResolutions` before), and it carries each side's resolutions **and** observed identities. **The false clause is gone from the page and replaced by the sentence a reader may quote:** *"every row below prints what each side's read made of its address — the resolution
that side's claim carried — so an address both sides carried prints both readings whenever they differ, and
an address only one side carried prints that side's alone."* The dedup arithmetic is unchanged and was re-measured: 8 membership rows, 8 changed row instances, 2 distinct keys with group sizes `[4,4]`, `8 − 2 = 6`, and the over-collapse probe still finds none. **The honest bound is recorded on this route and must travel with the claim:** the divergent path is evidenced against the **captured `familyReview.walkFinal` body through a fixture-backed API**, labelled as such, because **divergence exists nowhere in live data** — the fix round scanned every family of all **36** leaves and measured **zero** divergent addresses — so the live family renders the same 2 excerpts as before. **Citation accounting:** every row this route carries into `FamilyReviewCenter.tsx` was re-derived at the new tip (`:571-621` → `:571-632`, `:623-627` → `:634-638`, `:643-652` → `:654-663`, `:693-695` → `:712-717`, `:819-836` → `:845-862`, `:954-969` → `:984-999`, `:971-1013` → `:1001-1043`, `:1048-1111` → `:1078-1141`, `:1113-1163` → `:1143-1193`, and the L24 section's root row `:1306-1389` → `:1336-1419`), and the two rows into the case modules were re-derived with them (`:735-790` → `:735-803`; the unit lane's rows re-pointed at its new case ranges). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (leaf `260921-ICR-L36`, memory worktree only; no Python changed and no code committed — the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`, memory base `52c025e6f2c38d3207274d55e00a8889c0459bad`; worker report `temp/icr/report-l36.md`): **route body updated — the review child route's family selection gained its third part, so this route's account of the family column changed rather than its citation ranges alone.** The new section records the four decisions a reader must not have to re-derive from the source (the realization resolution against the comparison's own measured change set; the address-together-with-both-identities dedup key rather than the prototype's path-only key; why the collection reads the carried membership rows and not the centre's first-wins `distinct` list, with the captured `walkFinal` member revision `d24e5187…` that a `distinct`-built collection would have shown as resolved; and why one row names every membership row with the revision identity beside its label), the composition order and the fact that A3's member order is untouched, and the two sentences the attribution now shares with the collection through one owner each. **This section is the body update the memory-refresh attestation required**, not a history-only or metadata-only change. **Citation accounting:** the L24 section's row into `FamilyReviewCenter.tsx` was re-derived from the construct's own declaration at this tip (`:800-875` → `:1306-1389`), and the rows this leaf's insertion displaced in the three cards that reach into the same file were re-derived in the same pass. **Sweep result:** the sentence this route carried — that the centre renders "the family guarantee and the selected intent first, then the linked expressions" — was true of the **member** selection and read as a claim about the whole column; the L36 section states the family order explicitly so the two routes cannot be read as one. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.

## Bounded family context across review pages

The existing ReviewReadCycle retains exact member content and source claims only within an admitted same-comparison, same-subject family-side-revision continuation. Rejected continuations state failure beside the retained coherent display; refresh and subject/history changes remain replacement reads. FamilyTree, FamilyReviewCenter and ReviewExpressions distinguish loaded context from raw item counts and partial/unavailable source scope. Source inventory, primary statement and evidence remain their existing owners' facts. The captured-page regression fixture and mounted read-cycle cases document this boundary.
