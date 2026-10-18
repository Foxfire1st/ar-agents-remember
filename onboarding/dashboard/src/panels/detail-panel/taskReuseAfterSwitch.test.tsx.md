# dashboard/src/panels/detail-panel/taskReuseAfterSwitch.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

Pin the return side of a task switch: a revisited task is answered from the body the first visit
retained, with no second request for that body.

## Tested Boundary

The case mounts the task entry for one leaf, leaves to another selection, and returns. It asserts that
the retained body is shown and that the body endpoint was not requested again for the returned task.
The change-set and summary reads remain their own reads; this case pins the body retention, not a
page timing or a lifecycle result.

## Evidence

- The mounted case named `answers a revisited task from what the first visit kept, with no second
  request for it`.
- `TaskDocumentResources` and `useTaskDocumentBody`.
