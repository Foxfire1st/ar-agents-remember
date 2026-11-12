# dashboard/src/panels/detail-panel/limited-accessible.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

A surface with no display clock still owes its reset to the accessible status routes.

## Code Commentary

The order graph's unit, the constellation's nodes and the sidebar's progress mark each carry the served end in a computed accessible name, and a keyboard reader can reach the constellation's selectable nodes through its text alternative. The case asserts what a screen reader receives, not what the pixels show.

**INV-7GVWYD.** The accessibility claim is about the rendered word, and this case is the one that reads its accessible name.
