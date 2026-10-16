# mcp/src/agents_remember/worktrees/reopen_series.py

## Governing Overview

[mcp/src/agents_remember/worktrees/overview.md](overview.md)

## Purpose

Series handling for reopened worktrees.

## Code Commentary

The owner keeps a reopened leaf's series membership and history-file target consistent while the new attempt proceeds. Projection scope construction passes each prepared document with its actual JSON path to the shared task-fact owner rather than assuming an unlocated document tuple.

## Evidence

- The file realizes its current contract at the corrected candidate. [1]

## Current source evidence


- Series reopen passes source-path/document pairs to the existing scope owner. [2]
