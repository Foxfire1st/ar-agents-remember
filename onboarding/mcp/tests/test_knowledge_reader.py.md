# mcp/tests/test_knowledge_reader.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_reader.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R29's backend proof: the path-based knowledge reader's explorer, path view, subtree pages, truth views,
timeline, census, selections, failures, route and read-only behaviour.** 21 cases, self-contained (the module
imports no test support module, so the evidence-lifecycle catalog needed no re-pin). It is registered in the
`unit-regression` lane of `test-evidence-lanes.toml`.

## Code Commentary

### Logic

- **The fixture world** (`world`) is a coordination root with one repository `demo`: a code repository (the
  review file with `loadReview`, three sibling files, a test file and a binary blob with a NUL) and its
  converted memory repository at `memory-repos/ar-demo`, with three commits:
  - an **unconverted** commit (`memory.md` only);
  - **commit 1** (`Code-Commit` of the code commit): MIK-R23's review-example tree, a family realized across
    four files, a test proof, a decision and an incident linking to an invariant, a route sidecar, two leaves'
    history rows, a retired invariant, a sibling-prefix file (`dashboard/src/database.ts`), onboarding prose with
    numbered references, and a census;
  - **commit 2**: the invariant's statement revised, one realization re-anchored in place and one moved to
    another file, a third leaf's history row, an assumption facet, and a decision superseding the first.
- **The cases, by rule:**
  - rule 2: the file view (references, entries with states, the family via its route and its other
    locations, linked records), the bounded directory view (own level, children with counts, subtree size,
    the route link; F2), the test file (proofs with facets), and the without-proof list by path;
  - F2, F16, F17, R3-1 and R3-2: the subtree walk (complete, ordered, every whole answer within the bound, the
    sibling prefix never counted), a walk resumed after a code commit (page 2 at page 1's tree in both
    `page.codeTreeId` and `selection.codeTree`, the "moved since" note, a fresh walk at the new HEAD, and a token
    naming an absent tree refused), and another walk's token refused (another path, another memory tree,
    garbage);
  - rule 1: the explorer (code and onboarding children, `inCode: false` for a moved realization's new file, a
    retired invariant's entry not counted);
  - rules 3 and 4: the invariant view with a three-source timeline, moves against re-anchors while reading only
    the sidecars naming them (F1, F5), the bounded timeline cache (built once per tree; a failed source is not
    remembered, F7 and F17), the family, the decision (derived supersession), the incident and facet with
    typed links both ways (and unreadable links named, F11), and the census;
  - selections: hexadecimal names only, a branch name refused, a commit list that cannot be read named (F6,
    F11, N1 `paired-code-commit`); the published tree reads uncommitted state, writes nothing and offers a pin
    only when clean (N2, N1 `checkout-head`, the tree key in the cache key); a live leaf and its code note;
    a partial index and a missing code tree named where they apply;
  - the route: every view served over HTTP, 503 unwired, nothing written in either repository; bad requests
    400 (malformed locators F3, `../etc`, an unknown view, NUL and control characters on every path view F15),
    a directory as code `absent` (F18), a binary blob `binary`, and a blob above the bound `too-large` without
    its bytes being read (F14, F17).
- **Read-only proof.** `_snapshot` records refs, `--no-optional-locks` status, `count-objects` and the index
  file of both repositories; the route case and the published case compare it before and after.

### Conventions

- Subtree cases cut at 800 tokens, where one row fits beside the reader's envelope.
- Cases were split into assertion helpers so no test function is at radon C or worse (review F8).

### Invariants And Boundaries

- The file is 1,182 lines, under the 1,200-line cap (the architect noted its size at R3). A later case should go
  to a new module.

### Todos

- **Size:** the next reader case belongs in a new test module, not here (ruling 2026-09-30T11:24:12 note).

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the fixture's two converted commits. | "The fixture is a coordination root with one repository" | mcp/tests/test_knowledge_reader.py:1-12 |
| The converted tree, the second commit's changes and the world with an unconverted commit. | `_write_tree`; `_second_commit`; `world` | mcp/tests/test_knowledge_reader.py:177-315; mcp/tests/test_knowledge_reader.py:429-486; mcp/tests/test_knowledge_reader.py:490-514 |
| The read-only snapshot of both repositories. | `_snapshot` | mcp/tests/test_knowledge_reader.py:525-541 |
| The file and bounded directory views. | `test_a_file_path_view_shows_prose_references_entries_families_and_linked_records`; `test_a_directory_view_is_bounded_to_its_own_level_children_and_route` | mcp/tests/test_knowledge_reader.py:584-614 |
| The subtree walk, the walk's code tree (F16, R3-1, R3-2), and another walk refused. | `test_a_directorys_subtree_pages_through_the_shared_continuation`; `test_a_subtree_walk_measures_every_page_at_the_code_tree_it_began_at`; `test_a_subtree_continuation_of_another_walk_is_refused` | mcp/tests/test_knowledge_reader.py:653-713 |
| The whole answer, envelope included, within the bound (F17). | `_walk` | mcp/tests/test_knowledge_reader.py:640-650 |
| The test file, the explorer and the without-proof list. | `test_a_test_file_shows_its_proofs_by_invariant_with_their_facets`; `test_the_explorer_lists_code_and_onboarding_children_with_entry_counts`; `test_the_without_proof_list_is_filterable_by_path` | mcp/tests/test_knowledge_reader.py:716-760 |
| The invariant view, moves and re-anchors, and the timeline cache. | `test_an_invariant_truth_view_has_every_field_state_link_and_a_three_source_timeline`; `test_the_timeline_labels_moves_and_re_anchors_and_reads_only_the_sidecars_naming_them`; `test_a_complete_timeline_is_served_again_from_the_bounded_cache` | mcp/tests/test_knowledge_reader.py:801-838; mcp/tests/test_knowledge_reader.py:849-880 |
| The family, decision, incident and facet, and census views. | `test_a_family_truth_view_shows_guarantee_members_routes_and_every_location`; `test_a_decision_truth_view_shows_alternatives_and_derived_supersession`; `test_incident_and_facet_views_show_every_field_and_typed_links_both_ways`; `test_the_census_view_shows_measures_and_each_routes_status_history` | mcp/tests/test_knowledge_reader.py:883-949 |
| The selections: commits, published, a leaf, and a partial index with no code tree. | `test_any_commit_is_selectable_by_its_hexadecimal_name_only`; `test_the_published_tree_reads_uncommitted_state_writes_nothing_and_offers_a_pin`; `test_a_live_leafs_candidate_is_selectable_and_names_what_its_code_tree_leaves_out`; `test_a_partial_index_and_an_unavailable_code_tree_are_named_where_they_apply` | mcp/tests/test_knowledge_reader.py:957-1017; mcp/tests/test_knowledge_reader.py:1064-1083 |
| The route, and bad requests and bounded code notices. | `test_the_route_serves_every_view_and_the_reader_writes_nothing`; `test_bad_requests_are_400_and_large_or_binary_code_is_a_bounded_notice` | mcp/tests/test_knowledge_reader.py:1092-1126; mcp/tests/test_knowledge_reader.py:1142-1182 |
| The lane row. | "mcp/tests/test_knowledge_reader.py" | mcp/tests/test-evidence-lanes.toml:108-108 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new test module MIK-R29 adds (21 cases), recording the review fixes it proves (F1-F14 of 09:42:58, F15-F18 of 10:44:14, R3-1 and R3-2 of 11:24:12), the N1 and N2 cases, and the architect's 1,158-line size note (the file is 1,182 lines after R3). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
