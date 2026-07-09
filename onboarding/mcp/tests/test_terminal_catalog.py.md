# test_terminal_catalog.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_catalog.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T23:58:48+02:00 |
| lastVerifiedCommitHash | `c392985424896e9f392507295a23c4902d0c0696`       |
| lastVerifiedCommitDate | 2026-07-09T14:31:11+02:00|
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
Slice L5 adds `leaf_key` coverage: a row with a `leaf_key` round-trips through `to_json`/`from_json`,
an unset `leaf_key` is **omitted** from the serialized JSON, and a legacy row with no `leafKey` reads
back as `None` (migration-safe). L14 adds the same coverage for the `spawn_role` column
(`test_spawn_role_round_trips_and_is_omitted_when_unset`): a row with `spawn_role` serializes
`spawnRole` and reads back, an unset row omits the key and reads `None`. `with_leaf_key` is asserted to bind and to unbind (`None`). The L5 fix
pass makes uniqueness per **(leaf, role)**, so the `_entry` helper now takes a `kind` (a `harness` row is
chat-role, a `terminal` row is terminal-role) and the `active_for_leaf` coverage is role-aware:
`test_active_for_leaf_returns_running_owner` proves the **default role is `"chat"`** (resolving the harness
owner) and a differently-keyed leaf returns `None`; `test_active_for_leaf_is_scoped_by_role` seeds a chat
**and** a terminal on the same leaf and asserts `active_for_leaf(leaf, role="chat")` /
`role="terminal"` resolve each independently; and `test_active_for_leaf_ignores_exited_and_terminated`
proves an exited or terminated owner frees its leaf (the running-only, single-owner-per-role contract).
**HFX2-L11** adds `test_mark_landed_keeps_row_visible_and_non_active`: `mark_landed(id, at=, reason=,
edge=)` sets `status="landed"` + `landed_reason`, the row stays in `catalog.list()` (unlike terminated
rows, which are filtered by default), and `active_for_leaf` no longer resolves it as the live owner —
landing frees the leaf without hiding the row. `test_landed_state_round_trips_and_is_not_reanimated`
round-trips the full `landedAt`/`landedReason`/`landedEdge` provenance through the JSON file, then
proves `landed` is terminal-forward: `mark_attached`, `record_liveness_probe(alive=True)`, and
`mark_exited` are each called on a landed row and each returns the row still `status="landed"` —
none of the ordinary running/exited transition helpers can reanimate or downgrade a landed row.

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

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): added 46 lines of coverage for the new
  `status:"landed"` state — `mark_landed`/`with_landing` provenance round-trip, and confirms landed
  is preserved (never reverted) across `with_attachment`, `with_liveness_success`, and `mark_exited`
  (the terminal-forward guarantee the reviewer's D-3 probe and delta-verify both confirmed). Verification
  metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-06T23:58:48+02:00 — 260703-L14 (visual hierarchy + chat grouping): added
  `test_spawn_role_round_trips_and_is_omitted_when_unset` — the `spawn_role` column serializes as
  `spawnRole` when set, is omitted when unset, and reads back migration-safe (mirrors the L5
  `leaf_key` cases). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-03T12:50+02:00 — No content impact: L15 hoisted a function-local `import threading` to module top for the PLC0415 gate; no test logic change.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: `active_for_leaf` coverage is now role-aware — `_entry` takes a `kind`
  (harness ⇒ chat, terminal), `test_active_for_leaf_returns_running_owner` pins the default `"chat"` role,
  and `test_active_for_leaf_is_scoped_by_role` seeds a chat + a terminal on one leaf and asserts each role
  resolves independently. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added `leaf_key` coverage — round-trip + omit-when-unset + legacy
  row→`None` (migration-safe), `with_leaf_key` bind/unbind, and `active_for_leaf` returning the single
  running owner (not exited/terminated/other-keyed rows). Verification metadata pinned until closeout
  stamps the L5 commit.
- 2026-06-27T00:22+02:00 — Task 22 follow-up: added coverage that `mark_exited` cannot downgrade an
  explicitly terminated catalog row, matching the browser `End` behavior.
- 2026-06-26T23:05+02:00 — Created for task 22: covers catalog path, JSON schema/order, default
  terminated-row filtering, exited-row visibility, termination timestamps, and attach restoring running
  status. Verification metadata pinned until closeout stamps the task-22 code commit.
