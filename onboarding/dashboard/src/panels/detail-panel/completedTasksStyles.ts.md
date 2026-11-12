# dashboard/src/panels/detail-panel/completedTasksStyles.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Keep native completed-table and sort/name button appearance local to the task reader.

## Code Commentary

The table uses fixed layout, full width, wrapped cell content and a muted time column. Name and sort controls have local hover/focus-visible treatments using shared tokens.

Styles supply neither completion times nor sort state. A declaration intended to remain readable on narrow panels is not browser/pixel acceptance evidence; assembled responsive behavior requires its own witness.

## Evidence

- Fixed table/wrapped cell styles and local control focus states do not own completion or sorting semantics. [1]
