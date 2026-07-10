# mcp/src/agents_remember/serving/landing.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/landing.py`            |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`                                           |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`landing.py` owns the non-destructive completion classification for dashboard seats. It marks matching
catalog rows as `status:"landed"` after successful worktree integration/finalization so spent chats roll
into the dashboard archive while tmux remains available for inspection.

## Code Commentary

### 260707-HFX2-L17 Binding-Role Landing Filter

Completion-edge seat selection now matches the current binding role rather than immutable spawn
provenance. Rebound or hand-opened typed pipeline seats therefore land with their actual leaf role;
landing status/provenance and tmux-preservation behavior are unchanged.

### Logic

The domain function `land_seats_for_leaf(catalog, *, leaf_key, roles, reason, edge, at)` requires
callers to pass the completion edge's exact role set. It scans visible catalog rows, selects rows
whose `leaf_key` matches and whose `spawn_role` is in that caller-supplied set, and calls
`TerminalCatalog.mark_landed(session_id, at, reason, edge)` for each selected row. It returns the
changed entries so controllers can report session ids and emit observer events.

Unlike manual retire, this module never constructs `TerminalHost` and never kills a tmux session. A
landed row is an archive classification, not terminal cleanup.

### Invariants And Boundaries

- Landing is leaf-key scoped and role-filtered by the caller.
- Landing skips rows already `terminated`; `TerminalCatalog.mark_landed` owns the exact idempotence and
  transition rules.
- This module has no authority-policy check; it is called from completion edges that already succeeded.
  Manual retire authority remains in `retire.py`/`retire_policy.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Completion-edge controllers call `land_seats_for_leaf` after successful integrate/finalize and log each landed entry. | [worktree_tools.py](../controllers/worktree_tools.py) |
| The catalog status transition and landing provenance fields live in `TerminalCatalog`. | [terminal_catalog.py](terminal_catalog.py) |
| Manual retire remains the destructive/session-closing path. | [retire.py](retire.py) |
| Tests cover leaf/role selection and completion-edge auto-land results. | [../../../tests/test_seat_lifecycle.py](../../../tests/test_seat_lifecycle.py) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: moved landing role selection to current binding
  identity; no change to archive lifecycle semantics.

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: corrected the callable contract after
  reviewer F2. `roles` is a required completion-edge role set; the unused `LANDABLE_ROLES`
  constant was removed instead of becoming a broad default. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): created for the new
  non-destructive completion classification. Verification metadata remains pinned until closeout stamps
  the HFX2-L11 commit.
