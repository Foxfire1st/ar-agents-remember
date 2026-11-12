# dashboard/src/panels/changeset/useInspectionCounter.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The counter the inspection panel shows.

## Code Commentary

The counter answers for the comparison being inspected, and a preparation that is still busy is reported as busy rather than as a number. A failure is shown as a failure instead of a count.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- The counter shown belongs to the inspected comparison, and a failure is never displayed as a count. [1]
