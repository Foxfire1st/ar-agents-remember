# mcp/src/agents_remember/serving/daemon_identity.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves which dashboard process answers on a host and port, which build it serves and which settings file it runs with, so the dashboard supervisor and the settings report act on the real listener instead of a saved PID.

## Code Commentary

`observe_dashboard(host, port)` returns `None` when no product dashboard process owns a listening socket on that address, otherwise a `DashboardIdentity` (`pid`, `build`, `config_path`, `currentness`):

- The socket owner comes from `daemon_processes.listening_dashboard_pid` (wildcard hosts are probed through loopback). It is read before and after the HTTP read, and the two must be the same process.
- The HTTP read is `GET /api/state?status=true`. Its `servingProcessId`, when present, must equal the socket owner; its `servingBuild` and `buildCurrentness` become the identity's build and currentness. A timeout or a 503 (a starting or hung handler) leaves `build` and `currentness` empty but keeps the proven owner.
- `config_path` is the argument after `--config` in the owner's command line, or empty.
- Any inspection failure (OS error, malformed answer, a mismatch between answer and owner, an unsupported platform) raises `ConfigError("dashboard identity is unknown: …")`. Callers treat that as unknown, never as permission to signal.

`dashboard_coordination_root(identity)` reads the `coordinationRoot` of the owner's settings file and requires it to be absolute; a missing `--config` or unreadable settings is a `ConfigError`. `require_dashboard_root(identity, expected_root)` refuses a dashboard of another coordination root with a message that names its settings file and says no signal is authorized. `serving/daemon.py` uses both before adopting, restarting or stopping; `cli/settings_provenance.py` uses the root to compare a run's settings with the dashboard's.

## Evidence

- The socket owner is read twice around the HTTP answer and must match its `servingProcessId`. [1]
- A timeout or 503 keeps the owner without a build. [2]
- The owner's settings must declare an absolute coordination root. [3]
- A dashboard of another root is refused with no signal authorized. [4]
