# dashboard/src/panels/review/changeSetRanks.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The one order behind every change-set sort, and the one-line hint that explains it.

## Code Commentary

Every change-set sort is ranked by one order and explained by one hint, so a row's rank cannot differ between the list and the popup that offers the sort. The ranks are by effect and by currentness, and the hint names what the rank means rather than repeating the sort's label.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A row's rank is decided in one place, so the list and the popup cannot rank the same row differently. [1]

- Every sort offers a hint that says what its order means, not the sort's name again. [2]
