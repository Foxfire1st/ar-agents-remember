# mcp/src/agents_remember/serving/paseo/paseo_settings.py

## Governing Overview

[overview](../overview.md)

## Purpose

The daemon settings provision owns and which of their changes require a host restart.

## Code Commentary

`daemon_settings` is the complete list provision writes, each marked `start` or `live`; every other key is left alone. Among the live ones `agents.idleRuntimeCleanup` is written `false`: Paseo 0.14 and later otherwise close an agent's runtime after an hour idle, and the product reads a closed seat as ended, so a seat's runtime is closed only when the seat is retired or archived. `pending_settings` diffs the loaded configuration against it, and `restart_reasons` turns a running daemon's version, listen address or pending start-only setting into the named reasons the install reports without stopping the host.

`pending_settings` reads the configuration through the CLI and hands it to `pending_settings_from_document`, which compares any configured document; the install preview uses it on the home's `config.json`, as it would read after a pending provider recovery, when the product Node or the CLI is not yet installed or such a recovery is pending.

## Evidence

- The complete setting list with its start/live split. [1]
- The restart reasons of a running daemon. [2]

- The setting comparison works on a configured document without the CLI. [3]

- The cleanup key written false in the daemon-settings tuple, with its key constant. [4]
