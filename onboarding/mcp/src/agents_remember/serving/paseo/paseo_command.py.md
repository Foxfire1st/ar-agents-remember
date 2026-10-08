# mcp/src/agents_remember/serving/paseo/paseo_command.py

## Governing Overview

[overview](../overview.md)

## Purpose

Owns the command runner for npm and the pinned Paseo management CLI.

## Code Commentary

PaseoCli addresses every command with the configured home and removes inherited PASEO variables. It does not import the agent client or identify/signals processes by port. Command results and parse failures become bounded named runtime failures, allowing tests to replace this one runner.

L96: the module moved from `cli/paseo_command.py` into `serving/paseo/`, so both the install rank and the serving rank can reach it. The runner now builds every Paseo call's environment through the product's `host_environment` (the exact-name session list) and starts the product's Node by its full path; the one npm run gets the product Node folder first on its child PATH, and `PaseoRuntimeFailure` now lives in `errors.py`.

## Evidence

- The command boundary with the product environment and Node. [1]
- The named failure type shared with the host modules. [2]
