# mcp/tests/test_enclosure_adoption.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

`worktree_enclosure_adopt` is registered as documented: dry run, real run, repeated run.

## Code Commentary

MIK-R82 rule 4: the tool takes contract path, expected worktree group and a non-blank rationale, dry-runs by default and needs explicit approval for the real run. Every case fails without the change: the tool, its payload builder, and its refusal naming.

The dry-run witness keeps the delivered envelope free of `operation`, but asserts the actual operation identity from the logged whole result named by `log`. The outcome, no-effect and next-action assertions remain on their own respective surfaces. Absence alone is not the identity proof.

## Evidence

- Adoption dry run, real run and repeated run are pinned. [1]

- Operation identity is read from the whole result while dry-run and next-action assertions remain. [2]
