# mcp/src/agents_remember/serving/conversation/active/projector/__init__.py

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Preserves the former `active.projector` import surface after the implementation moved into a
package.

## Code Commentary

### Logic

Re-exports `ActiveSessionProjector`, `PageResult`, the close sentinel, and the two ordering
exceptions used by callers and tests. It contains no runtime state or forwarding behavior beyond
Python package exports.

### Conventions

Only intentionally public names belong in `__all__`.

### Invariants And Boundaries

- Existing imports from `agents_remember.serving.conversation.active.projector` keep working.
- Implementation ownership stays in the named component modules.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Public implementation facade. [1]

### Cross-Repo References

No meaningful cross-repository references found.
