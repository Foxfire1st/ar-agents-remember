# mcp/src/agents_remember/application/memory_quality/knowledge_inputs.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Prepares derived route-index inputs and compact worklist/gate/proof-coverage summaries without taking over their judgments.

## Code Commentary

build_route_indexes calls the missing-index owner, which leaves existing stale bytes untouched. A FileNotFoundError becomes a named onboarding-root build error only when the code root exists and onboarding root is absent; other cases re-raise. without_proof projects converted invariant coverage as informational rows/problem, returning None when unavailable under that owner. knowledge_briefs summarizes only already supplied worklist and gate results, omitting absent inputs.

## Invariants And Boundaries

Building an absent cache is distinct from refreshing a stale index. Without-proof inventory is not actionable merely because it is populated, and a summary never recomputes or accepts the worklist or gate.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Prepares derived route-index inputs and compact worklist/gate/proof-coverage summaries without taking over their judgments. Building an absent cache is distinct from refreshing a stale index. Without-proof inventory is not actionable merely because it is populated, and a summary never recomputes or accepts the worklist or gate. [1]
