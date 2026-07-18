# dashboard/src/data/taskIdentity.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/taskIdentity.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

`taskIdentity.ts` centralizes display identity helpers and Operations selection identity for dashboard
task rows, detail headers, and lifecycle-attached Event River rows. It lets promoted leaf lifecycles
show the human task/worktree leaf name, lets lifecycle-only history rows fall back to projected task
document titles, keeps stable lifecycle ids available, and defines typed selection namespaces so task
documents, series masters, and runtime-only lifecycles are not guessed from one overloaded string.
Slice L5 adds the **leaf-key identity** the sidebar chat is keyed on: helpers that derive a durable
qualified leaf id (`repo/master/leaf-id`) from the open task doc — not the enclosure — so a chat⇄leaf
binding resolves with no live worktree and after finalize.

## Code Commentary

### Logic

`taskDocSelectionKey`, `seriesSelectionKey`, and `lifecycleSelectionKey` create explicit Operations
selection keys (`taskdoc:<docPath>`, `series:<seriesId>`, `lifecycle:<id>`). `parseTaskSelection`
parses those keys and accepts older raw lifecycle ids / series ids only as a compatibility bridge for
surfaces that still emit raw ids. `lifecycleIdForSelection` derives the selected lifecycle for chats
and highlight context from either a lifecycle key or a task-document key whose projected document has
`lifecycleId`.

The slice-L5 leaf-key helpers sit beside the selection helpers. `qualifiedLeafKey(doc)` builds the
durable `repo/master/leaf-id` from a `Pick<TaskDocNode, "repository" | "docPath" | "id">`, where
`master` is the basename of the doc's directory (the series/contract folder) and the leaf is the doc id;
it returns `undefined` when any part is missing (a master-less / pathless doc). `leafKeyForSelection`
mirrors `lifecycleIdForSelection`: from the **open task doc** behind a `taskdoc`/`lifecycle` selection it
resolves the leaf key (a `series` selection has no single leaf → `undefined`). **L5 fix 1 superseded
`leafKeyForSelection`:** the rail chat now keys off the leaf the detail panel is actually *displaying*
(reported up via `DetailPanel.onViewLeaf` → `Cockpit`'s `viewedLeafKey`), because the top-level selection
is the master and a drilled sub-task shows a different leaf. `leafKeyForSelection` remains exported in this
file but **has no live caller** — left in place rather than deleted. `leafTitleForKey(taskDocuments,
leafKey)` resolves the bound leaf's display title (the matching doc's `title`, else `undefined`), and
`leafIdFromKey(leafKey)` returns the last path segment — the name-label fallback when no doc title resolves.
Both stay in use (the Chats page / `SessionList` / `RailChat`), as does `qualifiedLeafKey`, which
`DetailPanel` now calls directly on the displayed leaf doc.

`groupEnclosuresByLifecycle` builds a `lifecycleId -> EnclosureNode` lookup from projected enclosures.
`findLifecycleEnclosure` first respects `lifecycle.enclosure` when the lifecycle already points at a
known enclosure id, then falls back to the lifecycle-id lookup for promoted lifecycles whose durable
record has not carried the enclosure path in the same shape. `taskLabel` chooses a visible name:
master/task rows keep `taskName` when the lifecycle id is already the task id/name or multiple direct
docs are attached, while concrete leaf rows prefer `leafId`, then `enclosureId`, then task name, then
a direct task-document label. `taskDocumentLabel` chooses the master document title, then a single
direct document title, then the supplied fallback; `taskDocsForLifecycle` deliberately filters only
`TaskDocNode.lifecycleId === lifecycle.id`.

### Conventions

The helpers are pure and are shared by `Cockpit`, `LifecycleList`, and `DetailPanel` so the Operations
list, detail header, and chat/highlight lifecycle binding agree on selection identity. They do not read
the store directly.

### Invariants And Boundaries

- Visible names may come from enclosure metadata or directly attached task documents, but task-reader
  content must come from `analytics.taskDocuments`.
