# dashboard/src/data/useMasterCounters.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The series counter as the page shows it.

## Code Commentary

Net totals commit first and leaf attribution arrives on its own later, pinned read, so a counter never shows leaf numbers that disagree with the totals beside them. Where the pins have moved the page says so rather than presenting an older attribution as the current one.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Totals are committed before attribution, so the page cannot show leaf numbers that disagree with its own totals. [1]

- Attribution that no longer matches its pins is named as a mismatch rather than shown as current. [2]
