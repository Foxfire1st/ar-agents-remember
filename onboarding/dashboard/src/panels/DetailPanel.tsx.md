# dashboard/src/panels/DetailPanel.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/DetailPanel.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T13:41+02:00                           |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`       |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

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
display each authored leaf task document's own task id and default to creation order (`createdAt`) when
every row has structured creation metadata; they do not parse numeric filename prefixes or generate
reader-local display counters. Leaf progress
summaries in the master index and reader header are derived from visible top-level implementation steps,
not nested substeps. Master sub-task navigation resolves authored leaf documents from the full projected
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

The always-on `analytics.taskDocuments` collection is now summary-only. `DetailPanel` resolves the
single document whose reader is actually visible, requests its full body through
`fetchTaskDocument`, and caches the response under `docPath + bodyRevision`. Every render branch
(direct task document, series master, lifecycle-bound master/leaf, and drilled slice) substitutes the
cached merged node when available and otherwise keeps the bounded summary as a non-blocking fallback.
L16 merges the fetched body over the current summary while preserving each summary array when the body
omits it. Changing `bodyRevision` creates a new cache key and causes the currently displayed document
to be refetched. A failed fetch records `unavailable` for that key and shows the exact fallback line
"Full task document details are unavailable; showing the available summary." while retaining the
summary. Reselecting or changing revision retries; failure does not create an effect retry loop.

### Logic

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
`seriesSliceDocs` limits drill-in candidates to sibling leaf task docs. `taskLabel` uses enclosure
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
lifecycle's `lifecycleId`). `SubTaskIndex` calls `orderedByCreation` before rendering rows, displays
`${match?.id || ref.number}. ${match?.title || ref.name}` labels, and uses a separate position counter
only for stable test ids; if any row lacks `createdAt`, it preserves the input/master-authored order
rather than guessing from the number or filename. `SliceList`
uses the same helper so master-less leaf lists default to creation order when all docs expose
`createdAt`. `topLevelStepProgress` counts `doc.steps` and completed top-level step statuses;
`SubTaskIndex`, `SliceList`, and the `TaskReader` header `ProgressFill` use that top-level summary
instead of `TaskDocNode.stepsDone/stepsTotal`, which may be the backend's nested progress-bearing leaf
count. `TaskReader` renders the top-level progress fill in its head and the step rows exactly once
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
and decision cells through its inline variant; a `0/0` step count is suppressed. `SpineLane` draws the code→CGC / memory→GrepAI lanes, joining the
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
`taskChangeset`; the bar is omitted entirely when `onOpenChangeSet` is not wired. Step status is
data-driven so `STEP_MARK`/
`STEP_TITLE`/`SUBSTEP` are record lookups (not cvas). `badge` + `laneMeta` are local (the old
`.badge`/`.engine__meta` were removed with their panels).

**L9 (agent-orchestration)** adds the coordination-notes surface: `TaskReader` no longer renders its
own References bullets — the trailing References block moved into `TaskNotes` (rendered with
`repo = doc.repository`, `master = dirName(doc.docPath)`, `references = doc.references`) so a
reference naming an existing `notes/` file becomes an openable link into the series-notes view;
`MasterOverview` appends `TaskNotes` with empty references, so the series' notes (design records,
friction ledger, `reports/`) are browsable from the master overview too. All other sections are
unchanged.

### Todos

- Reviewer D-N4: `mergeTaskDocumentBody` lets present body scalars overwrite the live projection
  summary wholesale. A lagging body can display older scalar values until `bodyRevision` changes;
  array fields alone use the explicit absent-body preservation rule.
