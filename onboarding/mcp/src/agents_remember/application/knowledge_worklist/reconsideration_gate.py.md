# mcp/src/agents_remember/application/knowledge_worklist/reconsideration_gate.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Evaluates currentness and satisfying-row conditions for already produced reconsideration items at the registered gate seam.

## Code Commentary

The candidate decision set supplies superseded identities; a superseded item returns no open reason. Ordinary fired changes remain for reconsideration_item_open. For REFRESH_NOT_CURRENT, the addressed link must still be an anchor: an exact restored baseTarget needs no new refresh, otherwise observe_entry checks current candidate content. An absent/non-anchor/noncurrent refreshed link returns the explicit currentness reason. A failed code read raises CodeReadError instead of passing. If all fired changes are resolved refresh checks, the item closes; remaining changes still need the pure satisfying-row predicate.

## Invariants And Boundaries

This function does not invent triggers or cascading reconsideration. A satisfying history row alone cannot make a refreshed stale anchor current. Supersession, source observation and row satisfaction remain separate decisions.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Evaluates currentness and satisfying-row conditions for already produced reconsideration items at the registered gate seam. This function does not invent triggers or cascading reconsideration. A satisfying history row alone cannot make a refreshed stale anchor current. Supersession, source observation and row satisfaction remain separate decisions. [1]
