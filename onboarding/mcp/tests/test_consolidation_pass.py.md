# mcp/tests/test_consolidation_pass.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

End-to-end and unit verification suite for a consolidation pass across the worklist generator, leaf knowledge gate, item predicates, knowledge writer, and `TaskDocument.consolidationList` schema.

## Code Commentary

Reuses `test_knowledge_worklist.World` real Git code/memory fixtures and `knowledge_writer_test_support.build_world` to verify five contracts: (1) `Listing` raises one deduplicated `consolidation_target` item per listed family, listed rule, and family member beside normal change items, marks listed subjects on today's items with `LISTED_MARK`, leaves unlisted unchanged records silent, and rotates item IDs on revision bumps; (2) `evaluate_leaf_gate` holds open until every listed and accompanying item is closed—specifically rejecting a `stands` family row as a closure for `reached_family` while accepting `no_impact` to close both; (3) `item_open_reason` enforces that `stands` closes a title-only `touched_invariant` only when listed (never when an entry must be covered), and `unresolved` closes today's items only for listed subjects, while `consolidation_target` requires matching current revision and refuses unknown IDs; (4) `write_knowledge` refuses consolidation-task rule rows lacking `testsRun`/`testsNotRun`/`noProofRecorded`, records `consolidationSubjects` on the history file, keeps revision unchanged on title-only edits, accepts `unresolved`/`noProofRecorded`, and passes shape checks on persisted `consolidation_target` worklists; and (5) `TaskDocument.consolidationList` validates non-empty/pattern/no-duplicate constraints, forbids master documents, renders `**Consolidation list:**`, and registers as a `LIFECYCLE` field.

## Relationships

Exercises `application.knowledge_worklist.consolidation`, `application.knowledge_gate` (`evaluate_leaf_gate`, `predicates.item_open_reason`), `application.knowledge_writer`, and `tasks` (`TaskDocument`, `render_markdown`, `document_field_effects`). Shares test fixtures with `test_knowledge_worklist.py`, `test_planned_knowledge_effects.py`, `knowledge_writer_test_support.py`, and `writer_corrections_test_support.py`. Complements `test_consolidation_state.py` (post-closeout state and writer table) and `test_consolidator_role.py` (role launch and settings).

## Evidence

- Verifies `consolidation_target` deduplication across shared family members, revision-sensitive item IDs, `LISTED_MARK` tagging on today's items, and zero items for unlisted unchanged records. [1]
- Verifies `evaluate_leaf_gate` stays blocked when a family `stands` row leaves `reached_family` open and passes once a single `no_impact` row closes both items. [2]
- Verifies `stands` and `unresolved` predicate gating against `touched_invariant`, `reached_family`, and `consolidation_target` (including stale revision, missing row, and unknown subject). [3]
- Verifies `write_knowledge` records `consolidationSubjects`, preserves revision on title-only edits, and writes `stands`, `unresolved`, `testsRun`/`testsNotRun`, and `noProofRecorded` rows. [4]
