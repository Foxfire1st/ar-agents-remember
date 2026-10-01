# mcp/tests/test_knowledge_currentness.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R03 cases: stale invariants flagged at read time, over real Git code and a converted memory
tree.** Thirteen cases cover each entry state, the rule-2 precedence, `unrealized`, stale proofs, the
per-side computation, the observation cache key, Git failures, and the two read surfaces
(`knowledge_read` and the published-intent block). The module is in the `unit-regression` lane.

## Code Commentary

### Logic

- **The world.** Each case builds a real code repository (`pkg/review.py`, whose four functions
  `_not_listed`, `other`, `third` and `fourth` each realize their own invariant; `tests/test_review.py`,
  whose test proves one of them; a text file with a line-range anchor; a Markdown file with a symbol
  anchor) and a converted memory tree anchored at the code's first commit (`World`, `world`,
  `_memory_files`). A case then commits code changes the way raw Git would, outside any managed flow.
- **Entry states.** The packet's conforming example (`_body_edit` changes only `_not_listed`: exactly that
  invariant is stale and names its entry; the other three stay current); stale for an absent path, an
  ambiguous symbol and an unmappable range; `unverifiable` with a named reason for no tree, an unreadable
  tree and an unsupported locator.
- **The ruling-N1 order is pinned by `INV-HHHHHH`** (a symbol in Markdown): an unchanged blob is `current`,
  a changed blob is `unverifiable` ("no shipped grammar reads it"), a deleted file is `stale`.
- **Failures (ruling N2).** A patched `TimeoutExpired` gives an `unverifiable` entry, and the next read
  observes again (never cached). A patched `IndexMismatchError` in `knowledge_read` still returns
  `state: view` with its payload and a degraded block.
- **Surfaces.** `knowledge_read` with `codeTreeId` flags the stale invariant and keeps its statement;
  without a named tree, or with only `repositoryRoot`, it is `unverifiable` with compact entries even though
  `HEAD` holds the edit. The published-intent block names its resolved tree and the `treeScope` text; an
  uncommitted edit leaves every state unchanged; with no resolved tree it is `unverifiable`.

### Conventions

- The state-function cases pass a private cache (the `World` helper defaults to a fresh
  `BoundedMemo(1024)`), so they do not share cached answers. The surface cases go through the
  process-wide `OBSERVATIONS`.

### Invariants And Boundaries

- Every Git write is to the case's own temporary repository.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: real Git code, a converted memory tree, raw-Git edits. [1]
- The fixture world, with a fresh private cache by default. [2]
- The packet's conforming example. [3]
- Stale reasons. [4]
- Unverifiable reasons and the N1 order. [5]
- Git failures and no caching of them. [6]
- A missing recorded line-range blob. [7]
- Precedence and `unrealized`. [8]
- Stale proofs. [9]
- Per side. [10]
- The cache key. [11]
- `knowledge_read` with a named tree. [12]
- `knowledge_read` without one. [13]
- The published-intent block. [14]
- A failing step never refuses. [15]
- The lane row. [16]

### Cross-Repo References

No meaningful cross-repo references found: every case works in its own temporary repositories.

No cross-repo boundary is crossed by this file.
