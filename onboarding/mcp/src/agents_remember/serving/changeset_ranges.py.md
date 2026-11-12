# mcp/src/agents_remember/serving/changeset_ranges.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Typed disk answers for a master's immutable commit-pair ranges only.

## Code Commentary

Only the master's immutable commit-pair ranges are answered from disk; anything else falls through to the live path rather than being served from a range that does not describe it.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- MasterRangeAnswers answers immutable ranges and nothing else. [1]
