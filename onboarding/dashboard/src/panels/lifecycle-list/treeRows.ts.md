# dashboard/src/panels/lifecycle-list/treeRows.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

A pure flattening of one repository task tree into task rows and in-place completed/abandoned folds.

## Code Commentary

treeItems follows ordered served child keys with seen/cycle guards and stable need bands. Selected ancestors and terminal folds are held open; closed folds retain entries/counts without constructing descendant rows or propagating hidden descendant priorities. Parent collapse is persisted separately; open folds remain local. No chronological document/series reconstruction remains.

## Evidence
