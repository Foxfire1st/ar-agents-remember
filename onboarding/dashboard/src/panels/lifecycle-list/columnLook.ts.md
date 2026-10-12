# dashboard/src/panels/lifecycle-list/columnLook.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

The shared caret cell for the Operations task tree. It leaves the same room in a row without a disclosure, so state marks align.

## Code Commentary

The approved column uses a 14-pixel design root while the dashboard root is 16 pixels; column-owned rem values use the 0.875 conversion. The surrounding shared Panel keeps its own scale. Grouping, bell and Clear all reuse columnTabButton rather than independent tab recipes.

## Evidence

- The exported caret cell keeps a fixed one-character lane and muted column-scale glyph. [1]
