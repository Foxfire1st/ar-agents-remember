# mcp/src/agents_remember/application/knowledge_writer/entry_handles.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Resolves same-document handoff invariant handles after allocating the entries that author those invariants.

## Code Commentary

ordered_entries uses stable ordering so direct/new-author entries precede handle references. assign_entries first identifies entries with no invariant_id, then reuses an owner/origin-bound record or mints the author’s invariant identity. A HANDLE_PREFIX reference must name such an author in this document and carry exactly the same statement; only then is its handle mapped to the already allocated identity. Ordinary invariant IDs go through the existing kind requirement.

## Invariants And Boundaries

A local handoff handle is not a separately minted canonical truth identity. Input list position cannot make a valid author inaccessible, and a matching-looking handle with a different statement is a reported authoring problem.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Resolves same-document handoff invariant handles after allocating the entries that author those invariants. A local handoff handle is not a separately minted canonical truth identity. Input list position cannot make a valid author inaccessible, and a matching-looking handle with a different statement is a reported authoring problem. [1]
