# dashboard/src/panels/review/ReviewSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-21T17:30:00+02:00 |
| lastVerifiedCommitHash |  `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`|
| lastVerifiedCommitDate |  2026-09-21T18:13:19+02:00|
| reviewedWorkingCandidate | candidate `ar/260921-icr-l6`, uncommitted; base `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` |
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Intent Reviewer surface: three panes over one comparison, and the refusal states they render. The
header states the boundary in one line — **the surface is display-only** — and then the three things
that follow from it: it renders records other owners store, it carries every attribution it was given,
and it produces no conclusion of its own, so there is no summary, no severity, no score and no control
that writes anything. The one renderer it reuses is `DiffPane`, fed the statements the comparison
published: **both operands when both sides recorded one, and the available operand beside the named
absence when one side did not** — that second case is ICR-R06's, and its rule lives in
`KnowledgeStatements.tsx`, which this file now delegates the whole statement area to.

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

**The load is one `useCallback` plus one `useEffect`, and three states carry the outcome.**
`payload`, `refusal` and `error` are separate `useState` values, and `load` clears the error, calls
`intentReview(repo, master, leaf, selectorKind, selectorId)`, and stores **either** a payload (clearing
the refusal) **or** the result's own refusal (clearing the payload); a thrown error clears both and
records the message. The effect depends on `load`, whose dependency array is the five target fields,
so a target change refetches and an unrelated re-render does not. There is no submit handler, no form
and no POST anywhere in the file — which is the display-only boundary expressed as the absence of a
code path.

**The component's single `useState` for `payload` holds the refetch outcome, so a refusal and a stale
payload can never be on screen together.** That is the same rule the server's `KnowledgeReviewResult`
enforces, re-stated on the client because the two arrive over one response.

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

**`RefusalBlock` renders the typed refusal rather than an error string.** It prints the code and the
detail, the next action, and the offending input when there is one. It is rendered beside the error
line rather than instead of it, because a transport failure and a typed refusal are different facts.
`ReviewSurface`'s returned tree carries `data-testid="review-surface"`, `data-comparison` from the
payload's comparison reference (optional-chained, so an absent identity is an absent attribute rather
than a crash) and `data-review-target` from the three task identifiers, so the subject and the
comparison a rendering belongs to are on the element rather than inferred from its text.

**The takeover class is shared with the change-set viewer.** `TAKEOVER = "changeset-viewer"` is applied
to the pane grid, so the surface inherits the takeover layout rather than declaring a second one, while
the component is mounted under its own `data-view="intent-review"` on the cockpit side.

**The surface renders a review that compared nothing, and it renders an inventory.** The header prints
`whole task (no subject selected)` when no selector was named. `KnowledgePane` prints the comparison
identity when there is one and `no knowledge comparison was made · <selection_detail>` when there is
not, under the `review-selection` test id. `Inventory` renders all three inventory states (measured,
partial, unavailable) and never as an empty list, printing `listed_total`, the `+ N by byte form`
count, the server's own `detail` and the reproducing `command` with both tree ids; `inventoryEntry`
prints one changed path exactly as published, with its status and its renderability beside it; and
`byteNamedEntry` prints a changed path whose name this surface cannot carry as text by its exact byte
form, with its status and the stated reason.

### Conventions

The component imports its types and its one function from `../../data/review` and its one statement
renderer from `./KnowledgeStatements`; it declares no client of its own and **no longer imports
`DiffPane`** — the diff engine is reached through `KnowledgeStatements`, which is what keeps one rule
in one place. Inline `style` objects are used throughout, matching the cockpit panels' idiom, and
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
- **An unresolved attribution is printed, never dropped.** `attribution` prints
  `author: unresolved reference` for an absent author, and `unresolvedList` renders each pane's own
  unresolved rows.
- **Staleness and submission are printed together and neither has a favourable member.** The stale line
  appears only for `stale`, and the submission state is `DISABLED` or `not offered`.
- **The refusal is a state, not an error string.** `RefusalBlock` prints the typed code, detail, next
  action and offending input.
- **Boundary.** This is a presentation component. It holds no durable state, resolves no candidate and
  owns no route — and it owns no statement-side rule either, since R06 gave that rule a file of its
  own.

### Todos

