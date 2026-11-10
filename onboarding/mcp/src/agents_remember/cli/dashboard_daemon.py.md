# mcp/src/agents_remember/cli/dashboard_daemon.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

The command adapter behind `agents-remember dashboard --status`, `--stop` and `--daemon`: it dispatches each to the dashboard daemon supervisor in `serving/daemon.py`, prints what it observed and turns the outcome into the exit code.

## Code Commentary

`run_daemon_command` refuses `--sim` and `--reload` with these flags (exit 1). The host observe and host start callables are injected by `cli/dashboard.py`.

- **Status** probes the dashboard at the recorded endpoint and at the requested host and port. The dashboard is identified by the process that answers on the port, and a recorded state that names another process is corrected by the probe. Unknown ownership prints `dashboard daemon identity is unknown` and counts as not running. A running dashboard prints its pid, URL, version and log, then one build line from the build currentness the dashboard reports (mode, state, loaded and installed digests, first-seen time, reason and remedy), or `unknown` with the loaded digest when it reports none, then the best-effort background-work totals from `/api/diagnostics/background`. A diagnostics failure prints one unavailable line and changes no exit code. The host line follows. Exit 1 when the dashboard is not running, otherwise 0 when the host is ready and 3 when it is not.
- **Stop** prints the supervisor's result. It exits 0 for `not-running`, `stopped` or `killed` and 1 otherwise, including when the dashboard's identity is unknown and no signal is sent.
- **Daemon** runs `ensure` for the requested endpoint and cadence, which adopts a dashboard whose version, host, port and Python source digest match and restarts or starts one otherwise. It then starts the host. An `adopted` or `unknown` outcome (the installed digest could not be computed) records the host line in the daemon state. Exit 1 for any outcome other than `adopted`, `started`, `restarted` or `unknown`, otherwise 0 when the host is ready and 3 when it is not.

The adapter never installs or upgrades a host, and stopping the dashboard leaves host sessions running.

## Evidence

- Status, stop and daemon dispatch with their exit codes. [1]
- The status build line from the dashboard's reported currentness. [2]
- Background-work totals are best effort and never change the exit code. [3]
- The probe identifies the dashboard by the answering process and rewrites a mismatched record. [4]
- Adoption compares version, host, port and source digest; an uncomputable installed digest answers `unknown`. [5]
