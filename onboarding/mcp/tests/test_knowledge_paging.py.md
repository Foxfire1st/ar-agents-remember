# mcp/tests/test_knowledge_paging.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_paging.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement. | "Bounded continuation accepted by the mounted read (MIK-R02)." | mcp/tests/test_knowledge_paging.py:1-17 |
| Seeded, bounded randomized trials. | `RANDOMIZED_TRIALS` | mcp/tests/test_knowledge_paging.py:68-68 |
| The cross-surface 40-member walk, exactly once. | `test_a_forty_member_family_pages_from_read_ar_files_through_knowledge_read_exactly_once` | mcp/tests/test_knowledge_paging.py:225-259 |
| Threshold adherence over randomized families. | `test_pages_stay_within_the_threshold_over_randomized_families` | mcp/tests/test_knowledge_paging.py:277-312 |
| An oversized row alone and flagged, as the page's one counted leaf row. | `test_a_row_larger_than_the_threshold_is_returned_alone_and_flagged` | mcp/tests/test_knowledge_paging.py:315-326 |
| Binding refusals with no page. | `test_a_continuation_whose_binding_does_not_hold_is_refused_with_no_page` | mcp/tests/test_knowledge_paging.py:339-401 |
| The projection continues in parts and never raises. | `test_a_projection_over_the_artifact_limit_continues_in_parts_and_never_raises` | mcp/tests/test_knowledge_paging.py:404-455 |
| The whole block within the threshold, 5 and 16 seeds. | `test_the_whole_knowledge_block_of_several_seeds_stays_within_the_threshold` | mcp/tests/test_knowledge_paging.py:497-520 |
| A view walk keeps its ordering. | `test_a_view_walk_resumes_in_its_own_ordering_and_refuses_another` | mcp/tests/test_knowledge_paging.py:523-552 |
| Resumed pages stay at page 1's code tree: a leaf walk's entries are current at T1 and stale at T2, and a named view walk keeps its tree. | `test_a_resumed_leaf_walk_observes_entries_at_page_one_code_tree`; `test_a_view_walk_is_bound_to_its_named_code_tree` | mcp/tests/test_knowledge_paging.py:559-629; mcp/tests/test_knowledge_paging.py:647-696 |
| The leaf-row helpers: the counted rows, and the key that identifies each row once. | `_counted`; `_leaf_key` | mcp/tests/test_knowledge_paging.py:195-202 |
| An empty ordering is refused on every path. | `test_an_empty_ordering_is_refused_not_defaulted_on_every_path` | mcp/tests/test_knowledge_paging.py:699-721 |

## Cross-Repo References

No meaningful cross-repo references found: the cases build their repositories under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): MIK-R01 adapts the L02 walks from scope `items` to leaf `rows`. Purpose and Logic record the adaptation (`_counted`, `_leaf_key`, `words=150`, the literal reference row at `rows[0]`, the renamed code-tree case); one row was added and the module-statement row re-measured (`1-15` → `1-17`). **Two reopened claims were re-read and reworded:** the oversized-row row (this pass's generated-repair bullet for it was removed because its claim was reworded) and the code-tree row, whose test was renamed to `test_a_resumed_leaf_walk_observes_entries_at_page_one_code_tree` (re-measured: its extent is still `559-629`).
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 (the carried L23 projection ruling; 19:56:40 Q1, Q5, Q6; 20:40:40 F1, F2, F4, F5, F8). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
