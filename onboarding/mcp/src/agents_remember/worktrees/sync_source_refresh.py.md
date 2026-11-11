# mcp/src/agents_remember/worktrees/sync_source_refresh.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file centralizes the bounded pre-lock upstream refresh shared by direct sync and atomic-series
selecting admission. It updates remote-tracking evidence without confusing fetch results with local
protected-source authority.

## Code Commentary

### Logic

`fetch_source_upstreams(contract, sync_source)` builds the code target and optional external-memory
target, resolves each source branch's configured upstream, and reports `no-upstream`, `fetched`, or
`failed` per side. A source branch is the contract's own source line, or with
`sync_source="repository-default"` the repository's default branch (`source_strategy(sync_source).source_branch`: the code repository's
default and the memory repository's default), because that is the line the sync will pull. A default
that cannot be resolved (`BranchAuthorityUnavailable`) is reported as `default` with state
`unresolved` and the error text, never raised, and any target built before it is still fetched; the
sync admission answers it by name. Offline or remote-less state is returned as evidence; later sync proceeds from exact local
branch facts pinned only after repository integration authority is acquired.

### Conventions

Fetch is best-effort and result-shaped, never a mutation admission decision. The shared helper avoids
duplicating subtly different pre-lock fetch loops across selecting and explicit sync surfaces.

### Invariants And Boundaries

- This helper never reads or moves a local work/source branch.
- A failed fetch is not silently treated as a successful refresh.
- Local source tips, not remote-tracking refs, remain transaction authority.

### Todos

Final call sites are reconciled to the frozen source; verification remains empty until the real
code commit exists.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Selecting admission refreshes before acquiring integration authority and then re-reads the contract. [1]
- The sync module consumes fetched evidence while pinning local sources under authority. [2]

### Cross-Repo References

No cross-repository source is configured for this memory root.
