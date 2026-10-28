# dashboard/src/data/reviewReads.strict.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

That a page open costs one request per opening read, even under StrictMode replay.

## Code Commentary

Each of the four opening reads starts exactly one request while StrictMode replays the effect, so a page open is four requests and not eight; and a request for a leaf that is no longer open is cancelled rather than left running.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A page open starts one request per opening read, even when StrictMode replays the effect [1]

- A request for a leaf that changed or unmounted is cancelled rather than left running [2]
