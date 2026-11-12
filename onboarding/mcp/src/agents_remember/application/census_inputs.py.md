# mcp/src/agents_remember/application/census_inputs.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

**Capture what a census reads, so its receipt names its actual inputs (MIK-R198 rule 1).** A census answering against a directory path proves nothing about what it read: the tree can move while it is measured, and a path is not an identity. `measured_census` enumerates both sides once — a Git working-tree tree read back by object ID, or a plain directory captured as a byte map — runs the product census over those captured trees, and returns the census beside the `CensusInputs` the artifact writer records.

## Code Commentary

### Logic

- `_capture(root)` answers `(identity, files)`. A Git root yields its identity and no byte map, because the tree object is immutable and is read back through Git. An unreadable root raises `KnowledgeTreeReadError`, and a Git root whose working-tree tree object could not be built raises rather than degrading to a directory identity. A plain directory is captured, then re-digested from the captured bytes, so the identity names exactly the bytes the parser and resolver consume.
- `measured_census(memory_root, code_root)` builds the memory and code trees from the capture: `knowledge_tree_from_git` and `code_tree_from_git` at the captured tree object for a Git side, `KnowledgeTree` and `CodePathSet` over the captured byte map for a directory side. Only knowledge paths enter the directory memory tree, through `is_knowledge_path`.
- The census runs over the captured trees, never over the mutable paths whose identities were sampled, and its `inputIdentities` carries the capture. `CensusInputs.stable` is diagnostic: it is the comparison of a second live `pair_identities` measurement against the captured ones, so it can report a change that did not affect what was read, and cannot report a change that was later reverted.

### Conventions

- A capture that cannot be read raises `KnowledgeTreeReadError` naming the root; neither side falls back to a weaker identity.
- The returned `CensusInputs` is the only value the artifact writer takes for `artifactInputIdentities` and `artifactPairStableDuringRead`, so the receipt and the census cannot disagree about what was measured.

### Invariants And Boundaries

- **The census's denominator and targets come from bytes captured before it ran.** A live edit during the read cannot rebind them, whether or not it is reverted afterwards.
- **`stable` is diagnostic, not a completeness proof.** Endpoint equality cannot establish what a census read; the captured identities are what the answer's claim rests on.
- **A failed capture is a named error, never a partial tree.** A scratch index that Git refused to write does not become the measured memory tree.

### Todos

None recorded.

## Evidence

- The one entry point: capture both sides, census the captured trees, and carry the identities beside a diagnostic stability flag. [1]
- A Git side is captured as an immutable identity, a plain directory as its own bytes. [2]
- A Git root with no working-tree tree raises rather than degrading to a directory identity. [3]
- The memory side of a Git pair is read from the captured tree object. [4]
- Only knowledge paths form the directory memory tree. [5]
- A plain code directory becomes a path set over the same captured bytes. [6]
- The census carries the identities its capture read and the live comparison that qualifies them. [7]
- A live change during the read cannot rebind the captured census, whether or not it is restored. [8]
- A quiet pair yields reproducible identities, and a refused capture raises instead of measuring a partial index. [9]
