# dashboard/src/panels/detail-panel/task-groups.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own the grouped Now, Tasks and Masters indexes and their completed, abandoned and raw-row own views.

## Code Commentary

Row targets resolve an exact projected commanded-master reference first, a linked series second, and an authored local slice last. Full-index positions stay stable across filtered groups. Unresolved and seat rows remain visible rather than vanishing. Work appears under Now only; completed rows are a counted link. Discarded-before-start history remains alongside abandoned rows even with no live index entries.

Master Now reads the task document's steps and required whole-round review aggregates. Sprint Now resolves each commanded master across all projected documents and reads that master's live task totals. Unknown row states remain waiting. The sprint raw-row view deliberately exposes both authored row status and master-document status, rather than silently resolving the recorded truth gap. Index introductions alone keep the block meaningful; no duplicate structured index is synthesized.

## Grant-free index rows

Master Now, waiting-task and completed/abandoned group rows carry navigation, steps, requirements and history only. Neither the LeafExtra hand-through nor a giver badge/control remains. Sprint/master rows likewise display no direct-execution control or mark; the sole interactive grant surface belongs to a planning subTask's own page. The dedicated now-steps-N element remains the step-count text domain.

## Boundaries

Navigation callbacks and qualified document resolution stay with the reader. Grouping/display are not lifecycle state writes. Discarded-before-start audit is not a live row and never inflates progress totals.

## Evidence

- Every group retains exact commanded-master, linked-series and authored-slice navigation precedence. [1]
- Rows lacking a projected master remain in status groups and the all-row view. [2]
- The raw sprint view keeps row and master truth visibly separate. [4]

- Master Now retains its dedicated step count and no grant addition. [5]


- The gone group keeps discarded-before-start history reachable without live tasks. [3]
