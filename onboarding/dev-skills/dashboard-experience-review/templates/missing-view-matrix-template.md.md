# dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The matrix shape for the Stage 3b missing-view detector: workflow steps + reachable system states ×
forced UI states, where every blank cell is a missing-view finding.

## Code Commentary

### Logic

Specifies the row set (scenario steps + enumerated provider / lifecycle / worktree / session states),
the column set (the forced UI-state list), the cell legend (`✓` / `~` / `✗`), and the output rule
(promote every `✗` to the backlog + findings; drive states via a disposable dummy worktree where they
do not occur naturally).

### Conventions

A `✗` blocking a catalogued scenario step is Blocker/High. This diff is implemented by no installed
skill, so the conductor owns it.

### Invariants And Boundaries

- Rows must include every reachable entity state, not only happy-path steps.

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant external documentation found.

### Repo-Internal References

- Method 2 (workflow × UI-state matrix) that drives this template. [1]

### Cross-Repo References

No meaningful cross-repo references found.
