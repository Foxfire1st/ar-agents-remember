# test_terminal_catalog.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_catalog.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T18:30+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_catalog.py` covers the JSON-backed durable terminal-session catalog introduced by task
22. It is pure filesystem/unit coverage for the store, separate from the FastAPI route tests in
`test_terminal_ws.py`.

## Code Commentary

### 260713-PHA-L1 control metadata coverage

The optional projection suite now round-trips `controlState`, `controlEndpoint`, and
`controlProtocol` for harness rows, while legacy rows omit/read these fields as `None`. The test
keeps the catalog migration-safe and proves the bridge metadata is additive rather than a schema
replacement.

### 260707-HFX2-L18 Complete Optional Projection Proof

`test_complete_optional_projection_round_trips_without_contract_loss` constructs an exited harness
entry with every optional provenance, dispatch, session-log, liveness, retirement, landing, label,
turn-state, tuple, and path field populated. It asserts `from_json(to_json(entry)) == entry` and
spot-checks required `seatRole`, tuple-to-list conversion, path-to-string conversion, and
exited-only evidence. Existing tests continue to prove omitted/legacy fields read as `None`, so the
new case covers the complementary all-present direction without weakening migration semantics.
Remaining changes in this test file are Ruff formatting only.

### 260707-HFX2-L17 Catalog Pair And Migration Proof

Catalog tests cover `seatRole` serialization, legacy migration from spawn provenance or chat,
terminal preservation, in-place rewrite with stable ids/order/row count, binding-first lookup, and
different-role coexistence under same-role exclusivity.

### Logic

**260707-HFX2-L15 coverage.** Optional replacement-leaf, resolved-knob, and session-log fields
round-trip through catalog JSON. `bind_session_log` is regression-tested against a stale open-time
snapshot so newer exited/failure/pane evidence survives the targeted binding update.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog implementation under test, including typed optional reads and required/optional JSON projection. | "def from_json(cls" | mcp/src/agents_remember/models/terminal_catalog.py:80-510 |
| The FastAPI route tests that exercise catalog rows through open/list/rehydrate/terminate/image endpoints. | `test_get_terminal_sessions_lists_catalog_entries`; `test_post_open_spawns_shell_at_workspace_root`; `test_terminate_marks_catalog_and_kills_tmux`; `test_saves_under_session_cwd_and_returns_path` | mcp/tests/test_terminal_ws_misc.py:43-54; mcp/tests/test_terminal_ws_websocket_1.py:84-111; mcp/tests/test_terminal_ws_websocket_1.py:113-132; mcp/tests/test_terminal_ws_websocket_1.py:203-212 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 2 citation claims; scoped result 0 findings.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: documented additive control metadata
  round-trip and legacy omission coverage.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T18:30+02:00 — 260707-HFX2-L18: added one complete optional-field projection and
  round-trip regression covering role/provenance, tuples, paths, liveness, retirement/landing,
  labels, and turn state. Existing omission/legacy cases remain the complementary absent-field
  proof; other diffs are formatting only. Verification metadata remains pinned until closeout
  stamps the eventual L18 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added durable seat-role migration and pair-lookup
  regressions, including stable in-place catalog rewrite.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added dispatch-provenance round-trip and lock-safe
  log-binding race coverage. Verification metadata remains pinned until closeout stamps the eventual
  L15 code commit.

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
