# dashboard/src/panels/changeset/MasterCounterStatus.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The series counter's status as the page shows it.

## Code Commentary

A busy preparation reads as busy against its generation rather than as a count of zero, so a page that is still preparing cannot look like a series with nothing in it. The generation is shown with the state, so a reader can tell which count they are looking at.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Preparation in progress is shown as in progress, never as a zero count. [1]

- The generation is shown with the state, so a count is attributable to the generation it came from. [2]
