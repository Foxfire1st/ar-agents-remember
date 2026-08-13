# dashboard/src/panels/detail-panel/DetailPanel.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/detail-panel/DetailPanel.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T08:19Z                                |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`       |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[panels/ overview](../overview.md)

## 260731-EFA-L8 Split Layout

The 1,469-line `DetailPanel.tsx` was split by responsibility into the
`dashboard/src/panels/detail-panel/` folder. `DetailPanel.tsx` is now the canonical
entry (76 lines) that composes `useDetailPanelState` from `state.ts`, the lifecycle
reader/body from `lifecycleBody.tsx`, the task-document reader from `taskReader.tsx`
and `taskDocPanels.tsx`, and the change-set bar from `changeSetBar.tsx`. Pure
selection/derivation helpers live in `model.ts`; styles live in `styles.ts`; the
former monolithic test suite is split by behavior into `changeSetBar.test.tsx`,
`gateRespond.test.tsx`, `masterSeries.test.tsx`, `promotedIdentity.test.tsx`,
`seriesNotes.test.tsx`, `taskBody.test.tsx`, and `viewedLeaf.test.tsx` (shared
fixtures in `test-utils.tsx`). The behavior is preserved; the split is the
frontend-rail size remediation (260731-EFA-L8 R4/R5).

## Purpose

The selected lifecycle's detail (the operations centre viewport): phase stepper, durable **Gate Respond
surface** for explicit approval/rejection gates, the **task reader** (the JSON task content rendered to
read in the dashboard, not the filesystem), the lifecycle → worktree → provider spine, and the token
gauge. The largest panel. The task reader's coordination-notes surface (`TaskNotes`) opens the L17
**Notes Reader** takeover through the `onOpenNotes` prop that `DetailPanel` threads from `CockpitShell`
alongside `onOpenChangeSet` (down through `TaskReader` / `MasterOverview` / `TaskContent`); the GateResponder
is durable-gates-only (no wait-loop `ask` fallback).
Slice 6g makes a task **series** navigable: a master shows its overview + a clickable sub-task index,
you drill into a slice's reader, and the back / parent-series up-links sit in the panel's **sticky
header** (so they never scroll away); task prose renders as **markdown**, and a sub-task that points at
another series jumps to it. Promoted leaf lifecycles may get their visible title from the bound
enclosure, but the readable task body is still sourced only from `analytics.taskDocuments`. A selected
series master can also render directly from `analytics.series`, including when the selected sidebar row
is the root task lifecycle id and its structured enclosure `taskId`/`taskName` identifies the
folder-keyed series. Leaf lifecycle rows never use parent `taskName` as content. Master leaf rows
display each authored leaf task document's own task id and render in the order the projection sends
them; they do not parse numeric filename prefixes or generate reader-local display counters. Creation
ordering (`createdAt`) applies on the SERIES path only — `seriesAsMasterDoc` sorts there, because
`SeriesSubTaskNode` is the only sub-task row that carries the field at all. Leaf progress
summaries in the master index and reader header use the server-projected `stepsDone`/`stepsTotal`
counters; the visible top-level step list is content, not a second progress authority. Master sub-task navigation resolves authored leaf documents from the full projected
sibling task-document pool, so leaves can stay absent from the Operations sidebar while remaining
clickable from the master. Directly opened leaf task documents, including enclosure-backed leaf
lifecycle rows, now get the same sticky parent/root task backlink as the master-drill path. Master
readers also show the server-projected `seriesTokenTotal` scalar so aggregate series cost is visible
without changing the selected lifecycle token gauge. L8 removes the obsolete task-local response box for
ask-only attention details; follow-up conversation belongs in the adjacent leaf chat, while durable gate
decision controls still render for real `lifecycle.gate` requests. L8 also marks rendered leaf task
content with `data-task-leaf-key` so highlight capture can identify text selected from the displayed leaf.

## Code Commentary

### 260707-HFX2-L13 On-Demand Reader Contract

The always-on `analytics.taskDocuments` collection is summary-only. `DetailPanel` resolves the single
document whose reader is actually visible and passes it to `useTaskDocumentBody`, which requests the
full body and caches the merged response under `docPath + bodyRevision`. Every render branch (direct
task document, series master, lifecycle-bound master/leaf, and drilled slice) substitutes the cached
node when available and otherwise keeps the bounded summary visible. L16's absent-array preservation,
revision invalidation, explicit unavailable fallback, and no-effect-retry-loop behavior now live in
that hook.

260712-TRH-L1 makes this hydration the reader's first request priority. While the hook reports
`loading`, `DetailPanel` renders the available summary plus the exact status line "Loading complete
task document…" but does not mount `TaskNotes`, document change-set counters, or enclosure-spine
change-set counters. Those lower-priority request surfaces mount after the body succeeds or fails; a
failure still shows "Full task document details are unavailable; showing the available summary."

### Logic

The series change-set entry point requests the master net counters without the
optional per-leaf breakdown because this reader only opens the net viewer; the
existing task and leaf entry behavior is unchanged.

Resolves `selectedId` through `parseTaskSelection` before choosing content. A `taskdoc:<docPath>` key
selects a concrete `TaskDocNode`, `series:<seriesId>` selects the legacy folder-keyed series surface,
and `lifecycle:<id>` selects runtime lifecycle state. Raw lifecycle/series ids are accepted only
through the shared compatibility bridge. If a selected task document has `lifecycleId`, the panel
attaches that runtime lifecycle/enclosure/provider/gate context; if it is unbound, it still renders the
JSON-primary task document. The selected document's own `kind` decides the reader: `master` uses
`MasterOverview` with sibling slice docs, while `subTask`/`light` use `TaskReader`.

