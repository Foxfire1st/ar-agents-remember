# mcp/src/agents_remember/kernel/primitives/drift_snapshot.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/drift_snapshot.py` owns the drift-snapshot path and removal primitives,
created by 260731-EFA-L9 so the serving projection readers, worktrees, and memory quality can
resolve and remove drift snapshots without crossing packages.

## Code Commentary

### Logic

`sanitize_report_token` (cit:([`sanitize_report_token`], mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:15-15)) makes a report token filesystem-safe;
`drift_snapshot_path` (cit:([`drift_snapshot_path`], mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:21-21)) resolves the per-repository, per-branch
snapshot path under the coordination root; `remove_drift_snapshot`
(cit:([`remove_drift_snapshot`], mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:27-27)) deletes it with a `missing_ok`-style guard.

### Conventions

- Pure path/side-effect primitives with no repository knowledge; callers own the schema.

### Invariants And Boundaries

- The snapshot filename must stay deterministic from `(repository, branch)` so drift checks and
  pruning agree on the same file.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The projection-side pruning policy consumes these primitives. [1]
- Snapshot removal is owned by this primitive; no deleted-suite removal-edge coverage is asserted. [2]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
