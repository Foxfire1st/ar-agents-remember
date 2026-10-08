# mcp/tests/test_host_release_contract.py

## Governing Overview

[overview](overview.md)

## Purpose

The release-contract cases: plugin SDK drift fails concordance, a starter renders one shared block and preserves existing settings, concordance rejects a mismatched lock entry or archive URL, the same starter input differs only in the recorded root and ports, and each public host command (and the dashboard line) states the retired-selector notice once.

## Code Commentary

The module loads `scripts/check-host-contract.py`, renders starter files through the public renderer and drives the runtime/start commands through the fake Paseo runner.

## Evidence

- The plugin pin drift case. [1]
- The rendered-block case. [2]
- The lock/archive concordance case. [3]
- The notice-once case. [4]
