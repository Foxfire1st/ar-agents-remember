# dashboard/src/panels/session-cockpit/ChatContextBar.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatContextBar.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Pins lifecycle-routing honesty and server-first leaf attachment for the canonical Chats duty bar.

## Code Commentary

### FEUI MX-FIX-2 Raw Caller Matrix

The suite proves one accepted raw response creates and focuses the exact server id once. A network
failure and the Round 1 contradictory raw harness/control response both render their typed alerts,
leave the registry empty, and never invoke the focus callback.

Tests distinguish the explicitly local lifecycle patch from leaf authority, prove successful leaf
move sends the exact route/body and broadcasts invalidation, and prove a 409 same-role refusal leaves
the local row unchanged while surfacing an alert.

### Logic

The suite drives the raw create control through the real session store with request-matched
`Response` fixtures, then observes registry rows, alert copy, and the `onSessionOpened` callback. Leaf
attach/move cases use URL-aware fetch fixtures and broadcast doubles.

### Conventions

Stable `data-testid` seams locate the raw control and alert. Store and global transport state are
reset between cases so exact-one focus and zero-ghost assertions remain isolated.

### Invariants And Boundaries

Only an accepted server id may reach the focus callback. Network, protocol, and same-role attach
failure must leave the prior registry/focus state unchanged and visible to the operator.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Cross-Repo References

The suite exercises repository-local routing and browser broadcast doubles; no cross-repository source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Unit under test. | `ChatContextBar` | dashboard/src/panels/session-cockpit/ChatContextBar.tsx:74-117 |
| The typed `taskDoc` builder `leafDoc()` now returns, replacing an `as unknown as TaskDocNode` cast. | `taskDoc` | dashboard/src/test/fixtures/wire.ts:282-287 |
| `buildTaskTree` — the only consumer of the seeded doc, and the reason the richer base changes nothing. | `buildTaskTree` | dashboard/src/data/taskIdentity.ts:208-214 |

## Current L5I Maintenance

The context-bar suite now pins the split between persistent launch controls and stage-header session
actions, including history availability and the server-first leaf assignment path.

## Update History

- 2026-08-03T09:40+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 4 citation findings (1 missing anchor, 1 malformed source, and 2 prose citations) for the assigned component and task-identity references; all ranges were independently checked against the frozen source index.

- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **corrected the `buildTaskTree`
  field enumeration in the 11:05 entry below, which was incomplete in the one place that mattered.**
  It said `buildTaskTree` "reads only `kind`, `docPath`, `title`, `lifecycleId` and
  `masterLifecycleId`". Read end to end from the working tree, `data/taskIdentity.ts` L126-L165 reads
  those five directly (`doc.kind` L131/L152, `masterFolderOf(doc)` → `doc.docPath` L132/L157,
  `doc.title` L134/L155, `doc.lifecycleId` L137, `doc.masterLifecycleId` L142/L158) **and two more
  through `qualifiedLeafKey`**, which it calls at L153 for every leaf: that function is declared
  `Pick<TaskDocNode, "repository" | "docPath" | "id">` (cit:([`qualifiedLeafKey`], dashboard/src/data/taskIdentity.ts:64-70)) and reads `doc.repository` and
  `doc.id` at L67-L69. Seven fields, not five. The entry's conclusion survives — `leafDoc()` still
  passes `id: "260628-L5"` and `repository: "agents-remember"` explicitly, so the leaf key is
  unchanged — but the omission mattered: `repository` and `id` are exactly the two fields
  `BASE_TASK_DOC` *does* supply from `snapshot.json` (`repository: SERVED_TASK_DOC.repository`,
  `id: SERVED_TASK_DOC.id`, wire.ts), so the "the base supplies nothing this path reads" argument was
  resting on an enumeration that had dropped them. Recorded the corrected reasoning inline. No
  reference rows changed; the two added at 11:05 are correct, and this table is two-column.
  Verification metadata untouched.

- 2026-08-01T11:05+02:00 — 260731-EFA-L4 curator: **No content impact:** the only source change is
  `leafDoc()` returning `taskDoc({…})` from `test/fixtures/wire.ts` instead of an
  `{…} as unknown as TaskDocNode` cast, and every behavioural claim above is about raw-create
  responses, alert copy, focus, and leaf attach/move routing — none of which reads a task-document
  field. I checked the one place that does rather than assuming: `ChatContextBar.tsx` L140 passes
  `taskDocuments` into `buildTaskTree` and nothing else, and `buildTaskTree`
  (cit:([`buildTaskTree`], dashboard/src/data/taskIdentity.ts:208-214)) reads **seven** fields: `kind`, `docPath`, `title`, `lifecycleId`
  and `masterLifecycleId` directly, plus `repository` and `id` through `qualifiedLeafKey` (L64-L70,
  whose parameter is `Pick<TaskDocNode, "repository" | "docPath" | "id">`), which it calls at L153 to
  key every leaf node. All of `kind`, `docPath`, `title`, `repository` and `id` were already set by
  the old literal and are still passed explicitly by `leafDoc()`, and `lifecycleId`/`masterLifecycleId`
  are OPTIONAL, so `BASE_TASK_DOC` — which carries required fields only — does not supply them; the
  tree is built from exactly the same inputs as before. `repository` and `id` are the two that make
  this worth checking rather than asserting: `BASE_TASK_DOC` **does** carry both
  (`repository: SERVED_TASK_DOC.repository`, `id: SERVED_TASK_DOC.id`, drawn from `snapshot.json`), so
  had `leafDoc()` stopped overriding them the builder would have silently swapped a snapshot value into
  the leaf key the suite asserts as `LEAF_KEY`. It still overrides both. The dozen required fields the base did add
  (`status`, `stepsDone`, `stepsTotal`, `steps`, `objective`, `requirements`, `codeExamples`,
  `decisions`, `openQuestions`, `references`, `subTasks`, `sections`) have no reader on this path.
  Suite re-run: all cases pass. Two reference rows added; the `Repo-Internal References` table here is
  two-column, so both new rows carry two cells.

- 2026-07-24T13:17:17Z — Curator: recorded launch/action ownership regression coverage;
  verification fields remain pre-commit.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: added exact-one accepted raw focus plus network and
  contradictory-authority failure regressions with zero row and zero focus. Verification metadata
  remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 Chats duty-bar regressions; verification metadata
  remains blank until commit.
