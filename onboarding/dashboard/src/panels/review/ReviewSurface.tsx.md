# dashboard/src/panels/review/ReviewSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T06:50:00+02:00 |
| lastVerifiedCommitHash |  `09329a7ee598920c519b06305b73ba8e48d72c88`|
| lastVerifiedCommitDate |  2026-09-26T00:58:43+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Intent Reviewer surface: three panes over one comparison, and **every state that is not a review**.
The header states the boundary in one line — **the surface is display-only** — and then the three things
that follow from it: it renders records other owners store, it carries every attribution it was given,
and it produces no conclusion of its own, so there is no summary, no severity, no score and no control
that writes anything.

Since ICR-R16 the header also states the read's four phases, because the surface's job at the transport
boundary is to render each of them as itself: `loading` while the request is in flight, `reviewed` (with
the known-empty note when the answer measured nothing), `refused` for the owner's typed refusal, and
`failed` for a transport-level failure — an unwired adapter, an unadmitted input, no HTTP response at
all. Every non-review phase goes through `ReviewOutcome.tsx`, which carries the server's own code,
reason, offending input and next action, so an actionable refusal is visible instead of `404 Not Found`.
The header then states the two guarantees this file is responsible for keeping: **a failed read never
erases the last coherent comparison** (it stays on screen, labelled, and no empty review is claimed for
it), and **a retained comparison is stored and shown with the question it was read for** (`targetKeyOf`),
so a payload is never rendered under a header it was not read for. The **two** renderers it reuses are fed by other owners: the `DiffPane` fed the
statements the comparison published — **both operands when both sides recorded one, and the available
operand beside the named absence when one side did not** (that second case is ICR-R06's, and its rule
lives in `KnowledgeStatements.tsx`, which this file delegates the whole statement area to) — and the
Source pane's own entry expansion, whose rule lives in `SourceContent.tsx` and which is what a listed
inventory entry opens into.

Since ICR-R24@v3 the surface is a **composition** rather than three panes and two controls. It mounts
`ReviewWorkspace` as the reading path — scope/status header, the family tree and the unified central
column, with the complete source change explorer beneath it — and **retains** the three panes below
that inside one `<details data-testid="review-details">` disclosure, so every control, refusal,
limitation and technical identity they carry is still on the page, reached deliberately instead of
being the first thing a reviewer has to read past. The inventory body, `inventoryEntry` and
`byteNamedEntry` are [`SourceExplorer.tsx`](SourceExplorer.tsx.md)'s now: this file renders no
inventory, and the Source pane states where the one explorer is rather than rendering a second answer
to "which paths changed".

This is a new route under `panels/`, mounted through the cockpit's change-set takeover rather than
through a route of its own: `ChangeSetTarget` carries an optional `review` variant and `Cockpit.tsx`'s
`ChangeSetTakeover` renders this component instead of `ChangeSetViewer` when it is present, under
`data-view="intent-review"`.

## Code Commentary

### Logic

**`ReviewTarget` is the component's whole input, plus a back callback.** It carries `repo`, `master`,
`leaf` and the two optional selector fields — a task context and one *recorded* subject, and nothing
else — and `ReviewSurface` takes `ReviewTarget & { onBack: () => void }`. No path is accepted, so the
component cannot name a dataset; the server resolves the candidate from the task context the target
carries. Both selector fields are optional because a task-context review names no subject, and the
header line prints `whole task (no subject selected)` when neither is present.

