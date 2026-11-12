# mcp/src/agents_remember/application/review_invariant_changes.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Which invariants differ between the comparison a page shows and a newer one.

## Code Commentary

The difference is computed between the invariant record blobs of the two comparisons, so an invariant is reported changed only when its record differs rather than when the page around it moved. An unavailable record is named as unavailable instead of being counted as a change.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- invariants_that_differ compares record blobs and names the ones that differ. [1]

- _unavailable keeps an unreadable record visible as unavailable rather than as a change. [2]
