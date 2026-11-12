# mcp/src/agents_remember/application/memory_quality/endpoints.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Observes authored requirement references separately from validator findings and their acceptance verdict.

## Code Commentary

_references traverses record links and numbered sidecar reference targets from the parsed knowledge tree, retaining each authored occurrence and its exact field path. requirement_endpoint_documents delegates resolution to the requirement endpoint owner, then reports original reference, canonical key, state, archive flag, task root, code and detail. The complete occurrence list sorts by declaring path and field.

## Invariants And Boundaries

Resolution observations do not rewrite authored links or change the validator verdict. Unresolved and archived states remain explicit observations; this module does not substitute a fabricated endpoint or infer task acceptance.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Observes authored requirement references separately from validator findings and their acceptance verdict. Resolution observations do not rewrite authored links or change the validator verdict. Unresolved and archived states remain explicit observations; this module does not substitute a fabricated endpoint or infer task acceptance. [1]
