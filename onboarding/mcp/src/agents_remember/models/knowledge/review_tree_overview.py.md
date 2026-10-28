# mcp/src/agents_remember/models/knowledge/review_tree_overview.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Compact review facts, kept distinct from location rows and full worklist evidence.

## Code Commentary

The compact opening's facts are their own models rather than a projection of the location rows, so the summary a page opens with cannot be mistaken for the worklist evidence behind it.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- ReviewOverview is the compact fact set the opening page carries. [1]
