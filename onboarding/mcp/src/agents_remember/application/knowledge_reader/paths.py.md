# mcp/src/agents_remember/application/knowledge_reader/paths.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_reader/paths.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The explorer, the path view and the without-proof list of the knowledge reader (MIK-R29 rules 1 and
2).** Pick a path and see everything linked to it, the way overview and onboarding files work:

- **The explorer** (`tree_listing`) lists one directory level: the code tree's children joined with the
  onboarding mirror's, each with the number of live knowledge entries at or under it. A path with onboarding
  but no code (a card whose file is gone) is listed with `inCode: false`.
- **The path view** (`path_view`) of a file or directory: its onboarding Markdown with the sidecar's numbered
  references resolved; its realization and proof entries grouped by invariant, each with its MIK-R03 state;
  the families of those invariants and those routed over the path, each with its other locations; every
  record linking to the path or to those invariants, a decision shown whole; and for a test file, its proofs
  with their facets (`testFile`).
- **The without-proof list** (`without_proof`) is MIK-R28 rule 5's list, filtered to the invariants realized
  at or under a path when one is given.

## Code Commentary

### Logic

- **A directory's view is bounded (ruling 2026-09-30T09:42:58, F2).** `path_view` reads a file's entries with
  `entries_at_path` and a directory's with `entries_in_directory` (the files directly in it only), and adds
  `_directory_summary`: each immediate child holding knowledge with its live entry count, and
  `subtree: {entries, view: "subtree"}`. The full recursive list is the `subtree` view (`subtree.py`), paged
  through the shared continuation. The dashboard's default landing is the root's summary. At the root the
  remaining size is the root onboarding prose itself (one file's content, accepted by the architect).
- **Live only.** `_live_entries` drops entries whose invariant is retired or missing, and `_entry_counts`
  counts through `live_entry_paths_under`, so the explorer, the summary and the subtree agree.
- **Families.** `_families` takes each invariant's families (live only), then the families routed over the
  path: for a file, MIK-R05's `select_chain` (with the route each came `via`); for a directory,
  `families_governing` of the directory itself. Members come first. `_with_locations` adds the guarantee,
  routes, members, MIK-R03's `staleMembers` and every entry of the members that is not at (file) or under
  (directory) the path.
- **Records.** `_links_to` collects `links_to_path` (anchor and route targets) plus each invariant's
  `linked_from`; `_linked_records` summarises each linking record once and attaches a decision in full
  (`records.decision_document`), the rule carried from L13.
- **States.** `states_at` is the reader's one currentness call: MIK-R03's `invariant_currentness` at the
  selection's code tree, or the reason it failed. `_currentness_block` reports the counts, or the failure
  with `unverifiableReason`, never an empty state. `entry_document` places each entry's own state and reason.
- **Kind of a path.** `_path_kind` asks the code tree first, then a file sidecar, then file prose, then
  whether the index records entries at the path; otherwise it is a directory.
- **References.** `_references` reads the file or route sidecar and resolves its `references` through
  `records.reference_items`; an unreadable sidecar is `unavailable`, not an empty list.

### Conventions

- Nothing is re-derived: states come from L03's function, route chains from L05's, decisions from L13's
  helpers and the without-proof list from L28's index lookup.
- The prose path of a file is `onboarding/<path>.md`; a directory's is `onboarding/<path>/overview.md`.

### Invariants And Boundaries

- **Candidate invariant (not ingested): a directory view is bounded, and the full subtree is paged by a
  continuation bound to tree, policy and path.** Realized by `path_view`'s own-level read and
  `_directory_summary` here, and by `subtree.subtree_page`. Proved by
  `test_a_directory_view_is_bounded_to_its_own_level_children_and_route` and the subtree cases; on real data
  the root summary names 4 children and 179 subtree entries, walked in 2 pages each within 8,000 tokens.
- **A failed source is shown as partial or unavailable, never as empty:** an unverifiable state carries its
  reason, an unreadable sidecar is named, and a missing code tree still lists the onboarding side. Proved by
  `test_a_partial_index_and_an_unavailable_code_tree_are_named_where_they_apply`.
- A retired invariant is never shown as current, and a sibling that merely shares a prefix is never counted
  (`dashboard/src/database.ts` under `dashboard/src/data`, review F6).

### Todos

No additional work is asserted by this card.

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
| The module's own statement of the explorer, the path view and the without-proof list. | "**The explorer** lists one directory level" | mcp/src/agents_remember/application/knowledge_reader/paths.py:1-31 |
| One explorer level: code and onboarding children, with live entry counts. | `tree_listing`; `_entry_counts` | mcp/src/agents_remember/application/knowledge_reader/paths.py:85-111; mcp/src/agents_remember/application/knowledge_reader/paths.py:125-134 |
| The path view, bounded for a directory (F2). | `path_view` | mcp/src/agents_remember/application/knowledge_reader/paths.py:142-175 |
| Live entries only; the links naming the path or its invariants. | `_live_entries`; `_links_to` | mcp/src/agents_remember/application/knowledge_reader/paths.py:178-181; mcp/src/agents_remember/application/knowledge_reader/paths.py:184-190 |
| A directory's children with their counts, and its subtree's size. | `_directory_summary` | mcp/src/agents_remember/application/knowledge_reader/paths.py:193-208 |
| Prose and sidecar paths; the kind of a path; the resolved references. | `_onboarding_paths`; `_path_kind`; `_references` | mcp/src/agents_remember/application/knowledge_reader/paths.py:211-218; mcp/src/agents_remember/application/knowledge_reader/paths.py:221-232; mcp/src/agents_remember/application/knowledge_reader/paths.py:235-249 |
| The one currentness call, and its failure named. | `states_at`; `_currentness_block` | mcp/src/agents_remember/application/knowledge_reader/paths.py:252-263; mcp/src/agents_remember/application/knowledge_reader/paths.py:266-275 |
| One entry with its state; entries grouped by invariant. | `entry_document`; `_invariant_groups` | mcp/src/agents_remember/application/knowledge_reader/paths.py:278-300; mcp/src/agents_remember/application/knowledge_reader/paths.py:303-322 |
| Member and routed families, each with its other locations. | `_families`; `_with_locations`; `_elsewhere` | mcp/src/agents_remember/application/knowledge_reader/paths.py:325-344; mcp/src/agents_remember/application/knowledge_reader/paths.py:347-371; mcp/src/agents_remember/application/knowledge_reader/paths.py:374-385 |
| Linking records, a decision shown whole. | `_linked_records` | mcp/src/agents_remember/application/knowledge_reader/paths.py:394-401 |
| Invariants without proof, by path. | `without_proof` | mcp/src/agents_remember/application/knowledge_reader/paths.py:414-433 |
| The file, directory, test-file, explorer and without-proof cases. | `test_a_file_path_view_shows_prose_references_entries_families_and_linked_records`; `test_a_directory_view_is_bounded_to_its_own_level_children_and_route`; `test_a_test_file_shows_its_proofs_by_invariant_with_their_facets`; `test_the_explorer_lists_code_and_onboarding_children_with_entry_counts`; `test_the_without_proof_list_is_filterable_by_path` | mcp/tests/test_knowledge_reader.py:584-614; mcp/tests/test_knowledge_reader.py:716-760 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new module MIK-R29 adds, recording the carried L13 rule (a decision shown whole in every linking view), rulings 09:42:58 F2 (the bounded directory view and the root summary as the landing), F6 (the sibling-prefix and retired guards tested), F11 and F12 (one currentness helper, `states_at`), and one candidate invariant. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
