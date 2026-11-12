# dashboard/src/panels/review/reading/useReviewSearch.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

When the review page reads the whole location inventory, and how a failed read is told apart from no results.

## Code Commentary

The complete inventory is read only once the reviewer has typed a query, so opening a page does not load it; and a read that failed is reported as a failed read rather than as a search with no matches.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Opening the page does not read the whole inventory; a typed query does. [1]

- A failed search read is shown as a problem, not as an empty result. [2]
