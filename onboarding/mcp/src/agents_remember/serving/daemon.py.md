# mcp/src/agents_remember/serving/daemon.py

## Governing Overview

[overview](overview.md)

## Purpose

`serving/daemon.py` is the dashboard daemon supervisor: it lets the
cockpit outlive the terminal that started it. `agents-remember dashboard --daemon`
and the MCP server's `dashboard.autoStart` settings key both funnel into one
decision function, `ensure()` — adopt a healthy daemon, spawn a missing one,
restart on Python source digest/version/host/port mismatch (developer decision: a stale dashboard is
worse than a restart blip). `runtime_install` reaches the same decision through
`ensure_running_dashboard`, so an install restarts a running dashboard on a build change.

## Code Commentary

State lives under `<coordinationRoot>/logs/dashboard/`:

- `daemon.json` (`STATE_FILE_NAME`) — a `DaemonState` (pid, host, port, version,
  source_digest, config_path, log_path, started_at; camelCase JSON keys) written atomically
  (tmp + `os.replace`) and **immediately after `Popen`**, so a supervisor dying
  mid-ensure never strands an unrecorded child. `read_state` returns `None` for
  missing/malformed/wrong-shape files. `probe` rewrites the file from the dashboard that
  actually answers on the port whenever the saved identity differs.
- `dashboard.log` (`LOG_FILE_NAME`) — the child's stdio, rotated to `.log.1` per
  spawn (`_rotate_log`, best-effort); the child serves with `--no-access-log` so
  per-request noise never grows it.
- `ensure.lock` (`LOCK_FILE_NAME`) — one non-blocking `fcntl.flock` making
  concurrent MCP boots race-safe: losers return `EnsureResult(action="lock-held")`
  and skip; they never double-spawn.

`spawn(config, endpoint, *, cadence=DEFAULT_PROJECTION_CADENCE)` launches the plain
foreground CLI **by module string** (`sys.executable -m agents_remember.cli
dashboard --config <config.config_path> --host … --port … --interval …
--no-access-log --host-start-owner <supervisor pid>`) with `start_new_session=True`, stdio to the log, cwd at the
daemon dir, and records the endpoint's source digest. An explicit cadence heartbeat adds `--heartbeat <value>`
to the child argv before `--no-access-log`; `None` omits the flag so the child
uses the serving default (15s). Spawned `Popen` handles are kept in `_spawned` so a long-lived
supervisor reaps exited children (`_reap_spawned`) instead of leaving zombies.

Identity comes from what answers on the port, not from the saved PID. `probe` → `_observed_state`
asks `daemon_identity.observe_dashboard` for the saved and the requested endpoint: the native
socket owner (`daemon_processes`) must be a product dashboard process, its
`/api/state?status=true` answer must name that owner as `servingProcessId`, and
`require_dashboard_root` requires the owner's `--config` to declare this coordination root.
Liveness (`_state_alive`) is `kill(pid, 0)` (`_pid_alive`) **plus** a command line naming the
product dashboard (`dashboard` and an `agents_remember`/`agents-remember` marker) — PID reuse and
zombies cannot resurrect a foreign process. An identity that cannot be proved, including on a
platform with no native socket inspection, raises `ConfigError` and authorizes no signal.

`stop(directory, timeout=10)` is TERM → bounded `_wait_gone` → KILL fallback,
returning `not-running` | `stopped` | `killed`, each clearing the state file; an unprovable
identity returns `identity-unknown: …`, sends no signal and keeps the record. `ensure(...)`
compares a live daemon's version, port, host and Python source digest against the endpoint,
whose digest is the one installed now under this process's package root:
full match → `adopted`; an installed digest that cannot be computed → `unknown`, no restart;
mismatch → `stop` + `spawn` → `restarted`, or `failed` naming the stale pid when it still
serves after the stop; absent → `spawn` → `started`; an unprovable identity → `failed`.
After a spawn, `_wait_ready` requires the child to stay alive and to answer on its port as
itself — the observed socket owner is the spawned pid and its served build carries the
recorded digest and version — before success; a dead child clears state and
reports the log tail, a slow one keeps state with a "may still be starting"
detail (`failed` either way). `interval` / `heartbeat` reach the child only on
spawn/restart; an adopted daemon keeps the cadences it was started with.
**Deployment note:** because `ensure` adopts a healthy daemon
without comparing cadence flags, the adaptive change-driven pacing (or a new
`--heartbeat` value) reaches an already-running daemon only via an explicit
stop + spawn.

