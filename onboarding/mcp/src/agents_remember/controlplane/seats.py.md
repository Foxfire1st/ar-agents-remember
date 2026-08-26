# mcp/src/agents_remember/controlplane/seats.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/seats.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

What the control plane needs to know about a seat, declared by the control plane.

## Code Commentary

### Logic

Named command-seat classification includes architect, orchestrator, and manager as roles whose
identity must be structurally qualified. `SeatRow` exposes primary, replacement, and binding
identity as `TaskDocumentRef`; it does not expose leaf or sprint keys. This classification remains separate from
notifier subordinate membership: wake supervision uses direct manager spawn topology and therefore
admits reviewer, curator, and future subordinate role names without changing this finite set.

ARSPAWN-L2 adds the shared `current_seat_occupant` selector. It validates primary and staged-heir
cardinality independently, prefers one incumbent while present, and promotes the staged heir only
after the incumbent leaves. Duplicate claimants raise `SeatOccupancyError`; consumers may translate
or locally suppress that ambiguity, but may never choose the first row.

Module-level surface:

- `SeatRow` (class, lines 36-90) — One seat's row, as the control plane reads it.
- `SeatDirectory` (class, lines 93-106) — The seat catalog, as the control plane reads it: two pure reads and nothing else.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- Control-plane consumers compare repository-qualified task-document values, not reconstructed
  leaf/sprint strings.
- The protocol is read-only; catalog implementations own persistence and mutation.
- `replacement_for_task_document_ref` is a staged generation of the same canonical seat, not a
  second namespace.
- Exactly one selector owns incumbent/heir precedence across the repository.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `SeatRow` (lines 36-90) — One seat's row, as the control plane reads it.. | `SeatRow` | mcp/src/agents_remember/controlplane/seats.py:36-90 |
| Defines the read-only catalog protocol consumed by structural selectors. | `SeatDirectory` | mcp/src/agents_remember/controlplane/seats.py:95-108 |
| Resolves one canonical current generation and fails closed on duplicate primaries or heirs. | `current_seat_occupant` | mcp/src/agents_remember/controlplane/seats.py:145-167 |

## 260713-TES-L5 Completion Round — Fix-Round Docstring

The module docstring no longer names "the routing, ladder and orphan predicates" — the L5
fix round rewrote it to "The routing and rebind predicates in this package" (the escalation
ladder and orphan-policy modules are deleted; dead-owner rows surface through the rebind
machinery). `SeatRow`/`SeatDirectory` behavior is unchanged: pure catalog reads of the seat
shape declared by the control plane.

## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed the documented
  independent cardinality checks and incumbent-before-heir precedence. Verification remains
  closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: added the shared canonical incumbent/staged-heir
  selector and typed ambiguity. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Replaced leaf/sprint protocol fields with primary, replacement, and
  binding `TaskDocumentRef` properties owned by the control plane.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: clarified the named sprint-seat set and its separation
  from role-neutral manager-subordinate supervision. Verification metadata remains pinned until
  closeout stamps the code commit.

- 2026-08-09T13:59+02:00 — 260713-TES-L5 curator completion round 2: recorded the
  fix-round docstring refresh (ladder/orphan predicates wording removed; "routing and rebind
  predicates" per the demolition). Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
