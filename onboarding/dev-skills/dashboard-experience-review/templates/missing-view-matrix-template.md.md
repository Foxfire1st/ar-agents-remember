# dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md

## Current A8 source account

The current matrix lists lifecycle, worktree and session states, not session/TUI. It crosses scenario steps and reachable states with the forced UI-state columns; blank cells become missing-view findings, with a scenario-blocking blank Blocker/High. This describes the template, not a claim that owned-methods has deleted every provider reference or that a disposable harness was run.

- The current template enumerates session rather than session/TUI while retaining the workflow-by-forced-state matrix and missing-cell output rule. [2]


## Current operative account — MIK-R112

The matrix uses workflow steps and states the running system can actually reach, together with forced UI states. The changed source removes the provider-state row enumeration and provider_status observation; retained worktree_status/server_info and live DOM evidence decide reachability. A blank settled cell remains a finding, never proof a retired provider view should return. The conductor remains findings-only and this template grants no mutation.

The original prose, exact parameters, references and dated producer accounts below remain intact as history, not present-tense authority for superseded behavior. Current evidence is the source path `dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md` and the source-specific before/after extents preserved in the residual-hunk account. No code edit, proof rerun or new execution acceptance is claimed.

## Historical original card — preserved, not the current operative account

<details>
<summary>Original source account and historical evidence</summary>

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

</details>
