# dashboard/src/panels/review/changeSetFilter.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Narrowing the change set to a query without changing what a row means.

## Code Commentary

A query narrows the tree and leaves every row it keeps meaning what it meant; an empty query returns the tree unchanged rather than a filtered view of it. A path matches on what it is, including that it is code without an invariant, not on a rendered label.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- An empty query returns the tree unchanged, not a filtered copy of it. [1]

- A path is matched on what it is, including code without an invariant, not on a display label. [2]
