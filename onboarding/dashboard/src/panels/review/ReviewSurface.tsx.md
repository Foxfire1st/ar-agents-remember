# dashboard/src/panels/review/ReviewSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:05+02:00 |
| lastVerifiedCommitHash |  `4a0442d62eb842661a3dd04686c376d0f0dbc61f`|
| lastVerifiedCommitDate |  2026-09-20T14:22:54+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Intent Reviewer surface: three panes over one comparison, and the refusal states they render. The
header states the boundary in one line — **the surface is display-only** — and then the three things
that follow from it: it renders records other owners store, it carries every attribution it was given,
and it produces no conclusion of its own, so there is no summary, no severity, no score and no control
that writes anything. The one renderer it reuses is `DiffPane`, fed the two recorded statements the
comparison published and **only when both sides are `present`**.

This is a new route under `panels/`, mounted through the cockpit's change-set takeover rather than
through a route of its own: `ChangeSetTarget` carries an optional `review` variant and `Cockpit.tsx`'s
`ChangeSetTakeover` renders this component instead of `ChangeSetViewer` when it is present, under
`data-view="intent-review"`.

## Code Commentary

### Logic

**`ReviewTarget` is the component's whole input, plus a back callback.** It carries `repo`, `master`,
`leaf`, `selectorKind` and `selectorId` — a task context and one recorded subject, and nothing else —
and `ReviewSurface` takes `ReviewTarget & { onBack: () => void }`. No path is accepted, so the
component cannot name a dataset; the server resolves the candidate from the task context the target
carries.

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

**Four small helpers keep the pane bodies readable.** `pane(title, children)` wraps a section with
`data-pane={title}`; `muted(text, testid?)` renders the secondary-line paragraph the panes use for a
stated absence; `attribution(author?, inputs)` renders `author: unresolved reference` when the author
is `undefined` and `author: <name>` otherwise, appending the examined inputs when there are any; and
`unresolvedList(entries)` renders the `review-unresolved` list, or `null` when there is nothing
unresolved. `sideState(side, testid)` renders **only** the non-`present` case, with
`data-side-state={side.state}` and the state's own `detail` — so a missing side is printed as its named
state and never as an empty diff.

**`DiffPane` is fed the two statements only when both sides are `present`.** `KnowledgePane` computes
`bothPresent` and branches: when both sides are `present` it renders `DiffPane` with
`before={knowledge.before_statement.text ?? ""}`, `after=...`, the side's `language`, `mode="split"`
and `collapse={false}`; otherwise it renders the two `sideState` paragraphs. A binary or unresolved
operand therefore never reaches the diff renderer, and the `?? ""` can only ever apply to a `present`
side — which the model guarantees carries text.

**The three panes are three components, each reading only its own pane off the payload.**
`KnowledgePane` prints the comparison reference and policy, the diff or the two side states,
`KnowledgeFacts`, `AuthoredRecords`, the assessments or the `review-unassessed` line, and the pane's
own unresolved list. `SourcePane` prints the locations with their role
(`unclassified (no role recorded)` when the role is absent), a `before-only` marker, the change state
and the resolution, then the `review-remaining` line that renders `name: not measured (reason)` when
`value` is `undefined` and `name: <value>` otherwise, then the unattributed paths and the expansion
reference with its command, or the stated absence of an expansion. `EvidencePane` branches on
`evidence_state`: `recorded` renders the `review-evidence` link list and the `review-observations`
list, otherwise it prints "No recorded evidence links", then states that source-based inspection
remains available when `source_inspection_available`, then the assessments or the `review-unassessed`
line, then the pane's unresolved list.

**`KnowledgeFacts` and `AuthoredRecords` are extracted so pane 1 reads as a composition.**
`KnowledgeFacts` renders the essential conditions each side recorded (only when at least one side has
any), the retained-revision groups as `side:record_id=count` joined by `·` or `none selected`, and
every field transition as `field: before → after` with `(absent)` for a missing value.
`AuthoredRecords` renders the authored effects and the detection signals **under their own headings,
in their own lists** — "Authored effects and preservation claims" and "Detection signals (facts, not
findings)" — which is the display half of the vocabulary's rule that a signal is never rendered in the
shape of a finding. Each authored effect prints its `record_kind`, its label, its id, its rationale
and its attribution; each signal prints its condition, input set, id, extractor and policy versions,
its relationship paths and its scope limitations, and nothing else.

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
payload's comparison reference and `data-review-target` from the three task identifiers, so the
subject and the comparison a rendering belongs to are on the element rather than inferred from its
text.

**The takeover class is shared with the change-set viewer.** `TAKEOVER = "changeset-viewer"` is applied
to the pane grid, so the surface inherits the takeover layout rather than declaring a second one, while
the component is mounted under its own `data-view="intent-review"` on the cockpit side.

### Conventions

The component imports its types and its one function from `../../data/review` and its one reused
renderer from `../changeset/DiffPane`; it declares no client of its own. Inline `style` objects are
used throughout, matching the cockpit panels' idiom, and every list item carries a stable `key` derived
from the record's own identifiers (`assessment_id`, `record_kind:record_id`, `signal_id`,
`item_id:field`, `claim_id:path`, `claim_id`). Data attributes carry the machine-readable facts —
`data-pane`, `data-side-state`, `data-binding`, `data-change-state`, `data-submission-state`,
`data-testid` — so the surface's behaviour is inspectable without reading its text. Sub-components are
plain functions taking the payload or the pane they render; none of them holds state.

### Invariants And Boundaries

