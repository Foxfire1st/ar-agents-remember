# mcp/src/agents_remember/testing/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Defines the deliberately small package facade for classification, direct diagnostics, and the two
typed selection outcomes. Internal AST, admission, bootstrap, and evidence helpers stay behind
their owning modules.

## Code Commentary

`__all__` publishes `classify_direct_selection`, `run_direct_diagnostic`, result/error types, and
eligible/refused decision types. Adding an internal helper here turns it into supported package
surface and must be justified.

## Invariants And Boundaries

- The facade exposes diagnostics, not Dagger admission or certifying evidence constructors.
- One canonical classifier and one canonical runner are exported; no compatibility aliases.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public testing facade is explicitly enumerated. | `__all__` | mcp/src/agents_remember/testing/__init__.py:17-32 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
