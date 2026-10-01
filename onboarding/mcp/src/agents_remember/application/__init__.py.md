# mcp/src/agents_remember/application/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`__init__.py` marks `agents_remember.application` as an importable package.

## Code Commentary

The file currently contains no exported application-layer facade. Public MCP payload
builders import application entry point functions directly from their domain modules such as
`provider_tools.py`, `worktree_tools.py`, `memory_tools.py`, and
`coordination_tools.py`.

## Invariants And Boundaries

- Keep this package initializer empty unless there is a concrete import-surface
  requirement.
- Do not use it to recreate the old `skill_tools.py` mass facade.

## Evidence

### Repo-Internal References

- The overview hot path summarizes guarded commit-message and forwarding boundaries. [1]
- Public payload builders import application entry points from their owning modules. [2]
