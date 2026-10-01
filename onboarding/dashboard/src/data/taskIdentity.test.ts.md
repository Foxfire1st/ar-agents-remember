# dashboard/src/data/taskIdentity.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test (the `buildTaskTree` / `findMasterPath` / `masterFolderForSelection` helpers). [1]
- The leaf-key composer the assertions read through: `repository` + docPath folder + `id`, nothing else. [2]
- The test file's `doc` fixture helper. [3]
- The `taskDoc` / `analytics` builders and the thirteen-key `EMPTY_ANALYTICS` base. [4]
- ChatSessionActions derives its task tree from taskDocuments. [5]
- ChatSessionActions renders LeafAttachPicker. [6]
- LeafAttachPicker pre-drills to the context master with findMasterPath. [7]
- Master rows drill further through drillInto. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
