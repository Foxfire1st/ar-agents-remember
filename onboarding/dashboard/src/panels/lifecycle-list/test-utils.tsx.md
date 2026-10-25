# dashboard/src/panels/lifecycle-list/test-utils.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Typed test-only native entry/keyed-map/explicit-count fixtures for LifecycleList suites, with hierarchy and shared DOM/store/storage cleanup and stubbed-global restoration.

## Code Commentary

### Logic

task, taskMap, seed and hierarchy build native entries and served membership/count facts. rowOf finds the actual option. installListCleanup is explicit per-suite setup; it clears rendered DOM, the dashboard store, localStorage and stubbed globals, not production state.
The retired session store is not a cleanup target. `rowOf` resolves the actual option; `beforeEach` installs the CSS.escape test stand-in and `afterEach` restores stubbed globals. The former lifecycle/series builders and rowHover helper are not current exports.

### Conventions

Typed through the projection mirror; test-only.

### Invariants And Boundaries

Test-only: mounted suites call installListCleanup explicitly; importing this module is not cleanup installation.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References



- The shared typed fixture builders and explicitly installed cleanup retain DOM/global/dashboard/localStorage ownership, without the removed sessions store. [1]



### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Projection Fixture Alignment

Discarded history remains summary audit data, separate from native child counts. No seriesNode or lifecycle fixture grammar remains.
