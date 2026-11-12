# mcp/tests/test_knowledge_paging.py

## Governing Overview

[tests route overview](overview.md)

## Current source contract evidence


- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred. [27]


## Purpose

Pins token-bounded converted-tree leaf/view paging and continuation bindings.

**The MIK-R02 cases: bounded continuation accepted by the mounted read, over converted memory trees.**

The module is in the `unit-regression` lane. **Since 260928-MIK-L01 the path walks read the family-complete leaf read's `rows`** instead of the scope read's `items`, because a path seed of a converted tree is now the leaf read (MIK-R01); each case keeps its intent.

## Code Commentary


The source declares fifteen test functions, including four methods in TestRegisteredWalkCompleteness; this is a static definition count, not a collected case count. Direct knowledge_read walkers check no duplicate/lost kind/ID/role identities, randomized family pages, binding refusals, view ordering and page-one code-tree identity. Whole-block cases still exercise internal published intent with five and sixteen seeds. Large source prose is omitted from projected names, so that fixture produces no oversized_row page; a separate cut_page test uses an oversized synthetic projection to assert the single-row fallback. The registered walkers assert forty-member completeness, small names for large prose, and continuation completion when detail logs are unwritable or exhausted. No fixture or test was executed during this review.

### Logic

- `_walk_scope` starts and resumes with knowledge_read_payload, despite the retained forty-member test identifier mentioning read_ar_files. Counted rows exclude family/reference framing; `_leaf_key` distinguishes projected roles and raw structural endpoints. The forty-member walk asserts at least three pages, exactly-once total identity enumeration and projected family/reference framing on continued pages.
- Eight seeded randomized families compare direct leaf and family-view walks and assert page-threshold adherence with the product counter; family-view header references carry a kind, family identity and admitted state.
- The large-prose test asserts no oversized-row flag and no noise text in counted rows, with total exactly-once enumeration. The separate name-overflow test calls cut_page with synthetic padding and asserts PageCut.oversized plus the unchanged single row; it is not a registered oversized-answer witness.
- The multi-seed block cases remain internal published-intent fixtures, parametrized on five and sixteen seeds; those counts are not the current read_ar_files cap. Deferred queues are walked through knowledge_read.
- Continuation cases retain token/tree/order mismatch refusals with no partial payload, page-one code-tree currentness, and named unrelated-root/empty-ordering refusals. A separate moved-tree family read asserts admitted row states including stale.
- TestRegisteredWalkCompleteness calls the real registered handler in EntryPointWorld. It asserts exactly-once delivered enumeration for forty members, projected names for large prose, and complete delivered walks with logError but no log when logs cannot be written or are over budget. No detail file is used as the enumeration oracle.

### Conventions

- Imports `knowledge_index_test_support`; the lifecycle catalog lists it as a consumer of that module and of the node package-lock fixture (the Thirty-seventh re-pin).

### Invariants And Boundaries

- These source assertions cover threshold adherence, exactly-once enumeration, refusal with no partial page, and continuation binding. Direct-builder, synthetic-cut and registered-handler coverage are distinct; this review supplies no execution or acceptance receipt.

### Todos

- None recorded.

## Evidence


### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- `test_a_forty_member_family_pages_from_read_ar_files_through_knowledge_read_exactly_once` supplies the current fixture or assertion described above. [13]


- `test_a_row_larger_than_the_threshold_is_returned_alone_and_flagged` supplies the current fixture or assertion described above. [14]

- `test_the_whole_knowledge_block_of_several_seeds_stays_within_the_threshold` supplies the current fixture or assertion described above. [15]

- `test_a_view_walk_is_bound_to_its_named_code_tree` supplies the current fixture or assertion described above. [16]


### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

- Seeded, bounded randomized trials. [17]

- Forty-member direct knowledge_read walk, exactly once; the historical test name does not describe its current first call. [18]


- Threshold adherence over randomized families. [19]


- Large prose is not carried in projected rows and produces no oversized-row flag. [20]


- Binding refusals with no page. [21]

- Internal published-intent whole-block threshold assertions for five and sixteen seeds, not the read_ar_files path cap. [22]

- A view walk keeps its ordering. [23]


- Resumed pages stay at page 1's code tree: a leaf walk's entries are current at T1 and stale at T2, and a named view walk keeps its tree. [24]


- The leaf-row helpers: the counted rows, and the key that identifies each row once. [25]


- An empty ordering is refused on every path. [26]


### Cross-Repo References

No meaningful cross-repo references found: the cases build their repositories under `tmp_path`.

No cross-repo boundary is crossed by this file.
