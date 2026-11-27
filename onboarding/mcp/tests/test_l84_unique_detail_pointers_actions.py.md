# mcp/tests/test_l84_unique_detail_pointers_actions.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression proofs ensuring relocated action pointers, Architect named action reads, task-layout pointers, and retirement stop boundaries remain reachable across compiled capsules and reject pointer or clause removal.

## Code Commentary

Checks `MOVED_INDEX_POINTERS` across the full role/operation matrix (`test_moved_piece_pointers_reach_each_required_compile_and_reject_removal`), verifies Architect leaf creation reaches `reference/tasks/document-authoring.md` and `core/acceptance.md#record-how-retained-evidence-will-be-maintained` (`test_leaf_creation_reaches_retained_evidence_lifecycle_and_rejects_removal`), verifies all nine `ARCHITECT_ACTION_READS` scenarios with single-removal and duplication mutation teeth, verifies Architect task-layout pointers to `requirement-design.md`, and checks canonical, digest, and delivered-detail retirement stop boundaries (`RETIREMENT_DETAIL_ROLES = frozenset({"manager"})`, with non-Manager roles reaching `refused-write.md` via the shared `skill://` link).

## Relationships

Pairs with `test_l84_unique_detail_pointers.py` (imports `_assert_moved_action_pointer`) and `test_l84_capsule_delivery_proofs.py` (imports `_compiled`, `_compiled_outcome`, `_assert_index_detail_pointer`, `_emitted_instruction_detail`, `_linked_instruction_source`, `_shipped_parsed`). Reads `core/digest-map.json` via `load_digest_map`.

## Evidence


- Full role/operation matrix test pins `every-role.md` filtering, `IN8.8` settings-authority pointer, and `MOVED_INDEX_POINTERS` with removal/duplication mutation checks. [1]

- Leaf-creation and Architect action/task-layout tests verify retained-evidence lifecycle, 9 named Architect scenarios, and `requirement-design.md` sections with mutation teeth. [2]
- Retirement stop boundary test confirms canonical `core/authority.md`, digested `core/every-role.md`, Manager's delivered `refused-write.md`, and other roles' served `skill://` link preserve permission stops. [3]
