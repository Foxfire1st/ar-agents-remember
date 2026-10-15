# dashboard/src/panels/detail-panel/task-groups.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Compose grouped Now, Tasks and Masters indexes, the master completed-task preview and the sprint raw-row view; delegate shared row identities/navigation to indexRows and grouped own-view rendering to TaskGroupView.

## Code Commentary

indexRows row targets resolve an exact projected commanded-master reference first, a linked series second, and an authored local slice last. Full-index positions stay stable across filtered groups and completed sorting. Unresolved and seat rows remain visible rather than vanishing. Work appears under Now only. A master Tasks block draws at most five newest completed tasks above its counted all-link, using CompletedTaskList with names, navigation targets and completion times; missing times remain unknown. MasterTasksBlock calls indexedRows once per invocation and passes that matcher to completedEntries and resolveRowTarget, sharing first-match lookup across completed facts and navigation. The matched steps/review/waiting-row owners and sprint groups keep their existing responsibilities; there is no persistent lookup cache. Sprint completed groups remain a counted link. Discarded-before-start history remains alongside abandoned rows even with no live index entries.

Master Now reads the task document's steps and required whole-round review aggregates. Sprint Now resolves each commanded master across all projected documents and reads that master's live task totals. Unknown row states remain waiting. The sprint raw-row view deliberately exposes both authored row status and master-document status, rather than silently resolving the recorded truth gap. Index introductions alone keep the block meaningful; no duplicate structured index is synthesized. Major-step marks receive each matched task’s cached steps; ready graph nodes appear as an informational Can start next group. Neither display is permission or a task start command.

## Grant-free index rows

Master Now, waiting-task and completed/abandoned group rows carry navigation, steps, requirements and history only. Neither the LeafExtra hand-through nor a giver badge/control remains. Sprint/master rows likewise display no direct-execution control or mark; the sole interactive grant surface belongs to a planning subTask's own page. The dedicated now-steps-N element contains served step-count text and cached StepMarks pointer targets; a StepDot tooltip portals to document.body rather than remaining within that text domain.

## Boundaries

The reader supplies navigation callbacks and qualified reference-path resolution; indexRows owns target precedence, IDs and sprint grouping helpers. TaskGroupView owns GroupViewBody, re-exported here, and uses the shared completed table for completed master tasks. Grouping/display are not lifecycle state writes. Discarded-before-start audit is not a live row and never inflates progress totals.

## Evidence


- indexRows owns exact commanded-master, linked-series and authored-slice target precedence and stable full-index positions. [1]

- indexRows retains unresolved and seat rows with their authored status for grouping; task-groups renders them in the raw all-row view. [2]

- The raw sprint view keeps row and master truth visibly separate. [4]

- Master Now keeps served step counts and cached major-step dots without grant controls; readiness remains a navigation-only graph display. [5]

- Master Tasks keeps discarded-before-start history reachable beside abandoned rows, and GroupViewBody renders that audit even without live group rows. [3]

- MasterTasksBlock shares one call-local matcher between completed preview facts and navigation, with the completed count/all-link below the preview. [6]
