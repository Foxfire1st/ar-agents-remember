# mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T08:05+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Owns no-follow filesystem preflight, legacy projection removal, and recursive inventory for immutable
quality-report publication.

## Code Commentary

### Logic

`preflight_report_destination` rejects symlinks or irregular nodes at the exact destination,
generation-directory, candidate-generation, and declared legacy-projection boundaries supplied to it.
`remove_legacy_report_projection` deletes only declared former projection paths. `report_tree_inventory`
classifies files, directories, and irregular entries without following links.

This helper does not claim ownership of the complete historical-generation population. The clean
executor inventories, preflights, and prunes every managed 64-hex historical generation before
calling the final pointer replacement; that separate owner closes the population that this exact-path
helper intentionally does not traverse.

### Conventions

The publisher supplies the exact allowlisted file and directory sets; this helper supplies path
safety rather than another report schema.

### Invariants And Boundaries

- Supplied destination, exact generation, nested directory, and file boundaries are inspected
  without following links.
- Historical-generation population validation belongs to the clean executor's prune preflight, not
  to this exact-path helper.
- Legacy cleanup cannot recursively erase undeclared directories.
- Inventory preserves relative nested identity.
- Irregular nodes remain explicit refusal input.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Publication preflight covers each exact boundary supplied by the publisher. | `preflight_report_destination` | mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py:14-39 |
| Recursive inventory separates regular and irregular entries. | `report_tree_inventory` | mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py:62-78 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-31T08:05+02:00 — Corrected A003's overbroad claim: this helper validates supplied exact
  paths, while clean-executor pruning owns the complete historical-generation population.

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
