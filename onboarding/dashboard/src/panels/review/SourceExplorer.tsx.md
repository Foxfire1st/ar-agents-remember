# dashboard/src/panels/review/SourceExplorer.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SourceExplorer.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The complete source change explorer: **every changed path of the comparison's bound pair, openable at the
generation the listing named**, with an explicit diff layout and full-file control. It became its own
module because `ReviewSurface.tsx` is over the repository's file-size rail and the explorer is a
responsibility of its own — it owns one inventory's three states, the entries' opening controls and the two
display preferences a reader sets while reading.

**What it must not do, in the module's own words.** It lists *every* changed path the inventory measured,
including the ones no family or invariant attribution reaches: the family navigation is an **attribution
lens, never an exclusion filter**. The three inventory states are never rendered as one another — a
measured empty set says the two trees agree, an unavailable measurement says nothing was observed and why,
and a partial one says which entries could not be classified or carried as names.

**The two preferences are the reader's, not the selection's (`ICR-R24@v3`).** `layout` (split/inline) and
`fullFile` are owned by the caller and passed down, so switching the diff layout while a file is expanded
cannot reset that expansion, and selecting another family or member cannot either. The open path is the only
state this component holds, and it is keyed by the path the server published — and it too is owned by the
caller, so a linked expression in the central review can open the same entry.

**Verification stamp.** `lastVerifiedCommitHash` names the leaf's base commit
`5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`; this module exists only in the leaf's **uncommitted working
tree**, so the stamp means "leaf base commit plus this leaf's working-tree delta" and does not claim that
the commit holds this content. Governed closeout owns the real stamp.

## Code Commentary

### Logic

**`SourceExplorer` is the section, and its population sentence is the inventory's own.** The root is
`<section data-testid="review-source-explorer" data-inventory-state={inventory.state}>`. Its bar carries
the heading and `DisplayControls`; then the `review-inventory` paragraph prints `source change inventory
(<state>[, partial]): <listed_total> listed path(s)[ + N by byte form] — <detail>`; then
`review-population-scope` states that this explorer is the whole measured change set of the comparison's
bound pair and that **a family or member selection below attributes changes; it never removes one from this
list**; then `InventoryRows`; then, only when there are any, the `review-inventory-unclassified` tail naming
the listed paths whose kind or status these owners could not report; then the
`review-inventory-command` line: the reproducing `command` and, when both ids are present, the
`before_code_tree_id → after_code_tree_id` pair. The population sentence depends on no family or member
selection at all, which is why it is stated here rather than inside the family navigation.

**`InventoryRows` derives the one generation object from the inventory's own published tree ids and renders
two lists.** `generation` is `{ before: inventory.before_code_tree_id, after: inventory.after_code_tree_id }`,
and `byByteForm` is `inventory.unrepresentable_paths ?? []`. The measured entries render as one `<ul>`
(each through `inventoryEntry`), and the byte-form paths as a second `<ul>` (each through `byteNamedEntry`).
Either list is omitted when it is empty rather than rendered as an empty list.

**`inventoryEntry` is one row and the way into its own content.** It joins the row's extra notes —
`mode changed`, `content: <state>` unless the content is `unknown`, and the owner's own `detail` — and then
computes `expandable = generation.before !== undefined && generation.after !== undefined` and
`isOpen = open === entry.path`. The `<li>` carries `data-testid="review-inventory-entry"` and
`data-status={entry.status}`. When the inventory named both code trees the path is rendered inside a
`<button data-testid="review-inventory-open" data-path={entry.path} aria-expanded={isOpen}>` prefixed with
`▾ ` or `▸ `, and the same click toggles the row closed (`onOpen(isOpen ? null : entry.path)`); otherwise
the path is printed as plain `<code>`. Either way the status follows the path, and the notes follow the
status. When the row is open **and** expandable, the same function mounts `SourceContent` beneath it with
the task context (`repo`/`master`/`leaf`), the row's own entry, the two published tree ids
(`beforeCodeTreeId`/`afterCodeTreeId`), `mode={layout}` and `collapse={!fullFile}` — so the content a reader
opens is the generation the listing named, drawn with the caller's two preferences. The path text is
printed exactly as it was published: a tab or a newline inside a name is part of the address.

