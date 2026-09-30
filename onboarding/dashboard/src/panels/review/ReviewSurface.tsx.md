# dashboard/src/panels/review/ReviewSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash |  `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate |  2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Compose the normal Intent Reviewer from one subject catalogue, one comparison read cycle and a family-centered workspace. The surface is read-only and produces no semantic judgment. Since `260921-ICR-L48` (`ICR-R24@v3`) it also decides **which payload the workspace is mounted over**: the answer for the subject on screen, or — while that subject is pending, failed or refused — the task context's last admitted `frame`, so a selection never unmounts the workspace, its navigation or its open disclosures.

## Code Commentary

### Logic

The subject-selection callback carries the chosen family context into the new subject read. Selecting a member requests its invariant through the existing read cycle; it does not render a family payload as that member own assessment.

useSurface gets recorded subjects through useReviewNavigation and passes the chosen identity to useReviewReadCycle. Changing subjects (`selectSubject`) records the element that had focus (`focusSelection = { from }`), clears the prior page request and local family selection while the workspace display preferences persist. The retained payload is shown only when its full target key matches the question on screen. ReviewPanes mounts one workspace; records, pagination, submission contract and complete technical panes remain inspectable in the technical-details disclosure, whose renderers moved to `ReviewRecordPanes.tsx` (`ReviewTechnicalDetails`) in L48. Typed outcomes stay with ReviewOutcome, refresh identity with ReviewRefresh, source bytes with SourceContent, and family/intent/source composition with ReviewWorkspace.

**The mounted shell (L48).** `useSurface` owns one `ReviewReadCache` per mounted surface (`useState(() => new ReviewReadCache())`), passes it to the read cycle and provides it to source content through `ReviewReadCacheContext`. It computes `reading` with `readingStatusOf` only when a `frame` exists and no payload answers the question on screen: the status is keyed to the read cycle's target key, names the requested subject (`kind:id`, labelled from the catalogue entry when there is one) and, for a failed or refused read, carries the owner's `ReviewProblemBlock` labelled with that subject (retry for a transport failure, the source-changes offer for an intent-only refusal). `ReviewPanes` renders the workspace over `shown ?? (reading ? frame : null)`, passes `reading` only when nothing answers, and hands `ReviewTechnicalDetails` the answer alone (or an `unanswered` label), so records are never shown under another subject; the page controls render only for an answer. The root publishes `data-review-pending` or `data-review-unavailable` with the requested subject, and `ReviewOutcomeRegion` receives `readingInWorkspace` so the read is stated once. `useReaderEngagement` on the root reports reader gestures to `navigation.engage` (the late-catalogue rule, see `ReviewNavigation.tsx`).

**One lane read for the tree comparison on screen (MIK-L32; review R1 F1, ruling 2026-09-30T13:07:38).**
`ReviewPanes` calls `useReviewLane(repo, master, leaf, treeComparisonNumber(payload.limitations))` once and hands
the result as `laneRead` to both `ReviewWorkspace` (the lane's rail destinations, its center and the source
explorer's labels) and `ReviewTechnicalDetails` (the source pane's attribution counts and lists), so every surface of
a tree comparison shows the one classification and there is exactly one `lane=files` request per comparison. A
dataset review names no tree comparison, so the hook asks nothing and both receive `null`.

Since `260921-ICR-L47`, `useSurface` passes `hold: navigation.settling` to `useReviewReadCycle`, so the
reviewer's first read waits (at most `SUBJECT_HOLD_MS`) for the catalogue to choose a subject, and calls
`useObservedComparison(navigation.observeComparison, shown)` so the navigation re-reads its catalogue only
when the displayed snapshot pair changes. The file grew by 3 lines to 931, over the 900-line soft rail
(L47-R1-F5, routed to L48, which reworks this file). **L48 closed it:** the record panes moved to
`ReviewRecordPanes.tsx`, leaving this file at 585 lines.

| Finding | Anchor | Source |
| --- | --- | --- |
| The held first read and the snapshot observation. | `hold: navigation.settling`; `useObservedComparison` | dashboard/src/panels/review/ReviewSurface.tsx:484-509 |

### Conventions

