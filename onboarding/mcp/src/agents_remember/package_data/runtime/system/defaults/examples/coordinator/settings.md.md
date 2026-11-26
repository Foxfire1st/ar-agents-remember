# settings.md

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces. It also illustrates the local coordinator directory layout (`system/settings.md`, `memory-repos/`, `tasks/`, `notes/`, `worktrees/`) and memory-repo routing through `context_packet`.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file.

### Invariants And Boundaries

Product context resolution (`context_packet`) is the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths.

### Todos

None.

### Docs References

No external documentation is needed.

## Evidence

### Repo-Internal References

- The example states that coordinator settings are workspace-wide and do not replace per-repository memory settings. [1]

- The routing section tells agents to resolve the target repository through the product (`context_packet`) and treat repository-specific memory guidance as more specific. [2]

### Cross-Repo References

No sibling repository evidence is needed.
