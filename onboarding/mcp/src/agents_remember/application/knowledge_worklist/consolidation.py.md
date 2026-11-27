# mcp/src/agents_remember/application/knowledge_worklist/consolidation.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Defines the `consolidation_target` worklist item kind (`KNO-R05`), expands a task document's `consolidationList` into deduplicated worklist items and `consolidationListed` marks, and provides the gate predicates governing `consolidation_target` items and the `stands`/`unresolved` dispositions.

## Code Commentary

Registers `CONSOLIDATION_KIND` (`consolidation_target`, subject pattern `^(?:INV|FAM)-`, facts `("record", "revision", "families", "listed")`, owner `KNO-R05`) at import time via `register_item_kind`. `listing_from` accepts a `ConsolidationList` model or JSON mapping and returns `None` when empty. `consolidation_pass` unions listed families, listed rules, and every member of a listed family across either K_B or K_C (`_Reach.members`), producing one `consolidation_target` item per distinct subject sorted by ID, with item ID keyed on `[candidate_revision]` and `facts["unknown"] = True` when the subject exists on neither side. `ConsolidationPass.mark` attaches `consolidationListed: True` to `touched_invariant`, `stale_invariant`, and `reached_family` items whose subject is in the pass's subject set. `consolidation_target_open` keeps a list item open if the subject is `unknown`, if the leaf's history lacks an `InvariantRow`/`FamilyRow` for it at its K_C revision, or if a `FamilyRow`'s examined members changed revision in K_C. `new_disposition_reason` enforces that `stands` and `unresolved` answer ordinary items only when `consolidationListed` is `True`: `unresolved` answers any listed ordinary item, while `stands` answers only a listed `touched_invariant` item passing `_meaning_neutral` (not `added`/`retired`/`reanchored`, no entry in `COVERING_CLASSES`, and `baseRevision == candidateRevision == row.revision`, e.g., a title-only edit).

## Relationships

Called by `knowledge_worklist/compute.py` (`Listing`, `consolidation_pass`), `knowledge_worklist/leaf.py` (`Listing`, `listing_from`), `knowledge_worklist/leaf_inputs.py` (`Listing`), `knowledge_gate/direct.py` (`listing_from`), `knowledge_gate/predicates.py` (`CONSOLIDATION_KIND`, `consolidation_target_open`, `new_disposition_reason`), and `knowledge_writer/row_tests.py` (`CONSOLIDATION_KIND`). Depends on `knowledge_worklist/classify.py`, `knowledge_worklist/knowledge.py`, `knowledge_worklist/registry.py`, `models/knowledge_files/history.py`, and `models/knowledge_files/history_consolidation.py`.

## Evidence

- Module import registers `CONSOLIDATION_KIND` (`consolidation_target`, `^(?:INV|FAM)-`, owner `KNO-R05`) in the worklist item registry. [1]
- `consolidation_pass` expands listed families (using K_B and K_C membership) and listed rules into deduplicated, sorted `consolidation_target` items and records the reached subject set. [2]
- `consolidation_target_open` rejects unknown listed IDs, missing or stale-revision rule/family rows, and family rows whose examined members moved revision in K_C. [3]
- `new_disposition_reason` limits `unresolved` and `stands` on ordinary items to `consolidationListed` subjects, restricting `stands` to meaning-neutral `touched_invariant` items. [4]
