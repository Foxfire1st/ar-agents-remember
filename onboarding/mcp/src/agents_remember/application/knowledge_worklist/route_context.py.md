# mcp/src/agents_remember/application/knowledge_worklist/route_context.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Attaches mechanical governing-family route context using the worklist’s already parsed candidate knowledge.

## Code Commentary

_ChainLookups adapts record, family and families_governing queries to the shared leaf-chain selector. It supplies current parsed records with one complete IndexState and exact family member/route data, without opening a second index store. Each supplied record's lifecycle word is read through `record_status`, which answers a weakness's `state`, a status-bearing record's `status`, and the empty word for a dependent, so the lookup does not assume every record kind has a `status` attribute. Route candidates are equal/ancestor paths including the root. route_chain labels sorted path results mechanical. with_route_context recursively collects path/renamedTo values plus sourceBlobs keys and adds routeChain under facts.context while preserving the item and existing facts.

## Invariants And Boundaries

The runtime selector import avoids the leaf/currentness/worklist import cycle. Route context supplies retrieval information; it must not alter worklist item identity, trigger reach or acceptance.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Attaches mechanical governing-family route context using the worklist’s already parsed candidate knowledge. The runtime selector import avoids the leaf/currentness/worklist import cycle. Route context supplies retrieval information; it must not alter worklist item identity, trigger reach or acceptance. [1]
