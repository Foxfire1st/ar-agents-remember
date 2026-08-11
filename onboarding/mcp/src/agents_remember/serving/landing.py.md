# mcp/src/agents_remember/serving/landing.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/landing.py`            |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated | 2026-08-11T10:20+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                           |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Marks all non-terminated occupants of selected roles on one canonical task document as landed while
leaving their hosted transcript/process inspectable.

## Code Commentary

### Logic

`land_seats_for_task` scans catalog rows, matches exact task-document identity and role, skips
terminated occupants, and delegates the landing transition for each match.

### Conventions

Callers supply the real task document resolved from governed closeout/finalization context.

### Invariants And Boundaries

- Landing is document-and-role scoped, never leaf-key parsed.
- Landed seats remain inspectable and are distinct from explicit retirement.
- Unrelated roles on the same document remain unchanged.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Landing matches canonical document and explicit role set. | `land_seats_for_task` | mcp/src/agents_remember/serving/landing.py:13-32 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `landing.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
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