**The load is one `useCallback` plus one `useEffect`, and three values carry the outcome.** `read` is a
`ReviewRead` phase (`loading` | `reviewed` | `refused` | `failed`) produced by `readFrom(result)` or, on
a throw, `{ phase: "failed", problem: reviewProblemFromCause(cause) }`; `retained` is the last payload
this surface really read, stored **with the key it was read for**; and `instead` is the refusal the
reader answered by asking for the task's own source inventory. `load` sets `loading`, drops a retained
payload whose key is no longer the current question, calls
`intentReview(repo, master, leaf, instead ? undefined : selectorKind, instead ? undefined : selectorId)`
— the `instead` branch is the second, explicitly asked question, asked with **no selector** — and stores
the phase and, for a `review` answer with a payload, `{ key: targetKey, payload }`. The effect depends on
`load`, whose dependency array is the target fields plus `instead` and `targetKey`, so a target or
question change refetches and an unrelated re-render does not. There is no submit handler, no form and
no POST anywhere in the file — which is the display-only boundary expressed as the absence of a code
path.

**The retained generation is keyed to the question it was read for, and that key is what makes the two
guarantees one mechanism.** `targetKeyOf(repo, master, leaf, instead, selectorKind, selectorId)` is the
one definition of the identity a read answers for — the task context **and** the question asked
(`task-context` when the reader asked for the inventory instead, otherwise `<kind>:<id>`). `load` drops a
retained payload whose key differs from the current one, and the render re-checks `retained.key ===
targetKey` before `shownPayload` uses it — belt-and-braces beside the reset, because a payload under a
header it was not read for is exactly the mismatch this surface must not be able to produce. `coherent`
is therefore `null` for any other question, and `lastCoherent` is passed to the region only for a
`failed` read.

**Four small helpers keep the pane bodies readable, and a fifth now serves pane 1's field rows.**
`pane(title, children)` wraps a section with `data-pane={title}`; `muted(text, testid?)` renders the
secondary-line paragraph the panes use for a stated absence; `attribution(author?, inputs)` renders
`author: unresolved reference` when the author is `undefined` and `author: <name>` otherwise,
appending the examined inputs when there are any; and `unresolvedList(entries)` renders the
`review-unresolved` list, or `null` when there is nothing unresolved. **`fieldValue(value?)` is the
fifth, and it is the one this leaf added:** one mechanical field transition has three different facts
behind its two values — a value the server did not send is the recorded fact that the field was
*absent* on that side (`(absent)`), a value that IS there and is empty is a *recorded empty* list
(`(recorded empty)`), and anything else prints as itself. So no row is ever silently blank and no
reader has to decide which of the two a gap meant. **`sideState` is gone**, and its removal is the
seam: the statement area is no longer rendered here at all.

**The statement area is delegated, and that delegation is the R06 rule's one home.**
`KnowledgePane` renders `<KnowledgeStatements before={knowledge.before_statement}
after={knowledge.after_statement} />` where it used to hold the both-sides-present gate plus the two
`sideState` paragraphs. `KnowledgeStatements.tsx` owns the four branches (both present → the shipped
two-sided diff; one present beside an `absent` → a one-sided diff with the absent side named above it;
one present beside `binary`/`unresolved` → the available text as content, the reason beside it, and no
diff; neither present → both state lines) and it, not this file, imports `DiffPane` and `FilePane`.

**The three panes are three components, each reading only its own pane off the payload.**
`KnowledgePane` prints the comparison reference and policy (or `no knowledge comparison was made ·
<selection_detail>`), the delegated statement area, `KnowledgeFacts`, `AuthoredRecords`, the
assessments or the `review-unassessed` line, and the pane's own unresolved list. `SourcePane` opens
with the `review-source-explorer-pointer` paragraph — which names where the one explorer is, with the
measured listed-path count and the inventory's state — and prints the locations with their role
(`unclassified (no role recorded)` when the
role is absent), a `before-only` marker, the change state and the resolution, then the
`review-remaining` line that renders `name: not measured (reason)` when `value` is `undefined` and
`name: <value>` otherwise, then the unattributed paths and the expansion reference with its command,
or the stated absence of an expansion. `EvidencePane` branches on `evidence_state`: `recorded`
renders the `review-evidence` link list and the `review-observations` list, otherwise it prints "No
recorded evidence links", then states that source-based inspection remains available when
`source_inspection_available`, then the assessments or the `review-unassessed` line, then the pane's
unresolved list.