None recorded. The assessment-publication control is deliberately not shipped by this increment.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the header's own statement of the
display-only boundary, the target the component takes, the one load path, the three panes and their
sub-components, the refusal block, the statement-area delegation, and the cockpit and change-set files
that mount it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement that the surface is display-only, produces no conclusion of its own, and reuses `DiffPane` for both operands when both sides recorded one and for the available operand beside a named absence when one side did not.** | `DiffPane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewSurface.tsx:1-7 |
| **The whole input: a task context and one recorded subject, plus the back callback, with no path.** | `ReviewTarget`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:27-37; dashboard/src/panels/review/ReviewSurface.tsx:395-462 |
| The takeover class shared with the change-set viewer, and where it is applied. | `TAKEOVER` | dashboard/src/panels/review/ReviewSurface.tsx:38-38; dashboard/src/panels/review/ReviewSurface.tsx:453-453 |
| **The one load path: three separate outcome states, a refusal and a payload that can never be on screen together, and no submit handler anywhere.** | `load`; `intentReview` | dashboard/src/panels/review/ReviewSurface.tsx:395-462; dashboard/src/data/review.ts:271-285 |
| The four helpers that keep the pane bodies readable, including the attribution that prints an unresolved author rather than an anonymous one. | `pane`; `muted`; `attribution`; `unresolvedList` | dashboard/src/panels/review/ReviewSurface.tsx:40-74 |
| **The fifth helper this leaf added: one field value as `(absent)`, `(recorded empty)` or itself, so neither absence nor a recorded empty is printed as a blank.** | `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:70-77 |
| The one assessment renderer both panes reuse, so the two cannot disagree about how a recorded assessment looks. | `assessmentBlock` | dashboard/src/panels/review/ReviewSurface.tsx:78-90 |
| The authored record and the detection fact rendered under their own headings in their own lists. | `authoredEffect`; `signalBlock`; `AuthoredRecords` | dashboard/src/panels/review/ReviewSurface.tsx:91-126; dashboard/src/panels/review/ReviewSurface.tsx:156-178 |
| The mechanical half of pane 1: the conditions each side recorded, the retained revisions per side, and every field transition through `fieldValue`. | `KnowledgeFacts`; `fieldValue` | dashboard/src/panels/review/ReviewSurface.tsx:127-155 |
| **Pane 1, which now delegates its statement area and keeps the comparison line, the mechanical facts, the authored records and the unassessed state.** | `KnowledgePane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewSurface.tsx:179-206 |
| Pane 2: the inventory first, then the locations with an unclassified role kept as such, the remaining counts where an unmeasured quantity states its reason, and the unattributed paths and expansion. | `SourcePane` | dashboard/src/panels/review/ReviewSurface.tsx:265-307 |
| Pane 3: the two independent absence states, the observations, and the source-inspection sentence. | `EvidencePane` | dashboard/src/panels/review/ReviewSurface.tsx:308-358 |
| **The staleness and submission block, where neither state has a favourable member.** | `SubmissionBlock` | dashboard/src/panels/review/ReviewSurface.tsx:359-380 |
| The typed refusal rendered beside the error line rather than instead of it. | `RefusalBlock` | dashboard/src/panels/review/ReviewSurface.tsx:381-394 |
| **The statement area's owner: the four branches decided by declared state, with the state lines, the one-sided diff and the no-diff-claimed content path.** | `KnowledgeStatements`; `unavailable`; `sideLine` | dashboard/src/panels/review/KnowledgeStatements.tsx:32-44; dashboard/src/panels/review/KnowledgeStatements.tsx:93-118 |
| The reused diff renderer itself, imported by the statement area from the change-set route rather than re-implemented. | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-48; dashboard/src/panels/review/KnowledgeStatements.tsx:29-29 |
| The client this component reads through. | `intentReview` | dashboard/src/data/review.ts:271-285 |
| **The cockpit takeover that mounts this component under its own view, and the target variant that selects it.** | `ChangeSetTakeover`; `review` | dashboard/src/cockpit/Cockpit.tsx:561-590; dashboard/src/panels/changeset/ChangeSetViewer.tsx:41-41 |
| **The reviewer entry that opens this target, added beside the working and committed actions: it reads its subject from the server's own resolution rather than from a caller-supplied prop.** | `subject.selector_id`; `useReviewSubject` | dashboard/src/panels/detail-panel/changeSetBar.tsx:98-170; dashboard/src/panels/detail-panel/changeSetBar.tsx:71-96 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`): **the statement area left this file, and a field row learned to tell absence from a recorded empty.** `KnowledgePane` now renders `KnowledgeStatements` where it used to hold the both-sides-present gate on `DiffPane` plus the two `sideState` paragraphs; the `sideState` helper is deleted, `DiffPane` is no longer imported here, and `data-side-state` no longer appears in this file. The new `fieldValue` helper prints `(absent)` for a value the server did not send and `(recorded empty)` for a value that is present and empty, so no field row is silently blank. Every row in the reference table was **re-derived against this candidate** — `ReviewTarget` `27-37`, `TAKEOVER` `38`, `pane`/`muted`/`attribution`/`unresolvedList` `40-74`, `fieldValue` `70-77`, `assessmentBlock` `78-90`, `authoredEffect`/`signalBlock`/`AuthoredRecords` `91-126`/`156-178`, `KnowledgeFacts` `127-155`, `KnowledgePane` `179-206`, `SourcePane` `265-307`, `EvidencePane` `308-358`, `SubmissionBlock` `359-380`, `RefusalBlock` `381-394`, `ReviewSurface` `395-463` — while the rows describing the L22/R02/L45 constructs this leaf did not touch kept their claims and moved only where the source moved. The card's stale claims were **corrected rather than carried**: the header no longer says the diff is fed "only when both sides are `present`", `sideState` is recorded as deleted, and the invariants now say the statement-side rule belongs to `KnowledgeStatements.tsx`. **Stamp accounting:** the verification pair still names production line `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9`, the last real commit whose bytes this card was verified against; nothing in this leaf is committed, so claims whose evidence this leaf's change moved are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **R02's rendering half: the inventory is displayed in all three of its states, and a review with no comparison identity renders as itself.** Added `Inventory`, `inventoryEntry` and `byteNamedEntry`; made `SourcePane` open with the inventory; made the Knowledge pane's selection line survive an absent `comparison` by naming that no comparison was made; made `ReviewTarget`'s selectors optional and the header print `whole task (no subject selected)`; and made the root's `data-comparison` optional-chained. The card's Purpose and Logic were re-pointed accordingly and every row in the reference table was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's three-pane display. It records that the surface is **display-only** — no POST, no form, no submit handler, and a submission block that prints the existing authority's path rather than offering a control — and the five renderings a reader must not flatten: a missing side is printed as its own named state (so `DiffPane` is fed only when both sides are `present`), an unresolved attribution is printed rather than dropped, the remaining counts print `not measured (reason)` rather than a zero, the authored records and the mechanical signals sit under their own headings in their own lists, and the stale/submission block prints neither state as favourable. It also records that the component is mounted through the cockpit's change-set takeover under `data-view="intent-review"` rather than through a route of its own. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
