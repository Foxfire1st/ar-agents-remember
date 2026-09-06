# mcp/src/agents_remember/serving/daemon.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/daemon.py`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T20:24+02:00                           |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`       |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

`serving/daemon.py` is the dashboard daemon supervisor (260703 L2): it lets the
cockpit outlive the terminal that started it. `agents-remember dashboard --daemon`
and the MCP server's `dashboard.autoStart` settings key both funnel into one
decision function, `ensure()` — adopt a healthy daemon, spawn a missing one,
restart on version/host/port mismatch (developer decision: a stale dashboard is
worse than a restart blip).

## Code Commentary

State lives under `<coordinationRoot>/logs/dashboard/`:

- `daemon.json` (`STATE_FILE_NAME`) — a `DaemonState` (pid, host, port, version,
  config_path, log_path, started_at; camelCase JSON keys) written atomically
  (tmp + `os.replace`) and **immediately after `Popen`**, so a supervisor dying
  mid-ensure never strands an unrecorded child. `read_state` returns `None` for
  missing/malformed/wrong-shape files.
- `dashboard.log` (`LOG_FILE_NAME`) — the child's stdio, rotated to `.log.1` per
  spawn (`_rotate_log`, best-effort); the child serves with `--no-access-log` so
  per-request noise never grows it.
- `ensure.lock` (`LOCK_FILE_NAME`) — one non-blocking `fcntl.flock` making
  concurrent MCP boots race-safe: losers return `EnsureResult(action="lock-held")`
  and skip; they never double-spawn.

`spawn(config, *, host, port, version, interval=1.0, heartbeat=None)` launches the plain
foreground CLI **by module string** (`sys.executable -m agents_remember.cli
dashboard --config <config.config_path> --host … --port … --interval …
--no-access-log`) with `start_new_session=True`, stdio to the log, cwd at the
daemon dir. **260712-PTS-L3:** an explicit `heartbeat` adds `--heartbeat <value>`
to the child argv before `--no-access-log`; `None` omits the flag so the child
uses the serving default (15s). Spawned `Popen` handles are kept in `_spawned` so a long-lived
supervisor reaps exited children (`_reap_spawned`) instead of leaving zombies.

Liveness (`probe` → `_state_alive`) is `kill(pid, 0)` (`_pid_alive`) **plus** a
`/proc/<pid>/cmdline` marker probe (`_pid_is_dashboard`: must contain
`dashboard` and an `agents_remember`/`agents-remember` marker) — pid reuse
across reboots must not resurrect a foreign process, and a zombie's empty
cmdline fails the probe too. Without procfs (e.g. macOS) the kill-probe alone
decides.

`stop(directory, timeout=10)` is TERM → bounded `_wait_gone` → KILL fallback,
returning `not-running` | `stopped` | `killed`; the state file is cleared in
every branch. `ensure(...)` compares a live daemon's version/port/host against
the request: full match → `adopted`; mismatch → `stop` + `spawn` → `restarted`;
absent → `spawn` → `started`. After a spawn, `_wait_ready` requires the child to
both **stay alive and accept TCP** before success; a dead child clears state and
reports the log tail, a slow one keeps state with a "may still be starting"
detail (`failed` either way). `interval` / `heartbeat` reach the child only on
spawn/restart; an adopted daemon keeps the cadences it was started with.
**Deployment note (260712-PTS-L3):** because `ensure` adopts a healthy daemon
without comparing cadence flags, the adaptive change-driven pacing (or a new
`--heartbeat` value) reaches an already-running daemon only via an explicit
stop + spawn — a pre-PTS-L3 daemon keeps fixed 1s ticking until restarted.

`maybe_autostart_dashboard(config)` is the MCP boot hook: a no-op unless
`config.dashboard.auto_start`, otherwise a **daemon thread** runs `ensure(host=
"127.0.0.1", port=config.dashboard.port)`. It is total (catches everything) and
its only output goes to **stderr** — over stdio transport, stdout IS the MCP
protocol.

