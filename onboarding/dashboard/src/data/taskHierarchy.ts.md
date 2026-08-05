# dashboard/src/data/taskHierarchy.ts

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `dashboard/src/data/taskHierarchy.ts`     |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated | 2026-08-01T09:05+02:00 |
| lastVerifiedCommitHash |                                           `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |                                           2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No relevant external documentation found; this file implements same-repository task projection
semantics.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for this local task hierarchy helper. | — | — |

## Repo-Internal References

The helper is consumed by the Operations list and detail panel to keep sidebar numbering and parent
navigation aligned with the master task reader.

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper finds a parent series ref, keeps the authored child task id as the display number, builds hierarchy labels, and returns parent navigation keys. | "export function findParentTaskMatch" | dashboard/src/data/taskHierarchy.ts:43-43 |
| The L14 orchestration-command helpers are consumed by Operations `LifecycleList` for command tiers and parent rows. | "export function taskDocHierarchyLabel", "export const LifecycleList" | dashboard/src/data/taskHierarchy.ts:53-53; dashboard/src/panels/LifecycleList.tsx:425-425 |
| The current Chats session hierarchy is independently derived by `railModel`, not the retired `groupSessions` consumer. | "export function buildRailModel" | dashboard/src/data/railModel.ts:131-131 |
| The `TaskDocNode.orchestrates?` mirror these helpers read, and the two distinct sub-task row models `ParentTaskMatch.ref` had to choose between. | `TaskDocNode`; `TaskSubTaskRefNode`; `SeriesSubTaskNode` | dashboard/src/types/projection.ts:369-376; dashboard/src/types/projection.ts:437-463; dashboard/src/types/projection.ts:494-501; dashboard/src/types/projection.ts:484-491 |
| `orderedByCreation` is exported here and shared with `DetailPanel`'s `seriesAsMasterDoc`, which replaced the panel's byte-identical private copy. | "export function taskDocParentKey", "export const DetailPanel" | dashboard/src/data/taskHierarchy.ts:58-58; dashboard/src/panels/DetailPanel.tsx:723-723 |
| Operations uses the helper for numbered task labels, parent row keys, and BY REPO hierarchy rendering. | "export const LifecycleList" | dashboard/src/panels/LifecycleList.tsx:425-425 |
| DetailPanel uses the helper to render a parent link for directly opened leaf task documents and active leaf lifecycle documents. | "export const DetailPanel" | dashboard/src/panels/DetailPanel.tsx:723-723 |
| Focused tests cover BY REPO hierarchy nesting/indentation and numbered leaf labels; the enclosure-opened leaf parent link is pinned in the DetailPanel suite. | "limits sidebar rows to root docs" | dashboard/src/panels/LifecycleList.test.tsx:234-366 |
| The enclosure-opened leaf's parent-task link case. | "renders the gate respond drawer with the full request packet" | dashboard/src/panels/DetailPanel.test.tsx:439-447 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is involved. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and converted the history projection citation; exact non-fixing check returns zero
  findings.

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: recorded the two real changes in this file's diff
  against `abc7cbc`. (1) `ParentTaskMatch.ref` is now `SeriesSubTaskNode` — the mirror split the
  once-collapsed `TaskSubTaskRefNode`/`SeriesSubTaskNode` pair cit:(["export interface TaskSubTaskRefNode"], dashboard/src/types/projection.ts:494-494),
  and `createdAt` was REMOVED from the master row model, so the match's row type is now the only one
  that declares the field the helper sorts on. (2) `orderedByCreation` is exported and shared:
  `DetailPanel.tsx` deleted its byte-identical private copy, and inside the panel the call moved
  from `SubTaskIndex` (union rows, could never sort) to `seriesAsMasterDoc`. Corrected the
  "master sub-task ref" wording in the invariants and spelled out the all-or-nothing rule plus the
  `snapshots.py::_series_subtask_nodes` server-side ordering it backstops. Re-anchored every drifted
  citation: helper block L15-L58/L73-L88 → L4-L10/L43-L82 (now contains `ParentTaskMatch`,
  `findParentTaskMatch`, `taskDocHierarchyLabel`, `taskDocParentKey`, `parentTaskLinkForDoc`); the
  L14 block L68-L99 → L84-L122 (`L68-L99` stopped short of `orchestratorParentKey` at L109);
  `LifecycleList.tsx` L252-L312 → L582-L631 (the old range named nothing — `taskDocHierarchyLabel`
  is L592, `taskDocParentKey` L627); `DetailPanel.tsx` L337-L361/L453-L487 → L408-L412/L561-L566
  (`parentTaskLinkForDoc` is called at L411 and L564, in neither old range); `LifecycleList.test.tsx`
  L129-L257/L766-L778 → the hierarchy fixture + numbered-leaf + disclosure cases, and moved the
  enclosure-opened parent-link claim onto `DetailPanel.test.tsx` L1057-L1066, where that test
  actually lives.

- 2026-07-24T13:17:50Z — Added cached parent-task index semantics. Verification hash/date remain
  pinned to the pre-commit source stamp.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: restricted the orchestration-command helpers' current
  consumer to Operations `LifecycleList` and recorded `railModel` as the separate canonical Chats
  hierarchy owner; retired `groupSessions` is historical only. Verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-06T23:57:06+02:00 — 260703-L14 (visual hierarchy + chat grouping): added the
  orchestration-command helpers — `isOrchestrationDoc`, `masterCommandNames` (folder / doc id /
  title), and `orchestratorParentKey` (exact-string match, never self, `undefined` when unnamed) —
  shared by the tasks-tab tier derivation and the Chats command tree. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-24T18:11+02:00 — Corrected Task 17 live-data numbering: parent sub-task refs may carry
  display labels in `number`, so authored leaf hierarchy labels now use `TaskDocNode.id` and keep
  `ref.number` only as the unauthored-row fallback. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T18:02+02:00 — Corrected Task 17 leaf numbering: `findParentTaskMatch` still orders refs by
  structured creation metadata for placement, but labels now use structured task metadata instead of a
  generated row counter. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Created for the Task 17 Operations hierarchy follow-up: centralizes parent
  task matching, parent selection keys, and task path helpers so
  `LifecycleList` and `DetailPanel` do not reimplement the hierarchy join. Verification metadata will
  be stamped after the first code commit containing this new file.
