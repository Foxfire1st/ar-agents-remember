# mcp/src/agents_remember/serving/leaf_worktree_watch.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

One process-wide inotify watch over the leaves' worktrees.

## Code Commentary

One watch covers all the leaves' worktrees for the process, with an admitted budget and a read budget, rather than a watch per request. A directory that is not eligible is not watched, so the watch cannot grow with the worktrees a page happened to open.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- WatchBudget bounds what the single watch admits, and read_budget what a read may consume. [1]
