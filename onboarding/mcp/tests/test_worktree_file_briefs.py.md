# mcp/tests/test_worktree_file_briefs.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Checks derived source briefs at memory worktree start and sync.

## Code Commentary

The start case covers effective, missing and negated inherited ignore rules. The sync cases cover a settled fast-forward or merge along with preview, repeated start and sync, ref-only movement, missing ignore, skipped memory, refused validation and cancelled conflict. Positive checks compare the derived directory and brief headers with the measured memory tree and check the code commit in the brief.

## Evidence

- The live start cases verify when briefs are published and preserve the inherited ignore bytes. [1]
- A successful fast-forward refreshes the settled pair while previews, completed replay and already-current sync leave briefs untouched. [2]
- A fresh merge commits the tracked ignore rule and refreshes the settled brief. Refusal preserves memory HEAD and the prior ignore bytes. Parking and cancellation preserve the prior ignore bytes. The brief directory stays absent on the refusal and conflict paths. [3]
