# mcp/src/agents_remember/worktrees/modules/context.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Resolves coordination context for worktree lifecycle operations.

## Code Commentary

`resolve_context()` adapts the typed `WorktreeArgs` dataclass (from
`agents_remember.worktrees.modules.args`) to the kernel resolver.
`contract_context()` reconstructs context from a persisted worktree contract
and, for external-memory tasks, reparses settings from the memory worktree when
that task branch changed memory settings.

Since 260731-EFA-L2 both calls use the resolver's two parameter objects (from
`kernel.coordination_context_resolver`). `resolve_context` passes
`hints=CoordinationHints(topology=…, coordination_root=…)` plus an
`EnclosureSelector(contract_path, task_name, parent_task, leaf_id, worktree_name)` built from the
same `getattr(args, …, None)` reads as before; `contract_context` passes
`selector=EnclosureSelector(contract_path=contract.contract_path)`. This module is the
`WorktreeArgs`-to-resolver adapter, so it is where a new worktree-side resolution input gets
mapped onto a resolver bundle.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The kernel resolver facade and the coordination-context builder own topology, storage, path rules, and cross-repo resolution. [1]
- Closeout preview resolves candidate-rooted context for route-index and sidecar classification. [2]
- Closeout replaces the resolved context's code root with the task worktree. [3]
- The external-memory phase resolves that contract context before refreshing onboarding and running post-refresh quality. [4]

## Series-Contract Notes

The context wrapper forwards `parent_task` and `leaf_id` from `WorktreeArgs` to the resolver before operation modules build or load contracts.
