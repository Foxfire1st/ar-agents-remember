# mcp/src/agents_remember/application/runtime/skills.py

## Governing Overview

[runtime overview](overview.md)

## Purpose

`runtime/skills.py` contains only the `skills_install` application entry point for package
skill installation.

## Code Commentary

The former large skill-facing MCP facade was split into focused application entry point
modules. This file keeps `skills_install_tool()`, which delegates to
`install.skills.install_skills()` with dry-run, overwrite, and archive options
and returns an operation-labeled payload (the installer is a flat copy, so there
is no layout option).

## Invariants And Boundaries

- Do not rebuild `runtime/skills.py` as a mass re-exporter or mega-entry-point.
- New MCP operation application entry points should live in the domain module that owns the
  behavior, then be imported directly by the relevant `mcp/tools/` domain
  module.
- Skill installation remains a package install concern, not a provider,
  worktree, memory, or benchmark application entry point.
- `skills_install_tool` defaults `dry_run=False` (act-by-default), forwarding to
  `install.skills.install_skills`; `dry_run=true` previews the copy plan.

## Evidence

### Repo-Internal References

- Split application route explains the new application layer layout. [1]
- MCP payload builders import this file only for `skills_install`. [2]
- Skill install response model lives in the models package. [3]
