# dashboard/src/panels/review/ReviewSurface.readsOnce.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for review surface.reads once.test.tsx.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

Opening the Review tab under StrictMode performs each read once, aborts nothing and reads no seat, and the returned-to tab renews its opening reads once when memory moved.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Opening the Review tab under StrictMode performs each read once, aborts nothing and reads no seat, and the returned-to tab renews its opening reads once when memory moved [1]
