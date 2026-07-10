# mcp/src/agents_remember/serving/supervisor_heartbeat.py

| Field                  | Value                                                     |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/serving/supervisor_heartbeat.py`    |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-07-08T23:59+02:00                                        |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`                    |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`supervisor_heartbeat.py` is the supervisor sweep's own self-liveness primitive (260707-HFX2-L2,
R5): issue #15's "the watcher must be code AND watched". The supervisor sweeps other seats for
liveness/deadline drift, but the sweep itself is just another process that can silently stop — so
it writes its own heartbeat tick row on every completed sweep, durable across a daemon restart (a
timer alone would go blind on restart; a row does not). Two independent readers consume the tick
age: an MCP tool call opportunistically attaches a fail-loud banner when it goes stale
(`mcp/tools/base.py`), and the dashboard header renders it directly, mirroring how `servingBuild`
already surfaces the boot stamp.

## Code Commentary

### Logic

`SupervisorHeartbeatStore(observer_root)` is a JSON-backed single-row store — one atomic overwrite
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

`supervisor_staleness_banner(observer_root, *, now, stale_cutoff_seconds)` is the fail-loud surface
`mcp/tools/base.py::_tool_payload` calls: reads the heartbeat, returns `None` when it has NEVER
ticked (deliberately silent — the dashboard/supervisor is opt-in via `dashboard.autoStart`, so "no
row yet" in a repo that has never run it is not evidence of anything wrong) or when the age is still
under the cutoff, else a short human-readable one-liner (`"supervisor stale 2.3m (past the 60s
cutoff)"`). Best-effort by construction — every code path here either returns a value or `None`;
`base.py`'s call site additionally wraps the call in `try/except Exception` as defense-in-depth so
an unreadable heartbeat file can never block a tool response.

### Conventions

Same atomic-overwrite JSON pattern used elsewhere in this codebase for single-current-row state
(temp file with a pid-qualified name, then `os.replace` for atomicity across processes).

### Invariants And Boundaries

- **Durable, not a timer.** The tick row survives a daemon restart; staleness is computed from the
  LAST PERSISTED tick, not from process uptime — a restarted daemon correctly reports "stale since
  the last tick before the restart" until the next sweep ticks again.
- **Never-ticked ≠ stale.** `supervisor_staleness_banner` is silent (not alarmed) when there has
  been no tick at all — only a heartbeat that STARTED ticking and then went quiet triggers the
  banner. This asymmetry is deliberate (see Logic) and must be preserved by any future consumer.
- **Read-side never raises.** `read()` swallows every plausible corruption mode and returns `None`;
  callers must treat `None` as "no evidence", never propagate an exception from a heartbeat check.
- **One current row, not a log.** `tick()` overwrites; there is no history to prune or retain.
- **Backlog metrics are volatile status.** Pending/redeliverable inbox counts and last sweep
  duration describe the last completed sweep; they are surfaced through `/api/state`, not treated as
  reducer truth.

### Todos

No known follow-up in this file. The two documented consumer limitations (dashboard TS unverified by
`tsc` in this environment; the `/api/state` ETag short-circuit meaning an idle tab won't see
`ageSeconds` advance) live with the consumers (`app.py`, `Cockpit.tsx`), not with this store.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
supervisor-heartbeat-specific behavior; this is same-repository control-plane plumbing whose design
source is the leaf task doc (R5), not an external spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this heartbeat mechanism; the leaf task doc's R5 and this implementation are the source of truth. | L1-L99 | [supervisor_heartbeat.py](supervisor_heartbeat.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `run_supervisor_sweep` ticks this store unconditionally at the end of every sweep, even a zero-finding one. | `SupervisorHeartbeatStore.tick` | [supervisor.py](supervisor.py.md) |
| `_tool_payload` calls `supervisor_staleness_banner` on every MCP tool response, resolving the observer root via `AmbientLifecycle.root`. | `supervisor_staleness_banner` | [../mcp/tools/base.py](../mcp/tools/base.py.md) |
| `_supervisor_heartbeat_payload` reads this store to build the `supervisorHeartbeat` payload attached to `/api/state` and the SSE snapshot. | `heartbeat_age_seconds` | [app.py](app.py.md) |
| The `root` accessor this module's MCP-tool consumer resolves the observer root through. | `AmbientLifecycle.root` | [../observer/ambient.py](../observer/ambient.py.md) |
| Failing-first tests for read/tick/age/banner behavior, including the never-ticked-is-silent case. | `SupervisorHeartbeatTests` | [../../../tests/test_supervisor.py](../../../tests/test_supervisor.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local heartbeat store. | — | — |

## Update History

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
