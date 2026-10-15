# mcp/tests/test_writer_correction_history.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Describes paired-tree regression assertions for writer history eligibility, stable refusals and rule15 relocation.

## Code Commentary

A synthetic extended row adds one entry and relocates two carried entries while preserving invariant bytes, old IDs/origins and authored fields; before/after covers and persisted-request rerun bytes are asserted. The same no_impact request retains its exact refusal and no-write boundary. Other cases protect closed changed rows against hiding/reordered items, malformed persisted worklists, family guarantee changes, own-record aliases, and itemless planned/hunk rows, with explicit mutation checks.

## Invariants And Boundaries

Rule15 source tests describe the repaired candidate, not permission to use it for this leaf’s own memory. The thirteen deferred copy pairs remain under L63 custody; test declarations and existing historical passes are not new execution evidence.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Describes paired-tree regression assertions for writer history eligibility, stable refusals and rule15 relocation. Rule15 source tests describe the repaired candidate, not permission to use it for this leaf’s own memory. The thirteen deferred copy pairs remain under L63 custody; test declarations and existing historical passes are not new execution evidence. [1]
