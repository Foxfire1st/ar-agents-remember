# mcp/tests/test_paseo_status_bridge.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The bridge asks the native client for agent state and the last idle turn without reading unrelated timeline data. Resume opens only a closed target session and leaves every other agent alone. Controlled native-client responses supply state/event fixtures.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
