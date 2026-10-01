# mcp/src/agents_remember/serving/seat_binding.py

## Governing Overview

[serving overview](overview.md)

## Purpose

This small compatibility helper resolves an attach role for legacy/operator terminal assignment and
recognizes old role-suffixed leaf references so callers can refuse them with corrective guidance.
Canonical structural seat identity is owned elsewhere by task document plus role.

## Code Commentary

`attach_seat_role` fixes plain terminals to `terminal`, otherwise prefers an explicit requested role,
then spawn provenance, then a previously typed non-legacy binding. It never silently assigns an
untyped harness to `chat`. `role_suffixed_leaf_base` recognizes maintained pipeline-role suffixes
only as a legacy diagnostic.

This module does not resolve task documents, arbitrate seats, authorize callers, or persist catalog
state. Structural assignment validates the canonical task document and role altitude in
`terminal_task_assignment.py`.

## Invariants And Boundaries

- Role inference is compatibility input normalization, not structural authority.
- Plain terminals stay terminal seats.
- An untyped harness requires an explicit role.
- Role-suffixed leaf forms are rejected; they are not alternate canonical addresses.

## Evidence

### Docs References

No external domain source governs this repository-local helper.

No configured domain documentation was available.

### Repo-Internal References

- Attach-role normalization is deliberately narrow and fail-closed for an untyped harness. [1]
- Legacy role suffixes are detection-only. [2]
- Structural assignment validates canonical task identity, altitude, and live pair ownership. [3]