**`KnowledgeFacts` and `AuthoredRecords` are extracted so pane 1 reads as a composition.**
`KnowledgeFacts` renders the essential conditions each side recorded (only when at least one side has
any), the retained-revision groups as `side:record_id=count` joined by `·` or `none selected`, and
every field transition as `field: <beforeValue> → <afterValue>` through `fieldValue` — so an absent
value and a recorded empty one are two different words and neither is a blank. `AuthoredRecords`
renders the authored effects and the detection signals **under their own headings, in their own
lists** — "Authored effects and preservation claims" and "Detection signals (facts, not findings)" —
which is the display half of the vocabulary's rule that a signal is never rendered in the shape of a
finding. Each authored effect prints its `record_kind`, its label, its id, its rationale and its
attribution; each signal prints its condition, input set, id, extractor and policy versions, its
relationship paths and its scope limitations, and nothing else.

**`assessmentBlock` reuses one renderer for both panes' assessment lists.**
`KnowledgePane` and `EvidencePane` both map `assessmentBlock`, which prints the disposition, the
finding, the rationale, the attribution with the examined inputs, the binding state as
`data-binding`, and the role when it is present. There is no second rendering of a recorded
assessment, so the two panes cannot disagree about how one looks.

**`SubmissionBlock` prints staleness and submission together, because they are one fact.**
It prints the stale line with the statement and the previous input reference only when
`staleness.state === "stale"`, then the submission state as `DISABLED` or `not offered` with the
reason, the next action, and the dispositions the existing authority accepts with the standing
sentence that none is publication approval.

**`RefusalBlock` is gone: the outcome states left this file.** The old inline `RefusalBlock` and the
generic `review-error` paragraph were **removed, not duplicated** — `ReviewOutcome.tsx` now owns the
loading line, the known-empty note, the one refusal/failure block (with every field the owner published)
and the two notes about a shown payload. What stays here is the wiring: `retryFor(read, load)` offers the
retry **only** for a `failed` read (a typed refusal keeps its owner's own next action), and
`insteadFor(read, problem, instead, setInstead)` offers the source-inventory control only for a `refused`
read whose code is intent-only and only when the reader has not already taken it. `ReviewSurface`'s
returned tree carries `data-testid="review-surface"`, `data-comparison` from the **shown** payload's
comparison reference (optional-chained, so an absent identity is an absent attribute rather than a
crash) and `data-review-target` from the three task identifiers, so the subject and the comparison a
rendering belongs to are on the element rather than inferred from its text.

**The takeover class is shared with the change-set viewer.** `TAKEOVER = "changeset-viewer"` is applied
to the pane grid **inside the disclosure**, so the surface inherits the takeover layout rather than
declaring a second one, while the component is mounted under its own `data-view="intent-review"` on the
cockpit side.

**The workspace is the reading path, and the three panes are retained beneath it.** `ReviewPanes`
mounts `SubmissionBlock`, `PageControls` and then `ReviewWorkspace` — scope/status header, family tree
and the unified central column, with `SourceExplorer` as the population section — and puts the three
panes inside one `<details data-testid="review-details">` whose summary reads "complete payload details
— knowledge, attribution, evidence and refusal records". A disclosure is used rather than a tab bar
because collapsing it hides nothing from the DOM and nothing from the keyboard. `ReviewPanes` also
gained `selectorKind`/`selectorId`/`history`, because the workspace it mounts needs the same question
identity the read was asked for.

**The reader's local workspace state is owned here, above the pane switch.** `ReviewSurface` calls
`useWorkspaceState()` and passes the value down as `workspace` (the workspace receives it as `state`),
because `ReviewPanes` returns `null` while a page read is in flight: state owned below that switch is
destroyed and re-initialised by every page request, which discarded the reader's display choices (the
family/member selection, the filter, the diff layout, the full-file disclosure and the expanded path)
and made the centre's continuation control single-use (ICR-L24 fix round 5, V10).

