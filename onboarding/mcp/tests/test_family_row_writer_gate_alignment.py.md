# mcp/tests/test_family_row_writer_gate_alignment.py

## Governing Overview

[overview](overview.md)

## Purpose

Regression and gate-alignment test module verifying that `knowledge_write` accepts empty or omitted `examined` lists for empty families and base-revision fallback for members that left `K_C`, and that the written rows satisfy the knowledge gate.

## Code Commentary

All worlds are prepared through `writer_worklist_test_support.prepare_worklist` and `knowledge_writer_test_support.build_world`, exercising `native_write_knowledge`, `family_row_open`, and `evaluate_leaf_gate` on real Git fixture repositories:

- `test_empty_family_admits_empty_or_omitted_examined_and_answers_gate`: parametrized over active and retired empty families and over `examined: []` vs omitted `examined`. Modifies the family record so the worklist raises `reached_family` with `facts.members == []`, verifies the gate holds the item open before writing, writes the row (`examined == []`, `revision == 2`), and verifies both `family_row_open` and full `evaluate_leaf_gate` accept it.
- `test_empty_examined_refused_when_family_has_members_at_either_side`: parametrized over `[]` and omitted `examined`; verifies refusal with `"a family row names every member the curator examined"` and byte-unchanged memory when a member exists at `K_B` only (even with leaf `HEAD` already empty, proving worklist facts govern over `state.base_record`) or at `K_C` only.
- `test_empty_examined_refused_without_reached_family_item_or_worklist`: verifies refusal when the family has no `reached_family` worklist item and when a wave owner has `worklist=None`.
- `test_empty_examined_refused_when_same_write_adds_a_member`: parametrized over `[]` and omitted `examined`; verifies refusal when the same write batch adds a member to an empty family whose persisted worklist still shows `facts.members == []`.
- `test_member_that_left_candidate_stamps_base_revision_and_answers_gate`: removes `BASE_INVARIANT` (base revision 3) from `K_C` while advancing `SURVIVOR_INVARIANT` from revision 2 to 4; verifies the written family row stamps revisions 3 and 4 respectively and satisfies `family_row_open`.
- `test_examined_member_neither_stored_nor_in_worklist_facts_is_refused`: verifies `"examined member ... is not a stored invariant"` refusal for an unknown invariant ID, a stored family ID, and an absent member whose worklist entry has `base: None` or `base: 0`.

## Relationships

- Registered once in `unit-regression` in `mcp/tests/test-evidence-lanes.toml` and declared as an exact consumer of `mcp/tests/_user_settings_guard.py`, `mcp/tests/fixtures/repository_profiles/node/package-lock.json`, `mcp/tests/knowledge_writer_test_support.py`, and `mcp/tests/writer_worklist_test_support.py` in `mcp/tests/evidence-lifecycle.toml`.
- Guards `mcp/src/agents_remember/application/knowledge_writer/family_rows.py`, `authoring_rows.py`, `authoring.py`, and `writer.py` against the unchanged gate in `application/knowledge_gate/predicates.py`.
- These descriptions document test-module source definitions and catalog declarations, not an invocation receipt.

## Evidence

- Active and retired empty families admit explicit `[]` and omitted `examined` and satisfy both `family_row_open` and `evaluate_leaf_gate`. [1]
- Empty or omitted `examined` is refused when members exist at `K_B` only or `K_C` only, without a `reached_family` item or worklist, or when the same write adds a member. [2]
- A member absent from `K_C` stamps its worklist base revision and satisfies `family_row_open`, while unknown names, non-invariants, and invalid bases are refused. [3]







- The module is selected in `unit-regression` and listed on its four source-derived artifact consumer lists. [4]
