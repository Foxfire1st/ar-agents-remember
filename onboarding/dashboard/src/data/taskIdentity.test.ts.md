# dashboard/src/data/taskIdentity.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The unit source covers only `masterFolderForSelection` from `taskIdentity.ts`. Its single case resolves the master folder `ops` from the selected task-document key. It no longer declares nested/orphan tree or pre-drill path tests.

## Code Commentary

A local `doc(partial)` passes typed overrides to the shared `taskDoc` builder rather than casting past `TaskDocNode`. The case places a sub-task under `/tasks/repo/ops/05.json`, supplies `analytics({taskDocuments: docs})` and asserts the resolved folder. Shared builders supply their retained served-base fields. This is a pure function assertion, with no DOM, store, backend or execution claimed by this card. `buildTaskTree` and `findMasterPath` are not imported or tested.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The retained single assertion resolves the selected task document to its master folder; no tree or pre-drill cases remain. [1]
- The test file's `doc` fixture helper. [3]
- Typed taskDoc and analytics builders supply the retained served-base fields rather than casts. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
