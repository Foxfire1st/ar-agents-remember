# dashboard/src/panels/detail-panel/TaskGroupView.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Render completed/abandoned index groups through the shared row/navigation seams, keeping discarded-before-start audit separate.

## Code Commentary

A master’s completed group uses the shared sorted CompletedTaskList. Sprint completed groups and aborted rows retain served child order. All targets/positions come from the original children list, not a slice matcher; unresolved entries remain inert.

The full-list position map remains the row identity source. Discarded-before-start entries are rendered independently beside the retained group rather than counted as completed work. This extracted view consumes facts and navigation callbacks; it does not load documents or authorize completion.

## Evidence