For lifecycle selections, the panel resolves the matching enclosure with
`taskIdentity.findLifecycleEnclosure` and filters `analytics.taskDocuments` by the selected
`lifecycle.id`. It also looks up `analytics.series` only for explicit `series:` selection or when the
selected lifecycle is the root task identity (`lifecycle.id === enclosure.taskId` or
`enclosure.taskName`) and the served series projection is keyed by that enclosure `taskName`. This
covers the live master row without stealing leaf lifecycles whose `taskName` names the parent series.
`seriesAsMasterDoc` adapts the folder-keyed `SeriesNode` into the master overview shape and
`seriesSliceDocs` limits drill-in candidates to task documents in the same directory. It does not
exclude a master document if one is present in the supplied pool. `taskLabel` uses enclosure
identity for visible promoted-leaf titles, while `taskDocsForLifecycle` keeps the readable body limited
to actual task-document JSON for that lifecycle. With **no selection** (`!lifecycle && !selectedSeries && !selectedTaskDoc`) the panel early-returns a `Panel` `fill` holding the
shared `EmptyStateBackdrop` (slice 07b polish): a faint, effects-gated **battle-cruiser** boomerang-video
atmosphere (`/assets/sc2-battlecruiser-boomerang.mp4`, aria-hidden, absent under calm-cockpit /
reduced-motion) behind the **"Select a task to inspect its phase, gate, and tokens."** copy
(user-facing copy; the selected unit is still the `lifecycle`). The `Panel` `fill` variant gives the
backdrop the flex-column slot its `flex:1` canvas needs. The `stepper` is a `step` `cva`
(done/current/todo computed from the phase index).
Task 11/19 render `GateResponder` only when `activeLifecycle.gate` exists. That surface is the durable
decision affordance for explicit gates: the dialog shows the `GateNode.packet`, records approve/reject/
cancel through `/api/actions`, and can notify the hosted chat or operator inbox after a recorded decision.
L8 deliberately does **not** render it for `activeLifecycle.ask` alone; ask-only attention details no
longer show an in-task message box, because the adjacent leaf chat is the conversation surface. **Drill
state (`openSlug`) lives in
`DetailPanel`, not `TaskContent`**, so the
back / parent up-link sits in the `Panel` `head` slot (sticky): when a slice is open the body is its
`TaskReader` (objective/requirements/design/`StepList`/`CodeExample`/`DecisionList`/refs) and the head
shows `← {series}`; otherwise a matched `selectedSeries` renders `MasterOverview` from the
`analytics.series` master before any lifecycle-doc fallback. Without that series match, an actual
selected/bound master renders `MasterOverview` directly with sibling slice docs from
`seriesSliceDocs(allDocs, master.docPath)`. `seriesAsMasterDoc` carries `seriesTokenTotal` directly from
`Analytics.series`; `masterDocWithSeriesTokens` enriches concrete master `TaskDocNode`s by matching
`docPath` against `analytics.series`, and `MasterTokenSummary` renders the scalar `series tokens` row
when a total is present. This is deliberately broader than the selected lifecycle's
direct `docs` array and broader than the Operations sidebar rows: the master index remains the navigation
surface for authored leaf documents that are not sidebar-eligible. If no master is present,
`parentTaskLinkForDoc` asks `data/taskHierarchy.ts` whether the selected leaf document matches a
structured parent series sub-task ref; when it does, the sticky head renders an `↑ {parent}` link whose
target is the typed parent `taskdoc:` key when the parent master document is projected, otherwise the
typed `series:` fallback. The same parent-link path is used for unbound `taskdoc:` selections and active
enclosure-backed leaf lifecycles. If no master is present, `TaskContent`
renders a lone doc's
`TaskReader`, or a clickable `SliceList` for a master-less series; with no bound doc it shows the
fallback **"No task document bound to this task."** (user-facing copy; keyed off the selected
lifecycle's `lifecycleId`). `SubTaskIndex` renders rows **in the order received** — no client-side
sort — displays `${match?.id || ref.number}. ${match?.title || ref.name}` labels, and uses a separate
position counter only for stable test ids. `SliceList` still calls `orderedByCreation`, over
`TaskDocNode[]` (which does carry `createdAt`), so master-less leaf lists default to creation order.
`taskStepProgress` returns the projected `TaskDocNode.stepsDone/stepsTotal` counters;
`SubTaskIndex`, `SliceList`, and the `TaskReader` header `ProgressFill` use that authoritative summary.
`TaskReader` renders the progress fill in its head and the step rows exactly once
under **Implementation steps**; the former duplicate **Progress** step section is removed.
L8 wraps the task-reader body in `data-task-leaf-key={qualifiedLeafKey(doc)}`, giving the selection
capture helper a durable leaf identifier without changing any visible task content.
`StepList` and `CodeExample` display labels from structured id + title (`S11 — ...`, `E4 — ...`) while
leaving the underlying title fields clean. **L5 fix 1** adds the optional `onViewLeaf` prop: the panel
resolves the leaf it is actually **showing** with the `displayedLeafDoc(...)` helper — which mirrors the
render branches exactly (a drilled sub-task via `openSlug`, a directly-opened leaf doc, or a lone slice;
`undefined` for a master/series overview or the empty state) — derives that doc's `qualifiedLeafKey` as
`viewedLeafKey`, and reports it up through a `useEffect` keyed on `[viewedLeafKey, onViewLeaf]`. So the
rail chat + "attach to leaf" key by the leaf on screen, never the master/series behind it; a master or
series overview reports `undefined` (no single leaf). It renders freeform `sections` that are present on real task docs, including non-master `subTask` docs;
it does not parse or display `series-contract.md`. A sub-task row whose
`linkedLifecycleId` is set is a parallel/external series → an amber **"→"** that calls `onOpenLifecycle`
to switch the selected lifecycle; a child master's `masterLifecycleId` drives a **"↑ parent"** head
link. Prose (objective/design/section bodies) renders through the `Markdown` grammar component, bullets
and decision cells through its inline variant; `SubTaskIndex` omits its row-level `done/total ·` prefix when no matching task document supplies progress or when `progress.total === 0`; `SliceList` omits that prefix when `progress.total === 0`; `TaskReader` always mounts `ProgressFill`, so a zero-step reader displays `0/0`. `SpineLane` draws the code→CGC / memory→GrepAI lanes, joining the
enclosure's worktree-scoped engines by group name. **Operations-integration L4** adds change-set entry
buttons to the enclosure-spine block: a `ChangeSetButton` (lazily fetches its target's counters via the
L3 `data/changeset` client — deps are the stable target ids so the per-second projection tick does not
re-fetch; a `FilesApiError`, e.g. a completed task with no live worktree, hides the counts but keeps the
button) renders a **change-set** button (gated on `activeWorktreeGroups.includes(groupName)` →
`{ repo: enclosure.repoName, scope: groupName }`) and a **series** button (`enclosure.taskName` →
`{ repo, master }`), both calling the optional `onOpenChangeSet` prop to open the Change-Set Viewer
takeover. **L4a** moves the affordance onto the **task-document reader** itself (not only the live
enclosure spine, which is unchanged): `DocChangeSetBar` is rendered at the top of `MasterOverview` and
`TaskReader`, so it appears in **all** doc-render paths (no-lifecycle doc, series, active lifecycle).
Identity comes from the **doc node** — `repo = doc.repository`, `master = dirName(doc.docPath)` (the task
folder, which keys the change-set API), `leaf = doc.id` — so the bar shows with **no active enclosure**
(closing the L4 gap). A master gets a **series** button; a leaf gets a **committed** button (always — the
landed delta) plus a **working** button only when its enclosure is live (`DocChangeSetBar` reads
`enclosures` + `activeWorktreeGroups` itself, matching `repoName` + lowercased `leafId` + the worktree
group). `ChangeSetButton`'s target is the shared `ChangeSetTarget` (now `{repo, scope?, master?, leaf?,
mode?}`) and its counters fetch routes `leaf → leafChangeset`, else `master → masterChangeset`, else
`taskChangeset`; the bar is omitted entirely when `onOpenChangeSet` is not wired. Since
260712-TRH-L1, both reader-local and enclosure-spine change-set buttons stay unmounted while the visible
body is loading, so their eager counter effects cannot occupy the body request's connection slot.
Step status is
data-driven so `STEP_MARK`/
`STEP_TITLE`/`SUBSTEP` are record lookups (not cvas). `badge` + `laneMeta` are local (the old
`.badge`/`.engine__meta` were removed with their panels).

**L9 (agent-orchestration)** adds the coordination-notes surface: `TaskReader` no longer renders its
own References bullets — the trailing References block moved into `TaskNotes` (rendered with
`repo = doc.repository`, `master = dirName(doc.docPath)`, `references = doc.references`) so a
reference naming an existing `notes/` file becomes an openable link into the series-notes view;
`MasterOverview` appends `TaskNotes` with empty references, so the series' notes (design records,
friction ledger, `reports/`) are browsable from the master overview too. `TaskNotes` is likewise
unmounted while the visible body is loading and resumes after either terminal body state. All other
sections are unchanged.

### 260731-EFA-L4 The two sub-task row types

The master reader is fed by two different servers models, and the panel now says so in its types.
`SubTaskRow` (`types/projection.ts`) is the union `TaskSubTaskRefNode | SeriesSubTaskNode`, mirroring
two distinct `extra="forbid"` Python models in `observer/projection.py`:

- `TaskSubTaskRefNode` — a task-doc master's row. Fields `number/name/file/status/scope` plus the
  optional cross-series `linkedLifecycleId`. **No `createdAt`.**
- `SeriesSubTaskNode` — a series master's row. Same five fields plus `createdAt`. **No
  `linkedLifecycleId`.**

`MasterDocView` therefore declares `subTasks: SubTaskRow[]` explicitly instead of inheriting
`TaskDocNode["subTasks"]`; inheriting it is what let the two shapes read as one. `SubTaskIndex`,
`sliceForRef` and `subTaskKey` all take `SubTaskRow`.

Two consequences the panel now encodes rather than assumes:

1. **Creation ordering lives on the series branch only.** `seriesAsMasterDoc` calls
   `orderedByCreation(seriesNode.subTasks)`. Running it inside `SubTaskIndex` — where it used to live —
   was a permanent no-op on the task-doc-master path, because `orderedByCreation` bails unless EVERY
   row has `createdAt` and a `TaskSubTaskRefNode` never has one. On the series path it is a safety net:
   `snapshots.py::_series_subtask_nodes` already sorts by `createdAt` server-side.
2. **The cross-series `→` is reachable only from a task-doc master.** `SubTaskIndex` reads it as
   `"linkedLifecycleId" in ref ? ref.linkedLifecycleId : undefined`, and the narrowed local (not
   `ref.linkedLifecycleId as string`) is what feeds `onJump`/the title. For a series rendered through
   `seriesAsMasterDoc` the branch is structurally unreachable, because `SeriesSubTaskNode` has no such
   field.

`orderedByCreation` itself is no longer duplicated: the panel imports the one in
`data/taskHierarchy.ts` (now exported) instead of keeping a private copy. `SliceList` keeps calling it,
correctly — it sorts `TaskDocNode[]`, and task documents do carry `createdAt`.

### Todos

Body merge and cache follow-ups are owned by `data/useTaskDocumentBody.ts`; this panel has no additional
file-local follow-up.

### Invariants And Boundaries

`GateResponder` is only for durable gate decisions after L8. Ask-only attention details must not regain
an inline message-only response box in this panel; those conversations happen through the adjacent leaf
chat. Renders the full task content from the JSON-primary doc; only sections with content render.
Enclosure metadata can label a leaf or attach runtime state, but it is not a fallback content source for
leaf bodies — if no matching `TaskDocNode` exists, the no-doc fallback must render. The structured exception is master selection: an explicit
selected master document or `Analytics.series` is the master-reader surface, and `EnclosureNode.taskName`
may bridge a selected lifecycle row to it only when the selected lifecycle id is the root task identity
(`taskId`/`taskName`), still without parsing filenames or rendering contract prose as task content.

The reason for that ordering is that a promoted/attached leaf lifecycle carries parent task identity as
coordination metadata: `taskName` names the parent/root series folder, while the actual leaf content is
the `TaskDocNode` whose `lifecycleId` equals the selected lifecycle id. Treating `taskName` as a content
selector for every lifecycle makes all leaf lifecycle rows render the parent master. Therefore the
render precedence is deliberate: (1) an opened slice doc from the master sub-task index, (2) explicit
selected task document rendered by its own `kind`, (3) folder-keyed `analytics.series` for a selected
series/root task identity, (4) direct `analytics.taskDocuments` for selected leaf lifecycles, and only
then (5) the no-doc fallback.
Sub-task navigation — in-panel drill-in, the cross-master `→`, and the parent `↑` — is read-only routing
over the selected-lifecycle state, never a mutation; `onOpenLifecycle` is optional so the panel still
renders standalone (e.g. in tests). Parent `↑` links for directly opened leaves are navigation metadata
only and must not change the leaf content selector. A master row is clickable only when its authored
`file` resolves to a sibling JSON task document; rows without a projected sibling remain static. Creation ordering is
data-driven AND source-specific: `seriesAsMasterDoc` sorts a series' rows by `createdAt` (the only rows
that carry it), and `orderedByCreation` still preserves authored order whenever any row lacks the
field. A task-doc master's rows are never sorted here — they have no `createdAt`, so a sort placed on
that path would be a branch that can never do anything. Do not re-widen `MasterDocView.subTasks` back
to `TaskDocNode["subTasks"]`: the two server models are `extra="forbid"` and genuinely differ, and the
union is what keeps `linkedLifecycleId` and `createdAt` attached to the source that actually sends
them. Visible master leaf numbers are never generated row indexes or parsed
numeric filename/task prefixes. When an authored sibling `TaskDocNode` is projected, its `id` is the
visible number; the parent ref `number` is fallback only for rows without a projected child doc.
User-facing task progress in the master index and leaf reader must use projected
`stepsDone`/`stepsTotal`; the component must not derive a competing count from visible steps. Step and
code-example labels must compose structured ids with titles at render time; do not embed ids inside
title strings and do not strip ids from display.
Series token totals are displayed only from the server-projected `SeriesNode.seriesTokenTotal`; the
panel must not recompute the aggregate from lifecycle token gauges or child task rows.
Complete visible task content outranks optional reader metadata: `TaskNotes` and every eager
`ChangeSetButton` under the selected reader remain unmounted only while body state is `loading`, then
resume for both `available` and `unavailable` so fallback mode retains existing tools.

### 2026-07-24 Curator Delta

`DetailPanel` is now a memoized persistent cockpit layer. Stable callbacks and unchanged selection let
view switches skip its subtree, while real selection and store changes still pass through the memo gate.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `displayedReaderDoc`; `useTaskDocumentBody`; `taskDocumentBodyState`; `TaskNotes`; `DocChangeSetBar`; `MasterOverview`; `TaskReader`; "change-set"; "loading"; "Loading complete task document…" | `taskDocumentBodyState` | dashboard/src/panels/detail-panel/state.ts:138-146 |
| The hook owns fetch, merge, availability, and path-plus-revision caching; the API literal remains in the transport helper. | `useTaskDocumentBody`; `mergeTaskDocumentBody`; `taskDocumentBodyKey`; `fetchTaskDocument` | dashboard/src/data/useTaskDocumentBody.ts:9-11; dashboard/src/data/useTaskDocumentBody.ts:13-27; dashboard/src/data/useTaskDocumentBody.ts:29-74; dashboard/src/data/taskDocuments.ts:3-9 |
| Component regressions pin body-first request ordering, complete field rendering, fallback visibility, one implementation-step copy, and revision caching. | "loads the complete task body before mounting reader ancillary requests"; "renders the complete on-demand task-document body while retaining its summary"; "shows the available summary when the on-demand task-document body is absent"; "reuses an unchanged task body and refetches when its revision changes" | dashboard/src/panels/detail-panel/taskBody.test.tsx:115-115; dashboard/src/panels/detail-panel/taskBody.test.tsx:12-12; dashboard/src/panels/detail-panel/taskBody.test.tsx:184-184; dashboard/src/panels/detail-panel/taskBody.test.tsx:208-208 |
| `parseTaskSelection` resolves typed taskdoc/series/lifecycle selections before rendering by task-document `kind`. | "const selectedTaskDoc = resolveSelectedTaskDoc(selection, allDocs);"; "const TASKDOC_PREFIX = \"taskdoc:\";"; "const SERIES_PREFIX = \"series:\";"; "const LIFECYCLE_PREFIX = \"lifecycle:\";" | dashboard/src/panels/detail-panel/state.ts:119-120; dashboard/src/data/taskIdentity.ts:13-16 |
| Typed Operations selection helpers shared with Cockpit and LifecycleList. | "export const taskDocSelectionKey"; "key: taskDocSelectionKey(doc.docPath)"; "key: seriesSelectionKey(series.seriesId)"; "key: lifecycleSelectionKey(lifecycle.id)"; "function selectionKey(selection"; "lifecycleSelectionKey(id)" | dashboard/src/cockpit/Cockpit.tsx:517-517; dashboard/src/data/taskIdentity.ts:18-18; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:755-755; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:804-804; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:879-879; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:1004-1004 |
| The selected-series derivation: `selectedIsRootTask`, `selectedSeries`, `seriesAsMasterDoc`, `seriesSliceDocs`. | "selectedIsRootTask: boolean"; "const selectedSeries = resolveSelectedSeries("; "? seriesSliceDocs(allDocs, master.docPath)"; ": seriesAsMasterDoc(selectedSeries);" | dashboard/src/panels/detail-panel/state.ts:75-76; dashboard/src/panels/detail-panel/state.ts:131-137; dashboard/src/panels/detail-panel/lifecycleBody.tsx:67-67; dashboard/src/panels/detail-panel/lifecycleBody.tsx:87-87 |
| Lifecycle-bound selected masters render `MasterOverview` with sibling docs from the full projected task-document pool, so master rows can open authored leaves that are not sidebar rows. | "import { MasterOverview, TaskReader } from \"./taskReader\";"; "export function taskDocsForLifecycle(" | dashboard/src/data/taskIdentity.ts:281-281; dashboard/src/panels/detail-panel/taskDocPanels.tsx:15-15 |
| Direct taskdoc and active lifecycle leaf selections use `parentTaskLinkForDoc` to show a sticky parent/root backlink without changing leaf content selection. | "import { parentTaskLinkForDoc } from \"../../data/taskHierarchy\";"; "export function parentTaskLinkForDoc("; "export function TaskContent({" | dashboard/src/panels/detail-panel/taskDocPanels.tsx:1-1; dashboard/src/data/taskHierarchy.ts:68-68; dashboard/src/panels/detail-panel/taskReader.tsx:77-77 |
| `displayedLeafDoc` resolves the leaf actually on screen (mirroring the render branches; `undefined` for a master/series overview) and reports its `qualifiedLeafKey` up via effect (L5 fix 1). | "import { displayedLeafDoc, displayedReaderDoc } from './model';"; "export function displayedLeafDoc({"; "const viewedLeafDoc = displayedLeafDoc({"; "export function qualifiedLeafKey(" | dashboard/src/data/taskIdentity.ts:65-65; dashboard/src/panels/detail-panel/model.ts:123-123; dashboard/src/panels/detail-panel/state.ts:21-21; dashboard/src/panels/detail-panel/state.ts:147-155 |
| The task reader wraps rendered leaf content in `data-task-leaf-key={qualifiedLeafKey(doc)}` so selection capture can attribute highlighted text to the displayed leaf. | "const TASK_LEAF_SELECTOR ="; "export function readSelection(selection: Selection"; "export function qualifiedLeafKey("; "export function TaskReader({" | dashboard/src/data/selection.ts:22-22; dashboard/src/data/selection.ts:39-49; dashboard/src/data/taskIdentity.ts:64-70; dashboard/src/panels/detail-panel/taskReader.tsx:494-528 |
| `findParentTaskMatch`/`parentTaskLinkForDoc` resolve parent task links from projected series sub-task refs and typed selection keys; `orderedByCreation` is now exported from here rather than copied into this panel. | `findParentTaskMatch`; `parentTaskLinkForDoc`; `orderedByCreation`; `parentSelectionKey` | dashboard/src/data/taskHierarchy.ts:43-51; dashboard/src/data/taskHierarchy.ts:68-82; dashboard/src/data/taskHierarchy.ts:152-156; dashboard/src/data/taskHierarchy.ts:145-150 |
| `SubTaskRow`; `TaskSubTaskRefNode`; `SeriesSubTaskNode`; `linkedLifecycleId` | `SubTaskRow`; `TaskSubTaskRefNode`; `linkedLifecycleId` | dashboard/src/types/projection.ts:546-553; dashboard/src/types/projection.ts:567-567 |
| The two `extra="forbid"` server models the union mirrors. | `TaskSubTaskRefNode`; `SeriesSubTaskNode` | mcp/src/agents_remember/observer/projection.py:575-592; mcp/src/agents_remember/observer/projection.py:657-672 |
| `_series_subtask_nodes`; `seriesAsMasterDoc`; `orderedByCreation`; `createdAt` | "export function orderedByCreation" | dashboard/src/data/taskHierarchy.ts:145-145 |
| `MasterDocView`; `SubTaskRow`; `seriesAsMasterDoc`; `orderedByCreation` | `orderedByCreation` | dashboard/src/data/taskHierarchy.ts:145-150 |
| `SubTaskIndex` renders in received order and reads the cross-link as `"linkedLifecycleId" in ref`, so the `→` branch is unreachable for a series. | `SubTaskIndex` | dashboard/src/panels/detail-panel/taskReader.tsx:323-358 |
| `parentTaskLinkForDoc` links an enclosure-opened leaf back to its parent task document (`master-parent-link`), pinned by the promotedIdentity suite. | "export function parentTaskLinkForDoc("; "links an enclosure-opened leaf back to its parent task document" | dashboard/src/data/taskHierarchy.ts:68-68; dashboard/src/panels/detail-panel/promotedIdentity.test.tsx:29-29 |
| `taskStepProgress`, `SubTaskIndex`, `SliceList`, `TaskReader`, and `ProgressFill` compose the master/slice progress UI. | "export const taskStepProgress = (doc: TaskDocNode): { done: number; total: number } => ({"; "export function SubTaskIndex({"; "export function SliceList({"; "export function TaskReader({"; "export function ProgressFill({" | dashboard/src/panels/detail-panel/model.ts:155-155; dashboard/src/panels/detail-panel/taskReader.tsx:323-323; dashboard/src/panels/detail-panel/taskReader.tsx:361-361; dashboard/src/panels/detail-panel/taskReader.tsx:494-494; dashboard/src/grammar/ProgressFill.tsx:27-27 |
| Master leaf rows render in received order and display the matched child task document `id`, with `position` kept separate purely for stable test ids; `SliceList` keeps the `createdAt` sort because it orders `TaskDocNode`s. | "export function SubTaskIndex({"; "export function SliceList({"; "export function subTaskKey(ref: SubTaskRow"; "import { orderedByCreation } from \"../../data/taskHierarchy\";" | dashboard/src/panels/detail-panel/taskReader.tsx:323-323; dashboard/src/panels/detail-panel/taskReader.tsx:361-361; dashboard/src/panels/detail-panel/model.ts:208-208; dashboard/src/panels/detail-panel/taskReader.tsx:12-12 |
| `TaskReader` renders the top `ProgressFill` before the task body and keeps implementation-step copy later in the document. | "export function TaskReader({"; "export function ProgressFill({" | dashboard/src/panels/detail-panel/taskReader.tsx:494-494; dashboard/src/grammar/ProgressFill.tsx:27-27 |
| `seriesAsMasterDoc`; `masterDocWithSeriesTokens`; `seriesTokenTotal`; `MasterTokenSummary` | `masterDocWithSeriesTokens` | dashboard/src/panels/detail-panel/model.ts:198-201 |
| The `SeriesNode`, `TaskDocNode`, and `SeriesSubTaskNode.createdAt` contract fields consumed by this panel, mirrored in the dashboard projection types. | `SeriesNode`; `TaskDocNode`; `SeriesSubTaskNode` | dashboard/src/types/projection.ts:377-392; dashboard/src/types/projection.ts:400-407; dashboard/src/types/projection.ts:484-510 |
| `taskLabel`/`taskDocsForLifecycle`/`taskDocumentLabel` — the lifecycle-visible identity helpers used to label promoted leaf lifecycles without changing task-document filtering. | `taskLabel`; `taskDocsForLifecycle`; `taskDocumentLabel`; `findLifecycleEnclosure` | dashboard/src/data/taskIdentity.ts:253-260; dashboard/src/data/taskIdentity.ts:262-279; dashboard/src/data/taskIdentity.ts:281-286; dashboard/src/data/taskIdentity.ts:288-293 |
| The durable gate responder, now rendered only for real `activeLifecycle.gate` requests. | "testId=\"gate-review\""; "function DetailPanelImpl({"; "<GateResponder" | dashboard/src/panels/detail-panel/lifecycleBody.tsx:226-226; dashboard/src/panels/detail-panel/DetailPanel.tsx:18-18; dashboard/src/panels/detail-panel/lifecycleBody.tsx:222-222 |
| `Markdown`; `Bullets`; `DecisionList`; `MasterSection` | `DecisionList` | dashboard/src/panels/detail-panel/taskReader.tsx:612-627 |
| `ProgressFill` + `TokenGauge` grammar it composes. | `ProgressFill`; `TokenGauge` | dashboard/src/grammar/ProgressFill.tsx:27-45; dashboard/src/grammar/TokenGauge.tsx:18-53 |
| The shared empty-state backdrop the no-selection state renders. | `EmptyStateBackdrop` | dashboard/src/panels/EmptyStateBackdrop.tsx:52-97 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `DetailPanel.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: re-mapped this sidecar from dashboard/src/panels/DetailPanel.tsx to the detail-panel/ canonical entry after the responsibility split; added the L8 Split Layout section. Verification pinned to the leaf base until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `:1-1`/wrong ranges
  with exact source-backed occurrences; exact non-fixing check returns zero findings.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected two live contracts:
  `seriesSliceDocs` is a same-directory filter that does not itself exclude a master, and displayed
  progress forwards projected `stepsDone`/`stepsTotal` through `taskStepProgress`. New ranges are
  explicit `:1-1` curator input.

