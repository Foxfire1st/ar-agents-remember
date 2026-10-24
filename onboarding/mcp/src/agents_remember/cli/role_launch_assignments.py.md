# mcp/src/agents_remember/cli/role_launch_assignments.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Hold the assignment sentence of each role a launch admits without a canonical task: architect, investigator and bootstrap.

## Code Commentary

Each sentence is procedure, not preparation logic, so it lives here and the preparation module keeps the one call that asks for it. `architect_assignment` makes a project-scoped launch ask the developer for the outcome and the registered repository, names the shared Projects workspace as an execution location rather than a repository selection, and forbids inferring a target from the workspace name or a singleton registry. `investigator_assignment` scopes one concern to one report: the concern arrives in the parent's first message when a parent started the seat, and no code checkout, enclosure, memory, task document, status, commit or role may be changed. `bootstrap_assignment` names no sprint, master, leaf, task document, worktree or enclosure and selects no repository for the user: the setup conversation asks which code repository, which branch is its memory's foundation, whether the memory repository is new, and whether providers index now or later, then writes the setup report and never creates a task, worktree or role.

## Evidence

- The bootstrap sentence that invents no identity and creates no task, worktree or role. [1]
- The investigator sentence, whose concern comes from the parent that started the seat. [2]
- The project-scoped architect sentence. [3]
