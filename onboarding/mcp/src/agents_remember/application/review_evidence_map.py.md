# mcp/src/agents_remember/application/review_evidence_map.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Measured evidence grouped into a map that keeps its detail, with the packet built beside it.

## Code Commentary

Evidence is grouped for the page while keeping each group's measured detail, and the packet is built from the same observations rather than a second read. A changed invariant is named in the group it belongs to, so the map and the packet cannot drift apart.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- _group_map groups measured evidence without discarding the detail inside a group. [1]
