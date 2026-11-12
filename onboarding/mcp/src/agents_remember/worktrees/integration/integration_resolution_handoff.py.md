# mcp/src/agents_remember/worktrees/integration/integration_resolution_handoff.py

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Executable task-addressed handoff for reversible integration source drift.

## Code Commentary

### Logic

The public surface is `integration_resolution_required`. Protected-ref and door state are classified from exact live and journal evidence. A moved, missing, unreadable, or contradictory ref is never discarded: the same landing generation must reconcile or complete, with an executable task-addressed handoff for any later repair or revert planning.

The refusal's `summary` and `cancel_note` now route recovery through `worktree_sync` for the owning contract — settle any retained code or memory conflict (re-running the targeted test utility after code resolutions) — and then a new targeted closeout. They no longer instruct the operator to absorb a recorded source delta by hand; the refusal sentence itself is unchanged, and `replay` remains the carryover vehicle rather than this route's prompt.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `integration_resolution_required` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
