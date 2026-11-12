# dashboard/src/data/staleInvariants.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The marks that say a shown invariant has changed since it was read.

## Code Commentary

A changed invariant keeps a mark until the comparison that carries the change is actually loaded, so a row is never shown as current after it moved. Loading a later comparison that does not mention the invariant does not clear its mark.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A changed invariant stays marked until the comparison carrying the change is loaded. [1]

- A load that does not mention the marked invariant leaves the mark standing. [2]
