# mcp/src/agents_remember/serving/terminal_liveness.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/serving/terminal_liveness.py`   |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-10T13:03+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b`                                             |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
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

### 260707-HFX2-L12 CS-6 Update

The liveness sweeper now wraps refresh work in `TerminalCatalog.batch()` and runs catalog compaction inside the batch, so per-entry liveness and turn-state updates hit the in-memory buffer and commit once.

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
`_last_sweep_at`, and runs `_observe_catalog_entry` over every `catalog.list()` row. That helper
passes `status:"landed"` rows through unchanged without probing; landed/archive seats are frozen
inspection artifacts, so the background sweep must not spend per-row tmux capture or catalog-write
work on them. Non-landed rows still go through `observe_terminal_liveness`, including `exited` rows,
which is what lets a false exit self-heal within one sweep interval.

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

**Live turn-state classification (260707-HFX-L8)** rides this SAME sweep call — no new hot loop, no
new tmux round-trip cadence. `TerminalLivenessObservation` gained `turn_state_changed: bool = False`
(true only when THIS observation's classification differs from the row's previous `turn_state`, so
the caller can emit an observer event only on an actual transition, never once per sweep tick).
`observe_terminal_liveness` now routes every ALIVE result — both the direct in-process `is_alive`
branch and the tmux-probe-exists branch — through a new `_observe_alive(catalog, entry, *,
checked_at, pane_capturer)` helper instead of constructing the observation inline. `_observe_alive`
returns the entry unchanged (no classification, `turn_state_changed=False`) for `kind != "harness"`
rows — plain shell terminals are never classified; for a harness row it captures the pane via
`pane_capturer or _default_capture_pane` (the injected seam defaults to
`terminal_paste.capture_pane`, the SAME history-inclusive capture paste-verification already uses —
one capture-command shape, not two), classifies via `turn_state.classify_turn_state(pane_text,
harness=entry.harness)`, persists via `catalog.record_turn_state(entry.id, state, changed_at=...)`,
and sets `turn_state_changed` by comparing the previous vs. updated `turn_state`.
`TerminalCatalogLivenessSweeper.__init__` gained `pane_capturer` (the injectable capture seam,
threaded through every `observe_terminal_liveness` call) and `on_turn_state_change` (a callback
fired, from `refresh()`, for every observation whose `turn_state_changed` is true — `serving/app.py`
wires this to `log_turn_state_change_event`). `refresh()` now collects the full observation list
before returning entries, so it can fan the turn-state-change callback out over all of them in one
pass, still inside the sweeper's rate-limited/non-overlapping cadence.

### Conventions

Pure orchestration over injected seams: catalog writes stay in `terminal_catalog.py`, probe
classification stays in `terminal.py`, turn-state text classification stays in `turn_state.py`; this
module only sequences them under cadence/overlap control. Everything (host, catalog, clock, config,
pane_capturer, on_turn_state_change) is constructor-injected so tests run fake-driven and sleepless.

### Invariants And Boundaries

- **Rate limit + non-overlap are advisory availability, not staleness**: a rate-limited or
  overlapped `refresh()` serves the persisted catalog as-is — callers always get a list, never a
  block or an error.
- **Hysteresis is evidence-scaled**: `tmux-command-failed` needs threshold × window;
  `pane-gone` marks fast. A genuine whole-server tmux death takes the hysteresis path (~3 sweeps)
  before rows mark exited — the deliberate bias away from false exits (HFX-L5 review, disclosed).
- **Self-heal is one sweep away**: exited rows are probed too, so a false mark recovers
  automatically; `terminated` rows are excluded by `catalog.list()` and never revived.
- **Landed archive rows are sweep-cold**: `refresh()` returns them in the same list shape but never
  calls `observe_terminal_liveness`, `tmux capture-pane`, or turn-state classification for them.
  On-demand WebSocket attach/read inspection remains outside this background-sweep exclusion.
  Known limitation: a landed row whose tmux session dies later stays in the archive until explicit
  cleanup; attach performs the live check and fails instead of the sweeper reclaiming it.
- The module never spawns, kills, or attaches tmux sessions and never mutates anything but
  liveness state through `record_liveness_probe` (and, since HFX-L8, turn-state through
  `record_turn_state` for harness rows).
- Turn-state classification rides the SAME rate-limited sweep cadence as liveness — no separate
  cadence, no extra tmux round-trip beyond the one `pane_capturer` call per alive harness row per
  sweep. Only `kind == "harness"` rows are ever classified; plain `terminal` rows are untouched.

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
| Regression tests: failure-storm hysteresis, pane-gone fast-mark, self-heal, rate limit, overlap suppression, landed-row sweep exclusion, stderr classification. | `TerminalCatalogLivenessTests` | [../../../tests/test_terminal_liveness.py](../../../tests/test_terminal_liveness.py) |
| The marker-based classifier this module's `_observe_alive` calls on every alive harness row. | `classify_turn_state` | [turn_state.py](turn_state.py) |
| The public pane-capture wrapper `_observe_alive`'s default `pane_capturer` uses (same capture shape paste verification already uses). | `capture_pane` | [terminal_paste.py](terminal_paste.py) |
| `create_app` wires `on_turn_state_change` to `log_turn_state_change_event` so a sweep-detected transition becomes an observer event. | `TerminalCatalogLivenessSweeper(...)` construction | [app.py](app.py) |
| Failing-first tests for turn-state classification wiring: scripted pane fixtures, precedence ordering, "plain terminals never classified", `turn_state_changed` gating. | `test_seat_lifecycle.py` | [../../../tests/test_seat_lifecycle.py](../../../tests/test_seat_lifecycle.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local liveness plumbing. | — | — |

### 260713-PHA-L5 Protocol Liveness

Process existence remains tmux evidence, while hosted activity and turn state come from the exact
adapter snapshot. Bridge failures remain explicit disconnected/unknown states; pane classifiers are
stored only as diagnostics and cannot produce supervisor actions.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented adapter-derived liveness and diagnostic-only pane signals.

- 2026-07-10T13:03+02:00 — No content impact: 260707-HFX2-L15 removed a stale comment that called
  liveness pane capture part of dispatch acceptance. Runtime liveness behavior is unchanged;
  harness-log acceptance is owned by the delivery path. Verification metadata remains pinned until
  closeout stamps the eventual L15 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: recorded the known landed-archive
  limitation from review — sweep-cold rows are not reclaimed when their tmux session later dies;
  attach performs the on-demand check and explicit cleanup remains the reclamation path.
  Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: `TerminalCatalogLivenessSweeper`
  now passes `status:"landed"` rows through without calling `observe_terminal_liveness`; the landed
  archive remains returned to callers but no longer adds per-row tmux capture, turn-state
  classification, or catalog-write work to each background sweep. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: live turn-state): live turn-state
  classification folded into the existing alive-probe path via a new `_observe_alive` helper —
  harness rows only, classified with `turn_state.classify_turn_state` over `pane_capturer`'s
  captured text, persisted via `catalog.record_turn_state`. `TerminalLivenessObservation` gained
  `turn_state_changed`; `TerminalCatalogLivenessSweeper` gained `pane_capturer` +
  `on_turn_state_change` constructor seams, and `refresh()` fans the change callback out after
  collecting the full observation list. No new hot loop, no new tmux round-trip cadence beyond one
  capture per alive harness row per existing sweep. Verification metadata pinned until closeout
  stamps the HFX-L8 commit.
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