- The helpers never rewrite lifecycle ids or mutate projection state; they only choose labels and direct
  document matches for rendering.
- There is no parent/master fallback and no `series-contract.md` fallback in `taskDocsForLifecycle`.
- Parent `taskName` may label runtime context but must not select leaf task content. Typed selection
  keys are the boundary that prevents that regression.
- The leaf key is derived from the **task doc**, never the enclosure, so it is stable across worktree
  lifetime (no worktree, post-finalize). It is opaque downstream — `data/sessions` + the serving catalog
  treat it as a registry key, never parsing it.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Typed Operations keys and selection parsing live beside lifecycle/enclosure identity helpers. | L17-L45 | [taskIdentity.ts](agents-remember/dashboard/src/data/taskIdentity.ts) |
| Lifecycle labels prefer enclosure metadata when present and fall back through direct task-document titles before raw ids. | L77-L108 | [taskIdentity.ts](agents-remember/dashboard/src/data/taskIdentity.ts) |
| The Operations list creates `taskdoc:` / `series:` / `lifecycle:` row keys from these helpers. | — | [LifecycleList.tsx](agents-remember/dashboard/src/panels/LifecycleList.tsx) |
| The detail panel resolves the selected entity with `parseTaskSelection` before rendering by document kind. | — | [DetailPanel.tsx](agents-remember/dashboard/src/panels/DetailPanel.tsx) |
| Cockpit derives the chat/highlight lifecycle attachment through `lifecycleIdForSelection`; the rail-chat leaf key now comes from `DetailPanel.onViewLeaf` (via `qualifiedLeafKey`), superseding `leafKeyForSelection` (still exported here, no live caller). | — | [Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The session store binds the qualified `leafKey` these helpers mint, and `Chats`/`SessionList`/`RailChat` resolve leaf names via `leafTitleForKey` / `leafIdFromKey`. | — | [sessions.ts](agents-remember/dashboard/src/data/sessions.ts) |
| Event River imports `taskDocumentLabel` so history rows without live lifecycle projection can still render the task document title. | L1-L15; L296-L331 | [eventSummary.ts](agents-remember/dashboard/src/panels/eventSummary.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-30T00:00:00+02:00 — L5 follow-up: noted that `leafKeyForSelection` is now **superseded/unused** — the rail chat
  keys off the leaf the detail panel is *displaying* (`DetailPanel.onViewLeaf` → `Cockpit.viewedLeafKey`,
  which calls `qualifiedLeafKey` on the displayed leaf doc), not the top-level (master) selection. The
  helper is left exported in this file with no live caller; `qualifiedLeafKey` / `leafTitleForKey` /
  `leafIdFromKey` stay in use. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added the leaf-key identity helpers — `qualifiedLeafKey(doc)` (durable
  `repo/master/leaf-id` from the task doc, master = the doc's parent folder basename), `leafKeyForSelection`
  (the open task doc's leaf key for a taskdoc/lifecycle selection, mirroring `lifecycleIdForSelection`),
  `leafTitleForKey` (bound-leaf display title), and `leafIdFromKey` (leaf-id fallback). These key the
  sidebar chat's chat⇄leaf binding; derived from the doc, not the enclosure, so they survive finalize.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-26T19:40+02:00 — Task 20 lifecycle label follow-up: added the shared
  `taskDocumentLabel` helper so lifecycle-visible rows can use projected task
  document titles when enclosure/lifecycle projection metadata is unavailable,
  instead of falling back straight to cryptic lifecycle ids. Verification
  metadata pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first Operations: added typed selection helpers for
  `taskdoc:`, `series:`, and `lifecycle:` keys plus lifecycle extraction for task-document selections,
  replacing parent/task-name inference at the selection boundary. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Created for the promoted leaf identity correction: centralizes enclosure
  label lookup and direct lifecycle task-document filtering so UI labels do not become a contract-content
  fallback. Verification metadata pinned until closeout stamps the code commit.
