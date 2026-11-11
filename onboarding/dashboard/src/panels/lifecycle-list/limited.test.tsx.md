# dashboard/src/panels/lifecycle-list/limited.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

A started task working on nothing, with a seat held by its provider limit, says rate limited and counts as paused underneath.

## Code Commentary

The limit is served; the dashboard only shows it. The case checks the word on the sidebar and the task, the full hover detail, and that the grouping label, the counts and the header keep saying paused.

**INV-XZYGEB.** The case pins both halves of the requirement, the word and the counting, where the sidebar renders them.
