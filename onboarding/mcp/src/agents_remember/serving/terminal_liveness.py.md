# mcp/src/agents_remember/serving/terminal_liveness.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/serving/terminal_liveness.py`   |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-07T23:45+02:00                                   |
| lastVerifiedCommitHash | `607cab0d32d0527930e336b382c26362cf0ca22b`               |
| lastVerifiedCommitDate | 2026-07-07T23:29:25+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal_liveness.py` (new in **260707-HFX-L5**, catalog liveness hysteresis) owns liveness
probing for durable dashboard terminal catalog rows: a **rate-limited, non-overlapping sweeper**
(`TerminalCatalogLivenessSweeper`) plus the **shared single-row observation path**
(`observe_terminal_liveness`) that the sessions endpoint, WebSocket attach, and server-side paste
all route through. It decouples tmux probing cadence from the dashboard refresh cadence (the 1s
projection tick / `/api/terminal/sessions` polling no longer implies 1s tmux probing) and replaces
`serving.app`'s deleted `_refresh_catalog_entries`, whose immediate exit-marks on any probe
failure could mass-exit a live fleet during a transient tmux command-failure storm.

## Code Commentary

### Logic

Module constants are the **code-default hysteresis knobs** (deliberately not settings-backed in
this leaf): `DEFAULT_LIVENESS_FAILURE_THRESHOLD = 3` (consecutive command failures before an exit
mark), `DEFAULT_LIVENESS_FAILURE_WINDOW_SECONDS = 5.0` (minimum age of the first failure),
`DEFAULT_PANE_GONE_FAILURE_THRESHOLD = 1` (pane-gone is definitive, so it marks fast), and
`DEFAULT_LIVENESS_SWEEP_INTERVAL_SECONDS = 10.0` (minimum spacing between full catalog sweeps).
`TerminalCatalogLivenessConfig` is the frozen bundle of those four; `TerminalLivenessObservation`
pairs the (possibly updated) `TerminalCatalogEntry` with an `alive` verdict. `Clock` is
`Callable[[], datetime]` with the `utc_now()` default — `serving.app` injects its `now` seam so
sim/replay wiring keeps ONE timestamp base per app instance (the L5R2 F4 fix).

`TerminalCatalogLivenessSweeper.refresh()` enforces cadence and non-overlap: it returns the
current `catalog.list()` **without probing** when the sweep is rate-limited
(`_rate_limited(moment)` — last sweep younger than `sweep_interval_seconds`) or when another
refresh already holds the non-blocking `threading.Lock` (`acquire(blocking=False)`); inside the
lock it double-checks the rate limit (two callers can pass the unlocked check), stamps
`_last_sweep_at`, and runs `observe_terminal_liveness` over **every** `catalog.list()` row —
including `exited` rows, which is what lets a false exit self-heal within one sweep interval.

`observe_terminal_liveness(catalog, host, entry, *, checked_at, config=None)` probes ONE row and
persists the matching hysteresis transition via `catalog.record_liveness_probe(...)`. Evidence
ladder: an in-process host session with `is_alive` (via the duck-typed `_host_session` /
`_TerminalSessionLike` runtime protocol) is direct process evidence ⇒ record alive; otherwise
`_probe_tmux` asks the host — preferring an evidence-bearing `probe_session` returning a real
`TmuxProbeResult`, degrading to boolean `has_session` (mapped alive/pane-gone) for legacy hosts
(the `TerminalLivenessHost` protocol only requires `has_session`) — an alive probe records alive
(self-heal side), a dead one records the failure with `_failure_evidence(probe)`
(`tmux-command-failed` stays transient; everything else is `pane-gone`). When
`record_liveness_probe` returns `None` (row vanished from the catalog), the observation falls back
to the caller's entry (with `with_liveness_success()` applied on the alive side) without phantom
writes.

### Conventions

Pure orchestration over injected seams: catalog writes stay in `terminal_catalog.py`, probe
classification stays in `terminal.py`; this module only sequences them under cadence/overlap
control. Everything (host, catalog, clock, config) is constructor-injected so tests run
fake-driven and sleepless.

### Invariants And Boundaries

- **Rate limit + non-overlap are advisory availability, not staleness**: a rate-limited or
  overlapped `refresh()` serves the persisted catalog as-is — callers always get a list, never a
  block or an error.
- **Hysteresis is evidence-scaled**: `tmux-command-failed` needs threshold × window;
  `pane-gone` marks fast. A genuine whole-server tmux death takes the hysteresis path (~3 sweeps)
  before rows mark exited — the deliberate bias away from false exits (HFX-L5 review, disclosed).
- **Self-heal is one sweep away**: exited rows are probed too, so a false mark recovers
  automatically; `terminated` rows are excluded by `catalog.list()` and never revived.
- The module never spawns, kills, or attaches tmux sessions and never mutates anything but
  liveness state through `record_liveness_probe`.

### Todos

Hysteresis constants remain code defaults, not settings-backed knobs (builder-disclosed residual);
`exitEvidence` is persisted/API-visible but not yet surfaced in the dashboard UI.

## Docs References

No external documentation governs this module; the HFX-L5 leaf doc and review are the design
record.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No domain document defines the sweep/hysteresis semantics; the implementation is the source of truth. | module docstring; constants | [terminal_liveness.py](terminal_liveness.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The evidence-bearing tmux probe (`TmuxProbeResult`, `probe_session`, stderr-aware classification) this module consumes. | `_tmux_probe_session` | [terminal.py](terminal.py) |
| The persisted liveness state + locked `record_liveness_probe` write point this module drives. | `with_liveness_success`; `with_liveness_failure` | [terminal_catalog.py](terminal_catalog.py) |
| The app wiring: one sweeper behind `GET /api/terminal/sessions`, direct observations on WebSocket attach + paste, injected clock. | `create_app` | [app.py](app.py) |
| Regression tests: failure-storm hysteresis, pane-gone fast-mark, self-heal, rate limit, overlap suppression, stderr classification. | `TerminalCatalogLivenessTests` | [../../../tests/test_terminal_liveness.py](../../../tests/test_terminal_liveness.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local liveness plumbing. | — | — |

## Update History

- 2026-07-07T23:45+02:00 — Created for 260707-HFX-L5 (catalog liveness hysteresis):
  `TerminalCatalogLivenessSweeper` (rate-limited by `sweep_interval_seconds` — default 10s —
  non-overlapping via a non-blocking lock with a double-checked rate limit; rate-limited/overlapped
  callers get the current catalog without probing) + `observe_terminal_liveness` (the shared
  single-row observation path: in-process `is_alive` → evidence-bearing `probe_session` → legacy
  `has_session`, persisting through `record_liveness_probe`) + the frozen
  `TerminalCatalogLivenessConfig` over the four code-default constants (3 failures / 5s window /
  pane-gone=1 / 10s sweep). Replaces `serving.app._refresh_catalog_entries`; the L5R2 fix round
  wired the app's injected clock through attach/paste observations. Verification metadata pinned
  until closeout stamps the HFX-L5 commit.
