# mcp/src/agents_remember/controlplane/seats.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/seats.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-09T13:59+02:00 |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32` |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

What the control plane needs to know about a seat, declared by the control plane.

## Code Commentary

### Logic

Module-level surface:

- `SeatRow` (class, lines 36-90) — One seat's row, as the control plane reads it.
- `SeatDirectory` (class, lines 93-106) — The seat catalog, as the control plane reads it: two pure reads and nothing else.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `SeatRow` (lines 36-90) — One seat's row, as the control plane reads it.. | `SeatRow` | mcp/src/agents_remember/controlplane/seats.py:36-90 |
| Defines the class `SeatDirectory` (lines 93-106) — The seat catalog, as the control plane reads it: two pure reads and nothing else.. | `SeatDirectory` | mcp/src/agents_remember/controlplane/seats.py:93-106 |

## 260713-TES-L5 Completion Round — Fix-Round Docstring

The module docstring no longer names "the routing, ladder and orphan predicates" — the L5
fix round rewrote it to "The routing and rebind predicates in this package" (the escalation
ladder and orphan-policy modules are deleted; dead-owner rows surface through the rebind
machinery). `SeatRow`/`SeatDirectory` behavior is unchanged: pure catalog reads of the seat
shape declared by the control plane.

## Update History

- 2026-08-09T13:59+02:00 — 260713-TES-L5 curator completion round 2: recorded the
  fix-round docstring refresh (ladder/orphan predicates wording removed; "routing and rebind
  predicates" per the demolition). Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
