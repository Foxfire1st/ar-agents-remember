# mcp/src/agents_remember/serving/paseo/paseo_settings.py

## Governing Overview

[overview](../overview.md)

## Purpose

The daemon settings provision owns and which of their changes require a host restart.

## Code Commentary

`daemon_settings` is the complete list provision writes, each marked `start` or `live`; every other key is left alone. `pending_settings` diffs the loaded configuration against it, and `restart_reasons` turns a running daemon's version, listen address or pending start-only setting into the named reasons the install reports without stopping the host.

## Evidence

- The complete setting list with its start/live split. [1]
- The restart reasons of a running daemon. [2]
