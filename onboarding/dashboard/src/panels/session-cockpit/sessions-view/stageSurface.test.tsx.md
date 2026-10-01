# dashboard/src/panels/session-cockpit/sessions-view/stageSurface.test.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The stage-surface suite split from `SessionsView.test.tsx` by the 260731-EFA-L8 test
split. Pins the L6 stage surface: WorkingLine, InteractionBar, and stop-residual
behavior.

## Code Commentary

### Logic

Seeds a live session and asserts the stage renders the working line, the
interaction bar answers ride the gate channel, and stop residuals survive cleanup.

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

- The stage-surface suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260815-DAG Master Full-Gate Repair

Added an async `afterEach` that flushes the conversation timeline virtualizer's 150 ms scroll debounce (200 ms real-timer settle) before jsdom teardown.
