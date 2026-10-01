# dashboard/src/panels/detail-panel/DetailPanel.tsx

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


## 260831-CCR-L23 Shared Task-Artifact Reader Target

The panel's `NotesReaderTarget` import is now the shared discriminated
`TaskArtifactReaderTarget` alias from `dashboard/src/data/taskArtifacts.ts`
(`import type { TaskArtifactReaderTarget as NotesReaderTarget }`). The
`onOpenNotes` callback `DetailPanel` threads therefore carries the union:
a `kind: "notes"` member for note opens and a `kind: "requirements"` member
(with the task-document reference) for requirement-packet opens. Routing the callback
into the reader and takeover is unchanged.

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

The series change-set entry point requests the master net counters **with** the per-leaf breakdown
(`includeLeaves: true`, 260921-ICR-L33 / R33.2) and prints that attribution beside the total
(`2 leaf/leaves · 1 committed · 1 working`), because the net total IS the sum of those leaves and a
reviewer must be able to attribute it — the bar's `leafAttribution` reads the master read's own
`leaves` and renders nothing at all when the answer carried none, rather than a zero. **The sentence
that stood here said the opposite** — "without the optional per-leaf breakdown because this reader only
opens the net viewer" — and it was false at this candidate: it recorded the `includeLeaves: false`
optimisation commit `a1521685` introduced, which R33.2 supersedes. The existing task and leaf entry
behavior is unchanged.

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

Since 260815-DAG-L14 `DetailPanel` threads `docPathForRef` from `useDetailPanelState` into the
task readers so typed `masterRef` sprint rows can open their commanded master document (the sprint →
master leg of the drill-down).

## Evidence

### Repo-Internal References

- `displayedReaderDoc`; `useTaskDocumentBody`; `taskDocumentBodyState`; `TaskNotes`; `DocChangeSetBar`; `MasterOverview`; `TaskReader`; "change-set"; "loading"; "Loading complete task document…" [1]
- The hook owns fetch, merge, availability, and path-plus-revision caching; the API literal remains in the transport helper. [2]
- Component regressions pin body-first request ordering, complete field rendering, fallback visibility, one implementation-step copy, and revision caching. [3]
- `parseTaskSelection` resolves typed taskdoc/series/lifecycle selections before rendering by task-document `kind`. [4]
- The shared task-document selector prefixes the canonical docPath. [5]
- Task-document rows use the shared task-document key. [6]
- Series rows use the shared series key. [7]
- Lifecycle rows use the shared lifecycle key. [8]
- Selected typed identities map back to the same three row-key helpers. [9]
- Cockpit preserves typed selection keys and qualifies a raw lifecycle id before opening Operations. [10]
- The selected-series derivation: `selectedIsRootTask`, `selectedSeries`, `seriesAsMasterDoc`, `seriesSliceDocs`. [11]
- Lifecycle-bound selected masters render `MasterOverview` with sibling docs from the full projected task-document pool, so master rows can open authored leaves that are not sidebar rows. [12]
- Direct taskdoc and active lifecycle leaf selections use `parentTaskLinkForDoc` to show a sticky parent/root backlink without changing leaf content selection. [13]
- `displayedLeafDoc` resolves the leaf actually on screen (mirroring the render branches; `undefined` for a master/series overview) and reports its `qualifiedLeafKey` up via effect (L5 fix 1). [14]
- The task reader derives the displayed leaf key and places it on the rendered content wrapper. [15]
- The shared qualified key is repo/master/leaf-id and requires all three parts. [16]
- Selection attribution looks for the closest task-leaf wrapper. [17]
- Mouse selection context carries the leaf key read from that wrapper. [18]
- `findParentTaskMatch`/`parentTaskLinkForDoc` resolve parent task links from projected series sub-task refs and typed selection keys; `orderedByCreation` is now exported from here rather than copied into this panel. [19]
- SubTaskRow is the union of the distinct task-master and series row shapes. [20]
- Task-master rows may carry a linked lifecycle id and masterRef. [21]
- Series rows instead carry optional creation time. [22]
- The two `extra="forbid"` server models the union mirrors. [23]
- `_series_subtask_nodes`; `seriesAsMasterDoc`; `orderedByCreation`; `createdAt` [24]
- `MasterDocView`; `SubTaskRow`; `seriesAsMasterDoc`; `orderedByCreation` [25]
- `SubTaskIndex` renders in received order and reads the cross-link as `"linkedLifecycleId" in ref`, so the `→` branch is unreachable for a series. [26]
- `parentTaskLinkForDoc` links an enclosure-opened leaf back to its parent task document (`master-parent-link`), pinned by the promotedIdentity suite. [27]
- Task progress forwards the projected done and total counts. [28]
- The master index renders its received sub-task references. [29]
- The master-less slice list sorts task documents and displays their progress. [30]
- The task reader places ProgressFill in the header before body sections. [31]
- ProgressFill is the shared progress display primitive. [32]
- The master index preserves received order and passes a separate one-based position for test ids. [33]
- Sub-task labels prefer the matched child task id and title, then the received reference values. [34]
- The row uses position for test ids and the resolved child for navigation. [35]
- The slice list retains createdAt ordering because it operates on task documents. [36]
- `TaskReader` renders the top `ProgressFill` before the task body and keeps implementation-step copy later in the document. [37]
- `seriesAsMasterDoc`; `masterDocWithSeriesTokens`; `seriesTokenTotal`; `MasterTokenSummary` [38]
- SeriesNode provides the series fields and typed sub-task rows consumed by the panel. [39]
- TaskDocNode provides authored task identity, creation time and task-master references. [40]
- Only the series sub-task row has optional createdAt. [41]
- `taskLabel`/`taskDocsForLifecycle`/`taskDocumentLabel` — the lifecycle-visible identity helpers used to label promoted leaf lifecycles without changing task-document filtering. [42]
- The durable gate responder, now rendered only for real `activeLifecycle.gate` requests. [43]
- `Markdown`; `Bullets`; `DecisionList`; `MasterSection` [44]
- `ProgressFill` + `TokenGauge` grammar it composes. [45]
- The shared empty-state backdrop the no-selection state renders. [46]
