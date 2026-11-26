# mcp/src/agents_remember/worktrees/modules/closeout_source_heads.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Checks that closeout source branches still name the admitted base or this contract's observed output.

## Evidence

- Recorded completed and checkpointed outputs are read for each paired side. [1]
- Code and applicable external-memory source heads are checked separately. [2]
