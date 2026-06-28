# mcp/src/agents_remember/serving/terminal_catalog.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_catalog.py`   |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-06-27T00:22+02:00                                  |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`              |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal_catalog.py` is the durable JSON catalog for dashboard-owned terminal and harness sessions.
It records enough metadata to show sessions after a browser/dashboard restart and to reattach a
still-live tmux session without asking the browser to remember process-local state.

## Code Commentary

### Logic

`TerminalCatalogEntry` is the immutable row model. It stores the browser-visible session id and label,
the launch kind (`terminal` or `harness`), optional harness id and lifecycle id, cwd, tmux session
name, fixed command argv, creation and last-attach timestamps, status (`running`, `exited`, or
`terminated`), and optional termination timestamp. `from_json`/`to_json` translate between Python
snake_case and the dashboard API's camelCase fields. `with_attachment` restores a row to `running`,
refreshes `lastAttachedAt`, and clears `terminatedAt`; `with_status` changes status and records
`terminatedAt` only for explicit termination.

`terminal_catalog_path(coordination_root)` places the runtime file under
`logs/dashboard/terminal-sessions.json`. `TerminalCatalog` is a small JSON store over that file:
`list(include_terminated=False)` filters terminated rows by default while keeping exited rows visible,
`get` finds one row, `upsert` replaces by id, and the `mark_*` helpers persist status transitions.
`mark_exited` deliberately leaves an already terminated row untouched so the passive WebSocket/PTY exit
path cannot downgrade an explicit `End` action back to an `exited` row that would rehydrate in the UI.
`_read` accepts a missing file as an empty catalog and validates the top-level shape. `_write` creates
parent directories, serializes sorted rows under schema `ar-dashboard-terminal-sessions/v1`, writes a
sibling temp file, then atomically replaces the catalog.

### Conventions

The catalog is JSON-primary and API-shaped: persisted keys use the same camelCase names returned by
`GET /api/terminal/sessions`. Rows are sorted by `createdAt` to keep diffs stable.

### Invariants And Boundaries

- The catalog does not probe tmux and does not spawn or kill sessions. `serving.app` coordinates those
  effects through `TerminalHost`.
- Terminated rows stay available only when explicitly requested with `include_terminated=True`; exited
  rows remain listed so the UI can show an honest ended state.
- Explicit termination is terminal for catalog visibility: later exit bookkeeping must preserve the
  `terminated` status and `terminatedAt` timestamp.
- The command is stored as a tuple/list of fixed argv parts, not a shell string.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation (`docs/design/`)
for terminal-catalog-specific behavior; this file is same-repository runtime plumbing.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this catalog shape; the implementation is the source of truth. | L15-L30; L110-L185 | [terminal_catalog.py](terminal_catalog.py) |

## Repo-Internal References

`serving.app` is the catalog's only runtime orchestrator, and `terminal.py` supplies the tmux probe/kill
operations that keep catalog state honest.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The FastAPI app injects/creates the catalog, refreshes stale rows, rehydrates WebSockets from catalog metadata, persists opener rows, marks terminations, and uses catalog cwd for image uploads. | L334-L351; L291-L331; L481-L515; L528-L638 | [app.py](app.py) |
| The terminal host exposes the tmux probe and terminate hooks that app.py uses before rehydrate and during explicit termination. | L86-L121; L230-L239; L287-L289; L340-L347 | [terminal.py](terminal.py) |
| Unit tests pin catalog path, JSON schema/order, status filtering, attach/status transitions, and termination winning over later exit bookkeeping. | L46-L95 | [../../../tests/test_terminal_catalog.py](../../../tests/test_terminal_catalog.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local dashboard catalog. | — | — |

## Update History

- 2026-06-27T00:22+02:00 — Task 22 follow-up: documented that `mark_exited` preserves an already
  terminated row so a WebSocket teardown after `End` cannot make the hidden row visible again as
  `exited`.
- 2026-06-26T23:05+02:00 — Created for task 22 dashboard chat-session durability: records
  dashboard-owned terminal/harness rows under `logs/dashboard/terminal-sessions.json`, preserves exited
  rows, filters terminated rows by default, and provides attach/exited/terminated transitions for the
  serving layer. Verification metadata pinned until closeout stamps the task-22 code commit.
