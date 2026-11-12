# mcp/tests/test_dashboard_build_currentness.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that dashboard supervision follows the process and code actually answering the dashboard port, not the saved daemon record: which process may be signalled, when a running dashboard is adopted or restarted, and how its build currentness reaches status output and the browser.

## Code Commentary

`_state` writes a saved `DaemonState` for a coordination root, `_identity` turns it into the `DashboardIdentity` a port observation returns, and `_unresponsive_owner` simulates a listener that owns the port with a dashboard command line but does not answer HTTP. The cases drive `serving.daemon`, `serving.daemon_identity`, `serving.daemon_processes` and `cli.dashboard_daemon` with patched process, socket and HTTP observations; no real dashboard starts.

- **Identity before signal.** A saved pid is repaired from the actual listener before a stop, and only that pid is signalled; a saved pid nobody proves is never signalled. The served build and pid must match the process owning the socket, or observation refuses as not the same process. A listener for a foreign coordination root, a changed or absent owner, or a native lookup error (`lsof` missing, not permitted, timed out) yields a refusal or `identity-unknown` with no signal and the saved record unchanged; another settings file for the same root is adopted.
- **Restart and adoption.** With an equal version, a changed source digest restarts the dashboard and matching bytes adopt it without a second spawn; a failed stop keeps the stale identity and reports failure without spawning; an uncomputable installed digest answers `unknown` and touches nothing. A runtime preview reports `would-restart` against the observed process without rewriting the saved state. An unresponsive same-root owner can be stopped and replaced, but its liveness never proves a new child ready.
- **Process lookup.** On Linux the listener is found by socket inode and a dashboard command line; on macOS by `lsof` and `sysctl` arguments, which keep spaces and empty arguments and support adoption, readiness and stop.
- **Load-independent waits.** Readiness waits use the suite's hang guard or a fake clock, never a short wall-clock bound.
- **Currentness delivery.** Status prints the served build-currentness line with its first-seen time on every run, and an unchanged projection poll or an open status stream reports a newly stale build: the state answer changes its ETag and the stream emits a `buildCurrentness` event.

## Evidence

- A saved pid is repaired from the actual listener and only that pid is stopped. [1]
- An unproven saved pid is never signalled. [2]
- A changed digest at an equal version restarts once and matching bytes adopt. [3]
- A failed stop keeps the stale identity and an unknown digest acts on nothing. [4]
- A runtime preview does not repair the saved state. [5]
- The HTTP build and the socket owner must be the same process. [6]
- An unresponsive same-root owner can be stopped and replaced. [7]
- A foreign, changed or absent owner is not signalled. [8]
- Repeated status prints the served first-seen time. [9]

- An unresponsive owner does not prove a new child ready; its one-second bound runs on the fake clock. [10]

- The Linux listener lookup checks the socket inode and the dashboard command. [11]
- A foreign-root listener is neither adopted nor signalled. [12]
- macOS process arguments keep spaces and empty arguments. [13]

- The macOS owner supports adoption, readiness and stop; its readiness waits use the hang guard. [14]

- Native identity errors are unknown and never signal. [15]
- An unchanged projection poll and an open stream observe a newly stale build. [16]

- The macOS adoption readiness waits run under the suite's hang guard, and the unresponsive-owner case's one-second bound runs on a fake clock, so neither depends on machine load. [17]
