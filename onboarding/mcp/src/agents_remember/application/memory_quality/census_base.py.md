# mcp/src/agents_remember/application/memory_quality/census_base.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

**The memory census's comparison base on a converting leaf: K_B's conversion, as a Git tree (MIK-R24 rule 7; L37
fix round P1b).** The census compares the memory candidate with the leaf's baseline commit to find what the task
edited. When the candidate is converted and the baseline is not, every card differs only because it was converted,
and the census counted each one as a task edit with no metadata (2,509 false blockers at the cutover leaf's intake).
This module supplies the tree the census compares with instead.

## Code Commentary

### Logic

- `census_comparison(contract)` returns a `MemoryComparison`: `(repository, baseline, candidate tree) -> tree-ish`.
  It returns the baseline itself when the candidate holds no layout marker or the baseline already holds one
  (`_layout_version`). Otherwise it takes the conversion's files from
  `knowledge_worklist.base_cache.converted_base_files` (the code is the contract's code repository at its code
  base commit; the cache is the coordination root's shared one) and returns `_overlay(repository, baseline, files)`.
- `_overlay` builds the comparison tree: the baseline's tree with the converted kinds replaced. Every path the
  cache holds (onboarding Markdown and the knowledge JSON) is taken from the conversion; every other path of
  `knowledge/` and `onboarding/` that is not a cached kind (`is_cached_path`), and everything outside those two
  directories (`system/`, `docs/`, the frozen database), stays the baseline's own.
- `_hash` writes the conversion's files as blobs (`hash-object -w --stdin-paths`), and `_make_trees` writes the
  trees deepest directories first, one `mktree --batch` per depth, and returns the root tree.

### Conventions

- The comparison is bound by the application layer (`application/memory_quality/census.py`) into
  `memory_quality/memory_census_scope.capture_memory_census_scope`, which cannot reach the converted-base cache.

### Invariants And Boundaries

- **Only objects are written.** No ref, index or working tree of the memory repository is touched, and the same
  inputs always give the same tree. The loose objects are unreferenced and are collected by `git gc`.
- **A conversion that cannot be built is a named failure**: "the memory census cannot compare the converted
  candidate with its base: the conversion of `<commit>` (MIK-R24 rule 7) cannot be built". The census never falls
  back to the raw baseline.
- A memory path that holds a newline refuses the tree.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R24@v1` rule 7 and the L37 decision of 2026-10-01T10:06:02 in `37_cutover-to-text-storage.json`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: why the census compares with K_B's conversion, and that only objects are written. [1]
- The comparison base for a contract: K_B, or its conversion. [2]
- The baseline's tree with every cached kind replaced by the conversion. [3]
- The root tree, built deepest directories first. [4]
- The census scope is captured with this comparison. [5]

### Cross-Repo References

No meaningful cross-repo references found: the module writes Git objects into one memory repository.

No cross-repo boundary is crossed by this file.
