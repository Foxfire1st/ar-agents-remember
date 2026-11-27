# mcp/tests/test_knowledge_currentness.py

## Governing Overview

[tests route overview](overview.md)

## Current naming and source qualification

The IndexMismatchError case still returns state view and a degraded currentness reason, with INV-AAAAAA/RLZ-A00001 named and statement absent. The separate internal published_intent_block case retains full seeds/statement and distinguishes committed-tree from captured-working-tree observation; that is not the public MCP naming answer.

## Current source contract evidence


- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred.


## Purpose

**The MIK-R03 cases: stale invariants flagged at read time, over real Git code and a converted memory
tree.** Fourteen source test definitions cover each entry state, the rule-2 precedence, `unrealized`, stale proofs, family currentness, the
per-side computation, the observation cache key, Git failures, and the two read surfaces
(`knowledge_read` and the published-intent block).

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
- **Surfaces.** `knowledge_read` with codeTreeId keeps the stale invariant/realization visible as named IDs and states, without its statement text; the invariant currentness entry list includes both realization RLZ-A00001 and proof PRF-P00001. Without a named tree, a read with a resolved code root (including `repositoryRoot`) auto-pairs and observes that code root, while a read with no resolvable code root stays `unverifiable` with compact entries (`test_knowledge_read_without_a_named_tree_pairs_resolved_code_and_stays_unverifiable_without_root`). The published-intent block first names its committed tree and `treeScope`; an
  uncommitted edit is then observed at a different captured working tree with `codeState=working-tree`
  and a working-tree `treeScope`. The test does not compare the dirty invariant states with the earlier states.
  With no resolved tree it is `unverifiable`.

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



- An injected Git timeout reports the entry as unverifiable. The next read observes the real tree and finds the edit stale. [6]


- A missing recorded line-range blob. [7]
- Precedence and `unrealized`. [8]

- Stale proofs. [9]

- Per side. [10]
- The cache key. [11]

- `knowledge_read` with a named tree. [12]
- `knowledge_read` without `codeTreeId` pairs a resolved code root and stays unverifiable when no root resolves. [13]
- The published-intent block. [14]



- An injected IndexMismatchError leaves the read in view state with the invariant and realization IDs. Currentness gives the failure reason and the fixture statement stays out of the serialized response. [15]


### Cross-Repo References

No meaningful cross-repo references found: every case works in its own temporary repositories.

No cross-repo boundary is crossed by this file.

### Repo-Internal References (continued)

- The `unit-regression` lane selects `mcp/tests/test_knowledge_currentness.py`. [16]