- The body cache remains unbounded for the browser session; revisions are keyed safely but not evicted.

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
data-driven: when every row has `createdAt`, the panel sorts by that value; when any row lacks it, the
authored order is preserved. Visible master leaf numbers are never generated row indexes or parsed
numeric filename/task prefixes. When an authored sibling `TaskDocNode` is projected, its `id` is the
visible number; the parent ref `number` is fallback only for rows without a projected child doc.
User-facing task progress in the master index and leaf reader must match the visible top-level
implementation-step list; nested substeps should not inflate those orientation counts. Step and
code-example labels must compose structured ids with titles at render time; do not embed ids inside
title strings and do not strip ids from display.
Series token totals are displayed only from the server-projected `SeriesNode.seriesTokenTotal`; the
panel must not recompute the aggregate from lifecycle token gauges or child task rows.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The visible document fetch merges body arrays with the live summary, records availability, and renders an honest summary fallback on failure. | L343-L417; L1261-L1359 | [DetailPanel.tsx](DetailPanel.tsx) |
| The API literal belongs to the fetch helper, not this panel; the panel consumes `fetchTaskDocument`. | L10-L17 | [taskDocuments.ts](../data/taskDocuments.ts) |
| Component regressions pin body merge, fallback visibility, and single rendering of implementation steps. | L650-L865 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| DetailPanel resolves typed taskdoc/series/lifecycle selections before rendering by task-document `kind`. | L305-L361; L496-L508 | [DetailPanel.tsx](DetailPanel.tsx) |
| Typed Operations selection helpers shared with Cockpit and LifecycleList. | L1-L76 | [taskIdentity.ts](../data/taskIdentity.ts) |
| Selected series masters render directly from `analytics.series` by direct `seriesId` selection or by a selected root-task lifecycle whose enclosure `taskId`/`taskName` maps to the folder-keyed series, adapting a `SeriesNode` to the master overview shape and pairing only sibling slice docs. | L305-L361; L382-L452; L496-L506; L563-L571 | [DetailPanel.tsx](DetailPanel.tsx) |
| Lifecycle-bound selected masters render `MasterOverview` with sibling docs from the full projected task-document pool, so master rows can open authored leaves that are not sidebar rows. | L435-L440; L496-L508; L539-L552; L677-L740 | [DetailPanel.tsx](DetailPanel.tsx) |
| Direct taskdoc and active lifecycle leaf selections use `parentTaskLinkForDoc` to show a sticky parent/root backlink without changing leaf content selection. | L337-L361; L453-L487 | [DetailPanel.tsx](DetailPanel.tsx) |
| `displayedLeafDoc` resolves the leaf actually on screen (mirroring the render branches; `undefined` for a master/series overview) and `onViewLeaf` reports its `qualifiedLeafKey` up via effect (L5 fix 1). | L373-L389; L771-L818 | [DetailPanel.tsx](DetailPanel.tsx) |
| The task reader wraps rendered leaf content in `data-task-leaf-key={qualifiedLeafKey(doc)}` so selection capture can attribute highlighted text to the displayed leaf. | — | [DetailPanel.tsx](DetailPanel.tsx) |
| The shared hierarchy helper resolves parent task links from projected series sub-task refs and typed selection keys. | L45-L58; L85-L88 | [taskHierarchy.ts](../data/taskHierarchy.ts) |
| The enclosure-opened leaf backlink regression proves the parent link targets the parent master task document. | L766-L778 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| `topLevelStepProgress` derives user-facing progress from top-level `doc.steps`, and the master sub-task index, master-less slice list, and reader `ProgressFill` consume it. | L553-L556; L699-L707; L780-L795; L833-L846 | [DetailPanel.tsx](DetailPanel.tsx) |
| Master leaf rows sort by structured `createdAt` only when all rows have it, then display the matched child task document `id` while keeping row position separate for test ids. | L717-L785 | [DetailPanel.tsx](DetailPanel.tsx) |
| The task reader now renders top progress before Objective while retaining the implementation-step copy later in the document. | L833-L866 | [DetailPanel.tsx](DetailPanel.tsx) |
| The master reader maps `SeriesNode.seriesTokenTotal` onto concrete/folder-keyed master views and renders the aggregate series-token scalar. | L592-L620; L652-L705 | [DetailPanel.tsx](DetailPanel.tsx) |
| The `SeriesNode`, `TaskDocNode.createdAt`, and sub-task `createdAt` contract fields consumed by this panel are mirrored in the dashboard projection types. | L196-L250; L375-L386 | [types/projection.ts](../types/projection.ts) |
| Lifecycle-visible identity helpers used to label promoted leaf lifecycles without changing task-document filtering. | L1-L63 | [taskIdentity.ts](../data/taskIdentity.ts) |
| The durable gate responder, now rendered only for real `activeLifecycle.gate` requests. | L1-L124 | [GateResponder.tsx](GateResponder.tsx) |
| The markdown renderer for task prose / master sections / bullets / decisions (6g). | L1-L84 | [grammar/Markdown.tsx](../grammar/Markdown.tsx) |
| `ProgressFill` + `TokenGauge` grammar it composes. | L1-L58 | [grammar/overview.md](../grammar/overview.md) |
| The shared empty-state backdrop the no-selection state renders. | L1-L64 | [EmptyStateBackdrop.tsx](EmptyStateBackdrop.tsx) |

## Update History

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
- 2026-06-18T15:00 — Task 6 slice 6c Part B: the display-only gate banner became the **Gate Review drawer** — `GateReview` POSTs `lifecycle.gate.decisions` to `/api/actions` via `data/actions.postGateDecision`, with honest status; the `ask` proto-gate falls back to the display banner. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda css/cva; `badge`/`laneMeta`
  localized (their source panels' classes were removed). Verification metadata pinned until closeout
  stamps the 5d code commit.
