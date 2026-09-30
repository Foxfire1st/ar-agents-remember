# mcp/tests/test_knowledge_leaf_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_leaf_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T02:10:00+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R01 cases: the family-complete leaf read over converted memory trees, and the obligations L01 carries from L02.** Eleven collected cases cover the selection and its order, one selection on both surfaces, family names in the `invariant` view, the conforming example, the failure states, the carried obligations (the empty-repository root, the leaf walk's code tree, the seed-queue cap and the projection's 64-row cap), the derived reference title, and identity seeds beside a leaf. The module is in the `unit-regression` lane.

## Code Commentary

### Logic

- **The world.** `_invariant`, `_family`, `_sidecar` and `_graph` write a converted memory tree through the text-file layout (records, families, onboarding sidecars with `realizes` and `proves`); `_read` calls `knowledge_read_payload` with a `CoordinationContext`. The module imports `knowledge_index_test_support` for the shared review fixtures and Git helpers.
- **Selection and order** (`test_a_path_selects_one_family_hop_in_the_declared_order`). A three-family graph with a shared member, a retired member, a proof entry and an advertised family. It asserts the exact row sequence (rule 4), the header fields (rule 2), the member and entry fields (rule 3), the `member_reference` of `INV-CCCCCC` under `FAM-F22222` with `returnedUnder: FAM-F11111`, `title == "INV-CCCCCC holds."` and `titleDerivedFrom: "statement"` (rule 5, ruling Q1), one `advertised_family` row for `FAM-F33333` with `via == ["INV-CCCCCC", "INV-DDDDDD"]` (ruling N4), the exact `counts` (rule 8), `memoryTreeId` (rule 9), the block's top-level `policyVersion == "family-complete-leaf/v1"` (ruling Q5), and that a proof-only path also seeds the read (ruling Q3).
- **Both surfaces** (`test_both_surfaces_return_one_selection_under_one_manifest`): identical rows and manifest digest from `read_ar_files` and `knowledge_read` `source_context` (rule 6).
- **Family names** (`test_the_invariant_view_names_its_families`): the `invariant` view's `families` by ID and title (rule 7).
- **The conforming example** (`test_the_conforming_example_returns_the_whole_family_in_one_response`): the review fixture's path returns its own invariant first, its family and guarantee, every member statement and every entry, in one response.
- **Failure states** (`test_absent_and_partial_states_are_named`): `registration_absent` on both surfaces, naming "realization or proof claim" (ruling N6); a complete tree's refusal names the same memory tree as the block, and a partial index states `indexState: partial` and `indexComplete: false` (ruling N3).
- **Carried obligations.**
  - `test_a_repository_root_with_no_commit_is_refused_by_name`: a repository with no commit, and a plain directory, are refused `selected_input_unavailable` naming the root (carried 2026-09-29 21:17:07).
  - `test_a_leaf_walk_resumes_at_its_code_tree_from_the_named_repository`: the token carries no local path, the walk resumes at page 1's tree from the workspace, and an unrelated root is refused by name.
  - `test_a_tail_longer_than_one_queue_is_refused_by_name_within_the_threshold`: 104 seeds at deep `_DEEP` paths give `seed_queue_exceeded` with `seedCount` and `firstSeed`, the block stays within 8,000 tokens and nothing raises (carried 2026-09-29 21:32:34).
  - `test_a_tree_projection_carries_every_row_of_a_view`: a view of more than 64 rows is projected whole on a tree (carried 2026-09-29 19:56:40 Q7; ruling 23:21:57).
- **The derived title** (`test_a_derived_reference_title_is_the_first_sentence_cut_to_a_fixed_length`): the first of two sentences, a decimal inside a sentence, no sentence end, and a 200-character sentence cut to exactly `DERIVED_TITLE_LENGTH` ending in `…`.
- **Identity seeds on a tree** (`test_identity_seeds_on_a_tree_keep_the_scope_read_beside_the_leaf`, ruling N2): a 30-member family read through `read_published_intent` with an identity seed, a path, then 29 more identity seeds. It covers a scope page in the block, each kind's collapsed tail (continuation views `invariant` and `source_context`), every continuation walked through `knowledge_read` (including `tree_read._scope_response` and the moves between queued seeds), every seed's rows exactly once against `select_knowledge_scope` and `select_leaf`, every page within the threshold, and the mixed-block policy: the top level keeps `recorded-family-frontier/v1`, and each page states its own `selectionPolicy`.

