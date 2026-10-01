# mcp/tests/test_knowledge_index_surfaces.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rule 6 at the worklist scope and the mounted tools.** `construct_registered_scope` over the index through the adapter, retired records never presented as live, and `knowledge_read`, `knowledge_diff` and `knowledge_project` resolving a `databasePath` that names a converted memory tree while keeping today's behaviour for everything else. Registered in the `unit-regression` lane; 10 collected cases.

## Code Commentary

### Logic

- **Registered scope** (parametrized `same-sides` and `candidate-changed`): the scope over the parity database and over its converted tree (base the Git tree, candidate the working tree) has the same members and followed edges, keyed by legacy ID, path, locator, side and edge kind; in the changed case the keys differ and the candidate contributes more edges.
- **Retired records:** a retired invariant and its claim are not projected and not selected by a path read, while the index answers the record as `retired`; a retired family is not projected and is still answered with its members.
- **Mounted tools:** a read by root and by the `knowledge.sqlite` spelling returns a family view with `memoryTree` and writes exactly one cache file named by the key, and is refused without a coordination root; diff between two tree directories names both sides in `memoryTrees` and project publishes with `memoryTree`; an unconverted selection gets today's `selected_input_unavailable` with no `memoryTree` and no cache.
- **Partial and unbuildable:** every surface reports a partial index as incomplete (read: `completeWithinDeclaredScope`, the payload's completeness and `indexComplete` all `false`; diff and project: `indexComplete: false`), with a complete control; with the coordination root pointing at a file, diff and project return `state: refused` rather than raising.
- **Preservation:** a store-authored `knowledge.sqlite` in an unconverted Git root reads identically with and without a coordination root, with no new fields and no cache directory.
- **L37 (P2 task 4).** `test_a_converted_tree_refuses_a_seed_it_does_not_hold_and_a_database_read_is_unchanged`:
  on a converted tree a database-era UUID, a bare `INV-…`, a family UUID and an unheld family are each refused
  `selector_absent`, naming where seeds come from, for `knowledge_read` and for the view seeds of
  `knowledge_project`; a database read with an unknown seed is still `view` and complete.

### Conventions

- `_converted` and `_partial` build converted trees from the support module; `_canonical` and `_canonical_scope` spell a scope from either side's connection.

### Invariants And Boundaries

- The unconverted-root case uses a real store-authored database, not a fixture file, so the preservation boundary is measured on the shipped path.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases.

- The registered scope over the index equals the scope over the database. [1]
- Retired records are never live. [2]
- The mounted tools over converted and unconverted selections. [3]
- Partial and unbuildable indexes on every surface. [4]
- A real database in an unconverted root reads identically. [5]
- The lane row. [6]

- A converted tree refuses a seed it does not hold, and a database read is unchanged. [7]

### Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

No cross-repo boundary is crossed by this file.
