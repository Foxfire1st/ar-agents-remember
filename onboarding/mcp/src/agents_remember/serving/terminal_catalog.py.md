# mcp/src/agents_remember/serving/terminal_catalog.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_catalog.py`   |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-09T19:31+02:00 |
| lastVerifiedCommitHash | `dbe750e4cd7fb777b8f39e7ba6279d1080502d8e`              |
| lastVerifiedCommitDate | 2026-07-09T19:42:39+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal_catalog.py` is the durable JSON catalog for dashboard-owned terminal and harness sessions.
It records enough metadata to show sessions after a browser/dashboard restart and to reattach a
still-live tmux session without asking the browser to remember process-local state.

## Code Commentary

### 260707-HFX2-L12 CS-6 Update

`TerminalCatalog.batch()` is a read-once/write-once unit of work for full-catalog sweeps, and `compact()` reclaims aged `terminated` tombstones while preserving running, exited, and landed/archive rows. Landed row cleanup remains the explicit L11 manual path.

### Logic

`TerminalCatalogEntry` is the immutable row model. It stores the browser-visible session id and label,
the launch kind (`terminal` or `harness`), optional harness id and lifecycle id, cwd, tmux session
name, fixed command argv, creation and last-attach timestamps, status (`running`, `exited`,
`landed`, or `terminated`), optional termination timestamp, and (slice L5) an optional `leaf_key` — the durable
leaf-identity key (qualified leaf id `repo/master/leaf-id`) the catalog uses as the **leaf→chat
registry** key; it is opaque to the backend. Since **L2** the row also carries **spawned-by
provenance** — `spawned_by_session` + `spawned_by_lifecycle`, set when the row was created by the
`spawn_agent_session` tool (an orchestrator spawning a manager, a manager spawning a worker), and since
**L14** a `spawn_role` column — the l-01 role this session was spawned AS (the `AR_SPAWN_ROLE` value the
dispatching seat seeded into the spawn env), recorded so the Chats command tree can group command chats
(orchestrator/strategist/manager) by role provenance without re-reading tmux env. Since **L16** five
more optional spawn-provenance columns follow the same pattern: the free-form escape hatch —
`launch_args` (`launchArgs`, the verbatim argv passthrough that rode the launch), `prompt_keywords`
(`promptKeywords`, prepended to the brief paste), `session_commands` (`sessionCommands`, the
post-launch pastes, resolved list incl. a session-vehicle effort) — plus the resolved dispatch level
`spawn_level` (`spawnLevel`, leaf|master|portfolio) and `spawn_level_source` (`spawnLevelSource`,
explicit|default), the rolesPerLevel knob-resolution provenance. Since **260707-HFX-L5** the row
also carries **liveness probe state**: `liveness_failures` (consecutive failed probes,
`_non_negative_int` on read), `liveness_first_failed_at` / `liveness_last_failed_at` (ISO
timestamps), `liveness_evidence` and `exit_evidence`
(`TerminalLivenessEvidence = "tmux-command-failed" | "pane-gone"`, validated by
`_liveness_evidence` on read). Persisting the failure state means a daemon restart cannot erase
hysteresis progress; JSON keys are `livenessFailures` / `livenessFirstFailedAt` /
`livenessLastFailedAt` / `livenessEvidence` written only when set, and `exitEvidence` written only
when the row is actually `exited` — all migration-safe like the other optional columns.
`from_json`/`to_json` translate between Python
snake_case and the dashboard API's camelCase fields (`_string_tuple` reads the free-form lists back,
`None` for absent/legacy rows). `to_json` writes `leafKey` / `spawnedBySession` /
`spawnedByLifecycle` / `spawnRole` / the five L16 keys **only when set** (like `harness` / `lifecycleId` / `terminatedAt`), so legacy rows
with no such key read back as `None` — no schema bump, migration-safe, the SAME pattern for all optional
columns; the dashboard groups the Chats sidebar by `spawnRole` (L14) and reads the spawned-by pair to
render the spawner → spawned edges once that surface lands. `with_attachment` restores a normal row to
`running`, but preserves a row already classified as `landed`; it refreshes `lastAttachedAt`, clears
`terminatedAt`, and (HFX-L5) resets all liveness state — a fresh attach is direct evidence of life
without reopening archived successful seats. `with_status` changes status and records
`terminatedAt` only for explicit termination.

The **liveness transition copiers** (260707-HFX-L5) own the hysteresis math.
`with_liveness_success()` clears all failure state and restores a non-`terminated` `exited` row to
`running` — the **self-heal**: a false exit mark recovers automatically when a later probe finds
the tmux session alive; a `landed` row stays `landed` and a `terminated` row is never revived
(explicit `End` stays terminal).
`with_liveness_failure(evidence=…, checked_at=…, failure_threshold, minimum_failure_window_seconds,
pane_gone_failure_threshold)` records one failed probe on a `running` row (non-running rows are
untouched): it increments `liveness_failures`, pins `liveness_first_failed_at` on the first
failure, and marks `exited` only when `failures >= threshold` AND
`_elapsed_seconds(first_failed_at, checked_at) >= minimum_window`. The threshold/window pair is
**evidence-dependent**: `pane-gone` (a definitive missing-session probe) uses
`pane_gone_failure_threshold` with a zero window so it marks fast, while `tmux-command-failed`
(transient — a subprocess error, timeout, or non-missing-session nonzero exit) needs the full
`failure_threshold` across at least the minimum window, so a transient command-failure storm never
mass-exits a live fleet. On marking, the producing evidence is stamped into `exit_evidence`.
`TerminalCatalog.record_liveness_probe(session_id, *, alive, checked_at, evidence=None,
failure_threshold=3, minimum_failure_window_seconds=5.0, pane_gone_failure_threshold=1)` is the
store-level write point: under the catalog lock it reads, applies `with_liveness_success` (alive)
or `with_liveness_failure` (dead with evidence; a dead probe with `evidence=None` is a no-op), and
writes only when the row actually changed; an unknown id returns `None`. Callers are the
`terminal_liveness.py` sweeper + shared observation path. **L2** rewrote all three copiers
(`with_attachment` / `with_status` / `with_leaf_key`) to use `dataclasses.replace(self, …)` instead of
field-by-field reconstruction, so a newly added column (like the spawned-by pair) is preserved through a
re-attach/status change **by construction** rather than silently dropped. `with_leaf_key(leaf_key)` is
the leaf-attach write point: a copy bound to `leaf_key`, or unbound when `None`.

The **leaf-uniqueness role** (L5 fix 2) splits one slot into two: `TerminalSessionRole = "chat" |
"terminal"`, `role_for_kind(kind)` maps a shell (`kind == "terminal"`) to `"terminal"` and any harness to
`"chat"`, and the `entry.role` property derives a row's role from its kind. Uniqueness is per **(leaf,
role)** — a leaf may hold at most one running chat AND one running terminal, so an agent chat and a scratch
terminal can share a leaf without colliding. `active_for_leaf(leaf_key, *, role="chat")` is the
role-scoped registry lookup the opener + `attach-leaf` routes call before an upsert: the first `list()`
row whose `leaf_key == leaf_key and status == "running" and role == role`, else `None` (the default
`"chat"` is the agent slot). Because `active_for_leaf` gates on `running`, an exited/landed/terminated
session frees its leaf for that role (a stale `running` row is
downgraded to `exited` by the `terminal_liveness.py` sweeper / direct liveness observations once
the hysteresis evidence threshold is met — never by a single transient tmux command failure),
giving server-authoritative single-owner-per-role uniqueness.

**Seat lifecycle (260707-HFX-L8/HFX2-L11)** adds optional column groups, all written-only-when-set
via the same `to_json`/`from_json` migration-safe pattern: **retirement provenance**
(`retired_at`/`retired_by_session`/`retired_reason`/`retired_edge`, JSON `retiredAt`/
`retiredBySession`/`retiredReason`/`retiredEdge`) layered onto `status == "terminated"` for manual
retire/cleanup; **landing provenance** (`landed_at`/`landed_reason`/`landed_edge`, JSON `landedAt`/
`landedReason`/`landedEdge`) layered onto the visible `status == "landed"` archive state for normal
successful completion; **live identity** (`spawned_label`, JSON `spawnedLabel`) frozen on the FIRST
rename only; and **live turn-state** (`turn_state: SeatTurnState = "working"|"turn-ended"|
"awaiting-input"|"stale"`, `turn_state_changed_at`, JSON `turnState`/`turnStateChangedAt`,
`_turn_state` validates the literal on read). Three new copiers follow the `dataclasses.replace`
pattern: `with_retirement(at, by_session, reason, edge)` is a no-op returning `self` unchanged when
`status` is already `"terminated"` (idempotent — a retire of an already-terminated row never
re-stamps provenance), otherwise sets `status="terminated"` + `terminated_at=at` + the four retire
fields in one write; `with_label(label)` sets `label` and freezes `spawned_label = spawned_label or
label` — the ORIGINAL label survives every later rename; `with_turn_state(state, changed_at)` is a
no-op returning `self` when `state` already equals `turn_state` (so callers can detect an actual
transition by identity comparison, not by chasing a separate "changed" flag on the entry itself).
`TerminalCatalog` gained matching locked store write points: `mark_retired(session_id, at,
by_session, reason, edge)`, `mark_landed(session_id, at, reason, edge)`, `set_label(session_id,
label)`, `record_turn_state(session_id, state, changed_at)` — same shape as
`record_liveness_probe`: read under lock, apply the copier, write only when the row actually changed,
unknown id returns `None`. Manual retirement rides `status == "terminated"` and successful completion
rides `status == "landed"`; both compose with liveness because neither path is revived by
`with_liveness_success`.

`terminal_catalog_path(coordination_root)` places the runtime file under
`logs/dashboard/terminal-sessions.json`. `TerminalCatalog` is a small JSON store over that file:
`list(include_terminated=False)` filters terminated rows by default while keeping exited and landed
rows visible,
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
  effects through `TerminalHost`; `record_liveness_probe` only *persists* probe outcomes handed to it
  by `terminal_liveness.py`.
- Liveness self-heal revives any non-`landed`/non-`terminated` `exited` row on an alive probe (broader than a
  probe-caused exit alone — the WebSocket-close exit path's marks are also revivable when tmux still
  holds the session, which is semantically correct); `landed` and `terminated` are never revived. Known narrow
  race (HFX-L5 review F2): a false exit + a fast same-(leaf, role) respawn inside one sweep interval
  could revive into a momentary two-running-rows state for that slot.
- Terminated rows stay available only when explicitly requested with `include_terminated=True`; exited
  and landed rows remain listed so the UI can show an honest ended/archive state.
- Explicit termination is terminal for catalog visibility: later exit bookkeeping must preserve the
  `terminated` status and `terminatedAt` timestamp.
- The command is stored as a tuple/list of fixed argv parts, not a shell string.
- `leaf_key` is opaque (the catalog never parses it) and optional — omitted from JSON when unset so the
  schema stays back-compatible. The catalog only *reports* the single running owner **of a given role** via
  `active_for_leaf(leaf_key, role=…)`; the `409 leaf-taken` decision + the claim-then-write atomicity live
  in `serving.app`.
- Uniqueness is per **(leaf, role)**, not per leaf: a chat (any harness) and a terminal (a shell) are
  distinct slots and never conflict with each other on the same leaf; `role` is always derived from kind
  (`role_for_kind` / `entry.role`), never stored separately.
- Manual retirement is a TERMINAL mark: `with_retirement` sets `status="terminated"`, so a retired
  row is filtered out of `list()` exactly like any other terminated row and can never be resurrected by
  `with_liveness_success`. Normal successful completion is separate and non-destructive:
  `with_landing` sets `status="landed"` plus landing provenance, keeps the row listed for dashboard
  inspection, and releases the leaf slot because active lookup is running-only.
- Rename (`with_label`) touches only `label`/`spawned_label` — it must never touch `spawn_role` (the
  L6 role-seat-immutability field); a seat's role is fixed at spawn for its lifetime.
- Turn-state is classified for `kind == "harness"` rows only (see `terminal_liveness.py`); plain
  `terminal` (shell) rows never carry a meaningful `turn_state`.

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
| The liveness sweeper + shared observation path that drive `record_liveness_probe` (HFX-L5) and own the default hysteresis constants. | `TerminalCatalogLivenessSweeper`; `observe_terminal_liveness` | [terminal_liveness.py](terminal_liveness.py) |
| Regression tests for hysteresis, pane-gone fast-marking, self-heal, sweep rate-limit/overlap, and stderr classification. | `TerminalCatalogLivenessTests` | [../../../tests/test_terminal_liveness.py](../../../tests/test_terminal_liveness.py) |
| `mark_retired`/`mark_landed`/`set_label`/`record_turn_state` are called from the manual retire/rename tools and endpoints, the landed cleanup endpoint, and the integrate/finalize auto-land hooks. | `retire_entry`; `TerminalCatalog.mark_landed`; `TerminalCatalog.set_label`; `record_turn_state` | [retire.py](retire.py); [landing.py](landing.py); [terminal.py (mcp/tools)](../../mcp/tools/terminal.py); [worktree_tools.py](../../controllers/worktree_tools.py); [app.py](app.py) |
| The retire authority policy (`check_retire_authority`) is evaluated against `SeatRef`s built from this catalog's `spawn_role`/`leaf_key` fields before any `mark_retired` call. | `SeatRef`; `master_of` | [retire_policy.py](retire_policy.py) |
| Failing-first + regression tests for the retire/rename/turn-state mechanics, the retire-vs-liveness interplay, and idempotent provenance. | `test_seat_lifecycle.py` | [../../../tests/test_seat_lifecycle.py](../../../tests/test_seat_lifecycle.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local dashboard catalog. | — | — |

## Update History

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): added `landed` as a visible
  non-live `TerminalSessionStatus`, landing provenance (`landed_at`/`landed_reason`/`landed_edge`),
  `with_landing`, and `TerminalCatalog.mark_landed`. Attach/liveness/exit transitions now preserve
  landed rows instead of reanimating them, while manual retire remains a terminating action. Landed
  rows stay in `list()` for dashboard inspection and release leaf ownership because active lookup is
  running-only. Verification metadata remains pinned until closeout stamps the HFX2-L11 commit.

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state):
  three new optional column groups (retirement provenance `retired_at`/`retired_by_session`/
  `retired_reason`/`retired_edge`; live identity `spawned_label`; live turn-state
  `turn_state: SeatTurnState`/`turn_state_changed_at`), all written-only-when-set, migration-safe.
  New copiers `with_retirement` (idempotent -- a no-op on an already-terminated row), `with_label`
  (freezes `spawned_label` on first rename only, never touches `spawn_role`), `with_turn_state`
  (no-op when the state did not transition). New `TerminalCatalog` write points `mark_retired`/
  `set_label`/`record_turn_state`. Retirement rides the EXISTING `status == "terminated"` terminal
  state rather than a fourth status value, so it composes for free with the L5 liveness hysteresis
  (never resurrected) and the "never a zombie row" `list()` filter. Verification metadata pinned
  until closeout stamps the HFX-L8 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L5 (catalog liveness hysteresis): `TerminalCatalogEntry`
  gained persisted liveness state — `liveness_failures` / `liveness_first_failed_at` /
  `liveness_last_failed_at` / `liveness_evidence` / `exit_evidence`
  (`TerminalLivenessEvidence = "tmux-command-failed"|"pane-gone"`; JSON camelCase keys written
  only when set, `exitEvidence` only on an exited row — migration-safe) — plus the transition
  copiers `with_liveness_success` (clear failures; self-heal a non-terminated exited row back to
  `running`; never revive `terminated`) and `with_liveness_failure` (increment + pin
  first-failure; exit only at evidence-dependent threshold AND minimum window — pane-gone marks
  fast, command failures need 3 across ≥5s by default), and the locked store write point
  `TerminalCatalog.record_liveness_probe(...)` (writes only on actual change; unknown id ⇒
  `None`). `with_attachment` now also resets liveness state. The `active_for_leaf` docstring was
  refreshed to cite the liveness sweeper (L5R2 — `_refresh_catalog_entries` is deleted).
  Verification metadata pinned until closeout stamps the HFX-L5 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): five optional spawn-provenance
  columns — `launch_args`/`prompt_keywords`/`session_commands` (the free-form escape hatch, recorded
  VERBATIM, never validated) and `spawn_level`/`spawn_level_source` (the resolved dispatch level +
  whether the dispatcher supplied it) — written only when set (JSON `launchArgs`/`promptKeywords`/
  `sessionCommands`/`spawnLevel`/`spawnLevelSource`), read back via the `_string_tuple` helper,
  preserved through re-attach/status changes by the `replace`-based copiers by construction.
  Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:58:12+02:00 — 260703-L14 (visual hierarchy + chat grouping): `TerminalCatalogEntry`
  gained an optional `spawn_role` column (JSON `spawnRole`, written only when set — the same
  migration-safe pattern as `leaf_key`): the `AR_SPAWN_ROLE` recorded at spawn, the Chats
  command-tree grouping key. The `replace`-based copiers preserve it by construction.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T11:10+02:00 — L2 (agent-orchestration provenance): `TerminalCatalogEntry` gained optional
  `spawned_by_session` + `spawned_by_lifecycle` columns (the spawning session/lifecycle when the
  `spawn_agent_session` tool created the row) — `to_json`/`from_json` handle them migration-safe (written
  only when set), and `with_attachment`/`with_status`/`with_leaf_key` were rewritten to
  `dataclasses.replace(self, …)` so the new columns (and any future one) survive a re-attach/status change
  by construction. The dashboard reads the pair for the orchestration tree. Verification metadata pinned
  until closeout stamps the L2 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: leaf uniqueness is now per **(leaf, role)**. Added `TerminalSessionRole`
  (`chat`|`terminal`), `role_for_kind(kind)` (a shell ⇒ terminal, a harness ⇒ chat), and the `entry.role`
  property; `active_for_leaf` gained a `role` kwarg (default `"chat"`) so it probes the chat slot and the
  terminal slot independently — a leaf may hold one running chat AND one running terminal without conflict.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): `TerminalCatalogEntry` gained an optional `leaf_key` (the leaf→chat
  registry key) — `to_json` writes `leafKey` only when set (migration-safe), `with_attachment`/`with_status`
  thread it through, and a `with_leaf_key` copier is the attach write point. Added `TerminalCatalog.active_for_leaf(leaf_key)`,
  the running-only single-owner lookup the opener + attach-leaf routes probe for uniqueness. Verification
  metadata pinned until closeout stamps the L5 commit.
- 2026-06-27T00:22+02:00 — Task 22 follow-up: documented that `mark_exited` preserves an already
  terminated row so a WebSocket teardown after `End` cannot make the hidden row visible again as
  `exited`.
- 2026-06-26T23:05+02:00 — Created for task 22 dashboard chat-session durability: records
  dashboard-owned terminal/harness rows under `logs/dashboard/terminal-sessions.json`, preserves exited
  rows, filters terminated rows by default, and provides attach/exited/terminated transitions for the
  serving layer. Verification metadata pinned until closeout stamps the task-22 code commit.
