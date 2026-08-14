# test_terminal_liveness.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_liveness.py`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-09T19:31+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_liveness.py` (new in **260707-HFX-L5**) pins the catalog liveness hysteresis
semantics of `serving/terminal_liveness.py` + the liveness transitions in
`serving/terminal_catalog.py` and the stderr-aware probe classification in
`serving/terminal.py`. It is the regression net against the false-dead-fleet failure mode: a
transient tmux command-failure storm must never mass-exit live sessions, and a false exit must
self-heal. **260707-HFX2-L11** extends the regression net to a second failure mode: landed rows
must cost the sweeper nothing per-row, at any fleet size, since they now accumulate by design.

## Code Commentary

### 260707-HFX2-L12 CS-6 Update

The terminal-liveness scaling regression now counts true disk reads/writes separately from in-memory batch operations and proves landed-row-heavy sweeps still perform one disk read and one disk write regardless of catalog size.

### Logic

Helpers: `_entry(session_id)` builds a running harness `TerminalCatalogEntry` with deterministic
timestamps; `_Clock` is a dataclass fake clock (`__call__` returns `moment`, `advance(seconds)`
steps it) injected as the sweeper's `now`, so every case is sleepless. Two fake hosts: `_FakeHost`
returns a canned `TmuxProbeResult` (with optional `entered`/`release` threading events for the
overlap case, and a `calls` counter for the rate-limit case); `_TmuxSubprocessProbeHost` calls the
**real production classifier** `_tmux_probe_session` with `subprocess.run` mocked — the stderr
cases bite the shipping classification, not a fake.

`TerminalCatalogLivenessTests` builds a temp-dir `TerminalCatalog` per case; `_sweeper(...)`,
`_snapshot_sweeper(...)`, and `_control_sweeper(...)` construct a
`TerminalCatalogLivenessSweeper` with one `probe=LivenessProbe(...)` argument carrying the
hysteresis config plus the injected doubles — `hysteresis=TerminalCatalogLivenessConfig(threshold
3 / window 5s / pane-gone 1 / interval 0 unless overridden)`, and where a case needs them,
`pane_capturer=` and `snapshot_reader=`. Only `now=self.clock` stays a loose keyword. Cases:

- `test_transient_failure_storm_leaves_sessions_running_until_window_elapsed` — 14 sessions,
  `tmux-command-failed` on every probe, 3 sweeps over 3 seconds: all rows stay `running` with
  `liveness_failures == 3` (the count is met but the 5s window is not — no mass exit).
- `test_pane_gone_evidence_marks_exited_without_command_failure_window` — one `pane-gone` probe
  marks `exited` immediately with `exit_evidence == "pane-gone"` (definitive evidence, threshold 1,
  zero window).
- `test_non_missing_tmux_nonzero_stderr_uses_hysteresis` (L5R2) — a nonzero tmux exit with stderr
  `error connecting to tmux server` classifies `tmux-command-failed`: the row stays `running`,
  `liveness_evidence == "tmux-command-failed"`, no `exit_evidence`.
- `test_missing_session_stderr_uses_pane_gone_behavior` (L5R2) — stderr
  `can't find session: ar-gone` classifies `pane-gone` and marks `exited`.
- `test_alive_again_probe_clears_false_liveness_exit` — three spaced command failures exit-mark the
  row (`exit_evidence == "tmux-command-failed"`), then an alive probe on a later sweep self-heals
  it to `running` with failures cleared and `exit_evidence` gone.
- `test_fast_tick_respects_sweep_rate_limit` — with a 30s interval, three `refresh()` calls one
  second apart make exactly ONE host probe (the dashboard's 1s cadence cannot imply 1s probing).
- `test_overlapping_sweep_returns_current_catalog_without_second_probe` — a real second thread
  parks inside the host probe (via the `entered`/`release` events); the concurrent `refresh()`
  returns the current catalog with NO second probe (`calls == 1`), then the parked sweep completes
  without error.
- `test_landed_rows_do_not_add_per_row_sweep_probe_or_catalog_reads` (HFX2-L11 round-2 F1 fix) —
  a `_CountingCatalog` (subclasses `TerminalCatalog`, counts `_read()` calls) is seeded with N
  `status="landed"` rows plus one `running` row, then swept; run at N=5 and N=500 the result is
  byte-identical: exactly one host probe call, one pane capture (the running row only), and
  exactly 3 catalog `_read()` calls, regardless of how many landed rows exist. This pins
  `refresh()`'s `_observe_catalog_entry` short-circuit for `status=="landed"` (returns
  `TerminalLivenessObservation(entry=entry, alive=True)` without calling
  `observe_terminal_liveness`) as a genuinely flat-cost skip, not just a probe-count reduction —
  closing the round-1 BLOCK where landed seats were silently enrolled into the sweeper's
  per-cycle O(N) subprocess / O(N^2) catalog-read cost as they accumulated by design (the 3rd
  CS-6-class catch on this master after L7/L9).

### Conventions

Uses `unittest` and inserts `mcp/src` on `sys.path` (the suite-wide worktree pin idiom), matching
the surrounding MCP test suite. Fake clock + fake/mocked hosts keep every case sleepless and
tmux-free.

