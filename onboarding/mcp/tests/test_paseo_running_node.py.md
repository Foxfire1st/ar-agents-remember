# mcp/tests/test_paseo_running_node.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that talking to an already running owned Paseo host does not require this build's product Node to be installed: communication falls back to the running supervisor's Node, while starting a host never does.

## Code Commentary

The `old_host` fixture starts a fake host whose supervisor process facts name an `old-node` executable and removes the product Node. `communication_node` returns the product Node when it exists and otherwise the proven running Node; a missing old executable, a supervisor of another Paseo home, or no host process all refuse with `node_not_installed` instead of picking an unrelated executable. Status runs only on the old Node, and status, `observe_host` and the CLI bridge `bridge_call` (which invokes the old Node) report `restartRequired: ["node"]`, the bridge adding a remedy naming `paseo provision`, whereas `PaseoCli.call("daemon", "start"|"restart")` refuses with `node_not_installed` and signals nothing. A delivered bridge acknowledgement is returned as-is even when the follow-up host observation raises `ProcessUnreadable`. Everything runs against `paseo_runtime_test_support.FakePaseo` on test-owned roots.

## Evidence

- The product Node is preferred, otherwise the proven running Node [1]
- A missing, foreign or absent host Node refuses rather than selecting an unrelated executable [2]
- Status, dashboard observation and the bridge use the old Node; start and restart never do [3]
- A delivered acknowledgement survives an unreadable follow-up observation [4]
- The selector under test [5]