**`byteNamedEntry` is the one row that must not look openable, and it says so.** It renders the `<li>` with
`data-testid="review-inventory-byte-path"` and `data-status`, the exact `entry.path_bytes` inside `<code>`,
the status, a `mode changed` marker when there is one, the owner's `detail`, and then the
`data-testid="review-byte-path-not-addressable"` sentence: this row's content is not openable through this
surface, because its name is carried as bytes for identification and no expansion request can name it.
There is no `<button>` and no expansion affordance at all — that is `ICR-R03`'s boundary inherited from a
text-only vocabulary, not a decision taken here.

**`DisplayControls` is the reader's two preferences as controls rather than decorations.** It renders a
`<span data-testid="review-display-controls" data-diff-layout={layout}>` holding a labelled
`<select data-testid="review-diff-layout">` with `split`/`inline` (the change handler maps anything that is
not `"inline"` back to `"split"`) and a `<button data-testid="review-full-file" data-full-file={...}
aria-pressed={fullFile}>` whose label is `showing full file` or `showing changed regions`. Neither control
claims anything about the comparison.

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

- **Every changed path the inventory measured is listed.** The byte-form rows are a second list, not an
  omission; a path whose content cannot be rendered is still a change that must be listed.
- **The family navigation is an attribution lens, never an exclusion filter.** A selection attributes
  changes and never removes one from the list, and the population sentence says so on the page.
- **The three inventory states are never rendered as one another.** A measured empty set, an unavailable
  measurement and a partial one are three different facts, and the state also rides
  `data-inventory-state` on the section.
- **`layout` and `fullFile` are the caller's, so neither a diff-layout switch nor a family/member selection
  can collapse an expansion.** `open` is the caller's for the same reason; this component holds no state.
- **A listed entry opens at the generation the listing named.** The two tree ids are the inventory's own
  `before_code_tree_id`/`after_code_tree_id`, travel with the request, and a row opened after the branch
  moved still shows the generation the reader was looking at.
- **A row whose name is bytes is listed and marked unopenable, not offered a control.** `byteNamedEntry`
  carries the exact byte form, the status, the reason and no expansion affordance, because no request this
  vocabulary can spell would address it.
- **An entry is openable only when the inventory named both code trees.** `expandable` gates the button,
  so a row is never offered a control that could not fetch anything.
- **The path is printed exactly as published.** A tab or a newline inside a name is part of the address, and
  the same string is the button's `data-path`.
- **A long path wraps and the control stays unclipped.** The path is a `mono` string with no spaces in
  it, so it has a very large **min-content** width; without a break opportunity the button takes that
  width, every grid item above it refuses to shrink, and the whole column grows past its track.
  `rowButton` therefore carries `overflowWrap: "anywhere"` and `maxWidth: "100%"` (260921-ICR-L25,
  register B7). The property that matters is the one `break-word` does **not** have: `anywhere` also
  lowers the element's own min-content width, which is what lets the column shrink instead of
  overflowing. Measured on the mounted product at 320 px before the fix, one `review-inventory-open`
  button was **556 px wide inside a 294 px column** and its right 262 px was cut off by the app shell's
  `overflow-x: hidden` with **no pannable ancestor** — neither visible nor reachable; after the fix it
  is 252 px in a 252 px container with `scrollWidth == clientWidth`.
