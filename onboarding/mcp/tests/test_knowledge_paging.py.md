# mcp/tests/test_knowledge_paging.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R02 cases: bounded continuation accepted by the mounted read, over converted memory trees.** Eleven collected cases (one parametrized twice) cover the cross-surface walk, threshold adherence, oversized rows, binding refusals, the projection over the artifact limit, the whole-block bound, the ordering and code-tree bindings, and the empty ordering. The module is in the `unit-regression` lane. **Since 260928-MIK-L01 the path walks read the family-complete leaf read's `rows`** instead of the scope read's `items`, because a path seed of a converted tree is now the leaf read (MIK-R01); each case keeps its intent.

## Code Commentary

### Logic

- **The world.** `write_family_tree` builds a converted memory tree with one family of N members at `src/pkg/...` paths; the code repository is real Git where a case needs a code tree.
- **Cross-surface walk (the conforming example).** A 40-member family (`words=150` since L01, because leaf rows are more compact and the walk must still span three or more pages): page 1 from the published-intent block, later pages from `knowledge_read`; every row exactly once (by `_leaf_key`: kind, ID and `via`, over `_counted` rows, which exclude the uncounted reference row), counts checked on every page, and a continued family page starts with the literal `family_header_reference` row at `rows[0]`, naming the family and its title (the carried L02 Q3 obligation, formerly `page.headerReference`).
- **Threshold adherence.** `RANDOMIZED_TRIALS = 8`, seeded: families of 3–45 members, statements of 1–600 words with Latin, Cyrillic and CJK characters, both surfaces, every page at most 8,000 wire tokens.
- **Oversized row:** a ~20k-character statement arrives alone as the page's one counted leaf row, flagged and whole.
- **Binding refusals:** eight token edits plus a changed tree, each with no `payload` and no `page`.
- **Projection:** a payload over the 20,000-character artifact bound continues in parts; a row too large alone is refused `oversized_row` (the carried L23 ruling).
- **Whole block:** parametrized `mounted-maximum` (5 seeds) and `synthetic-16` (16 seeds at 747-character paths, forcing the collapse); each seed's walk is exactly once.
- **Ordering, code tree and empty ordering:** a view walk resumes in its own ordering; a resumed leaf walk (renamed from the scope walk in L01: it now asserts entry `state` is `current` at page 1's tree T1 and `stale` when the same path is read fresh at T2, and that page 1 has a continuation) and a named view walk stay at page 1's code tree after HEAD moves, a different `codeTreeId` is refused naming both trees and stating the threshold, an unrelated root is refused by name, and the token carries no local path; an empty `orderingInput` is refused on a tree read and a database read.

### Conventions

- Imports `knowledge_index_test_support`; the lifecycle catalog lists it as a consumer of that module and of the node package-lock fixture (the Thirty-seventh re-pin).

### Invariants And Boundaries

- The tests prove the candidate invariants recorded on the `application` overview: the threshold, exactly-once enumeration, refusal with no partial page, and a token that is the whole state.

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

- The module statement. [1]
- Seeded, bounded randomized trials. [2]
- The cross-surface 40-member walk, exactly once. [3]
- Threshold adherence over randomized families. [4]
- An oversized row alone and flagged, as the page's one counted leaf row. [5]
- Binding refusals with no page. [6]
- The projection continues in parts and never raises. [7]
- The whole block within the threshold, 5 and 16 seeds. [8]
- A view walk keeps its ordering. [9]
- Resumed pages stay at page 1's code tree: a leaf walk's entries are current at T1 and stale at T2, and a named view walk keeps its tree. [10]
- The leaf-row helpers: the counted rows, and the key that identifies each row once. [11]
- An empty ordering is refused on every path. [12]

### Cross-Repo References

No meaningful cross-repo references found: the cases build their repositories under `tmp_path`.

No cross-repo boundary is crossed by this file.
