# mcp/src/agents_remember/worktrees/task_stage.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Prepare task-document stage changes for existing worktree task-fact transactions, including the mirrored parent row, without adding a stage store.

## Code Commentary

A planning or abandoned leaf cannot transition to inProgress while intentReview is open; the same gate covers the successor path.

Start promotes a planning or admitted abandoned document to inProgress only after its native intentReview is absent or go; an open review raises intent-review-open before any planned stage write; an attach passes no requested stage and preserves the current one. Completed documents keep their explicit reopen/finalize ownership. Abandon requests abandoned. A missing document is not invented.

The change captures each actual document path and original source snapshot. Its candidates keep those exact pairs for projection overrides, including cross-root master/sprint batches. Validation rejects a changed source before batch publication; restoration belongs to the existing source-snapshot writer. The mirrored parent row is planned from the updated canonical document rather than inferred from step marks.

## Evidence

- Stage planning preserves attachment/completed ownership and mirrors the actual document into its parent row. [1]
- Captured document/path pairs validate before the existing batch writer publishes them. [2]

- A planning or abandoned leaf cannot transition to inProgress while intentReview is open; the same gate covers the successor path. [3]
