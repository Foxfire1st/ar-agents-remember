# dashboard/src/panels/detail-panel/task-groups.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Compose grouped Now, Tasks and Masters indexes, the master completed-task preview and the sprint raw-row view; delegate shared row identities/navigation to indexRows and grouped own-view rendering to TaskGroupView.

## Code Commentary

Rows follow served children/stages/counts and exact keys; Now owns active work. Master completed preview shows newest five plus all-link via CompletedTaskList; sprint completed rows keep served order. Positions stay full-list-based. Discarded audit remains separate from aborted/live completion, without slice/series matching.

Now reads served started/planned/completed/aborted counts and resolves matching children by key. Task cells use entry major-step counts and cached summary steps; master cells use served child counts. Summary review aggregates remain whole-round facts. Can start next renders only ready graph nodes and is not a task-start permission.

## Grant-free index rows

Master Now, waiting-task and completed/abandoned group rows carry navigation, steps, requirements and history only. Neither the LeafExtra hand-through nor a giver badge/control remains. Sprint/master rows likewise display no direct-execution control or mark; the sole interactive grant surface belongs to a planning subTask's own page. The dedicated now-steps-N element contains served step-count text and cached StepMarks pointer targets; a StepDot tooltip portals to document.body rather than remaining within that text domain.

## Boundaries

The reader supplies navigation callbacks and qualified reference-path resolution; indexRows owns entry-key targets, stable positions and served-count helpers. TaskGroupView owns GroupViewBody, re-exported here, and uses the shared completed table for completed master tasks. Grouping/display are not lifecycle state writes. Discarded-before-start audit is not a live row and never inflates progress totals.

## Evidence





- Master Now keeps served step counts and cached major-step dots without grant controls; readiness remains a navigation-only graph display. [5]

- Master Tasks keeps discarded-before-start history reachable beside abandoned rows, and GroupViewBody renders that audit even without live group rows. [3]
