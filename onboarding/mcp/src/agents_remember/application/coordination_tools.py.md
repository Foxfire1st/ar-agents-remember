# mcp/src/agents_remember/application/coordination_tools.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`coordination_tools.py` exposes the `resolve_context` MCP application entry point.

## Code Commentary

`resolve_context_tool(config, task: TaskRef, *, worktree_name=None, topology=None)` — since
260731-EFA-L2 the five locators arrive as one `TaskRef` (`application/task_ref.py`), shared with
`worktree_attach_tool` and `worktree_status_tool`. `worktree_name` and `topology` stay separate
because neither identifies the task. The resolver call itself now passes
`hints=CoordinationHints(...)` and `selector=EnclosureSelector(...)` instead of five loose keywords.

The application entry point validates the requested repo ID against MCP settings via
`require_repo()` and confines an optional contract path under the coordination
root via `require_within_coordination()` — both now imported from the shared
`agents_remember.kernel.authority` module rather than defined locally (the
former private `_repo` / `_coord_path` helpers were removed). It then narrows
topology to supported values with `_topology()`, calls
`resolve_coordination_context()`, and serializes the result with
`context_to_dict()`. The guards raise `AuthorityError` (not `ValueError`) when a
repo is disallowed or a path escapes the coordination root.

## Invariants And Boundaries

- MCP settings are the authority for allowed repos and workspace roots; repo
  resolution and path confinement run through the shared `kernel/authority.py` module so the
  security boundary is written and reviewed once.
- Caller-provided coordination paths must remain under the configured
  coordination root; a disallowed repo or an escaping path raises
  `AuthorityError` rather than a generic `ValueError`.
- Topology values should stay explicit rather than free-form strings.

## Evidence

### Repo-Internal References

- Runtime/coordination response models include `ResolveContextResponse`. [1]
- Coordination context resolver owns the actual context construction. [2]
- `require_repo` and `require_within_coordination` (repo resolution and path confinement) now live in the shared `kernel/authority.py` module. [3]
- `AuthorityError` is the authority-violation error type the guards raise. [4]

## Series-Contract Notes

The context application entry point still resolves nested active task roots and a specific leaf enclosure —
`parent_task` and `leaf_id` now travel inside the `TaskRef` through the same trusted config-bound
resolver path, preserving task-name ergonomics.
