# mcp/src/agents_remember/serving/paseo/paseo_running_node.py

## Governing Overview

[overview](../overview.md)

## Purpose

Chooses an existing Node for talking to an already running host, so a build that names another Node than the running host still reaches it.

## Code Commentary

`communication_node` returns this build's product Node when its executable exists; otherwise the executable of the owned running supervisor, proven by the home's process record and read from its process facts, when that file exists. When neither exists it raises `node_not_installed` with the remedy `runtime_install`, then `agents-remember paseo provision` with the active `--config`. It grants no authority to start a host on an earlier Node: `PaseoCli` uses the product Node for a host start or a staged install root and this selector for every other call, and the Paseo bridge uses it for its calls.

## Evidence

- The product Node first, then the owned running host's Node, else `node_not_installed`. [1]
- The Paseo CLI selects this Node for every call that does not start a host. [2]
- The bridge runs its script on this Node. [3]
