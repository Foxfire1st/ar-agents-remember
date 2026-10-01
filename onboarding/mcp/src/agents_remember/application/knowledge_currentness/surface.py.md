# mcp/src/agents_remember/application/knowledge_currentness/surface.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The `currentness` block the two read surfaces attach for a converted memory tree (MIK-R03 rule 4).**
`knowledge_read` and the published-intent block of `read_ar_files` both read a converted tree through its
derived index, whose projection names records by UUID (MIK-R23 rule 6). This module finds the invariants
and families an answer returns, computes their state with `invariant_currentness`, and returns the block.

## Code Commentary

### Logic

- **What a read returns (architect ruling 3, 18:42:37).** `returned_records(index, answer)` walks every
  string in the answer, keeps the UUIDs, and translates each through the index's reverse map
  (`index.text_id`). Those that name an invariant or family record are returned; a family-membership row
  (a text ID containing `/`), claim, anchor and member UUIDs are ignored. The counts therefore cover every
  invariant the answer carries, whether it names the invariant (for example as a relationship) or returns
  it in full, plus every member of a family it carries (review N5, 19:13:41).
- **Which tree `knowledge_read` asks at (ruling 2, 18:42:37).** `requested_code_tree(code_tree_id,
  repository_root, default_repository)` counts only a named `codeTreeId`. A `repositoryRoot` alone, or
  nothing, requests nothing, so the block is `unverifiable`; `HEAD` is never substituted. A tree named
  without a repository is read from the mount's workspace object store.
  **Since MIK-R02 no production path calls `requested_code_tree` or `read_currentness`:** the
  converted-tree `knowledge_read` applies the same rule in `knowledge_paging/tree_read.py` (`_at_code_tree`:
  only the named `codeTreeId`, or the continuation's tree on a resumed page) and computes the block through
  `evaluate_answer`. Both functions stay exported, and L03's tests still exercise them.
- **The published-intent block's tree (ruling 1, 18:42:37)** is chosen by its caller, `published_intent.py`:
  the tree that route already resolved for the source it returns. This module takes whatever `CodeTree`
  it is given.
- `read_currentness(index_path, tree_key, code_tree, answer)` opens the index for that tree key, collects the
  records, and returns `invariant_currentness(...).to_document()`.
- **It never raises (ruling N2, 19:13:41).** An index, SQLite, file-system, `ValueError` or
  `SubprocessError` failure (`CURRENTNESS_FAILURES`, public since MIK-R02; `IndexMismatchError`, `MemoryTreeError`,
  `KnowledgeStorageError` and `CodeReadError` are all `ValueError`s) returns a block with the `codeTree`,
  zero counts, no invariants or families, and `unverifiableReason` "currentness could not be computed
  (<type>: <message>)". With no readable index there are no entries to attach a per-entry reason to, so the
  reason is stated once for the block (the worker's deviation, accepted in review round 2).
- **The seam MIK-R02 extracted (260928-MIK-L02, ruling F3 of 2026-09-29 20:40:40).** A bounded page is found
  by rendering candidate pages, and each candidate carries its `currentness`, so the evaluation is split
  out to run once per page: `named_uuids(answer)` (every projected UUID), `record_of(index, value)` (the
  `(kind, ID)` one UUID names, or `None`), `evaluate_answer(index_path, tree_key, code_tree, answer)` (every
  named record by UUID plus their `Currentness`; it raises the failures instead of degrading) and
  `failure_document(code_tree, error)` (the degraded block). `returned_records` and `read_currentness` are
  rebuilt on these helpers and behave as before: L03's `test_knowledge_currentness.py` passes unchanged,
  and the index is still opened through this module's `KnowledgeIndex`, so its failure injection holds.
  The caller is `application/knowledge_paging/currentness.py` (`WalkCurrentness`).

### Conventions

- The answer is passed in already dumped to JSON (`knowledge_read` dumps its payload once, review N6).

### Invariants And Boundaries

- **A currentness failure never refuses a read.** The block is advisory beside the answer.
- **The answer is never edited**, so every invariant stays visible with its statement and relationships
  whatever its state (D9).
- **No fallback to `HEAD` or the working tree** for a missing code tree.

### Todos

- None recorded. MIK-R29 may add an explicit tree selector to `read_ar_files` (ruling 1, 18:42:37).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: returned records are the UUIDs the index translates, and the answer is never edited. [1]
- Every failure class the step degrades on, now public for the paged caller. [2]
- The records an answer returns, built on the per-UUID helper. [3]
- The UUIDs an answer carries, and the index's reverse map for one. [4]
- The one evaluation a paged caller cuts candidates from; it raises instead of degrading. [5]
- Only a named tree ID is a request; `HEAD` is never substituted. [6]
- The block, which degrades to the failure document and never raises. [7]
- The degraded block's reason text. [8]
- The `knowledge_read` consumer since MIK-R02: currentness once per page at the walk's code tree. [9]
- The published-intent consumer since MIK-R02, at its resolved source tree and inside the bounded block. [10]
- No tree, or only a repository, is unverifiable and never reads `HEAD`. [11]
- A failing step degrades to a reason and never refuses the read. [12]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one memory tree's index and one code tree,
both named by its caller.

No cross-repo boundary is crossed by this file.
