# mcp/src/agents_remember/serving/paseo/paseo_daemon.py

## Governing Overview

[overview](../overview.md)

## Purpose

Reports and stops the configured home daemon through its own CLI boundary.

## Code Commentary

runtime_status reports version, daemon, owned plugin and embed state. stop_runtime inspects the home process record before asking the home-addressed CLI to stop; no AR code selects a process by listen port or signals one directly. A foreign/unreadable record remains a named refusal instead of permission to stop another home.

L96: the module moved from `cli/paseo_daemon.py` into `serving/paseo/`. Stop now runs under the bounded home lock shared with install and start, and its named-remedy text comes from `paseo_remedy`.

`runtime_status` includes the expected contract Node and observed owned executable. A mismatch reports `restartRequired=["node"]` with the existing explicit terminal provision remedy. Observation leaves the running host and its files unchanged.

## Evidence

- The status/stop boundary and its home record proof. [1]

- Public Paseo status includes the Node restart reason and remedy. [2]
