# mcp/src/agents_remember/serving/landing.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/landing.py`            |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                           |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`landing.py` owns the non-destructive completion classification for dashboard seats. It marks matching
catalog rows as `status:"landed"` after successful worktree integration/finalization so spent chats roll
into the dashboard archive while tmux remains available for inspection.

## Code Commentary

### 260707-HFX2-L16 Binding-Role Landing Filter

Completion-edge seat selection now matches the current binding role rather than immutable spawn
provenance. Rebound or hand-opened typed pipeline seats therefore land with their actual leaf role;
landing status/provenance and tmux-preservation behavior are unchanged.

### Logic

The domain function cit:([`land_seats_for_leaf`], mcp/src/agents_remember/serving/landing.py:9-28)
receives a `SeatClosure` plus the leaf key and role set. It scans visible catalog rows, selects rows
whose `leaf_key` matches and whose `binding_role` is in that role set, and calls
`TerminalCatalog.mark_landed` with the closure's `at`, `reason`, and `edge` for each selected row. It
returns the changed entries so application entry points can report session ids and emit observer events.

This module never constructs `TerminalHost` and never kills tmux. Since ARG-L1 it is the explicit
`autoCloseCompletedSeats=false` compatibility path and still handles pre-flip archive rows; normal
default completion uses exact-report-gated retirement instead.

### Invariants And Boundaries

- Landing is leaf-key scoped and role-filtered by the caller.
- Landing skips rows already `terminated`; `TerminalCatalog.mark_landed` owns the exact idempotence and
  transition rules.
- This module has no authority-policy check; it is called from completion edges that already succeeded.
  Manual retire authority remains in `retire.py`/`retire_policy.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Completion cleanup calls `land_seats_for_leaf` only in the close opt-out branch. | "landed = land_seats_for_leaf(" | mcp/src/agents_remember/application/completion_cleanup.py:51-56 |
| The same compatibility branch logs every landed catalog entry. | "log_landed_event(config, entry)" | mcp/src/agents_remember/application/completion_cleanup.py:57-59 |
| The catalog status transition and landing provenance fields live in `TerminalCatalog`. | `TerminalCatalog` | mcp/src/agents_remember/serving/terminal_catalog.py:48-386 |
| Manual retire remains the destructive/session-closing path. | `SeatClosure`; `retire_entry` | mcp/src/agents_remember/serving/retire.py:21-34; mcp/src/agents_remember/serving/retire.py:37-71 |
| Tests cover leaf/role selection, opt-out end-to-end landing, and retained archive cleanup behavior. | `AutoLandHookIntegrationTests`; `LandSeatsForLeafTests` | mcp/tests/test_seat_lifecycle.py:593-869 |

## 260731-EFA-L2 Current Delta

Landing currently passes `SeatClosure.at`, `SeatClosure.reason`, and `SeatClosure.edge` to
`TerminalCatalog.mark_landed`; retirement persists those facts plus `SeatClosure.by_session`, while
the landing transition does not persist `by_session`. The `SeatClosure` documentation says both
closure paths write four facts, so whether landing should gain that authority provenance or the claim
should be narrowed remains an explicit Tier-3 developer-owned question. The landing selection rules
remain leaf-key and binding-role scoped.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T05:45+02:00 — 260805-ARG-L1: repositioned landing as the settings opt-out and
  pre-flip archive compatibility path; the domain mechanic itself is unchanged.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the shared `SeatClosure` provenance value on the landing path.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: moved landing role selection to current binding
  identity; no change to archive lifecycle semantics.

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: corrected the callable contract after
  reviewer F2. `roles` is a required completion-edge role set; the unused `LANDABLE_ROLES`
  constant was removed instead of becoming a broad default. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): created for the new
  non-destructive completion classification. Verification metadata remains pinned until closeout stamps
  the HFX2-L11 commit.

