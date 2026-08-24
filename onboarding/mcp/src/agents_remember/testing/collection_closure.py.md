# mcp/src/agents_remember/testing/collection_closure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/collection_closure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Analyzes module/class import-time statements that pytest collection would execute before a
selected test body begins.

## Code Commentary

`CollectionClosure` delegates imports, expressions, unsafe effects, and unsupported collection
constructs to the dependency analyzer while handling assignments, decorators, class bodies, and
other supported AST statements in source order.

## Invariants And Boundaries

- Collection-time behavior is part of eligibility even when the selected test body is pure.
- Unknown executable statements refuse; the analyzer never runs them to discover behavior.
- First source-order refusal is stable and source-backed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One collection analyzer owns supported statement dispatch. | `CollectionClosure` | mcp/src/agents_remember/testing/collection_closure.py:35-150 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
