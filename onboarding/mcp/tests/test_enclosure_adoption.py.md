# mcp/tests/test_enclosure_adoption.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

`worktree_enclosure_adopt` is registered as documented: dry run, real run, repeated run.

## Code Commentary

MIK-R82 rule 4: the tool takes contract path, expected worktree group and a non-blank rationale, dry-runs by default and needs explicit approval for the real run. Every case fails without the change: the tool, its payload builder, and its refusal naming.

## Evidence

- Adoption dry run, real run and repeated run are pinned. [1]
