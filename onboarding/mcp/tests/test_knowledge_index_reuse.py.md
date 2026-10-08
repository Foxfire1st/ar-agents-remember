# mcp/tests/test_knowledge_index_reuse.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Pins reuse of the existing read, view and comparison logic over converted memory-tree indexes.

## Code Commentary

A parity fixture compares selected sets and source-path counts over its test dataset and the index projected from converted text. Views read that index, and a comparison binds two distinct tree indexes. These are read-side parity assertions over a constructed fixture, not production canonical authoring.

The ordinary converted-tree read returns a complete index and bounded selection; a malformed record names a partial index. An unconverted root instead returns unusable/legacy-format with empty seeds and preserves the retired database bytes. It creates no runtime index there. Legacy selection is refused rather than kept as an alternate readable database route.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_reused_selection_selects_the_same_set_over_the_index_as_over_the_database` supplies the current fixture or assertion described above. [6]
- `test_the_ordinary_read_selects_a_converted_memory_tree_through_its_index` supplies the current fixture or assertion described above. [7]
- `test_a_partial_tree_selection_says_it_is_partial` supplies the current fixture or assertion described above. [8]
- `test_an_unconverted_memory_root_refuses_the_retired_database_selection` supplies the current fixture or assertion described above. [9]