- **`inReviewSurface: 0` was true of the wrong root, and the B7 line was completed in round 3 — the whole
  history, because two successive readings of this one sentence were both wrong.** The round-2 sentence
  this card first carried — *"the residual 64 are the cockpit's own status bar, **outside the review
  surface**"* — was **false as worded** (round-2 verifier's F1, `verify-l25-round2.md`, sha256
  `dd34cee2b5bc2068023ba9e7af1f7b037edc995bc6019d9bacbed9f00619870b`): the count had been classified
  against the **inner** `[data-testid="review-workspace"]` root (`ReviewWorkspace.tsx:515`) while the
  Intent Reviewer's own root is `[data-testid="review-surface"]` (`ReviewSurface.tsx:906`, mounted by
  `Cockpit.tsx:585`). Against the reviewer's own root, **51 of the 64** overflowing elements at 320 px
  were descendants of the reviewer — sections 565 px wide inside a 294 px column, `pannableCount 0` of
  64, the root's own `scrollWidth 311 > clientWidth 294` — and the vertical half was worse: **nothing in
  the document was user-scrollable at all**, because `MAIN` is `overflow-y: hidden` carrying 7 620 px of
  content in a 706 px box. **Round 3 then fixed both halves in the reviewer's own code**, and the numbers
  are re-measured: descendants of `review-surface` past the edge **51 → 0**, total **64 → 13** with all
  13 in *neither* review root (cockpit chrome), the pane sections **294 px in a 294 px column** (were
  565), the root's own `scrollWidth`/`clientWidth` **311/294 → 294/294**, and `userScrollableCount`
  **0 → 1** as `review-surface` itself became the scrollport (a wheel over the review moves it
  **0 → 800 px**). **The improvement was not bought by changing the root**: the inner root's count was 0
  in *both* rounds. The cause round 3 removed was a **grid-item minimum**, not a width — each pane is a
  grid item whose automatic minimum size is content-based, and `break-word` does not lower min-content —
  which is why the same `min-width: 0` + `overflow-wrap: anywhere` pair this card's own `rowButton`
  carries is also what the panes needed. **What remains routed, and it is no longer the reviewer's:** the
  shell's deliberate `MAIN: overflow: hidden` decision and its **13** cockpit-chrome elements, owned by
  R24's cockpit takeover.
- **Boundary.** This module lists and opens; it measures nothing. The inventory, its state, its counts and
  its `command` are the server's, the expansion's own branches and refusals belong to `SourceContent.tsx`,
  and the diff renderer is reached from there rather than re-implemented here.

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