- **Display-only.** The file contains no POST, no form and no submit handler; the one request is a
  read, and the submission block prints the authority's path rather than offering a control.
- **No conclusion is rendered.** There is no summary, severity, score, verdict or approval anywhere in
  the tree; the surface prints the records and the attributions it was given.
- **A missing side is printed as its state.** `sideState` renders only the non-`present` case, and
  `DiffPane` is fed only when both sides are `present`.
- **The diff renderer is reused, not re-implemented.** `KnowledgePane` imports `DiffPane` from the
  change-set route rather than declaring a second differ.
- **An unresolved attribution is printed, never dropped.** `attribution` prints
  `author: unresolved reference` for an absent author, and `unresolvedList` renders each pane's own
  unresolved rows.
- **Staleness and submission are printed together and neither has a favourable member.** The stale line
  appears only for `stale`, and the submission state is `DISABLED` or `not offered`.
- **The refusal is a state, not an error string.** `RefusalBlock` prints the typed code, detail, next
  action and offending input.
- **Boundary.** This is a presentation component. It holds no durable state, resolves no candidate and
  owns no route.

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
sub-components, the refusal block, and the cockpit and change-set files that mount it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The header's own statement that the surface is display-only, produces no conclusion of its own, and reuses `DiffPane` only when both sides are present. | `DiffPane` | dashboard/src/panels/review/ReviewSurface.tsx:1-6; dashboard/src/panels/review/ReviewSurface.tsx:182-195 |
| **The whole input: a task context and one recorded subject, plus the back callback, with no path.** | `ReviewTarget`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:24-30; dashboard/src/panels/review/ReviewSurface.tsx:339-346 |
| The takeover class shared with the change-set viewer. | `TAKEOVER` | dashboard/src/panels/review/ReviewSurface.tsx:32-32; dashboard/src/panels/review/ReviewSurface.tsx:394-398 |
| **The one load path: three separate outcome states, a refusal and a payload that can never be on screen together, and no submit handler anywhere.** | `load`; `intentReview` | dashboard/src/panels/review/ReviewSurface.tsx:347-371 |
| The four helpers that keep the pane bodies readable, including the attribution that prints an unresolved author rather than an anonymous one. | `pane`; `muted`; `attribution`; `unresolvedList` | dashboard/src/panels/review/ReviewSurface.tsx:34-62 |
| **The helper that prints a missing side as its own named state and never as an empty diff.** | `sideState` | dashboard/src/panels/review/ReviewSurface.tsx:64-69 |
| The one assessment renderer both panes reuse, so the two cannot disagree about how a recorded assessment looks. | `assessmentBlock` | dashboard/src/panels/review/ReviewSurface.tsx:71-82 |
| The authored record and the detection fact rendered under their own headings in their own lists. | `authoredEffect`; `signalBlock`; `AuthoredRecords` | dashboard/src/panels/review/ReviewSurface.tsx:84-115; dashboard/src/panels/review/ReviewSurface.tsx:147-170 |
| The mechanical half of pane 1: the conditions each side recorded, the retained revisions per side, and every field transition with `(absent)` for a missing value. | `KnowledgeFacts` | dashboard/src/panels/review/ReviewSurface.tsx:117-145 |
| **Pane 1, with the both-sides-present gate on the diff renderer.** | `KnowledgePane` | dashboard/src/panels/review/ReviewSurface.tsx:172-208 |
| Pane 2: the locations with an unclassified role kept as such, the remaining counts where an unmeasured quantity states its reason, and the unattributed paths and expansion. | `SourcePane` | dashboard/src/panels/review/ReviewSurface.tsx:210-250 |
| Pane 3: the two independent absence states, the observations, and the source-inspection sentence. | `EvidencePane` | dashboard/src/panels/review/ReviewSurface.tsx:252-301 |
| **The staleness and submission block, where neither state has a favourable member.** | `SubmissionBlock` | dashboard/src/panels/review/ReviewSurface.tsx:303-323 |
| The typed refusal rendered beside the error line rather than instead of it. | `RefusalBlock` | dashboard/src/panels/review/ReviewSurface.tsx:325-337 |
| The reused diff renderer itself, imported from the change-set route rather than re-implemented. | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-48 |
| The client this component reads through. | `intentReview` | dashboard/src/data/review.ts:215-225 |
| **The cockpit takeover that mounts this component under its own view, and the target variant that selects it.** | `ChangeSetTakeover`; `review` | dashboard/src/cockpit/Cockpit.tsx:561-590; dashboard/src/panels/changeset/ChangeSetViewer.tsx:41-41 |
| **The reviewer entry that opens this target, added beside the working and committed actions: it now reads its subject from the server's own resolution rather than from a caller-supplied prop.** | `subject.selector_id`; `useReviewSubject` | dashboard/src/panels/detail-panel/changeSetBar.tsx:148-154; dashboard/src/panels/detail-panel/changeSetBar.tsx:71-96 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's three-pane display. It records that the surface is **display-only** — no POST, no form, no submit handler, and a submission block that prints the existing authority's path rather than offering a control — and the five renderings a reader must not flatten: a missing side is printed as its own named state (so `DiffPane` is fed only when both sides are `present`), an unresolved attribution is printed rather than dropped, the remaining counts print `not measured (reason)` rather than a zero, the authored records and the mechanical signals sit under their own headings in their own lists, and the stale/submission block prints neither state as favourable. It also records that the component is mounted through the cockpit's change-set takeover under `data-view="intent-review"` rather than through a route of its own. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
