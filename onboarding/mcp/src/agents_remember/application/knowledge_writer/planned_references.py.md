# mcp/src/agents_remember/application/knowledge_writer/planned_references.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Checks planned-effect references at their owning requirement, task-decision and stored-record boundaries before publication.

## Code Commentary

For a deferred row with a requirement reference, resolve_requirement_endpoint must return resolved or the refusal identifies key, code and correction. A decision reference requires a task-owner resolver and carries its detailed refusal. An invariant reference must name a stored invariant, not merely an existing record of another kind; a row reference must be present in known_ids. None denotes no unresolved reference found by these checks.

## Invariants And Boundaries

The helper consumes a parsed PlannedEffectRow; it does not choose a disposition, allocate requirement authority or replace model validation. Missing task ownership is not treated as a resolved dropped-row decision.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Checks planned-effect references at their owning requirement, task-decision and stored-record boundaries before publication. The helper consumes a parsed PlannedEffectRow; it does not choose a disposition, allocate requirement authority or replace model validation. Missing task ownership is not treated as a resolved dropped-row decision. [1]