Every claim on this card is checkable in the shipped candidate: the module's own statement of its
responsibility and of the rule it must not break, the caller-owned preferences and open path, the two row
renderers and the generation they open at, the display controls, the inventory's own population sentence,
the unclassified tail and the reproducing command, plus the owners it reuses and the centre that mounts it.
Every anchor in a row below occurs on a line inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it is and why it is its own module, and the two renderers it reuses rather than restating.** | "The complete source change explorer"; "WHY THIS IS ITS OWN MODULE"; "ICR-R24@v3"; `DiffPane` | dashboard/src/panels/review/SourceExplorer.tsx:1-19 |
| **The population rule: the family navigation is an attribution lens, and the three inventory states are never rendered as one another.** | "exclusion filter"; "A measured empty set says the two trees agree"; "None of the three is rendered as another" | dashboard/src/panels/review/SourceExplorer.tsx:15-19 |
| The two preferences are the caller's, so neither a layout switch nor a selection change can collapse an expansion; the open path is this component's only state. | "open path is the only state this component holds" | dashboard/src/panels/review/SourceExplorer.tsx:10-13 |
| The exported layout type the workspace and the centre both take. | `DiffLayout` | dashboard/src/panels/review/SourceExplorer.tsx:29-29 |
| One row's extra notes: a mode change, a content classification that is not `unknown`, and the owner's own detail line. | "entry.mode_change"; "entry.content === \"unknown\""; "entry.detail ?? null" | dashboard/src/panels/review/SourceExplorer.tsx:102-104; dashboard/src/panels/review/SourceExplorer.tsx:103-104; dashboard/src/panels/review/SourceExplorer.tsx:104-153; dashboard/src/panels/review/SourceExplorer.tsx:104-273 |
| **The row's own control style, and (260921-ICR-L25) the two properties that keep a long path wrapped and unclipped.** | `rowButton`; `overflowWrap`; `maxWidth` | dashboard/src/panels/review/SourceExplorer.tsx:60-89 |
| The expansion gate and the open row's identity, both derived from the published values. | "const expandable"; "const isOpen" | dashboard/src/panels/review/SourceExplorer.tsx:106-107 |
| The row itself: the entry test id with its status, and the published path as a button carrying `data-path` and `aria-expanded`. | "review-inventory-entry"; "data-status"; "review-inventory-open"; "data-path={entry.path}"; "aria-expanded={isOpen}" | dashboard/src/panels/review/SourceExplorer.tsx:63-148 |
| The path printed exactly as published with the status beside it, and the notes after that. | "{entry.path}"; "{entry.status}"; "notes.join" | dashboard/src/panels/review/SourceExplorer.tsx:109-126; dashboard/src/panels/review/SourceExplorer.tsx:125-126; dashboard/src/panels/review/SourceExplorer.tsx:126-151 |
| **The open row's content: `SourceContent` mounted with the task context, the row's entry, the inventory's two tree ids and the caller's layout and full-file disclosure.** | `SourceContent`; `beforeCodeTreeId`; `afterCodeTreeId`; `mode={layout}`; `collapse={!fullFile}` | dashboard/src/panels/review/SourceExplorer.tsx:7-134; dashboard/src/panels/review/SourceExplorer.tsx:27-134; dashboard/src/panels/review/SourceExplorer.tsx:128-134 |
| **The byte-form row: listed by its exact byte form with its status and detail, carrying no expansion control, and stating in words that no expansion request can name it.** | "review-inventory-byte-path"; "entry.path_bytes"; "review-byte-path-not-addressable" | dashboard/src/panels/review/SourceExplorer.tsx:151-155; dashboard/src/panels/review/SourceExplorer.tsx:152-155 |
| The byte-form row's own sentence: its content is not openable through this surface because its name is carried as bytes. | "not openable through this surface" | dashboard/src/panels/review/SourceExplorer.tsx:156-156 |
| The explorer's two display controls, with the layout and full-file values published as data attributes and an `aria-pressed` state. | "review-display-controls"; "review-diff-layout"; "review-full-file"; "data-full-file" | dashboard/src/panels/review/SourceExplorer.tsx:153-189 |
| The rows list: every measured entry, then every path carried by byte form, with the generation taken from the inventory's own tree ids. | `InventoryRows`; `inventory.entries.map`; `byByteForm.map(byteNamedEntry)` | dashboard/src/panels/review/SourceExplorer.tsx:194-232 |
| The explorer section, its own inventory state attribute, and the bar holding the heading and the controls. | `SourceExplorer`; "review-source-explorer"; "data-inventory-state"; "Complete source change explorer" | dashboard/src/panels/review/SourceExplorer.tsx:246-246; dashboard/src/panels/review/SourceExplorer.tsx:279-279; dashboard/src/panels/review/SourceExplorer.tsx:280-280; dashboard/src/panels/review/SourceExplorer.tsx:283-283; dashboard/src/panels/review/SourceExplorer.tsx:294-294 |
| **The inventory's own population sentence: the state, the partial flag, the measured listed total, the byte-form count and the owner's detail.** | "review-inventory"; `listed_total`; "by byte form"; "inventory.detail" | dashboard/src/panels/review/SourceExplorer.tsx:63-203; dashboard/src/panels/review/SourceExplorer.tsx:63-297 |
| **The module's own statement that a family or member selection attributes changes and never removes one from this list.** | "review-population-scope"; "it never removes one from this list" | dashboard/src/panels/review/SourceExplorer.tsx:299-299; dashboard/src/panels/review/SourceExplorer.tsx:301-301 |
| The unclassified tail: the listed paths whose kind or status these owners could not report. | "review-inventory-unclassified"; "unclassified.length" | dashboard/src/panels/review/SourceExplorer.tsx:313-314; dashboard/src/panels/review/SourceExplorer.tsx:314-315 |
| The reproducing command with both tree ids, so a reader can re-measure the listing. | `review-inventory-command`; `inventory.command`; `before_code_tree_id` | dashboard/src/panels/review/SourceExplorer.tsx:226-226; dashboard/src/panels/review/SourceExplorer.tsx:321-321; dashboard/src/panels/review/SourceExplorer.tsx:322-322 |
| The open path is owned by the workspace rather than by this component, so a linked expression in the central review can open the same entry. | "owned by the workspace rather than by this component" | dashboard/src/panels/review/SourceExplorer.tsx:266-266 |
| The entry-expansion renderer this module mounts and does not restate. | "export function SourceContent(" | dashboard/src/panels/review/SourceContent.tsx:189-189 |
| The centre that mounts this explorer at the payload's own inventory, handing it the caller-owned preferences and the workspace-owned open path. | `SourceExplorer`; `open={openPath}`; `onOpen={onOpenPath}` | dashboard/src/panels/review/SourceExplorer.tsx:246-246 |
| The workspace that owns the open path and the two preferences this explorer renders. | `useWorkspaceState`; `openFromCenter` | dashboard/src/panels/review/ReviewWorkspace.tsx:387-387; dashboard/src/panels/review/ReviewWorkspace.tsx:392-424 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The explorer lists one repository namespace's
changed paths and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-25T22:19:46+00:00: Generated citation repair: "const expandable"; "const isOpen" repointed to dashboard/src/panels/review/SourceExplorer.tsx:106-106; dashboard/src/panels/review/SourceExplorer.tsx:107-107. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "not openable through this surface" repointed to dashboard/src/panels/review/SourceExplorer.tsx:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "review-population-scope"; "it never removes one from this list" repointed to dashboard/src/panels/review/SourceExplorer.tsx:299-299; dashboard/src/panels/review/SourceExplorer.tsx:301-301. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "owned by the workspace rather than by this component" repointed to dashboard/src/panels/review/SourceExplorer.tsx:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `useWorkspaceState`; `openFromCenter` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:392-424; dashboard/src/panels/review/ReviewWorkspace.tsx:387-387. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T00:15:00+02:00 — 260921-ICR-L25 curator, round 3 (same uncommitted change set, now also carrying `ReviewSurface.tsx` + the new `ReviewSurface.narrow.test.tsx`; round-3 report `report-l25-round3.md` = `cf6fb86e4d20cf5a1baf6bd093e4d9b1ccbf017062503da23edbf40d44e52b86`): **body update — the B7 residual sentences this card carried from round 2 are superseded, because round 3 fixed both halves in the reviewer's own code.** The invariant now carries the whole history of one sentence rather than only its latest state: the round-2 "residual is outside the review surface" claim was **false as worded** (classified against the inner `review-workspace` root), round 3 fixed the reviewer's own overflow and its own scrollport, and the numbers are re-measured — descendants of `review-surface` past the edge **51 → 0**, total **64 → 13** (all 13 in neither review root), panes **565 → 294 px** in a 294 px column, the root's own **311/294 → 294/294**, `userScrollableCount` **0 → 1**, and a wheel over the review moving the surface **0 → 800 px**. **The two sentences that were false are quoted in the corrected text so a later reader can see what changed and why** — a correction that only states the new number would leave the next reader unable to tell whether the old one was wrong or merely stale. **What remains routed and is no longer the reviewer's:** the shell's deliberate `MAIN: overflow: hidden` decision (`cockpit/Cockpit.tsx:323`) and its 13 cockpit-chrome elements, owned by R24. **Citation accounting:** this module's own rows are unchanged — its `rowButton` fix was never the disputed part — and the corrected text cites the reviewer root's own current line. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2, **correction against the independent verifier** (same uncommitted change set; verifier `verify-l25-round2.md` first line `pass-with-findings`, file sha256 `dd34cee2b5bc2068023ba9e7af1f7b037edc995bc6019d9bacbed9f00619870b`; its findings F1/F2, §4): **the B7 sentence this card first carried was FALSE AS WORDED and is corrected in place.** The round-2 claim — `inReviewSurface: 0`, with the 64 residual elements being the cockpit's own chrome "outside the review surface" — classified membership against the **inner** `[data-testid="review-workspace"]` root (`ReviewWorkspace.tsx:515`) rather than the Intent Reviewer's own root `[data-testid="review-surface"]` (`ReviewSurface.tsx:866`, mounted by `Cockpit.tsx:585`). Re-measured by the verifier against both roots at 320 px: **64 total overflowing · 0 descendants of `review-workspace` · 51 descendants of `review-surface` · 13 neither** — so 51 of the 64 are **inside** the reviewer, including `review-refresh`, `diff-pane`, `review-selection`, `review-conditions`, `review-locations`, `review-field-changes`, `review-unassessed`, `review-applicability`, `review-expansion` and `review-source-explorer-pointer` (565 px wide in a 294 px column, `pannableCount 0` of 64, the reviewer root's own `scrollWidth 311 > clientWidth 294`). **F2 makes the vertical half worse:** at 320 px **no element in the document is user-scrollable** — `MAIN` is `overflow-y: hidden` with 5 375–7 620 px of content in a 706 px box, the window is exactly viewport-height, and three wheel trials move nothing, so the review is reachable only by programmatic focus scroll. **What this card still states, because it is measured and true:** this module's own fix is real — the path button is 252 px in a 252 px container with `scrollWidth == clientWidth`, and the page no longer overflows horizontally at 1600 or at 320. **What changed:** B7 is not fully fixed, the residual is inside B7's own criterion and inside the reviewer, and it is **routed to the cockpit/R24 owner as a named residual rather than placed outside the surface.** No verification stamp was advanced. No commit was made.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the path button now wraps instead of being clipped, and this card gained the invariant and the row that record it.** `rowButton` gained `overflowWrap: "anywhere"` and `maxWidth: "100%"`. The discriminating property is that `anywhere`, unlike `break-word`, also lowers the element's **min-content** width — the property that was forcing the grid track to grow — so the column shrinks instead of overflowing. Measured on the mounted product at 320 px: before, one `review-inventory-open` button was 556 px wide inside a 294 px column with its right 262 px cut off by the shell's `overflow-x: hidden` and no pannable ancestor (neither visible nor reachable); after, 252 px in a 252 px container (register B7). **The residual sentence this entry first carried is superseded by the correction above, which is dated and stands on the verifier's own measurement.** **Citation accounting:** the two rows this file's own insertion moved were re-derived from their constructs' declarations (`rowButton` `:70-89`, `inventoryEntry` `:90-148`), and the new row cites `:60-89` for the comment block plus the style it explains. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the complete source change explorer. It records that the module is the comparison's whole changed-path population (the family navigation is an attribution lens and never an exclusion filter), that `layout`, `fullFile` and `open` are owned by the caller so neither a diff-layout switch nor a family/member selection can collapse an expansion, that `inventoryEntry` prints the published path exactly and opens it at the inventory's own two tree ids through `SourceContent`, that `byteNamedEntry` lists a byte-carried path and marks it not addressable with no expansion control, that `InventoryRows` renders the measured entries and the byte-form paths as two lists, that `DisplayControls` carries the two preferences as controls with `data-*`/`aria-*` state, and that `SourceExplorer` renders the inventory's own population sentence and the statement that a selection never removes a change from the list. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