## Invariants And Boundaries

- **Import-light by design:** stdlib + `mcp.config` types + `SERVER_VERSION`
  only — never uvicorn/FastAPI/the serving app. The child is addressed by module
  string, never imported, so `mcp/server.py` can call the boot hook without
  pulling the serving stack into MCP startup.
- **The boot hook must never block or break the MCP handshake** — threaded,
  total, stderr-only.
- **State file writes are atomic and pre-readiness**; readers never see a torn
  file, and a mid-ensure crash leaves a findable record.
- **Liveness requires identity**, not just a live pid (reboot/pid-reuse safety).
- One `ensure` at a time per coordination root (flock); `lock-held` is a skip,
  not an error.
- `version` defaults to `SERVER_VERSION` (installed package metadata) — the
  mismatch comparator that makes an upgrade restart the daemon on next boot.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CLI dispatch (`--daemon`/`--status`/`--stop`) and the `--no-access-log` child flag. | `add_arguments` | mcp/src/agents_remember/cli/dashboard.py:84-158 |
| The `dashboard` settings key (`DashboardSettings`: autoStart, port) it consumes. | `DashboardSettings` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:90-95 |
| The MCP boot seam calling `maybe_autostart_dashboard`. | `maybe_autostart_dashboard` | mcp/src/agents_remember/serving/daemon.py:336-356 |
| The version comparator (`SERVER_VERSION`, kernel-owned since L9). | "agents-remember-mcp" | mcp/src/agents_remember/kernel/primitives/version.py:18-18 |


## 260731-EFA-L2 Current Delta

Two named concepts replaced five loose arguments on the daemon ensure/spawn path:

- **`DaemonEndpoint`** (`host`, `port`, `version`, defaulting to `SERVER_VERSION`) — *which daemon
  this is*: where it serves and which build it runs. Adoption is exactly an equality check on these
  three (`_describe_mismatch`); a daemon matching two of them is still the wrong daemon, so they are
  compared, recorded and passed as one value.
- **`ProjectionCadence`** (from the new stdlib-only [cadence.py](cadence.py.md)) replaces the
  `interval` / `heartbeat` pair. It is imported here precisely *because* that module pulls in
  nothing from the serving stack: the supervisor can name the cadence it hands a spawned child
  without importing the projector.

The spawn argv is built the same way (`--heartbeat` still appended only when set), and the
documented rule is unchanged: the cadence reaches the child only when this call spawns or restarts
it — an **adopted** daemon keeps the cadences it was started with.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-12T10:20+02:00 — Citation maintenance only: widened the kernel version-comparator
  reference to the named metadata/fallback resolver introduced by the rc7 leaf; daemon behavior
  is unchanged. Verification metadata remains pinned until closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 5 citation entries (10 findings); no Tier-3 findings.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `DaemonEndpoint` and the `ProjectionCadence` import from the new stdlib-only cadence module; adoption-equality rule unchanged.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: `spawn`/`ensure`/`_ensure_locked` gained
  `heartbeat: float | None = None` — an explicit value rides the child argv as `--heartbeat`,
  `None` omits the flag (serving default 15s). Like `interval`, it reaches the child only on
  spawn/restart: `ensure` adopts healthy daemons without cadence comparison, so adaptive pacing
  reaches a live daemon only via explicit stop + spawn. Verification metadata pinned until
  closeout stamps the PTS-L3 commit.
- 2026-07-03T11:40+02:00 — Created for 260703 L2 (daemon mode + MCP auto-start): pidfile store,
  identity-checked liveness, detached spawn via module string, TERM→KILL stop, the flock-guarded
  `ensure` decision function (adopt/start/restart), and the total, threaded, stderr-only
  `maybe_autostart_dashboard` boot hook. Verification metadata pinned until closeout stamps the
  code commit.
