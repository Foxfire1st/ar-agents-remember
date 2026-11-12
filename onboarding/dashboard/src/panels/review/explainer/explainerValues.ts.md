# dashboard/src/panels/review/explainer/explainerValues.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The narrowing guards the explainer's parsers read unknown JSON through.

## Code Commentary

An answer of unknown shape is narrowed to a record, a string, or nothing before anything reads it, so a malformed answer cannot be consumed as a valid one. A value that is not the expected shape yields nothing rather than a default that looks like data.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A malformed explainer answer becomes nothing rather than a default that reads like a real value. [1]
