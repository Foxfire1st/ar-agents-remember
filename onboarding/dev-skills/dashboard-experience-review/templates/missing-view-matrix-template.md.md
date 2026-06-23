# dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `../../overview.md` |

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

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Method 2 (workflow × UI-state matrix) that drives this template. | whole file | [owned-methods.md](agents-remember/dev-skills/dashboard-experience-review/owned-methods.md) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-23T05:31 — Created with the skill (issue #92).
