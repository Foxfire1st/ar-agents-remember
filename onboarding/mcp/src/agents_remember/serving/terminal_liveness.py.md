# mcp/src/agents_remember/serving/terminal_liveness.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal_liveness.py` owns protocol-derived liveness/activity projection for durable dashboard
terminal catalog rows through a **rate-limited, non-overlapping sweeper**
(`TerminalCatalogLivenessSweeper`) plus the **shared single-row observation path**
(`observe_terminal_liveness`) that WebSocket attach, the server-side paste target
(`_live_paste_target`), and the harness-control routes all route through. The sweeper's own
steady-state driver is the serving lifespan (`_app_lifespan.py::_terminal_observation_loop`); the
terminal-session GET is **not** among its callers — that route projects `runtime.catalog.list()` and
names no sweeper (see `## 260831-LOCR-R02 Current Delta`). The module decouples tmux probing cadence
from the dashboard refresh cadence (the 1s projection tick / `/api/terminal/sessions` polling no
longer implies 1s tmux probing) and replaces
`serving.app`'s deleted `_refresh_catalog_entries`, whose immediate exit-marks on any probe
failure could mass-exit a live fleet during a transient tmux command-failure storm.

## Code Commentary

### 260707-HFX2-L12 CS-6 Update

The liveness sweeper wraps the observation phase of a full refresh in `TerminalCatalog.batch()`, so per-entry liveness and turn-state updates hit the in-memory buffer and commit once. Catalog compaction does **not** run inside that batch: it runs after the batch commits, because the registration that authorizes reclamation takes the task CAS and no process may nest that beneath the catalog lock (see `## 260831-LOCR-R23 Current Delta`).

### Logic

For hosted harnesses, the current L5 liveness contract reads the exact adapter snapshot: control,
activity, acceptance, vendor identity, sequence, pending interaction, and raw vendor detail are
projected additively. Bridge failure becomes explicit disconnected/unknown state. Tmux/process
existence remains process-liveness evidence only; pane text, turn-state classifiers, terminal logs,
copy mode, and capture timing are diagnostic detail and cannot authorize readiness, delivery,
completion, or supervisor action. Ordinary shell rows remain ordinary terminal rows.

The detailed pane/turn-state path below is historical pre-L5 behavior and is retained only to explain
the migration surface; it is not current hosted authority.

The **code-default hysteresis knobs** (deliberately not settings-backed) are
`DEFAULT_LIVENESS_FAILURE_THRESHOLD = 3` (consecutive command failures before an exit
mark), `DEFAULT_LIVENESS_FAILURE_WINDOW_SECONDS = 5.0` (minimum age of the first failure),
`DEFAULT_PANE_GONE_FAILURE_THRESHOLD = 1` (pane-gone is definitive, so it marks fast), and
`DEFAULT_LIVENESS_SWEEP_INTERVAL_SECONDS = 10.0` (minimum spacing between full catalog sweeps).
Since 260731-EFA-L2 those four constants and `TerminalCatalogLivenessConfig` (the frozen bundle of
them, plus `DEFAULT_LIVENESS_HYSTERESIS`) are **defined in `terminal_catalog.py`** and imported
here. `TerminalLivenessObservation`
pairs the (possibly updated) `TerminalCatalogEntry` with an `alive` verdict. `Clock` is
`Callable[[], datetime]` with the `utc_now()` default — `serving.app` injects its `now` seam so
sim/replay wiring keeps ONE timestamp base per app instance (the L5R2 F4 fix).

