# mcp/src/agents_remember/kernel/coordination_context_resolver.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`coordination_context_resolver.py` is the public `c-08-ar-coordination-context-resolver` skill resolver facade and
`python -m` entrypoint for one configured repository.

## Code Commentary

### Logic

The module re-exports the stable public API from
`agents_remember.kernel.coordination_context.*`, delegates command-line
execution to `coordination_context.cli`, and preserves the existing
`agents_repo_from_script` monkeypatch seam used by resolver tests. The actual
resolution, settings parsing, storage decisions, cross-repo checks,
serialization, and contract loading now live in focused modules under
`coordination_context/`. The re-exported contract helpers are `resolve_contract`,
`find_task_contract`, and `find_worktree_contract` (the worktree-name fallback),
all kept in sync in `__all__`.

Since 260731-EFA-L2 the facade's `resolve_coordination_context` mirrors the resolver's new
signature — `(code_repository_name=None, workspace_root=None, code_repository_root=None, *,
hints: CoordinationHints | None = None, selector: EnclosureSelector | None = None)` — forwarding
the two bundles through `_with_facade_agents_repo` as keywords while the three repository
arguments stay positional. `__all__` gained the four new model names: `CodeRepository`,
`CoordinationHints`, `CoordinationRoots`, `EnclosureSelector`. Importing them from this facade is
the supported path for callers outside the `coordination_context` package.

The cross-repo re-export is `git_head_or_empty` (formerly `git_head`), and the
storage re-export is the boolean predicate `is_sidecar_storage` (the former
`sidecar_storage_label` is no longer re-exported); both names are kept in sync
in `__all__`. The `_with_facade_agents_repo` swap is documented in-source as an
identity rebind under normal use (the facade re-exports `agents_repo_from_script`
from `_paths`) that stays load-bearing only as a test seam: patching the
facade-level name propagates into `_paths`, where `resolve_coordination_root_hint`
invokes it.

### Invariants And Boundaries

- `c-08-ar-coordination-context-resolver` skill is facts-only and does not mutate Git, onboarding, or worktree state.
- Source-checkout `.env` files are not resolver authority; MCP settings or an
  explicit coordination root own that path.
- Resolver behavior must not depend on deleted skill-local `_shared` paths.
- Missing supported memory roots should fail explicitly instead of fabricating a
  usable context.
- New implementation logic belongs under `coordination_context/`; this file
  stays a facade for imports and module execution.

## Evidence

### Repo-Internal References

- The compatibility facade exposes the package resolver entry point. [1]
- The facade delegates context resolution through its current canonical package owner. [2]
- Focused implementation modules live under the coordination-context package. [3]

## Series-Contract Notes

The compatibility facade preserves the old import path while forwarding `parent_task` and `leaf_id` into the focused resolver package.
