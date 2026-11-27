# mcp/src/agents_remember/application/knowledge_writer/row_reason_evidence.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Preserves writer-appended foreign-evidence segments (`" Evidence (<hand-off entry>): ..."`) on history row `reason` strings across later rewrites of the same row (MIK-R53 rule 8).

## Code Commentary

`EVIDENCE_MARKER` (`" Evidence ("`) is the sole delimiter written by the knowledge writer when appending foreign-record update evidence to a row reason. `carried_evidence_segments(reason)` scans forward by `str.find` for every `EVIDENCE_MARKER` slice, preserving segments byte-exact including an edge-case trailing bare `" Evidence ("` marker that a naive `split()` would drop on a reason-only rewrite. `with_carried_evidence(reason, carry)` appends every segment extracted from `carry` that is not already present in `reason` (with an explicit `endswith` check for a bare `EVIDENCE_MARKER` segment), preventing duplication across repeated rewrites.

## Relationships

Imported by `knowledge_writer/authoring_rows.py` (`with_carried_evidence`). Standalone utility with no internal imports.

## Evidence

- `EVIDENCE_MARKER` fixes `" Evidence ("` as the delimiter for writer-appended foreign-evidence segments. [1]
- `carried_evidence_segments` scans `reason` using `str.find` to recover every appended segment byte-exact, including a trailing bare marker. [2]
- `with_carried_evidence` appends each prior segment from `carry` missing from `reason` without duplicating already-carried segments. [3]