### Conventions

- Imports `knowledge_index_test_support`, so the lifecycle catalog lists this module as a consumer of that module and of the node package-lock fixture (the Thirty-ninth re-pin).

### Invariants And Boundaries

- The tests prove the candidate invariants recorded on the `application` overview: the complete one-hop selection equal on both surfaces, a shared member returned once and referenced after, the header reference row first on a continued family page, and refusals that name the memory tree.
- They do not re-prove unconverted-read preservation; that is `test_read_ar_files.py`, unchanged, plus the worker's and reviewer's byte-identical comparisons.

### Todos

- The N2 case does not cover `_scope_response`'s refusal branches (review R2-I2); scope-token refusals are covered at the binding level by `test_knowledge_paging.py`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R01@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`01_family-complete-leaf-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement. | "The family-complete leaf read (MIK-R01) and the obligations L01 carries from L02." | mcp/tests/test_knowledge_leaf_read.py:1-13 |
| The converted-tree world written through the text-file layout. | `_invariant`; `_family`; `_sidecar`; `_graph` | mcp/tests/test_knowledge_leaf_read.py:67-158 |
| Selection, order, reference row, frontier, counts and policy. | `test_a_path_selects_one_family_hop_in_the_declared_order` | mcp/tests/test_knowledge_leaf_read.py:185-270 |
| One selection on both surfaces. | `test_both_surfaces_return_one_selection_under_one_manifest` | mcp/tests/test_knowledge_leaf_read.py:273-292 |
| Family names in the `invariant` view. | `test_the_invariant_view_names_its_families` | mcp/tests/test_knowledge_leaf_read.py:295-309 |
| The conforming example in one response. | `test_the_conforming_example_returns_the_whole_family_in_one_response` | mcp/tests/test_knowledge_leaf_read.py:312-332 |
| Absent and partial states, and refusals naming the tree. | `test_absent_and_partial_states_are_named` | mcp/tests/test_knowledge_leaf_read.py:335-355 |
| A root with no commit refused by name. | `test_a_repository_root_with_no_commit_is_refused_by_name` | mcp/tests/test_knowledge_leaf_read.py:358-371 |
| A leaf walk resumes at its code tree, with no path in the token. | `test_a_leaf_walk_resumes_at_its_code_tree_from_the_named_repository` | mcp/tests/test_knowledge_leaf_read.py:374-433 |
| More than one queue of seeds refused by name within the threshold. | `test_a_tail_longer_than_one_queue_is_refused_by_name_within_the_threshold`; `_DEEP` | mcp/tests/test_knowledge_leaf_read.py:436-459 |
| A tree projection carries every row of a view. | `test_a_tree_projection_carries_every_row_of_a_view` | mcp/tests/test_knowledge_leaf_read.py:462-493 |
| The derived reference title. | `test_a_derived_reference_title_is_the_first_sentence_cut_to_a_fixed_length` | mcp/tests/test_knowledge_leaf_read.py:496-501 |
| Identity seeds keep the scope read beside the leaf, and the mixed-block policy. | `test_identity_seeds_on_a_tree_keep_the_scope_read_beside_the_leaf`; `_walk_entries` | mcp/tests/test_knowledge_leaf_read.py:520-582 |
| The lane row. | "mcp/tests/test_knowledge_leaf_read.py" | mcp/tests/test-evidence-lanes.toml:109-109 |

## Cross-Repo References

No meaningful cross-repo references found: the cases build their repositories under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): created this card for the new file MIK-R01 adds (11 collected cases). It records the carried obligations and the architect rulings of 2026-09-29 23:21:57 (Q1, Q3, Q5) and 2026-09-30 00:08:39 (N2, N3, N4, N6). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
