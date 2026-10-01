# mcp/src/agents_remember/models/skills.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`skills.py` defines the response model for the `skills_install` MCP tool.

## Code Commentary

`SkillsInstallResponse` exposes dry-run/layout/install-root facts plus planned,
installed, removed, and archived path lists while allowing installer-specific
fields to pass through during service evolution.

## Invariants And Boundaries

- Skill installation reports are modeled but intentionally flexible around
  installer detail fields.
- Copy/archive semantics remain owned by the install service and application entry point.

## Evidence

### Repo-Internal References

- The skills install application entry point delegates to package install services. [1]
