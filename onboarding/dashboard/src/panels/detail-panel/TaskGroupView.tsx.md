# dashboard/src/panels/detail-panel/TaskGroupView.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Render completed/abandoned index groups through the shared row/navigation seams, keeping discarded-before-start audit separate.

## Code Commentary

Only a nonempty all-Completed group with a defined parent master ID uses the sorted CompletedTaskList. For that branch, GroupViewBody builds one call-local indexSlices matcher and shares it between completedEntries fact preparation and resolveRowTarget navigation, rather than rebuilding or scanning a document pool per completed row. Sprint groups and other task groups retain their incoming order. Ordinary task rows show the matched primary requirement; sprint rows can show projected master task counts.

The full-list position map remains the row identity source. Discarded-before-start entries are rendered independently beside the retained group rather than counted as completed work. This extracted view consumes facts and navigation callbacks; it does not load documents or authorize completion.

## Evidence

- Completed-master sorting is conditional and shares one call-local slice index for facts/navigation; other groups and discarded audit keep their separate ownership. [1]
