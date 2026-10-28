# mcp/src/agents_remember/application/review_tree_overview.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Already validated inventory and worklist facts, projected for the compact review opening.

## Code Commentary

The compact opening projects facts that were already validated elsewhere rather than re-deciding them: counts, currentness and the summary are read from the inventory and worklist, so the opening cannot disagree with the page it opens.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- summarize_inventory projects validated inventory facts without re-deciding them. [1]
