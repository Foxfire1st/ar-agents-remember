# mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_archive.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_archive.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Legacy lifecycle bridge overview](overview.md)

## Purpose

Validates and crash-safely publishes schema-1 terminal archives and receipts.

## Code Commentary

### Logic

It checks terminal/recovery commit evidence, constructs expected archive payloads, handles existing identical publications, recovers receipt write/unlink interruption, and binds payload digests.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Only terminal legacy records with complete exact evidence may archive; mismatched existing bytes refuse; publication and unlink retry converge idempotently.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_ReceiptWrite` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_archive.py:1-309 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_ReceiptWrite` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_archive.py:1-309 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_ReceiptWrite` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_archive.py:1-309 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