`TerminalCatalogLivenessSweeper.refresh()` enforces cadence and non-overlap. A call whose moment is
rate-limited (`_rate_limited(moment)` — last sweep younger than `sweep_interval_seconds`) does not
probe the full catalog; it delegates to the targeted starting-row fast path
(`_refresh_starting_rows`, cit:([`_refresh_starting_rows`], mcp/src/agents_remember/serving/terminal_liveness.py:223-268)).
A call that passes the outer cadence check but cannot take the non-blocking `threading.Lock`
(`acquire(blocking=False)`) returns `catalog.list_committed()` — the last atomically replaced file —
and never waits and never runs a second sweep. That distinction is load-bearing: `catalog.list()`
reads the instance snapshot and would block on the catalog `RLock` the winning sweep holds for its
whole batch, which is exactly the contended-sweep stall. `list_committed()` is the explicit
contention read, with no cache, alternate parser, or fallback. Inside the lock the sweep re-checks
the rate limit (cit:([`_rate_limited`], mcp/src/agents_remember/serving/terminal_liveness.py:277-282)
— two callers can pass the unlocked check), stamps `_last_sweep_at`, and runs
`_observe_catalog_entry` (cit:([`_observe_catalog_entry`], mcp/src/agents_remember/serving/terminal_liveness.py:284-298))
over every `catalog.list()` row inside exactly ONE `catalog.batch()`. That helper passes
`status:"landed"` rows through unchanged without probing; landed/archive seats are frozen
inspection artifacts, so the background sweep must not spend per-row tmux capture or catalog-write
work on them. Non-landed rows still go through `observe_terminal_liveness`, including `exited` rows,
which is what lets a false exit self-heal within one sweep interval. The sweep lock is released in
`finally`, so a later cadence retries after success, expected failure, or an unexpected exception.

A due full sweep then runs one fixed post-commit order (cit:([`refresh`], mcp/src/agents_remember/serving/terminal_liveness.py:174-221)): enumerate terminated
rows with `include_terminated=True` and keep `status == "terminated"`
(cit:([`list`], mcp/src/agents_remember/serving/terminal_catalog.py:80-84)) → offer exactly that set to the injected
`register_execution_evidence` registrar (cit:([`register_execution_evidence`], mcp/src/agents_remember/serving/terminal_liveness.py:140-142)) → hand only the
returned proven id set to `compact(now=..., registered_execution_ids=...)`
(cit:([`compact`], mcp/src/agents_remember/serving/terminal_catalog.py:315-345)) → drain the deferred interaction syncs → fire the
turn-state callbacks. Registration precedes compaction because the registrar writes to a different store and
takes the task CAS, which must never be nested beneath the catalog lock the batch holds. Only the
registrar's own return value is treated as proof of registration; when no registrar is wired, `refresh`
supplies the literal `frozenset()` — a fail-closed default — and a task-bound leaf row is then retained
by the catalog's reclamation predicate (cit:([`_leaf_execution_entry`], mcp/src/agents_remember/serving/terminal_catalog.py:52-62)). A raising registrar escapes unguarded, so the
pass fails before compaction and the terminal rows stay available for a later attempt. The rate-limited
starting-row fast path (`_refresh_starting_rows`) performs neither operation: registration and
compaction are full-sweep responsibilities only. The registered-order proof lives in
`mcp/tests/test_terminal_liveness_registration_order.py`.

`observe_terminal_liveness(catalog, host, entry, *, checked_at, probe=DEFAULT_LIVENESS_PROBE)` probes ONE row and
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

**Historical — live turn-state classification (260707-HFX-L8, superseded as hosted authority).** It rode this SAME sweep call — no new hot loop, no
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

### 260718-CHATS-L5 H1/F2 — hosted-interaction synchronizer quarantine

`_observe_alive` wires the app's `on_control_snapshot` observer (the `HostedInteractionSynchronizer`
built in `app.py`'s `create_app`) — a DOWNSTREAM durable projection (agent-question gates +
operator-inbox completion rows), NOT part of computing this row's liveness/control state, which
`catalog.upsert(projected)` has already committed BEFORE the observer runs. L5 routes that call
through the new `_observe_control_snapshot(catalog, entry, snapshot, observer, *,
previous_sync_error)`, which **quarantines the per-entry side effect**: on ANY exception it records
the failure loudly on that one row (`control_raw["interactionSyncError"] = str(exc)`, re-`upsert`,
and — F2 — a `warning` log only on STATE CHANGE) and returns the quarantined entry, so the sweep
continues over the rest of the catalog.

Before this guard the observer call sat unguarded inside the sweep's per-entry list comprehension,
INSIDE `with self._catalog.batch()`: a single `HarnessControlError` (a hosted completion whose
`vendorCorrelationId` matches no accepted inbox row) propagated out, aborted the whole batch, and
500-ed `GET /api/terminal/sessions` for EVERY row (the developer's stuck-loading rail — H1 / L4
verdict E1). The broad `except Exception` is deliberate: a broken-pipe/disk failure in the same
durable side effect must equally not fail the catalog; it is fail-loud (row marker + log + standing
regressions in `test_chats_l5_hardening.py`), never swallowed. The completion-correlation contract
that raised (`hosted_interactions.py`) is left untouched — this is availability hardening, not a
correlation redesign.

