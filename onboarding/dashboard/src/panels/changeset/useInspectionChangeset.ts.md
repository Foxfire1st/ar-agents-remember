# dashboard/src/panels/changeset/useInspectionChangeset.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The changeset the inspection panel shows.

## Code Commentary

The inspection changeset is the one for the comparison being inspected, and a read for another comparison cannot be shown as this one's. A failed read is shown as a failure rather than as an empty changeset.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- The changeset shown is the one for the comparison inspected, not one that arrived for another. [1]
