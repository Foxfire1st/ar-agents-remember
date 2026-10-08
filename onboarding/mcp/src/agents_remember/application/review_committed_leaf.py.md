# mcp/src/agents_remember/application/review_committed_leaf.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Reopens the exact retained comparison of a committed leaf and reports the limitations of that retained subject.

## Code Commentary

The default generation first uses the converted four-tree reopen and `tree_resolution`. An explicitly named historical generation, or the legacy path, reopens its retained comparison record and passes it to `legacy_comparison_resolution`: exact source and retained evidence remain readable, while canonical dataset halves report legacy unavailability. The reader does not substitute today's candidate or recreate a deleted dataset. `ClosedLeafReview` carries the reopened result and its limitation sentence; the removed dataset measurement and provenance helper suite is not part of this module.

## Evidence

### Repo-Internal References

- `resolve_committed_leaf_review` owns the current boundary described above. [28]
- `ClosedLeafReview` owns the current boundary described above. [29]
- `closed_leaf_limitations` owns the current boundary described above. [30]