**260731-EFA-L16 — the quarantined placement was itself a lock-order violation.** The guard kept a
synchronizer exception from aborting the sweep, but the guarded call still ran INSIDE `with
self._catalog.batch()`, and the synchronizer folds the operator-inbox and gate stores: on
2026-08-05 the production serving daemon deadlocked twice (py-spy-verified ABBA) — this sweep held
the catalog batch lock (RLock + flock) across those inbox/gate acquisitions while the supervisor
sweep held the inbox lock across a catalog read, and the uvicorn event loop then queued on the
same catalog RLock via async endpoints doing synchronous catalog reads, so the server stopped
accepting. The synchronizer still rides the ONE sweep tick (no second hot loop), but it no longer
runs inside the batch: `refresh()` and `_refresh_starting_rows()` collect a `sync_collector` list
and `_observe_catalog_entry` bundles it into the probe (`replace(probe, sync_collector=...)` — a
`LivenessProbe` field beside the observer it defers, so `observe_terminal_liveness` keeps its
five-argument signature), `_observe_alive` appends a `_PendingInteractionSync` (entry, snapshot,
previous_sync_error) instead of calling `_observe_control_snapshot`, and after the batch commits
the new `_run_deferred_interaction_syncs` drains the list — re-reading each row via `catalog.get`
before the quarantine upsert, so the marker composes with the just-committed turn state. A probe
whose `sync_collector` is `None` (the direct callers outside a batch — WS attach, paste) keeps
the legacy inline call. The quarantine semantics above are otherwise unchanged; the one visible
cost is that a freshly-quarantined row shows its `interactionSyncError` marker from the next
catalog read rather than inside this sweep's return value.

**Load-bearing steady state.** An orphan `vendorCorrelationId` is the NORMAL steady state of every
cockpit-driven hosted (`+ Chat`) codex chat — a cockpit turn's terminal result carries a correlation
id that matches no operator-inbox row because it never was an inbox delivery — so this quarantine
path is HOT, not an edge corruption, and re-fires on every ~10 s sweep for the affected row
indefinitely (reviewer observed it live on an ordinary chat). F2 bounds the resulting log spam to
state changes (first occurrence / a changed error / heal) while still refreshing the per-sweep wire
marker so the row stays honestly degraded on every read; `_observe_control_snapshot` logs `info`
once on heal and drops the marker (the marker is rebuilt from the snapshot each sweep, so it
self-heals when the fault stops). F3 — the root completion-correlation contract that treats every
terminal result as inbox-correlated and aborts at the first orphan (so a later legitimate inbox
completion never records for that row) — is a REQUIRED master-exit disposition (recommended: a
non-inbox completion is a normal skip, not an error), explicitly outside this leaf's bounded scope.

**Residual (L5 delta-verify F8, Low, second-half-eligible).** Re-warns still occur on PHANTOM state
changes: a `control_raw` rebuild on a non-observer path (a transient bridge-error sweep, or the
WS-attach path that runs `observe_terminal_liveness` with no observer) drops the marker, so the next
failing sweep sees no previous marker and warns again, and no intermediate `recovered` line is
emitted for that transition. Correction not taken here: carry `interactionSyncError` through
`control_raw` rebuilds on non-observer paths, or log the intermediate transitions symmetrically.

### Conventions

Pure orchestration over injected seams: catalog writes stay in `terminal_catalog.py`, probe
classification stays in `terminal.py`, turn-state text classification stays in `turn_state.py`; this
module only sequences them under cadence/overlap control. Everything (host, catalog, clock, config,
pane_capturer, on_turn_state_change) is constructor-injected so tests run fake-driven and sleepless.

### Invariants And Boundaries

