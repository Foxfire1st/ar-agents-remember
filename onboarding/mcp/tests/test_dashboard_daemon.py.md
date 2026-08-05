# test_dashboard_daemon.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_dashboard_daemon.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T20:24+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Unit tests for `serving/daemon.py` and its CLI dispatch (260703 L2): daemon state,
liveness probes, stop escalation, the `ensure` decision matrix, the MCP autostart
hook, and `--daemon`/`--status`/`--stop` wiring.

## Code Commentary

Helpers: `make_config(root, auto_start=…, port=…)` builds a real `McpRuntimeConfig`
directly (tmp coordination root); `make_state(**overrides)` builds `DaemonState`
fixtures; `_spawn_sleeper(ignore_term=…)` launches a real python child that prints
`ready` **after** installing (or not) a SIGTERM ignore handler — reading that line
before signalling removes the classic install-race flake; the handshake pipe is then
closed by the helper itself, since the caller keeps the `Popen` only for its pid and an
open read end would otherwise be finalised by GC. `_write_settings` writes a
minimal real settings JSON for CLI dispatch tests.

- `StateFileTests` — round-trip equality, camelCase JSON keys, no `.tmp` residue,
  missing/malformed/non-dict/missing-key all read as `None`, idempotent clear.
- `ProbeTests` — no state; a really-exited child pid; a live-but-foreign pid (probe
  seam patched False: pid-reuse safety); a live dashboard (both seams patched True).
- `StopTests` — not-running; stale-state clear; real cooperative child → `stopped`;
  real TERM-ignoring child → `killed`. Test children are registered into
  `daemon._spawned` so `_wait_gone`'s reaping collects them (the test process is the
  parent; without reaping a dead child would zombie and read as alive).
- `SpawnTests` — `subprocess.Popen` mocked: asserts the module-string command shape
  (`-m agents_remember.cli dashboard --config … --port … --interval … --no-access-log`),
  `start_new_session=True`, immediate state write, and per-spawn log rotation. 260712-PTS-L3
  adds the `--heartbeat` plumbing pair: the default spawn asserts `--heartbeat` is NOT in the
  child argv (the child uses the serving default), and
  `test_spawn_forwards_an_explicit_heartbeat_to_the_child` asserts
  `cadence=ProjectionCadence(heartbeat=20.0)` rides as `--heartbeat 20.0` before
  `--no-access-log`. Every call is `daemon.spawn(config, DaemonEndpoint(host=…, port=…,
  version=…), cadence=…)` — host/port/version travel as one endpoint value.
- `EnsureTests` — the decision matrix with `spawn`/`stop`/`probe`/`_wait_ready`
  patched: absent→`started`, healthy-match→`adopted` (no spawn), version-mismatch and
  port-mismatch→`restarted` (stop then spawn), child-death→`failed`+state cleared,
  slow-start→`failed`+state kept, and a really-held flock→`lock-held` (no spawn). `daemon.ensure`
  likewise takes the endpoint positionally, and the absent→`started` case pins the full spawn call
  shape — `spawn(config, DaemonEndpoint(host=…, port=…, version=…),
  cadence=ProjectionCadence(interval=1.0, heartbeat=None))` — including the PTS-L3 `heartbeat=None`
  pass-through.
- `AutostartTests` — off→no-op (ensure never called); on→a joined worker thread that
  called `ensure` with the settings port and reported to captured stderr; an ensure
  exception is swallowed and reported (`failed: …`), never raised.
- `CliDaemonDispatchTests` — real parser + real settings file, `serving_daemon.*`
  patched: `--status` exit 0/1, `--stop` reporting, `--daemon` using the settings
  port by default with explicit `--port` winning (both read off the positional
  `DaemonEndpoint` as `ensure.call_args.args[1].port`), failure exit 1, `--daemon --sim`
  rejected, and `--status`/`--stop` mutual exclusion (SystemExit).

## Invariants And Boundaries

- Real-child tests must register children in `daemon._spawned` (zombie reaping) and
  always clean up via `addCleanup` kill/wait.
- The flock test holds the real lock on a second fd — flock conflicts are per open
  file description, so single-process testing is sound.
- CLI tests never bind ports or spawn servers; everything behind `ensure`/`stop`/
  `probe` is patched at the daemon module.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `ensure` | mcp/src/agents_remember/serving/daemon.py:264-290 |
| The CLI wiring under test. | `_run_daemon_command` | mcp/src/agents_remember/cli/dashboard.py:270-297 |
| The `dashboard` settings key parsing (companion tests live in test_config.py). | `parse_dashboard_settings` | mcp/src/agents_remember/mcp/config.py:437-453 |

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 6 citation findings. Re-anchored the
  three rows with exact spans: the module under test (`ensure`, daemon.py:264-292), the CLI wiring
  (`_run_daemon_command`, cli/dashboard.py:270-297), and the settings parsing
  (`parse_dashboard_settings`, config.py:437-455). Scoped recheck clean.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: `daemon.spawn` and `daemon.ensure` now take a
  positional `DaemonEndpoint(host, port, version)` plus an optional
  `cadence=ProjectionCadence(interval, heartbeat)`, so the pinned `spawn.assert_called_once_with`
  shape, the explicit-heartbeat assertion, and the CLI port assertions (`call_args.args[1].port`)
  all changed; updated the `SpawnTests`, `EnsureTests`, and `CliDaemonDispatchTests` bullets to the
  new call shapes. Also recorded that `_spawn_sleeper` now closes the handshake pipe after reading
  `ready`. The 33 test cases and the decision matrix they pin are otherwise unchanged.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: `SpawnTests` pins heartbeat argv plumbing (omitted by
  default, `--heartbeat 20.0` when explicit) and `EnsureTests` pins the `heartbeat=None`
  pass-through on the started path — the ensure-adopts-without-cadence-comparison behaviour that
  makes adaptive pacing reach a live daemon only via explicit stop + spawn is unchanged and
  documented in the daemon sidecar. Verification metadata pinned until closeout stamps the PTS-L3
  commit.
- 2026-07-03T11:40+02:00 — Created for 260703 L2 alongside `serving/daemon.py` (32 tests across
  state/probe/stop/spawn/ensure/autostart/CLI-dispatch). Verification metadata pinned until
  closeout stamps the code commit.
