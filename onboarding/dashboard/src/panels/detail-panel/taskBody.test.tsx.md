# dashboard/src/panels/detail-panel/taskBody.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The on-demand task-body suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the task-11 on-demand body loading, states, and the
`TaskBodyNotice`.

## Code Commentary

### Logic

Mounts the reader with a task document whose body loads on demand and asserts the
loading/error/settled states and the notice surface.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The on-demand task-body suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
