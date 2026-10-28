# dashboard/src/panels/review/reviewShown.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Which mounted review page is the one on screen.

## Code Commentary

A mounted review page knows whether it is the one on screen, so a hidden review keeps its own page state and does not take the visible tab's keys. Two reviews open at once therefore behave as two, not as one with a stale view.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A hidden review keeps its page and does not answer for the visible one. [1]
