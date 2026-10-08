# mcp/tests/test_tool_entry_point_sweep.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Runs the public tool-entry probes declared by the census, using the extracted world and pin owners.

## Code Commentary

EntryPointProbeTests drives the registered entry points through the shared world and declared input pins. The classifier, census controls and phase-budget machinery are extracted owners, not declarations in this module. A probe records the tool's actual route outcome; its existence alone proves neither every environment nor every unsupported consumer. Removed local classifier helpers, pin constants and control class names must not be attributed to this file. Test definitions are not an execution result.

## Evidence

### Repo-Internal References

- `EntryPointProbeTests` owns the current boundary described above. [25]
