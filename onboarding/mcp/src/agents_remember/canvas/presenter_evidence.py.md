# mcp/src/agents_remember/canvas/presenter_evidence.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The presenter's additional read grant uses R102's exact-tree, bounded source reader. The packet is the authority: the author names a side and relative path, never a repository, revision or current checkout.

## Code Commentary

- Every tool call rechecks the packet's immutable digest, and historical/worktree roots stay exactly as admitted.

## Evidence

- The presenter reads only through the admitted packet's exact-tree reader. [1]
