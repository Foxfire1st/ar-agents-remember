# mcp/tests/test_worktree_sync_knowledge_merge.py

## Governing Overview

[overview](overview.md)

## Purpose

Tests for the knowledge merge in managed sync: the structural merge of knowledge files on converted or crossing memory merges, the conversion boundary, and the reference alignment through the real transaction.

## Code Commentary

The tests drive structural knowledge merging on converted or crossing memory merges and the conversion boundary. All-unconverted fast-forward/merge movement refuses with the central `legacy-format` message before mutation; converted merges never fall back to plain Git when the structural merge is unbound. Already-current and `skip-memory` plans are not structural-merge claims.
Both-lines-added references align to a fresh number through the transaction; the report seam checks renumbered-reference, evidence-only, skip-only, conflict, converted and empty plans; it asserts no alignedCards-only emission control; and a successful sync
carries the journaled report and counts. `_unconverted_line` and `_converted_lines` take a `source_branch` (default `main`) and pass it to `SyncFixture`, and `Lines` moves code on that branch, so another suite can build converted lines on a named official branch.

## Evidence

- Both lines added one reference each: the merge aligns them to a fresh number. [2]
- The report seam keeps every nonzero alignment population. [3]

- Evidence-only and skip-only plans write a report. [4]

- A successful sync carries the journaled report and counts. [5]