The component imports its types from `../../data/review` (the public entry that re-exports the
transport surface), the page helpers it mounts (`REVIEW_WALKABLE_COLLECTIONS`, `carriedPage`,
`continuationOf`, `intentOnlyRefusal`, `pageBounds`) from that same public entry, `ReviewPagedCollection`
as a type from it, its read cycle (`ReviewPageRequest`, `targetKeyOf`, `useReviewReadCycle`) from
`./ReviewReadCycle`, the refresh control and its one derivation from `./ReviewRefresh`, the read phases
plus the region from `./ReviewOutcome`, and the workspace together with its state hook from
`./ReviewWorkspace` — which is what makes one module the owner of the outcome states. It declares no
client of its own, **no longer imports `DiffPane`** — the diff engine is reached through
`KnowledgeStatements`, which is what keeps one rule in one place — and **no longer imports
`SourceContent`**, because an openable row is mounted by `SourceExplorer.tsx` now. Inline `style`
objects are used throughout,
matching the cockpit panels' idiom, and
every list item carries a stable `key` derived from the record's own identifiers (`assessment_id`,
`record_kind:record_id`, `signal_id`, `item_id:field`, `claim_id:path`, `claim_id`). Data attributes
carry the machine-readable facts — `data-pane`, `data-binding`, `data-change-state`,
`data-submission-state`, `data-testid` — so the surface's behaviour is inspectable without reading its
text. Sub-components are plain functions taking the payload or the pane they render; **none of them
holds state**, and the only reader state this file owns is `instead`, `selection`, the
`useWorkspaceState()` value and (L48) the surface's read cache, all held by `useSurface` for
`ReviewSurface`. The per-record keys and `data-*` attributes listed above now live with the record
renderers in `ReviewRecordPanes.tsx`. `data-side-state` **no longer
appears in this file**: it moved with the statement area into
`KnowledgeStatements.tsx`, where the same attribute still spells a side's declared state.

### Invariants And Boundaries

No browser path selects a dataset. Failed reads may retain only the last coherent answer to the same question and never invent an empty review. The frame keeps only the shell: nothing of the frame's subject is rendered as the requested subject's reading, records or comparison identity (`ICR-R26` isolation, L48). A selection never unmounts the workspace once a frame exists; only the first read, which has no frame, is stated at the surface level. One-sided statements, subject applicability, evidence currentness and authored assessments retain their existing owners. Source review remains reachable when only intent is unavailable.

### Todos

None recorded. The assessment-publication control is deliberately not shipped by this increment, and
the Source pane's expansion is a read: no control on this surface writes, and the byte-form rows stay
identification-only until this vocabulary can carry a path as bytes.

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
| `useSurface` owns the behavior described above, including the cache, `selectSubject` and the `reading` status. | `useSurface`; `selectSubject`; `ReviewReadCache` | dashboard/src/panels/review/ReviewSurface.tsx:453-532 |
| The unanswered subject's status, keyed and labelled with the requested subject. | `readingStatusOf` | dashboard/src/panels/review/ReviewSurface.tsx:375-395 |
| `ReviewPanes` owns the behavior described above: the workspace over the answer or the frame, the records only for an answer, and the one lane read handed to both (MIK-L32). | "function ReviewPanes({"; "const laneRead = useReviewLane("; "<ReviewTechnicalDetails" | dashboard/src/panels/review/ReviewSurface.tsx:302-370 |
| One lane read per comparison through the real surface; none for a dataset review. | "offers the two lane destinations after the families, with their file and hunk totals" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:85-99 |
| `ReviewSurface` owns the behavior described above, including the cache provider, the pending/unavailable root attributes and the engagement observer. | `ReviewSurface`; `ReviewReadCacheContext`; `useReaderEngagement` | dashboard/src/panels/review/ReviewSurface.tsx:534-598 |
| `PageControls` owns the behavior described above. | `PageControls` | dashboard/src/panels/review/ReviewSurface.tsx:256-295 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260921-ICR-L25 Round 3 — The Reviewer's Own Narrow-Width Shape

**This surface gained its own scrollport and the layout constraints that let its panes fit a narrow
column.** The work is one round of the accepted design's B7 line, and it was driven by the round-2
verifier's findings F1 and F2 — so the shape of the change is best read as *two answers to two measured
facts*, not as a restyle.

