# mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Measures a stored assessment's dependency binding against the exact identities supplied by its current read.

## Code Commentary

Recorded and measured identity maps remain distinct. `measured_binding_status` returns unavailable for unread dependencies, not-measured for absent coverage, stale for an observed disagreement, and current only when the required identities are fully measured and equal. Separate semantic freshness reasons are carried without rewriting the stored assessment. The removed _subject_state helper is not the current measurement owner; absence of evidence cannot be reported as current.

## Evidence

### Repo-Internal References

- `measured_binding_status` owns the current boundary described above. [6]
- `assessment_currentness` owns the current boundary described above. [7]
- `require_assessment_dependencies` owns the current boundary described above. [8]
