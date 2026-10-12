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

Loading/error/settled and TaskBodyNotice ownership remain the contract. The settled body assertions
now scope requirements to their block and read free-form Evidence through the Further-notes own view
with Back, rather than assuming all body text is inline. The reports stub is a typed bounded response,
not backend acceptance or proof that a product test was rerun here.

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
