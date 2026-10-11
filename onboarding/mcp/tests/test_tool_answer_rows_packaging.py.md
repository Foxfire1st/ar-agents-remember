# mcp/tests/test_tool_answer_rows_packaging.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derives memory packaging, integrity and coherence answer rows from hermetic service runs.

## Code Commentary

Cases cover refresh and preview, initialization/baseline, carryover plan/apply, validator listing and coherence actions. Retired drift and migration tools have projection-only cases: retained internal services do not restore their public MCP adapters. The forty-path carryover comparison checks full population both with an apply report and a no-report plan, not an extra per-tool cap. These are assertion/fidelity boundaries, not this Curator’s execution or current-pair verdict.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- Report and no-report carryover retain all forty source paths. [1]
- Refresh and stale-preview results derive the route row. [2]
- Actual validator results derive integrity answer cases. [3]
- Actual coherence actions derive bounded cases. [4]
