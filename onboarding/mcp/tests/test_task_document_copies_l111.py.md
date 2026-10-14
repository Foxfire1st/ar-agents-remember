# mcp/tests/test_task_document_copies_l111.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard the leaf/requirement copy set and transactional refresh on isolated typed-reference, reclamation, budget and rollback fixtures.

## Code Commentary

Typed persisted requirement references are copied as real task-documents files and represented in index rows. Reconciliation controls add/remove requirements, preserve a parent-row-bound leaf through refresh, and reject an unintended master copy. Budget and scan cases distinguish report populations from the rows that fit an answer.

The admitted-large-copy test injects an INDEX write failure after a public task write and compares the whole copy-tree digests with its pre-call snapshot. It expects an I/O ToolError, not an ordinary task-state refusal; the evidence is restored copy bytes, not successful publication. The leaf-clear case exercises the union refresh and reclamation while retaining the leaf's rendered file.

Helper-seam controls and registered-tool cases have different proof scopes. These fixtures do not establish a real host start, every malformed requirement's admission policy, or content-hash drift checking beyond the source's hash budget.

## Evidence

- Typed references produce a real requirement copy and a nonmissing index row. [1]
- An injected INDEX failure restores the admitted large copy-tree snapshot. [2]
- Clearing leaf requirements reclaims their copies while retaining only the leaf document. [3]
