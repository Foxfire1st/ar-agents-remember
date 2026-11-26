# dashboard/src/panels/review/explainer/explainerRevisionInventory.ts

## Governing Overview

[Governing overview](../overview.md)

## Purpose

These readers decode optional metadata for one saved explanation revision.

## Code Commentary

A valid inventory summary takes precedence over an omission message. Absent metadata yields no inventory fields. The revision adapter augments the saved row through the parsers passed in by its caller.

## Relationships

`explainerApi.ts` uses the readers for state and revision rows. The view selects the matching revision before it renders the line.

## Evidence

- Saved revision metadata uses one parser with explicit optional inventory fields. [1]
