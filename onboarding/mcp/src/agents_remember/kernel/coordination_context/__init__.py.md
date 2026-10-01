# mcp/src/agents_remember/kernel/coordination_context/__init__.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`__init__.py` marks `coordination_context/` as the focused implementation
package behind the public `c-08-ar-coordination-context-resolver` skill resolver facade.

## Code Commentary

### Logic

The module is intentionally declarative and contains no import-time wiring.

### Invariants And Boundaries

- Keep implementation ownership in the sibling modules.
- Keep public compatibility exports in `coordination_context_resolver.py`.

## Evidence

### Docs References

No external documentation is needed for a package marker module.

No relevant external documentation is needed.

### Repo-Internal References

### Cross-Repo References

No cross-repository evidence is needed for this package marker.

No meaningful cross-repo references found.
