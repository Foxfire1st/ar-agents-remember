# mcp/tests/test_knowledge_index_reuse.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rule 6: the existing read, view and comparison code runs over the index unchanged.** Parity against a legacy database fixture, the view seam and the two-snapshot comparison over index files, and the ordinary read's published-memory selection of a converted tree. Registered in the `unit-regression` lane; 6 collected cases.

## Code Commentary


A parity fixture compares selected sets and source-path counts over its test dataset and the index projected from converted text. Views read that index, and a comparison binds two distinct tree indexes. These are read-side parity assertions over a constructed fixture, not production canonical authoring.

The ordinary converted-tree read returns a complete index and bounded selection; a malformed record names a partial index. An unconverted root instead returns unusable/legacy-format with empty seeds and preserves the retired database bytes. It creates no runtime index there. Legacy selection is refused rather than kept as an alternate readable database route.

### Logic

- **Parity:** `build_parity_dataset` writes a store-authored database; `convert_dataset` turns it into a converted Git tree. `select_recorded_scope` runs for path, invariant and family seeds over both; the selected items are compared keyed by legacy ID, statement, guarantee, path, locator, role and rationale (`_database_key`, `_index_key`), and must be identical.
- **Views and comparison:** the family, source_context and invariant views return `state == "view"` over the index; a comparison between a committed tree and an edited working tree returns the new statement with no refusal.

### Conventions

- `_context` builds a `CoordinationContext` whose coordination root is under `tmp_path`, so the cache is outside the repository.

### Invariants And Boundaries

- The comparison is non-empty and keyed by the legacy identities the converted records carry, so parity cannot pass vacuously.

### Todos

None recorded.

## Evidence


### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_reused_selection_selects_the_same_set_over_the_index_as_over_the_database` supplies the current fixture or assertion described above. [6]
- `test_the_ordinary_read_selects_a_converted_memory_tree_through_its_index` supplies the current fixture or assertion described above. [7]
- `test_a_partial_tree_selection_says_it_is_partial` supplies the current fixture or assertion described above. [8]
- `test_an_unconverted_memory_root_refuses_the_retired_database_selection` supplies the current fixture or assertion described above. [9]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases and their keys.


- The parity keys on each side. [10]

- The reused selection selects the same set over the index as over the database. [11]

- Views and the comparison over index files. [12]



### Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

No cross-repo boundary is crossed by this file.



- The lane row.  Anchor: `test_knowledge_index_reuse` [13]