**F2's answer: a vertical affordance of this panel's own.** The cockpit's `MAIN` is `overflow: hidden` by
a deliberate, documented shell decision (`cockpit/Cockpit.tsx`: *"the viewport does not scroll, its panel
scrolls on its own"*), shared with every other view. This panel had supplied no scrollport, so at 320 px
it rendered 7 620 px of content into a 706 px box that clipped it: `userScrollableCount` was **0**, the
window was exactly viewport-height, three wheel trials moved nothing, and a long guarantee was reachable
only by the browser's programmatic focus scroll. The root now carries
`style={{ height: "100%", minHeight: 0, minWidth: 0, overflowY: "auto" }}` — `height: 100%` plus
`minHeight: 0` *fills* the shell's row instead of growing past it, and `overflowY: auto` is the
scrollport a reader can move. **The shell was not changed and its decision is not overridden here.**

**F1's answer: the panes may shrink and wrap.** F1's measurement is what named the real cause — 51 of the
64 overflowing elements at 320 px were descendants of `[data-testid="review-surface"]` (the reviewer's own
root, `:906`), not of the inner `review-workspace`, and the pane sections were **565 px wide inside a
294 px column** with no pannable ancestor. The cause is a grid-item minimum, not a width: each pane is a
**grid item** of the disclosure, so its automatic minimum size is content-based unless it is told
otherwise, and the identities this surface prints are single unbreakable tokens — a 64-character
comparison reference measured **539 px**, a repository path **565 px** — while the inherited `break-word`
does **not** lower min-content. Three declarations answer it together, and none of them works alone:

- `pane` carries `minWidth: 0` and `overflowWrap: "anywhere"` (`:89-97`);
- the disclosure's own grid track is `minmax(0, 1fr)`, not the implicit `auto` (`:774-782`), because the
  track must be allowed to shrink below its items' min-content for the panes' `min-width: 0` to bite;
- the header row wraps (`flexWrap: "wrap"`) and the subject span takes its own `minWidth: 0` +
  `overflowWrap: "anywhere"` (`:828-848`), because at 320 px that row was the last thing past the edge —
  one unbreakable line of identities beside two controls, pushing the refresh control 4 px out.

**The regression pin, and what it does not claim.** `ReviewSurface.narrow.test.tsx` is the new
acceptance module for this change and it asserts **these declarations**, on `review-surface` rather than
on the inner root, precisely because neither round's defect was a wrong computation a rendered-text case
could catch. It is honest about its own limit: jsdom has no layout engine, so a `getBoundingClientRect()`
case there would read zeros and pass vacuously, and the module labels itself a **pin** while pointing at
the served-bundle probe for the measurement. Its card is
[ReviewSurface.narrow.test.tsx](ReviewSurface.narrow.test.tsx.md).

**Re-measured after the fix, and stated as the round-3 measurement reports it:** descendants of
`review-surface` past the viewport edge went **51 → 0** and the total **64 → 13**, with all 13 in neither
review root — they are cockpit chrome. `review-surface` is now the scrollport (`userScrollableCount`
0 → 1; a wheel over the review moves it 0 → 800 px), and `MAIN` no longer clips (its `scrollHeight`
7620 → 706, equal to its `clientHeight`). **The number was not improved by changing the root** — the
inner root's count was already 0 in both rounds, which is exactly why F1 was a classification defect.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The pane helper's two load-bearing declarations (moved unchanged to `ReviewRecordPanes.tsx` by L48).** | `pane`; "minWidth: 0"; "overflowWrap"; `data-pane` | dashboard/src/panels/review/ReviewRecordPanes.tsx:33-41 |
| **The disclosure track that lets the panes shrink: `minmax(0, 1fr)`, not the implicit `auto`.** | "const TAKEOVER = 'changeset-viewer'"; "gridTemplateColumns: 'minmax(0, 1fr)'"; `review-details` | dashboard/src/panels/review/ReviewRecordPanes.tsx:31-31; dashboard/src/panels/review/ReviewRecordPanes.tsx:462-483 |
| The header wraps the task/subject controls while keeping their context and refresh action available. | `ReviewHeader` | dashboard/src/panels/review/ReviewSurface.tsx:397-451 |
| The reviewer root owns its vertical scrollport while the shell retains its own layout responsibility. | `reviewShell`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:52-81; dashboard/src/panels/review/ReviewSurface.tsx:534-598 |
| The fixture builder and the mount this pin relies on, cited from their own declarations. | `payload` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:44-110 |
| The shell decision this file does **not** change, and which stays routed to the cockpit owner: the comment that states it sits on the declaration itself. | "the viewport does not scroll"; `overflow: "hidden"` | dashboard/src/cockpit/Cockpit.tsx:328-328 |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32 (review R1 F1, ruling 2026-09-30T13:07:38).** Logic records that `ReviewPanes` makes the one lane read (`useReviewLane` over `treeComparisonNumber(payload.limitations)`) and hands it to the workspace and the technical details; none for a dataset review. The `ReviewPanes` row is reworded and re-anchored on line-exact quotes ("function ReviewPanes({", "const laneRead = useReviewLane(", "<ReviewTechnicalDetails"), re-measured to `302-370`; one row added (the one-read surface case). The other rows moved by the two imports and the read were re-pointed by the installed fixer (its bullets kept) or by the exact base-to-staged shift. No verification stamp was advanced.
- 2026-09-30T12:06:26+00:00: Generated citation repair: `pane`; "minWidth: 0"; "overflowWrap" repointed to dashboard/src/panels/review/ReviewRecordPanes.tsx:33-41; dashboard/src/panels/review/ReviewRecordPanes.tsx:35-35; dashboard/src/panels/review/ReviewRecordPanes.tsx:35-35. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:06:26+00:00: Generated citation repair: "the viewport does not scroll" repointed to dashboard/src/cockpit/Cockpit.tsx:328-328. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T21:55:52+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **re-citation of rows whose earlier range arrived by generated projection.** The memory-quality check reopened the disclosure-track row because an older *Generated citation repair* bullet in this card names `TAKEOVER` and `gridTemplateColumns`, so a range written there was never shown to be reviewed. Each row was re-read against the construct it is about in this candidate, the claim still holds, and its anchor was re-bound from the bare name to the exact declaration text the curator read (`const TAKEOVER = 'changeset-viewer'`, `gridTemplateColumns: 'minmax(0, 1fr)'`), which is the check's own remedy (re-cite the location the claim is about). The generated bullets below are left untouched as the dated record of the projection. No stamp advanced.
- 2026-09-28T21:46:09+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — the reviewer stays mounted across subject selection (`ICR-R24@v3`; Architect ruling on L48-R1 F1/F2; L47-R1-F5; `ICR-R26`/`R17`/`R10`/`R12`/`R16` preserved).** The surface now owns one bounded `ReviewReadCache`, computes a subject-bound `reading` status (`readingStatusOf`) over the read cycle's `frame`, mounts the workspace over the answer or that frame, hands records only for an answer, publishes pending/unavailable root attributes, and observes reader engagement. The record panes moved to `ReviewRecordPanes.tsx` (931 → 585 lines), closing L47-R1-F5. The card's L47-era account that a selection re-reads into an unmounted surface is **superseded**; the rule that a payload is shown only under its own target key is **preserved** and now also governs the shell. Purpose, Logic, Conventions and Invariants updated; the five reopened claims were re-read; the round-3 rows now cite the moved `pane`/`TAKEOVER`/disclosure track in `ReviewRecordPanes.tsx` (the old "comment that states why" wording named a comment that does not exist and was dropped). Historical section prose (line counts, `:NN` ranges) is left as the dated record it is. No stamp advanced.
- 2026-09-28T17:11:24+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — the surface wires the navigation's hold and snapshot observation (`ICR-R24@v3`).** Records the two added calls and the soft-rail overrun routed to L48 (L47-R1-F5). Displaced rows re-pointed. No stamp advanced.
- 2026-09-26T21:10:43+00:00: Generated citation repair: `TAKEOVER`; `gridTemplateColumns` repointed to dashboard/src/panels/review/ReviewSurface.tsx:80-80; dashboard/src/panels/review/ReviewSurface.tsx:706-706. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:43+00:00: Generated citation repair: `payload` repointed to dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:44-110. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T20:20:54Z — Reconciled authoritative subject reads, exact revision comparison and accessible selection behavior.
- 2026-09-26T19:49:05Z — Reconciled the shared navigation, single read-cycle composition and progressive technical details.
- 2026-09-26T00:35+02:00 — 260921-ICR-L25 curator, round 3 (re-read of a reopened claim on the round-3 change itself; leaf `260921-ICR-L25`): **the reopened `pane` claim was re-read against the current anchored construct and both its wording and its range are correct as they now stand.** The finding is the expected consequence of this round editing the very construct the claim is about: `pane` gained `minWidth: 0` and `overflowWrap: "anywhere"` in this leaf's round 3, so its evidence legitimately changed after the card was verified. The claim's own words — that the four helpers keep the pane bodies readable and that the attribution prints an unresolved author rather than an anonymous one — still hold, and the row now cites each helper's own declaration. **The round-3 section above was written in this same pass and is the body update this change required**; this entry records the re-read the guidance asks for. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `ReviewHeader`; `flexWrap` repointed to dashboard/src/panels/review/ReviewSurface.tsx:797-857; dashboard/src/panels/review/ReviewSurface.tsx:831-831. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T00:15:00+02:00 — 260921-ICR-L25 curator, round 3 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 verifier `verify-l25-round2.md` sha256 `dd34cee2b5bc2068023ba9e7af1f7b037edc995bc6019d9bacbed9f00619870b`, findings F1/F2): **body update — the surface gained its own scrollport and the declarations that let its panes fit a narrow column, and this card gained the round-3 section and the two invariants that state them.** The new section records F2's answer (the panel's own `overflowY: auto` scrollport, with the shell's `MAIN: overflow: hidden` left as the shell's deliberate decision rather than overridden) and F1's answer (the real cause is a **grid-item minimum**, so `minWidth: 0` + `overflowWrap: "anywhere"` on `pane`, `minmax(0, 1fr)` on the disclosure track, and a wrapping header row — three declarations of which none works alone), plus the re-measured after-state (51 → 0 inside the reviewer root, 64 → 13 with the 13 in neither root; `userScrollableCount` 0 → 1; `MAIN.scrollHeight` 7620 → 706). It names the new pin module and its card, and states plainly that the pin holds **declarations** and not pixels. **Citation accounting:** every row this round's insertions displaced was re-derived from each construct's declaration at this tip; the two pre-existing rows into `changeSetBar.tsx` (`:455`, `:337-384` for `selector_id`/`useReviewCatalogue`) were checked and left where their anchors still resolve. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **the outcome states left this file, the read became four phases, and the retained generation is now keyed to the question it was read for.** This is the body update for that change, and it corrects three statements the card previously made rather than carrying them: (1) "three states carry the outcome" — `payload`/`refusal`/`error` are replaced by one `ReviewRead` phase plus `retained` and `instead`; (2) "the component's single `useState` for `payload` holds the refetch outcome, so a refusal and a stale payload can never be on screen together" — that is no longer the mechanism and no longer the rule: a **failed** read deliberately keeps the last coherent comparison on screen, while a **typed refusal** replaces the panes, and the asymmetry lives in `shownPayload`; (3) the `RefusalBlock` paragraph — the inline `RefusalBlock` and the `review-error` paragraph were **removed, not duplicated**, and `ReviewOutcome.tsx` owns them. The new mechanism is recorded in full: `targetKeyOf` as the one identity a read answers for, the reset in `load` plus the render-time check as the two halves of "never under the wrong header", `instead` as the second explicitly-asked question (asked with no selector), and `retryFor`/`insteadFor` as the only two controls the composition adds. The card also records **two measured limits as routed, not fixed**: the **in-flight** prop/question race (pre-existing at HEAD and on the round-1 bytes, routed to **R17** with R24) and the **browser-class A01/A13 journeys** (not verified by this leaf; **R25** with R24/R17). Line count 549 → 632. Every row of the reference table was re-derived against this candidate. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00), and the leaf's own recorded working candidate states what was actually read; nothing in this leaf is committed, so closeout owns the stamp.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the Source pane's inventory rows became the way into their own content, and the file grew 462 → 549 lines.** `inventoryEntry` gained `repo`/`master`/`leaf`/`generation`/`open`/`onOpen` and now renders the published path as a `<button data-testid="review-inventory-open" data-path=… aria-expanded=…>` **only when the inventory named both code trees**, mounting the new `SourceContent` beneath an open row at those two tree ids; `byteNamedEntry` gained `data-testid="review-byte-path-not-addressable"`, which states that a byte-form row cannot be opened through this surface because no expansion request can name it; `Inventory` gained `const [open, setOpen] = useState<string | null>(null)`, derives the generation pair from its own published `before_code_tree_id`/`after_code_tree_id`, and is now the one stateful sub-component on this card; `SourcePane` forwards the task context into `Inventory`; and the header now names **two** reused renderers — `DiffPane` (through `KnowledgeStatements`) and `SourceContent` — instead of one. The body was updated before this entry: Purpose, the Conventions paragraph (the import, and the one stateful sub-component), two new invariants (an entry opens at the generation the listing published; a byte-named row is marked unopenable rather than offered a control), the boundary sentence, and Todos. **Citation accounting:** every row of the reference table was re-derived against this candidate and the re-derived rows are stated here so a reader can audit the pass — `ReviewSurface.tsx` header `1-7` → `1-9`, `ReviewTarget` `27-37` → `30-39`, `ReviewSurface` `395-462` → `482-549`, `TAKEOVER` `38`/`453` → `41`/`540`, `pane`/`muted`/`attribution`/`unresolvedList` `40-74` → `43-71`, `fieldValue` `70-77` → `78-79`, `assessmentBlock` `78-90` → `81-92`, `authoredEffect`/`signalBlock` `91-126` → `94-125`, `KnowledgeFacts` `127-155` → `130-155`, `AuthoredRecords` `156-178` → `159-180`, `KnowledgePane` `179-206` → `182-205`, `SourcePane` `265-307` → `337-393`, `EvidencePane` `308-358` → `395-444`, `SubmissionBlock` `359-380` → `446-466`, `RefusalBlock` `381-394` → `468-480`, and `review.ts` `intentReview` `271-285` → `328-342`; three rows were added for the constructs this leaf introduced (`inventoryEntry`/`review-inventory-open`/`SourceContent` at `214-260`, `byteNamedEntry`/`review-byte-path-not-addressable` at `270-282`, `Inventory`/`useState` at `291-335`), and one cross-range correction was made on the cockpit/target row (`ChangeSetViewer.review` `41` → `38-44`, so the anchor occurs inside the cited range). The superseded L6 row values are left in place in the entry below, because this history is append-only and that entry was true of the candidate it names. **Stamp accounting:** the verification pair now names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against — and the recorded working candidate states the leaf's own uncommitted candidate; no commit contains the bytes this card now describes, so closeout owns the real stamp.
- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`): **the statement area left this file, and a field row learned to tell absence from a recorded empty.** `KnowledgePane` now renders `KnowledgeStatements` where it used to hold the both-sides-present gate on `DiffPane` plus the two `sideState` paragraphs; the `sideState` helper is deleted, `DiffPane` is no longer imported here, and `data-side-state` no longer appears in this file. The new `fieldValue` helper prints `(absent)` for a value the server did not send and `(recorded empty)` for a value that is present and empty, so no field row is silently blank. Every row in the reference table was **re-derived against this candidate** — `ReviewTarget` `27-37`, `TAKEOVER` `38`, `pane`/`muted`/`attribution`/`unresolvedList` `40-74`, `fieldValue` `70-77`, `assessmentBlock` `78-90`, `authoredEffect`/`signalBlock`/`AuthoredRecords` `91-126`/`156-178`, `KnowledgeFacts` `127-155`, `KnowledgePane` `179-206`, `SourcePane` `265-307`, `EvidencePane` `308-358`, `SubmissionBlock` `359-380`, `RefusalBlock` `381-394`, `ReviewSurface` `395-463` — while the rows describing the L22/R02/L45 constructs this leaf did not touch kept their claims and moved only where the source moved. The card's stale claims were **corrected rather than carried**: the header no longer says the diff is fed "only when both sides are `present`", `sideState` is recorded as deleted, and the invariants now say the statement-side rule belongs to `KnowledgeStatements.tsx`. **Stamp accounting:** the verification pair still names production line `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9`, the last real commit whose bytes this card was verified against; nothing in this leaf is committed, so claims whose evidence this leaf's change moved are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **R02's rendering half: the inventory is displayed in all three of its states, and a review with no comparison identity renders as itself.** Added `Inventory`, `inventoryEntry` and `byteNamedEntry`; made `SourcePane` open with the inventory; made the Knowledge pane's selection line survive an absent `comparison` by naming that no comparison was made; made `ReviewTarget`'s selectors optional and the header print `whole task (no subject selected)`; and made the root's `data-comparison` optional-chained. The card's Purpose and Logic were re-pointed accordingly and every row in the reference table was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's three-pane display. It records that the surface is **display-only** — no POST, no form, no submit handler, and a submission block that prints the existing authority's path rather than offering a control — and the five renderings a reader must not flatten: a missing side is printed as its own named state (so `DiffPane` is fed only when both sides are `present`), an unresolved attribution is printed rather than dropped, the remaining counts print `not measured (reason)` rather than a zero, the authored records and the mechanical signals sit under their own headings in their own lists, and the stale/submission block prints neither state as favourable. It also records that the component is mounted through the cockpit's change-set takeover under `data-view="intent-review"` rather than through a route of its own. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. What was actually read is this leaf's uncommitted working tree, and closeout owns the stamp once the code commit exists.

## 260921-ICR-L10 The Page Control That Reaches The Rest, And The Refusal It Renders

`260921-ICR-L10` (`ICR-R10@v1`) makes the remainder reachable. The surface used to render a
remainder with no control that reached the rest of the collection — the packet's own non-conforming
example — and it now renders the bounds, the scope and one action that advances the walk with the cursor
**the server published**, plus a first page action when a cursor was refused.

The control is `PageControls` with `PagePicker`, `PageActions` and `PageBoundsLine`, and the refusal is
`PageRefusalBlock`: the code, the owner's two identities, and a live first page of the collection that
was asked for. The page is part of the read's target key, so a page change is its own read rather than a
re-render over the wrong payload. No next action is offered for a body that published no cursor,
whatever remainder it reported — a button that fetches nothing is the defect this control exists to
prevent. Keyboard and focus traversal of the control remain `ICR-R24@v1`'s.

**ICR-R31@v1 narrows what the picker offers, not what the wire carries.** `PagePicker` maps
`REVIEW_WALKABLE_COLLECTIONS`, so it offers only the collections whose first page exists — `knowledge`
and `records`. The client's `ReviewPagedCollection` still carries all three members, and
`family_members` is deliberately not offered with no cursor because it is the set of per-family roster
walks a response composed: naming it would fetch the server's own `comparison_page_unreadable` refusal
for a question the reader did not mean to ask. A response whose page *is* `family_members` still renders
through the same bounds and continuation controls as any other.

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the page control, and the refusal it renders.** `PageControls`, `PagePicker`, `PageActions`,
`PageBoundsLine` and `PageRefusalBlock` are new, and the page is now part of the read's target key, so a
page change is its own read. Two facts are load-bearing: the action sends the cursor the server
published rather than the one the client stands on, and no next action is offered without a published
cursor. Every row on this card that cited this component by line was re-derived against this candidate,
because this leaf moved them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
## 260921-ICR-L26 The Three Mounted Labels

`260921-ICR-L26` (`ICR-R26@v1`) mounts the server's attribution facts on both review panes through three
small renderers and no new state: `applicabilityNote` prints one record's treatment with the true subject
its binding names (and prints **nothing** when the payload carries no label), `contextList` renders the
labelled context rows with the relationship that reached each one and the record's kind, and
`applicabilityCounts` renders the six-way partition beside the collections it filtered.
**879 → 946 lines.**

**A label is displayed, never computed.** The three renderers read the fields the server sent — the note
prints the server's own `detail` beside its `state` and subject, the context list prints the server's
`relationship` and `references`, and the counts block formats the server's numbers — and none of them
derives a treatment, a relationship or a total. A payload published before this vocabulary mounts exactly
as it did before, with no empty block standing in for an absent one.

**One record, one treatment, two panes.** `applicabilityNote` is called on the knowledge pane's
assessment/effect/signal rows and on the evidence pane's evidence link and observation rows, so the same
record cannot read one way in one pane and another way in the other; `contextList` and
`applicabilityCounts` are mounted on both panes for the same reason. The sibling's finding is **not**
rendered from a context row at all — the row carries the record's kind, and that is the whole point of
the value.

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the three attribution renderers and their mount points on both panes (879 → 946 lines; `ICR-R26@v1`).** The card records that the labels are displayed rather than computed, that an absent label mounts nothing, and that the same record carries one treatment across both panes. **Citation accounting:** the rows this leaf's insertions moved were re-derived from each renderer's own extent in the 946-line candidate — the per-record blocks `116`/`109`/`225`/`464`→`174-186`/`226-251`, `authoredEffect`/`signalBlock` (six one-line ranges)→`188-201`/`203-221`/`255-276`, `KnowledgePane`→`278-303` with `SourcePane` `435-491`, and `EvidencePane` `395-444`→`493-546`. Wording was retained where the claim still states what the code does. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
## 260921-ICR-L12 The Record Is Part Of The Question, And The Header States It

`260921-ICR-L12` (`ICR-R12@v1`) makes the record a first-class part of this surface's question and
says out loud which record the panes below are read from:

- **`history` joins `ReviewTarget` and the target key.** The key is now
  `repo/master/leaf/<history ?? "live">/<question>/<position>`, so switching records reloads rather
  than reinterpreting a response read for another record — the same rule the page cursor already
  followed. `intentReview` receives it as its last argument.
- **`ReviewHeader` is the surface's header, extracted as one component because the record statement is
  a claim about everything under it.** It renders the mounted provenance line
  (`data-testid="review-history"`) only for the recorded read: "recorded comparison — this leaf's
  durable generation, re-read from its own record: the panes below are the comparison it bound, not
  whatever the repository holds now." The root publishes `data-review-history` (`live` or the record)
  so a reader or a case can see the record without opening a pane.
- **`ReviewPanes` mounts the three panes and the two controls above them for one payload.**
- **Both extractions clear the lint rail without widening it.** `ReviewSurface` had grown past its
  `max-lines-per-function` rail while gaining the record statement; the two components were extracted
  with no ignore added and no limit changed, and every prop is threaded rather than re-derived.

The refusal path is untouched: a recorded read that earns a refusal still reaches the reader with its
code, detail and action, which is what makes a leaf that recorded nothing a stated state rather than a
missing entry.

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the record is part of the question, and the header states it (ICR-R12@v1).** `history` joined
`ReviewTarget` and the target key, so a response is never applied to a surface that asked for another
record; `ReviewHeader` mounts the provenance line and the root publishes `data-review-history`; and
`ReviewHeader`/`ReviewPanes` were extracted to clear the `max-lines-per-function` rail with no ignore
and no limit widened. **Citation accounting:** every row into this module was re-derived against the
candidate. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and
the governed closeout owns the real stamp.

## 260921-ICR-L17 The Read Cycle And The Refresh Control Leave The Surface

`260921-ICR-L17` (`ICR-R17@v1`) makes this surface a renderer of a read cycle it no longer owns, and
takes **462 lines of read logic and rendering out of it**. Two new modules arrive beside it in the same
child route:

- [`ReviewReadCycle.ts`](ReviewReadCycle.ts.md) owns the question's identity (`targetKeyOf`), the one
  read started for it (`startRead` through `askReview`) and the state a reader's refresh needs
  (`useReviewReadCycle`, returning the read, the retained comparison, the carried binding identity and
  the `refresh` callback). `ReviewPageRequest` is declared there now and imported back, because the page
  position participates in the target key the hook computes.
- [`ReviewRefresh.tsx`](ReviewRefresh.tsx.md) owns the reader's explicit refresh control, the notice
  that answers it, and the one derivation of a claim (`generationOf`). The header receives both as a
  `refresh` node and mounts them beside the subject line, because the control belongs to the question the
  header names and the notice describes the comparison the panes below are showing.

**What is deleted here rather than moved.** The inline `load` callback, the `useEffect` that called it,
the `targetKeyOf` function, the private `ReviewPageRequest` interface and the `useState`/`useCallback`
read state are all gone: `useReviewReadCycle` supplies `read`, `retained`, `carried` and `refresh`, and
what stays in this component is the `instead` state, the `selection` state, the coherence check on the
retained generation and the wiring of the three regions.

**What a later reader must not undo.** The retained generation is still used only when it was read for
the question on screen now (`retained.key === targetKey`): the check is belt-and-braces beside the
reset inside the hook, because a payload under a header it was not read for is exactly the mismatch this
surface must not be able to produce. `retryFor` now takes the hook's `refresh` rather than a reload
promise, so a retry is the same one read path as the refresh control and can never become a second way
of composing a review.


## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the read cycle and the refresh control left the surface for their own modules (`ICR-R17@v1`).** The inline `load` callback, its `useEffect`, `targetKeyOf` and the private `ReviewPageRequest` are **deleted, not annotated**: `ReviewReadCycle.ts` supplies the read, the retained generation, the carried identity and `refresh`, and `ReviewRefresh.tsx` supplies the control and the notice, both mounted through the header's new `refresh` node. `retryFor` re-asks through the same one read path. The coherence check on the retained generation is kept, because a payload read for another question must not render under this one's header. **Citation accounting:** the rows this extraction moved were re-derived from each construct's own declaration on the 986-line candidate — `Inventory` `:389`, `pane` `:81`, `unresolvedList` `:154`, `targetKeyOf` (now `ReviewReadCycle.ts:62-83`, called at `ReviewSurface.tsx:934`) and `reviewSourceContent` (`data/review.ts:654`). **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the extraction exists only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.

## 260921-ICR-L23 The Unmeasured Line The Submission Block Mounts

`SubmissionBlock` gains a third mounted line, keyed on `staleness.state === "not-measured"`
(`:557-565`) and carrying `data-testid="review-staleness-unmeasured"`. It renders the boundary's
own sentence and nothing else: no previous input is named, because nothing was observed to move,
and the block's existing `stale` line (`:554`) and disabled-submission state are untouched.
That is the whole point of the state — a switched checkout or an unreadable generation must not
be able to read as an ordinary current review on the one line this block mounts, and it must not
be able to borrow the `stale` rendering that would assert a movement nobody measured.

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed, no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **body refresh for the workspace composition and the single inventory owner, plus the citation repair of this card's 18 unsatisfied rows.** The card now states what this candidate does: `ReviewPanes` mounts `ReviewWorkspace` as the reading path and **retains** the three panes inside one `<details data-testid="review-details">` disclosure; the inventory body, `inventoryEntry` and `byteNamedEntry` were deleted here and moved to [`SourceExplorer.tsx`](SourceExplorer.tsx.md), so `SourcePane` carries a `review-source-explorer-pointer` paragraph and the attribution side of the same records instead of a second inventory; `ReviewSurface` owns `useWorkspaceState()` above the pane switch — so a page request can no longer destroy the reader's display choices — and passes it down as `workspace`/`state`; `ReviewPanes` gained `selectorKind`/`selectorId`/`history`; and `PagePicker` offers only `REVIEW_WALKABLE_COLLECTIONS`. The row describing the one load path was corrected with it, because the surface no longer composes the request itself. **Citation repair:** both `citation_claim_reopened` rows were re-pointed at the constructs that replaced the ones they named (`SourcePane` → `302-352`; `byteNamedEntry` → `SourceExplorer.tsx:137-149`), the fourteen `citation_anchor_absent_from_range` rows at the ranges that really hold their anchors (`60-74`/`819-910` for the whole input, `844-853` for the one load path, `78-83`/`85-89`/`91-100`/`151-167` for the four helpers, `168-170`/`242` for `fieldValue`, `171-183`/`290`/`397` for `assessmentBlock`, `185-198`/`200-218`/`252-273` for the authored half, `275-300` for pane 1, the explorer's `78-129`/`99-109`/`116-125`/`137-149`/`227-229`/`194-232`/`234-315` for the moved inventory row, byte-form row and inventory body, `409-438`/`740` for the submission block, `SourceContent.tsx:189-265`/`85-129`/`131-141`/`143-155` for the entry-expansion renderer, and `data/review.ts:533-549`/`717-735` for the client), and the two `citation_range_out_of_bounds` citations (`68-946`, `922-934`) were replaced by the ranges their constructs occupy now. Every target range was verified with `sed -n 'START,ENDp'` over the frozen candidate before it was written. The two further rows whose constructs this leaf's own diff moved were re-pointed in the same pass (the takeover row → `76-77`/`757`; pane 3 → `354-407`/`760`), and the workspace-state invariant now cites the hook's reset rather than a `load` this file no longer has. A third row was repaired the same way: the reviewer-entry row named `subject.selector_id`, a spelling that occurs nowhere in the code, so it now names `selector_id` and cites `changeSetBar.tsx:460-460`, the line that reads it from the server's own resolution, with the two contributing citations kept. No row was dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **the surface mounts the boundary's own sentence, and this card's body now states where.** `SubmissionBlock` renders `staleness.statement` behind `data-testid="review-staleness-unmeasured"` when the state is `not-measured` (`:557-565`), naming no previous input and borrowing neither the `stale` line (`:554`) nor its disabled-submission state. The new section above records the rendering and the reason it may not read as an ordinary current review. **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
