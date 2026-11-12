# mcp/tests/test_knowledge_reader_tree_coverage.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The focused tests for the Knowledge tree's coverage computation (MIK-R79 rule 6 and OR-R009): the
composed listing, truthful counts and presence marks, and the named unavailable states when scope,
path or code reads fail. Five added test declarations cover memory selection, bounded UTF-8 summaries and whole-prose retrieval, and timeline continuation and memo behavior.

## Code Commentary

### Logic

- The coverage cases build a selected memory tree and code tree and call `read_tree_listing`, asserting the
  immediate children, the `hasKnowledge`/`hasOverview` marks, the directory `coverage` counts, and
  the negative cases: an empty or sidecar-only mirror directory is not knowledge, own-card versus
  at-or-below knowledge is kept apart, a missing or unreadable scope settings file yields
  `coverage unavailable`, and a code enumeration failure names the code state.
- The real composed-tree case counts presence and coverage from the selected settings.
- Selection cases admit full or abbreviated commits and branches, including an old commit outside the forty-entry recent list; reject NUL-containing names before Git invocation; and name an unavailable recent-commit read.
- Path summaries bound prose to 65,536 UTF-8 bytes and report its full size and truncation. Whole-prose reads return the complete text by code path at the selected tree, with named invalid, absent and unreadable outcomes.
- Timeline cases walk pages of at most fifty events with commit, record and manifest binding, refuse crossed or malformed continuations and restart from the first page. Instrumented assertions require one manifest build and one hash visit per event for the walk. Memo checks price retained bytes, evict older entries within budget, isolate caller mutations, and allow an individually over-budget timeline to be read without retention.

### Conventions

- pytest; the fixtures are temporary repository trees, so the cases are deterministic and offline.

### Invariants And Boundaries

The tests bind the listing's truthful counts and its negative semantics (empty is not knowledge,
unknown is not false, unavailable is named). They do not test the dashboard rendering.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 6) with ruling OR-R009; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The real composed-tree presence and coverage case. [1]

- The listing entry point under test. [2]







### Cross-Repo References

No cross-repo boundary is crossed by this file.

- Memory commits and branches remain selectable beyond the recent list; malformed names are rejected before Git and failed commit-list reads are unavailable. [4]
- UTF-8 summaries are byte bounded while whole-prose reads retain full text and selected-tree identity, with named invalid, absent and unavailable outcomes. [5]
- Timeline pages retain event identity and bound continuations; instrumentation asserts one build and one hash walk. Bounded memo checks cover byte pricing, eviction, mutation isolation and unretained over-budget reads. [6]



- The suite's lane membership in the evidence catalog. [3]
