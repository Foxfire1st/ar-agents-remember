# dashboard/src/data/taskIdentity.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/taskIdentity.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T09:44+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit tests for the **task-tree** helpers in `taskIdentity.ts` (Operations Integration L5): they pin the
recursive master→…→leaf hierarchy the leaf-attach picker drills. Coverage focuses on the three new
helpers — `buildTaskTree`, `findMasterPath`, and `masterFolderForSelection` — and especially on the
hard case the picker exists for: **a master that is itself a sub-task of another master**, plus orphan
leaves and pre-drill path resolution.

## Code Commentary

### Logic

A terse `doc(partial)` factory builds a `TaskDocNode` from only the fields the tree builder reads
(`kind` / `docPath` / `id` / `repository` / `title` / `lifecycleId` / `masterLifecycleId`). It
delegates to `test/fixtures/wire.ts::taskDoc`, which fills the remaining required fields from the
served row in `fixtures/snapshot.json`; the `as unknown as TaskDocNode` it used to close with is
gone, so each partial is now checked against `types/projection.ts` at the call site instead of
asserted past it. Cases:

- **`buildTaskTree` — nesting.** From an `ops` master, an `L5` sub-task (folder `ops`), a nested `eng`
  master (its `masterLifecycleId` points at the ops lifecycle; its own folder is `engine`), and an `E1`
  sub-task (folder `engine`), it asserts there is exactly **one** root (Operations) with Engine Room
  nested inside it (not a second root); the ops leaf resolves to `repo/ops/L5` and Engine Room's child
  leaf to `repo/engine/E1`. This proves arbitrary nesting via the cross-series `masterLifecycleId` link.
- **`buildTaskTree` — orphan leaf.** A lone sub-task with no matching master node still appears at the
  top level, keyed by its folder, with `leafKey === "repo/ops/L5"`.
- **`findMasterPath`.** Over a two-master tree (ops → nested engine), `findMasterPath(tree, "engine")`
  returns the master chain `["ops", "engine"]` — the path the picker pre-drills along to an in-context
  master.
- **`masterFolderForSelection`.** Given a `taskdoc:` selection key and an analytics bundle holding the
  doc, it resolves the selected doc's master folder (`"ops"`) — the value that drives the picker's
  in-context ordering. The bundle comes from `test/fixtures/wire.ts::analytics`, so it carries all
  thirteen of the reducer's list keys; the literal it replaced declared two of them
  (`taskDocuments`, `series`) and reached the parameter through `as never`, which is a shape the
  server cannot send.

### Conventions

Vanilla function tests — call the pure helper and assert the returned tree/array/string; no renderer, no
store, no DOM. Fixtures are minimal `doc(...)` partials over the shared served builders — the
overrides name only what a case depends on, and the builder supplies the rest as real served values
rather than a cast standing in for them.

### Invariants And Boundaries

Pure logic tests; no React, no backend, no store. They exercise the tree-shape contract
(`buildTaskTree`), the pre-drill path (`findMasterPath`), and selection-folder resolution
(`masterFolderForSelection`) — the leaf-key string helpers (`qualifiedLeafKey` etc.) are exercised
indirectly through the resulting `leafKey` values rather than asserted in isolation here.

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
| The module under test (the `buildTaskTree` / `findMasterPath` / `masterFolderForSelection` helpers). | `buildTaskTree`; `findMasterPath`; `masterFolderForSelection` | [taskIdentity.ts](taskIdentity.ts) |
| The leaf-key composer the assertions read through: `repository` + docPath folder + `id`, nothing else. | `qualifiedLeafKey` | [taskIdentity.ts](taskIdentity.ts) |
| The `doc` factory and the analytics bundle, both now built from the shared served builders. | L7-L12; L60-L64 | [taskIdentity.test.ts](taskIdentity.test.ts) |
| The `taskDoc` / `analytics` builders and the thirteen-key `EMPTY_ANALYTICS` base. | L219-L233; L278-L318 | [../test/fixtures/wire.ts](../test/fixtures/wire.ts) |
| The picker these tree helpers feed (it drills `buildTaskTree`'s output and pre-drills with `findMasterPath`). | — | [panels/LeafAttachPicker.tsx](../panels/LeafAttachPicker.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-08-01T09:44+02:00 — 260731-EFA-L4 curator: the card stated twice that the fixtures are casts —
  "casting via `as unknown as TaskDocNode`" in Logic and "minimal `doc(...)` partials cast to
  `TaskDocNode`" in Conventions — and the diff against `abc7cbc` removed both casts. `doc()` now
  delegates to `test/fixtures/wire.ts::taskDoc` and the `masterFolderForSelection` case builds its
  bundle with `analytics({ taskDocuments: docs })` instead of
  `{ taskDocuments: docs, series: [] } as never`. Corrected both, and named the size of the second
  change: the old literal declared 2 of the reducer's 13 analytics lists, so it stood in for a
  payload the server never sends. Checked that neither change moves an assertion — the `doc`
  overrides still name exactly the seven fields the tree builder reads, everything the builder adds
  (`status`, `stepsDone`/`stepsTotal`, the eight empty lists) is invisible to `buildTaskTree`,
  `findMasterPath` and `qualifiedLeafKey` (which composes `repository`/docPath folder/`id` and
  nothing else), and the eleven analytics lists the bundle gained are all empty, so the
  `folder === "ops"` result is reached the same way. All three case names and both `leafKey`
  expectations are unchanged. Added citations for the factory, the bundle and the builders.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-30T00:00:00+02:00 — Operations Integration L5 (Sidebar chat): created — unit tests for the task-tree helpers:
  `buildTaskTree` nesting a master under another master with leaves under each (and an orphan leaf at the
  top level), `findMasterPath` returning the master chain to a nested master, and
  `masterFolderForSelection` resolving a selected task doc's master folder. Verification metadata pinned
  until closeout stamps the L5 commit.
