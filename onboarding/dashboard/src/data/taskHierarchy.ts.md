# dashboard/src/data/taskHierarchy.ts

## Governing Overview

[data overview](overview.md)

## Purpose

`taskHierarchy.ts` centralizes the task-document hierarchy joins that are shared by Operations and
Detail. It resolves a leaf `TaskDocNode` back to the structured parent `SeriesNode.subTasks` row,
uses creation order for placement while preserving the leaf document's own task `id` for display,
builds parent selection keys, and exposes path helpers used for task-document/enclosure matching.
Since 260703-L14 it also owns the **orchestration-command relation**: an orchestration task is a
`kind:"master"` doc carrying a non-empty top-level `orchestrates` list (the owner data-model ruling
— no new task kind), and `LifecycleList` uses these helpers to derive the current Operations command
tiers and parent rows. The retired Chats grouping modules no longer consume this relation; the Chats
session rail derives its role hierarchy through `railModel.ts` instead.

## Code Commentary

### Logic

`findParentTaskMatch` skips master docs, walks projected series masters, orders each series' `subTasks`
by structured `createdAt` when all rows provide it, and matches a sub-task ref's declared `file` against
the leaf document path. The returned `number` is `doc.id` for an authored leaf task document and falls
back to the matched ref's `number` only for rows without a projected child doc, while the ordered ref
list still decides where the row appears. Operations can therefore show the leaf task's own number
without parsing numbers from filenames, slugs, titles, or parent labels.

`ParentTaskMatch.ref` is typed `SeriesSubTaskNode`, not `TaskSubTaskRefNode`. Those are two distinct
`extra="forbid"` server models that the mirror once collapsed into one interface; the match is always
read off `series.subTasks`, so it is a SERIES row — it carries `createdAt` and can never carry the
cross-series `linkedLifecycleId` that only a master's own `subTasks` rows use.

`orderedByCreation` is exported. It was file-private here while `DetailPanel.tsx` held a
byte-identical second copy; the copy is gone and the panel imports this one. Within the panel the
call also moved from `SubTaskIndex` (which renders the `SubTaskRow` union and so could never sort a
master's rows, because `TaskSubTaskRefNode` declares no `createdAt` at all) to `seriesAsMasterDoc`,
the only call site whose rows actually carry the field.

The L14 helper block: `isOrchestrationDoc(doc)` is `kind === "master"` with a non-empty
`orchestrates`; `masterCommandNames(doc)` returns the names a master answers to when matched against
an `orchestrates` list — its task folder (the durable series key, `basename(pathDir(docPath))`), its
doc `id`, and its `title` (forgiving but exact-string); `orchestratorParentKey(names, docs,
selfDocPath?)` finds the first orchestration doc whose list names any of them and returns its
`taskdoc:` selection key — a doc never commands itself (`selfDocPath` is excluded), and masters named
nowhere return `undefined` (top-level exactly as today, the D3 rule).

`taskDocHierarchyLabel` prepends that task-document number to the leaf title when a parent match exists.
`taskDocParentKey` and `parentTaskLinkForDoc` choose the parent navigation target as a typed
`taskdoc:<docPath>` key when the parent master document is projected, otherwise as a typed
`series:<seriesId>` fallback. `pathDir`, `pathStem`, and `stripExt` are small path-shape helpers for the
dashboard's projected POSIX-like task paths.

### Conventions

The helper is pure and store-free. It uses existing typed selection-key helpers from `taskIdentity.ts`
instead of duplicating selection prefixes.

### Invariants And Boundaries

- Authored leaf display numbers come from `TaskDocNode.id`; the parent series' sub-task ref
  (`SeriesSubTaskNode`) `number` is only a fallback for rows without a projected child doc. Creation
  order only controls row placement. Do not derive display numbers from task-name, slug, filename,
  path prefixes, parent label strings, or local indexes.
- The helper resolves parent navigation only from projected task/series metadata; it does not read the
  filesystem or contracts.
- Missing `createdAt` preserves authored sub-task order rather than guessing a different order —
  `orderedByCreation` reorders only when EVERY row carries the field, so a partially stamped list is
  left alone instead of sorting the stamped rows to the front. A row type that declares no
  `createdAt` therefore passes through untouched by construction, and
  `snapshots.py::_series_subtask_nodes` has already applied the same rule server-side, which makes
  this an order-preserving safety net rather than the thing that establishes the order.
- The orchestration-command match (L14) is exact-string over declared names only (folder / doc id /
  title); no fuzzy matching, no title parsing, and never self-command. A doc without `orchestrates`
  participates in no command relation.

### Todos

No standing todos.

### 2026-07-24 Curator Delta

Parent task lookup now builds one weakly cached normalized-reference index per series-list identity.
It preserves the established first-series and creation-order precedence while avoiding repeated
sort-and-normalize scans for every task row.

## Evidence

### Docs References

No relevant external documentation found; this file implements same-repository task projection
semantics.

No external documentation is required for this local task hierarchy helper.

### Repo-Internal References

The helper is consumed by the Operations list and detail panel to keep sidebar numbering and parent
navigation aligned with the master task reader.

- The helper finds a parent series ref, keeps the authored child task id as the display number, builds hierarchy labels, and returns parent navigation keys. [1]
- The L14 orchestration-command helpers are consumed by Operations `LifecycleList` for command tiers and parent rows. [2]
- The current Chats session hierarchy is independently derived by `railModel`, not the retired `groupSessions` consumer. [3]
- The task document mirror provides the required orchestrates list these helpers read. [4]
- The task-doc master reference is distinct from a series row and may carry linkedLifecycleId. [5]
- ParentTaskMatch uses the series-row model, which can carry createdAt. [6]
- `orderedByCreation` is exported here and shared with `DetailPanel`'s `seriesAsMasterDoc`, which replaced the panel's byte-identical private copy. [7]
- Operations uses the helper for numbered task labels, parent row keys, and BY REPO hierarchy rendering. [8]
- DetailPanel uses the helper to render a parent link for directly opened leaf task documents and active leaf lifecycle documents. [9]
- Focused tests cover BY REPO hierarchy nesting/indentation and numbered leaf labels; the enclosure-opened leaf parent link is pinned in the DetailPanel suite. [10]
- The enclosure-opened leaf's parent-task link case. [11]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is involved.