**The collection picker offers only the collections that have a first page (ICR-R31@v1).** `PagePicker`
maps `REVIEW_WALKABLE_COLLECTIONS`, so the two options beside "whole review" are `knowledge` and
`records`. The client's `ReviewPagedCollection` still carries all three members and this narrows
nothing about the server contract: `family_members` is the set of per-family roster walks a response
composed rather than one walk, so naming it with no cursor would be a control that fetches the server's
own `comparison_page_unreadable` refusal for a question the reader did not mean to ask. A response whose
page *is* `family_members` renders through the same bounds and continuation controls as any other.

**The surface renders a review that compared nothing, and the inventory it used to render has one owner
elsewhere.** The header prints `whole task (no subject selected)` when no selector was named.
`KnowledgePane` prints the comparison identity when there is one and
`no knowledge comparison was made · <selection_detail>` when there is not, under the `review-selection`
test id. The inventory body, `inventoryEntry` and `byteNamedEntry` were **deleted here and moved to
[`SourceExplorer.tsx`](SourceExplorer.tsx.md)**, which the workspace mounts once as the population
section: it renders all three inventory states (measured, partial, unavailable) and never as an empty
list, prints `listed_total`, the `+ N by byte form` count, the server's own `detail` and the reproducing
`command` with both tree ids, prints one changed path exactly as published with its status and its
renderability beside it, and prints a changed path whose name cannot be carried as text by its exact
byte form with its status and the stated reason. `SourcePane` therefore carries the attribution side of
the same records plus the pointer paragraph, because a second inventory here would be a second answer
to "which paths changed".

