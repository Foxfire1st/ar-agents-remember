# mcp/src/agents_remember/application/knowledge_paging/currentness.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R03 currentness for the pages of one walk, computed once and cut to each candidate page.** A bounded page that carries a `currentness` block is measured with it, so the block counts toward the threshold (ruling F3, 20:40:40).

## Code Commentary

### Logic

- `WalkCurrentness(index_path, tree_key, code_tree, candidates)` calls `knowledge_currentness.surface.evaluate_answer` once over every row the page could carry, at the walk's code tree: the tree the caller named on a fresh view read, the token's tree on a resumed page, and the source-resolution tree for the published-intent block.
- `subset(answer)` (since MIK-R01) returns the subset as a `Currentness` object, or `None` when the one evaluation failed; `document(answer)` renders it, or the failure document. `knowledge_leaf/currentness.py` merges this scope subset with a leaf subset when one `read_ar_files` block carries both identity seeds and path seeds. The rendered block is unchanged in output.
- `document(answer)` returns the subset block for one candidate answer: the same records and order `read_currentness` would compute for that answer, with each family's stale members counted over all its members. The reviewer compared 13 real pages and found them equal to `read_currentness`.
- A failure of the one evaluation (`CURRENTNESS_FAILURES`) becomes the `failure_document` for every candidate, so currentness never refuses a read.

### Conventions

- Once per page, never once per cutting iteration (ruling F3).

### Invariants And Boundaries

- Currentness is advisory beside the page; it never edits the rows and never refuses the read (MIK-R03).

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: once per walk page, cut to each candidate. [1]
- The one evaluation, and its failure document. [2]
- A candidate's subset block. [3]
- The subset as an object, for the merge with a leaf subset (MIK-R01). [4]

### Cross-Repo References

No meaningful cross-repo references found: the evaluation reads one memory tree's index and one code tree.

No cross-repo boundary is crossed by this file.