`plan_running_dashboard(config)` is the read-only install preview: it returns `None` when no
dashboard answers, otherwise `would-adopt`, `would-restart` with the mismatch, `unknown` or
`failed`. `ensure_running_dashboard(config)` is what a real `runtime_install` runs: a running
dashboard goes through `ensure` on its own host and port, an absent one stays stopped (`None`),
and an error is `failed` with the restart remedy.

`maybe_autostart_dashboard(config)` is the MCP boot hook: a no-op unless
`config.dashboard.auto_start`, otherwise a **daemon thread** runs `ensure(config,
DaemonEndpoint(host="127.0.0.1", port=config.dashboard.port))`. It is total (catches everything) and
its only output goes to **stderr** — over stdio transport, stdout IS the MCP
protocol.

## Invariants And Boundaries

- **Import-light by design:** never uvicorn/FastAPI/the serving app. The build-currentness,
  identity and process helpers it imports carry no web dependency. The child is addressed by module
  string, never imported, so `mcp/server.py` can call the boot hook without
  pulling the serving stack into MCP startup.
- **The boot hook must never block or break the MCP handshake** — threaded,
  total, stderr-only.
- **State file writes are atomic and pre-readiness**; readers never see a torn
  file, and a mid-ensure crash leaves a findable record.
- **Liveness requires identity**, not just a live pid (reboot/pid-reuse safety). A saved PID
  never authorizes a signal by itself, and a dashboard of another coordination root on the port
  is refused, never stopped.
- One `ensure` at a time per coordination root (flock); `lock-held` is a skip,
  not an error.
- `DaemonEndpoint.version` is read from installed package metadata and `source_digest` is the
  installed Python source digest, both when the endpoint is built — the comparators that make an
  install (through `runtime_install`) or the next boot restart the daemon.

## Evidence

### Repo-Internal References

- CLI dispatch (`--daemon`/`--status`/`--stop`) and the `--no-access-log` child flag. [1]

- The `dashboard` settings key (`DashboardSettings`: autoStart, port) it consumes. [2]
- The MCP boot seam calling `maybe_autostart_dashboard`. [3]

- The version comparator is resolved from installed package metadata. [4]


- The endpoint carries the installed version and Python source digest. [7]
- `probe` observes the answering dashboard, checks its root and repairs a mismatched saved record. [8]
- The install preview and the install-time ensure of a running dashboard. [9]
- An unprovable identity stops nothing and keeps the record. [10]
- Adoption also requires the installed digest; an unknown digest restarts nothing; a stop that leaves the stale daemon serving fails. [11]
- Readiness requires the spawned pid to answer with its recorded build. [12]

## Endpoint and cadence values

Two named values carry the daemon ensure/spawn path:

- **`DaemonEndpoint`** (`host`, `port`, `version`, `source_digest`; version and digest resolved when the
  endpoint is built) — *which daemon this is*: where it serves and which build it runs. Adoption is an
  equality check on all four (`_describe_mismatch` names each difference); a daemon matching only some
  of them is still the wrong daemon, so they are compared, recorded and passed as one value.
- **`ProjectionCadence`** (from the stdlib-only [cadence.py](cadence.py.md)) carries the
  `interval` / `heartbeat` pair. It is imported here precisely *because* that module pulls in
  nothing from the serving stack: the supervisor can name the cadence it hands a spawned child
  without importing the projector.

The spawn argv appends `--heartbeat` only when set, and the cadence reaches the child only when this call spawns or restarts
it — an **adopted** daemon keeps the cadences it was started with.

## Host start, adopt and stop

`ensure` remains this module's dashboard supervision (adopt, spawn, restart). The host composition happens outside it: the MCP boot hook's `_autostart` (serving/daemon.py) and the dashboard CLI adapter (`cli/dashboard.py::_run_daemon_command` and `::_start_host_background`) call `ensure_host` from the shared host package and record the host outcome for a running daemon, while `stop` and every daemon restart path still signal only the dashboard's recorded process and never the host.

- The daemon ensure the dashboard calls. [5]

- The spawn path the host is not part of. [6]