**A listed entry is still the way into its own content, and the open row is the explorer's.** It is
`SourceExplorer`'s `open` prop — the path the server published — and it is owned by the workspace rather
than by the explorer, so a linked expression in the central column can open the same entry and neither a
diff layout switch nor a family selection collapses it. `InventoryRows` derives the `generation` object
from the inventory's own `before_code_tree_id`/`after_code_tree_id`, and `inventoryEntry` renders the
row's path as a `<button data-testid="review-inventory-open" data-path={entry.path}
aria-expanded={isOpen}>` **only when the inventory named both code trees**; the same click toggles the
row closed. The path text is still printed literally — a tab or a newline inside a name is part of the
address, and the address is also the button's `data-path`, which is how a case or a reader can find the
row it means. When a row is open it mounts `SourceContent` beneath it with the task context
(`repo`/`master`/`leaf`), the two published tree ids and the reader's `layout`/`fullFile` preferences,
so the content a reader opens is the generation the listing named.

**The byte-form row is the one row that must not look openable, and it says so.** `byteNamedEntry` (now
`SourceExplorer.tsx`'s) has no control at all and carries
`data-testid="review-byte-path-not-addressable"`, which states that the row's content cannot be opened
through this surface because its name is carried as bytes for identification and no expansion request
can name it. A reader can still act on the bytes beside it with Git directly; what the pane must not do
is imply that clicking it would open anything. That is the boundary ICR-R03 inherits from the text-only
vocabulary rather than a decision taken here.

**The pane grid no longer forwards the task context, because it no longer mounts the expansion.** The
three panes receive the payload alone; `ReviewPanes` forwards `repo`/`master`/`leaf`, the selector and
the history into `ReviewWorkspace`, which passes them on to `SourceExplorer` — the same three the root's
`data-review-target` stamps. Nothing in this file resolves a tree, a path or a generation: the ids it
forwards are the ones the server published to this client.

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
holds state**, and the only reader state this file owns is `instead`, `selection` and the
`useWorkspaceState()` value, all three held by `ReviewSurface` itself. `data-side-state` **no longer
appears in this file**: it moved with the statement area into
`KnowledgeStatements.tsx`, where the same attribute still spells a side's declared state.

### Invariants And Boundaries

- **Display-only.** The file contains no POST, no form and no submit handler; the one request is a
  read, and the submission block prints the authority's path rather than offering a control.
- **No conclusion is rendered.** There is no summary, severity, score, verdict or approval anywhere in
  the tree; the surface prints the records and the attributions it was given.
- **A side's state is printed by its new owner, and this file does not re-decide it.**
  `KnowledgeStatements` renders every non-two-sided area's state lines and chooses diff versus content
  from the declared states; this file passes the two `ReviewSideContent` values through unchanged.
- **A field row's absence and its recorded-empty value are two different words.** `fieldValue` is the
  only place a missing value becomes text, and it prints `(absent)` for the first and
  `(recorded empty)` for the second.
- **The diff renderer is reused, not re-implemented.** It is reached through `KnowledgeStatements`
  (which imports `DiffPane` from the change-set route and `FilePane` from the file-viewer route)
  rather than declared a second time here.
- **The three panes are retained, not removed.** They are mounted inside one
  `<details data-testid="review-details">` disclosure below the workspace: collapsing it hides nothing
  from the DOM and nothing from the keyboard, so every control, refusal, limitation and technical
  identity they carry is still on the page.
- **The reader's workspace state is owned above the pane switch.** `useWorkspaceState()` is called by
  `ReviewSurface` and passed down, because `ReviewPanes` returns `null` while a page read is in flight;
  state owned below that switch is destroyed and re-initialised by every page request.
- **The inventory has exactly one owner.** The inventory body, `inventoryEntry` and `byteNamedEntry`
  live in `SourceExplorer.tsx`, which the workspace mounts once; `SourcePane` prints where the explorer
  is and never renders a second inventory, because two renderings of the measured change set would be
  two answers to "which paths changed".
- **A listed entry opens at the generation the listing published.** `SourceExplorer` addresses the open
  row by the path the server published and forwards that inventory's own `before_code_tree_id` /
  `after_code_tree_id` into `SourceContent`; this file never resolves a tree, a path or a generation,
  and no expansion control is rendered when the inventory named no pair.
- **The open row and the display preferences are the reader's, and survive the switch.** The expanded
  path lives in the workspace state, and `layout`/`fullFile` are passed down to `SourceContent` rather
  than held beside it, so a layout switch cannot reset an expansion.
- **A collection is offered with no cursor only when it has a first page.** `PagePicker` maps
  `REVIEW_WALKABLE_COLLECTIONS`; `family_members` is reachable by continuing the roster page that
  published its cursor, and its absence from the picker narrows no part of the server contract.
- **A row whose name is bytes is listed and marked unopenable, not offered a control.**
  `byteNamedEntry` (in `SourceExplorer.tsx`) renders the exact byte form and the
  `review-byte-path-not-addressable` statement, and carries no expansion affordance, because no request
  this vocabulary can spell would address it.
- **An unresolved attribution is printed, never dropped.** `attribution` prints
  `author: unresolved reference` for an absent author, and `unresolvedList` renders each pane's own
  unresolved rows.
- **Staleness and submission are printed together and neither has a favourable member.** The stale line
  appears only for `stale`, and the submission state is `DISABLED` or `not offered`.
- **A failure never erases the last coherent comparison, and never invents an empty one.** The retained
  payload is shown, labelled, and no empty review is claimed for it; the two statements about a shown
  payload are decided in `ReviewOutcomeRegion`.
- **A comparison is never rendered under a header it was not read for.** The key is `targetKeyOf`'s, and
  both the reset inside `useReviewReadCycle` and the render-time check read it.
- **The refusal is a phase, not an error string.** `readFrom` produces it; `ReviewOutcomeRegion` renders
  it with every field the owner published.
- **The retry belongs to the state with no owner-published route.** Only a `failed` read gets one.
- **The reviewer supplies its own vertical scrollport, because the shell's is deliberately absent
  (260921-ICR-L25 round 3, register B7).** `cockpit/Cockpit.tsx` sets `MAIN` to `overflow: hidden` as
  a documented, shared decision — *"the viewport does not scroll, its panel scrolls on its own"* — so
  a panel that supplies none renders its whole height into a clipped box. Measured before this fix at
  320 px: `review-surface` held 7 620 px of content in a 706 px box, `userScrollableCount` was **0**,
  the window was exactly viewport-height, and three wheel trials moved nothing — a long guarantee was
  reachable only by the browser's programmatic focus scroll. The root now carries `height: 100%`,
  `minHeight: 0`, `minWidth: 0`, `overflowY: "auto"`, which *fills* the shell's row instead of growing
  past it. **This file does not change the shell's decision**, and the shell-level choice stays routed.
- **The complete-payload panes may shrink and wrap, and that is a layout requirement rather than a
  style choice.** Each pane is a **grid item** of the disclosure, so its automatic minimum size is
  content-based unless told otherwise; the identities printed here are single unbreakable tokens (a
  64-character comparison reference measured 539 px, a repository path 565 px) and the inherited
  `break-word` does **not** lower min-content. `pane` therefore carries `minWidth: 0` and
  `overflowWrap: "anywhere"`, and the disclosure's own track is `minmax(0, 1fr)` rather than the
  implicit `auto` — the track must be allowed to shrink below its items' min-content for the panes'
  `min-width: 0` to take effect. The header row wraps for the same reason: at 320 px it was the last
  thing past the viewport edge, one unbreakable line of identities beside two controls.
- **Boundary.** This is a presentation component. It holds no durable state, resolves no candidate and
  owns no route — and it owns no statement-side rule either, since R06 gave that rule a file of its own,
  nor the entry-expansion rule, which R03 gave to `SourceContent.tsx`, nor the outcome states, which
  R16 gave to `ReviewOutcome.tsx`, nor the inventory, which ICR-R24@v3 gave to `SourceExplorer.tsx`.
- **Two measured limits of this mechanism, recorded as routed rather than fixed.** (1) An **in-flight**
  prop/question change can still let an earlier read settle under a newer header: if target A's request
  is still pending when the props change to B and B's read fails, A's late response still reaches
  `setRead(readFrom(result))` and its payload renders under B's header. The retained-key guard protects
  the `retained` path, not the read phase. It is **pre-existing** — measured identically at HEAD and on
  the round-1 bytes, so it is not introduced here — and it is **routed to R17 (coherent live refresh)**,
  with R24 for the interaction side. The retained-generation guarantee holds for every **settled**
  change (a delivered target change, a same-target selector change, an A→B→A round trip, and a retry).
  (2) The **browser-class A01/A13 journeys** — a served dashboard bundle, a real browser, and the
  retry-vs-target race — are **not verified by this leaf** and belong to **R25 with R24/R17**.

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

Every claim on this card is checkable in the shipped candidate: the header's own statement of the
display-only boundary and of the two reused renderers, the target the component takes, the one load
path, the three panes and their sub-components, the openable inventory row and the entry it mounts,
the byte-form row's explicit non-addressability, the refusal block, the two delegations, and the
cockpit and change-set files that mount it. Every row was re-derived against this candidate — this
leaf's additions moved every construct below pane 1 — and every anchor in a row occurs inside the
range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement that the surface is display-only, produces no conclusion of its own, and reuses two renderers fed by other owners: `DiffPane` for both operands when both sides recorded one and for the available operand beside a named absence when one side did not, and the Source pane's entry expansion, whose rule `SourceContent` owns.** | `DiffPane`; `KnowledgeStatements`; `SourceContent` | dashboard/src/panels/review/ReviewSurface.tsx:1-9 |
| **The whole input: a task context and one recorded subject, plus the back callback, with no path.** | `ReviewTarget`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:60-74; dashboard/src/panels/review/ReviewSurface.tsx:819-910 |
| The takeover class shared with the change-set viewer, and where it is applied. | `TAKEOVER` |dashboard/src/panels/review/ReviewSurface.tsx:76-77; dashboard/src/panels/review/ReviewSurface.tsx:757-757|
| **The one load path: the read cycle's hook supplies the read, the retained comparison and the refresh; the phases are rendered as themselves and there is no submit handler anywhere.** | `useReviewReadCycle`; `intentReview` | dashboard/src/panels/review/ReviewSurface.tsx:55-55; dashboard/src/panels/review/ReviewSurface.tsx:884-884; dashboard/src/data/review.ts:533-549 |
| The four helpers that keep the pane bodies readable, including the attribution that prints an unresolved author rather than an anonymous one. | `pane`; `muted`; `attribution`; `unresolvedList` | dashboard/src/panels/review/ReviewSurface.tsx:89-89; dashboard/src/panels/review/ReviewSurface.tsx:99-99; dashboard/src/panels/review/ReviewSurface.tsx:105-105; dashboard/src/panels/review/ReviewSurface.tsx:165-165 |
| **The fifth helper this leaf added: one field value as `(absent)`, `(recorded empty)` or itself, so neither absence nor a recorded empty is printed as a blank.** | `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:182-182; dashboard/src/panels/review/ReviewSurface.tsx:256-256 |
| The one assessment renderer both panes reuse, so the two cannot disagree about how a recorded assessment looks. | `assessmentBlock` | dashboard/src/panels/review/ReviewSurface.tsx:185-185; dashboard/src/panels/review/ReviewSurface.tsx:304-304; dashboard/src/panels/review/ReviewSurface.tsx:411-411 |
| The authored record and the detection fact rendered under their own headings in their own lists. | `authoredEffect`; `signalBlock`; `AuthoredRecords` | dashboard/src/panels/review/ReviewSurface.tsx:165-311 |
| The mechanical half of pane 1: the conditions each side recorded, the retained revisions per side, and every field transition through `fieldValue`. | `KnowledgeFacts`; `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:171-251; dashboard/src/panels/review/ReviewSurface.tsx:113-113; dashboard/src/panels/review/ReviewSurface.tsx:221-221; dashboard/src/panels/review/ReviewSurface.tsx:106-106; dashboard/src/panels/review/ReviewSurface.tsx:177-177 |
| **Pane 1, which delegates its statement area and keeps the comparison line, the mechanical facts, the authored records and the unassessed state.** | `KnowledgePane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewSurface.tsx:275-300 |
| **The openable inventory row — the explorer's now, not this file's: the path published to this client rendered as a button carrying `data-path` and `aria-expanded`, its status and renderability beside it, and `SourceContent` mounted beneath it at the two tree ids the inventory named.** | `inventoryEntry`; `review-inventory-open`; `SourceContent` | dashboard/src/panels/review/SourceExplorer.tsx:78-129; dashboard/src/panels/review/SourceExplorer.tsx:99-109; dashboard/src/panels/review/SourceExplorer.tsx:116-125 |
| **The byte-form row — the explorer's now: listed by its exact byte form with its status and reason, carrying no expansion control, and stating in words that no expansion request can name it.** | `byteNamedEntry`; `review-byte-path-not-addressable` | dashboard/src/panels/review/SourceExplorer.tsx:137-149; dashboard/src/panels/review/SourceExplorer.tsx:227-229 |
| **The inventory in all three states and never as an empty list, and the one state it holds — which row is open, and the generation pair derived from the inventory's own published tree ids — are the explorer's now: this file mounts the explorer and carries no inventory body and no open-path state of its own.** | `InventoryRows`; `SourceExplorer` |dashboard/src/panels/review/SourceExplorer.tsx:194-232; dashboard/src/panels/review/SourceExplorer.tsx:234-315|
| **Pane 2: the explorer pointer first — it names where the one inventory is instead of rendering a second — then the locations with an unclassified role kept as such, the remaining counts where an unmeasured quantity states its reason, and the unattributed paths and expansion.** | `SourcePane` |dashboard/src/panels/review/ReviewSurface.tsx:302-352|
| Pane 3: the two independent absence states, the observations, and the source-inspection sentence. | `EvidencePane` | dashboard/src/panels/review/ReviewSurface.tsx:354-407; dashboard/src/panels/review/ReviewSurface.tsx:760-760 |
| **The staleness and submission block, where neither state has a favourable member.** | `SubmissionBlock` | dashboard/src/panels/review/ReviewSurface.tsx:409-438; dashboard/src/panels/review/ReviewSurface.tsx:740-740 |
| The typed refusal rendered by the one shared block, which this leaf moved to the outcome owner with the rest of the non-payload states. | `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:108-171 |
| **The statement area's owner: the four branches decided by declared state, with the state lines, the one-sided diff and the no-diff-claimed content path.** | `KnowledgeStatements`; `unavailable`; `sideLine` | dashboard/src/panels/review/KnowledgeStatements.tsx:32-44; dashboard/src/panels/review/KnowledgeStatements.tsx:93-118 |
| **The entry-expansion renderer an openable row mounts — the explorer's row now: the state-decided branches, the reused two-sided diff, the bounded-prefix note and the typed refusal.** | `SourceContent`; `Sides`; `boundedNote`; `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:189-265; dashboard/src/panels/review/SourceContent.tsx:85-129; dashboard/src/panels/review/SourceContent.tsx:131-141; dashboard/src/panels/review/SourceContent.tsx:143-155 |
| The reused diff renderer itself, imported by the statement area from the change-set route rather than re-implemented. | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-48; dashboard/src/panels/review/KnowledgeStatements.tsx:29-29 |
| The client this component reads through, and the expansion read its rows make. | `intentReview`; `reviewSourceContent` | dashboard/src/data/review.ts:533-549; dashboard/src/data/review.ts:717-735 |
| **The cockpit takeover that mounts this component under its own view, and the target variant that selects it.** | `ChangeSetTakeover`; `review` | dashboard/src/cockpit/Cockpit.tsx:561-591; dashboard/src/panels/changeset/ChangeSetViewer.tsx:38-44 |
| **The reviewer entry that opens this target, added beside the working and committed actions: it reads its subject from the server's own resolution rather than from a caller-supplied prop.** | `selector_id`; `useReviewCatalogue` | dashboard/src/panels/detail-panel/changeSetBar.tsx:384-565 |

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
| **The pane helper's two load-bearing declarations, and the comment that states why each one is required rather than cosmetic.** | `pane`; "minWidth: 0"; "overflowWrap"; `data-pane` | dashboard/src/panels/review/ReviewSurface.tsx:8-97 |
| **The disclosure track that lets the panes shrink: `minmax(0, 1fr)`, not the implicit `auto`.** | `TAKEOVER`; `gridTemplateColumns`; `review-details` | dashboard/src/panels/review/ReviewSurface.tsx:771-786 |
| **The header row that wraps, and the subject span's own break opportunity and zero minimum.** | `ReviewHeader`; `flexWrap`; `review-subject` | dashboard/src/panels/review/ReviewSurface.tsx:797-857 |
| **The reviewer's own vertical scrollport on its own root, with the shell's decision left where it belongs.** | `review-surface`; "overflowY: auto"; "height: 100%"; "minHeight: 0" | dashboard/src/panels/review/ReviewSurface.tsx:903-920 |
| The fixture builder and the mount this pin relies on, cited from their own declarations. | `payload` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:36-36 |
| The shell decision this file does **not** change, and which stays routed to the cockpit owner: the comment that states it sits on the declaration itself. | "the viewport does not scroll"; `overflow: "hidden"` | dashboard/src/cockpit/Cockpit.tsx:323-323 |

## Update History
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
