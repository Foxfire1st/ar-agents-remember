# dashboard/src/data/reviewOpen.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The accounting of what opening the review page costs, and which page an open belongs to.

## Code Commentary

Each page open is counted once per opening read, and an opening read carries the header that says which open it belongs to, so the cost of a page is measurable per open rather than per process. The page id is fixed for the life of the page, so two reads of one open are known to be the same open.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- An opening read is attributed to the open it belongs to, so a page's cost is counted per open. [1]

- One page keeps one id, so its reads are known to belong to the same open. [2]