### Invariants And Boundaries

No FastAPI routes, WebSockets, or real tmux here — the app wiring is covered by
`test_terminal_ws.py`, the probe's real-subprocess integration by `test_terminal.py`, and pure
catalog JSON semantics by `test_terminal_catalog.py`. This file pins hysteresis, evidence
classification, self-heal, and sweep cadence/overlap only.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sweeper + shared observation path under test. | `TerminalCatalogLivenessSweeper`; `observe_terminal_liveness` | mcp/src/agents_remember/serving/terminal_liveness.py:97-212; mcp/src/agents_remember/serving/terminal_liveness.py:282-326 |
| The liveness transition copiers retain success-side healing and thresholded failure behavior. | `with_liveness_success`; `with_liveness_failure` | mcp/src/agents_remember/serving/terminal_catalog.py:145-145; mcp/src/agents_remember/serving/terminal_catalog.py:149-149 |
| The catalog records each probe through the success/failure transition copiers. | "def record_liveness_probe("; "updated = entry.with_liveness_success()"; "updated = entry.with_liveness_failure("; "pane_gone_failure_threshold=hysteresis.pane_gone_failure_threshold" | mcp/src/agents_remember/serving/terminal_catalog.py:128-128; mcp/src/agents_remember/serving/terminal_catalog.py:145-145; mcp/src/agents_remember/serving/terminal_catalog.py:149-149; mcp/src/agents_remember/serving/terminal_catalog.py:154-154 |
| The production observer caller drives the catalog probe on alive and failed paths. | "def observe_terminal_liveness("; "if session is not None and session.is_alive: updated = catalog.record_liveness_probe(entry.id"; "if tmux.exists: updated = catalog.record_liveness_probe(entry.id"; "updated = catalog.record_liveness_probe( entry.id"; "return TerminalLivenessObservation(entry=updated or entry" | mcp/src/agents_remember/serving/terminal_liveness.py:302-302; mcp/src/agents_remember/serving/terminal_liveness.py:318-319; mcp/src/agents_remember/serving/terminal_liveness.py:328-329; mcp/src/agents_remember/serving/terminal_liveness.py:337-338; mcp/src/agents_remember/serving/terminal_liveness.py:344-344 |
| The production stderr-aware probe classifier the `_TmuxSubprocessProbeHost` cases exercise for real. | `_tmux_missing_session_stderr`; `tmux_probe_session` | mcp/src/agents_remember/serving/terminal_tmux.py:149-176; mcp/src/agents_remember/serving/terminal_tmux.py:179-181 |
| The catalog JSON/storage unit tests this file deliberately does not duplicate. | `TerminalCatalogTests` | mcp/tests/test_terminal_catalog.py:48-516 |

## 260718-CHATS-L5I Current Delta

Liveness regressions now pin the one-second starting-row path and multi-read disconnect hysteresis separately from definitive tmux exit handling.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: rebound the production stderr-classifier
  reference to the exact terminal-tmux symbols and completed the catalog copier, probe-record, and
  observer-caller ownership chain.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  `TerminalCatalogLivenessSweeper` now takes one `probe=LivenessProbe(...)` argument in place of
  the separate `config=`, `pane_capturer=`, and `snapshot_reader=` keywords, so every sweeper
  construction in the suite changed shape. Rewrote the sentence describing the three sweeper
  builders to name `LivenessProbe`, its `hysteresis=TerminalCatalogLivenessConfig(...)` slot, and
  the two injected doubles that now ride inside it. The threshold-3 / window-5s / pane-gone-1 /
  interval values are passed unchanged, and none of the eight enumerated cases gained, lost, or
  altered an assertion.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive), round-2 F1 fix: added
  `test_landed_rows_do_not_add_per_row_sweep_probe_or_catalog_reads`, a flat-cost scaling
  regression run at 5 vs 500 `landed`-status rows plus one `running` row. Both sizes assert the
  exact same result — one host probe call (`host.calls == 1`), one pane capture (only for the
  running row), and exactly 3 `_read()` calls on the catalog — proving `refresh()` no longer
  fans out per-row tmux/catalog work across landed rows (the round-1 BLOCK: landed seats were
  silently enrolled into the sweeper's O(N)-subprocess/O(N^2)-catalog-read per-cycle cost as they
  accumulated by design — the 3rd CS-6-class catch on this master after L7/L9). Uses a new
  `_CountingCatalog` subclass to count `_read()` calls and a `status=` kwarg added to `_entry(...)`.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-07T23:45+02:00 — Created for 260707-HFX-L5 (catalog liveness hysteresis): pins the
  14-session transient command-failure storm staying `running`, pane-gone marking immediately,
  alive-again self-heal of a false exit, sweep rate limiting (1 probe across 3 fast ticks), and
  overlapping-sweep suppression (real threads + events); the L5R2 fix round added the two
  stderr-classification regressions driving the REAL `_tmux_probe_session` with `subprocess.run`
  mocked (non-missing nonzero stderr ⇒ hysteresis; missing-session stderr ⇒ pane-gone).
  Verification metadata pinned until closeout stamps the HFX-L5 commit.
