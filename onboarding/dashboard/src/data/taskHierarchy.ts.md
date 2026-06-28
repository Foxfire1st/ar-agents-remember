# dashboard/src/data/taskHierarchy.ts

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `dashboard/src/data/taskHierarchy.ts`     |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated            | 2026-06-24T18:11+02:00                    |
| lastVerifiedCommitHash |                                           `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                           2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                          |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`taskHierarchy.ts` centralizes the task-document hierarchy joins that are shared by Operations and
Detail. It resolves a leaf `TaskDocNode` back to the structured parent `SeriesNode.subTasks` row,
uses creation order for placement while preserving the leaf document's own task `id` for display,
builds parent selection keys, and exposes path helpers used for task-document/enclosure matching.

## Code Commentary

### Logic

`findParentTaskMatch` skips master docs, walks projected series masters, orders each series' `subTasks`
by structured `createdAt` when all rows provide it, and matches a sub-task ref's declared `file` against
the leaf document path. The returned `number` is `doc.id` for an authored leaf task document and falls
back to the matched ref's `number` only for rows without a projected child doc, while the ordered ref
list still decides where the row appears. Operations can therefore show the leaf task's own number
without parsing numbers from filenames, slugs, titles, or parent labels.

`taskDocHierarchyLabel` prepends that task-document number to the leaf title when a parent match exists.
`taskDocParentKey` and `parentTaskLinkForDoc` choose the parent navigation target as a typed
`taskdoc:<docPath>` key when the parent master document is projected, otherwise as a typed
`series:<seriesId>` fallback. `pathDir`, `pathStem`, and `stripExt` are small path-shape helpers for the
dashboard's projected POSIX-like task paths.

### Conventions

The helper is pure and store-free. It uses existing typed selection-key helpers from `taskIdentity.ts`
instead of duplicating selection prefixes.

### Invariants And Boundaries

- Authored leaf display numbers come from `TaskDocNode.id`; the master sub-task ref `number` is only a
  fallback for rows without a projected child doc. Creation order only controls row placement. Do not
  derive display numbers from task-name, slug, filename, path prefixes, parent label strings, or local
  indexes.
- The helper resolves parent navigation only from projected task/series metadata; it does not read the
  filesystem or contracts.
- Missing `createdAt` preserves authored sub-task order rather than guessing a different order.

### Todos

No standing todos.

## Docs References

No relevant external documentation found; this file implements same-repository task projection
semantics.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external documentation is required for this local task hierarchy helper. | — | — |

## Repo-Internal References

The helper is consumed by the Operations list and detail panel to keep sidebar numbering and parent
navigation aligned with the master task reader.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper finds a parent series ref, keeps the authored child task id as the display number, builds hierarchy labels, and returns parent navigation keys. | L15-L58; L73-L88 | [taskHierarchy.ts](taskHierarchy.ts) |
| Operations uses the helper for numbered task labels, parent row keys, and BY REPO hierarchy rendering. | L15-L20; L252-L312; L358-L390 | [LifecycleList.tsx](../panels/LifecycleList.tsx) |
| DetailPanel uses the helper to render a parent link for directly opened leaf task documents and active leaf lifecycle documents. | L337-L361; L453-L487 | [DetailPanel.tsx](../panels/DetailPanel.tsx) |
| Focused tests cover BY REPO hierarchy/indentation, numbered labels, and enclosure-opened leaf parent links. | L129-L257; L766-L778 | [LifecycleList.test.tsx](../panels/LifecycleList.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is involved. | — | — |

## Update History

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
