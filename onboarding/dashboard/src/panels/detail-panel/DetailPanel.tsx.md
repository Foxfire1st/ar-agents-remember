# dashboard/src/panels/detail-panel/DetailPanel.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Canonical memoized Operations detail entry. It composes selection/body state, lifecycle spine and
explicit durable gates with one fixed sprint/master/task document reader, without making runtime
identity, page appearance or reader-local state a competing task authority.

## Code Commentary

### Composition and selection

The original monolith was split by responsibility: state.ts owns selection/body state, model.ts pure
derivation, taskDocPanels.tsx panel variants, lifecycleBody.tsx runtime spine and taskReader.tsx form
composition. The fixed-page head, blocks, own views, index groups and styles have separate owners
(docHead, taskBlocks, skeletons, docViews, task-groups, pageParts/pageStyles). The shared Panel remains
unchanged. A selected document has exactly one in-page ID/title; sticky Panel chrome keeps Back/parent
navigation, not a duplicate title or ProgressFill header.

parseTaskSelection distinguishes taskdoc, series and lifecycle keys, with the shared raw-ID bridge.
A document can render without a lifecycle; attaching one adds only its runtime/enclosure/provider/gate
context. Direct and lifecycle-resolved documents dispatch sprint/master/task by docForm, including
the model-rule fallback for an older projection. Series selection uses its real projected document
when available and only then seriesAsMasterDoc. An opened slice wins before the overview.

A root task lifecycle can identify a folder-keyed series by its own enclosure identity. A leaf's
parent taskName is NEVER its content selector: its body is the TaskDocNode whose lifecycleId matches
that leaf. Parent/up links are navigation metadata and must not alter the leaf selector. The full
projected sibling pool resolves authored leaves even when they are absent from the sidebar. Qualified
displayedLeafDoc attribution follows the actual render branches and the reader's task-leaf wrapper,
not the sidebar row alone; a master/series overview has no displayed leaf key.

### Durable hierarchy, progress and navigation

Task-master and series sub-task rows are distinct extra-forbid server models. Their union preserves
linkedLifecycleId/masterRef versus optional createdAt; do not widen it back to TaskDocNode.subTasks.
Master task rows keep received order and display the matched child's authored ID/title, falling back
to parent ref values only when unresolved. One-based positions are test/navigation identities, not
invented visible task numbers. Creation ordering belongs to the series adapter and master-less slice
fallback; missing creation times preserve authored order. Commanded-master targets resolve across
the full qualified document pool, then linked series or authored local slices; an unresolved target
stays visible/inert rather than vanishing.

Progress facts use projected stepsDone/stepsTotal, never a second count of a visible slice. Task steps
now have one table with marks/counts and their body content; index rows use StepMarks/ProgressBar as
appropriate. The standalone grammar ProgressFill still exists for other consumers but is not a
second task-page header. Structured step/code IDs compose with titles at render time rather than
being inserted into stored title strings. No aggregate lifecycle or series token figure is rendered.

### Body first and read-only artifacts

useDetailPanelState resolves the visible document and useTaskDocumentBody fetches its full body by
stable path/revision. Available summary content remains visible while loading, with the explicit
loading notice; unavailable full content retains the summary/failure notice. Current summary identity,
status, progress, step state and review aggregates remain authoritative. A matching revision can
restore longer marked previews/full collections without a stale body replacing current facts.
Ancillary Notes, references/reports and reader/spine change-set counters mount after body loading
settles, for both available and unavailable outcomes; their eager effects must not occupy its first
request slot. Requirement links retain the shared repository/task-qualified provider on every form.

The shared kind-tagged TaskArtifactReaderTarget carries notes, requirement packets and recorded task
reports through onOpenNotes into the existing reader takeover. The page reads no note tree/content:
its single Notes line uses the root count. Task reports use the path inside the task root, not the
physical projected filesystem path. Document-local own-view/expansion state resets on a different
docIdentity and persists on a same-document refresh; own-view Back restores its captured scroll owner.

ChangeSetBar retains the master net with includeLeaves:true and its own leaf attribution, not a fake
zero when breakdown is absent. Leaf working and single Intent review controls retain their own owners,
brief states/disclosures and task-context targets. Lifecycle GateResponder is durable-gates-only:
ask-only conversation belongs to the adjacent native leaf chat, never a task-local response box.
Spine lanes remain read-only joins of enclosure/worktree/provider facts, not command authority.
The no-selection Panel retains EmptyStateBackdrop and its existing effects/motion gating. Memoization
skips unchanged persistent selections but allows actual store/selection changes.

## Boundaries

Read-only navigation, hydration and projection display confer no authoring, review, landing or
lifecycle authority. Task JSON/qualified references remain the structural source of truth; the
reader never steals a leaf's parent content. The fixed form order deliberately supersedes the old
ad-hoc body/duplicate-header composition while preserving requirement links, Notes transport,
discard-before-start audit, progress ownership, durable gates and runtime spine separation.

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

- The grouped index preserves received order and retains the qualified commanded-master, linked-series and authored-slice navigation guards. [26]

- `parentTaskLinkForDoc` links an enclosure-opened leaf back to its parent task document (`master-parent-link`), pinned by the promotedIdentity suite. [27]
- Task progress forwards the projected done and total counts. [28]

- The master Tasks block renders received sub-task references through the shared grouped rows. [29]

- The master-less slice list sorts task documents and displays their progress. [30]

- Task step progress/count is placed in the Steps table block, not a duplicate ProgressFill page header. [31]

- ProgressFill is the shared progress display primitive. [32]

- Full-index one-based positions stay stable across groups without generating visible task numbers. [33]


- Task row labels prefer matched child ID/title, then the received reference values. [34]


- Each index row uses its full-index position for test identity and the resolved qualified target for navigation. [35]

- The slice list retains createdAt ordering because it operates on task documents. [36]

- The fixed page uses StepsBlock for its table/count; standalone ProgressFill remains a separate grammar primitive, not mounted as a duplicate task-page header. [37]

- SeriesNode provides the series fields and typed sub-task rows consumed by the panel. [39]
- TaskDocNode provides authored task identity, creation time and task-master references. [40]
- Only the series sub-task row has optional createdAt. [41]
- `taskLabel`/`taskDocsForLifecycle`/`taskDocumentLabel` — the lifecycle-visible identity helpers used to label promoted leaf lifecycles without changing task-document filtering. [42]
- The durable gate responder, now rendered only for real `activeLifecycle.gate` requests. [43]

- Shared block text remains Markdown and the relocated decision preview retains newest-authored semantics. [44]

- Standalone `ProgressFill` remains a shared grammar primitive for its existing consumers; the fixed document page no longer mounts it in a second header. [45]
- The shared empty-state backdrop the no-selection state renders. [46]
