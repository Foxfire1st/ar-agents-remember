# dashboard/src/panels/review/ReviewSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-22T07:05:34+02:00 |
| lastVerifiedCommitHash |  `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`|
| lastVerifiedCommitDate |  2026-09-23T00:33:19+02:00|
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
with `Inventory` and prints the locations with their role (`unclassified (no role recorded)` when the
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
to the pane grid, so the surface inherits the takeover layout rather than declaring a second one, while
the component is mounted under its own `data-view="intent-review"` on the cockpit side.

**The surface renders a review that compared nothing, and it renders an inventory whose entries open.**
The header prints `whole task (no subject selected)` when no selector was named. `KnowledgePane` prints
the comparison identity when there is one and `no knowledge comparison was made · <selection_detail>`
when there is not, under the `review-selection` test id. `Inventory` renders all three inventory states
(measured, partial, unavailable) and never as an empty list, printing `listed_total`, the `+ N by byte
form` count, the server's own `detail` and the reproducing `command` with both tree ids;
`inventoryEntry` prints one changed path exactly as published, with its status and its renderability
beside it; and `byteNamedEntry` prints a changed path whose name this surface cannot carry as text by
its exact byte form, with its status and the stated reason.

**A listed entry is also the way into its own content, and that is one state on `Inventory`.** `Inventory`
holds `const [open, setOpen] = useState<string | null>(null)` — which row is open, addressed by the
path the server published — and derives the `generation` object from the inventory's own
`before_code_tree_id`/`after_code_tree_id`. `inventoryEntry` takes that state and the generation pair
and renders the row's path as a `<button data-testid="review-inventory-open" data-path={entry.path}
aria-expanded={isOpen}>` **only when the inventory named both code trees**; the same click toggles the
row closed. The path text is still printed literally — a tab or a newline inside a name is part of the
address, and the address is also the button's `data-path`, which is how a case or a reader can find the
row it means. When a row is open the same function mounts `SourceContent` beneath it with the task
context (`repo`/`master`/`leaf`) and the two published tree ids, so the content a reader opens is the
generation the listing named.

**The byte-form row is the one row that must not look openable, and it says so.** `byteNamedEntry` has
no control at all and carries `data-testid="review-byte-path-not-addressable"`, which states that the
row's content cannot be opened through this surface because its name is carried as bytes for
identification and no expansion request can name it. A reader can still act on the bytes beside it with
Git directly; what the pane must not do is imply that clicking it would open anything. That is the
boundary ICR-R03 inherits from the text-only vocabulary rather than a decision taken here.

**The pane grid forwards the task context, so the expansion target is the surface's own.** `SourcePane`
takes `repo`/`master`/`leaf` as well as the payload and hands them to `Inventory`, and `ReviewSurface`
passes its own three identifiers into `SourcePane` — the same three the root's `data-review-target`
stamps. Nothing in this file resolves a tree, a path or a generation: the ids it forwards are the ones
the server published to this client.

### Conventions

The component imports its types and its three functions from `../../data/review` (the public entry that
re-exports the transport surface), its statement renderer from `./KnowledgeStatements`, its
entry-expansion renderer from `./SourceContent`, and the read phases plus the region from
`./ReviewOutcome` — which is what makes one module the owner of the outcome states. It declares no
client of its own and **no longer imports `DiffPane`** — the diff engine is reached through
`KnowledgeStatements`, which is what keeps one rule in one place. `Inventory` is the one sub-component
that holds state (which inventory row is open), and it is where the expansion's generation pair is
derived from the inventory's own published tree ids. Inline `style` objects are used throughout,
matching the cockpit panels' idiom, and
every list item carries a stable `key` derived from the record's own identifiers (`assessment_id`,
`record_kind:record_id`, `signal_id`, `item_id:field`, `claim_id:path`, `claim_id`). Data attributes
carry the machine-readable facts — `data-pane`, `data-binding`, `data-change-state`,
`data-submission-state`, `data-testid` — so the surface's behaviour is inspectable without reading its
text. Sub-components are plain functions taking the payload or the pane they render; none of them holds
state. `data-side-state` **no longer appears in this file**: it moved with the statement area into
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
- **A listed entry opens at the generation the listing published.** `Inventory` addresses the open row
  by the path the server published and forwards that inventory's own `before_code_tree_id` /
  `after_code_tree_id` into `SourceContent`; this file never resolves a tree, a path or a generation,
  and it renders no expansion control when the inventory named no pair.
- **A row whose name is bytes is listed and marked unopenable, not offered a control.**
  `byteNamedEntry` renders the exact byte form and the `review-byte-path-not-addressable` statement,
  and carries no expansion affordance, because no request this vocabulary can spell would address it.
- **An unresolved attribution is printed, never dropped.** `attribution` prints
  `author: unresolved reference` for an absent author, and `unresolvedList` renders each pane's own
  unresolved rows.
- **Staleness and submission are printed together and neither has a favourable member.** The stale line
  appears only for `stale`, and the submission state is `DISABLED` or `not offered`.
- **A failure never erases the last coherent comparison, and never invents an empty one.** The retained
  payload is shown, labelled, and no empty review is claimed for it; the two statements about a shown
  payload are decided in `ReviewOutcomeRegion`.
- **A comparison is never rendered under a header it was not read for.** The key is `targetKeyOf`'s, and
  both the reset in `load` and the render-time check read it.
- **The refusal is a phase, not an error string.** `readFrom` produces it; `ReviewOutcomeRegion` renders
  it with every field the owner published.
- **The retry belongs to the state with no owner-published route.** Only a `failed` read gets one.
- **Boundary.** This is a presentation component. It holds no durable state, resolves no candidate and
  owns no route — and it owns no statement-side rule either, since R06 gave that rule a file of its own,
  nor the entry-expansion rule, which R03 gave to `SourceContent.tsx`, nor the outcome states, which
  R16 gave to `ReviewOutcome.tsx`.
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
| **The whole input: a task context and one recorded subject, plus the back callback, with no path.** | `ReviewTarget`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:65-65; dashboard/src/panels/review/ReviewSurface.tsx:784-784; dashboard/src/panels/review/ReviewSurface.tsx:58-58; dashboard/src/panels/review/ReviewSurface.tsx:551-551 |
| The takeover class shared with the change-set viewer, and where it is applied. | `TAKEOVER` | dashboard/src/panels/review/ReviewSurface.tsx:76-76; dashboard/src/panels/review/ReviewSurface.tsx:540-540; dashboard/src/panels/review/ReviewSurface.tsx:69-69; dashboard/src/panels/review/ReviewSurface.tsx:623-623 |
| **The one load path: three separate outcome states, a refusal and a payload that can never be on screen together, and no submit handler anywhere.** | `load`; `intentReview` | dashboard/src/panels/review/ReviewSurface.tsx:50-50; dashboard/src/data/review.ts:328-342; dashboard/src/panels/review/ReviewSurface.tsx:45-45; dashboard/src/panels/review/ReviewSurface.tsx:519-519 |
| The four helpers that keep the pane bodies readable, including the attribution that prints an unresolved author rather than an anonymous one. | `pane`; `muted`; `attribution`; `unresolvedList` | dashboard/src/panels/review/ReviewSurface.tsx:96-96; dashboard/src/panels/review/ReviewSurface.tsx:78-78; dashboard/src/panels/review/ReviewSurface.tsx:79-79; dashboard/src/panels/review/ReviewSurface.tsx:113-113; dashboard/src/panels/review/ReviewSurface.tsx:114-114; dashboard/src/panels/review/ReviewSurface.tsx:128-128; dashboard/src/panels/review/ReviewSurface.tsx:140-140; dashboard/src/panels/review/ReviewSurface.tsx:144-144; dashboard/src/panels/review/ReviewSurface.tsx:147-147; dashboard/src/panels/review/ReviewSurface.tsx:163-163; dashboard/src/panels/review/ReviewSurface.tsx:196-196; dashboard/src/panels/review/ReviewSurface.tsx:204-204; dashboard/src/panels/review/ReviewSurface.tsx:215-215; dashboard/src/panels/review/ReviewSurface.tsx:228-228; dashboard/src/panels/review/ReviewSurface.tsx:275-275; dashboard/src/panels/review/ReviewSurface.tsx:303-303; dashboard/src/panels/review/ReviewSurface.tsx:304-304; dashboard/src/panels/review/ReviewSurface.tsx:355-355; dashboard/src/panels/review/ReviewSurface.tsx:392-392; dashboard/src/panels/review/ReviewSurface.tsx:411-411; dashboard/src/panels/review/ReviewSurface.tsx:416-416; dashboard/src/panels/review/ReviewSurface.tsx:445-445; dashboard/src/panels/review/ReviewSurface.tsx:457-457; dashboard/src/panels/review/ReviewSurface.tsx:460-460; dashboard/src/panels/review/ReviewSurface.tsx:467-467; dashboard/src/panels/review/ReviewSurface.tsx:483-483; dashboard/src/panels/review/ReviewSurface.tsx:487-487; dashboard/src/panels/review/ReviewSurface.tsx:488-488; dashboard/src/panels/review/ReviewSurface.tsx:608-608; dashboard/src/panels/review/ReviewSurface.tsx:3-3; dashboard/src/panels/review/ReviewSurface.tsx:84-84; dashboard/src/panels/review/ReviewSurface.tsx:115-115; dashboard/src/panels/review/ReviewSurface.tsx:129-129; dashboard/src/panels/review/ReviewSurface.tsx:407-407; dashboard/src/panels/review/ReviewSurface.tsx:89-89; dashboard/src/panels/review/ReviewSurface.tsx:131-131; dashboard/src/panels/review/ReviewSurface.tsx:230-230; dashboard/src/panels/review/ReviewSurface.tsx:418-418; dashboard/src/panels/review/ReviewSurface.tsx:437-437; dashboard/src/panels/review/ReviewSurface.tsx:469-469 |
| **The fifth helper this leaf added: one field value as `(absent)`, `(recorded empty)` or itself, so neither absence nor a recorded empty is printed as a blank.** | `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:113-113; dashboard/src/panels/review/ReviewSurface.tsx:106-106; dashboard/src/panels/review/ReviewSurface.tsx:177-177 |
| The one assessment renderer both panes reuse, so the two cannot disagree about how a recorded assessment looks. | `assessmentBlock` | dashboard/src/panels/review/ReviewSurface.tsx:116-116; dashboard/src/panels/review/ReviewSurface.tsx:109-109; dashboard/src/panels/review/ReviewSurface.tsx:225-225; dashboard/src/panels/review/ReviewSurface.tsx:464-464 |
| The authored record and the detection fact rendered under their own headings in their own lists. | `authoredEffect`; `signalBlock`; `AuthoredRecords` | dashboard/src/panels/review/ReviewSurface.tsx:129-129; dashboard/src/panels/review/ReviewSurface.tsx:143-143; dashboard/src/panels/review/ReviewSurface.tsx:194-194; dashboard/src/panels/review/ReviewSurface.tsx:222-222; dashboard/src/panels/review/ReviewSurface.tsx:136-136; dashboard/src/panels/review/ReviewSurface.tsx:201-201 |
| The mechanical half of pane 1: the conditions each side recorded, the retained revisions per side, and every field transition through `fieldValue`. | `KnowledgeFacts`; `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:165-165; dashboard/src/panels/review/ReviewSurface.tsx:113-113; dashboard/src/panels/review/ReviewSurface.tsx:221-221; dashboard/src/panels/review/ReviewSurface.tsx:106-106; dashboard/src/panels/review/ReviewSurface.tsx:177-177 |
| **Pane 1, which delegates its statement area and keeps the comparison line, the mechanical facts, the authored records and the unassessed state.** | `KnowledgePane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewSurface.tsx:217-217; dashboard/src/panels/review/ReviewSurface.tsx:7-7; dashboard/src/panels/review/ReviewSurface.tsx:48-48; dashboard/src/panels/review/ReviewSurface.tsx:220-220; dashboard/src/panels/review/ReviewSurface.tsx:210-210; dashboard/src/panels/review/ReviewSurface.tsx:624-624 |
| **The openable inventory row: the path published to this client rendered as a button carrying `data-path` and `aria-expanded`, its status and renderability beside it, and `SourceContent` mounted beneath it at the two tree ids the inventory named.** | `inventoryEntry`; `review-inventory-open`; `SourceContent` | dashboard/src/panels/review/ReviewSurface.tsx:214-260; dashboard/src/panels/review/ReviewSurface.tsx:8-8; dashboard/src/panels/review/ReviewSurface.tsx:49-49; dashboard/src/panels/review/ReviewSurface.tsx:277-277 |
| **The byte-form row: listed by its exact byte form with its status and reason, carrying no expansion control, and stating in words that no expansion request can name it.** | `byteNamedEntry`; `review-byte-path-not-addressable` | dashboard/src/panels/review/ReviewSurface.tsx:305-305; dashboard/src/panels/review/ReviewSurface.tsx:298-298; dashboard/src/panels/review/ReviewSurface.tsx:352-352 |
| **The inventory in all three states and never as an empty list, and the one state this leaf added to it — which row is open, and the generation pair derived from the inventory's own published tree ids.** | `Inventory`; `useState` | dashboard/src/panels/review/ReviewSurface.tsx:28-28 |
| **Pane 2: the inventory first, then the locations with an unclassified role kept as such, the remaining counts where an unmeasured quantity states its reason, the unattributed paths and expansion — and the task context it forwards into the inventory so an opened row reads at the surface's own target.** | `SourcePane` | dashboard/src/panels/review/ReviewSurface.tsx:337-393 |
| Pane 3: the two independent absence states, the observations, and the source-inspection sentence. | `EvidencePane` | dashboard/src/panels/review/ReviewSurface.tsx:395-444 |
| **The staleness and submission block, where neither state has a favourable member.** | `SubmissionBlock` | dashboard/src/panels/review/ReviewSurface.tsx:481-481; dashboard/src/panels/review/ReviewSurface.tsx:474-474; dashboard/src/panels/review/ReviewSurface.tsx:622-622 |
| The typed refusal rendered by the one shared block, which this leaf moved to the outcome owner with the rest of the non-payload states. | `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:108-171 |
| **The statement area's owner: the four branches decided by declared state, with the state lines, the one-sided diff and the no-diff-claimed content path.** | `KnowledgeStatements`; `unavailable`; `sideLine` | dashboard/src/panels/review/KnowledgeStatements.tsx:32-44; dashboard/src/panels/review/KnowledgeStatements.tsx:93-118 |
| **The entry-expansion renderer this file mounts from a row: the state-decided branches, the reused two-sided diff, the bounded-prefix note and the typed refusal.** | `SourceContent`; `Sides`; `boundedNote`; `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:76-112; dashboard/src/panels/review/SourceContent.tsx:114-124; dashboard/src/panels/review/SourceContent.tsx:126-138; dashboard/src/panels/review/SourceContent.tsx:164-222 |
| The reused diff renderer itself, imported by the statement area from the change-set route rather than re-implemented. | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-48; dashboard/src/panels/review/KnowledgeStatements.tsx:29-29 |
| The client this component reads through, and the expansion read its rows make. | `intentReview`; `reviewSourceContent` | dashboard/src/data/review.ts:403-403; dashboard/src/data/review.ts:547-547
| **The cockpit takeover that mounts this component under its own view, and the target variant that selects it.** | `ChangeSetTakeover`; `review` | dashboard/src/cockpit/Cockpit.tsx:561-591; dashboard/src/panels/changeset/ChangeSetViewer.tsx:38-44 |
| **The reviewer entry that opens this target, added beside the working and committed actions: it reads its subject from the server's own resolution rather than from a caller-supplied prop.** | `subject.selector_id`; `useReviewCatalogue` | dashboard/src/panels/detail-panel/changeSetBar.tsx:29-170; dashboard/src/panels/detail-panel/changeSetBar.tsx:122-187 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
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

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the page control, and the refusal it renders.** `PageControls`, `PagePicker`, `PageActions`,
`PageBoundsLine` and `PageRefusalBlock` are new, and the page is now part of the read's target key, so a
page change is its own read. Two facts are load-bearing: the action sends the cursor the server
published rather than the one the client stands on, and no next action is offered without a published
cursor. Every row on this card that cited this component by line was re-derived against this candidate,
because this leaf moved them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.

