# mcp/tests/test_writer_correction_history.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Describes paired-tree regression assertions for writer history eligibility, stable refusals and rule15 relocation.

## Code Commentary

A synthetic extended row adds one entry and relocates two carried entries while preserving invariant bytes, old IDs/origins and authored fields; before/after covers and persisted-request rerun bytes are asserted. The same no_impact request retains its exact refusal and no-write boundary. Other cases protect closed changed rows against hiding/reordered items, malformed persisted worklists, family guarantee changes, own-record aliases, and itemless planned/hunk rows, with explicit mutation checks.

The own-leaf renewal regression records a real prior own row, shifts its realization anchor and retains that old history through another leaf's carry. It observes R09 and the missing worklist subject, then renews the same row ID with the current after-anchor and checks byte-idempotent repetition. Fresh own-row cases include foreign-history and same-operation controls across literal and handle aliases; they retain the exact refusal and no-mutation checks. Malformed-history non-admission is a separately inspected production boundary, not a native malformed-history execution claim from these cases.

## Invariants And Boundaries

Rule15 source tests describe the repaired candidate, not permission to use it for this leaf’s own memory. The thirteen deferred copy pairs remain under L63 custody; test declarations and existing historical passes are not new execution evidence.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Describes paired-tree regression assertions for writer history eligibility, stable refusals and rule15 relocation. Rule15 source tests describe the repaired candidate, not permission to use it for this leaf’s own memory. The thirteen deferred copy pairs remain under L63 custody; test declarations and existing historical passes are not new execution evidence. [1]

- A persisted own row renews at the shifted after-anchor without a worklist item, retaining row identity and idempotent bytes. [2]
- Fresh own rows retain refusal despite foreign history or current-operation authoring. [3]
