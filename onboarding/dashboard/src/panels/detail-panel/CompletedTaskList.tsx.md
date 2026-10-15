# dashboard/src/panels/detail-panel/CompletedTaskList.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Render one completed-task table shared by the whole completed list and its newest-five preview.

## Code Commentary

Each mount owns Number/time sort preference, defaulting to newest completion time. Header buttons toggle direction with aria-sort; switching column uses its own initial direction. Preview ignores the local preference, always shows at most the newest five and omits headers. An empty list renders nothing.

Rows keep supplied full-list positions, optional target navigation and a dash when completion time is absent. Actual timestamp production and legacy fallback belong to other owners. The table consumes facts; it does not author completion or migrate stored order.

## Evidence

- Mount-local sorting, newest-five preview and optional row navigation share the same completed-row renderer. [1]
