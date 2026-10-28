# mcp/src/agents_remember/worktrees/modules/kept_capture.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A worktree's kept capture index: a review read's capture writes only what moved.

## Code Commentary

A capture writes only what moved against the kept index, and the index is what says a tree is already captured, so a second read does not re-capture an unchanged tree.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- kept_candidate_tree answers a tree from the kept index when nothing moved. [1]
