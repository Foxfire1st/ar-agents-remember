# test_dashboard_daemon.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_dashboard_daemon.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-03T11:40+02:00                           |
| lastVerifiedCommitHash | `66af2a722e20e291163e280371b3f42cd920966e`       |
| lastVerifiedCommitDate | 2026-07-03T11:34:31+02:00|
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
before signalling removes the classic install-race flake. `_write_settings` writes a
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
  `start_new_session=True`, immediate state write, and per-spawn log rotation.
- `EnsureTests` — the decision matrix with `spawn`/`stop`/`probe`/`_wait_ready`
  patched: absent→`started`, healthy-match→`adopted` (no spawn), version-mismatch and
  port-mismatch→`restarted` (stop then spawn), child-death→`failed`+state cleared,
  slow-start→`failed`+state kept, and a really-held flock→`lock-held` (no spawn).
- `AutostartTests` — off→no-op (ensure never called); on→a joined worker thread that
  called `ensure` with the settings port and reported to captured stderr; an ensure
  exception is swallowed and reported (`failed: …`), never raised.
- `CliDaemonDispatchTests` — real parser + real settings file, `serving_daemon.*`
  patched: `--status` exit 0/1, `--stop` reporting, `--daemon` using the settings
  port by default with explicit `--port` winning, failure exit 1, `--daemon --sim`
  rejected, and `--status`/`--stop` mutual exclusion (SystemExit).

## Invariants And Boundaries

- Real-child tests must register children in `daemon._spawned` (zombie reaping) and
  always clean up via `addCleanup` kill/wait.
- The flock test holds the real lock on a second fd — flock conflicts are per open
  file description, so single-process testing is sound.
- CLI tests never bind ports or spawn servers; everything behind `ensure`/`stop`/
  `probe` is patched at the daemon module.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The module under test. | [serving/daemon.py](agents-remember/mcp/src/agents_remember/serving/daemon.py) |
| The CLI wiring under test. | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |
| The `dashboard` settings key parsing (companion tests live in test_config.py). | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-07-03T11:40+02:00 — Created for 260703 L2 alongside `serving/daemon.py` (32 tests across
  state/probe/stop/spawn/ensure/autostart/CLI-dispatch). Verification metadata pinned until
  closeout stamps the code commit.
