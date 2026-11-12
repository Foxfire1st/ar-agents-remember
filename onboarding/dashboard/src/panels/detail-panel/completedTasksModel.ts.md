# dashboard/src/panels/detail-panel/completedTasksModel.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Supply completion facts and ephemeral ordering for completed task tables without migrating canonical documents.

## Code Commentary

completedEntries follows served children at stage completed, carrying entry, original position, short id and summary.completedAt. No decision-text timestamp fallback or slice index remains. Missing/invalid times sort after finite times in either direction.

Sorting copies the input. Number order uses numeric English locale comparison rather than parsing task IDs; time order uses parsed dates and leaves absent/invalid dates last in both directions. Sorting and fallback are presentation only: they write neither timestamps nor task state.

## Evidence
