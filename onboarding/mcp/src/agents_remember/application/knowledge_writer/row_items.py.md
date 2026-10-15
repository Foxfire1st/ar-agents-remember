# mcp/src/agents_remember/application/knowledge_writer/row_items.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Reads history-row worklist item identifiers literally while reporting malformed item values.

## Code Commentary

None gives empty tokens/refusals, and one string is accepted as a singleton. Other values must be a list. Non-string members report a refusal and are not appended; string members are preserved in order without stripping, deduplication or normalization. Blank/whitespace strings remain in the returned token list and also receive an explicit not-blank refusal.

## Invariants And Boundaries

This parser preserves the evidence of malformed tokens instead of repairing them into valid identifiers. It returns tokens and problems; callers must not equate a nonempty token list with successful admission or silently drop refusals.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Reads history-row worklist item identifiers literally while reporting malformed item values. This parser preserves the evidence of malformed tokens instead of repairing them into valid identifiers. It returns tokens and problems; callers must not equate a nonempty token list with successful admission or silently drop refusals. [1]