- The `on_control_snapshot` hosted-interaction synchronizer runs as a QUARANTINED per-entry side
  effect (L5 H1): its correctness is independent of the row's liveness/control projection, which is
  already committed, so one row's synchronizer failure records fail-loud on that row's
  `interactionSyncError` and NEVER aborts the catalog sweep. An orphan-`vendorCorrelationId`
  completion is the normal steady state of cockpit-driven hosted chats, so this path is hot; the
  marker refreshes every sweep and self-heals when the fault clears (F2 bounds the log to state
  changes; F8 phantom re-warns on non-observer `control_raw` rebuilds remain a Low residual).
- **The synchronizer NEVER runs under the catalog batch lock** (260731-EFA-L16): the sweep collects
  `_PendingInteractionSync` evidence inside `catalog.batch()` and drains it after the commit via
  `_run_deferred_interaction_syncs`, re-reading each row before the marker upsert. One store's lock
  is never held while another store's is acquired — the cross-store order doctrine in
  [durable_store.py](../controlplane/durable_store.py.md), written from the 2026-08-05 ABBA
  deadlock.
- Hosted activity and turn state are adapter-derived; pane/log/copy-mode observations are
  diagnostics-only and cannot drive readiness, delivery, completion, or supervisor action.
- The sweeper remains rate-limited and non-overlapping, and process-liveness failures remain
  explicit disconnected/unknown evidence rather than a hidden compatibility fallback.
- **Contention serves the committed snapshot, never a blocking read.** A `refresh()` that loses the
  non-blocking sweep lock returns `catalog.list_committed()`; `catalog.list()` belongs only to
  admitted callers, because the snapshot path would wait on the winning sweep's catalog batch lock.
- **The starting fast path acquires before it lists.** `_refresh_starting_rows` takes the shared
  non-blocking lock first, re-checks the starting cadence behind the lock, and only then lists and
  filters the capped starting selection. An empty selection returns without opening a batch and
  without stamping `_last_starting_sweep_at`, so an empty tick does not consume the one-second
  window.
- **One admitted path owns exactly one batch, and one final row per observation.** Full and
  starting paths each wrap their observations in a single `catalog.batch()`; the alive projection
  composes the adapter (or raw-TUI unsupported) projection together with `paneDiagnostic` and
  issues one `catalog.upsert`, so no intermediate row variant is persisted.
- Liveness projection never consumes inbox rows. Inbox delivery is inbox-rooted and explicit
  recipient `consume` remains the sole acknowledgement.

The remaining bullets below describe historical hysteresis and diagnostic mechanics retained for
migration archaeology; they do not override the protocol-backed L5 contract above.

- **Rate limit + non-overlap are advisory availability, not staleness**: a rate-limited `refresh()`
  still serves the catalog (via the bounded starting-row fast path) and an overlapped one serves
  the committed atomic snapshot — callers always get a list, never a block or an error.
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
  liveness state through `record_liveness_probe` and turn/terminal truth through
  `seat_turn_truth.record_turn_projection` (the module's only catalog write for turn truth —
  `terminal_liveness.py:619`). **It does not call `catalog.record_turn_state`.** That method still
  exists on the port and on `TerminalCatalog` (`serving/ports.py:179`,
  `serving/terminal_catalog.py:265`) and is exercised by `mcp/tests/test_terminal_catalog.py:151`, but
  no production caller uses it, and the per-entry-mutator sentence in
  `terminal_catalog.py:285`'s `batch()` docstring names it as a sweep mutator it no longer is. This
  bullet replaces an earlier claim that the module wrote turn state through `record_turn_state`
  (260707-HFX-L8); that was true of the pre-authority-change sweep and is historical.
- Turn truth is projected, not classified in place: `_record_adapter_turn_state` composes a
  `CatalogTurnEvidence` stamp from the canonical adapter snapshot (or the literal `"stale"` on the R21
  threshold and the legacy unsupported-control path) and hands it to
  `seat_turn_truth.record_turn_projection`, so this module can never write a pane reading into
  `turn_state`, `terminal_outcome`, `terminal_evidence_id`, `interrupted_by` or
  `state_signal_emitted_for`.
- Turn-state classification rides the SAME rate-limited sweep cadence as liveness — no separate
  cadence, no extra tmux round-trip beyond the one `pane_capturer` call per alive harness row per
  sweep. Only `kind == "harness"` rows are ever classified; plain `terminal` rows are untouched.

### Todos

Hysteresis constants remain code defaults, not settings-backed knobs (builder-disclosed residual);
`exitEvidence` is persisted/API-visible but not yet surfaced in the dashboard UI.

