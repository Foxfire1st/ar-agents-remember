# mcp/src/agents_remember/mcp/tools/terminal.py

## Governing Overview

[mcp/tools overview](overview.md)

## Purpose

Adapts internal terminal-session application operations. Structural public tools do not call these
exact-id payloads directly; runtime ids remain available here for operator/control-plane seams.

## Code Commentary

### Logic

Task assignment accepts a runtime session correlation plus canonical task document and role.
Spawn/retire/rename adapters continue to wrap internal application primitives. Public agent
registration uses `mcp/tools/structural_agent.py` instead.

### Conventions

This is an internal response-adapter family, not the agent-facing address vocabulary.

### Invariants And Boundaries

- Do not register exact-id terminal adapters as public agent cognition.
- Assignment has no leaf-key compatibility shape.
- Structural authorization occurs before internal runtime mutation.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Internal assignment carries session correlation plus structural binding. [1]
- Legacy internal spawn/retire/rename primitives remain behind the structural application. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
