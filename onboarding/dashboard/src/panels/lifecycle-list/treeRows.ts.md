# dashboard/src/panels/lifecycle-list/treeRows.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

A pure flattening of one repository task tree into task rows and in-place completed/abandoned folds.

## Code Commentary

treeItems follows ordered served child keys with seen/cycle guards and stable need bands. Selected ancestors and terminal folds are held open unless their control was explicitly released during the current selection episode; closed folds retain entries/counts without constructing descendant rows or propagating hidden descendant priorities. Parent collapse is persisted separately; open folds remain local. No chronological document/series reconstruction remains.

Each parent's served children are ordered with `rowOrder` instead of `rowBand`, so the started band's host-timed rows order newest first and every other band keeps the server's order; the sort is stable, so ties and untimed rows do too.

## Evidence

- Sibling placement uses the band-then-host-time order rather than the band alone. [2]

- The pure flattener combines served ancestors with per-selection released keys for parent collapse and terminal-fold holding; seen guards retain one placement. [1]
