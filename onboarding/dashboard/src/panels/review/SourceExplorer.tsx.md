# dashboard/src/panels/review/SourceExplorer.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SourceExplorer.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
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
| One row's extra notes: a mode change, a content classification that is not `unknown`, and the owner's own detail line. | "entry.mode_change"; "entry.content === \"unknown\""; "entry.detail ?? null" | dashboard/src/panels/review/SourceExplorer.tsx:89-93 |
| The expansion gate and the open row's identity, both derived from the published values. | "const expandable"; "const isOpen" | dashboard/src/panels/review/SourceExplorer.tsx:94-95 |
| The row itself: the entry test id with its status, and the published path as a button carrying `data-path` and `aria-expanded`. | "review-inventory-entry"; "data-status"; "review-inventory-open"; "data-path={entry.path}"; "aria-expanded={isOpen}" | dashboard/src/panels/review/SourceExplorer.tsx:97-109 |
| The path printed exactly as published with the status beside it, and the notes after that. | "{entry.path}"; "{entry.status}"; "notes.join" | dashboard/src/panels/review/SourceExplorer.tsx:110-114 |
| **The open row's content: `SourceContent` mounted with the task context, the row's entry, the inventory's two tree ids and the caller's layout and full-file disclosure.** | `SourceContent`; `beforeCodeTreeId`; `afterCodeTreeId`; `mode={layout}`; `collapse={!fullFile}` | dashboard/src/panels/review/SourceExplorer.tsx:115-126 |
| **The byte-form row: listed by its exact byte form with its status and detail, carrying no expansion control, and stating in words that no expansion request can name it.** | "review-inventory-byte-path"; "entry.path_bytes"; "review-byte-path-not-addressable" | dashboard/src/panels/review/SourceExplorer.tsx:137-149 |
| The byte-form row's own sentence: its content is not openable through this surface because its name is carried as bytes. | "not openable through this surface" | dashboard/src/panels/review/SourceExplorer.tsx:143-146 |
| The explorer's two display controls, with the layout and full-file values published as data attributes and an `aria-pressed` state. | "review-display-controls"; "review-diff-layout"; "review-full-file"; "data-full-file" | dashboard/src/panels/review/SourceExplorer.tsx:153-189 |
| The rows list: every measured entry, then every path carried by byte form, with the generation taken from the inventory's own tree ids. | `InventoryRows`; `inventory.entries.map`; `byByteForm.map(byteNamedEntry)` | dashboard/src/panels/review/SourceExplorer.tsx:194-232 |
| The explorer section, its own inventory state attribute, and the bar holding the heading and the controls. | `SourceExplorer`; "review-source-explorer"; "data-inventory-state"; "Complete source change explorer" | dashboard/src/panels/review/SourceExplorer.tsx:234-278 |
| **The inventory's own population sentence: the state, the partial flag, the measured listed total, the byte-form count and the owner's detail.** | "review-inventory"; `listed_total`; "by byte form"; "inventory.detail" | dashboard/src/panels/review/SourceExplorer.tsx:279-286 |
| **The module's own statement that a family or member selection attributes changes and never removes one from this list.** | "review-population-scope"; "it never removes one from this list" | dashboard/src/panels/review/SourceExplorer.tsx:287-290 |
| The unclassified tail: the listed paths whose kind or status these owners could not report. | "review-inventory-unclassified"; "unclassified.length" | dashboard/src/panels/review/SourceExplorer.tsx:301-306 |
| The reproducing command with both tree ids, so a reader can re-measure the listing. | `review-inventory-command`; `inventory.command`; `before_code_tree_id` | dashboard/src/panels/review/SourceExplorer.tsx:307-312 |
| The open path is owned by the workspace rather than by this component, so a linked expression in the central review can open the same entry. | "owned by the workspace rather than by this component" | dashboard/src/panels/review/SourceExplorer.tsx:254-256 |
| The entry-expansion renderer this module mounts and does not restate. | "export function SourceContent(" | dashboard/src/panels/review/SourceContent.tsx:189-189 |
| The centre that mounts this explorer at the payload's own inventory, handing it the caller-owned preferences and the workspace-owned open path. | `SourceExplorer`; `open={openPath}`; `onOpen={onOpenPath}` | dashboard/src/panels/review/FamilyReviewCenter.tsx:861-872 |
| The workspace that owns the open path and the two preferences this explorer renders. | `useWorkspaceState`; `openFromCenter` | dashboard/src/panels/review/ReviewWorkspace.tsx:377-390 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The explorer lists one repository namespace's
changed paths and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the complete source change explorer. It records that the module is the comparison's whole changed-path population (the family navigation is an attribution lens and never an exclusion filter), that `layout`, `fullFile` and `open` are owned by the caller so neither a diff-layout switch nor a family/member selection can collapse an expansion, that `inventoryEntry` prints the published path exactly and opens it at the inventory's own two tree ids through `SourceContent`, that `byteNamedEntry` lists a byte-carried path and marks it not addressable with no expansion control, that `InventoryRows` renders the measured entries and the byte-form paths as two lists, that `DisplayControls` carries the two preferences as controls with `data-*`/`aria-*` state, and that `SourceExplorer` renders the inventory's own population sentence and the statement that a selection never removes a change from the list. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
