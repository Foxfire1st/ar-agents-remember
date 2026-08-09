# mcp/src/agents_remember/serving/agent_notifier_heartbeat.py

| Field                  | Value                                                     |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/serving/agent_notifier_heartbeat.py` |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-08T21:20+02:00                                        |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`                    |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`agent_notifier_heartbeat.py` is the agent-notifier sweep's own self-liveness primitive
(260707-HFX2-L2, R5): issue #15's "the watcher must be code AND watched". The agent-notifier sweeps other seats for
liveness/deadline drift, but the sweep itself is just another process that can silently stop — so
it writes its own heartbeat tick row on every completed sweep, durable across a daemon restart (a
timer alone would go blind on restart; a row does not). Two independent readers consume the tick
age: an MCP tool call opportunistically attaches a fail-loud banner when it goes stale
(`mcp/tools/base.py`), and the dashboard header renders it directly, mirroring how `servingBuild`
already surfaces the boot stamp.

## Code Commentary

### 260713-TES-L1 Rename — Identifiers and Wire Key

Module renamed from `supervisor_heartbeat.py`; all identifiers now use `AgentNotifier*`
(`AgentNotifierHeartbeat` durable row, `AgentNotifierHeartbeatPayload` read-side model,
`AgentNotifierHeartbeatStore`, `agent_notifier_staleness_banner`). The on-disk artifact name
`supervisor-heartbeat.json` is RETAINED during the compatibility window (renaming it would orphan
pre-window rows and change "stale" behavior); `agent_notifier_heartbeat_path()` returns the
retained path. The wire key is now `agentNotifierHeartbeat`, with the legacy `supervisorHeartbeat`
key emitted alongside the same payload by `serving/served_state.py::served_state_tail` during the
window. Removal rides the heartbeat-schema migration.

### 260731-EFA-L4 Current Delta — The Read-Side Payload Is Now A Declared Model

This module now owns **two** shapes, not one, and the distinction is the point:

- cit:(["class AgentNotifierHeartbeat:", "def tick(", "def read("], mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:23-28; mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:73-108; mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:110-127) is the durable **row** — what `tick()` writes and `read()`
  parses.
- cit:([`AgentNotifierHeartbeatPayload`, `heartbeat_age_seconds`], mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:31-55; mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:128-139) is what a reader computes **about** that row at
  response time: the row's own counters plus `ageSeconds` and the `stale` verdict against the
  configured cutoff. Serving-layer arithmetic on a tick-time artifact, which is exactly why it
  is not a projection field.

`app._agent_notifier_heartbeat_payload` used to build that answer as a bare `dict[str, Any]` and
write it straight into an already-dumped, already-validated projection body under
`agentNotifierHeartbeat` — a key nothing declared. It now returns this model, and
`serving/served_state.py` declares the key (now `agentNotifierHeartbeat`, plus the legacy
`agentNotifierHeartbeat` alias) on `ServedWorkspaceProjection`. No bytes moved: the
model is `extra="forbid"` with the same seven camelCase field names the dict carried
(`lastTickAt`, `ageSeconds`, `staleCutoffSeconds`, `stale`, `pendingInboxCount`,
`redeliverableInboxCount`, `lastSweepDurationSeconds`) cit:(["def _agent_notifier_heartbeat_payload(runtime: _ServingRuntime) -> AgentNotifierHeartbeatPayload:"], mcp/src/agents_remember/serving/_app_lifespan.py:219-219) cit:([`ServedWorkspaceProjection`], mcp/src/agents_remember/serving/served_state.py:47-55).

It is deliberately serialized **without** `exclude_none` (`served_state_tail` dumps it plainly,
while it dumps the build stamp with `exclude_none=True`): a supervisor that has never ticked
reports `lastTickAt`/`ageSeconds` as explicit nulls, because the cockpit distinguishes "never
ticked" from "this server does not report a heartbeat at all". That asymmetry between the two
halves of the tail is why they are two dumps and not one cit:([`served_state_tail`], mcp/src/agents_remember/serving/served_state.py:63-78).

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

`AgentNotifierHeartbeatStore(observer_root)` is a JSON-backed single-row store — one atomic overwrite
per tick via a temp-file-then-`os.replace` swap (`supervisor-heartbeat.json` under
`observer_root/workspace/`), never an append log: there is exactly one current tick, no history
worth folding. `read()` returns `None` on any read/parse failure (`OSError`, `ValueError`,
`KeyError`, `TypeError`) rather than raising — a corrupt or absent file degrades to "never ticked".
`tick(now=, pending_inbox_count=, redeliverable_inbox_count=, last_sweep_duration_seconds=)`
increments `sweepCount` from the previous read (or starts at 1) and persists `lastTickAt`,
`sweepCount`, the latest inbox backlog counts, and the latest sweep duration. `read()` defaults the
L8 fields when it sees an older heartbeat file, so existing runtime rows remain readable.

`heartbeat_age_seconds(heartbeat, *, now)` returns `None` for a `None` heartbeat (never ticked) or
an unparseable `lastTickAt`, else the plain `(now - last).total_seconds()`.

