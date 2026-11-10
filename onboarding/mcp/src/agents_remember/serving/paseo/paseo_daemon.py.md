# mcp/src/agents_remember/serving/paseo/paseo_daemon.py

## Governing Overview

[overview](../overview.md)

## Purpose

Reports and stops the configured home daemon through its own CLI boundary.

## Code Commentary

runtime_status reports version, daemon, owned plugin and embed state, and the inherited harness homes of the running host. stop_runtime inspects the home process record before asking the home-addressed CLI to stop; no AR code selects a process by listen port or signals one directly. An unreadable record is a named refusal, and a record that names another home's or no Paseo supervisor is removed as stale with nothing signalled, never taken as permission to stop another home.

Stop runs under the bounded home lock shared with install and start, and its named-remedy text comes from `paseo_remedy`.

`runtime_status` includes the expected contract Node and observed owned executable. A mismatch reports `restartRequired=["node"]` with the existing explicit terminal provision remedy. Observation leaves the running host and its files unchanged.

Status and stop reach the host through `PaseoCli`'s communication Node, so a missing product Node alone does not refuse them; a missing Paseo CLI while the home holds a process record is `paseo_cli_unavailable`. `inheritedHarnessHomes` names, without values, the harness-home variables the running host took from its start environment that the settings' provider `env` does not carry, with `harnessHomeRemedy` to move them there; a home without a running daemon reports an empty list.

## Evidence

- The status/stop boundary and its home record proof. [1]

- Public Paseo status includes the Node restart reason and remedy. [2]

- The running status carries the inherited harness-home names and their remedy. [3]
- A missing CLI with a process record refuses as `paseo_cli_unavailable`; the product Node is not checked here. [4]
