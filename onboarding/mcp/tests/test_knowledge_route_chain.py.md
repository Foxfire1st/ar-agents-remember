# mcp/tests/test_knowledge_route_chain.py

## Governing Overview

[tests route overview](overview.md)

## Current source contract evidence

- Public family/walk premises measure fitting text-free pages with continuation; complete domain-unit walks retain rows and filter raw or projected framing-reference vocabulary, not pointer proof or a runtime verdict. [13]

## Purpose

**The MIK-R05 cases: route-chain family retrieval over converted memory trees.** Twelve source test definitions, including one parametrized on two values cover the chain over nested directories, compact entries after the leaf content, `memberAtSeed` and live member counts, `no_governing_family`, the conforming example, expansion from a family seed and its spellings, the budget and resumption, the family-seed resume rules of review F4 and ruling R2-1, the v1-policy token refusal, and repeatable read_ar_files naming without served_earlier. The thirteen-case wording is a historical collection account; this inspection counts twelve test definitions and one two-value parametrization, without collecting or executing them.

## Code Commentary

### Logic

- **The world.** `_tree` writes the layout marker; `_family` writes a family with routes (and an optional title and guarantee); `_nested` builds families routed at `a/b/c`, `a/b` and `a`, `a`, `.`, a sibling `a/x`, a child `a/b/c/d` and a retired family. The module reuses L01's `test_knowledge_leaf_read` helpers (`SEED`, `_context`, `_graph`, `_invariant`, `_read`, `_shape`, `_sidecar`) and `test_read_ar_files`'s context and config builders.
- **The chain** (`test_the_chain_is_the_directory_and_its_ancestors_never_a_child_or_a_sibling`): `a/b/c/new.py` returns four chain rows nearest first, a family with two routes on the chain once through both, never the child, the sibling or the retired family; `routeChain` is asserted exactly (`a/b/c`, 4 links, `mechanical`, `governed`, 4 families); ties at one distance fall back to the family ID; a root file sees only `.`.
- **Compact entries** (split by review R1 F1, 2026-09-30 04:12:49):
  - `test_chain_entries_are_compact_after_the_leaf_and_name_a_member_at_the_seed`: the first chain row directly follows `advertised_family` (rule 5), the exact `FAM-F44444` entry (`_F4_ENTRY`, including `expand`), every entry with exactly that field set, and `rowsTotal` equal to the structure's order;
  - `test_a_chain_entry_flags_a_family_expanded_above_and_counts_live_members`: `memberAtSeed` true for the families expanded above (ruling Q2, 2026-09-30 03:32:18), false for the routed neighbour, and a retired member not counted;
  - `test_entries_no_route_covers_state_no_governing_family`: a path with entries under no route is a page of its MIK-R01 rows stating `no_governing_family`, with no `registration` and `chainFamilies: 0`.
- **The conforming example** (`test_the_conforming_example_returns_the_governing_family_of_an_unattributed_file`): the unattributed `mcp/src/agents_remember/worktrees/new_helper.py` returns "attribution-and-landing-pairing" compactly and states `registration_absent` (the non-conforming answer would be `registration_absent` alone); knowledge_read asserts the projected family/chain identity and the same routeChain, not equality with raw block rows or their full prose.
- **Expansion from a family seed** (rule 3; ruling Q1):
  - `test_a_family_seed_returns_the_full_family_content`: the projected path page names a family/chain row; reading its family ID asserts projected family/header, invariant/member, realization and family/advertised identities with no routeChain. It no longer follows an expand object or compares full row content;
  - `test_a_family_seed_is_named_by_id_revision_or_projected_uuid`: `ID`, `ID@1` and the projected UUID give one manifest; `@2`, a bare `@` (ruling R2-1) and an unknown ID are `selector_absent`.
- **Public boundary and domain-body scope.** `_walk` accepts either payload-nested tool rows or top-level published-intent rows. It checks public outcomes and externally measures fitting answers; overflow tails keep the named overflow contract, while the explicitly marked domain body supplies rows and its top-level next token. These assertions do not claim pointer retrieval. The family-walk premise separately asserts a within-bound, text-free public page and a mounted continuation; the domain-unit walk then retains the complete 75-row selection, not merely the first page. Continued framing rows are filtered in either the raw `family_header_reference` vocabulary or the projected `family`/`reference` kind-role vocabulary.
- **Budget and resumption** (the module-scoped `long_tree`: 24 long members in one family and 24 long-guarantee families at `.`):
  - `test_chain_entries_count_toward_the_threshold_and_resume_like_the_leaf`: page 1 continues, the walk returns every row exactly once, every page is within the threshold (`_walk`), and the 25 chain rows are the last 25;
  - `test_a_family_seed_walk_resumes_under_any_spelling_of_its_family` (review F4): a family-seed walk resumed naming `FAM-B16000`, `FAM-B16000@1` or the projected UUID walks all 24 members; naming another family is `continuation_binding_mismatch`;
  - `test_a_family_seed_walk_resumed_naming_a_revision_the_tree_lacks_is_refused` (ruling R2-1, 2026-09-30 04:45:22, parametrised on `@99` and a bare `@`): the resume is `selector_absent`, the same code as a fresh read;
  - `test_a_continuation_minted_under_the_v1_policy_is_refused` (review F2): a `v2` token re-encoded as `v1` is `continuation_binding_mismatch` (ruling Q4).
- **Repeatable read_ar_files naming** (`test_read_ar_files_names_the_same_files_on_every_call`, with the lifecycle fixture): the first call is named and contains the seed path; the second files array equals the first and the serialized answer contains no served_earlier. A direct knowledge_read asserts the three governing family/chain IDs. This test does not invoke refresh, a second seed, or a changed-family repeat; those are no longer its assertions.

### Conventions

- Imports `test_knowledge_leaf_read` and `test_read_ar_files`, so the lifecycle catalog lists this module as a consumer of `knowledge_index_test_support.py`, the node `package-lock.json` fixture, `read_scope_test_support.py` and `curator_coherence_test_support.py` (the Forty-first re-pin).
- No test function is at radon C (review R1 F1).

### Invariants And Boundaries

- The tests prove the MIK-R05 candidate invariants recorded on the `application` overview: the chain after the leaf content, each chain row once, within the bound; a continuation bound to tree, policy and seed; a revision the tree does not hold refused `selector_absent` on fresh read and resume alike.
- This module does not assert unchanged unconverted read_ar_files behavior. Current missing/unconverted naming cases belong to test_read_ar_files.py; no byte-identical preservation or execution receipt is supplied here.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R05@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`05_route-chain-family-retrieval.json`); it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement. [1]
- The reused L01 and `read_ar_files` helpers. [2]
- The world: the layout, routed families and the nested fixture. [3]
- The chain over nested directories, never a child or a sibling. [4]
- The exact compact entry. [5]
- Compact entries after the leaf, `memberAtSeed` with live counts, and `no_governing_family`. [6]
- The conforming example. [7]
- Expansion from a family seed, and its spellings. [8]
- The walk helper and the long fixture. [9]
- The budget, the family-seed resume under any spelling, a lacking revision refused on resume, and the v1 token refused. [10]
- Repeated calls name the same files, omit served_earlier and retain governing family/chain IDs without session state. [14]
- The lane row. [12]

### Cross-Repo References

No meaningful cross-repo references found: the cases build their repositories under `tmp_path`.

No cross-repo boundary is crossed by this file.

- Route-chain walks keep public outcomes and obtain complete domain-unit rows and continuations.
