# mcp/tests/test_knowledge_index_reuse.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rule 6: the existing read, view and comparison code runs over the index unchanged.** Parity against a legacy database fixture, the view seam and the two-snapshot comparison over index files, and the ordinary read's published-memory selection of a converted tree. Registered in the `unit-regression` lane; 6 collected cases.

## Code Commentary

### Logic

- **Parity:** `build_parity_dataset` writes a store-authored database; `convert_dataset` turns it into a converted Git tree. `select_recorded_scope` runs for path, invariant and family seeds over both; the selected items are compared keyed by legacy ID, statement, guarantee, path, locator, role and rationale (`_database_key`, `_index_key`), and must be identical.
- **Views and comparison:** the family, source_context and invariant views return `state == "view"` over the index; a comparison between a committed tree and an edited working tree returns the new statement with no refusal.
- **Published intent:** `published_intent_block` over a converted memory root selects the tree through its index (with `memoryTree`), and the path's page is the family-complete leaf read, whose statements the case reads from `rows` (since 260928-MIK-L01, MIK-R01; formerly the scope read's `items`); a partial index's pages carry `indexState: partial` and `enumerationComplete: false`; an unconverted memory root keeps the database selection.

### Conventions

- `_context` builds a `CoordinationContext` whose coordination root is under `tmp_path`, so the cache is outside the repository.

### Invariants And Boundaries

- The comparison is non-empty and keyed by the legacy identities the converted records carry, so parity cannot pass vacuously.

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

The cases and their keys.

- The parity keys on each side. [1]
- The reused selection selects the same set over the index as over the database. [2]
- Views and the comparison over index files. [3]
- The published-memory selection: converted, partial and unconverted. [4]
- The lane row. [5]

### Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

No cross-repo boundary is crossed by this file.