## Evidence

### Docs References

No external documentation governs this module; the HFX-L5 leaf doc and review are the design
record.

- No domain document defines the sweep/hysteresis semantics; the implementation is the source of truth. [1]

### Repo-Internal References

- The evidence-bearing tmux probe (`TmuxProbeResult`, `probe_session`, stderr-aware classification) this module consumes. [2]
- The persisted liveness state + locked `record_liveness_probe` write point this module drives. [3]
- The app wiring: one sweeper whose steady-state caller is the serving lifespan's observation loop, direct observations on WebSocket attach + the live-paste target, injected clock. `GET /api/terminal/sessions` is not a caller — it projects `runtime.catalog.list()` and names no sweeper (see `## 260831-LOCR-R02 Current Delta`). [4]
- Regression tests: failure-storm hysteresis, pane-gone fast-mark, self-heal, rate limit, overlap suppression, landed-row sweep exclusion, stderr classification, committed-snapshot contention, dirty-gated single-write batches. [5]
- The marker-based classifier this module's `_observe_alive` calls on every alive harness row. [6]
- The public pane-capture wrapper `_observe_alive`'s default `pane_capturer` uses (same capture shape paste verification already uses). [7]
- `create_app` wires `on_turn_state_change` to `log_turn_state_change_event` so a sweep-detected transition becomes an observer event. [8]
- The explicit contention read and dirty-gated batch the sweep depends on. [9]
- The pure projection helpers the alive path composes before its single final upsert. [10]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes this local liveness plumbing.

#### 260713-PHA-L5 Protocol Liveness

Process existence remains tmux evidence, while hosted activity and turn state come from the exact
adapter snapshot. Bridge failures remain explicit disconnected/unknown states; pane classifiers are
stored only as diagnostics and cannot produce supervisor actions.

## 260718-CHATS-L5I Current Delta

Terminal liveness now checks starting control rows on a one-second fast path and requires consecutive failed reads before marking a busy bridge disconnected. Full-sweep cadence and prompt tmux-death detection remain distinct from this startup/read hysteresis.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

Two changes, both about where things live:

1. **`TerminalCatalogLivenessConfig` and the `DEFAULT_LIVENESS_*` constants moved OUT of this
   module** into [terminal_catalog.py](terminal_catalog.py.md); this module imports
   `DEFAULT_LIVENESS_HYSTERESIS` / `TerminalCatalogLivenessConfig` from there. Any reference to
   `terminal_liveness.DEFAULT_LIVENESS_FAILURE_THRESHOLD` (or its siblings) is stale.
2. **`LivenessProbe`** (`hysteresis`, `pane_capturer`, `snapshot_reader`, `on_control_snapshot`;
   module default `DEFAULT_LIVENESS_PROBE`) is the new single argument: **how one catalog row is
   observed — the instruments that read it, and the rule that judges it**. Reading and judging are
   one decision: the pane capturer and the bridge snapshot reader produce the evidence,
   `hysteresis` decides how much of it is required before a row is marked exited, and
   `on_control_snapshot` is who else gets to see that same evidence. Substituting one without the
   others — a fake reader against production thresholds, say — observes a session that does not
   exist, which is exactly the mistake four separate parameters made easy.

The observation semantics and exit-marking rules themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L16 Current Delta

One change, about when the side effect runs: the hosted-interaction synchronizer no longer runs
inside `TerminalCatalog.batch()`. During the batch the sweep only COLLECTS the evidence — one
`_PendingInteractionSync` (entry, snapshot, previous_sync_error) per alive harness row with an
observer — and the new `_run_deferred_interaction_syncs` drains the list after the commit,
re-reading each row (`catalog.get`) before the quarantine upsert so the marker composes with the
just-committed turn state. The collector is a `LivenessProbe` field bundled beside
`on_control_snapshot` (the observer it defers): `_observe_catalog_entry` swaps it in via
`replace(probe, sync_collector=...)`, so `observe_terminal_liveness` keeps its five-argument
signature; a probe whose collector is `None` (the direct callers outside a batch — WS attach,
paste) keeps the legacy inline behavior. The quarantine contract — fail-loud
`interactionSyncError`, log on state change, self-heal on clear — is unchanged; the visible cost
is that a freshly-quarantined row shows its marker from the next catalog read rather than inside
this sweep's return value.

