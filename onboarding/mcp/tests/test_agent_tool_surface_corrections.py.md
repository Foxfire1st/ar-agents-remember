# mcp/tests/test_agent_tool_surface_corrections.py

## Governing Overview

[mcp/tests route overview](../overview.md)

## Purpose

**The leaf's case set for MIK-R73 and MIK-R83: the tool surface and the truthful read.** Each case protects
one stated behaviour of the two packets on a real fixture world — a converted memory tree, a Git code
checkout, a scratch coordination root and the registered tool handlers — rather than on a mock of the reader.

## Code Commentary

### Logic

- **Task-file discovery (MIK-R83 rules 1, 2, 4).** `test_task_folders_are_the_direct_children_except_the_archive`,
  `test_only_canonical_positions_are_a_task_document_or_a_contract` and
  `test_the_stray_scan_lists_copies_outside_canonical_places` assert the one walker, the canonical places and
  the stray facts.
- **A contract names its own place (rule 3).** `test_a_contract_at_a_canonical_place_naming_another_path_is_refused`
  (parametrised over the named places) and `test_a_contract_outside_the_canonical_places_is_not_checked`.
- **Index and page answers (MIK-R73 rule 6).** `test_a_page_states_its_index_state_and_never_calls_a_partial_walk_complete`
  and `test_knowledge_index_answers_legacy_format_for_an_unconverted_tree`.
- **The mounted writer (rule 1).** `test_the_mounted_writer_refuses_before_it_writes`, and
  `test_the_writer_and_the_reads_have_their_answer_rows` for the MIK-R108 rows.
- **Record link states (rule 2).** `test_registered_record_targets_observe_full_anchors_and_selected_routes`
  (parametrised over `symbol`, `line_range` and `file`) reads one assumption through the registered
  `knowledge_read` view `record` at a commit and at the working tree, then asserts the same rows through the
  dashboard's HTTP route: an unchanged anchor is `current`, an edited or deleted one `stale` with the observed
  and recorded blobs named, a captured route is `current` and a deleted one `stale`, an unreadable tree is
  `unverifiable` with its reason, and a committed selection is immune to later checkout edits.
  `test_registered_record_requirement_targets_preserve_owner_answers_and_latest_version` (parametrised over
  `archived`) asserts the owner's own answer: `resolved`, and `unresolved` with the owner's exact code
  (`task-intent-requirement-packet-version-mismatch`, `…-missing`), the archival flag, and the latest approved
  version even when a draft exists.
- **The read that finds a card (rule 5).** `test_a_card_omitted_by_a_stale_route_index_is_served_registered`.
- **The leaf read (rule 6).** `test_a_registered_leaf_read_observes_both_edited_worktrees`,
  `test_a_leaf_read_names_its_own_source_and_memory_roots`,
  `test_an_unscoped_read_is_identified_as_the_official_line` and
  `test_a_leaf_whose_memory_worktree_is_gone_is_refused_by_name`.
- **The observed tree (rule 7).** `test_the_working_tree_selector_captures_and_keeps_the_store_readable` and
  `test_a_clean_checkout_reads_its_commit_and_captures_nothing`.
- The helpers `_linked_assumption`, `_registered_target_states` and `_dashboard_target_states` build one
  record with explicit targets and read the same states through the mounted tool and the HTTP route, which is
  what makes the parity assertion possible.

### Conventions

- Evidence comes in three classes and the card says which each case stands on: direct pure-function and
  path-validation cases, direct builder calls (`knowledge_write_payload`) and mocked-admission cases, and the
  CLI, registered-handler (`EntryPointWorld`) and real FastAPI route cases. A change in the registration is
  caught only by the registered and HTTP class; the direct cases assert their owner's behaviour without the
  route.
- The fixture world is the existing `converted_reader_world` / `EntryPointWorld` contract; no new fixture
  protocol is introduced.

### Invariants And Boundaries

- **A case asserts a stated behaviour, not a code path.** The parametrised locator cases exist because the
  packet names three locator kinds with different observation rules.
- **The dashboard parity case is the point of the second half of rule 2**: the two surfaces must answer the
  same target states, and the test compares the whole row set rather than one field.
- **Nothing here writes to a repository**: the world's Git state is a scratch clone and the capture store is
  removed by the read.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is `MIK-R73@v1` and
`MIK-R83@v1` of task `260928_maintained-invariant-knowledge`, whose expected-evidence sections name these
behaviours; the packets live outside the code and memory repositories and are named here, not cited as rows.

### Repo-Internal References

No numbered references are recorded for this new module. The behaviours it protects are recorded on the cards
of the modules that realize them (`knowledge_reader/records.py`, `read_files.py`, `task_scoped_mcp.py`,
`kernel/primitives/runtime_config.py`, `worktrees/worktree_contract.py`).

### Cross-Repo References

None.
