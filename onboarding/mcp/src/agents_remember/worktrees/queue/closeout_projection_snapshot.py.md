# mcp/src/agents_remember/worktrees/queue/closeout_projection_snapshot.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_snapshot.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Carries one immutable closeout-projection source observation and builds the disposable persisted
projection only when the observation is readable and completely classified.

## Code Commentary

### Logic

`ProjectionSourceSnapshot` freezes identity, classification, current members, and capture time.
`build` returns no projection for unreadable or incomplete source identity; otherwise it constructs
`CloseoutProjectionBuild` from only that snapshot. Prior projection rows are never an input.

### Conventions

- The source observation is a frozen dataclass.
- `None` means the source is unreadable or unclassified; it never invents a synthetic identity.

### Invariants And Boundaries

- A snapshot is immutable and describes one current census.
- Unreadable/unclassified identity cannot publish a replacement projection.
- This value object owns no source reads, lifecycle mutation, or queue selection.

### Todos

None.

## Docs References

No external source is required.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The immutable snapshot gates projection construction on complete readable identity. | "One exact current source census; old projection rows are never an input." | mcp/src/agents_remember/worktrees/queue/closeout_projection_snapshot.py:17-39 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — Checklist follow-up: re-read the exact new snapshot definition and
  retained its range without fabricating a commit verification stamp.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the projection source-snapshot card.
  Verification remains closeout-owned.
