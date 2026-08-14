# mcp/src/agents_remember/serving/seat_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/seat_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T12:15+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external domain source governs this repository-local helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Attach-role normalization is deliberately narrow and fail-closed for an untyped harness. | `attach_seat_role` | mcp/src/agents_remember/serving/seat_binding.py:32-48 |
| Legacy role suffixes are detection-only. | `role_suffixed_leaf_base` | mcp/src/agents_remember/serving/seat_binding.py:51-64 |
| Structural assignment validates canonical task identity, altitude, and live pair ownership. | `assign_terminal_session_to_task` | mcp/src/agents_remember/serving/terminal_task_assignment.py:96-170 |

## Update History

- 2026-08-11T12:15+02:00 — Clarified that this file is a legacy/operator normalization helper, not
  the source of canonical structural identity. Verification remains pinned pending closeout.
- 2026-07-10T15:07+02:00 — Created for role normalization, explicit hand-opened role claims, and
  rejection of role-suffixed leaf workarounds.
