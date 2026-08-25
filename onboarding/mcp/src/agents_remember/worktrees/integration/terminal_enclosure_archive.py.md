# mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Integration overview](overview.md)

## Purpose

Publishes a crash-safe terminal enclosure archive before destructive worktree-root cleanup.

## Code Commentary

### Logic

It proves terminal operations, resolved workers/mutations/publications, exact cleanup arguments, canonical manifest entries, receipt readback, and convergent retry after interrupted archive/unlink.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Cleanup cannot remove the enclosure root until durable archive and receipt prove everything needed for later status/recovery; mismatched existing evidence refuses.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_OPERATION_RECORD` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:1-883 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_OPERATION_RECORD` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:1-883 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_OPERATION_RECORD` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:1-883 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