- 2026-08-03T08:32:29+02:00 — 260731-EFA-L6 W3-B11 max-reviewer correction, provenance
  closure, and developer-authorized line-146 factual correction: restaged and independently
  verified whole-claim evidence for rows 270, 273, 274, 276, 277, 278, and 293; a fresh exact
  fixer repair emitted `repairs[].now` for row 274's frozen consumer call sites and removed all
  provisional `:1-1` inputs. The authorized current-behavior sentence replaced the false `0/0`
  suppression clause. The final checker remains at two intentional row-275 diagnostics. Unrelated
  green-row ambiguity declines were not treated as findings. The `seriesSliceDocs` residual remains
  unchanged; code content was read-only.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations — the reference row and the restatement in the 09:58 entry
  below — after that module was restructured. `L542-L559` → `L552-L569` (`class TaskSubTaskRefNode`
  L552, `extra="forbid"` L559, `linkedLifecycleId` L569) and `L624-L639` → `L634-L649` (`class
  SeriesSubTaskNode` L634, `extra="forbid"` L642, `createdAt` L649). Each range ends on exactly the
  field the finding names. No body claim changed.

- 2026-08-01T09:58+02:00 — 260731-EFA-L4 curator: corrected two false body claims. `SubTaskIndex` no
  longer calls `orderedByCreation` — it renders in received order — so "calls `orderedByCreation` before
  rendering rows" and the Purpose line's unconditional "default to creation order" were both wrong; the
  sort now lives in `seriesAsMasterDoc`, the only path whose rows carry `createdAt`. Documented the
  `SubTaskRow` union (`TaskSubTaskRefNode | SeriesSubTaskNode`, two `extra="forbid"` server models),
  `MasterDocView.subTasks` widening to it, and the `"linkedLifecycleId" in ref` narrowing that makes
  the cross-series `→` structurally unreachable for a series. Verified against the models
  (`projection.py` L552-L569 / L634-L649) that only `TaskSubTaskRefNode` declares `linkedLifecycleId`
  and only `SeriesSubTaskNode` declares `createdAt`, and against `snapshots.py::_series_subtask_nodes`
  that the server already sorts a series' rows — so the surviving client sort is a safety net, recorded
  as such. Noted `orderedByCreation` is now imported from `data/taskHierarchy.ts` rather than kept as a
  private copy, and that `SliceList` still calls it correctly (it orders `TaskDocNode`s, which do carry
  `createdAt`). Repaired nine citations that had drifted off their symbols, including
  `topLevelStepProgress` L553-L556 → L932-L935, `displayedLeafDoc` L771-L818 → L884-L931,
  `MasterTokenSummary` L652-L705 → L1099-L1108, `TaskReader` L833-L866 → L1307-L1345, and the
  projection-mirror row cit:([`TaskDocNode`, `SeriesNode`, `SeriesSubTaskNode`], dashboard/src/types/projection.ts:377-392; dashboard/src/types/projection.ts:400-407; dashboard/src/types/projection.ts:484-510),
  whose prior ranges contained none of the named types.

