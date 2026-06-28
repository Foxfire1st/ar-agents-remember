# dashboard/src/data/taskIdentity.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/taskIdentity.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-26T19:40+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`taskIdentity.ts` centralizes display identity helpers and Operations selection identity for dashboard
task rows, detail headers, and lifecycle-attached Event River rows. It lets promoted leaf lifecycles
show the human task/worktree leaf name, lets lifecycle-only history rows fall back to projected task
document titles, keeps stable lifecycle ids available, and defines typed selection namespaces so task
documents, series masters, and runtime-only lifecycles are not guessed from one overloaded string.

## Code Commentary

### Logic

`taskDocSelectionKey`, `seriesSelectionKey`, and `lifecycleSelectionKey` create explicit Operations
selection keys (`taskdoc:<docPath>`, `series:<seriesId>`, `lifecycle:<id>`). `parseTaskSelection`
parses those keys and accepts older raw lifecycle ids / series ids only as a compatibility bridge for
surfaces that still emit raw ids. `lifecycleIdForSelection` derives the selected lifecycle for chats
and highlight context from either a lifecycle key or a task-document key whose projected document has
`lifecycleId`.

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Typed Operations keys and selection parsing live beside lifecycle/enclosure identity helpers. | L17-L45 | [taskIdentity.ts](agents-remember/dashboard/src/data/taskIdentity.ts) |
| Lifecycle labels prefer enclosure metadata when present and fall back through direct task-document titles before raw ids. | L77-L108 | [taskIdentity.ts](agents-remember/dashboard/src/data/taskIdentity.ts) |
| The Operations list creates `taskdoc:` / `series:` / `lifecycle:` row keys from these helpers. | — | [LifecycleList.tsx](agents-remember/dashboard/src/panels/LifecycleList.tsx) |
| The detail panel resolves the selected entity with `parseTaskSelection` before rendering by document kind. | — | [DetailPanel.tsx](agents-remember/dashboard/src/panels/DetailPanel.tsx) |
| Cockpit derives the chat/highlight lifecycle attachment through `lifecycleIdForSelection`. | — | [Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| Event River imports `taskDocumentLabel` so history rows without live lifecycle projection can still render the task document title. | L1-L15; L296-L331 | [eventSummary.ts](agents-remember/dashboard/src/panels/eventSummary.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

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
