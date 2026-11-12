# mcp/src/agents_remember/worktrees/modules/landing_commit_check_pipes.py

## Governing Overview

[overview](overview.md)

## Purpose

Best-effort discovery of other processes retaining a private hook output pipe.

## Code Commentary

`_pipe_write_end_holders` scans numeric `/proc` entries, excludes this process, and collects a PID when an fd symlink matches the private pipe inode. Missing `/proc`, unreadable fd directories and per-link errors are tolerated; results are unique and sorted. The implementation matches inode symlinks, not fd access flags, and performs no kill itself. Its private-hook-subtree premise does not imply a universal process census.

## Invariants And Boundaries

The extracted helper retains its caller-owned operation and refusal boundary; this card is source inspection, not a new product execution or publication grant.

## Evidence

- Best-effort discovery of other processes retaining a private hook output pipe. [1]
