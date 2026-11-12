# mcp/src/agents_remember/kernel/primitives/observer_paths.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/observer_paths.py` resolves the observer store root — the one read/write path
abstraction (260731-EFA-L9 moved it into kernel so the serving projection readers, the observer
write side, worktrees, and memory quality resolve the same roots without crossing packages).

## Code Commentary

### Logic

`observer_logs_root` (cit:([`observer_logs_root`], mcp/src/agents_remember/kernel/primitives/observer_paths.py:34-34)) resolves `logs/observer` under the
coordination root; `observer_root` resolves the observer root from the runtime config;
`drift_snapshot_dir` (cit:([`drift_snapshot_dir`], mcp/src/agents_remember/kernel/primitives/observer_paths.py:44-44)) resolves the drift-snapshot directory; and
`LANDING_FINAL_BASENAME` names the immutable landing-final file.

### Conventions

- Dependency-light: no reducer/snapshot/store imports; callers combine these paths with their own
  I/O.

### Invariants And Boundaries

- A future synced coordination store is a swap at this one site, not a refactor of every reader.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The projection readers use these paths after the observer→serving move. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
