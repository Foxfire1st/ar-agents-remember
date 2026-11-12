# mcp/src/agents_remember/serving/review_open_observation.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

One observation per open of the review page, shared by that open's reads as a snapshot.

## Code Commentary

Every read of one page open shares a single observation taken at the open, so the page's parts cannot disagree about what the tree held when it was opened. A later open takes its own observation.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- OpenObservations serves one open's reads from the observation taken at that open. [1]