Provenance: on 2026-08-05 the production serving daemon deadlocked twice (py-spy-verified ABBA) —
this sweep held the catalog batch lock across the synchronizer's operator-inbox/gate lock
acquisitions while the supervisor sweep held the inbox lock across a catalog read, and the uvicorn
event loop queued on the same catalog RLock via async endpoints doing synchronous catalog reads.
The placement CHATS-L5 had quarantined was the second symptom: the guard absorbed the failure
mode, not the lock-order one. Forcing regressions live in `mcp/tests/test_cross_store_lock_order.py`
(placement property on both sweep paths, rendezvous-parked ABBA reproduction on real sweeps,
event-loop offload).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260821-CLIVE Register-Then-Compact Boundary

`TerminalLivenessActions` bundles turn-state notification with the task-execution registrar.
`refresh` completes and releases the catalog liveness batch, snapshots terminated rows, registers
eligible task-bound leaf execution evidence, and only then compacts with the returned ids. This
ordering avoids nesting the task CAS beneath the catalog lock. When no registrar is injected, the
empty registered set authorizes no task-bound reclamation; there is no second evidence reader or
fallback scan.

## 260831-LOCR-L22 Current Delta — Committed Contention Read, Admission-Before-List, Final-Only Projection

Three sweeper facts changed, all inside the existing non-blocking single-pass architecture:

1. **Full-sweep contention** returns `self._catalog.list_committed()` instead of `self._catalog.list()`.
   The previous call could park on the catalog `RLock` held by the active batch, so a contended
   `refresh()` — at that time reachable from the `GET /api/terminal/sessions` path, today reached
   only from the serving lifespan's observation loop and the notifier's inline refresh (see
   `## 260831-LOCR-R02 Current Delta`) — could stall instead of returning current state.
2. **The starting-row fast path acquires before it lists.** It previously listed rows, filtered the
   capped starting selection, and only then attempted the sweep lock, so a contender could block on
   the active catalog batch during that first list. It now attempts the shared lock first, returns
   `list_committed()` on contention, and re-checks the starting cadence behind the lock before the
   first list; an empty selection still returns without opening a batch or consuming the one-second
   window.
3. **Final-only liveness projection.** The alive path builds the final row from the pure
   `control_snapshot_entry` / `legacy_control_unsupported_entry` helpers, adds `paneDiagnostic`, and
   issues one `catalog.upsert`; a hosted snapshot or legacy unsupported row is no longer persisted
   and then replaced inside the same observation. Combined with the catalog's equal-row upsert
   guard, a repeated clean sweep performs zero file replacements.

Preserved by construction: one batch per admitted path, post-lock cadence recheck, `finally`
release of the sweep lock on success/expected failure/unexpected exception, the deferred
post-commit interaction drain, and the post-batch registration-then-compaction order. This leaf does
NOT own cadence values (LOCR-R12), failure hysteresis (LOCR-R21), registration/compaction order
(LOCR-R23), pane diagnostic authority (LOCR-R27), or cross-store post-commit work (LOCR-R28).

Verified against the uncommitted LOCR-L22 candidate (branch `ar/260831-locr-l22`, HEAD
`4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`); verification metadata stays pinned until closeout
stamps the leaf code commit.

## 260831-LOCR-R23 Current Delta — Registration Before Compaction, Now Observable

The R23 obligation is a **preservation** contract: no production byte changed for it, and the
post-batch registration-then-compaction order the `## 260821-CLIVE Register-Then-Compact Boundary`
section already recorded is the current source (cit:([`refresh`], mcp/src/agents_remember/serving/terminal_liveness.py:174-221)). What this delta changes is this
card's account of it:

1. **A stale sentence is corrected, not overridden.** The `### 260707-HFX2-L12 CS-6 Update` section
   above said the sweeper "runs catalog compaction inside the batch". It does not: the batch
   (`cit:([`batch`], mcp/src/agents_remember/serving/terminal_liveness.py:193-199)`) covers only the observation phase, and the terminated-row
   read, the registrar callback and `compact` all run after the commit. That sentence now carries the
   current contract in the body rather than a later block superseding it.
