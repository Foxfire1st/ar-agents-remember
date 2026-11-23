# mcp/src/agents_remember/application/review_overview_precompute.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The leaf-wide view of a leaf's newest trees, built before the page asks for it.

## Code Commentary

The overview is built ahead of the request from the leaf's newest trees, and a build in progress is distinguishable from a settled one, so a page never waits on a build it could have been told about. Reuse requires the same four comparison trees, converted base and recorded memory-base commit. Capturing a new base commit can supersede an in-flight build even when all four tree IDs match.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence


- OverviewPrecompute builds the live leaf-wide view before the page asks for it. Its build identity includes the comparison trees, the converted base tree when present, and the exact recorded memory-base commit. [1]
