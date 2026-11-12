# mcp/tests/test_unused_settings_keys.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects honest settings load/report behavior for keys whose only readers were removed, without rewriting the user file.

## Code Commentary

### Logic

Tests load former retirement keys, tolerate their values without old validation, report dotted names once across MCP and orchestration settings, preserve bytes and keep supported harness/provider choices readable. A server_info case remains successful when invalid orchestration settings cannot be read, reporting only the successfully resolved unused family. Shared user-settings writes obtain the guard before mutation.

### Invariants And Boundaries

Unused keys are retained data, not active knobs. Reporting or parse failure is not authorization to edit settings. Mocked ServingBuild values and pytest settings are fixtures, not facts about a real installation.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Unused retired-settings reporting: implementation/assertion boundary described above. [1]
