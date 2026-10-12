# dashboard/src/panels/lifecycle-list/test-utils.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Shared fixture builders for the split LifecycleList test files, extracted from
`LifecycleList.test.tsx` by the 260731-EFA-L8 split. Seeds lifecycles, enclosures,
task documents, series, collapsible hierarchies, and the shared localStorage/store
cleanup.

## Code Commentary

### Logic

`lifecycle` / `enclosure` / `taskDoc` / `seriesNode` build typed nodes;
`collapsibleHierarchyProjection` builds the grouping scenario;
`installLifecycleListCleanup` is called explicitly by each mounted suite; its afterEach clears rendered DOM, stubbed globals, dashboard/session stores and localStorage. rowOf and rowHover resolve the actual option and its hover-bearing first child; standInForCssEscape is a test-only jsdom compatibility stand-in restored by cleanup.

### Conventions

Typed through the projection mirror; test-only.

### Invariants And Boundaries

Never imported by production code; mounted split suites must call installLifecycleListCleanup, not rely on an import-time side effect.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The shared fixture builders and cleanup. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Projection Fixture Alignment

No helper behavior changed. `seriesNode()` now defaults the required `discardedCount: 0` and
`discardedSubTasks: []` cells. Existing seat/execution-wave defaults and shared store/localStorage
cleanup remain unchanged.
