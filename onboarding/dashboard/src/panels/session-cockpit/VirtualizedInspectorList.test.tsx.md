# dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the exact 100-row ordinary-DOM boundary and proves that 101 rows enter virtualization while
retaining the full accessible set size.

## Code Commentary

### Logic

- The 100-row case expects ordinary list items and `data-virtualized=false`.
- The 101-row case installs the jsdom geometry seam, expects virtualization, and asserts logical
  total/position semantics rather than requiring every row in the DOM.

### Invariants And Boundaries

- The boundary is strictly `> 100`, not `>= 100`.
- Tests distinguish logical data retention from physical DOM retention.

### Todos

None recorded; the task-local concurrent jsdom shutdown residual is tracked in the curator report.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- 100-row ordinary DOM case. [1]
- 101-row virtualized logical-total case. [2]
- Component under test. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
