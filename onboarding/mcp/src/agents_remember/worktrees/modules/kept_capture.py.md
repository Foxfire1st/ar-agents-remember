# mcp/src/agents_remember/worktrees/modules/kept_capture.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Produces the native capture tree from a private Git index that can be reused.

## Code Commentary

The capture lock protects the retained index and its witness check. When the real index, tracked paths, eligible untracked names and HEAD still match, the capture returns the witnessed tree. Native calls hold that witness in their request owner. A later native request can use the settled retained index to run add and write-tree again.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence


- Under the capture lock, kept_candidate_tree returns the witnessed tree when the private index still exists and its captured observations still agree. A witness miss takes the native kept-index capture path. [1]
