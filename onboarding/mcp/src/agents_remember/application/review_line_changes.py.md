# mcp/src/agents_remember/application/review_line_changes.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Line counts for resolved ranges, using the reviewer's edit-distance rule.

## Code Commentary

Line counts are produced by the reviewer's own edit-distance rule over fully resolved ranges, so the number a reader sees is the one the reviewer's rule yields rather than an approximation of it.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- line_changes counts a resolved range by the reviewer's rule. [1]
