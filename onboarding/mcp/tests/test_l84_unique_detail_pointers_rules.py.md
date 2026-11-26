# mcp/tests/test_l84_unique_detail_pointers_rules.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression proofs that retired per-topic rule files remain absent while their clauses stay intact on their current owning surfaces and that approved short rules match `core/digest-map.json` SHA-256 bindings.

## Code Commentary

`CURRENT_INLINE_RULE_CLAUSES` maps 28 retired `reference/...` rule files to their current owning surface, heading, and exact clauses; `test_v13_inline_rules_reach_their_actual_owning_sections_and_reject_deletion` asserts none of the retired files appear in compiled `detail_references` or `{{detail:...}}` pointers and verifies every clause with deletion and duplication mutation checks across the manifest matrix. `CURRENT_SHORT_RULE_CLAUSES` pins six `digest-map.json` units (`AU11.6`, `AC0.3`, `AU11.4`, `AU10.4`, `AC0.5`, `AU10.3`), verifying line-slice SHA-256 digests, audience-filtered shared-block delivery, and absence of `REMOVED_SHORT_RULE_ACTIONS`. `CURRENT_GROUPED_DETAIL_CLAUSES` verifies unfragmented whole-owner index reads for `requirement-design.md`, `review-baseline.md`, and `sandbox-actors.md`.

## Relationships

Sibling split of `test_l84_unique_detail_pointers.py` alongside `test_l84_unique_detail_pointers_actions.py`. Depends on `test_l84_capsule_delivery_proofs.py`, `filter_shared_block`, `shared_block`, `load_digest_map`, `REMOVED_SHORT_RULE_ACTIONS`, and `RENEW_COMMAND`.

## Evidence

- All 28 retired rule sources are verified absent from compiled details while their clauses remain intact in current owning sections with deletion/duplication mutation checks. [1]
- Six `digest-map.json` short rules are pinned against line-slice SHA-256 hashes, audience-filtered shared blocks, and removal of deprecated step reads. [2]
- Grouped detail owners (`requirement-design.md`, `review-baseline.md`, `sandbox-actors.md`) are asserted to be linked whole (no fragment) and preserve their clauses. [3]
