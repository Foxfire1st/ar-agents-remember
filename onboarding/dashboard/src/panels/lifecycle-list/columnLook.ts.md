# dashboard/src/panels/lifecycle-list/columnLook.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

The shared caret cell for the Operations task tree. It leaves the same room in a row without a disclosure, so state marks align.

## Code Commentary

The approved layout remains column-local, but its text now follows the task page rather than applying the proposal's 14-to-16-pixel conversion. Row titles use 0.8rem; the caret and other owned sidebar/bell-layer text use 0.72rem, the task page's smaller text. caretCell keeps a one-character lane with muted colour and the explicit 0.72rem size. The surrounding shared Panel keeps its own scale. Grouping, bell and Clear all reuse columnTabButton rather than independent tab recipes.

## Evidence

- The exported caret cell keeps a fixed one-character lane, muted colour and 0.72rem task-page smaller text. [1]
- Sidebar typography takes its title and smaller-text sizes from the task-page row and count recipes. [2]
