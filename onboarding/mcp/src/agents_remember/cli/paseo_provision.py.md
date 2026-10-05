# mcp/src/agents_remember/cli/paseo_provision.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Converges the configured install, home config, plugin and daemon while reporting exact changes.

## Code Commentary

provision_runtime stages the exact pinned version before activation, validates owned daemon record and listen address, changes start-only settings around stop/start, and acknowledges the loaded plugin stamp after successful load. A no-change pass uses read-only native calls. Preserve packet-stated rollback/activation interruption limits rather than claiming every failure leaves all prior state untouched.

## Evidence

- Frozen implementation of provision_runtime supporting the stated file behavior. [1]
- Frozen implementation of _ensure_install supporting the stated file behavior. [2]
- Frozen implementation of _converge_daemon supporting the stated file behavior. [3]
- Rejects non-exact, malformed and padded version selectors. [4]
- Checks a mismatched install is replaced and a failed staged installation preserves the preceding install and daemon. [5]
