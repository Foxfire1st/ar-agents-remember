# mcp/tests/test_crossing_history_interruption.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Covers close-checkpoint recovery during a retained structural memory merge.

## Code Commentary

A refused retry reopens the history state owned by the closing checkpoint. The tests compare both on-disk bytes and stage-zero entries and verify that a later valid crossing row or unstaged edit survives. Recovery recognizes a matching parent pair, and cancellation retires a matching checkpoint only after a verified rollback.

## Relationships

Exercises the retained continuation and rollback in `worktrees/sync_transaction_git/_merge.py` and the history checkpoint helpers in `worktrees/knowledge_crossing.py`.

## Evidence

- An interrupted close followed by a refused retry restores the writable open history. [1]
- The later row survives refusal and remains in closed history after a successful follow-up merge. [2]
- Recovery distinguishes partial closure, untouched state, later edits and mismatched parents. [3]
- A rejected rollback keeps the checkpoint and a verified rollback removes it. [4]
