# mcp/src/agents_remember/serving/retire.py

| Field                  | Value                                        |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/retire.py`     |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-08T02:43+02:00                          |
| lastVerifiedCommitHash | `2322ffc15ef803ea29bf900beeae84de19b43019`      |
| lastVerifiedCommitDate | 2026-07-08T03:14:39+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire.py` is the shared seat-retirement mechanics module (260707-HFX-L8, issue #12): kill the
tmux session, then persist the catalog's terminal mark + retirement provenance. It exists so the
MANUAL retire path (`session_retire` MCP tool, `POST /api/terminal/{session}/retire`) and the
AUTOMATED completion-edge hooks (`worktree_integrate`, `lifecycle_finalize_task`) retire seats
identically — one code path for "kill + mark", not two that could drift.

## Code Commentary

### Logic

`RETIRABLE_ROLES = frozenset({"worker", "reviewer", "manager", "designer", "strategist"})`
documents every `l-01` role that can occupy a retirable seat (the orchestrator is portfolio-level
and is never a retire TARGET through the automation hooks). It is currently unused by any function
signature in this module — callers pass their own `roles` frozenset per completion edge
(`{"worker", "reviewer"}` at leaf-integration, `{"manager", "reviewer"}` at master-finalization) —
so this constant documents intent for future automation-hook role sets without hardcoding one set
into `retire_seats_for_leaf`.

`retire_entry(catalog, host, entry, *, at, by_session, reason, edge)` is the atomic single-seat
retire: calls `host.terminate(entry.id, tmux_name=entry.tmux_name)` (idempotent against an
already-gone tmux session — the terminate endpoint already relies on this same idempotence), then
`catalog.mark_retired(entry.id, at=at, by_session=by_session, reason=reason, edge=edge)`. Returns
the updated row, `None` if the catalog no longer has the id (a concurrent retire/terminate raced
this one), or the unchanged entry if it was already retired (`mark_retired`/`with_retirement` is
idempotent — see `terminal_catalog.py`).

`retire_seats_for_leaf(catalog, host, *, leaf_key, roles, reason, edge, at)` is the automation-hook
entry point: iterates `catalog.list(include_terminated=True)`, retiring every candidate whose
`leaf_key` matches AND whose `status != "terminated"` AND whose `spawn_role` is in `roles`, calling
`retire_entry` for each with `by_session=None` (the completion-edge automation has no acting
session — the provenance `reason`/`edge` names the automated edge instead of an actor id). Returns
the list of actually-retired rows.

### Conventions

`TerminalHost` is imported only under `TYPE_CHECKING` (a lazy/type-only import) to avoid a runtime
import cycle — callers pass a real `TerminalHost` instance at call time.

### Invariants And Boundaries

- Transcripts are never touched here — retiring is a catalog-and-tmux operation only; this module
  has no knowledge of transcript storage.
- `retire_seats_for_leaf` deliberately bypasses `retire_policy.check_retire_authority`: an automated
  completion edge (`worktree_integrate`/`lifecycle_finalize_task`) is not an actor SEAT with its own
  `SeatRef`, so the manager/orchestrator authority split does not apply to it — the automation is
  itself the trusted caller, scoped only by the `leaf_key` + `roles` filter its own caller supplies.
  Contrast with `retire_entry`'s manual-path callers, which always call `check_retire_authority`
  BEFORE invoking `retire_entry` (see `mcp/tools/terminal.py`, `serving/app.py`).
- `retire_entry`/`retire_seats_for_leaf` themselves do not catch exceptions from catalog I/O or
  `host.terminate` — the best-effort/never-blocks-the-edge guarantee for the automation path is the
  CALLER's responsibility (`controllers/worktree_tools.py::_auto_retire_completed_seats` wraps the
  whole call in `try/except Exception: return []`, per the F1 doctrine-review fix — this module
  itself raises normally on I/O failure).

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

`retire.py` is called from the manual MCP/serving retire paths (after policy approval) and from
the completion-edge automation hooks (with no policy check, scoped by the caller's own filter).

| Finding | Citations | Source Path |
| --- | --- | --- |
| `check_retire_authority` gates the manual path BEFORE `retire_entry` is ever called; `retire_entry` itself performs no authority check. | `check_retire_authority` | [retire_policy.py](retire_policy.py) |
| `mark_retired`/`with_retirement` are the catalog-side terminal mark this module writes; idempotence (a no-op on an already-`terminated` row) originates there, not in this file. | `TerminalCatalog.mark_retired`; `with_retirement` | [terminal_catalog.py](terminal_catalog.py) |
| `session_retire_payload` calls `retire_entry` after its own authority check, with `edge="manual"`. | `session_retire_payload` | [../../mcp/tools/terminal.py](../../mcp/tools/terminal.py) |
| `POST /api/terminal/{session}/retire` calls `retire_entry` identically to the MCP tool path. | `api_terminal_retire` | [app.py](app.py) |
| `_auto_retire_completed_seats` calls `retire_seats_for_leaf` inside a broad `try/except Exception` (F1 doctrine-review fix) so a catalog-I/O failure in this module's retire body can never fail an already-succeeded `worktree_integrate`/`lifecycle_finalize_task` call. | `_auto_retire_completed_seats` | [../../controllers/worktree_tools.py](../../controllers/worktree_tools.py) |
| `log_retire_event` is called by every caller of this module AFTER a successful retire, never from inside this module itself (retire mechanics and observer-event emission stay separate). | `log_retire_event` | [seat_events.py](seat_events.py) |
| Failing-first tests for `retire_seats_for_leaf`'s role/leaf-key scoping, already-terminated skip, and the F1 exception-guard-widening regression via the automation-hook wiring. | `RetireSeatsForLeafTests`; `AutoRetireHookIntegrationTests` | [../../../tests/test_seat_lifecycle.py](../../../tests/test_seat_lifecycle.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local retire-mechanics module. | — | — |

## Update History

- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the
  shared retire mechanics — `retire_entry` (kill tmux + persist the terminal mark, idempotent),
  `retire_seats_for_leaf` (the automation-hook entry point, scoped by `leaf_key` + `roles`,
  `by_session=None`), `RETIRABLE_ROLES` (documentation-only role census). Shared by the manual
  MCP/serving retire paths (after `check_retire_authority` gates them) and the completion-edge
  automation (which bypasses that policy by design — see Invariants). Verification metadata pinned
  until closeout stamps the HFX-L8 commit.
