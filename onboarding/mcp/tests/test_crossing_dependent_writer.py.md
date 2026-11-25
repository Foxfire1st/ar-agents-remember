# mcp/tests/test_crossing_dependent_writer.py

## Governing Overview

[MCP tests](overview.md)

## Purpose

Exercise the mounted knowledge writer's dry plan for a dependent record changed on both sides of a crossing merge.

## Code Commentary

The fixture builds the shared parked crossing world: a series contract, a memory worktree holding the open crossing history, and a sync record whose code side has settled at the code branch's commit and whose memory side is parked at resolution-required with that history owner and the conflicted dependent. The plan updates the existing dependent and reports its next revision. The plan's code tree equals the tree of a committed snapshot of the code branch, and the snapshot's commit is the peeled branch commit. The test checks that the dry plan leaves every memory file and the merge index unchanged.

## Evidence

- The crossing dry plan updates the existing record and confirms the resolved committed code state. [1]
