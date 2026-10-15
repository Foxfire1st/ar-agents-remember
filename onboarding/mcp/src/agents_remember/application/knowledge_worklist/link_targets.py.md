# mcp/src/agents_remember/application/knowledge_worklist/link_targets.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Raises link_target work for a surviving authored record link whose retrieval target this leaf removed.

## Code Commentary

The registered kind has no satisfying history-row lookup. Base record links other than reconsider_on are inspected only while the same canonical target key remains in K_C. A formerly populated route becoming empty, a disappearing anchored path, or a symbol resolving at B but not C supplies a named removal reason. Symbol resolution explicitly uses the base side at B. Items use stable record/target keys, deduplicate by subject and sort deterministically.

## Invariants And Boundaries

Range-content changes alone raise no item: links are retrieval pointers, not realization-currentness claims. Remove or restate the target key in K_C; a no-impact history row cannot answer it. Reconsideration links belong to their separate trigger owner.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Raises link_target work for a surviving authored record link whose retrieval target this leaf removed. Range-content changes alone raise no item: links are retrieval pointers, not realization-currentness claims. Remove or restate the target key in K_C; a no-impact history row cannot answer it. Reconsideration links belong to their separate trigger owner. [1]
