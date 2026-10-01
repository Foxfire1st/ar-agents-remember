# mcp/src/agents_remember/serving/control_plane_identity_migration.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Performs the bounded startup migration of existing control-plane logs from leaf/runtime-oriented
address fields to canonical task-document structural fields before strict readers open them.

## Code Commentary

### Logic

`migrate_control_plane_identity_logs` constructs an `IdentityMigrationContext`, visits the known
durable record families, derives task references from authoritative catalog/topology evidence, and
rewrites only recognized legacy rows. `_migrate_row` and `_address_ref` keep mapping decisions
explicit and idempotent.

### Conventions

Migration is a one-way deployment boundary, not a permissive reader fallback. Strict current models
remain strict after migration.

### Invariants And Boundaries

- Run before strict control-plane stores parse durable rows.
- Prefer an exact catalog binding; otherwise map recognized orchestration roles to the altitude that
  can be derived from the legacy leaf, leaving unresolved/non-orchestration addresses leaf-local
  for subsequent strict model validation.
- Do not preserve dual current/legacy write schemas.
- Re-running produces no additional changes.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Startup log migration is explicit and context-bounded. [1]
- Row mapping is one-way and field-specific. [2]

### Cross-Repo References
