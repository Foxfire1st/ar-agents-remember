# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/git-workspace.ts

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/lib/git-workspace.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### Application-side git workspace helper

A library helper of the AR-owned eve application that gives the running agent a git-shaped view of
its workspace. It is application code inside the image installed at
`<coordination_root>/runtime/eve-agent`; the worktree authority itself remains the MCP-owned
worktree tools, and this helper does not create, move or clean up a worktree.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/lib/git-workspace.ts` is the authored
  source.
- Read/assist helper only: worktree lifecycle authority stays with the MCP worktree tools.

## Evidence

### Repo-Internal References

- The generated mirror of the application tree this helper belongs to, and the target that produces it. [1]
- The generator declares the `eve-runtime` target with its per-target ignore set. [2]