2. **The registration stage is now a documented stage, not an implication.** `refresh` enumerates
   terminated rows with `include_terminated=True` (cit:([`list`], mcp/src/agents_remember/serving/terminal_catalog.py:80-84)), offers that
   set to `register_execution_evidence` (cit:([`register_execution_evidence`], mcp/src/agents_remember/serving/terminal_liveness.py:140-142)), and passes
   **only the returned proved-id set** to `compact(...)` (cit:([`compact`], mcp/src/agents_remember/serving/terminal_catalog.py:315-345)). The
   production registrar really is partial: `register_terminal_catalog_execution_evidence` adds an id
   only when every registration result reports `durable_or_irrelevant`
   (cit:([`register_terminal_catalog_execution_evidence`], mcp/src/agents_remember/application/task_docs/task_execution_registration.py:353-389)).
3. **The fail-closed default is named.** With no registrar injected, `refresh` supplies `frozenset()` —
   never an assumed registration — so a task-bound worker/curator/leaf-reviewer row is retained by the
   catalog's reclamation predicate (cit:([`_leaf_execution_entry`], mcp/src/agents_remember/serving/terminal_catalog.py:52-62)) until its id is explicitly
   proved. The app wires the registrar through `TerminalLivenessActions`
   (cit:([`create_app`], mcp/src/agents_remember/serving/app.py:253-314)).
4. **The fast path is stated as an exclusion.** `_refresh_starting_rows` registers nothing and compacts
   nothing (cit:([`_refresh_starting_rows`], mcp/src/agents_remember/serving/terminal_liveness.py:223-268)); both remain full-sweep
   responsibilities.
5. **The order is now pinned where it happens.** `mcp/tests/test_terminal_liveness_registration_order.py`
   records the enumeration itself — the traced `TerminalCatalog.list` emits an event carrying the
   batch-commit state observed at the read — and asserts the chain
   `batch-enter → batch-exit → enumerate[include_terminated=True, batch=closed] → register → compact`.
   That module is ordinary version-controlled test source, **not** a governed evidence artifact
   (`governed_artifact_paths` returns `False` for it), so it needs no evidence-lifecycle registration.

Not owned here: evidence identity (`LOCR-R10`), retention-period values, workspace-river compaction, and
the evidence-lifecycle registration of the new test (all excluded by the requirement packet).

## 260831-LOCR-R02 Current Delta — The GET Route Is No Longer A Sweeper Caller

`260831-LOCR-L02` removed the terminal-session GET route's call to
`runtime.liveness_sweeper.refresh()`: `api_terminal_sessions` now serializes `runtime.catalog.list()`
and the route module names no sweeper. Nothing inside `terminal_liveness.py` changed — this is a
correction of *who calls the sweeper*, so this card's account of the caller moves and the module's
own contract does not.

Three sentences in this card said the route was a caller; all three are corrected in the body rather
than left for a later block to override:

1. **The `## Purpose` paragraph** said `observe_terminal_liveness` is the shared path "that the
   sessions endpoint, WebSocket attach, and server-side paste all route through". The sessions
   endpoint is no longer among them; WebSocket attach (`_app_common.py:363`), the live-paste target
   (`_app_terminal_routes.py:429-440`), and the harness-control routes (`harness_control_api.py:651`)
   are.
2. **The `## Repo-Internal References` app-wiring row** said "one sweeper behind
   `GET /api/terminal/sessions`". The sweeper's steady-state driver is the serving lifespan's
   observation loop; the GET route is not a caller.
3. **The `## 260831-LOCR-L22 Current Delta` contention note** described a contended `refresh()` as
   "the `GET /api/terminal/sessions` path". That was true when written and is now historical; the
   sentence states the current callers and keeps the L22 contract itself (the contention read, the
   admission-before-list ordering, the final-only projection) unchanged.

`refresh()`'s own behaviour is preserved exactly: rate-limited to ≤1 full probe sweep per 10s,
non-overlapping, the bounded one-second starting-row fast path, the committed-snapshot contention
read, one dirty-gated catalog batch per admitted path, and the post-batch registration-then-compaction
order. Those are owned by LOCR-R12/R21/R22/R23/R27 and are untouched here. This leaf also does **not**
decide the notifier's pre-existing inline refresh, which remains a second recurring caller.