- 2026-08-01T09:58+02:00 — 260731-EFA-L4 curator: corrected two false body claims. `SubTaskIndex` no
  longer calls `orderedByCreation` — it renders in received order — so "calls `orderedByCreation` before
  rendering rows" and the Purpose line's unconditional "default to creation order" were both wrong; the
  sort now lives in `seriesAsMasterDoc`, the only path whose rows carry `createdAt`. Documented the
  `SubTaskRow` union (`TaskSubTaskRefNode | SeriesSubTaskNode`, two `extra="forbid"` server models),
  `MasterDocView.subTasks` widening to it, and the `"linkedLifecycleId" in ref` narrowing that makes
  the cross-series `→` structurally unreachable for a series. Verified against the models
  (`projection.py` L552-L569 / L634-L649) that only `TaskSubTaskRefNode` declares `linkedLifecycleId`
  and only `SeriesSubTaskNode` declares `createdAt`, and against `snapshots.py::_series_subtask_nodes`
  that the server already sorts a series' rows — so the surviving client sort is a safety net, recorded
  as such. Noted `orderedByCreation` is now imported from `data/taskHierarchy.ts` rather than kept as a
  private copy, and that `SliceList` still calls it correctly (it orders `TaskDocNode`s, which do carry
  `createdAt`). Repaired nine citations that had drifted off their symbols, including
  `topLevelStepProgress` L553-L556 → L932-L935, `displayedLeafDoc` L771-L818 → L884-L931,
  `MasterTokenSummary` L652-L705 → L1099-L1108, `TaskReader` L833-L866 → L1307-L1345, and the
  projection-mirror row cit:([`TaskDocNode`, `SeriesNode`, `SeriesSubTaskNode`], dashboard/src/types/projection.ts:376-391; dashboard/src/types/projection.ts:399-406; dashboard/src/types/projection.ts:457-509),
  whose prior ranges contained none of the named types.

