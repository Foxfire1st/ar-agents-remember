# mcp/src/agents_remember/serving/retire.py

| Field                  | Value                                        |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/retire.py`     |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-09T13:36:16+02:00                        |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`                                    |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire.py` is the shared explicit seat-retirement mechanics module (260707-HFX-L8, issue #12):
kill the tmux session, then persist the catalog's terminal mark + retirement provenance. It exists
so the manual retire paths (`session_retire` MCP tool, `POST /api/terminal/{session}/retire`) and
explicit landed archive cleanup (`POST /api/terminal/landed-cleanup`) share the same one-seat
"kill + mark" primitive. Normal successful completion no longer uses this module; HFX2-L11 moved
that edge to non-destructive landing in `landing.py`.

## Code Commentary

### Logic

`retire_entry(catalog, host, entry, *, at, by_session, reason, edge)` is the atomic single-seat
retire: calls `host.terminate(entry.id, tmux_name=entry.tmux_name)` (idempotent against an
already-gone tmux session — the terminate endpoint already relies on this same idempotence), then
`catalog.mark_retired(entry.id, at=at, by_session=by_session, reason=reason, edge=edge)`. Returns
the updated row, `None` if the catalog no longer has the id (a concurrent retire/terminate raced
this one), or the unchanged entry if it was already retired (`mark_retired`/`with_retirement` is
idempotent — see `terminal_catalog.py`).

The module intentionally has no leaf-scoped bulk-retire helper after HFX2-L11. Completion edges call
`land_seats_for_leaf` instead, and the landed cleanup endpoint performs its own per-session
server-side recheck before calling `retire_entry`.

### Conventions

`TerminalHost` is imported only under `TYPE_CHECKING` (a lazy/type-only import) to avoid a runtime
import cycle — callers pass a real `TerminalHost` instance at call time.

### Invariants And Boundaries

- Transcripts are never touched here — retiring is a catalog-and-tmux operation only; this module
  has no knowledge of transcript storage.
- Manual-path callers always call `check_retire_authority` before invoking `retire_entry` (see
  `mcp/tools/terminal.py`, `serving/app.py`). The landed cleanup endpoint has no acting seat; it
  limits itself by re-reading each requested catalog row and accepting only rows still
  `status:"landed"`.
- `retire_entry` itself does not catch exceptions from catalog I/O or `host.terminate`; callers own
  route-specific error handling and reporting.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
seat-retirement-specific behavior; this file is same-repository runtime plumbing implementing a
developer-ruled cleanup automation, not an external standard.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this retire mechanics shape; the leaf task doc's E2 example and this implementation are the source of truth. | L1-L70 | [retire.py](retire.py) |

## Repo-Internal References

`retire.py` is called from the manual MCP/serving retire paths (after policy approval) and from the
landed archive cleanup endpoint after that endpoint rechecks current catalog status.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `check_retire_authority` gates the manual path BEFORE `retire_entry` is ever called; `retire_entry` itself performs no authority check. | `check_retire_authority` | [retire_policy.py](retire_policy.py) |
| `mark_retired`/`with_retirement` are the catalog-side terminal mark this module writes; idempotence (a no-op on an already-`terminated` row) originates there, not in this file. | `TerminalCatalog.mark_retired`; `with_retirement` | [terminal_catalog.py](terminal_catalog.py) |
| `session_retire_payload` calls `retire_entry` after its own authority check, with `edge="manual"`. | `session_retire_payload` | [../../mcp/tools/terminal.py](../../mcp/tools/terminal.py) |
| `POST /api/terminal/{session}/retire` calls `retire_entry` identically to the MCP tool path after policy approval. | `api_terminal_retire` | [app.py](app.py) |
| `POST /api/terminal/landed-cleanup` rechecks each requested row and calls `retire_entry` only for rows still `status:"landed"`. | `api_terminal_landed_cleanup` | [app.py](app.py) |
| Normal successful completion calls `land_seats_for_leaf`, not retire mechanics. | `_auto_land_completed_seats` | [../../controllers/worktree_tools.py](../../controllers/worktree_tools.py) |
| `log_retire_event` is called by every caller of this module AFTER a successful retire, never from inside this module itself (retire mechanics and observer-event emission stay separate). | `log_retire_event` | [seat_events.py](seat_events.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local retire-mechanics module. | — | — |

## Update History

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: removed the production-dead
  `retire_seats_for_leaf` helper and documentation-only `RETIRABLE_ROLES` constant after completion
  edges switched to `landing.py`; this sidecar now documents only explicit per-session retire and
  landed archive cleanup use of `retire_entry`. Verification metadata pinned until closeout stamps
  the 260707-HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the
  shared retire mechanics — `retire_entry` (kill tmux + persist the terminal mark, idempotent),
  `retire_seats_for_leaf` (the automation-hook entry point, scoped by `leaf_key` + `roles`,
  `by_session=None`), `RETIRABLE_ROLES` (documentation-only role census). Shared by the manual
  MCP/serving retire paths (after `check_retire_authority` gates them) and the completion-edge
  automation (which bypasses that policy by design — see Invariants). Verification metadata pinned
  until closeout stamps the HFX-L8 commit.
