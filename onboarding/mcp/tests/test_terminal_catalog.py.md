# test_terminal_catalog.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_catalog.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T00:22+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_catalog.py` covers the JSON-backed durable terminal-session catalog introduced by task
22. It is pure filesystem/unit coverage for the store, separate from the FastAPI route tests in
`test_terminal_ws.py`.

## Code Commentary

### Logic

The `_entry` helper builds a running `TerminalCatalogEntry` with deterministic timestamps and tmux
name. `TerminalCatalogTests` creates a temp catalog path per case and verifies: `terminal_catalog_path`
places runtime state under `logs/dashboard/terminal-sessions.json`; `upsert` writes schema
`ar-dashboard-terminal-sessions/v1` and sorts rows by `createdAt`; exited rows remain visible while
terminated rows are filtered by default but still available with `include_terminated=True`; and
`mark_attached` restores a row to `running` with a refreshed `lastAttachedAt`. The regression case
`test_mark_exited_does_not_downgrade_terminated_session` covers the `End`/WebSocket teardown race:
explicit termination must keep `status="terminated"` and remain filtered even if later exit
bookkeeping runs.

### Conventions

Uses `unittest` and inserts `mcp/src` on `sys.path`, matching the surrounding MCP test suite.

### Invariants And Boundaries

No tmux, FastAPI, or WebSocket behavior is covered here. Those boundaries stay in `test_terminal.py`
and `test_terminal_ws.py`; this file pins only catalog JSON/storage semantics.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The catalog implementation under test. | L15-L30; L110-L185 | [serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py) |
| The FastAPI route tests that exercise catalog rows through open/list/rehydrate/terminate/image endpoints. | L325-L415; L571-L583 | [test_terminal_ws.py](test_terminal_ws.py) |

## Update History

- 2026-06-27T00:22+02:00 — Task 22 follow-up: added coverage that `mark_exited` cannot downgrade an
  explicitly terminated catalog row, matching the browser `End` behavior.
- 2026-06-26T23:05+02:00 — Created for task 22: covers catalog path, JSON schema/order, default
  terminated-row filtering, exited-row visibility, termination timestamps, and attach restoring running
  status. Verification metadata pinned until closeout stamps the task-22 code commit.
