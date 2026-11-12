# mcp/src/agents_remember/serving/paseo/paseo_command.py

## Governing Overview

[overview](../overview.md)

## Purpose

Owns the command runner for npm and the pinned Paseo management CLI.

## Code Commentary

PaseoCli addresses every command with the configured home and removes inherited PASEO variables. It does not import the agent client or identify/signals processes by port. Command results and parse failures become bounded named runtime failures, allowing tests to replace this one runner.

The runner builds every Paseo call's environment through the product's `host_environment` (the exact-name session list) and starts Node by its full path; the one npm run gets the product Node folder first on its child PATH, and `PaseoRuntimeFailure` lives in `errors.py`. A call that starts a host (`daemon start`, `daemon restart`) or runs a staged install root uses the build's product Node only. Every other call uses `communication_node`: the product Node when it is installed, otherwise the Node of the owned running host named by the home's process record, so a build change that names another Node still reaches a running host. `node_not_installed` is raised when the selected Node does not exist.

## Evidence

- The command boundary: the product environment for every call, the product Node for a host start or a staged install root, the communication Node for every other call. [1]

- The named failure type shared with the host modules. [2]

- A call that does not start a host selects its Node through the running-node selector. [3]