`agent_notifier_staleness_banner(observer_root, *, now, stale_cutoff_seconds)` is the fail-loud surface
`mcp/tools/base.py::_tool_payload` calls: reads the heartbeat, returns `None` when it has NEVER
ticked (deliberately silent — the dashboard/supervisor is opt-in via `dashboard.autoStart`, so "no
row yet" in a repo that has never run it is not evidence of anything wrong) or when the age is still
under the cutoff, else a short human-readable one-liner (now worded `"agent-notifier stale ..."`,
formerly `"supervisor stale 2.3m (past the 60s cutoff)"`). Best-effort by construction — every code
path here either returns a value or `None`;
`base.py`'s call site additionally wraps the call in `try/except Exception` as defense-in-depth so
an unreadable heartbeat file can never block a tool response.

### Conventions

Same atomic-overwrite JSON pattern used elsewhere in this codebase for single-current-row state
(temp file with a pid-qualified name, then `os.replace` for atomicity across processes).

### Invariants And Boundaries

- **Durable, not a timer.** The tick row survives a daemon restart; staleness is computed from the
  LAST PERSISTED tick, not from process uptime — a restarted daemon correctly reports "stale since
  the last tick before the restart" until the next sweep ticks again.
- **Never-ticked ≠ stale.** `agent_notifier_staleness_banner` is silent (not alarmed) when there has
  been no tick at all — only a heartbeat that STARTED ticking and then went quiet triggers the
  banner. This asymmetry is deliberate (see Logic) and must be preserved by any future consumer.
- **Read-side never raises.** `read()` swallows every plausible corruption mode and returns `None`;
  callers must treat `None` as "no evidence", never propagate an exception from a heartbeat check.
- **One current row, not a log.** `tick()` overwrites; there is no history to prune or retain.
- **Backlog metrics are volatile status.** Pending/redeliverable inbox counts and last sweep
  duration describe the last completed sweep; they are surfaced through `/api/state`, not treated as
  reducer truth.
- **The row and the read-side payload stay separate types.** `AgentNotifierHeartbeatPayload` may
  gain response-time arithmetic (`ageSeconds`, `stale`) that must never be persisted into
  `supervisor-heartbeat.json`, and `AgentNotifierHeartbeat` must never carry a per-response value.
- **The payload's nulls are meaningful.** Do not serialize it with `exclude_none`: dropping
  `lastTickAt`/`ageSeconds` would collapse "never ticked" into "not reported".

### Todos

No known follow-up in this file. The two documented consumer limitations (dashboard TS unverified by
`tsc` in this environment; the `/api/state` ETag short-circuit meaning an idle tab won't see
`ageSeconds` advance) live with the consumers (`app.py`, `Cockpit.tsx`), not with this store.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
supervisor-heartbeat-specific behavior; this is same-repository control-plane plumbing whose design
source is the leaf task doc (R5), not an external spec.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this heartbeat mechanism; the leaf task doc's R5 and this implementation are the source of truth. | `AgentNotifierHeartbeatStore`; `agent_notifier_staleness_banner` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:63-109; mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:141-157 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application computes response-time heartbeat age/staleness, while the served body declares both wire keys and `served_state_tail` serializes the payload without `exclude_none`. |"def _agent_notifier_heartbeat_payload"; `ServedWorkspaceProjection`; `served_state_tail`|mcp/src/agents_remember/serving/_app_lifespan.py:219-219; mcp/src/agents_remember/serving/served_state.py:48-59; mcp/src/agents_remember/serving/served_state.py:71-90|

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local heartbeat store. | — | — |
## Update History
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the `AgentNotifier*` identifiers, the retained `supervisor-heartbeat.json` artifact name, and the `agentNotifierHeartbeat` + legacy `supervisorHeartbeat` dual wire key. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-04T15:29:35+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: bound application response-time heartbeat payload computation to its operative source span. Verification metadata unchanged.

- 2026-08-01T08:24+02:00 — 260731-EFA-L4 curator: recorded the new
  cit:([`AgentNotifierHeartbeatPayload`], mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:31-55) and the row-vs-read-side split it makes explicit. The
  seven-key answer `app._supervisor_heartbeat_payload` used to build as a bare `dict[str, Any]`
  and write into an already-dumped projection body is now a declared `extra="forbid"` model, and
  the `supervisorHeartbeat` key it rides is declared on
  `served_state.ServedWorkspaceProjection`. Added the two invariants that keep it correct — the
  row and the payload stay separate types, and the payload's nulls are meaningful so it must not
  be dumped with `exclude_none` (a never-ticked supervisor reports explicit nulls, unlike the
  build stamp beside it, which omits). Repaired the Docs References citation, which pointed at a
  bare `L1-L99` range in a file that is now 153 lines and named no symbol; it now names
  `SupervisorHeartbeatStore` and `supervisor_staleness_banner`. Wire bytes unchanged.
  Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: heartbeat rows now carry
  `pendingInboxCount`, `redeliverableInboxCount`, and `lastSweepDurationSeconds`, with backward
  compatible reads for older two-field heartbeat files. Verification metadata pinned until closeout
  stamps the HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R5): the
  self-liveness heartbeat — `SupervisorHeartbeatStore` (atomic-overwrite single-row JSON store),
  `heartbeat_age_seconds`, and `supervisor_staleness_banner` (silent when never-ticked, a
  fail-loud one-liner past the staleness cutoff). Consumed by the MCP tool choke point
  (`mcp/tools/base.py`) and the dashboard header payload (`app.py`'s `/api/state` + SSE snapshot).
  Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
