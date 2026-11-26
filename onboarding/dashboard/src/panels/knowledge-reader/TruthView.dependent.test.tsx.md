# dashboard/src/panels/knowledge-reader/TruthView.dependent.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Unit tests for dependent-record rendering in the Knowledge reader (`TruthView` and `KnowledgeTree`), verifying derived dependent states (`deferred`, `stale`), deferral cards, moved links, and tree navigation under `Records > Dependents`.

## Code Commentary

### Logic

- Uses Vitest and `@testing-library/react` with `readerTestSupport` (`captured`, `open`, `overrides`) and stubbed fetch responses (`dependentRecordAnswer` for `DPD-X6G7K3`); no live browser or backend process runs.
- Verifies that a deferred dependent renders the derived `record-state` badge (`deferred`), leads with `document` in `record-lead`, omits `deferrals` from generic `record-fields` to avoid duplicate display, lists open and orphaned deferrals in `dependent-deferrals` (with owner, age, passage, and condition task/file/note), and renders `dependent-moved-links`.
- Verifies that a non-deferred stale dependent renders `stale`, omits `dependent-deferrals`, and keeps `dependent-moved-links`.
- Verifies that `KnowledgeTree` groups `DPD-*` records under `Records > Dependents` and opens `reader-truth-view` when selected.

## Relationships

- Exercises `dashboard/src/panels/knowledge-reader/TruthView.tsx`, `dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx`, and the dependent view DTOs in `dashboard/src/data/knowledgeReader.ts`.

## Evidence

- The suite builds stubbed dependent record answers and checks deferred, stale, and tree-navigation rendering in `TruthView` and `KnowledgeTree`. [1]