- 2026-07-24T13:17:50Z — Added persistent DetailPanel memoization semantics. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: changed the existing series change-set counter call site to request `includeLeaves=false`; no new reader state or transport behavior was introduced. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1: moved hydration/cache ownership to
  `data/useTaskDocumentBody.ts`, threaded explicit body state through every reader branch, added honest
  loading copy, and deferred notes plus all eager change-set counters until body success or failure.
  Moved the merge/cache Todos to the owning hook sidecar. Verification metadata stays pinned until
  closeout stamps the code commit.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 R7: merged on-demand body fields over the current
  summary with absent-array preservation, surfaced an explicit summary fallback on fetch failure,
  and removed the duplicate Progress step list so implementation steps render once. Recorded the
  scalar-overwrite and cache-eviction reviewer notes. The `/api/task-document` literal remains owned
  by `data/taskDocuments.ts` (CD-N1 attribution correction). Verification metadata stays pinned until
  closeout stamps the eventual L16 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6: migrated every task-reader branch from broadcast
  bodies to one on-demand full-body fetch, keyed the local cache by `docPath + bodyRevision`, and
  documented the accepted no-eviction follow-up. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.

- 2026-07-07T14:00+02:00 — agent-orchestration L17: `DetailPanel` now threads an `onOpenNotes` prop
  (parallel to `onOpenChangeSet`) from `CockpitShell` down through `TaskReader` / `MasterOverview` /
  `TaskContent` into `TaskNotes`, so a note list-row or resolved reference opens the L17 Notes Reader
  takeover (the inline `TaskNotes` reading pane is retired). Also de-staled the header comment: the Gate
  Respond surface is durable-gates-only (the wait-loop "ask fallback" phrasing was removed). The series-notes
  test now asserts the `onOpenNotes` callback instead of an inline `note-view`. Verification metadata pinned
  until closeout stamps the L17 commit.
