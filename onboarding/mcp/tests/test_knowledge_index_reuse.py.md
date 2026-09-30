# mcp/tests/test_knowledge_index_reuse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_index_reuse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rule 6: the existing read, view and comparison code runs over the index unchanged.** Parity against a legacy database fixture, the view seam and the two-snapshot comparison over index files, and the ordinary read's published-memory selection of a converted tree. Registered in the `unit-regression` lane; 6 collected cases.

## Code Commentary

### Logic

- **Parity:** `build_parity_dataset` writes a store-authored database; `convert_dataset` turns it into a converted Git tree. `select_recorded_scope` runs for path, invariant and family seeds over both; the selected items are compared keyed by legacy ID, statement, guarantee, path, locator, role and rationale (`_database_key`, `_index_key`), and must be identical.
- **Views and comparison:** the family, source_context and invariant views return `state == "view"` over the index; a comparison between a committed tree and an edited working tree returns the new statement with no refusal.
- **Published intent:** `published_intent_block` over a converted memory root selects the tree through its index (with `memoryTree`), and the path's page is the family-complete leaf read, whose statements the case reads from `rows` (since 260928-MIK-L01, MIK-R01; formerly the scope read's `items`); a partial index's pages carry `indexState: partial` and `enumerationComplete: false`; an unconverted memory root keeps the database selection.

### Conventions

- `_context` builds a `CoordinationContext` whose coordination root is under `tmp_path`, so the cache is outside the repository.

### Invariants And Boundaries

- The comparison is non-empty and keyed by the legacy identities the converted records carry, so parity cannot pass vacuously.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases and their keys.

| Finding | Anchor | Source |
| --- | --- | --- |
| The parity keys on each side. | `_database_key`; `_index_key` | mcp/tests/test_knowledge_index_reuse.py:64-97; mcp/tests/test_knowledge_index_reuse.py:100-132 |
| The reused selection selects the same set over the index as over the database. | `test_the_reused_selection_selects_the_same_set_over_the_index_as_over_the_database` | mcp/tests/test_knowledge_index_reuse.py:142-201 |
| Views and the comparison over index files. | `test_the_views_read_the_index_as_their_dataset`; `test_a_comparison_reads_two_trees_through_their_indexes` | mcp/tests/test_knowledge_index_reuse.py:216-242; mcp/tests/test_knowledge_index_reuse.py:245-274 |
| The published-memory selection: converted, partial and unconverted. | `test_the_ordinary_read_selects_a_converted_memory_tree_through_its_index`; `test_a_partial_tree_selection_says_it_is_partial`; `test_an_unconverted_memory_root_keeps_the_database_selection` | mcp/tests/test_knowledge_index_reuse.py:294-310; mcp/tests/test_knowledge_index_reuse.py:313-322; mcp/tests/test_knowledge_index_reuse.py:325-333 |
| The lane row. | "mcp/tests/test_knowledge_index_reuse.py" | mcp/tests/test-evidence-lanes.toml:106-106 |

## Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): MIK-R01 makes a converted tree's path seed the family-complete leaf read, so `test_the_ordinary_read_selects_a_converted_memory_tree_through_its_index` reads statements from `rows` instead of `items` (a one-line adaptation; the case's intent is unchanged). The published-intent Logic bullet says so; the rows were projected or normalised by the installed fixer.
- 2026-09-30T00:00:40+00:00: Generated citation repair: "mcp/tests/test_knowledge_index_reuse.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot af78c18a536ac2f00d794dbac67f4d678cae173b43b31e0e7de2b8d520b727b6; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