- 2026-07-06T02:30+02:00 — agent-orchestration L9 (friction F-M): the References section moved out
  of `TaskReader` into the new `TaskNotes` component (repo/master derived from the doc node like
  `DocChangeSetBar`), which resolves references into openable notes links and lists the series'
  `notes/` tree; `MasterOverview` appends `TaskNotes` (list only). Verification metadata pinned
  until closeout stamps the L9 commit.
- 2026-07-02T16:18+02:00 — L8: `GateResponder` now renders only for durable `activeLifecycle.gate`
  requests, removing the obsolete ask-only task-local response box from attention details. `TaskReader`
  now marks leaf content with `data-task-leaf-key` so highlight capture can route obvious leaf selections
  to the adjacent chat draft. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: added the optional `onViewLeaf` prop + a `displayedLeafDoc(...)` helper that
  resolves the leaf actually on screen (a drilled sub-task / a directly-opened leaf doc / a lone slice;
  `undefined` for a master/series overview) and reports its `qualifiedLeafKey` up via effect — so the rail
  chat + "attach to leaf" key by the displayed leaf, not the top-level (master) selection. Verification
  metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — Operations Integration L4a (change-set on the doc reader): added
  `DocChangeSetBar`, rendered at the top of `MasterOverview` (a **series** button) and `TaskReader` (a
  **committed** button always + a **working** button only when the leaf's enclosure is live), with identity
  derived from the doc node (`repo=doc.repository`, `master=dirName(doc.docPath)`, `leaf=doc.id`) so it
  shows with no active enclosure. `ChangeSetButton`/`onOpenChangeSet` now use the shared `ChangeSetTarget`
  (`leaf?`+`mode?` added) and the counters fetch routes leaf→`leafChangeset`; the L4 enclosure-spine block
  is unchanged. The bar is omitted when `onOpenChangeSet` is not wired. Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4 (Change-Set Viewer): the enclosure-spine block gained change-set entry buttons — a `ChangeSetButton` (lazy counters via the L3 `data/changeset` client; deps are the stable target ids; a `FilesApiError` hides the counts but keeps the button) renders a **change-set** button (gated on `activeWorktreeGroups.includes(groupName)` → `taskChangeset(repo, groupName)`) and a **series** button (`enclosure.taskName` → `masterChangeset`), opening the Change-Set Viewer takeover via the new optional `onOpenChangeSet` prop. Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: master readers now display
  `seriesTokenTotal` from `Analytics.series`, including concrete master task docs matched by `docPath`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:11+02:00 — Corrected Task 17 live-data numbering: authored master leaf rows now show the
  child `TaskDocNode.id` and title, using the parent ref number/name only when no child doc is projected.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Corrected Task 17 leaf numbering: master sub-task rows still order by
  structured creation metadata, but visible labels now use each ref's structured task number instead of
  a generated local counter. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 parent-link follow-up: directly opened leaf task documents and
  enclosure-backed leaf lifecycles now show a sticky parent/root task backlink resolved through
  structured series metadata, while leaf content still comes only from the selected leaf task document.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:20+02:00 — Task 17 master-navigation/sidebar-scope correction: lifecycle-bound masters
  now render their sub-task index against the full projected sibling task-document pool, keeping authored
  leaves clickable from the master even when they are not sidebar rows; missing authored siblings remain
  static. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first reader: DetailPanel now resolves typed
  `taskdoc:`/`series:`/`lifecycle:` selections, renders unbound planning documents, uses document
  `kind` to choose master vs leaf content, and displays structured step/example ids with titles.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T15:37+02:00 — Task 17 live-projection correction: selected lifecycle rows bridge to
  `analytics.series` only for root task identity (`lifecycle.id` equals enclosure `taskId`/`taskName`);
  leaf lifecycle rows without projected task docs show the no-doc fallback instead of rendering the
  parent master, while projected leaf docs still render their own reader. Verification metadata pinned
  until closeout stamps the follow-up code commit.
- 2026-06-24T15:23+02:00 — Superseded Task 17 lifecycle-leaf regression note: the first follow-up used
  "no direct task document" as the bridge discriminator; live projection inspection showed that was the
  wrong boundary because unprojected leaf docs also have no direct task document. The current rule above
  uses root task identity instead.
- 2026-06-24T13:59+02:00 — Task 17 progress-count follow-up: master leaf rows, master-less slice rows,
  and the leaf reader's blue progress fill now summarize top-level implementation steps instead of the
  backend's nested progress-bearing leaf totals. Verification metadata pinned until closeout stamps the
  follow-up code commit.
- 2026-06-24T12:53+02:00 — Master selection follow-up: selected task-id lifecycles now join through
  structured enclosure `taskName` to the folder-keyed `analytics.series` master, so clicking the root
  master row renders master content instead of the lifecycle no-doc fallback. Verification metadata
  pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:21+02:00 — Task 17 master reader update: selected series masters can render from
  `analytics.series`, master rows display labelled sub-task rows and sort by structured creation time when
  available, and leaf task docs show a top Progress block before Objective. Ordering deliberately
  preserves authored order when `createdAt` is incomplete rather than parsing filename prefixes.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Promoted leaf task-document correction: `DetailPanel` now uses
  `taskIdentity` helpers to label selected leaf lifecycles from enclosure metadata while reading body
  content only from direct `analytics.taskDocuments` matches; real task-doc `sections` render, but
  `series-contract.md` never becomes task content. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-23T13:45+02:00 — Task 11: replaced the local `GateReview` `/api/actions` decision drawer
  with the shared `GateResponder` for both durable gates and proto `ask`s. The detail panel remains the
  canonical task gate surface, but responses now route back into the attached hosted chat via
  `deliverToSession`. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-23T07:25+02:00 — UI copy rename (user-facing lifecycle → task): the no-selection placeholder
  now reads **"Select a task to inspect its phase, gate, and tokens."** (was "…a session…") and the
  `TaskContent` empty fallback **"No task document bound to this task."** (was "…this lifecycle.").
  Display copy only — the selected unit, props (`selectedId`), and `lifecycleId` keying are unchanged.
  Refreshed the Logic commentary for both strings. Verification metadata pinned until closeout stamps
  the rename code commit.
- 2026-06-23T04:20+02:00 — Slice 07b polish: the no-selection state now renders inside the shared
  `EmptyStateBackdrop` — a faint, effects-gated **battle-cruiser** boomerang-video atmosphere
  (`/assets/sc2-battlecruiser-boomerang.mp4`, aria-hidden, absent under calm-cockpit / reduced-motion)
  behind the "Select a session to inspect…" copy, inside the `Panel` `fill` slot (its flex column lets
  the backdrop's `flex:1` canvas fill). Added the `EmptyStateBackdrop` reference. Verification metadata
  pinned until closeout stamps the slice-07b code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: master overview + clickable `SubTaskIndex` (pinned above the description + in its authored section, `subtask-open`/`subtask-mid` testids); in-panel drill-in with the back/parent up-link lifted into the `Panel` sticky `head` (drill `openSlug` state moved from `TaskContent` to `DetailPanel`); markdown rendering via the new `Markdown` grammar component; cross-master `→` rows + parent `↑` breadcrumb that switch lifecycles through the new optional `onOpenLifecycle` prop; `0/0` step counts suppressed. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-18T15:00+02:00 — Task 6 slice 6c Part B: the display-only gate banner became the **Gate Review drawer** — `GateReview` POSTs `lifecycle.gate.decisions` to `/api/actions` via `data/actions.postGateDecision`, with honest status; the `ask` proto-gate falls back to the display banner. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-15T17:00+02:00 — Created for slice 5d: migrated onto `Panel` + Panda css/cva; `badge`/`laneMeta`
  localized (their source panels' classes were removed). Verification metadata pinned until closeout
  stamps the 5d code commit.
